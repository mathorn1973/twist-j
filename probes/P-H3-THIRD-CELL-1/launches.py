# SPDX-License-Identifier: Apache-2.0
"""Prepare the published four-wire inputs and their original bare clocks."""

import json
from hashlib import sha256
from pathlib import Path

import kernel as k
import measure as m

HERE = Path(__file__).resolve().parent
CLOCK = (0, 1, 4, 5, 8, 9)
WIRES = ((0, 7, (-2, 0, -1, 0)), (1, 28, (-3, 0, -1, 0)),
         (2, 8, (1, 0, 2, 3)), (3, 31, (0, 1, 0, 1)))
LAUNCH_DIGEST = "8e65f16a2f545c566c3b2fa915fd993f3fd0e78644a17b12567a42ccc434c4cd"


def encode(field):
    return " ".join(str(i) for cell in field for word in cell for i in k.reported(word))


def bare_inputs():
    findings = k.Findings()
    orbit, _, ready = k.bare_reference(findings, sha256())
    m.require(not findings.counts and set(ready) == set(range(85)), "bare rank bijection")
    fields = [orbit[(ready[rank] - 1) % k.PERIOD] for rank in range(85)]
    m.require(all(k.reported_account(f) == k.BARE_ACCOUNTS for f in fields), "bare accounts")
    return fields


def four_wire(bare):
    raw = (HERE / "launch43.json").read_bytes()
    m.require(sha256(raw).hexdigest() == "1a4d47ff21e95385f93fe05915aed409a38d1ebb40f3e2f0e724c6f8eb267d7f",
              "literal four-wire input")
    template = tuple(tuple(k.from_j(*word) for word in cell) for cell in json.loads(raw))
    fields = []
    for original in bare:
        field = [list(cell) for cell in template]
        for site in CLOCK:
            field[site][k.CORR] = original[site][k.CORR]
        for source, site, bias in WIRES:
            field[site][k.CLK] = k.add(original[source][k.CLK], k.from_j(*bias))
        fields.append(tuple(map(tuple, field)))
    clocks = {tuple(f[i][k.CORR] for i in CLOCK) for f in fields}
    m.require(len(clocks) == len(set(fields)) == 85 and fields[43] == template, "input identity")
    m.require(all(k.reported_account(f) == m.LEDGER for f in fields), "four-wire accounts")
    digest = sha256("".join(encode(f) + "\n" for f in fields).encode("ascii"))
    m.require(digest.hexdigest() == LAUNCH_DIGEST, "ordered input family")
    return fields
