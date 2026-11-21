# SPDX-License-Identifier: Apache-2.0
"""Exact prospective census of downstream H3 reads from a restored word."""
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from functools import cache
from hashlib import sha256
from pathlib import Path
import json
import subprocess
import tempfile

import calibration
import kernel as k
import measure
import models
import stock

DEPTHS = (9, 124, 150, 156, 157, 158, 160, 162)
CLOCK = (0, 1, 4, 5, 8, 9)
BASE = stock.BASE
HERE = Path(__file__).resolve().parent
HEADER = measure.HEADER
ix = {name: i for i, name in enumerate(HEADER)}


def emit(section, value):
    print(json.dumps(dict(section=section, value=value),sort_keys=True,separators=(",",":")))


def native_baselines(inputs):
    result = {}
    ledger = k.account(inputs[0])
    for rank, field in enumerate(inputs):
        states = {0:field}
        for tick in range(1,max(DEPTHS)+1):
            field = measure.native(field,tick,ledger,("baseline",rank))[1]
            if tick in DEPTHS:
                states[tick] = field
        result[rank] = states
    return result


@cache
def word(a):
    return " ".join(map(str,k.reported(a)))


def encode(field):
    return " ".join(word(a) for cell in field for a in cell)


def uid(depth,mode):
    return 10000*depth+mode


def field_for(states, rank, num):
    depth, mode = divmod(num,10000)
    field = models.decorate(states[rank][depth],mode)
    if field is None:
        return None
    return field


def run_batch(exe, states, requests):
    records = []
    domain = set()
    for num,rank in requests:
        field = field_for(states,rank,num)
        if field is None:
            if num < 10000:
                raise AssertionError(("ineligible direct",num,rank))
            continue
        depth=num//10000
        records.append(f"{num} {rank} {depth} "+encode(field)+"\n")
        domain.add((num,rank))
    if not records:
        return {}
    proc=subprocess.run([str(exe)],input="".join(records).encode("ascii"),capture_output=True,check=True)
    if proc.stderr:
        raise AssertionError(proc.stderr)
    lines=proc.stdout.decode("ascii").splitlines()
    if lines[0].split()!=HEADER:
        raise AssertionError(("schema",lines[0],HEADER))
    result={}
    for line in lines[1:]:
        row=tuple(map(int,line.split()))
        if len(row)!=len(HEADER) or row[:2] in result:
            raise AssertionError(("invalid native row",row))
        result[row[:2]]=row
    if set(result)!=domain:
        raise AssertionError("incomplete native census")
    return result


def collect(pool,exe,states,requests):
    result={}
    jobs=[pool.submit(run_batch,exe,states,requests[i:i+480]) for i in range(0,len(requests),480)]
    for job in jobs:
        batch=job.result()
        if result.keys() & batch.keys():
            raise AssertionError("duplicate query")
        result.update(batch)
    return result


def priority(row):
    if row is None:
        return (0,)*9
    get=lambda key: bool(row[ix[key]])
    return (int(get("retained_work_tick") and get("escrow_tick")),
            int(get("work_tick") and get("escrow_tick")),int(get("retained_work_tick")),
            int(get("work_tick")),int(get("paid_work_tick")),int(get("retained_read_tick")),
            int(get("read_tick") or get("inhibit_tick")),int(get("paid_effect_tick")),
            int(get("restore157")))


def best(rows, candidates):
    return max(candidates,key=lambda num:(priority(rows.get((num,43))),-num))


def detailed(states,num,rows):
    audited=[]
    first=None
    raw43=None
    clocks=0
    seeds=set()
    projections=set()
    skipped=[]
    for rank in range(85):
        field=field_for(states,rank,num)
        if field is None:
            skipped.append(rank)
            continue
        depth=num//10000
        wanted=field
        for tick in range(depth,0,-1):
            field=k.inverse_step(field,tick%2)
        f=field
        for tick in range(1,depth+1):
            f=k.native_step(f,tick%2)[1]
        if f!=wanted:
            raise AssertionError(("python native preimage",num,rank))
        original=states[rank][0]
        exact=all(field[site][3]==original[site][3] for site in CLOCK)
        clocks+=exact
        seeds.add(sha256(encode(field).encode("ascii")).hexdigest())
        projections.add(tuple(field[site][3] for site in CLOCK))
        native_row=rows[num,rank]
        want_report=(rank==43 or (first is None and any(native_row[ix[key]] for key in
                    ("work_tick","read_tick","inhibit_tick","paid_effect_tick","paid_work_tick"))))
        py_row,report=measure.trial(field,num,rank,details=want_report)
        if tuple(py_row)!=native_row:
            raise AssertionError(("Python/C++ row",num,rank,py_row,native_row))
        audited.append(py_row)
        if want_report:
            witness=dict(rank=rank,original_clock=exact,launch_sha256=sha256(encode(field).encode()).hexdigest(),detail=report)
            if rank==43:
                raw43=witness
            if first is None and any(native_row[ix[key]] for key in ("read_tick","inhibit_tick","paid_effect_tick")):
                first=rank if rank==43 else witness
    return dict(mode=num,eligible=len(audited),ineligible=skipped,rows=audited,
                intact_clocks=clocks,distinct_launches=len(seeds),distinct_clock_projections=len(projections),
                raw43=raw43,first=first)


def summarize(num, rows):
    data=[rows[num,i] for i in range(85) if (num,i) in rows]
    counts=[sum(bool(r[i]) for r in data) for i in range(2,len(HEADER))]
    digest=sha256()
    for row in data:
        digest.update((" ".join(map(str,row))+"\n").encode("ascii"))
    return [num,len(data),digest.hexdigest(),counts,rows.get((num,43))]


def main():
    findings,digest=k.Findings(),sha256()
    bare,_,ready=k.bare_reference(findings,digest)
    if findings.counts or set(ready)!=set(range(85)):
        raise AssertionError(findings.first)
    seeds=[stock.baseline(bare[(ready[i]-1)%k.PERIOD]) for i in range(85)]
    states=native_baselines(seeds)
    emit("protocol",dict(columns=HEADER,bare_sha256=digest.hexdigest(),direct_modes=len(models.ALL),
                        depth_choices=DEPTHS,ranks=len(seeds),target_rank=43))
    with tempfile.TemporaryDirectory() as temp, ThreadPoolExecutor(max_workers=2) as pool:
        exe=Path(temp)/"relay"
        subprocess.run(["g++","-std=c++20","-O3",str(HERE/"audit.cpp"),"-o",str(exe)],check=True)
        direct=collect(pool,exe,states,[(num,r) for num in models.ALL for r in range(85)])
        screen=collect(pool,exe,states,[(uid(depth,mode),43) for depth in DEPTHS for mode in models.ALL if mode!=BASE])
        shortlist=[]
        for depth in DEPTHS:
            for family in ((500,959),(960,973),(2000,max(models.DESIGNS))):
                nums=[uid(depth,m) for m in models.ALL if family[0]<=m<=family[1] and (uid(depth,m),43) in screen]
                if nums:
                    shortlist.append(best(screen,nums))
        extension=collect(pool,exe,states,[(num,r) for num in shortlist for r in range(85)])
    if any(screen[num,43]!=extension[num,43] for num in shortlist):
        raise AssertionError("rank 43 repeat")
    rows={**direct,**extension}
    emit("screen",dict(eligible=len(screen),rows=[list(r) for _,r in sorted(screen.items())],shortlist=shortlist))
    emit("census",[summarize(num,rows) for num in (*models.ALL,*shortlist)])
    reps={BASE,best(direct,[m for m in models.ALL if 500<=m<=959]),
          best(direct,[m for m in models.ALL if 960<=m<=973]),best(direct,list(models.DESIGNS))}
    if shortlist:
        reps.add(best(extension,shortlist))
        reps.add(best(extension,[m for m in shortlist if m//10000>=157]) if
                 any(m//10000>=157 for m in shortlist) else best(extension,shortlist))
    for num in sorted(reps):
        emit("replay",detailed(states,num,rows))
    emit("intermediate_calibration",calibration.run(bare[(ready[43]-1)%k.PERIOD]))


if __name__=="__main__":
    main()
