# SPDX-License-Identifier: Apache-2.0
"""Confirm the restored-word relay directly from a literal H3 field."""
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import tempfile

import kernel as k
import measure

HERE = Path(__file__).resolve().parent
CLOCK = (0, 1, 4, 5, 8, 9)
# For the four-wire preparation each target CLK equals one bare input CLK
# plus its fixed bias, in the (1,j,jÂ˛,jÂł) basis.
WIRES = (
    (0, 7, (-2, 0, -1, 0)),
    (1, 28, (-3, 0, -1, 0)),
    (2, 8, (1, 0, 2, 3)),
    (3, 31, (0, 1, 0, 1)),
)


def require(condition, failure):
    if not condition:
        raise ValueError(failure)


def encode(field):
    return " ".join(str(coef) for cell in field for word in cell for coef in k.reported(word))


def emit(name, value):
    print(json.dumps({"section": name, "value": value}, sort_keys=True, separators=(",", ":")))


def prepare(template, bare, mode):
    field = [list(cell) for cell in template]
    for site in CLOCK:
        field[site][k.CORR] = bare[site][k.CORR]
    if mode == 1:
        words = [bare[s][k.CORR] for s in CLOCK]
        selector, remainder = divmod(k.reported(k.add(*words))[2] + 4, 4)
        require(not remainder and selector in (0, 1), "outside the two observed input accounts")
        for s, bias in ((8, (1, 0, -2, 0)), (28, (-1, 0, -2, 0))):
            field[s][k.CLK] = k.add(template[s][k.CLK], k.scale(selector, k.from_j(*bias)))
    elif mode == 2:
        for source, target, bias in WIRES:
            field[target][k.CLK] = k.add(bare[source][k.CLK], k.from_j(*bias))
    else:
        raise ValueError(mode)
    return tuple(map(tuple, field))


def unobserved(field):
    # The transition takes only the complete current field and its bit.
    start, bit = field, 1
    for tick in range(1, 165):
        pre = field
        post_c, field = k.native_step(field, bit)
        bit = 1 - bit
        if tick == 159:
            worker_cuts = tuple(tuple(k.reported(w) for w in cut[28]) for cut in (pre, post_c, field))
    end = field, bit
    for _ in range(164):
        bit = 1 - bit
        field = k.inverse_step(field, bit)
    require((field, bit) == (start, 1), "complete 164-tick round trip")
    return end, worker_cuts


def main():
    template = tuple(tuple(k.from_j(*word) for word in cell)
                     for cell in json.loads((HERE / "launch43.json").read_bytes()))
    require(len(template) == 32 and all(len(c) == 4 for c in template), "literal field shape")
    verdicts, bare_digest = k.Findings(), sha256()
    history, _, ready = k.bare_reference(verdicts, bare_digest)
    require(not verdicts.counts and set(ready) == set(range(85)), "bare ready orbit")
    inputs = [history[(ready[i] - 1) % k.PERIOD] for i in range(85)]
    clocks = [tuple(inp[s][k.CORR] for s in CLOCK) for inp in inputs]
    require(len(set(clocks)) == 85, "input alias")
    emit("fixture", dict(ledger=measure.LEDGER, bare_sha256=bare_digest.hexdigest(),
                         template_sha256=sha256((HERE / "launch43.json").read_bytes()).hexdigest(),
                         original_clock_projections=len(set(clocks)), four_wires=WIRES))
    with tempfile.TemporaryDirectory() as build:
        exe = Path(build) / "audit"
        subprocess.run(["g++", "-std=c++20", "-O3", str(HERE / "audit.cpp"), "-o", str(exe)], check=True)
        for mode in (1, 2):
            launches = [prepare(template, inp, mode) for inp in inputs]
            require(len(set(launches)) == 85 and launches[43] == template, "physical launch identity")
            for rank, field in enumerate(launches):
                require(tuple(field[s][k.CORR] for s in CLOCK) == clocks[rank], "clock fidelity")
                require(k.reported_account(field) == measure.LEDGER, "launch ledger")
            lines = [f"{mode} {rank} 0 {encode(field)}\n" for rank, field in enumerate(launches)]
            external = subprocess.run([str(exe)], input="".join(lines).encode("ascii"),
                                      capture_output=True, check=True)
            schema, *entries = external.stdout.decode("ascii").splitlines()
            require(not external.stderr and schema.split() == measure.HEADER and len(entries) == 85,
                    "native row schema or coverage")
            rows = [list(map(int, line.split())) for line in entries]
            ends, hits = sha256(), []
            for rank, field in enumerate(launches):
                row, details = measure.trial(field, mode, rank, details=rank == 43)
                require(row == rows[rank], ("five/four coefficient disagreement", mode, rank))
                (end, bit), plain_worker = unobserved(field)
                ends.update(f"{rank} {bit} {encode(end)}\n".encode("ascii"))
                if row[measure.HEADER.index("work_tick")]:
                    hits.append(rank)
                if rank == 43:
                    work = details.get("work_tick")
                    if work and work["tick"] == 159:
                        scored = tuple(tuple(map(tuple, work["live_worker"][cut]))
                                       for cut in ("pre_C", "post_C", "post_B"))
                        require(plain_worker == scored, "plain launch worker cuts disagree")
                    emit("rank43", dict(mode=mode, row=row, plain_worker_159=plain_worker, source=details.get("source"),
                                        restore=details.get("restore"), retained=details["live_retained_through"],
                                        worker=details.get("work_tick")))
            emit("census", dict(mode=mode, columns=measure.HEADER, rows=rows, work_ranks=hits,
                                physical_launches=len(set(launches)), complete_inverses=len(launches),
                                final_fields_and_bits_sha256=ends.hexdigest(),
                                launch_fields_sha256=sha256("".join(encode(f)+"\n" for f in launches)
                                                            .encode("ascii")).hexdigest()))


if __name__ == "__main__":
    main()
