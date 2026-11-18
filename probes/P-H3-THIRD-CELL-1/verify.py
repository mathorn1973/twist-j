# SPDX-License-Identifier: Apache-2.0
"""Reproduce the H3 third-cell, two-word and preparation tests."""

import json
import os
from pathlib import Path
import subprocess
import tempfile

import experiments
import launches
import measure
import simple
import sparse

HERE = Path(__file__).resolve().parent


def emit(section, data):
    print(json.dumps({"section": section, "value": data}, sort_keys=True, separators=(",", ":")))


def main():
    bare = launches.bare_inputs()
    fields = launches.four_wire(bare)
    emit("inputs", {"ranks": len(fields), "four_wire_sha256": launches.LAUNCH_DIGEST,
                    "ledger": measure.LEDGER})
    with tempfile.TemporaryDirectory() as temporary:
        directory = Path(temporary)
        query_path = directory / "queries.tsv"
        query_path.write_bytes("".join(f"2 {i} 0 {launches.encode(f)}\n"
                                       for i, f in enumerate(fields)).encode("ascii"))
        programs = {}
        for name in ("cascade", "dual", "natural", "seed"):
            exe = directory / (name + (".exe" if os.name == "nt" else ""))
            subprocess.run(["g++", "-std=c++20", "-O3", str(HERE / (name + ".cpp")), "-o", str(exe)],
                           check=True)
            programs[name] = str(exe)
        for name, result in experiments.run(query_path, programs, directory).items():
            emit(name, result)
    emit("two_tick_binary", simple.run(bare))
    emit("sparse_preparation", sparse.run(bare))


if __name__ == "__main__":
    main()
