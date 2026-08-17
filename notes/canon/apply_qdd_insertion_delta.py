#!/usr/bin/env python3
"""
apply_qdd_insertion_delta.py  --  conservative fold delta for the QDD Route A
algebra (owner audit of 2026-08-15: effect_ids UNRESOLVED, effects obligation
open, QUADRATIC-DECODER-DATA unchanged at [O]/STOP).

Registers 17 DEF-QDD-* definitions, three L1 theorems
(QDD-ALGEBRAIC-FACTORIZATION, QDD-PROJECTOR-PAIR-TR4,
QDD-QCARRIER-DIAGONAL-BOUNDARY) and the separate obligation
QDD-INSTRUMENT-APPARATUS [O].  It adds NO gate, NO bridge, NO L6 row, and it
does not touch the QUADRATIC-DECODER-DATA registry, normative, frontier or
prose entries in any way.

Applies the delta to a checkout given as argv[1] and runs the checkers.
NON-CANONICAL until the owner folds it as a Canon content commit.
"""
import hashlib, subprocess, sys
from pathlib import Path

ROOT = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
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
def append_rows(path, rows):
    with open(path, "a", encoding="utf-8", newline="") as f:
        for r in rows: f.write("\t".join(r) + "\n")

BUNDLE_SHA = bundle_sha256(ROOT / BUNDLE, ROOT)

# ------------------------------------------------------------------ 1. CANON.md block at the end of section 2
block = open(Path(__file__).with_name("CANON-BLOCK-QDD-ROUTE-A.md"), encoding="utf-8").read()
assert ANCHOR in block
text = (canon / "CANON.md").read_text(encoding="utf-8")
marker = "\n## 3. The kernel and the census\n"
assert text.count(marker) == 1
text = text.replace(marker, "\n" + block.rstrip("\n") + "\n" + marker)
src = f"canon/CANON.md::{ANCHOR}"

# ------------------------------------------------------------------ 1b. section 18: add the apparatus entry after the untouched QDD entry
qdd_entry = ("  QUADRATIC-DECODER-DATA     the typed quadratic/Born D_matter action and its\n"
             "                             exact factorization through Q; carrier, bridge,\n"
             "                             Gram, dagger, transpose, QCarrier equality,\n"
             "                             effects, MatterData schema, write map, domain, and\n"
             "                             complete dependencies remain open; linear, binary,\n"
             "                             reconstruction, and post-state instrument claims\n"
             "                             are outside this row")
apparatus_entry = ("  QDD-INSTRUMENT-APPARATUS   the physical instrument family {K_a} with\n"
                   "                             E_a = K_a^sharp K_a realizing the frozen ordered\n"
                   "                             effect pair as physical effects; apparatus\n"
                   "                             carrier, ready state, coupling, pointer,\n"
                   "                             reduction, occurrence law, sampling and\n"
                   "                             post-state remain open; fills no completion\n"
                   "                             contract field")
assert text.count(qdd_entry) == 1
text = text.replace(qdd_entry, qdd_entry + "\n" + apparatus_entry)
(canon / "CANON.md").write_text(text, encoding="utf-8")

# ------------------------------------------------------------------ 2. definitions and claims
defs = ["DEF-QDD-DOMAIN-K0", "DEF-QDD-BALANCED-PISTON", "DEF-QDD-AMPLITUDE-B0", "DEF-QDD-COEFFICIENT-Q",
        "DEF-QDD-TRACE-PAIRING", "DEF-QDD-GRAM", "DEF-QDD-DAGGER", "DEF-QDD-TRANSPOSE", "DEF-QDD-QPAIR",
        "DEF-QDD-QCARRIER-EQUALITY", "DEF-QDD-LOW-LINE", "DEF-QDD-PROJECTOR-LOW", "DEF-QDD-PROJECTOR-HIGH",
        "DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-MATTER-RECORD", "DEF-QDD-DIRECT-WRITE", "DEF-QDD-FACTOR-MAP"]

S = {}
S["QDD-ALGEBRAIC-FACTORIZATION"] = ("T", "L1", BUNDLE,
 "the owner-adopted Route A dictionary on the finite balanced piston carrier: the direct cyclotomic write D_QDD_direct = R_cyc o iota_B0 o beta_QDD equals the factor route F_QDD o Q_QDD o beta_QDD field by field on all 15625 checkpoints; the tagged record is total with exactly 25 ZERO_SUPPORT heads and no division on the zero branch, exactly normalized on the 15600 supported heads (w_low + w_high = m and the normalized pair sums to 1, nonnegative weights, m > 0), independent of q and r and dependent on each piston coordinate, constant on each of the 313 Q_QDD-fibres (one of size 25 and 312 of size 50) and injective on QCarrier_QDD; the direct write and its definitional closure in the dependency ledger name neither Q_QDD, the Gram, the dagger or transpose slots, the effect pair, the Born pairing nor F_QDD, per the EFFECT_SHADOW_MINIMAL independence firewall and section 6 of the DICTIONARY-DIRECT amendment, with the transitive closure enforced by the status-separation witness; negative controls: the rational-line reading Q.1 in place of the LOW LINE mismatches on 480 of 625 pistons and omitting G on 540 of 625; an exact identity of the adopted definitions confirmed on the complete finite domain, not an independent readout, not a physical selection, not a decoder-completion, totality-of-D_matter or uniqueness claim, and no completion-contract field is filled by this row",
 "fires if any field of D_QDD_direct and F_QDD o Q_QDD o beta_QDD differs on one checkpoint, if one supported head violates w_low + w_high = m or a normalized pair not summing to 1 or has a negative weight, if a Q_QDD-fibre carries two records, if two fibres carry one record, if the record depends on q or r, or if the direct write acquires a direct or transitive dependency on Q_QDD, the Gram, the projectors, the Born pairing or the factor map")
S["QDD-PROJECTOR-PAIR-TR4"] = ("T", "L1", BUNDLE,
 "on Q^4 with G = I_4 - (1/5) 1 1^T: E_low = (1/4) 1 1^T is the unique G-self-adjoint idempotent with kernel ker Tr_4 = {v : sum v_i = 0}, because a G-self-adjoint idempotent has image (ker)^perp_G and G^-1 1 = 5 1 gives (ker Tr_4)^perp_G = span(1); hence {E_low, E_high = I_4 - E_low} is the G-orthogonal resolution of Q^4 along the piston character Tr_4, both are G-self-adjoint idempotents with E_low E_high = 0 and E_low + E_high = I_4, and im(E_high) = ker Tr_4; under iota_B0 the image line of E_low is the LOW LINE Q lambda_B with lambda_B = 1 + zeta + zeta^2 + zeta^3 = -zeta^4, not the rational line and not the trace kernel of K; closed forms m = |v|^2 - s^2/5, w_low = s^2/20, w_high = |v|^2 - s^2/4 with s = sum v_i, so w_low and w_high are the squared trace-pairing lengths of the projections onto span(1) and onto ker Tr_4; linear algebra only, no apparatus, no physical reading, and no uniqueness-from-J: the theorem identifies the pair inside the stated algebraic class and does not force the choice of that class",
 "fires if a G-self-adjoint idempotent other than E_low has kernel ker Tr_4, if G^-1 1 differs from 5 1, if any displayed completeness identity or closed form fails on one piston, or if iota_B0(1,1,1,1) differs from -zeta^4")
S["QDD-QCARRIER-DIAGONAL-BOUNDARY"] = ("T", "L1", BUNDLE,
 "on the frozen carrier V_eff = ell(F_5)^4 the two typed slots of Q_QDD(v) = (A_dagger, A_T) coincide, A_dagger = A_T = v v^T, because the dagger of DEF-QDD-DAGGER is the transpose over Q; both slots remain typed and declared, the frozen domain does not test their difference, and no physical central phase is derived from this equality; the cyclotomic pair (w sigma_4(w), w^2) with w = iota_B0(v) has 90 distinct Hermitian slots and 313 distinct pairs on the 625 pistons, and 80 Hermitian slots carry more than one record, so neither a Herm-only reading nor a use of both slots is asserted for the frozen record; diagnostic only, no new field, no L6 claim",
 "fires if A_dagger differs from A_T on one piston of V_eff, or if the counts 90, 313 and 80 differ under the frozen definitions")
S["QDD-INSTRUMENT-APPARATUS"] = ("O", "MULTI", "inline",
 "the physical instrument family {K_a} with E_a = K_a^sharp K_a in the frozen Gram form realizing the frozen ordered pair (E_low, E_high) of DEF-QDD-PROJECTOR-LOW and DEF-QDD-PROJECTOR-HIGH as physical effects, from a public apparatus carrier, ready state, coupling, pointer and reduction, together with the occurrence law, sampling, post-state and completeness of the physically admissible class; registered separately from QUADRATIC-DECODER-DATA and filling no field of the decoder completion contract, per the EFFECT_SHADOW_MINIMAL owner freeze; the reverse inference from effects to instruments is forbidden and equality of effects does not identify post-state instruments",
 "STOP until the apparatus carrier, ready state, coupling, pointer, reduction to K_a, the K-level and E-level equivalence relations, occurrence law and completeness statement are public; closes positively when an exhibited public instrument family realizes E_low and E_high exactly with a complete acyclic dependency graph and no new free dimensionless input; closes negatively if every admissible family violates a registered input or fails to reproduce the frozen ordered effect pair")

typ = {"T": "THEOREM", "O": "OBLIGATION"}
norm_rows = [[d, "DEFINITION", "", "", "L1", "", src] for d in defs]
for cid, (st, layer, loc, scope, fals) in S.items():
    norm_rows.append([cid, typ[st], cid, st, layer, "", src])
append_rows(canon / "NORMATIVE.tsv", norm_rows)

reg_rows, ev_rows, hist_rows = [], [], []
for cid, (st, layer, loc, scope, fals) in S.items():
    reg_rows.append([cid, st, scope, "2. Time, space, and the decoder", loc, fals])
    if loc == "inline":
        ev_rows.append([cid, f"EV-{cid}", "INLINE_CANON", "inline", sha(scope), "registry-scope-sha256-v1", "none"])
        evsha = sha(scope)
    else:
        ev_rows.append([cid, f"EV-{cid}", "REPRODUCTION", loc, BUNDLE_SHA, "bundle-manifest-sha256-v1", "two-architecture"])
        evsha = BUNDLE_SHA
    hist_rows.append([f"CANON48-DECLARE-{cid}", "1", DATE, RELEASE, cid, "DECLARE", "-", st, sha(scope), f"EV-{cid}", loc, evsha,
                      "QDD Route A conservative insertion: declared from the merged DICTIONARY-DIRECT owner amendment, the EFFECT_SHADOW_MINIMAL owner freeze and the owner audit of 2026-08-15; effect_ids stays UNRESOLVED, the effects obligation stays open, QUADRATIC-DECODER-DATA stays O and is not modified by this fold"])
append_rows(canon / "REGISTRY.tsv", reg_rows)
append_rows(canon / "EVIDENCE.tsv", ev_rows)
append_rows(canon / "HISTORY.tsv", hist_rows)

# ------------------------------------------------------------------ 3. FRONTIER_PROGRAMS: add the apparatus row, QDD row untouched
def read_rows(path):
    with open(path, encoding="utf-8", newline="") as f:
        return [line.rstrip("\n").split("\t") for line in f]
def write_rows(path, rows):
    with open(path, "w", encoding="utf-8", newline="") as f:
        for r in rows: f.write("\t".join(r) + "\n")
fp = read_rows(canon / "FRONTIER_PROGRAMS.tsv")
head, body = fp[0], fp[1:]
assert any(r[0] == "QUADRATIC-DECODER-DATA" for r in body), "QDD program row must stay"
body.append(["QDD-INSTRUMENT-APPARATUS", "DECODER_CORE", "FOLLOWUP", "STOP", "FORMAL"])
body.sort(key=lambda r: r[0])
write_rows(canon / "FRONTIER_PROGRAMS.tsv", [head] + body)

# ------------------------------------------------------------------ 4. DEPENDENCIES (no edge touches QUADRATIC-DECODER-DATA)
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
D("DEF-QDD-MATTER-RECORD", "DEF-QDD-COEFFICIENT-Q", "the field types are stated over the declared coefficient data; a typing source only, no computation rule")
D("DEF-QDD-DIRECT-WRITE", "DEF-QDD-AMPLITUDE-B0", "the direct write reads iota_B0 o beta_QDD")
D("DEF-QDD-DIRECT-WRITE", "DEF-QDD-TRACE-PAIRING", "m_tr, the projections and MATRIX_B0 are trace pairings")
D("DEF-QDD-DIRECT-WRITE", "DEF-QDD-LOW-LINE", "the direct write projects onto Q lambda_B")
D("DEF-QDD-DIRECT-WRITE", "DEF-QDD-MATTER-RECORD", "the direct write emits the record; the record is a pure type schema")
D("DEF-QDD-FACTOR-MAP", "DEF-QDD-QCARRIER-EQUALITY", "F_QDD is defined on QCarrier_QDD with its equality")
D("DEF-QDD-FACTOR-MAP", "DEF-QDD-BRANCH-WEIGHT-PAIRING", "F_QDD uses the Gram/projector formulas")
D("DEF-QDD-FACTOR-MAP", "DEF-QDD-MATTER-RECORD", "F_QDD emits the record")
D("QDD-ALGEBRAIC-FACTORIZATION", "DEF-QDD-DIRECT-WRITE", "left side of the identity")
D("QDD-ALGEBRAIC-FACTORIZATION", "DEF-QDD-FACTOR-MAP", "right side of the identity")
D("QDD-ALGEBRAIC-FACTORIZATION", "DEF-QDD-QPAIR", "the fibres are the Q_QDD fibres")
D("QDD-PROJECTOR-PAIR-TR4", "DEF-QDD-GRAM", "self-adjointness and orthogonality are taken with respect to G")
D("QDD-PROJECTOR-PAIR-TR4", "DEF-QDD-PROJECTOR-LOW", "the projector whose uniqueness is stated")
D("QDD-PROJECTOR-PAIR-TR4", "DEF-QDD-PROJECTOR-HIGH", "the complementary projector")
D("QDD-PROJECTOR-PAIR-TR4", "DEF-QDD-LOW-LINE", "the cyclotomic image of the projector line")
D("QDD-PROJECTOR-PAIR-TR4", "CODEC-TR4", "Tr_4 is the registered piston character whose kernel is the stated kernel; a mathematical identity, not a physical inheritance")
D("QDD-QCARRIER-DIAGONAL-BOUNDARY", "DEF-QDD-QPAIR", "the two typed slots whose coincidence on V_eff is stated")
D("QDD-QCARRIER-DIAGONAL-BOUNDARY", "DEF-QDD-DAGGER", "the dagger is the transpose over Q on the frozen carrier")
D("QDD-QCARRIER-DIAGONAL-BOUNDARY", "DEF-QDD-TRANSPOSE", "the second slot")
D("QDD-INSTRUMENT-APPARATUS", "DEF-QDD-PROJECTOR-LOW", "the instrument family must realize the frozen E_low exactly")
D("QDD-INSTRUMENT-APPARATUS", "DEF-QDD-PROJECTOR-HIGH", "the instrument family must realize the frozen E_high exactly")
D("QDD-INSTRUMENT-APPARATUS", "DEF-QDD-GRAM", "E_a = K_a^sharp K_a is taken in the frozen Gram form")
# transitive independence firewall of the direct write (DICTIONARY-DIRECT section 6)
fw_requires = {}
for a, b, rel, basis in dep:
    fw_requires.setdefault(a, set()).add(b)
fw_seen, fw_stack = set(), ["DEF-QDD-DIRECT-WRITE"]
while fw_stack:
    cur = fw_stack.pop()
    for nxt in fw_requires.get(cur, ()):
        if nxt not in fw_seen:
            fw_seen.add(nxt); fw_stack.append(nxt)
FW_ALLOWED = {"DEF-QDD-DOMAIN-K0", "DEF-QDD-BALANCED-PISTON", "DEF-QDD-AMPLITUDE-B0",
              "DEF-QDD-COEFFICIENT-Q", "DEF-QDD-TRACE-PAIRING", "DEF-QDD-LOW-LINE",
              "DEF-QDD-MATTER-RECORD"}
FW_FORBIDDEN = {"DEF-QDD-GRAM", "DEF-QDD-DAGGER", "DEF-QDD-TRANSPOSE", "DEF-QDD-QPAIR",
                "DEF-QDD-QCARRIER-EQUALITY", "DEF-QDD-PROJECTOR-LOW", "DEF-QDD-PROJECTOR-HIGH",
                "DEF-QDD-BRANCH-WEIGHT-PAIRING", "DEF-QDD-FACTOR-MAP"}
fw_qdd = {x for x in fw_seen if x.startswith("DEF-QDD-") or x.startswith("QDD-")}
if fw_qdd != FW_ALLOWED or (fw_seen & FW_FORBIDDEN):
    sys.exit(f"direct-write firewall violated: closure {sorted(fw_qdd)} forbidden hits {sorted(fw_seen & FW_FORBIDDEN)}")
print(f"direct-write firewall closure OK: {len(fw_seen)} items, no factor-side object")

append_rows(canon / "DEPENDENCIES.tsv", dep)

print(f"delta applied: {len(defs)} definitions, {len(S)} new claims (3 T, 1 O), 0 gates, QUADRATIC-DECODER-DATA untouched, {len(dep)} dependency rows, bundle sha {BUNDLE_SHA}")

# ------------------------------------------------------------------ 5. witness, views and checks, all fail-closed
def must(argv, label):
    r = subprocess.run(argv, cwd=ROOT, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    print(f"[{label}] " + ((out.splitlines() or ["(no output)"]))[-1])
    if r.returncode != 0:
        print(out[-2000:])
        sys.exit(f"delta step failed: {label}")

must([sys.executable, str(Path(__file__).with_name("update_status_separation_witness.py")), str(ROOT)], "status-separation witness")
must([sys.executable, "tools/generate_canon_views.py", "--apply"], "generate_canon_views --apply")
# check_canon runs in the finalizer, decisively, after SHA256SUMS regeneration
for tool in ("check_ledger.py", "check_status_labels.py"):
    must([sys.executable, f"tools/{tool}"], tool)
