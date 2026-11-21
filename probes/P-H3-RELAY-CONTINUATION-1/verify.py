# SPDX-License-Identifier: Apache-2.0
"""Retrospective exact verification of the rank-43 H3 continuation."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import sys
import tempfile

HERE = Path(__file__).resolve().parent
FAMILY = HERE.parent / "P-H3-THIRD-CELL-1"
PREVIOUS = HERE.parent / "P-H3-RECEIVER-OUTPUT-RELAY-1"
LOW, HIGH = 1 << 26, 1 << 30
PINS = {
    FAMILY / "launch43.json": "1a4d47ff21e95385f93fe05915aed409a38d1ebb40f3e2f0e724c6f8eb267d7f",
    FAMILY / "launches.py": "086ef90a76f929ffb0c1d9a1bf34d2d0ecb687cf13f9e2c12568d1e4a0457c93",
    FAMILY / "kernel.py": "e12b05ab92a48cd65630fd689d880e5f36dcee08771e3703a01a357bba5f9f84",
    FAMILY / "measure.py": "be1eaa262ab1b4a238828322dcb6697a4e1c6da7019d7f12a1679e046c6ce960",
    HERE.parent / "P-H3-SECOND-WRITE-1" / "audit.cpp":
        "0434d95cb7b1c376ea81259be7266db8c964977ecb46c3c9aab6d3f620d590e9",
    PREVIOUS / "EXPECTED.txt": "a9e8dc1a09797b72970064b7a558544c1a2cf4d06fbcbb8d80119c14f94d4910",
}
QUERY_DIGEST = "d7edbbf3816819a7078c7f9b85da242fcb4d85dddd7b5b0c641b33b73a65b396"
FINAL_DIGEST = "b05fee6196a0be63a6ab150a2db111114633a66a8c74dc76c8945964c1c7acfa"
SIZES = {"PREFIX": 12, "POST": 12, "READINESS": 3, "PAIRS": 3, "FIXED": 5,
         "FIXED_WORDS": 112, "FINAL": 514}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def parse(data):
    rows = {}
    for line in data.decode("ascii").splitlines():
        tag, *numbers = line.split()
        require(tag in SIZES and tag not in rows and len(numbers) == SIZES[tag],
                "unexpected, duplicated or incomplete native row: " + tag)
        rows[tag] = list(map(int, numbers))
    require(rows.keys() == SIZES.keys(), "incomplete native record inventory")
    return rows


def counts(row):
    require(min(row) >= 0, "negative population")
    result = {"end_tick": row[0], "recurrent_source_writes": row[1]}
    for i, branch in enumerate(("B1", "B2")):
        reads, hits, returns, overwrites, pending = row[2+i::2]
        require(reads == hits + returns + overwrites + pending, "unresolved branch accounting")
        result[branch] = dict(reads=reads, delivered=hits, returned_to_1=returns,
                              overwritten_at_2=overwrites, pending=pending)
    return result


def split_words(numbers):
    return [numbers[i:i+4] for i in range(0, len(numbers), 4)]


def verify_reference(k, rows):
    words = split_words(rows["FIXED_WORDS"])
    cells = [tuple(k.from_j(*w) for w in words[i:i+4]) for i in range(0, 24, 4)]
    write_c, write_b, source, read_pre, read_c, read_b = cells
    for before, after in ((write_c, write_b), (read_c, read_b)):
        require(k.scatter(before) == (after, 2) and k.scatter(after) == (before, 1),
                "five-coordinate B2 and inverse")
    require(source[:2] == write_b[:2] and all(
        k.contact(source[i], read_pre[i])[1] == read_c[i] for i in range(3)
    ) and all(read_c[i] != read_pre[i] for i in range(2)), "source delivery to site 2")
    for i in range(2):
        target_pre = k.from_j(*words[24+i])
        target_c = k.from_j(*words[26+i])
        require(k.contact(read_b[i], target_pre)[1] == target_c and target_pre != target_c,
                "five-coordinate onward transfer to site 3")
    require(rows["FIXED"] == [8176761, 36442231, 36442233, 36442234, 2], "fixed event times")
    return dict(zip(("prior", "write", "read", "delivery", "moved_rails"), rows["FIXED"]),
                readiness=words[12:16] + words[18:20], emitted=words[4:6],
                arrival=words[16:18], output=words[20:22], third_pre=words[24:26],
                third_contact=words[26:28], third_branch=0)


def emit(section, value):
    print(json.dumps({"section": section, "value": value}, separators=(",", ":"), sort_keys=True))


def main():
    for path, digest in PINS.items():
        require(sha256(path.read_bytes()).hexdigest() == digest, "source pin drift: " + path.name)
    sys.path.insert(0, str(FAMILY))
    import kernel
    import launches
    import measure

    launch = launches.four_wire(launches.bare_inputs())[43]
    query = ("2 43 0 " + launches.encode(launch) + "\n").encode("ascii")
    require(sha256(query).hexdigest() == QUERY_DIGEST, "rank-43 input drift")
    with tempfile.TemporaryDirectory() as temp:
        exe = Path(temp) / "continuation"
        subprocess.run(["g++", "-std=c++20", "-O3", str(HERE / "continuation.cpp"), "-o", str(exe)],
                       check=True)
        run = subprocess.run([str(exe)], input=query, capture_output=True, check=True)
        require(not run.stderr, "unexpected native stderr")
    rows = parse(run.stdout)
    before, after = (counts(rows[key]) for key in ("PREFIX", "POST"))
    require((before["end_tick"], after["end_tick"]) == (LOW, HIGH), "interval boundary")
    prior_sections = {row["section"]: row["value"] for row in
                      map(json.loads, (PREVIOUS / "EXPECTED.txt").read_bytes().splitlines())}
    old = prior_sections["scan"]
    require(old["ticks"] == LOW and not prior_sections["alternative"] and
            before["recurrent_source_writes"] == old["recurrent_B2_site1"], "published prefix")
    for b in ("B1", "B2"):
        require([before[b][key] for key in ("reads", "delivered", "pending")] ==
                [old[f"{key}_{b}"] for key in ("reads", "relays", "pending")], "prefix branch counts")
    fixed = verify_reference(kernel, rows)
    contacts, four, six = rows["READINESS"]
    require(contacts == (HIGH-LOW)//2 and 0 <= six <= four <= contacts, "readiness accounting")
    fixed_pairs, historical_pairs, all_pairs = rows["PAIRS"]
    require(0 <= fixed_pairs <= historical_pairs <= all_pairs, "pair-pool ordering")
    require(rows["FINAL"][:2] == [HIGH, 1], "right boundary field or matching")
    coefficients = rows["FINAL"][2:]
    vals = [kernel.from_j(*w) for w in split_words(coefficients)]
    final_field = [vals[i:i+4] for i in range(0, len(vals), 4)]
    account = kernel.reported_account(final_field)
    require(account == measure.LEDGER == kernel.reported_account(launch), "endpoint account drift")
    final_digest = sha256((" ".join(map(str, coefficients)) + "\n").encode("ascii")).hexdigest()
    observed = [after["B1"]["reads"], after["B2"]["reads"], after["B1"]["delivered"],
                after["B2"]["delivered"], after["B1"]["returned_to_1"], after["B1"]["overwritten_at_2"],
                after["B1"]["pending"], after["B2"]["pending"], four, six, *rows["PAIRS"]]
    confirmed = observed == [6940,2852,702,188,885,5353,0,0,0,0,0,0,0] and final_digest == FINAL_DIGEST
    emit("launch", dict(rank=43, ordered_family_sha256=launches.LAUNCH_DIGEST, query_sha256=QUERY_DIGEST))
    emit("prefix", before)
    emit("continuation", after)
    emit("fixed_B2", fixed)
    emit("readiness", dict(contacts=contacts, pre_four=four, full_six=six))
    emit("compatible_pairs", dict(fixed=fixed_pairs, historical=historical_pairs, full=all_pairs))
    emit("endpoint", dict(next_bit=1, account=account, field_sha256=final_digest))
    emit("retrospective_confirmation", confirmed)


if __name__ == "__main__":
    main()
