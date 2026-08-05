#!/usr/bin/env python3
# build_skeleton_v36_proposal.py
# Census v2 follow-up, consumption item 1: a MECHANICAL v36 rebase
# PROPOSAL for the P-DMATTER-TOTAL-1 completion-manifest skeleton.
# Additive: writes a NEW file, does not touch the pinned original.
# Documented deltas, and nothing else:
#   R1  pin block: v23 references replaced by the v36 pins
#   R2  factor-canonicity overlay added (v24 contract extension),
#       all slots UNRESOLVED, gauge_square_manifest empty until a
#       square is declared
#   R3  effect_ids and born_pairing_id bound to the 2026-08-04
#       EFFECT_SHADOW_MINIMAL owner freeze (proposal-local ids;
#       proposal_local_ids_are_public_ids stays false)
#   R4  a top-level _rebase_note (underscore key, not a slot)
# The script prints every delta and the before/after census counts.
import hashlib, json, sys

SRC = "notes/canon/P-DMATTER-TOTAL-1-COMPLETION-MANIFEST-SKELETON.json"
DST = "notes/canon/P-DMATTER-TOTAL-1-COMPLETION-MANIFEST-SKELETON-V36-REBASE-PROPOSAL.json"
V36 = {
    "public_canon": "Public Canon v36",
    "content_commit": "df64035f6f0cadbeb17f539eaeec5d8d0f444515",
    "canon_sha256": "c8f50d0ce4686d7eedc11599a95debee15c71a2cf13c52c93c3f0605890fa2d5",
    "canon_bytes": 175814,
    "base_head": "470d95826037d75e29530177171763f1376b4614",
}
raw = open(SRC, "rb").read()
print("source sha256", hashlib.sha256(raw).hexdigest())
d = json.loads(raw)

deltas = []

# R1: replace any string leaf mentioning v23 pins inside authority/status
def walk_replace(node, path):
    if isinstance(node, dict):
        for k in list(node):
            v = node[k]
            if isinstance(v, (dict, list)):
                walk_replace(v, path + "/" + k)
            elif isinstance(v, str) and ("v23" in v or "canon-v23" in v):
                node[k] = v.replace("canon-v23", "canon-v36").replace(
                    "v23", "v36")
                deltas.append("R1 %s/%s: %r -> %r" % (path, k, v, node[k]))
for blk in ("authority", "status", "skeleton_format", "manifest_scope"):
    if blk in d:
        walk_replace(d[blk], "/" + blk)
if "authority" in d and isinstance(d["authority"], dict):
    for k, v in V36.items():
        old = d["authority"].get(k)
        if old != v:
            d["authority"][k] = v
            deltas.append("R1 /authority/%s: %r -> %r" % (k, old, v))

# R2: overlay
FC = ["owner_item_id", "stage_id", "leg_id", "source_carrier_id",
      "output_carrier_id", "domain_id", "totality_domain_id",
      "source_equality_id", "output_equality_id", "qcarrier_id",
      "q_equality_id", "q_map_id", "q_image_id", "q_corestriction_id",
      "q_image_inclusion_id", "factor_map_id", "factor_equation_id",
      "fiber_constancy_test_id", "fiber_factor_equivalence_statement_id",
      "fiber_factor_equivalence_proof_id", "nonconstancy_test_id",
      "candidate_class_id", "candidate_membership_test_id",
      "candidate_equivalence_id",
      "candidate_equivalence_reflexivity_proof_id",
      "candidate_equivalence_symmetry_proof_id",
      "candidate_equivalence_transitivity_proof_id",
      "candidate_isomorphism_closure_proof_id",
      "candidate_completeness_statement_id",
      "candidate_completeness_proof_id", "hidden_input_closure_id"]
cm = d["contract_manifest"]
if "factor_canonicity_manifest" not in cm:
    cm["factor_canonicity_manifest"] = {k: "UNRESOLVED" for k in FC}
    cm["gauge_square_manifest"] = []
    cm["_overlay_note"] = ("factor-canonicity overlay per the v24 contract "
                           "extension, carried by Public Canon v36; all "
                           "slots UNRESOLVED; gauge_square_manifest rows "
                           "are added when a square is declared")
    deltas.append("R2 overlay added: factor_canonicity_manifest with %d "
                  "UNRESOLVED slots, empty gauge_square_manifest" % len(FC))

# R3: bind the two owner-frozen slots
qm = cm["quadratic_manifest"]
FREEZE = "P-DMATTER-TOTAL-1-EFFECT-SHADOW-MINIMAL-OWNER-FREEZE-2026-08-04"
old_e, old_b = qm.get("effect_ids"), qm.get("born_pairing_id")
qm["effect_ids"] = [FREEZE + ":E_low", FREEZE + ":E_high"]
qm["born_pairing_id"] = FREEZE + ":BORN-TRACE-PAIRING"
deltas.append("R3 effect_ids: %r -> %r" % (old_e, qm["effect_ids"]))
deltas.append("R3 born_pairing_id: %r -> %r" % (old_b, qm["born_pairing_id"]))

# R4: note
d["_rebase_note"] = (
    "V36 REBASE PROPOSAL, mechanical, produced by the census v2 lane on "
    "2026-08-05. Additive: the pinned v23 skeleton is unchanged and stays "
    "the file of record until the lane owner adopts this proposal. Deltas "
    "are exactly R1 pins, R2 overlay, R3 the two EFFECT_SHADOW_MINIMAL "
    "bindings, R4 this note. No other slot was touched; the local binding "
    "artifacts remain STALE_BASE per the freeze note and are NOT rebuilt "
    "here.")
deltas.append("R4 _rebase_note added (underscore key, not a slot)")

# census before/after
def unres(v):
    if isinstance(v, str):
        return v == "UNRESOLVED"
    if isinstance(v, list):
        return len(v) > 0 and all(x == "UNRESOLVED" for x in v)
    return False
def slots(x):
    out = []
    if isinstance(x, dict):
        for k in sorted(x):
            if k.startswith("_"):
                continue
            out += slots(x[k])
    elif isinstance(x, list) and x and isinstance(x[0], dict):
        for v in x:
            out += slots(v)
    else:
        out.append(x)
    return out
orig = json.loads(raw)
S0 = slots(orig["contract_manifest"])
S1 = slots(cm)
print("census before: slots=%d carried=%d unresolved=%d"
      % (len(S0), sum(1 for v in S0 if not unres(v)),
         sum(1 for v in S0 if unres(v))))
print("census after:  slots=%d carried=%d unresolved=%d"
      % (len(S1), sum(1 for v in S1 if not unres(v)),
         sum(1 for v in S1 if unres(v))))
# accounting: +31 UNRESOLVED overlay slots; +2 carried (the two R3
# bindings); +1 carried leaf for the empty gauge_square_manifest list
# (the census leaf rule counts an empty list as one carried leaf)
exp = (len(S0) + 31 + 1, sum(1 for v in S0 if not unres(v)) + 2 + 1,
       sum(1 for v in S0 if unres(v)) + 31 - 2)
got = (len(S1), sum(1 for v in S1 if not unres(v)),
       sum(1 for v in S1 if unres(v)))
assert got == exp, "delta accounting failed: %s vs %s" % (got, exp)

out = json.dumps(d, indent=2, ensure_ascii=True) + "\n"
open(DST, "w").write(out)
print("proposal written:", DST)
print("proposal sha256", hashlib.sha256(out.encode()).hexdigest(),
      len(out.encode()), "B")
print("deltas (%d):" % len(deltas))
for x in deltas:
    print("  " + x)
print("BUILD OK")
sys.exit(0)
