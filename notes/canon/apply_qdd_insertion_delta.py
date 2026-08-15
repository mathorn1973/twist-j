#!/usr/bin/env python3
"""
apply_qdd_insertion_delta.py  --  prospective public fold delta for the QDD Route A
insertion package (owner decisions of 2026-08-15: SPLIT, ACCEPT T1, ACCEPT GATE, SLOT RULING).

Applies the delta to a scratch copy of the Public Canon v47 tree (given as argv[1]) and
runs tools/check_ledger.py.  It also expects reproduce/qdd-route-a/{verify.py,EXPECTED.txt,README.md}
to be present in the tree.  NON-CANONICAL until the owner folds it as a Canon content commit.
"""
import csv, hashlib, sys, subprocess
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else "/home/claude/fold")
canon = ROOT / "canon"
ANCHOR = "QDD Route A dictionary"
DATE = "2026-08-15"; RELEASE = "canon-v48-candidate"
BUNDLE = "reproduce/qdd-route-a"

def sha(s): return hashlib.sha256(s.encode("utf-8")).hexdigest()
def sha_bytes(b): return hashlib.sha256(b).hexdigest()
def bundle_sha256(path, root):
    lines = []
    for item in sorted((p for p in path.rglob("*") if p.is_file()), key=lambda c: c.relative_to(root).as_posix()):
        if "__pycache__" in item.parts or item.suffix == ".pyc" or "RUNS" in item.relative_to(path).parts: continue
        lines.append(f"{sha_bytes(item.read_bytes())}  {item.relative_to(root).as_posix()}\n")
    return sha_bytes("".join(lines).encode("utf-8"))
def read_rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return [line.rstrip("\n").split("\t") for line in f]
def write_rows(path, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        for r in rows: f.write("\t".join(r) + "\n")

BUNDLE_SHA = bundle_sha256(ROOT / BUNDLE, ROOT)

# ------------------------------------------------------------------ 1. CANON.md block
block = open(Path(__file__).with_name("CANON-BLOCK-QDD-ROUTE-A.md"), encoding="utf-8").read()
assert ANCHOR in block
_text = (canon / "CANON.md").read_text(encoding="utf-8")
_marker = "\n## 3. The kernel and the census\n"
assert _text.count(_marker) == 1
_text = _text.replace(_marker, "\n" + block.rstrip("\n") + "\n" + _marker)   # placed at the end of section 2 (decoder interface)
(canon / "CANON.md").write_text(_text, encoding="utf-8")
src = f"canon/CANON.md::{ANCHOR}"

# ------------------------------------------------------------------ 1b. prose occurrences of the old status in CANON.md
text = (canon / "CANON.md").read_text(encoding="utf-8")
subs = [
 ("quadratic pair, remains in QUADRATIC-DECODER-DATA [O]. No umbrella",
  "quadratic pair, is registered in QUADRATIC-DECODER-DATA [D] (QDD Route A\ndictionary). No umbrella"),
 ("cross-layer lift. In particular QUADRATIC-DECODER-DATA [O] remains STOP\nand unchanged.",
  "cross-layer lift. In particular they do not touch QUADRATIC-DECODER-DATA\n[D]."),
 ("measure lift. QUADRATIC-DECODER-DATA [O] and COLOR-MEASURE-SELECTION [O]\nremain STOP and unchanged.",
  "measure lift. QUADRATIC-DECODER-DATA [D] is untouched and\nCOLOR-MEASURE-SELECTION [O] remains STOP and unchanged."),
 ("operators can be registered as separate gates. `QUADRATIC-DECODER-DATA`\n[O] asks for a\npublicly typed action on data; no unregistered closure of state-update,",
  "operators can be registered as separate gates. `QUADRATIC-DECODER-DATA`\n[D] registers the\npublicly typed action on data; no unregistered closure of state-update,"),
 ("  QUADRATIC-DECODER-DATA     the typed quadratic/Born D_matter action and its\n                             exact factorization through Q; carrier, bridge,\n                             Gram, dagger, transpose, QCarrier equality,\n                             effects, MatterData schema, write map, domain, and\n                             complete dependencies remain open; linear, binary,\n                             reconstruction, and post-state instrument claims\n                             are outside this row",
  "  QDD-INSTRUMENT-APPARATUS   the physical instrument family {K_a} with\n                             E_a = K_a^sharp K_a realizing the ordered LOW/HIGH\n                             effect shadow; apparatus carrier, ready state,\n                             coupling, pointer, reduction, occurrence law,\n                             sampling and post-state remain open; STOP"),
]
for old, new in subs:
    assert text.count(old) == 1, old[:60]
    text = text.replace(old, new)
(canon / "CANON.md").write_text(text, encoding="utf-8")

# ------------------------------------------------------------------ 2. definitions
defs = ["DEF-QDD-DOMAIN-K0", "DEF-QDD-BALANCED-PISTON", "DEF-QDD-AMPLITUDE-B0", "DEF-QDD-COEFFICIENT-Q",
        "DEF-QDD-TRACE-PAIRING", "DEF-QDD-GRAM", "DEF-QDD-DAGGER", "DEF-QDD-TRANSPOSE", "DEF-QDD-QPAIR",
        "DEF-QDD-QCARRIER-EQUALITY", "DEF-QDD-LOW-LINE", "DEF-QDD-PROJECTOR-LOW", "DEF-QDD-PROJECTOR-HIGH",
        "DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-MATTER-RECORD", "DEF-QDD-DIRECT-WRITE", "DEF-QDD-FACTOR-MAP",
        "DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION"]

# ------------------------------------------------------------------ 3. claims
S = {}
S["QDD-ALGEBRAIC-FACTORIZATION"] = ("T", "L1", "", BUNDLE,
 "the owner-adopted Route A dictionary on the finite balanced piston carrier: the direct cyclotomic write D_QDD_direct = R_cyc o iota_B0 o beta_QDD equals the factor route F_QDD o Q_QDD o beta_QDD field by field on all 15625 checkpoints; the tagged record is total with exactly 25 ZERO_SUPPORT heads and no division on the zero branch, exactly normalized on the 15600 supported heads (w_low + w_high = m and p_low + p_high = 1, nonnegative weights, m > 0), independent of q and r and dependent on each piston coordinate, constant on each of the 313 Q_QDD-fibres (one of size 25 and 312 of size 50) and injective on QCarrier_QDD; negative controls: the rational-line reading Q.1 in place of the LOW LINE mismatches on 480 of 625 pistons and omitting G on 540 of 625; an exact identity of the adopted definitions confirmed on the complete finite domain, not an independent readout, not a physical selection, not a decoder-completion, totality-of-D_matter or uniqueness claim",
 "fires if any field of D_QDD_direct and F_QDD o Q_QDD o beta_QDD differs on one checkpoint, if one supported head violates w_low + w_high = m or p_low + p_high = 1 or has a negative weight, if a Q_QDD-fibre carries two records, if two fibres carry one record, or if the record depends on q or r")
S["QDD-PROJECTOR-PAIR-TR4"] = ("T", "L1", "", BUNDLE,
 "on Q^4 with G = I_4 - (1/5) 1 1^T: E_low = (1/4) 1 1^T is the unique G-self-adjoint idempotent with kernel ker Tr_4 = {v : sum v_i = 0}, because a G-self-adjoint idempotent has image (ker)^perp_G and G^-1 1 = 5 1 gives (ker Tr_4)^perp_G = span(1); hence {E_low, E_high = I_4 - E_low} is the G-orthogonal resolution of Q^4 along the piston character Tr_4, both are G-self-adjoint idempotents, im(E_high) = ker Tr_4; under iota_B0 the image line of E_low is the LOW LINE Q lambda_B with lambda_B = 1 + zeta + zeta^2 + zeta^3 = -zeta^4, not the rational line and not the trace kernel of K; closed forms m = |v|^2 - s^2/5, w_low = s^2/20, w_high = |v|^2 - s^2/4 with s = sum v_i; linear algebra only, no apparatus, no physical selection and no uniqueness-from-J claim",
 "fires if a G-self-adjoint idempotent other than E_low has kernel ker Tr_4, if G^-1 1 differs from 5 1, if any closed form fails on one piston, or if iota_B0(1,1,1,1) differs from -zeta^4")
S["QDD-QCARRIER-DIAGONAL-BOUNDARY"] = ("T", "L1", "", BUNDLE,
 "on the frozen carrier V_eff = ell(F_5)^4 the two typed slots of Q_QDD(v) = (A_dagger, A_T) coincide, A_dagger = A_T = v v^T, because the dagger of DEF-QDD-DAGGER is the transpose over Q; both slots remain typed and declared, the frozen domain does not test their difference, and no physical central phase is derived from this equality; the cyclotomic pair (w sigma_4(w), w^2) with w = iota_B0(v) has 90 distinct Hermitian slots and 313 distinct pairs on the 625 pistons, and 80 Hermitian slots carry more than one record, so neither a Herm-only reading nor a use of both slots is asserted for the frozen record; diagnostic only, no new field, no L6 claim",
 "fires if A_dagger differs from A_T on one piston of V_eff, or if the counts 90, 313 and 80 differ under the frozen definitions")
S["QDD-BORN-READOUT-MEASURE"] = ("D", "L6", "GATE-L1-L6-QDD-BORN-READOUT", BUNDLE,
 "the L6 dictionary reading of the field normalized_weight_state on the NONZERO branch: (p_low, p_high) = (w_low, w_high)/m read as a finite two-outcome measure on the ordered pair (LOW, HIGH), where by DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION LOW reads the Tr_4 line and HIGH its G-orthogonal complement ker Tr_4; the ZERO branch remains the tag ZERO_DENOMINATOR and is not a measure; the fields support_state, total_weight, branch_weights and density_state are L1-derived D_matter fields and are not lifted; the value table over the 312 nonzero classes has 22 distinct values with 42 classes at p_low = 0 and 2 at p_low = 1, and the value 1/6 at 12 classes is a numerical witness with no dependency, input, threshold, normalization or confirmation role; the LOW/HIGH assignment is a dictionary choice, not derived from J; no apparatus, instrument, realized outcome, occurrence law, sampling, post-state or SI claim",
 "fires if QDD-ALGEBRAIC-FACTORIZATION or QDD-PROJECTOR-PAIR-TR4 fires, if a supported head yields a value outside [0,1] or a pair not summing to 1, if the ordered pair (LOW, HIGH) is swapped or quotiented, or if the ZERO branch is read as a measure")
S["QDD-INSTRUMENT-APPARATUS"] = ("O", "MULTI", "", "inline",
 "the physical instrument family {K_a} realizing the ordered LOW/HIGH effect shadow of QDD-BORN-READOUT-MEASURE, with E_a = K_a^sharp K_a in the frozen Gram form, from a public apparatus carrier, ready state, coupling, pointer and reduction, together with the occurrence law, sampling, post-state and completeness of the physically admissible class; the effect shadow, the Born trace evaluation and the MatterData_QDD write are owned by QUADRATIC-DECODER-DATA and are not repeated here; the reverse inference from effects to instruments is forbidden and equality of effects does not identify post-state instruments",
 "STOP until the apparatus carrier, ready state, coupling, pointer, reduction to K_a, the K-level and E-level equivalence relations, occurrence law and completeness statement are public; closes positively when an exhibited public instrument family realizes E_low and E_high exactly with a complete acyclic dependency graph and no new free dimensionless input; closes negatively if every admissible family violates a registered input or fails to reproduce the ordered effect pair")

QDD_ID = "QUADRATIC-DECODER-DATA"
QDD_NEW = ("D", "MULTI", "", BUNDLE,
 "the typed quadratic/Born D_matter action of the registered leg: on the common total domain K_QDD of pointed forward orbits, the direct write D_QDD_direct = R_cyc o iota_B0 o beta_QDD writes the five-field MatterData_QDD schema (support_state, total_weight, branch_weights, density_state, normalized_weight_state) and factors through the ordered pair Q_QDD(psi) = (A_dagger, A_T) on QCarrier_QDD by QDD-ALGEBRAIC-FACTORIZATION; coefficient ring Q with the amplitude field Q(zeta_5), Gram G, dagger, transpose and Gram adjoint as distinct typed operations, componentwise QCarrier equality, the projector pair of QDD-PROJECTOR-PAIR-TR4 as effect shadow, the Born trace pairing and the exact write map with a complete acyclic dependency graph; the L6 reading of the normalized branch is QDD-BORN-READOUT-MEASURE; the physical instrument family, occurrence law, sampling and post-state remain in QDD-INSTRUMENT-APPARATUS [O]; the linear CODEC-TR4 and binary Thue-Morse/census legs, cross-leg or state reconstruction, the hybrid label extension and post-state instrument uniqueness are excluded; a dictionary of declared definitions, not a totality, uniqueness or completeness theorem for D_matter and not a derivation of the architecture from J",
 "fires if QDD-ALGEBRAIC-FACTORIZATION, QDD-PROJECTOR-PAIR-TR4, QDD-QCARRIER-DIAGONAL-BOUNDARY or QDD-BORN-READOUT-MEASURE fires, if an input outside the frozen allowlist (the n = 0 head, its four piston coordinates, the balanced section, the fixed rational and cyclotomic constants and maps) is required, if a field is not constant on Q_QDD-fibres, if two heads distinguished by the record have equal Q_QDD, or if the dependency graph acquires a cycle")

# ------------------------------------------------------------------ 4. NORMATIVE
rows = read_rows(canon / "NORMATIVE.tsv")
for i, r in enumerate(rows):
    if r and r[0] == QDD_ID:
        rows[i] = [QDD_ID, "DICTIONARY", QDD_ID, "D", "MULTI", "", r[6]]
for d in defs: rows.append([d, "DEFINITION", "", "", "L1", "", src])
typ = {"T": "THEOREM", "D": "DICTIONARY", "O": "OBLIGATION"}
for cid, (st, layer, gates, loc, scope, fals) in S.items(): rows.append([cid, typ[st], cid, st, layer, gates, src])
write_rows(canon / "NORMATIVE.tsv", rows)

# ------------------------------------------------------------------ 5. REGISTRY / EVIDENCE / HISTORY
reg = read_rows(canon / "REGISTRY.tsv")
for i, r in enumerate(reg):
    if r and r[0] == QDD_ID:
        reg[i] = [QDD_ID, QDD_NEW[0], QDD_NEW[4], r[3], QDD_NEW[3], QDD_NEW[5]]
for cid, (st, layer, gates, loc, scope, fals) in S.items():
    reg.append([cid, st, scope, "2. Time, space, and the decoder", loc, fals])
write_rows(canon / "REGISTRY.tsv", reg)

ev = read_rows(canon / "EVIDENCE.tsv")
def ev_row(cid, loc, scope):
    if loc == "inline": return [cid, f"EV-{cid}", "INLINE_CANON", "inline", sha(scope), "registry-scope-sha256-v1", "none"]
    return [cid, f"EV-{cid}", "REPRODUCTION", loc, BUNDLE_SHA, "bundle-manifest-sha256-v1", "two-architecture"]
for i, r in enumerate(ev):
    if r and r[0] == QDD_ID: ev[i] = ev_row(QDD_ID, BUNDLE, QDD_NEW[4])
for cid, (st, layer, gates, loc, scope, fals) in S.items(): ev.append(ev_row(cid, loc, scope))
write_rows(canon / "EVIDENCE.tsv", ev)

hist = read_rows(canon / "HISTORY.tsv")
qdd_seq = max(int(r[1]) for r in hist[1:] if r[4] == QDD_ID)
def evsha(cid, loc, scope): return sha(scope) if loc == "inline" else BUNDLE_SHA
for cid, (st, layer, gates, loc, scope, fals) in S.items():
    hist.append([f"CANON48-DECLARE-{cid}", "1", DATE, RELEASE, cid, "DECLARE", "-", st, sha(scope), f"EV-{cid}", loc, evsha(cid, loc, scope),
                 "QDD Route A insertion package: declared from the merged DICTIONARY-DIRECT owner amendment, the owner decisions of 2026-08-15 (SPLIT, ACCEPT T1, ACCEPT GATE, SLOT RULING) and the two-architecture reproduction reproduce/qdd-route-a; the physical instrument family is registered separately and QDD does not hide it"])
hist.append([f"CANON48-SCOPE-{QDD_ID}", str(qdd_seq + 1), DATE, RELEASE, QDD_ID, "SCOPE_CHANGE", "O", "O", sha(QDD_NEW[4]), f"EV-{QDD_ID}", BUNDLE, BUNDLE_SHA,
             "QDD Route A insertion: the fourteen required data (coefficient ring, effective carrier, common total domain, orbit-to-amplitude bridge, Gram, dagger, transpose, QCarrier equality, Q, effect shadow, Born pairing, MatterData schema, write map, complete dependency graph) become public definitions; the physical instrument family is split out as QDD-INSTRUMENT-APPARATUS [O]; the linear, binary, reconstruction, hybrid and post-state surfaces stay excluded"])
hist.append([f"CANON48-STATUS-{QDD_ID}", str(qdd_seq + 2), DATE, RELEASE, QDD_ID, "STATUS_CHANGE", "O", "D", sha(QDD_NEW[4]), f"EV-{QDD_ID}", BUNDLE, BUNDLE_SHA,
             "closes as a dictionary after the public insertion of all identifiers, the common total domain, the five fields, the equalities, the dependencies, the L1 to L6 gate and the two-architecture reproduction; the algebraic factorization is QDD-ALGEBRAIC-FACTORIZATION [T], the projector pair QDD-PROJECTOR-PAIR-TR4 [T], the slot boundary QDD-QCARRIER-DIAGONAL-BOUNDARY [T], the L6 reading QDD-BORN-READOUT-MEASURE [D]; no uniqueness-from-J, no apparatus, no totality or completeness of D_matter"])
write_rows(canon / "HISTORY.tsv", hist)

# ------------------------------------------------------------------ 6. GATE
gates = read_rows(canon / "GATES.tsv")
gates.append(["GATE-L1-L6-QDD-BORN-READOUT", "QDD-BORN-READOUT-MEASURE", "L1", "L6", "DICTIONARY_LIFT",
 "PASS exactly when (1) the direct write is total into the tagged MatterData_QDD, (2) the ZERO branch is complete and performs no division, (3) on NONZERO the weights are nonnegative, (4) w_low + w_high = total_weight exactly, (5) the normalized weights sum to 1, (6) all five fields agree with the factor route, (7) the dependency graph is complete and acyclic, (8) no L2 to L5 claim is implicitly appropriated; closes negatively when one supported head yields a value outside [0,1], a pair not summing to 1, or two heads with equal Q_QDD yield different pairs; STOP while the record, the ordered outcome set or the L1 factorization theorem is missing; only normalized_weight_state on the NONZERO branch is lifted to L6; the value 1/6 is not an input, threshold, normalization or confirmation"])
write_rows(canon / "GATES.tsv", gates)

# ------------------------------------------------------------------ 7. FRONTIER_PROGRAMS
fp = read_rows(canon / "FRONTIER_PROGRAMS.tsv")
head, body = fp[0], [r for r in fp[1:] if r and r[0] != QDD_ID]
body.append(["QDD-INSTRUMENT-APPARATUS", "DECODER_CORE", "FOLLOWUP", "STOP", "FORMAL"])
body.sort(key=lambda r: r[0])
write_rows(canon / "FRONTIER_PROGRAMS.tsv", [head] + body)

# ------------------------------------------------------------------ 8. DEPENDENCIES
dep = []
def D(a, b, basis, rel="REQUIRES"): dep.append([a, b, rel, basis])
D("DEF-QDD-DOMAIN-K0", "DEF-ARCHITECTURE", "the head carrier is the set of pointed forward U-orbits of the declared architecture")
D("DEF-QDD-DOMAIN-K0", "DEF-DECODER-MATTER", "K_QDD is the common total domain of the quadratic D_matter leg")
D("DEF-QDD-BALANCED-PISTON", "DEF-QDD-DOMAIN-K0", "beta_QDD reads the n = 0 head of kappa in K_QDD")
D("DEF-QDD-AMPLITUDE-B0", "DEF-QDD-BALANCED-PISTON", "iota_B0 is composed with beta_QDD")
D("DEF-QDD-AMPLITUDE-B0", "DEF-QDD-COEFFICIENT-Q", "the amplitude lives in the declared field K with bar = sigma_4")
D("DEF-QDD-TRACE-PAIRING", "DEF-QDD-COEFFICIENT-Q", "the pairing uses sigma_4 and Tr_(K/Q)")
D("DEF-QDD-GRAM", "DEF-QDD-TRACE-PAIRING", "G is the matrix of the trace pairing in B0")
D("DEF-QDD-DAGGER", "DEF-QDD-COEFFICIENT-Q", "dagger is the trivial involution over Q")
D("DEF-QDD-TRANSPOSE", "DEF-QDD-COEFFICIENT-Q", "transpose over Q")
D("DEF-QDD-QPAIR", "DEF-QDD-DAGGER", "first slot A_dagger = v v^dagger")
D("DEF-QDD-QPAIR", "DEF-QDD-TRANSPOSE", "second slot A_T = v v^T")
D("DEF-QDD-QPAIR", "DEF-QDD-BALANCED-PISTON", "Q_QDD is restricted to V_eff")
D("DEF-QDD-QCARRIER-EQUALITY", "DEF-QDD-QPAIR", "ordered componentwise rational equality on im(Q_QDD | V_eff)")
D("DEF-QDD-LOW-LINE", "DEF-QDD-TRACE-PAIRING", "lambda_B and its pairing values are stated in the trace pairing")
D("DEF-QDD-PROJECTOR-LOW", "DEF-QDD-GRAM", "E_low is G-self-adjoint")
D("DEF-QDD-PROJECTOR-HIGH", "DEF-QDD-PROJECTOR-LOW", "E_high = I_4 - E_low")
D("DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-PROJECTOR-LOW", "w_low uses E_low")
D("DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-PROJECTOR-HIGH", "w_high uses E_high")
D("DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-GRAM", "m and the weights are traces against G on the transpose slot")
D("DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-LOW-LINE", "the cyclotomic pi_low projects onto Q lambda_B")
D("DEF-QDD-MATTER-RECORD", "DEF-QDD-BRANCH-WEIGHT-PAIRING", "the record fields are m, the branch weights, the density and their normalization")
D("DEF-QDD-DIRECT-WRITE", "DEF-QDD-AMPLITUDE-B0", "the direct write reads iota_B0 o beta_QDD")
D("DEF-QDD-DIRECT-WRITE", "DEF-QDD-LOW-LINE", "the direct write projects onto Q lambda_B")
D("DEF-QDD-DIRECT-WRITE", "DEF-QDD-MATTER-RECORD", "the direct write emits the record")
D("DEF-QDD-FACTOR-MAP", "DEF-QDD-QCARRIER-EQUALITY", "F_QDD is defined on QCarrier_QDD with its equality")
D("DEF-QDD-FACTOR-MAP", "DEF-QDD-BRANCH-WEIGHT-PAIRING", "F_QDD uses the Gram/projector formulas")
D("DEF-QDD-FACTOR-MAP", "DEF-QDD-MATTER-RECORD", "F_QDD emits the record")
D("DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION", "DEF-QDD-PROJECTOR-LOW", "LOW is the ordered outcome of the Tr_4 line projector")
D("DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION", "DEF-QDD-PROJECTOR-HIGH", "HIGH is the ordered outcome of the ker Tr_4 projector")
D("DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION", "CODEC-TR4", "explicit bridge to the Tr_4 line of the linear leg; a bridge row, not inheritance from a shared decoder stage")
D("QDD-ALGEBRAIC-FACTORIZATION", "DEF-QDD-DIRECT-WRITE", "left side of the identity")
D("QDD-ALGEBRAIC-FACTORIZATION", "DEF-QDD-FACTOR-MAP", "right side of the identity")
D("QDD-ALGEBRAIC-FACTORIZATION", "DEF-QDD-QPAIR", "the fibres are the Q_QDD fibres")
D("QDD-PROJECTOR-PAIR-TR4", "DEF-QDD-GRAM", "self-adjointness and orthogonality are taken with respect to G")
D("QDD-PROJECTOR-PAIR-TR4", "DEF-QDD-PROJECTOR-LOW", "the projector whose uniqueness is stated")
D("QDD-PROJECTOR-PAIR-TR4", "DEF-QDD-PROJECTOR-HIGH", "the complementary projector")
D("QDD-PROJECTOR-PAIR-TR4", "DEF-QDD-LOW-LINE", "the cyclotomic image of the projector line")
D("QDD-QCARRIER-DIAGONAL-BOUNDARY", "DEF-QDD-QPAIR", "the two typed slots whose coincidence on V_eff is stated")
D("QDD-QCARRIER-DIAGONAL-BOUNDARY", "DEF-QDD-DAGGER", "the dagger is the transpose over Q on the frozen carrier")
D("QDD-QCARRIER-DIAGONAL-BOUNDARY", "DEF-QDD-TRANSPOSE", "the second slot")
D("QDD-BORN-READOUT-MEASURE", "QDD-ALGEBRAIC-FACTORIZATION", "the measure reads the exact normalized record")
D("QDD-BORN-READOUT-MEASURE", "QDD-PROJECTOR-PAIR-TR4", "the outcomes LOW and HIGH are the Tr_4 line and its G-orthogonal complement")
D("QDD-BORN-READOUT-MEASURE", "DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION", "the explicit dictionary bridge assigning the ordered outcomes")
D("QDD-BORN-READOUT-MEASURE", "DEF-QDD-MATTER-RECORD", "only normalized_weight_state on the NONZERO branch is lifted")
D("QDD-BORN-READOUT-MEASURE", "DEF-ACTION-LAYERS", "the L6 reading is a lift across the action layers")
D("QDD-BORN-READOUT-MEASURE", "QDD-INSTRUMENT-APPARATUS", "any occurrence law, sampling or post-state reading is bounded by the open apparatus row", rel="BOUNDED_BY")
D("QDD-INSTRUMENT-APPARATUS", "DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION", "the instrument family must realize the ordered LOW/HIGH effect shadow")
D("QDD-INSTRUMENT-APPARATUS", "DEF-QDD-GRAM", "E_a = K_a^sharp K_a is taken in the frozen Gram form")
for d in ["DEF-QDD-DOMAIN-K0", "DEF-QDD-QPAIR", "DEF-QDD-QCARRIER-EQUALITY", "DEF-QDD-MATTER-RECORD", "DEF-QDD-DIRECT-WRITE",
          "DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-PROJECTOR-LOW", "DEF-QDD-PROJECTOR-HIGH", "DEF-BRIDGE-QDD-TR4-EFFECT-SELECTION",
          "DEF-DECODER-COMPLETION-CONTRACT", "DEF-ACTION-LAYERS"]:
    D(QDD_ID, d, "public binding of a required QDD datum")
D(QDD_ID, "QDD-ALGEBRAIC-FACTORIZATION", "the exact factorization through Q_QDD")
D(QDD_ID, "QDD-PROJECTOR-PAIR-TR4", "the effect shadow is the unique G-orthogonal pair along Tr_4")
D(QDD_ID, "QDD-QCARRIER-DIAGONAL-BOUNDARY", "the two Q slots coincide on the frozen carrier and stay typed")
D(QDD_ID, "QDD-BORN-READOUT-MEASURE", "the L6 reading of the normalized branch")
D(QDD_ID, "QDD-INSTRUMENT-APPARATUS", "the physical instrument family bounds every occurrence, sampling or post-state reading of the record", rel="BOUNDED_BY")
with open(canon / "DEPENDENCIES.tsv", "a", encoding="utf-8", newline="") as f:
    for r in dep: f.write("\t".join(r) + "\n")

# ------------------------------------------------------------------ 9. status-separation release witness (updated by every fold)
r = subprocess.run([sys.executable, str(Path(__file__).with_name("update_status_separation_witness.py")), str(ROOT)], cwd=ROOT, capture_output=True, text=True)
print((r.stdout + r.stderr).strip()[-600:])

print(f"delta applied: {len(defs)} definitions, {len(S)} new claims, {QDD_ID} O -> D, {len(dep)} dependency rows, 1 gate, bundle sha {BUNDLE_SHA}")
subprocess.run([sys.executable, "tools/generate_canon_views.py", "--apply"], cwd=ROOT, capture_output=True, text=True)
for tool in ("check_ledger.py", "check_canon.py", "check_status_labels.py"):
    r = subprocess.run([sys.executable, f"tools/{tool}"], cwd=ROOT, capture_output=True, text=True)
    print(f"[{tool}] " + (r.stdout + r.stderr).strip().splitlines()[-1] if (r.stdout+r.stderr).strip() else f"[{tool}] (no output)")
