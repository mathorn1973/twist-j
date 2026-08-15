#!/usr/bin/env python3
"""
update_status_separation_witness.py  --  part of the conservative QDD Route A
insertion package.  Updates reproduce/status-separation/verify.py for the
folded tree: new counts and a 33rd check for the conservative QDD partition.
The existing CENTRAL, CM-2I and J-SEAM checks keep reading
QUADRATIC-DECODER-DATA as O and are not modified.  Regenerates EXPECTED.txt.
Usage: python3 update_status_separation_witness.py <tree root>
"""
import os, subprocess, sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
ss = ROOT / "reproduce" / "status-separation" / "verify.py"
t = ss.read_text(encoding="utf-8")

def rep(old, new):
    global t
    assert t.count(old) == 1, (t.count(old), old[:70])
    t = t.replace(old, new)

rep('    expected_counts = {"T": 135, "D": 42, "C": 27, "F": 13,\n                       "O": 22, "H": 2}',
    '    expected_counts = {"T": 138, "D": 42, "C": 27, "F": 13,\n                       "O": 23, "H": 2}')
rep('        "registry and companion-ledger counts match Public Canon v47",\n'
    '        len(rows) == 241\n'
    '        and counts == expected_counts\n'
    '        and len(normative) == 259\n'
    '        and len(dependencies) == 384\n'
    '        and len(evidence) == 241\n'
    '        and two_architecture == 161\n'
    '        and len(history) == 756\n'
    '        and len(gates) == 10\n'
    '        and len({row["program_id"] for row in programs.values()}) == 7\n'
    '        and sum(path.is_dir() for path in REPRODUCE.iterdir()) == 22,',
    '        "registry and companion-ledger counts match Public Canon v48",\n'
    '        len(rows) == 245\n'
    '        and counts == expected_counts\n'
    '        and len(normative) == 280\n'
    '        and len(dependencies) == 425\n'
    '        and len(evidence) == 245\n'
    '        and two_architecture == 164\n'
    '        and len(history) == 760\n'
    '        and len(gates) == 10\n'
    '        and len({row["program_id"] for row in programs.values()}) == 7\n'
    '        and sum(path.is_dir() for path in REPRODUCE.iterdir()) == 23,')

NEW_CHECK = '''
    qdd_path = "reproduce/qdd-route-a"
    checks.append((
        "QDD-ROUTE-A",
        "the QDD Route A algebra is three L1 theorems on two-architecture evidence; the apparatus is a separate O; QUADRATIC-DECODER-DATA stays O with its ROOT/STOP program row; no gate and no L6 row exist",
        all(
            has_status(index, claim, "T")
            and normative.get(claim, {}).get("layer") == "L1"
            and normative.get(claim, {}).get("gate_ids") == ""
            and index.get(claim, {}).get("evidence") == qdd_path
            and evidence.get(claim, {}).get("architecture_requirement")
            == "two-architecture"
            for claim in ("QDD-ALGEBRAIC-FACTORIZATION", "QDD-PROJECTOR-PAIR-TR4",
                          "QDD-QCARRIER-DIAGONAL-BOUNDARY")
        )
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("program_id")
        == "DECODER_CORE"
        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("queue_role")
        == "FOLLOWUP"
        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("work_state")
        == "STOP"
        and has_status(index, "QUADRATIC-DECODER-DATA", "O")
        and programs.get("QUADRATIC-DECODER-DATA", {}).get("queue_role")
        == "ROOT"
        and programs.get("QUADRATIC-DECODER-DATA", {}).get("work_state")
        == "STOP"
        and "QDD-BORN-READOUT-MEASURE" not in index
        and "DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION" not in normative
        and "GATE-L1-L6-QDD-BORN-READOUT" not in gates
        and normative.get("DEF-QDD-PROJECTOR-LOW", {}).get("item_type")
        == "DEFINITION"
        and scope_lacks(index, "QDD-ALGEBRAIC-FACTORIZATION",
                        ("apparatus", "occurrence"))
        and scope_contains_all(index, "QDD-ALGEBRAIC-FACTORIZATION",
                               ("no completion-contract field is filled",))
        and scope_contains_all(index, "QDD-PROJECTOR-PAIR-TR4",
                               ("no uniqueness-from-j",))
        and scope_contains_all(index, "QDD-QCARRIER-DIAGONAL-BOUNDARY",
                               ("a_dagger = a_t = v v^t",
                                "no physical central phase"))
        and scope_contains_all(index, "QDD-INSTRUMENT-APPARATUS",
                               ("filling no field of the decoder completion contract",)),
    ))

    print("TWIST-J theorem/dictionary separation audit")'''
rep('\n    print("TWIST-J theorem/dictionary separation audit")', NEW_CHECK)
ss.write_text(t, encoding="utf-8")

env = dict(os.environ, LC_ALL="C", LANG="C", PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0", TZ="UTC")
r = subprocess.run([sys.executable, "reproduce/status-separation/verify.py"], cwd=ROOT, capture_output=True, text=True, env=env)
last = (r.stdout.strip().splitlines() or ["(no output)"])[-1]
print("[status-separation] " + last + f" (exit {r.returncode})")
if r.returncode != 0 or not last.endswith("ALL PASS"):
    print((r.stdout + r.stderr)[-2000:])
    sys.exit("status-separation witness did not pass; EXPECTED.txt not written")
(ROOT / "reproduce" / "status-separation" / "EXPECTED.txt").write_text(r.stdout, encoding="utf-8")
