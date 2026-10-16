#!/usr/bin/env python3
"""Independent #748 state reader for P-PHOTON-AXIS-POS-PRIMAL-1 (Python + numpy).

This program shares no reduction code with the engine or with axis_core.  For
every saved TWISTJ_Z5_LINK_STATE_V1 file it

* checks the seven-line format, chain, sample and MACROCYCLE = T + m (s + 1);
* rebuilds every oriented plaquette flux from the link digits with numpy;
* recomputes the five flux counts and both TWISTJ_FNVLIKE64_V1 fingerprints;
* recomputes all 24 slice-sum series S_{I,r}(t) in Z[phi];

and requires exact equality with the engine transcript (SAMPLE and AXIS_S),
then recomputes the autocorrelations and contrasts from its own S and requires
exact equality with the committed AXIS_Q and AXIS_RTOT records.  Any
difference is a mismatch; READER_STATUS PASS requires none.

Output: READER.txt and STATE_MANIFEST.tsv in the output directory.
"""

from __future__ import annotations

import argparse
import hashlib
from multiprocessing import Pool
from pathlib import Path
import sys

import numpy as np

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import axis_core as core  # noqa: E402  (configuration constants only)

PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
ORIENTED = (("01", 0, 1), ("02", 0, 2), ("03", 0, 3), ("23", 2, 3), ("31", 3, 1), ("12", 1, 2))
G_U = np.array([0, 1, 1, -1, -1], dtype=np.int64)
G_V = np.array([0, 0, 2, -2, 0], dtype=np.int64)
FNV_OFFSET = 1469598103934665603
FNV_PRIME = 1099511628211
MASK = (1 << 64) - 1


def fnv(data: bytes, h: int = FNV_OFFSET) -> int:
    for value in data:
        h = ((h ^ value) * FNV_PRIME) & MASK
    return h


def plaquette(A: np.ndarray, a: int, b: int) -> np.ndarray:
    return (A[..., a] + np.roll(A[..., b], -1, axis=a) - np.roll(A[..., a], -1, axis=b) - A[..., b]) % 5


def read_one(task: tuple[str, int, str, int, int]) -> dict:
    path, L, chain, sample, macrocycle = task
    raw = Path(path).read_bytes()
    result = {"sample": sample, "sha256": hashlib.sha256(raw).hexdigest(), "bytes": len(raw), "errors": []}
    parts = raw.split(b"\n")
    expected_head = [b"TWISTJ_Z5_LINK_STATE_V1", f"L={L}".encode(), f"CHAIN={chain}".encode(),
                     f"SAMPLE={sample}".encode(), f"MACROCYCLE={macrocycle}".encode()]
    if len(parts) != 8 or parts[:5] != expected_head or parts[6] != b"END" or parts[7] != b"" \
            or not parts[5].startswith(b"LINKS="):
        result["errors"].append("state_format")
        return result
    digits = np.frombuffer(parts[5][6:], dtype=np.uint8)
    if digits.size != 4 * L**4 or digits.min() < 48 or digits.max() > 52:
        result["errors"].append("state_links")
        return result
    links = (digits - 48).astype(np.uint8)
    A = links.reshape(L, L, L, L, 4).astype(np.int64)
    flux = np.stack([plaquette(A, a, b) for a, b in PAIRS], axis=-1).astype(np.uint8)
    result["counts"] = [int(c) for c in np.bincount(flux.ravel(), minlength=5)]
    flux_bytes = flux.ravel().tobytes()
    result["cache_hash"] = f"{fnv(flux_bytes):016x}"
    result["state_hash"] = f"{fnv(flux_bytes, fnv(links.tobytes())):016x}"
    S = np.zeros((6, 4, L, 2), dtype=np.int64)
    for i, (_, a, b) in enumerate(ORIENTED):
        f = plaquette(A, a, b)
        gu, gv = G_U[f], G_V[f]
        for r in range(4):
            axes = tuple(ax for ax in range(4) if ax != r)
            S[i, r, :, 0] = gu.sum(axis=axes)
            S[i, r, :, 1] = gv.sum(axis=axes)
    result["S"] = S
    return result


def autocorrelations(S: np.ndarray, L: int) -> np.ndarray:
    K = L // 2 + 1
    R = np.zeros((6, 4, K, 2), dtype=np.int64)
    u, v = S[..., 0], S[..., 1]
    for k in range(K):
        uk, vk = np.roll(u, -k, axis=2), np.roll(v, -k, axis=2)
        R[:, :, k, 0] = (u * uk + v * vk).sum(axis=2)
        R[:, :, k, 1] = (u * vk + v * uk + v * vk).sum(axis=2)
    return R


SIGN = np.array([[1 if str(r) in name else -1 for r in range(4)] for name, _, _ in ORIENTED], dtype=np.int64)


def split_fields(line: str) -> dict[str, str]:
    return dict(token.split("=", 1) for token in line.split(" ")[1:])


def pairs(text: str) -> list[tuple[int, int]]:
    return [tuple(int(z) for z in cell.split(",")) for cell in text.split(";")]  # type: ignore[misc]


def parse_transcript(path: Path, L: int, samples: int):
    lines = path.read_bytes().decode("ascii").split("\n")[:-1]
    cut = next(i for i, line in enumerate(lines) if line.startswith("MEASURE_BEGIN "))
    accepted = int(lines[cut].split("=", 1)[1])
    rows, S = [], []
    cursor = cut + 1
    for s in range(samples):
        fields = split_fields(lines[cursor])
        if not lines[cursor].startswith("SAMPLE ") or fields["index"] != str(s):
            raise ValueError("transcript sample order")
        rows.append(fields)
        cursor += 1
        block = np.zeros((6, 4, L, 2), dtype=np.int64)
        for i, (name, _, _) in enumerate(ORIENTED):
            for r in range(4):
                fields = split_fields(lines[cursor])
                if not lines[cursor].startswith("AXIS_S ") or (fields["index"], fields["I"], fields["r"]) != (
                        str(s), name, str(r)):
                    raise ValueError("transcript AXIS_S order")
                block[i, r] = np.array(pairs(fields["S"]), dtype=np.int64)
                cursor += 1
        S.append(block)
    return accepted, rows, S


def parse_measure(path: Path, L: int, samples: int):
    lines = path.read_bytes().decode("ascii").split("\n")[:-1]
    Q = np.zeros((samples, 4, L // 2 + 1, 2), dtype=np.int64)
    rtot = np.zeros((6, 4, L // 2 + 1, 2), dtype=object)
    names = [name for name, _, _ in ORIENTED]
    for line in lines:
        if line.startswith("AXIS_Q "):
            f = split_fields(line)
            Q[int(f["index"]), int(f["r"])] = np.array(pairs(f["Q"]), dtype=np.int64)
        elif line.startswith("AXIS_RTOT "):
            f = split_fields(line)
            rtot[names.index(f["I"]), int(f["r"])] = np.array(pairs(f["R"]), dtype=object)
    return Q, rtot


def read_chains_tsv(path: Path) -> list[dict[str, str]]:
    lines = path.read_text(encoding="ascii").splitlines()
    header = lines[0].split("\t")
    return [dict(zip(header, line.split("\t"))) for line in lines[1:]]


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", required=True, choices=sorted(core.CONFIGS))
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--attempt-root", required=True, type=Path)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args(argv)
    cfg = core.CONFIGS[args.config]
    out_lines = [f"READER {core.PROBE_ID} {cfg.name} V1 numpy={np.__version__}"]
    manifest = ["chain\tsample\tmacrocycle\tbytes\tsha256"]
    failures = 0
    rows = {row["chain"]: row for row in read_chains_tsv(args.out / "CHAINS.tsv")}
    with Pool(args.workers) as pool:
        for name, L, start, replica in cfg.chains():
            row = rows[name]
            transcript = args.attempt_root / "transcripts" / f"{name}.txt"
            thermal_record = (args.out / "records" / f"{name}.thermal.txt").read_bytes()
            if row["thermal_endpoint"] == "0" or row["measure_record_sha256"] == "-":
                same = transcript.read_bytes() == thermal_record
                failures += 0 if same else 1
                out_lines.append(f"READER_CHAIN chain={name} states=0 status=NOT_MEASURED "
                                 f"thermal_record_is_transcript={'YES' if same else 'NO'}")
                continue
            mismatches = 0
            notes: list[str] = []
            try:
                data = transcript.read_bytes()
                if hashlib.sha256(data).hexdigest() != row["transcript_sha256"] or str(len(data)) != row[
                        "transcript_bytes"]:
                    raise ValueError("transcript hash differs from CHAINS.tsv")
                cut = data.index(b"\nMEASURE_BEGIN ")
                if data[:data.index(b"\n", cut + 1) + 1] != thermal_record:
                    raise ValueError("thermal record is not the transcript prefix through MEASURE_BEGIN")
                measure_path = args.out / "records" / f"{name}.measure.txt"
                measure_bytes = measure_path.read_bytes()
                measure_sha = hashlib.sha256(measure_bytes).hexdigest()
                if measure_sha != row["measure_record_sha256"]:
                    raise ValueError("measure record hash differs from CHAINS.tsv")
                measure_lines = measure_bytes.decode("ascii").split("\n")[:-1]
                transcript_lines = data[data.index(b"\n", cut + 1) + 1:].decode("ascii").split("\n")[:-1]
                header = split_fields(measure_lines[0])
                if (header.get("transcript_sha256"), header.get("transcript_bytes")) != (
                        row["transcript_sha256"], row["transcript_bytes"]):
                    raise ValueError("measure record header does not bind the transcript")
                if [x for x in measure_lines if x.startswith("SAMPLE ")] != [
                        x for x in transcript_lines if x.startswith("SAMPLE ")]:
                    raise ValueError("measure record SAMPLE lines differ from the transcript")
                if measure_lines[-3:] != transcript_lines[-3:]:
                    raise ValueError("measure record diagnostics or footer differ from the transcript")
                accepted, trows, tS = parse_transcript(transcript, L, cfg.samples)
                Q, rtot = parse_measure(measure_path, L, cfg.samples)
                m = cfg.spacing_for(L)
                state_dir = args.attempt_root / "states" / name
                expected_files = {f"s{s:06d}.state" for s in range(cfg.samples)}
                if {p.name for p in state_dir.iterdir()} != expected_files:
                    raise ValueError("state directory inventory")
                tasks = [(str(state_dir / f"s{s:06d}.state"), L, name, s, accepted + m * (s + 1))
                         for s in range(cfg.samples)]
                acc = np.zeros((6, 4, L // 2 + 1, 2), dtype=object)
                for res in pool.imap(read_one, tasks, chunksize=4):
                    s = res["sample"]
                    manifest.append(f"{name}\t{s}\t{accepted + m * (s + 1)}\t{res['bytes']}\t{res['sha256']}")
                    bad = list(res["errors"])
                    if not bad:
                        t = trows[s]
                        if res["counts"] != [int(t[f"flux_count_{v}"]) for v in range(5)]:
                            bad.append("flux_counts")
                        if res["state_hash"] != t["state_hash"] or res["cache_hash"] != t["cache_hash"]:
                            bad.append("fingerprints")
                        if not np.array_equal(res["S"], tS[s]):
                            bad.append("slice_sums")
                        R = autocorrelations(res["S"], L)
                        q = np.einsum("ir,irkc->rkc", SIGN, R)
                        if not np.array_equal(q, Q[s]):
                            bad.append("contrast")
                        acc += R.astype(object)
                    if bad:
                        mismatches += 1
                        if len(notes) < 5:
                            notes.append(f"s{s}:" + "+".join(bad))
                if not np.array_equal(acc, rtot):
                    mismatches += 1
                    notes.append("rtot")
            except (OSError, ValueError, KeyError, IndexError, StopIteration) as error:
                mismatches += 1
                notes.append(str(error).replace(" ", "_") or error.__class__.__name__)
                data = b""
                measure_sha = row.get("measure_record_sha256", "-")
            failures += mismatches
            out_lines.append(
                f"READER_CHAIN chain={name} states={cfg.samples} transcript_sha256={row['transcript_sha256']} "
                f"measure_record_sha256={measure_sha} mismatches={mismatches}"
                + (" notes=" + ",".join(notes) if notes else ""))
    manifest_bytes = ("\n".join(manifest) + "\n").encode("ascii")
    (args.out / "STATE_MANIFEST.tsv").write_bytes(manifest_bytes)
    out_lines.append(f"READER_MANIFEST sha256={hashlib.sha256(manifest_bytes).hexdigest()} "
                     f"rows={len(manifest) - 1}")
    out_lines.append("READER_STATUS " + ("PASS" if failures == 0 else "FAIL"))
    (args.out / "READER.txt").write_bytes(("\n".join(out_lines) + "\n").encode("ascii"))
    print(out_lines[-1])
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
