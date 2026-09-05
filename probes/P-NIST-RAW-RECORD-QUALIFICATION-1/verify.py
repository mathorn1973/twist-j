#!/usr/bin/env python3
"""Pinned, bounded NIST archive/record qualification; no Bell-window analysis.

The little-endian interpretation is a declared hypothesis, never inferred by
trying alternatives.  Source-order intervals between channel-6 rows are record
partitions, not physical trials.  In particular zero channel-0 rows means only
NO_RECORDED_DETECTOR_ROW.  Channel 64 contains calendar metadata, not a timetag.

Only main() performs I/O.  Every complete archive is checked before ZIP access;
only the declared prefix of its one named original member is interpreted.
"""

from collections import Counter
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import struct
import sys
import tempfile
from urllib import error as urlerror
from urllib import request
from urllib.parse import urlsplit
import zipfile
import zlib


MANIFEST_SHA256 = "653e5dd17b041ecf38244bcd8312fa724863eb681f940795e38974182f7bbe8a"
RECORD_LIMIT = 1_048_576
RECORD_BYTES = 24
MAX_ZIP_ENTRIES = 100
MAX_MEMBER_BYTES = 16 * 1024**3
IO_CHUNK_BYTES = 1024 * 1024
READ_RECORD_CHUNK = 8192
WITNESS_LIMIT = 8
PHYSICAL_CHANNELS = frozenset((0, 2, 4, 5, 6))
ALLOWED_CHANNELS = PHYSICAL_CHANNELS | frozenset((64,))


class FatalError(Exception):
    """Transport, custody or execution failure; never a scientific result."""


class DataViolation(Exception):
    """A structural incompatibility in authenticated scientific bytes."""


class NoRedirect(request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def canonical_json(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True,
                      separators=(",", ":"), allow_nan=False)


def hex_digest(value):
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def require(condition, reason):
    if not condition:
        raise FatalError(reason)


def load_source():
    base = Path(__file__).resolve().parent
    data = (base / "SOURCE.json").read_bytes()
    require(hex_digest(MANIFEST_SHA256), "MANIFEST_PIN_NOT_SET")
    require(hashlib.sha256(data).hexdigest() == MANIFEST_SHA256,
            "MANIFEST_HASH_MISMATCH")
    source = json.loads(data)
    require(isinstance(source, dict), "MANIFEST_NOT_OBJECT")
    objects = source.get("objects")
    require(isinstance(objects, list) and len(objects) == 4,
            "MANIFEST_REQUIRES_FOUR_OBJECTS")
    ids = set()
    station_roles = set()
    for obj in objects:
        require(isinstance(obj, dict), "INVALID_OBJECT_DESCRIPTION")
        identifier = obj.get("id")
        require(isinstance(identifier, str)
                and re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", identifier) is not None,
                "INVALID_OBJECT_ID")
        require(identifier not in ids, "DUPLICATE_OBJECT_ID")
        ids.add(identifier)
        station = obj.get("station")
        role = obj.get("role")
        require(station in ("alice", "bob") and role in ("RUN", "SYNC"),
                "INVALID_STATION_OR_ROLE")
        require((station, role) not in station_roles, "DUPLICATE_STATION_ROLE")
        station_roles.add((station, role))
        require(type(obj.get("archive_bytes")) is int and obj["archive_bytes"] > 0,
                "INVALID_ARCHIVE_SIZE")
        require(hex_digest(obj.get("sha256")), "INVALID_ARCHIVE_HASH")
        name = obj.get("member_basename")
        require(isinstance(name, str) and name.endswith(".dat") and name != ".dat"
                and "/" not in name and "\\" not in name and "\x00" not in name,
                "INVALID_MEMBER_BASENAME")
        url = obj.get("url")
        require(isinstance(url, str), "INVALID_SOURCE_URL")
        parsed = urlsplit(url)
        require(parsed.scheme == "https" and parsed.hostname in
                ("s3.amazonaws.com", "nist-belltestdata.s3.amazonaws.com")
                and parsed.username is None and parsed.password is None
                and not parsed.fragment and parsed.port in (None, 443),
                "INVALID_SOURCE_URL")
        if parsed.hostname == "s3.amazonaws.com":
            require(parsed.path.startswith("/nist-belltestdata/"),
                    "INVALID_SOURCE_BUCKET")
    notice_path = source.get("notice_path")
    require(isinstance(notice_path, str), "MISSING_NOTICE_PATH")
    notice = (base / notice_path).resolve()
    repository = base.parent.parent.resolve()
    require(notice.is_relative_to(repository), "NOTICE_OUTSIDE_REPOSITORY")
    notice_bytes = notice.read_bytes()
    require(hex_digest(source.get("notice_sha256")), "INVALID_NOTICE_HASH")
    require(hashlib.sha256(notice_bytes).hexdigest() == source["notice_sha256"],
            "NOTICE_HASH_MISMATCH")
    return source, notice_bytes


def download_archive(obj, destination):
    """Fetch exactly the pinned object; no redirection or cache substitution."""
    opener = request.build_opener(NoRedirect())
    req = request.Request(obj["url"], method="GET", headers={
        "Accept-Encoding": "identity",
        "User-Agent": "TWIST-J-P-NIST-RAW-RECORD-QUALIFICATION-1",
    })
    try:
        with opener.open(req, timeout=60) as response:
            require(response.status == 200, "HTTP_STATUS_NOT_200")
            require(response.geturl() == obj["url"], "HTTP_URL_CHANGED")
            encoding = response.headers.get("Content-Encoding", "identity")
            require(encoding.lower() == "identity", "HTTP_CONTENT_ENCODING")
            length = response.headers.get("Content-Length")
            if length is not None:
                require(length.isdecimal() and int(length) == obj["archive_bytes"],
                        "HTTP_LENGTH_MISMATCH")
            count = 0
            with destination.open("wb") as target:
                while True:
                    # The extra byte detects an overlong object without an
                    # unbounded fetch, including absent Content-Length.
                    block = response.read(min(IO_CHUNK_BYTES,
                                              obj["archive_bytes"] - count + 1))
                    if not block:
                        break
                    count += len(block)
                    require(count <= obj["archive_bytes"], "DOWNLOAD_SIZE_EXCEEDED")
                    target.write(block)
            require(count == obj["archive_bytes"], "DOWNLOAD_SIZE_MISMATCH")
    except (urlerror.URLError, TimeoutError) as exc:
        raise FatalError("NETWORK_TRANSFER_FAILED") from exc


def verify_archive_bytes(stream, obj):
    """Hash the entire open archive, then rewind the same file handle."""
    digest = hashlib.sha256()
    count = 0
    while True:
        block = stream.read(IO_CHUNK_BYTES)
        if not block:
            break
        count += len(block)
        require(count <= obj["archive_bytes"], "ARCHIVE_SIZE_EXCEEDED")
        digest.update(block)
    require(count == obj["archive_bytes"], "ARCHIVE_SIZE_MISMATCH")
    require(digest.hexdigest() == obj["sha256"], "ARCHIVE_HASH_MISMATCH")
    stream.seek(0)


def histogram_summary(counter):
    """The digest binds every integer bin, including those omitted from top8."""
    digest = hashlib.sha256()
    ordered = sorted(counter.items())
    for value, count in ordered:
        digest.update(f"{value}\t{count}\n".encode("ascii"))
    top = sorted(ordered, key=lambda item: (-item[1], item[0]))[:8]
    return {
        "count": sum(counter.values()),
        "support_size": len(counter),
        "minimum": ordered[0][0] if ordered else None,
        "maximum": ordered[-1][0] if ordered else None,
        "complete_histogram_sha256": digest.hexdigest(),
        "hash_encoding": "ASCII ascending signed integer, TAB count, LF per bin",
        "top8_by_count_then_value": [[value, count] for value, count in top],
    }


class Differences:
    def __init__(self):
        self.previous = None
        self.counts = {"negative": 0, "zero": 0, "positive": 0}
        self.witnesses = {"negative": [], "zero": [], "positive": []}

    def add(self, index, value):
        if self.previous is not None:
            old_index, old_value = self.previous
            delta = value - old_value
            category = "negative" if delta < 0 else "zero" if delta == 0 else "positive"
            self.counts[category] += 1
            if len(self.witnesses[category]) < WITNESS_LIMIT:
                self.witnesses[category].append([old_index, index])
        self.previous = (index, value)

    def report(self):
        return {"counts": self.counts, "first8_record_index_pairs": self.witnesses}


def valid_calendar(value):
    """Exactly YYYYMMDDhhmmss, Gregorian calendar, seconds 00..59; no UTC claim."""
    if not 10_000_000_000_000 <= value <= 99_999_999_999_999:
        return False
    digits = str(value)
    try:
        datetime(int(digits[:4]), int(digits[4:6]), int(digits[6:8]),
                 int(digits[8:10]), int(digits[10:12]), int(digits[12:14]))
    except ValueError:
        return False
    return True


class RecordAudit:
    """Streaming audit of the selected prefix in unchanged source order."""

    def __init__(self):
        self.rows = 0
        self.channels = Counter()
        self.unknown_first8 = []
        self.calendar_valid = 0
        self.calendar_invalid = 0
        self.calendar_invalid_first8 = []
        self.physical_rows = 0
        self.time_differences = Differences()
        self.transfer_differences = Differences()
        self.sync_count = 0
        self.previous_sync = None
        self.sync_deltas = Counter()
        self.prefix_rows = 0
        self.open_interior_rows = 0
        self.open_rng0 = 0
        self.open_rng1 = 0
        self.open_detection = 0
        self.closed_intervals = 0
        self.closed_interior_rows = 0
        self.rng_joint = Counter()
        self.rng_classes = Counter({"missing": 0, "exact0": 0, "exact1": 0,
                                    "repeated_one_setting": 0, "both": 0})
        self.onehot_failed = 0
        self.onehot_failed_first8 = []
        self.detection_census = Counter()

    def add(self, channel, word2, transfer):
        index = self.rows
        self.rows += 1
        self.channels[channel] += 1
        self.transfer_differences.add(index, transfer)
        if channel in PHYSICAL_CHANNELS:
            self.physical_rows += 1
            self.time_differences.add(index, word2)
        elif channel == 64:
            if valid_calendar(word2):
                self.calendar_valid += 1
            else:
                self.calendar_invalid += 1
                if len(self.calendar_invalid_first8) < WITNESS_LIMIT:
                    self.calendar_invalid_first8.append(index)
        elif len(self.unknown_first8) < WITNESS_LIMIT:
            self.unknown_first8.append(index)

        if channel == 6:
            self.sync_count += 1
            if self.previous_sync is not None:
                left_index, left_time = self.previous_sync
                self.sync_deltas[word2 - left_time] += 1
                self.closed_intervals += 1
                self.closed_interior_rows += self.open_interior_rows
                pair = (self.open_rng0, self.open_rng1)
                self.rng_joint[pair] += 1
                if pair == (0, 0):
                    category = "missing"
                elif pair == (1, 0):
                    category = "exact0"
                elif pair == (0, 1):
                    category = "exact1"
                elif pair[0] > 0 and pair[1] > 0:
                    category = "both"
                else:
                    category = "repeated_one_setting"
                self.rng_classes[category] += 1
                if pair not in ((1, 0), (0, 1)):
                    self.onehot_failed += 1
                    if len(self.onehot_failed_first8) < WITNESS_LIMIT:
                        self.onehot_failed_first8.append({
                            "left_sync_record_index": left_index,
                            "right_sync_record_index": index,
                            "rng0_rows": pair[0], "rng1_rows": pair[1],
                        })
                self.detection_census[self.open_detection] += 1
            self.previous_sync = (index, word2)
            self.open_interior_rows = 0
            self.open_rng0 = 0
            self.open_rng1 = 0
            self.open_detection = 0
        elif self.previous_sync is None:
            self.prefix_rows += 1
        else:
            self.open_interior_rows += 1
            self.open_rng0 += channel == 2
            self.open_rng1 += channel == 4
            self.open_detection += channel == 0

    def finish(self):
        suffix_rows = self.open_interior_rows if self.previous_sync is not None else 0
        accounted_rows = (self.prefix_rows + self.sync_count
                          + self.closed_interior_rows + suffix_rows)
        unknown = sum(count for channel, count in self.channels.items()
                      if channel not in ALLOWED_CHANNELS)
        checks = {
            "all_rows_partitioned": accounted_rows == self.rows,
            "channel_counts_sum": sum(self.channels.values()) == self.rows,
            "interval_count": self.closed_intervals == max(0, self.sync_count - 1),
            "rng_census_count": sum(self.rng_joint.values()) == self.closed_intervals,
            "rng_class_count": sum(self.rng_classes.values()) == self.closed_intervals,
            "detection_census_count": sum(self.detection_census.values()) == self.closed_intervals,
            "sync_delta_count": sum(self.sync_deltas.values()) == self.closed_intervals,
            "transfer_comparison_count": sum(self.transfer_differences.counts.values())
                == max(0, self.rows - 1),
            "physical_comparison_count": sum(self.time_differences.counts.values())
                == max(0, self.physical_rows - 1),
            "calendar_count": self.calendar_valid + self.calendar_invalid
                == self.channels[64],
        }
        # These are implementation invariants, not empirical falsifiers.
        require(all(checks.values()), "INTERNAL_BOOKKEEPING_FAILURE")
        return {
            "rows": self.rows,
            "channel_counts": [[channel, count]
                               for channel, count in sorted(self.channels.items())
                               if channel in ALLOWED_CHANNELS],
            "all_channel_histogram": histogram_summary(self.channels),
            "recognized_physical_rows": self.physical_rows,
            "unknown_channel_rows": unknown,
            "unknown_channel_first8_record_indices": self.unknown_first8,
            "calendar_metadata_64": {
                "rows": self.calendar_valid + self.calendar_invalid,
                "valid_YYYYMMDDhhmmss": self.calendar_valid,
                "invalid": self.calendar_invalid,
                "invalid_first8_record_indices": self.calendar_invalid_first8,
                "second_word_is_not_timetag": True,
                "timezone_or_clock_calibration_claim": False,
            },
            "physical_timetag_differences_in_source_order": self.time_differences.report(),
            "transfer_counter_differences_all_rows": self.transfer_differences.report(),
            "sync": {
                "rows": self.sync_count,
                "signed_delta_ticks": histogram_summary(self.sync_deltas),
                "closed_source_order_intervals": self.closed_intervals,
                "prefix_rows_before_first_sync": self.prefix_rows,
                "suffix_rows_after_last_sync": suffix_rows,
                "all_rows_unanchored_if_no_sync": self.sync_count == 0,
                "closed_interior_rows": self.closed_interior_rows,
                "rng_joint_census": [[n0, n1, count]
                                     for (n0, n1), count in sorted(self.rng_joint.items())],
                "rng_class_counts": dict(sorted(self.rng_classes.items())),
                "onehot_failed_intervals": self.onehot_failed,
                "onehot_failed_first8": self.onehot_failed_first8,
                "raw_detection_rows_per_interval_census": [
                    [number, count] for number, count in sorted(self.detection_census.items())],
                "NO_RECORDED_DETECTOR_ROW_intervals": self.detection_census[0],
                "physical_trial_or_no_detection_certificate": False,
            },
            "bookkeeping": checks,
        }


def member_descriptor(index, info):
    name_bytes = info.filename.encode("utf-8", errors="surrogatepass")
    return {
        "index": index,
        "name_excerpt": info.filename[:200],
        "name_truncated": len(info.filename) > 200,
        "name_utf8_sha256": hashlib.sha256(name_bytes).hexdigest(),
        "uncompressed_bytes": info.file_size,
        "compressed_bytes": info.compress_size,
        "header_crc32_hex": f"{info.CRC:08x}",
        "compression_method": info.compress_type,
        "flags": info.flag_bits,
        "is_directory": info.is_dir(),
        "contents_extracted": False,
    }


def inspect_zip(stream, obj, report):
    with zipfile.ZipFile(stream, mode="r") as archive:
        infos = archive.infolist()
        report["zip_entry_count"] = len(infos)
        if len(infos) > MAX_ZIP_ENTRIES:
            raise DataViolation("ZIP_ENTRY_LIMIT_EXCEEDED")
        descriptors = [member_descriptor(index, info) for index, info in enumerate(infos)]
        report["zip_member_descriptors"] = descriptors
        report["zip_descriptor_sha256"] = hashlib.sha256(
            canonical_json(descriptors).encode("ascii")).hexdigest()
        matches = [info for info in infos
                   if PurePosixPath(info.filename).name == obj["member_basename"]]
        if len(matches) != 1:
            raise DataViolation("EXPECTED_MEMBER_NOT_UNIQUE")
        info = matches[0]
        if info.is_dir():
            raise DataViolation("EXPECTED_MEMBER_IS_DIRECTORY")
        if info.flag_bits & 1:
            raise DataViolation("EXPECTED_MEMBER_IS_ENCRYPTED")
        if info.compress_type not in (zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED):
            raise DataViolation("UNSUPPORTED_ZIP_COMPRESSION")
        if info.file_size > MAX_MEMBER_BYTES:
            raise DataViolation("MEMBER_SIZE_LIMIT_EXCEEDED")
        if info.file_size % RECORD_BYTES:
            raise DataViolation("MEMBER_SIZE_NOT_MULTIPLE_OF_24")
        total_rows = info.file_size // RECORD_BYTES
        selected_rows = min(RECORD_LIMIT, total_rows)
        complete = selected_rows == total_rows
        report["selected_member"] = {
            "name": info.filename,
            "total_uncompressed_bytes_declared_by_zip": info.file_size,
            "total_records_declared_by_zip": total_rows,
            "selected_records": selected_rows,
            "selected_record_bytes": selected_rows * RECORD_BYTES,
            "scope": "FULL_MEMBER" if complete else "PREFIX_ONLY",
            "whole_archive_sha256_verified": True,
            "unread_tail_crc_required": False,
            "full_member_crc_verified": False,
        }
        audit = RecordAudit()
        with archive.open(info, mode="r") as member:
            remaining_rows = selected_rows
            while remaining_rows:
                rows = min(READ_RECORD_CHUNK, remaining_rows)
                block = member.read(rows * RECORD_BYTES)
                if len(block) != rows * RECORD_BYTES:
                    raise DataViolation("SELECTED_MEMBER_PREFIX_TRUNCATED")
                for channel, word2, transfer in struct.iter_unpack("<QQQ", block):
                    audit.add(channel, word2, transfer)
                remaining_rows -= rows
            if complete:
                # Force end-of-member handling, including ZIP CRC checking.
                if member.read(1):
                    raise DataViolation("MEMBER_EXCEEDS_DECLARED_SIZE")
                report["selected_member"]["full_member_crc_verified"] = True
        records = audit.finish()
        require(records["rows"] == selected_rows, "INTERNAL_SELECTED_ROW_COUNT")
        report["records"] = records
        if records["unknown_channel_rows"]:
            report["qualification_violations"].append("UNKNOWN_CHANNEL_CODE")
        if records["calendar_metadata_64"]["invalid"]:
            report["qualification_violations"].append("INVALID_CALENDAR_METADATA_64")


def process_archive(path, obj):
    report = {
        "id": obj["id"], "station": obj["station"], "role": obj["role"],
        "archive_bytes": obj["archive_bytes"], "archive_sha256": obj["sha256"],
        "whole_archive_verified_before_zip_access": False,
        "qualification_violations": [],
        "B_onehot": "NOT_APPLICABLE" if obj["role"] == "SYNC" else "NOT_EVALUATED",
    }
    with path.open("rb") as stream:
        verify_archive_bytes(stream, obj)
        report["whole_archive_verified_before_zip_access"] = True
        try:
            inspect_zip(stream, obj, report)
        except DataViolation as exc:
            report["qualification_violations"].append(str(exc))
        except (zipfile.BadZipFile, zipfile.LargeZipFile, zlib.error,
                EOFError, UnicodeDecodeError):
            report["qualification_violations"].append("CORRUPT_ZIP_STRUCTURE_OR_CONTENT")
        except NotImplementedError:
            report["qualification_violations"].append("UNSUPPORTED_ZIP_COMPRESSION")
    report["A_qualification"] = ("QUALIFICATION_FAILED" if report["qualification_violations"]
                                  else "QUALIFIED")
    if obj["role"] == "RUN" and "records" in report:
        sync = report["records"]["sync"]
        onehot = (sync["closed_source_order_intervals"] > 0
                  and sync["onehot_failed_intervals"] == 0)
        report["B_onehot"] = "ONEHOT" if onehot else "NOT_ONEHOT"
    return report


def main():
    require(len(sys.argv) == 1, "ARGUMENTS_NOT_ACCEPTED")
    source, notice_bytes = load_source()
    cache_hint = os.environ.get("TWISTJ_NIST_CACHE_DIR")
    cache = Path(cache_hint) if cache_hint else None
    reports = []
    with tempfile.TemporaryDirectory(prefix="twistj-nist-raw-") as directory:
        temp = Path(directory)
        # Retain the complete pinned reuse notice beside temporary acquisitions.
        # A cache hint changes acquisition only, never the identity check/output.
        (temp / "NOTICE.md").write_bytes(notice_bytes)
        for obj in source["objects"]:
            cached = cache / (obj["id"] + ".zip") if cache is not None else None
            if cached is not None and cached.exists():
                path = cached
            else:
                path = temp / (obj["id"] + ".zip")
                download_archive(obj, path)
            reports.append(process_archive(path, obj))
    a_pass = all(report["A_qualification"] == "QUALIFIED" for report in reports)
    run_results = [report["B_onehot"] for report in reports if report["role"] == "RUN"]
    if "NOT_EVALUATED" in run_results:
        b_result = "NOT_EVALUATED"
    else:
        b_result = "ONEHOT" if all(value == "ONEHOT" for value in run_results) else "NOT_ONEHOT"
    output = {
        "schema": "nist-raw-record-qualification/1",
        "manifest_sha256": MANIFEST_SHA256,
        "notice_sha256": source["notice_sha256"],
        "selected_record_cap_per_object": RECORD_LIMIT,
        "declared_record_layout": "<QQQ",
        "endianness_is_declared_not_identified": True,
        "metadata_channel_64_second_word_is_not_timetag": True,
        "record_indices_are_zero_based": True,
        "scope": "Authenticated archive prefixes; source-order record partition only",
        "physical_trial_window_calibration_bell_or_born_claim": False,
        "A_qualification": "QUALIFIED" if a_pass else "QUALIFICATION_FAILED",
        "B_run_record_onehot": b_result,
        "objects": reports,
    }
    print(json.dumps(output, sort_keys=True, indent=2, ensure_ascii=True, allow_nan=False))


if __name__ == "__main__":
    try:
        main()
    except FatalError as exc:
        sys.stderr.write("VERIFIER_ERROR " + str(exc) + "\n")
        sys.exit(2)
    except OSError:
        sys.stderr.write("VERIFIER_ERROR ENVIRONMENT_IO_FAILED\n")
        sys.exit(2)
    except Exception as exc:
        # No local path, server message, token, timing or platform detail leaks
        # into deterministic scientific stdout or the fixed error category.
        sys.stderr.write("VERIFIER_ERROR INTERNAL_" + type(exc).__name__ + "\n")
        sys.exit(2)
