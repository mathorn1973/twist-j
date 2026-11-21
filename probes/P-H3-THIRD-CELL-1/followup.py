# SPDX-License-Identifier: Apache-2.0
"""Supplementary four-coordinate binary replay and the short 181 B output trace."""

from collections import Counter
from pathlib import Path
import subprocess
import tempfile

import kernel as k
import launches
import measure as m

HERE = Path(__file__).resolve().parent


def binary(bare):
    values = "".join(f"{rank} {launches.encode(f)}\n" for rank, f in enumerate(bare))
    with tempfile.TemporaryDirectory() as build:
        exe = Path(build) / "binary"
        subprocess.run(["g++", "-std=c++20", "-O2", str(HERE / "independent_binary.cpp"),
                        "-o", str(exe)], check=True)
        run = subprocess.run([str(exe)], input=values.encode("ascii"), capture_output=True, check=True)
        m.require(not run.stderr, "binary follow-up stderr")
        print(run.stdout.decode("ascii").replace("\r\n", "\n"), end="")


def short_trace(rank, start):
    field = start
    ledger = k.account(start)
    for tick in range(1, 182):
        _, field, _ = m.native(field, tick, ledger, rank)
    writer = 28
    output = (k.from_j(0, 1, 0, 1), k.from_j(0, -1, 0, -1))
    m.require(field[writer][:2] == output, "original 181 B word")
    other = m.replace(field, writer, (*m.W_WORD, *field[writer][2:]))
    m.require(k.account(other) == ledger, "word comparison")
    for tick in range(182, 185):
        c, live, tags = m.native(field, tick, ledger, rank)
        alt_c, alt, alt_tags = m.native(other, tick, ledger, rank)
        print("trace", rank, tick, "writer live/control", tags[writer], alt_tags[writer],
              "holds O after C/B", int(c[writer][:2] == output), int(live[writer][:2] == output),
              "matter difference after C at 31", int(c[31][:2] != alt_c[31][:2]),
              "radiation difference after B at 28", int(live[28][2:] != alt[28][2:]),
              "radiation difference after C at 29", int(c[29][2:] != alt_c[29][2:]))
        field, other = live, alt


def main():
    bare = launches.bare_inputs()
    print("x7 wrap CORR parity at both boundary cells",
          sorted(Counter(tuple(tuple(i % 2 for i in k.reported(f[s][3])) for s in (0, 1))
                         for f in bare).items()))
    binary(bare)
    fields = launches.four_wire(bare)
    for rank in (0, 22, 43):
        short_trace(rank, fields[rank])


if __name__ == "__main__":
    main()
