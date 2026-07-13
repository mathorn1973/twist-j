#!/usr/bin/env python3
"""Build the Public Canon v1 Genesis companion-ledger snapshot.

This command is intentionally limited to the first public Genesis snapshot.
It does not infer pre-public history.  Future releases append explicit events
to HISTORY.tsv instead of rebuilding earlier events.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path
import re


REGISTRY_FIELDS = (
    "claim_id",
    "status",
    "scope",
    "canon_section",
    "evidence",
    "falsifier",
)
NORMATIVE_FIELDS = (
    "item_id",
    "item_type",
    "claim_id",
    "status",
    "layer",
    "gate_ids",
    "statement_source",
)
DEPENDENCY_FIELDS = ("item_id", "depends_on", "relation", "basis")
EVIDENCE_FIELDS = (
    "claim_id",
    "evidence_id",
    "evidence_kind",
    "location",
    "sha256",
    "hash_mode",
    "architecture_requirement",
)
HISTORY_FIELDS = (
    "event_id",
    "event_date",
    "release",
    "claim_id",
    "event_type",
    "previous_status",
    "new_status",
    "scope_sha256",
    "evidence_id",
    "rationale",
)
GATE_FIELDS = (
    "gate_id",
    "claim_id",
    "from_layer",
    "to_layer",
    "gate_kind",
    "decision_condition",
)

STATUS_TYPES = {
    "T-LOCK": "THEOREM",
    "T": "THEOREM",
    "D": "DICTIONARY",
    "C": "COMPUTATION",
    "H": "HYPOTHESIS",
    "O": "OBLIGATION",
    "F": "FALSIFIED",
}

INVENTORY = (
    ("AXIOM-J", "AXIOM", "FOUNDATION", "canon/CANON.md::Axiom (A0)"),
    ("DEF-MJ", "DEFINITION", "FOUNDATION", "canon/CANON.md::Primitive and architecture inventory"),
    ("DEF-CHECKPOINT", "DEFINITION", "L1", "canon/CANON.md::2. Time, space, and the decoder"),
    ("DEF-ODOMETER-ORBIT", "DEFINITION", "L1", "canon/CANON.md::2. Time, space, and the decoder"),
    ("DEF-KERNEL-GENERATORS", "DEFINITION", "L1", "canon/CANON.md::3. The kernel and the census"),
    ("DEF-SELECTOR", "DEFINITION", "L1", "canon/CANON.md::2. Time, space, and the decoder"),
    ("DEF-AUTONOMOUS-STATE", "DEFINITION", "L1", "canon/CANON.md::2. Time, space, and the decoder"),
    ("DEF-LOG-STREAM", "DEFINITION", "L5", "canon/CANON.md::2. Time, space, and the decoder"),
    ("DEF-DECODER-MATTER", "DEFINITION", "MULTI", "canon/CANON.md::2. Time, space, and the decoder"),
    ("DEF-DECODER-GEOMETRY", "DEFINITION", "MULTI", "canon/CANON.md::2. Time, space, and the decoder"),
    ("DEF-DECODER-CLOCK", "DEFINITION", "MULTI", "canon/CANON.md::2. Time, space, and the decoder"),
    ("DEF-ARCHITECTURE", "DEFINITION", "MULTI", "canon/CANON.md::Primitive and architecture inventory"),
    ("DEF-ACTION-LAYERS", "DEFINITION", "MULTI", "canon/CANON.md::Conventions"),
    ("DEF-PUBLIC-STATUSES", "DEFINITION", "NOT_APPLICABLE", "canon/CANON.md::Statuses"),
    ("ANCHOR-ELECTRON-MASS", "EMPIRICAL_ANCHOR", "MULTI", "canon/CANON.md::Primitive and architecture inventory"),
)

DEFINITION_DEPENDENCIES = (
    ("DEF-MJ", "AXIOM-J", "REQUIRES", "M_J is multiplication by J"),
    ("DEF-AUTONOMOUS-STATE", "DEF-CHECKPOINT", "REQUIRES", "Omega contains the finite checkpoint"),
    ("DEF-AUTONOMOUS-STATE", "DEF-ODOMETER-ORBIT", "REQUIRES", "Omega contains the forward odometer orbit"),
    ("DEF-AUTONOMOUS-STATE", "DEF-KERNEL-GENERATORS", "REQUIRES", "U applies one declared generator"),
    ("DEF-AUTONOMOUS-STATE", "DEF-SELECTOR", "REQUIRES", "U reads the declared selector"),
    ("DEF-LOG-STREAM", "DEF-AUTONOMOUS-STATE", "REQUIRES", "the Log is a derived orbit record"),
    ("DEF-DECODER-MATTER", "DEF-AUTONOMOUS-STATE", "REQUIRES", "D_matter reads a forward orbit"),
    ("DEF-DECODER-GEOMETRY", "DEF-DECODER-MATTER", "REQUIRES", "geometry reads MatterData"),
    ("DEF-DECODER-CLOCK", "DEF-DECODER-GEOMETRY", "REQUIRES", "clock reads accumulated geometry"),
    ("DEF-ARCHITECTURE", "DEF-AUTONOMOUS-STATE", "REQUIRES", "declared architecture contains Omega and U"),
    ("DEF-ARCHITECTURE", "DEF-DECODER-CLOCK", "REQUIRES", "declared architecture contains the partial decoder"),
)

CLAIM_DEPENDENCIES = (
    ("J-UNIT", "AXIOM-J", "REQUIRES", "unit theorem starts from J"),
    ("J-PROJECTIONS", "AXIOM-J", "REQUIRES", "polar decomposition starts from J"),
    ("J-MODULUS-CHORD", "AXIOM-J", "REQUIRES", "chord identity starts from J"),
    ("PI-FROM-J", "AXIOM-J", "REQUIRES", "principal logarithm identity starts from J"),
    ("J-TENTH-ROOT", "AXIOM-J", "REQUIRES", "root identity starts from J"),
    ("J-GOLDEN-BRIDGE", "AXIOM-J", "REQUIRES", "bridge identities start from J"),
    ("J-STEP", "DEF-MJ", "REQUIRES", "J-STEP is the matrix action of M_J"),
    ("PLENUM-POINT", "AXIOM-J", "REQUIRES", "plenum identities start from J"),
    ("J-RAMIFIED-CHORD", "AXIOM-J", "REQUIRES", "ramified chord starts from J"),
    ("LOG-AXES-INDEPENDENCE", "AXIOM-J", "REQUIRES", "the two logarithmic axes are projections of J"),
    ("AXIOM-PROJECTION-DICTIONARY", "J-PROJECTIONS", "REQUIRES", "registry scope names the theorem input"),
    ("AXIOM-PROJECTION-DICTIONARY", "PLENUM-POINT", "REQUIRES", "registry scope names the theorem input"),
    ("AXIOM-PROJECTION-DICTIONARY", "J-MODULUS-CHORD", "REQUIRES", "registry scope names the theorem input"),
    ("AXIOM-PROJECTION-DICTIONARY", "J-RAMIFIED-CHORD", "REQUIRES", "registry scope names the theorem input"),
    ("BOOST-COUNT-LADDER", "BOOST-READING-SPLIT", "REQUIRES", "count dictionary rests on the exact split"),
    ("READING-SPLIT", "CODEC-TR4", "REQUIRES", "linear leg is CODEC-TR4"),
    ("SILVER-SIBLING", "SILVER-RING-FACTS", "REQUIRES", "dictionary rests on finite ring facts"),
    ("FORCE-AS-CURVATURE", "FORCE-WEYL-HOLONOMY", "REQUIRES", "curvature reading rests on the Weyl theorem"),
    ("MEASURE-BORN-VERB", "BORN-FACE-WEIGHTS", "REQUIRES", "registry scope names the theorem input"),
    ("COSMOLOGY-READING-DICTIONARY", "TT-LINEAR-ZERO", "REQUIRES", "dictionary reads the exact zero response"),
    ("COSMOLOGY-READING-DICTIONARY", "GYRON-DENSITY", "REQUIRES", "dictionary reads the exact density"),
    ("COSMOLOGY-READING-DICTIONARY", "COSMOLOGY-REGISTER", "REQUIRES", "dictionary reads the committed forms"),
    ("ELECTRON-G-TREE", "ELECTRON-G-RATIO", "REQUIRES", "dictionary rests on the exact ratio"),
    ("ELECTRON-G-TREE", "ELECTRON-G-DOUBLE-COVER", "REQUIRES", "dictionary rests on the exact double cover"),
    ("ELECTRON-SIGN", "ELECTRON-SIGN-LAWS", "REQUIRES", "dictionary rests on the exhaustive laws"),
    ("FRW-INHOM", "FRW-CANONICAL-FORM", "REQUIRES", "inhomogeneous extension starts from the homogeneous theorem"),
    ("TM-SYM2-MEASURE", "GYRON-DENSITY", "REQUIRES", "registered measure residual uses rho = 1/6"),
    ("MASS-LADDER-FORMS", "NEUTRON-DELTA-EM", "BOUNDED_BY", "neutron comparison remains open"),
    ("TT-QUADRATIC-GERM", "TT-GAUGE-PULLBACK", "BOUNDED_BY", "g_mu remains the named open input"),
    ("TT-QUADRATIC-INDUCED", "TT-VECTOR-STATE-NORMALIZATION", "BOUNDED_BY", "normalization remains open"),
    ("COSMOLOGY-REGISTER", "NS-TILT", "BOUNDED_BY", "tilt remains a live hypothesis"),
    ("CONFORMAL-PREFACTOR", "FRW-INHOM", "BOUNDED_BY", "inhomogeneous action remains open"),
    ("CONFORMAL-PREFACTOR", "METRO-EDGE-SCALE", "BOUNDED_BY", "SI clause remains open"),
    ("STRONG-SEED", "ALPHA-S-RUNNING", "BOUNDED_BY", "running remains open"),
    ("STRONG-SEED", "SCHEME-DICTIONARY", "BOUNDED_BY", "measurement scheme remains open"),
    ("ELECTRON-G-TREE", "QUANT-SUBSTRATE", "BOUNDED_BY", "quantum substrate remains open"),
)

GATES = (
    ("GATE-L1-L2-CURVATURE", "CURVATURE-TRACE-VALUE", "L1", "L2", "OPEN_LIFT"),
    ("GATE-L2-L3-GENERATIONS", "GENERATIONS-L3", "L2", "L3", "OPEN_LIFT"),
    ("GATE-L4-L6-COLOR-MEASURE", "COLOR-MEASURE-SELECTION", "L4", "L6", "OPEN_LIFT"),
    ("GATE-L5-L6-BORN-READING", "MEASURE-BORN-VERB", "L5", "L6", "DICTIONARY_LIFT"),
    ("GATE-L5-L6-METRO-NORMALIZATION", "METRO-ADMISSIBILITY", "L5", "L6", "OPEN_LIFT"),
)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def bundle_sha256(path: Path, root: Path) -> str:
    if path.is_file():
        return sha256_bytes(path.read_bytes())
    lines: list[str] = []
    for item in sorted(candidate for candidate in path.rglob("*") if candidate.is_file()):
        if "__pycache__" in item.parts or item.suffix == ".pyc":
            continue
        relative = item.relative_to(root).as_posix()
        lines.append(f"{sha256_bytes(item.read_bytes())}  {relative}\n")
    return sha256_bytes("".join(lines).encode("utf-8"))


def write_tsv(path: Path, fields: tuple[str, ...], rows: list[dict[str, str]]) -> None:
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, delimiter="\t", fieldnames=fields, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def explicit_layer(scope: str) -> str:
    layers = sorted(set(re.findall(r"(?<![A-Z0-9])L[1-6](?![A-Z0-9])", scope)))
    if len(layers) == 1:
        return layers[0]
    if len(layers) > 1:
        return "MULTI"
    return "NOT_APPLICABLE"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--date", default="2026-07-13")
    args = parser.parse_args()
    root = args.root.resolve()
    canon = root / "canon"

    with (canon / "REGISTRY.tsv").open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        if tuple(reader.fieldnames or ()) != REGISTRY_FIELDS:
            raise SystemExit("REGISTRY.tsv schema mismatch")
        registry = list(reader)

    gate_ids_by_claim: dict[str, list[str]] = {}
    registry_by_id = {row["claim_id"]: row for row in registry}
    for gate_id, claim_id, _from, _to, _kind in GATES:
        gate_ids_by_claim.setdefault(claim_id, []).append(gate_id)

    normative: list[dict[str, str]] = []
    for item_id, item_type, layer, source in INVENTORY:
        normative.append({
            "item_id": item_id,
            "item_type": item_type,
            "claim_id": "",
            "status": "",
            "layer": layer,
            "gate_ids": "",
            "statement_source": source,
        })
    for row in registry:
        claim = row["claim_id"]
        normative.append({
            "item_id": claim,
            "item_type": STATUS_TYPES[row["status"]],
            "claim_id": claim,
            "status": row["status"],
            "layer": explicit_layer(row["scope"]),
            "gate_ids": ";".join(gate_ids_by_claim.get(claim, [])),
            "statement_source": f"canon/CANON.md::{row['canon_section']}",
        })

    dependencies = [
        {"item_id": item, "depends_on": dependency, "relation": relation, "basis": basis}
        for item, dependency, relation, basis
        in (*DEFINITION_DEPENDENCIES, *CLAIM_DEPENDENCIES)
    ]
    # The Canon states that every downstream statement is conditional on the
    # declared architecture.  Record that top-level boundary for every claim
    # outside the purely algebraic first section; do not infer finer edges.
    for row in registry:
        if row["canon_section"] == "1. The axiom and the two projections":
            continue
        dependencies.append({
            "item_id": row["claim_id"],
            "depends_on": "DEF-ARCHITECTURE",
            "relation": "REQUIRES",
            "basis": "Canon definition boundary: every downstream statement is conditional on the declared architecture",
        })

    canon_hash = sha256_bytes((canon / "CANON.md").read_bytes())
    evidence: list[dict[str, str]] = []
    history: list[dict[str, str]] = []
    for row in registry:
        claim = row["claim_id"]
        location = row["evidence"]
        evidence_id = f"EV-{claim}"
        if location == "inline":
            kind = "INLINE_CANON"
            digest = canon_hash
            hash_mode = "file-sha256"
            architecture = "none"
        elif location.startswith(("https://", "http://")):
            kind = "EXTERNAL_SOURCE"
            digest = "PENDING-SOURCE-MANIFEST"
            hash_mode = "external-manifest"
            architecture = "none"
        else:
            kind = "REPRODUCTION"
            artifact = root / location
            digest = bundle_sha256(artifact, root)
            hash_mode = "bundle-manifest-sha256-v1"
            if row["status"] in {"T", "T-LOCK"}:
                runs = artifact / "RUNS"
                recorded = (
                    (runs / "aarch64.md").is_file()
                    and (runs / "x86_64.md").is_file()
                )
                architecture = (
                    "two-architecture" if recorded
                    else "two-architecture-pending"
                )
            elif row["status"] == "C":
                architecture = "one-architecture"
            else:
                architecture = "recorded-audit"
        evidence.append({
            "claim_id": claim,
            "evidence_id": evidence_id,
            "evidence_kind": kind,
            "location": location,
            "sha256": digest,
            "hash_mode": hash_mode,
            "architecture_requirement": architecture,
        })
        history.append({
            "event_id": f"GENESIS-{claim}",
            "event_date": args.date,
            "release": "canon-v1-genesis",
            "claim_id": claim,
            "event_type": "DECLARE",
            "previous_status": "-",
            "new_status": row["status"],
            "scope_sha256": sha256_bytes(row["scope"].encode("utf-8")),
            "evidence_id": evidence_id,
            "rationale": "Initial public declaration; pre-public mapping remains in legacy/CUTOVER_AUDIT.md",
        })

    gates: list[dict[str, str]] = []
    for gate_id, claim_id, from_layer, to_layer, kind in GATES:
        row = registry_by_id[claim_id]
        condition = row["falsifier"] or row["scope"]
        gates.append({
            "gate_id": gate_id,
            "claim_id": claim_id,
            "from_layer": from_layer,
            "to_layer": to_layer,
            "gate_kind": kind,
            "decision_condition": condition,
        })

    write_tsv(canon / "NORMATIVE.tsv", NORMATIVE_FIELDS, normative)
    write_tsv(canon / "DEPENDENCIES.tsv", DEPENDENCY_FIELDS, dependencies)
    write_tsv(canon / "EVIDENCE.tsv", EVIDENCE_FIELDS, evidence)
    write_tsv(canon / "HISTORY.tsv", HISTORY_FIELDS, history)
    write_tsv(canon / "GATES.tsv", GATE_FIELDS, gates)
    print(
        "GENESIS LEDGER BUILT "
        f"claims={len(registry)} inventory={len(INVENTORY)} "
        f"dependencies={len(dependencies)} gates={len(gates)}"
    )


if __name__ == "__main__":
    main()
