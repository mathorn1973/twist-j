# SPDX-License-Identifier: Apache-2.0
"""Compile and run the finite C++ census, then independently replay selected modes."""
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from functools import cache
from hashlib import sha256
from pathlib import Path
import csv
import io
import json
import subprocess
import tempfile

import bank
import kernel as k
import measure
from crosscheck import index_rows, summarize
from fixture import stock


HERE = Path(__file__).resolve().parent
CLOCK = (0, 1, 4, 5, 8, 9)


def emit(section, value):
    print(json.dumps({"section": section, "value": value}, sort_keys=True, separators=(",", ":")))


@cache
def word_text(word):
    return " ".join(map(str, k.reported(word)))


def census_chunk(exe, modes, inputs):
    stream = io.StringIO()
    provenance = {}
    for mode in modes:
        notes, hashes, clock_same, ready_clock = [], [], [], []
        for rank, bare in inputs:
            original = stock(bare)
            field, receipt = bank.prepare_info(bare, rank, mode)
            if mode and field[31][0] == field[31][1]:
                raise AssertionError(("empty launch gap", mode, rank))
            if k.account(field) != k.account(original):
                raise AssertionError(("launch account", mode, rank))
            line = " ".join(word_text(z) for cell in field for z in cell)
            stream.write(f"{mode} {rank} {line}\n")
            notes.append(receipt)
            hashes.append(sha256((line+"\n").encode("ascii")).hexdigest())
            clock_same.append(all(field[i][3] == original[i][3] for i in CLOCK))
            ready_clock.append(tuple(field[i][3] for i in CLOCK))
        provenance[mode] = dict(
            input_sha256=hashes, distinct_launches=len(set(hashes)), receipts=notes,
            intact_clock=clock_same, distinct_clock_projections=len(set(ready_clock)))
    result = subprocess.run([str(exe)], input=stream.getvalue().encode("ascii"),
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    if result.stderr:
        raise AssertionError(result.stderr)
    reader = csv.reader(io.StringIO(result.stdout.decode("ascii")), delimiter="\t")
    if next(reader) != measure.HEADER:
        raise AssertionError("C++ event header")
    rows = index_rows((list(map(int,row)) for row in reader), "native")
    by_mode = {m: [] for m in modes}
    for (m,r,t), row in rows.items():
        by_mode[m].append(row)
    summaries = {s["mode"]:s for s in summarize(rows,set(modes))}
    reports = []
    for mode in modes:
        event_rows = sorted(by_mode[mode])
        h = sha256()
        for row in event_rows:
            h.update((" ".join(map(str,row))+"\n").encode("ascii"))
        protected = provenance[mode]["intact_clock"]
        first_held = [r for r in event_rows if r[14]]
        reports.append(dict(mode=mode, events=len(event_rows), row_sha256=h.hexdigest(),
                            strict_west=[r for r in first_held if r[3]==-1 and r[14]==r[7]],
                            protected_west=[r for r in first_held if r[3]==-1 and protected[r[1]]],
                            first_work=next((r for r in event_rows if r[8]),None),
                            first_held=next(iter(first_held),None),
                            counts=summaries[mode], provenance=provenance[mode]))
    return reports, by_mode


def selection(summaries, lo, hi):
    # Equal scores resolve toward the smallest published recipe ID.
    def key(s):
        c=s["counts"]
        return (sum(s["provenance"]["intact_clock"][r[1]] for r in s["strict_west"]),
                len(s["strict_west"]), len(s["protected_west"]), c["west_held"]["ranks"],
                c["held"]["ranks"], c["west_work"]["ranks"], c["work"]["ranks"],
                c["first_isolated"]["ranks"], -s["mode"])
    return max((s for s in summaries if lo<=s["mode"]<=hi), key=key)["mode"]


def main():
    problems, digest = k.Findings(), sha256()
    cuts, _, arrivals = k.bare_reference(problems, digest)
    if problems.counts or len(arrivals)!=85:
        raise AssertionError(problems.first)
    inputs = [(r,cuts[(arrivals[r]-1)%k.PERIOD]) for r in sorted(arrivals)]
    emit("reference", dict(ranks=len(inputs), bare_sha256=digest.hexdigest(), modes=len(bank.ALL)))
    summaries, indexed = [], {}
    with tempfile.TemporaryDirectory() as tmp:
        exe=Path(tmp)/"funded_audit"
        subprocess.run(["g++","-std=c++20","-O3",str(HERE/"audit.cpp"),"-o",str(exe)],check=True)
        groups=[bank.ALL[i:i+8] for i in range(0,len(bank.ALL),8)]
        with ThreadPoolExecutor(max_workers=2) as pool:
            tasks=[pool.submit(census_chunk,exe,group,inputs) for group in groups]
            for task in tasks:
                reports, rows=task.result()
                summaries.extend(reports)
                indexed.update(rows)
    selected = sorted({0,400,*(selection(summaries,lo,hi) for lo,hi in
                                ((1,247),(300,363),(400,407),(408,415)))})
    emit("selection", selected)
    for summary in summaries:
        prov=summary["provenance"]
        prov["launch_list_sha256"]=sha256("".join(prov["input_sha256"]).encode("ascii")).hexdigest()
        if summary["mode"] not in selected:
            del prov["input_sha256"]
        if summary["mode"]<400 and summary["mode"] not in selected:
            prov["receipt_classes"]=dict(Counter(str(r) for r in prov.pop("receipts")))
            prov["intact_clock_ranks"]=sum(prov.pop("intact_clock"))
        emit("survey",summary)
    for mode in selected:
        report,=measure.run(cuts,arrivals,[(mode,mode)],bank.prepare)
        if list(map(tuple,report["rows"]))!=sorted(indexed[mode]):
            raise AssertionError(("independent event projection",mode))
        # Preserve a full certificate for a held original westward launch when available.
        for r in report["rows"]:
            if r[3]==-1 and r[14] and r[14]==r[7]:
                rank=r[1]
                # Recreate the one rank with a callback for the exact qualifying event.
                report["strict_west_witness"]=measure.event_witness(
                    inputs[rank][1],rank,mode,bank.prepare,r[2],r[14])
                break
        emit("mode", report)


if __name__ == "__main__":
    main()
