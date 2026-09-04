#!/usr/bin/env python3
"""Validate Public Canon companion ledgers.

The core ledger validator lives in check_ledger_core.py. This wrapper adds one
representation rule: same-layer OPEN_DECISION rows
are validated by check_gate_contract.py and are not cross-layer dependency
gates. All other ledger validation is delegated to the core.
"""

from __future__ import annotations

import argparse
from pathlib import Path

try:  # package import under unittest
    from tools import check_ledger_core as _core
    from tools.check_gate_contract import GateContractError, validate_gate_contract
except ModuleNotFoundError:  # direct `python tools/check_ledger.py`
    import check_ledger_core as _core
    from check_gate_contract import GateContractError, validate_gate_contract


# Preserve the complete public import surface of the historical checker. Several
# generators and validators import constants/helpers from check_ledger.py; a
# maintenance wrapper must not make those names disappear.
for _name in dir(_core):
    if not _name.startswith("_") and _name not in {"validate", "main"}:
        globals()[_name] = getattr(_core, _name)

_core_validate = _core.validate
_core_read_tsv = _core.read_tsv


def _open_decision_ids(root: Path) -> set[str]:
    rows = _core_read_tsv(root / "canon" / "GATES.tsv", GATE_FIELDS)
    return {
        row["gate_id"].strip()
        for row in rows
        if row["gate_kind"].strip() == "OPEN_DECISION"
    }


def validate(root: Path) -> Snapshot:
    root = root.resolve()
    validate_gate_contract(root)
    decision_ids = _open_decision_ids(root)
    if not decision_ids:
        return _core_validate(root)

    def filtered_read_tsv(path: Path, fields: tuple[str, ...]) -> list[dict[str, str]]:
        rows = _core_read_tsv(path, fields)
        if path.name == "GATES.tsv":
            return [
                row for row in rows
                if row["gate_id"].strip() not in decision_ids
            ]
        if path.name == "NORMATIVE.tsv":
            filtered: list[dict[str, str]] = []
            for row in rows:
                copy = dict(row)
                gates = [
                    gate.strip()
                    for gate in copy["gate_ids"].split(";")
                    if gate.strip() and gate.strip() not in decision_ids
                ]
                copy["gate_ids"] = ";".join(gates)
                filtered.append(copy)
            return filtered
        return rows

    original = _core.read_tsv
    _core.read_tsv = filtered_read_tsv
    try:
        snapshot = _core_validate(root)
    finally:
        _core.read_tsv = original

    return Snapshot(
        claims=snapshot.claims,
        items=snapshot.items,
        dependencies=snapshot.dependencies,
        evidence=snapshot.evidence,
        history_events=snapshot.history_events,
        gates=snapshot.gates + len(decision_ids),
        frontier_programs=snapshot.frontier_programs,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        snapshot = validate(args.root.resolve())
    except (LedgerError, GateContractError) as error:
        print(f"FAIL: {error}")
        raise SystemExit(1)
    print(
        "LEDGER PASS "
        f"claims={snapshot.claims} items={snapshot.items} "
        f"dependencies={snapshot.dependencies} evidence={snapshot.evidence} "
        f"history={snapshot.history_events} gates={snapshot.gates}"
        f" programs={snapshot.frontier_programs}"
    )


if __name__ == "__main__":
    main()
