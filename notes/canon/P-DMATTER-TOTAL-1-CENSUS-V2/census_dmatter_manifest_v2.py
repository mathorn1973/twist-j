#!/usr/bin/env python3
# census_dmatter_manifest_v2.py
# Census v2 of the P-DMATTER-TOTAL-1 completion-manifest skeleton:
# pairing and classification. Mechanical, no mathematics. RECON grade,
# single platform, deterministic stdout, stdlib only.
#
# Inputs (pinned):
#   notes/canon/P-DMATTER-TOTAL-1-COMPLETION-MANIFEST-SKELETON.json
#     sha256 b19e0737... (unchanged since census v1; still pinned at v23)
#   notes/canon/P-DMATTER-TOTAL-1-EFFECT-SHADOW-MINIMAL-OWNER-FREEZE.md
#     (owner freeze of 2026-08-04, PR #272, base v36)
#
# Classes for UNRESOLVED slots:
#   S-BIND    binding and publication of an already-displayed local
#             object (includes the v36 rebuild of stale local typing)
#   S-NAME    a pure naming act (candidate_id)
#   S-MECH    resolved mechanically at pin time (public_pin_id)
#   S-EVAL    obligation evaluation after the rebuild
#   S-AFTER   session derivation gated by a named dependency
#   S-DERIVE  session derivation with real missing content
#   OWNER     a genuine owner choice or freeze
#   O-FROZEN  owner choice ALREADY frozen by the 2026-08-04 note;
#             slot fill is now binding against that freeze
import hashlib, json, sys

SKEL = "notes/canon/P-DMATTER-TOTAL-1-COMPLETION-MANIFEST-SKELETON.json"
raw = open(SKEL, "rb").read()
print("skeleton sha256", hashlib.sha256(raw).hexdigest(), len(raw), "B")
d = json.loads(raw)
cm = d["contract_manifest"]

def unres(v):
    if isinstance(v, str):
        return v == "UNRESOLVED"
    if isinstance(v, list):
        return len(v) > 0 and all(x == "UNRESOLVED" for x in v)
    return False

def slots(x, path=""):
    out = []
    if isinstance(x, dict):
        for k in sorted(x):
            if k.startswith("_"):
                continue
            out += slots(x[k], path + "/" + k)
    elif isinstance(x, list) and x and isinstance(x[0], dict):
        for i, v in enumerate(x):
            key = v.get("_row_key", str(i))
            out += slots(v, path + ":" + str(key))
    else:
        out.append((path, x))
    return out

S = slots(cm)
U = [p for p, v in S if unres(v)]
C = [p for p, v in S if not unres(v)]
print("v1 cross-check: slots=%d carried=%d unresolved=%d (v1: 242/38/204)"
      % (len(S), len(C), len(U)))
assert (len(S), len(C), len(U)) == (242, 38, 204), "v1 cross-check failed"

# pairing: unresolved slot -> displayed local object (proposal_local_catalog)
PAIR = {
    "/read_convention_id": "identity_values/read_convention = PRE_UPDATE_CHECKPOINT_N0",
    "/history_equivalence_id": "identity_values/history_equivalence",
    "/region_id": "identity_values/region = ORDERED_PISTON4_N0",
    "/coarse_graining_id": "identity_values/coarse_graining = IDENTITY_N0",
    "/quadratic_manifest/coefficient_ring_id": "operation_values/coefficient_ring = Q",
    "/quadratic_manifest/effective_carrier_id": "carrier_values/Veff",
    "/quadratic_manifest/orbit_to_amplitude_bridge_id": "map_values/iota_B0 o beta",
    "/quadratic_manifest/gram_id": "operation_values/G = I_4-(1/5)*1*1^T",
    "/quadratic_manifest/dagger_id": "operation_values/dagger",
    "/quadratic_manifest/transpose_id": "operation_values/transpose",
    "/quadratic_manifest/qcarrier_id": "carrier_values/QCarrier",
    "/quadratic_manifest/q_equality_id": "map_values/definition_audit_identity",
    "/quadratic_manifest/q_map_id": "map_values/Qcan",
}
for ck in ("X", "K0", "Veff", "V_lin", "K_amp", "QCarrier",
           "CandidateQuadraticData"):
    PAIR["/carrier_manifest:%s/carrier_id" % ck] = "carrier_values/%s" % ck
for rf in ("support_state", "total_weight", "branch_weights",
           "density_state", "normalized_weight_state"):
    PAIR["/record_field_manifest:%s/write_map_id" % rf] = "map_values/D_scoped"
for b, m in (("beta", "map_values/beta"), ("iota_B0", "map_values/iota_B0"),
             ("D_scoped_record", "map_values/D_scoped")):
    PAIR["/bridge_manifest:%s/map_id" % b] = m

# classification rules, most specific first
def classify(p):
    if p == "/candidate_id":
        return "S-NAME", "naming act under lane conventions"
    if p == "/public_pin_id":
        return "S-MECH", "assigned by the future public pin itself"
    if p in ("/quadratic_manifest/effect_ids",
             "/quadratic_manifest/born_pairing_id"):
        return "O-FROZEN", "EFFECT_SHADOW_MINIMAL owner freeze 2026-08-04 " \
                           "(E_low=(1/4)11^T, E_high=I-E_low, Born trace " \
                           "pairing); skeleton not yet updated"
    if p == "/quadratic_manifest/factorization_map_id":
        return "S-DERIVE", "F_Gram displayed but declared NOT an " \
                           "independent factorization; the direct-write " \
                           "treatment is gated by settled ruling 9.2"
    if p.startswith("/bridge_manifest:") and (
            p.endswith("/from_layer") or p.endswith("/to_layer")
            or p.endswith("/gate_ids")):
        return "OWNER", "OD2 residue: layer_state and gate_state left " \
                        "UNRESOLVED by the owner ruling; layer typing " \
                        "needs its own named owner declaration"
    if p == "/measure_manifest/measure_id":
        return "OWNER", "TM-SYM2-PHYSICAL-MEASURE is the one owner-STOP: " \
                        "successor L5 source must be owner-approved"
    if p == "/measure_manifest/scheme_id":
        return "OWNER", "SCHEME-DICTIONARY requires a NAMED measurement " \
                        "scheme; naming it is an owner act"
    if p == "/measure_manifest/metrology_id":
        return "S-AFTER", "gated by METRO-REDUCTION-CALCULUS (B, D, E)"
    if p == "/measure_manifest/normalization_id":
        return "S-AFTER", "gated by measure_id"
    if p == "/physics_manifest/source_id":
        return "OWNER", "TT-SOURCE: the public source object must be " \
                        "chosen and defined; a session can draft, the " \
                        "choice is the owner's"
    if p == "/physics_manifest/detector_id":
        return "OWNER", "detector model choice; OD4 kept the instrument " \
                        "UNRESOLVED and requires separate predefinition"
    if p.startswith("/physics_manifest/"):
        return "S-AFTER", "derivable once source_id is frozen"
    if p == "/closure_manifest/terminality_basis_id":
        return "S-AFTER", "gated by the OBSERVER-WRITE-PORT dependency " \
                          "subtree (METRO cluster plus QDD)"
    if p.startswith("/obligation_manifest:") and p.endswith("/value_state"):
        return "S-EVAL", "evaluation after the v36 rebuild of the " \
                         "binding package (STALE_BASE per the freeze note)"
    return "S-BIND", "displayed or stale-local object; publication and " \
                     "v36 rebuild debt"

counts, by_block, owner_slots, pairs_used = {}, {}, [], 0
for p in U:
    cls, why = classify(p)
    counts[cls] = counts.get(cls, 0) + 1
    blk = p.split("/")[1].split(":")[0]
    by_block.setdefault(blk, {}).setdefault(cls, 0)
    by_block[blk][cls] += 1
    if cls == "OWNER":
        owner_slots.append(p)
    if p in PAIR:
        pairs_used += 1

print("")
print("classification of the 204 UNRESOLVED slots:")
for cls in sorted(counts):
    print("  %-8s %3d" % (cls, counts[cls]))
total = sum(counts.values())
print("  TOTAL    %3d" % total)
assert total == 204

print("")
print("per block (block: class=count):")
for blk in sorted(by_block):
    inner = " ".join("%s=%d" % (c, n) for c, n in sorted(by_block[blk].items()))
    print("  %-24s %s" % (blk, inner))

print("")
print("explicit pairings applied: %d slots carry a displayed catalog value"
      % pairs_used)
print("")
print("OWNER slots (%d):" % len(owner_slots))
for p in sorted(owner_slots):
    print("  " + p)
print("")
print("owner DECISIONS behind the %d owner slots:" % len(owner_slots))
print("  D1 layer typing and gates of the three record bridges (9 slots,")
print("     one declaration; OD2 residue)")
print("  D2 measure_id: approve a successor L5 source (TM-SYM2 owner-STOP)")
print("  D3 scheme_id: name the measurement scheme (SCHEME-DICTIONARY)")
print("  D4 source_id: choose and define the public source object (TT-SOURCE)")
print("  D5 detector_id: instrument choice (OD4: separate predefinition)")
print("")
print("named missing objects OUTSIDE the 204 slots (catalog-level):")
print("  D_direct_state UNRESOLVED (the direct write; ruling 9.2 governs)")
print("  required_dependency_delta ledger edge QDD REQUIRES")
print("    DEF-DECODER-COMPLETION-CONTRACT: ledger_state UNRESOLVED (a fold act)")
print("  stream_extension, hybrid_extension: UNRESOLVED by design (OD2, OD3")
print("    open boundaries, outside the core scope)")
print("")
print("rebase state: skeleton declares pin Public Canon v23; head is v36;")
print("the factor-canonicity overlay (added v24) is still absent; the four")
print("local binding artifacts are STALE_BASE per the 2026-08-04 freeze and")
print("need a rebuild on v36 before any S-EVAL slot can be filled.")
print("CENSUS-V2 COMPLETE")
sys.exit(0)
