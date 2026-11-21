# SPDX-License-Identifier: Apache-2.0
"""Summarize every native cycle run, in a fixed order."""

from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
from pathlib import Path
import subprocess
import sys


def fields(line):
    return dict(token.split("=", 1) for token in line.split() if "=" in token)


def run(case):
    executable, fixture, seed, horizon = case
    result = subprocess.run([executable, fixture, seed, str(horizon)],
                            capture_output=True, check=True)
    if result.stderr:
        raise RuntimeError(result.stderr.decode())
    data = result.stdout.replace(b"\r\n", b"\n")
    lines = data.decode("ascii").splitlines()
    summary = fields(lines[1])
    phases = [fields(line) for line in lines if line.startswith("raw=")]
    if [phase["raw"] for phase in phases] != ["44", "4"]:
        raise ValueError("missing phase record")
    def measured(prefix, key):
        return fields(next(line for line in lines if line.startswith(prefix + " ")))[key]
    row = [fixture, seed, horizon, summary["ticks"], summary["first_full_return"]]
    for phase in phases:
        row.extend(phase[key] for key in ("B1_reads", "changed_words",
                                          "nominal_mismatched_predecessors",
                                          "nominal_predecessors_without_B1"))
    row.extend([measured("written_class_intersection", "distinct"),
                measured("unscheduled_substep_changes", "count"),
                measured("hold_mismatches", "count"),
                sha256(data).hexdigest()])
    return row


def main():
    executable = str(Path(sys.argv[1]).resolve())
    cases = [(executable, fixture, seed, bound)
             for fixture in ("no_bridge", "bridge", "supported", "material_support")
             for bound, seeds in ((3110, [f"raw{i}" for i in range(85)]),
                                  (1000000, ["rawzero", "raw44", "raw4"]))
             for seed in seeds]
    print("fixture seed horizon ticks first_return reads44 writes44 missed_projection44 "
          "missed_B1_44 reads4 writes4 missed_projection4 missed_B1_4 "
          "write_overlap unscheduled_changes hold_mismatches stdout_sha256")
    with ThreadPoolExecutor(max_workers=4) as pool:
        for row in pool.map(run, cases):
            print(*row)


if __name__ == "__main__":
    main()
