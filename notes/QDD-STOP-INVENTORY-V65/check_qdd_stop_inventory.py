#!/usr/bin/env python3
"""QDD STOP inventory refresh at Public Canon v65 (NON-CANONICAL).

Re-runs, against the current public ledger, the fourteen-item inventory that
notes/canon/P-DMATTER-TOTAL-1-QDD-PUBLIC-REQUIREMENTS-AUDIT.md recorded at
Public Canon v27 as PUBLIC 0 / MISSING 14.

The authoritative requirement is the QUADRATIC-DECODER-DATA falsifier text in
canon/REGISTRY.tsv. This script pins that text, extracts the fourteen named
inputs from it, resolves each to a registered public normative identifier with
an exact canon-text anchor, and then audits the QDD dependency closure for
completeness and acyclicity.

The script establishes no claim, changes no status, and creates no definition,
probe, evidence, gate or dependency. It reports the state of the public ledger
and names the residuals that remain outside the inventory.

Run from the repository root. Standard library only. Deterministic output.
"""

import csv
import hashlib
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
CANON = ROOT / "canon"

# The frozen STOP clause of the QUADRATIC-DECODER-DATA falsifier. If the
# registry text moves, this audit must be rewritten rather than adjusted.
STOP_CLAUSE = (
    "STOP until the coefficient ring, effective carrier, common total domain, "
    "orbit-to-amplitude bridge, Gram, dagger, transpose, QCarrier equality, Q, "
    "effects, Born pairing, MatterData schema, write map, and complete "
    "dependency graph are public"
)

# The fourteen named inputs, in registry order, each with the public normative
# identifiers that resolve it and an exact substring of that identifier's canon
# definition text that anchors the resolution.
RESOLUTION = [
    ("coefficient ring", [
        ("DEF-QDD-COEFFICIENT-Q", "coefficient ring Q with the trivial involution")]),
    ("effective carrier", [
        ("DEF-QDD-BALANCED-PISTON", "V_eff = ell(F_5)^4")]),
    ("common total domain", [
        ("DEF-QDD-DOMAIN-K0",
         "the common total domain of the quadratic D_matter leg")]),
    ("orbit-to-amplitude bridge", [
        ("DEF-QDD-AMPLITUDE-B0", "Amp_QDD = iota_B0 o beta_QDD")]),
    ("Gram", [
        ("DEF-QDD-GRAM", "the matrix of the trace pairing in B0")]),
    ("dagger", [
        ("DEF-QDD-DAGGER", "v^dagger = v^T on Q^4")]),
    ("transpose", [
        ("DEF-QDD-TRANSPOSE", "transpose(A) = A^T on M_4(Q)")]),
    ("QCarrier equality", [
        ("DEF-QDD-QCARRIER-EQUALITY",
         "ordered componentwise rational matrix equality")]),
    ("Q", [
        ("DEF-QDD-QPAIR", "Q_QDD(v) = (A_dagger, A_T) = (v v^dagger, v v^T)")]),
    ("effects", [
        ("DEF-QDD-PROJECTOR-LOW", "the first member of the frozen ordered effect pair"),
        ("DEF-QDD-PROJECTOR-HIGH", "the second member of the frozen ordered pair")]),
    ("Born pairing", [
        ("DEF-QDD-BRANCH-WEIGHT-PAIRING", "the factor-route Born trace pairing")]),
    ("MatterData schema", [
        ("DEF-QDD-MATTER-RECORD",
         "MatterData_QDD, a pure type schema of five typed fields")]),
    ("write map", [
        ("DEF-QDD-DIRECT-WRITE", "D_QDD_direct = R_cyc o iota_B0 o beta_QDD")]),
    ("complete dependency graph", []),  # audited structurally, not by anchor
]

# Factor-side objects the direct write must not name, per the
# EFFECT_SHADOW_MINIMAL independence firewall.
FACTOR_SIDE = {
    "DEF-QDD-GRAM", "DEF-QDD-DAGGER", "DEF-QDD-TRANSPOSE", "DEF-QDD-QPAIR",
    "DEF-QDD-QCARRIER-EQUALITY", "DEF-QDD-PROJECTOR-LOW",
    "DEF-QDD-PROJECTOR-HIGH", "DEF-QDD-BRANCH-WEIGHT-PAIRING",
    "DEF-QDD-FACTOR-MAP",
}

CLOSURE_SEED = [i for _, ids in RESOLUTION for i, _ in ids] + [
    "DEF-QDD-TRACE-PAIRING", "DEF-QDD-LOW-LINE", "DEF-QDD-FACTOR-MAP",
    "QDD-ALGEBRAIC-FACTORIZATION",
]


def read_tsv(name):
    with (CANON / name).open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def canon_version():
    """Read the live Canon version from the CANON.md title."""
    title = (CANON / "CANON.md").read_text(encoding="utf-8").splitlines()[0]
    match = re.fullmatch(r"# TWIST-J Public Canon v([1-9][0-9]*)", title)
    if not match:
        raise SystemExit("CANON.md lacks a Public Canon vN title")
    return match.group(1)


def canon_definitions():
    """Extract the DEF-QDD-* definition bodies from the Route A dictionary."""
    text = (CANON / "CANON.md").read_text(encoding="utf-8")
    start = text.index("### QDD Route A dictionary")
    fence = text.index("```", text.index("Definitions.", start))
    block = text[fence + 3:]
    block = block[:block.index("```")]
    defs, current = {}, None
    for line in block.splitlines():
        if line.startswith("DEF-QDD-"):
            current = line.strip()
            defs[current] = []
        elif current is not None:
            defs[current].append(line.strip())
    return {k: " ".join(v) for k, v in defs.items()}


def main():
    registry = {r["claim_id"]: r for r in read_tsv("REGISTRY.tsv")}
    normative = {r["item_id"]: r for r in read_tsv("NORMATIVE.tsv")}
    evidence = {r["claim_id"]: r for r in read_tsv("EVIDENCE.tsv")}
    gates = read_tsv("GATES.tsv")
    deps = read_tsv("DEPENDENCIES.tsv")
    defs = canon_definitions()

    results, residuals, gaps = [], [], []

    def check(tag, name, ok, detail):
        results.append((ok, tag, name, detail))

    # 01 the row and its frozen STOP clause
    row = registry.get("QUADRATIC-DECODER-DATA")
    ok = row is not None and row["status"] == "O" and STOP_CLAUSE in row["falsifier"]
    check("01", "ROW", ok,
          "QUADRATIC-DECODER-DATA is O and carries the pinned STOP clause")

    # 02 the clause names exactly fourteen inputs
    named = STOP_CLAUSE[len("STOP until the "):-len(" are public")]
    parts = [p.strip() for p in named.replace(", and ", ", ").split(", ")]
    ok = len(parts) == 14 and parts == [n for n, _ in RESOLUTION]
    check("02", "ITEMS", ok, "the STOP clause names exactly 14 required public inputs")

    # 03-06 resolution of the thirteen definitional inputs
    ids = [i for _, pair in RESOLUTION for i, _ in pair]
    unresolved = [n for n, pair in RESOLUTION[:-1] if not pair]
    check("03", "RESOLVE", not unresolved,
          "%d/13 definitional inputs resolve to %d public normative IDs"
          % (13 - len(unresolved), len(ids)))

    bad_type = [i for i in ids
                if normative.get(i, {}).get("item_type") != "DEFINITION"]
    check("04", "TYPES", not bad_type,
          "all %d resolving IDs are registered DEFINITION rows" % len(ids))

    bad_layer = [i for i in ids if normative.get(i, {}).get("layer") != "L1"]
    check("05", "LAYER", not bad_layer,
          "all %d resolving IDs are declared at layer L1" % len(ids))

    missing_text = [i for i in ids if i not in defs]
    check("06", "TEXT", not missing_text,
          "all %d resolving IDs carry definition text in canon/CANON.md" % len(ids))

    bad_anchor = [i for _, pair in RESOLUTION for i, a in pair
                  if a not in defs.get(i, "")]
    check("07", "ANCHOR", not bad_anchor,
          "each resolution is anchored by an exact canon phrase")

    # 08-09 the dependency closure: completeness and acyclicity
    requires = {}
    for d in deps:
        if d["relation"] == "REQUIRES":
            requires.setdefault(d["item_id"], set()).add(d["depends_on"])

    closure, stack = set(), list(CLOSURE_SEED)
    while stack:
        node = stack.pop()
        if node in closure:
            continue
        closure.add(node)
        stack.extend(requires.get(node, ()))

    unregistered = sorted(n for n in closure if n not in normative)
    check("08", "CLOSURE",
          not unregistered,
          "the QDD closure is %d nodes, every node registered in NORMATIVE.tsv"
          % len(closure))

    order, mark = [], {}

    def visit(node):
        state = mark.get(node)
        if state == 2:
            return True
        if state == 1:
            return False
        mark[node] = 1
        for nxt in sorted(requires.get(node, ())):
            if nxt in closure and not visit(nxt):
                return False
        mark[node] = 2
        order.append(node)
        return True

    acyclic = all(visit(n) for n in sorted(closure))
    check("09", "ACYCLIC", acyclic,
          "the closure is acyclic; %d nodes in dependency order" % len(order))

    # 10 the independence firewall on the direct write
    direct, stack = set(), ["DEF-QDD-DIRECT-WRITE"]
    while stack:
        node = stack.pop()
        if node in direct:
            continue
        direct.add(node)
        stack.extend(requires.get(node, ()))
    leak = sorted(direct & FACTOR_SIDE)
    check("10", "FIREWALL", not leak,
          "DEF-QDD-DIRECT-WRITE closure (%d nodes) names no factor-side object"
          % len(direct))

    # 11 the factorization theorem and its evidence grade
    fact = registry.get("QDD-ALGEBRAIC-FACTORIZATION", {})
    fev = evidence.get("QDD-ALGEBRAIC-FACTORIZATION", {})
    ok = (fact.get("status") == "T"
          and fev.get("architecture_requirement") == "two-architecture"
          and fev.get("location") == "reproduce/qdd-route-a")
    check("11", "FACTOR", ok,
          "QDD-ALGEBRAIC-FACTORIZATION is T on two-architecture evidence")

    # 12 item 14 has two halves: the closure, and the row's edge into it.
    row_req = sorted(requires.get("QUADRATIC-DECODER-DATA", ()))
    qdd_defs = sorted(n for n in closure if n.startswith("DEF-QDD-"))
    named = sorted({i for _, pair in RESOLUTION for i, _ in pair})
    unwired = sorted(set(named) - set(row_req))
    check("12", "ROWEDGE", not unwired,
          "QUADRATIC-DECODER-DATA carries %d REQUIRES edges reaching %d of the "
          "%d STOP-named definitions (%d-node DEF-QDD-* block)"
          % (len(row_req), len(named) - len(unwired), len(named),
             len(qdd_defs)))
    if unwired:
        gaps.append(("BINDING",
                     "item 14 is complete and acyclic for the definitions but "
                     "the open row does not reach %d of them: %s"
                     % (len(unwired), ", ".join(unwired))))

    # residuals: outside the fourteen-item inventory, still open
    qdd_gates = [g for g in gates
                 if "QDD" in g["gate_id"] or "QDD" in g["owner_item_id"]]
    residuals.append(("GATE",
                      "canon/GATES.tsv carries no QDD binding gate (%d gates, %d QDD)"
                      % (len(gates), len(qdd_gates))))
    residuals.append(("DOMAIN",
                      "K_QDD is total for the quadratic leg and is the n = 0 "
                      "headed pointed-orbit set; DEF-DECODER-MATTER keeps "
                      "dom(D_matter) a declared subset of K and no K_QDD = K "
                      "identity is registered"))
    residuals.append(("SLOTS",
                      "QDD-QCARRIER-DIAGONAL-BOUNDARY: the two typed slots of "
                      "Q_QDD coincide on V_eff, so the frozen domain does not "
                      "test the pair structure"))
    residuals.append(("ADOPTED",
                      "DEF-QDD-BRANCH-WEIGHT-PAIRING is an adopted dictionary "
                      "input, not derived from J"))

    version = canon_version()
    print("TWIST-J QDD STOP inventory refresh (NON-CANONICAL)")
    print("Public Canon v%s; authority is canon/REGISTRY.tsv, not this script"
          % version)
    print()
    for ok, tag, name, detail in results:
        print("%s %s %-9s %s" % ("PASS" if ok else "GAP ", tag, name, detail))
    print()
    for i, (name, detail) in enumerate(gaps, start=len(results) + 1):
        print("GAP   %02d %-9s %s" % (i, name, detail))
    print()
    for i, (name, detail) in enumerate(residuals,
                                       start=len(results) + len(gaps) + 1):
        print("RESID %02d %-9s %s" % (i, name, detail))
    print()
    print("INVENTORY v27          PUBLIC  0 / MISSING 14")
    rowedge = all(r[0] for r in results if r[1] == "12")
    structural = all(r[0] for r in results if r[1] in ("08", "09")) and rowedge
    public = (13 - len(unresolved)) + (1 if structural else 0)
    print("INVENTORY v%-3s         PUBLIC %2d / MISSING %2d"
          % (version, public, 14 - public))
    print("STOP CLAUSE            %s"
          % ("DISCHARGED" if public == 14
             else "DISCHARGED FOR %d OF 14; 1 BINDING GAP" % public))
    print("POSITIVE CLOSURE       NOT CLAIMED; %d residuals outside the inventory"
          % len(residuals))
    print("QUADRATIC-DECODER-DATA O / STOP, unchanged by this audit")
    print()
    digest = hashlib.sha256(
        "\n".join(order).encode("utf-8")).hexdigest()
    print("closure order sha256   %s" % digest)
    print()

    # Frontier definitional debt: how many DEFINITION rows each live O/H claim
    # reaches, above the architecture baseline every live row inherits.
    defs_all = {i for i, r in normative.items() if r["item_type"] == "DEFINITION"}
    owned = {}
    for claim, r in registry.items():
        if r["status"] not in ("O", "H"):
            continue
        seen, stack = set(), [claim]
        while stack:
            node = stack.pop()
            if node in seen:
                continue
            seen.add(node)
            stack.extend(requires.get(node, ()))
        owned[claim] = seen & defs_all
    # The baseline is what DEF-ARCHITECTURE itself reaches: the declared
    # architecture every conditional statement in the Canon rests on.
    seen, stack = set(), ["DEF-ARCHITECTURE"]
    while stack:
        node = stack.pop()
        if node in seen:
            continue
        seen.add(node)
        stack.extend(requires.get(node, ()))
    baseline = seen & defs_all
    print("FRONTIER DEFINITIONAL DEBT")
    print("  live O/H rows                        %d" % len(owned))
    print("  shared architecture baseline         %d definitions" % len(baseline))
    ranked = sorted(((len(v - baseline), k) for k, v in owned.items()),
                    reverse=True)
    for n, claim in ranked:
        if n:
            print("  %-38s +%d" % (claim, n))
    zero = sum(1 for n, _ in ranked if not n)
    print("  rows owning no definition above it   %d of %d" % (zero, len(owned)))
    print()
    # Audit integrity: checks 01-11 verify the ledger state this audit reports
    # and must all hold. Check 12 is the finding, not an audit failure.
    integrity = [r for r in results if r[1] != "12"]
    broken = [r for r in integrity if not r[0]]
    print("RESULT %d/%d audit checks hold; %d gap, %d residuals"
          % (len(integrity) - len(broken), len(integrity), len(gaps),
             len(residuals)))
    return 1 if broken else 0


if __name__ == "__main__":
    sys.exit(main())
