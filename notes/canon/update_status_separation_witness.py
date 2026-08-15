#!/usr/bin/env python3
"""
update_status_separation_witness.py  --  part of the QDD Route A insertion package.

Updates reproduce/status-separation/verify.py for the folded tree (the release
audit is updated by every completed Canon fold): new counts, QDD read as D,
the apparatus row in the program table, and a 33rd check for the QDD partition.
Then regenerates EXPECTED.txt.  Usage: python3 update_status_separation_witness.py <tree root>
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
    '    expected_counts = {"T": 138, "D": 44, "C": 27, "F": 13,\n                       "O": 22, "H": 2}')
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
    '        len(rows) == 246\n'
    '        and counts == expected_counts\n'
    '        and len(normative) == 282\n'
    '        and len(dependencies) == 448\n'
    '        and len(evidence) == 246\n'
    '        and two_architecture == 166\n'
    '        and len(history) == 763\n'
    '        and len(gates) == 11\n'
    '        and len({row["program_id"] for row in programs.values()}) == 7\n'
    '        and sum(path.is_dir() for path in REPRODUCE.iterdir()) == 23,')
# check 10 CENTRAL
rep('        and has_status(index, "QUADRATIC-DECODER-DATA", "O")\n'
    '        and programs.get("QUADRATIC-DECODER-DATA", {}).get("work_state")\n'
    '        == "STOP"\n'
    '        and central not in programs,',
    '        and has_status(index, "QUADRATIC-DECODER-DATA", "D")\n'
    '        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("work_state")\n'
    '        == "STOP"\n'
    '        and central not in programs,')
# check 15 CM-2I
rep('        and has_status(index, "SPIN-LIFT-FORCED", "F")\n'
    '        and has_status(index, "QUADRATIC-DECODER-DATA", "O")\n'
    '        and has_status(index, "COLOR-MEASURE-SELECTION", "O")\n'
    '        and programs.get("QUADRATIC-DECODER-DATA", {}).get("program_id")\n'
    '        == "DECODER_CORE"\n'
    '        and programs.get("QUADRATIC-DECODER-DATA", {}).get("queue_role")\n'
    '        == "ROOT"\n'
    '        and programs.get("QUADRATIC-DECODER-DATA", {}).get("work_state")\n'
    '        == "STOP"\n'
    '        and programs.get("QUADRATIC-DECODER-DATA", {}).get("work_mode")\n'
    '        == "FORMAL"',
    '        and has_status(index, "SPIN-LIFT-FORCED", "F")\n'
    '        and has_status(index, "QUADRATIC-DECODER-DATA", "D")\n'
    '        and has_status(index, "COLOR-MEASURE-SELECTION", "O")\n'
    '        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("program_id")\n'
    '        == "DECODER_CORE"\n'
    '        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("queue_role")\n'
    '        == "FOLLOWUP"\n'
    '        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("work_state")\n'
    '        == "STOP"\n'
    '        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("work_mode")\n'
    '        == "FORMAL"')
rep('"marked semilinear pair stays T at L4; decoder and measure stay O/STOP"',
    '"marked semilinear pair stays T at L4; decoder dictionary at D, apparatus and measure stay O/STOP"')
# check 26 J-SEAM
rep('        and has_status(index, "LOG-AXES-INDEPENDENCE", "T")\n'
    '        and has_status(index, "QUADRATIC-DECODER-DATA", "O")\n'
    '        and seam not in programs,',
    '        and has_status(index, "LOG-AXES-INDEPENDENCE", "T")\n'
    '        and has_status(index, "QUADRATIC-DECODER-DATA", "D")\n'
    '        and seam not in programs,')

NEW_CHECK = '''
    qdd_path = "reproduce/qdd-route-a"
    qdd_gate = "GATE-L1-L6-QDD-BORN-READOUT"
    checks.append((
        "QDD-ROUTE-A",
        "QDD algebra stays T at L1; the L6 Born reading is D behind its gate; the apparatus is O; QDD is a dictionary",
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
        and has_status(index, "QDD-BORN-READOUT-MEASURE", "D")
        and normative.get("QDD-BORN-READOUT-MEASURE", {}).get("layer") == "L6"
        and normative.get("QDD-BORN-READOUT-MEASURE", {}).get("gate_ids")
        == qdd_gate
        and gates.get(qdd_gate, {}).get("owner_item_id")
        == "QDD-BORN-READOUT-MEASURE"
        and gates.get(qdd_gate, {}).get("from_layer") == "L1"
        and gates.get(qdd_gate, {}).get("to_layer") == "L6"
        and has_status(index, "QDD-INSTRUMENT-APPARATUS", "O")
        and programs.get("QDD-INSTRUMENT-APPARATUS", {}).get("program_id")
        == "DECODER_CORE"
        and has_status(index, "QUADRATIC-DECODER-DATA", "D")
        and normative.get("QUADRATIC-DECODER-DATA", {}).get("layer") == "MULTI"
        and "QUADRATIC-DECODER-DATA" not in programs
        and normative.get("DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION", {}).get("item_type")
        == "DEFINITION"
        and normative.get("DEF-QDD-PROJECTOR-LOW", {}).get("item_type")
        == "DEFINITION"
        and scope_lacks(index, "QDD-ALGEBRAIC-FACTORIZATION",
                        ("apparatus", "occurrence"))
        and scope_contains_all(index, "QDD-QCARRIER-DIAGONAL-BOUNDARY",
                               ("a_dagger = a_t = v v^t",
                                "no physical central phase"))
        and scope_contains_all(index, "QDD-BORN-READOUT-MEASURE",
                               ("numerical witness", "not derived from j",
                                "zero_denominator")),
    ))

    print("TWIST-J theorem/dictionary separation audit")'''
rep('\n    print("TWIST-J theorem/dictionary separation audit")', NEW_CHECK)
ss.write_text(t, encoding="utf-8")

env = dict(os.environ, LC_ALL="C", LANG="C", PYTHONDONTWRITEBYTECODE="1", PYTHONHASHSEED="0", TZ="UTC")
r = subprocess.run([sys.executable, "reproduce/status-separation/verify.py"], cwd=ROOT, capture_output=True, text=True, env=env)
(ROOT / "reproduce" / "status-separation" / "EXPECTED.txt").write_text(r.stdout, encoding="utf-8")
print("[status-separation] " + r.stdout.strip().splitlines()[-1] + f" (exit {r.returncode})")
