# SPDX-License-Identifier: Apache-2.0
# Non-canonical scorer for five frozen H3 contact-phase fixtures.
from argparse import ArgumentParser
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
from pathlib import Path
import subprocess

MODES = ("baseline", "ingress_active", "ingress_sham", "delayed_active", "delayed_sham")
LABELS = ("44", "4")


def tokens(line):
    return dict(token.split("=", 1) for token in line.split() if "=" in token)


def run(case):
    executable, mode, start, horizon = case
    process = subprocess.run(
        [executable, mode, start, str(horizon)], capture_output=True, check=True,
    )
    if process.stderr:
        raise RuntimeError(process.stderr.decode("ascii"))
    stdout = process.stdout.replace(b"\r\n", b"\n")
    lines = stdout.decode("ascii").splitlines()
    summary = tokens(lines[1])
    phases = [tokens(line) for line in lines if line.startswith("raw=")]
    if [phase["raw"] for phase in phases] != list(LABELS):
        raise RuntimeError("unexpected phase inventory")
    row = [mode, start, horizon, tokens(lines[0])["Q"], summary["ticks"],
           summary["first_full_return"], summary["audit_count"]]
    for phase in phases:
        row.extend(phase[name] for name in ("B1_reads", "changed_words",
                                            "work_carrier_clears", "work_radiation_clears"))
    for name in ("unscheduled_substep_changes", "hold_mismatches", "post_write_loss"):
        item = tokens(next(line for line in lines if line.startswith(name + " ")))
        row.extend([item["count"], item.get("first_tick", "-"), item.get("first_stage", "-")])
    row.append(sha256(stdout).hexdigest())
    groups = {}
    for group in ("written_class", "post_write_cuts"):
        cuts = [line.split()[2:] for line in lines if line.startswith(group + " ")]
        if len(cuts) != len(LABELS):
            raise RuntimeError("unexpected class inventory")
        groups[group] = [dict(item.split("@") for item in cut) for cut in cuts]
    return row, stdout, groups


def main():
    parser = ArgumentParser()
    parser.add_argument("executable", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--jobs", type=int, default=2)
    args = parser.parse_args()
    args.output.mkdir(parents=True, exist_ok=False)
    executable = str(args.executable.resolve())
    cases = [(executable, mode, start, bound)
             for mode in MODES
             for bound, starts in ((3110, [f"raw{rank}" for rank in range(85)]),
                                   (1_000_000, ["rawzero"] + ([f"raw{rank}" for rank in range(85)]
                                                    if mode.endswith("_active") else ["raw44", "raw4"])))
             for start in starts]
    coverage = ["mode start horizon Q ticks first_full_return audits reads44 writes44 "
                "carrier_clear44 radiation_clear44 reads4 writes4 carrier_clear4 radiation_clear4 "
                "change_count first_change_tick first_change_stage hold_count first_hold_tick "
                "first_hold_stage post_write_loss_count first_post_write_loss_tick "
                "first_post_write_loss_stage stdout_sha256"]
    inventory = {}
    with ThreadPoolExecutor(max_workers=args.jobs) as pool:
        for row, stdout, groups in pool.map(run, cases):
            mode, start, horizon = row[:3]
            (args.output / f"{mode}-{start}-{horizon}.txt").write_bytes(stdout)
            coverage.append(" ".join(map(str, row)))
            for group, classes in groups.items():
                for label, values in zip(LABELS, classes):
                    target = inventory.setdefault((mode, group, label), {})
                    for word, cut in values.items():
                        target.setdefault(word, (start, horizon, cut))
    (args.output / "coverage.txt").write_bytes(("\n".join(coverage) + "\n").encode("ascii"))
    aliases = ["mode group distinct first_word raw44_start/horizon/cut raw4_start/horizon/cut"]
    for mode in MODES:
        for group in ("written_class", "post_write_cuts"):
            left, right = (inventory[(mode, group, label)] for label in LABELS)
            overlap = left.keys() & right.keys()
            fields = [mode, group, str(len(overlap))]
            if overlap:
                word = min(overlap)
                fields.extend([word, "/".join(map(str, left[word])), "/".join(map(str, right[word]))])
            aliases.append(" ".join(fields))
    (args.output / "aliases.txt").write_bytes(("\n".join(aliases) + "\n").encode("ascii"))


if __name__ == "__main__":
    main()
