# P-DMATTER-TOTAL-1 census v2: pairing and classification (NON-CANONICAL)

```text
STATUS      NON-CANONICAL audit note. Mechanical, no mathematics, single
            platform, deterministic stdout. No claim, no status move, no
            normative edit. Follows census v1 of 2026-08-01 (project-side
            provenance; its counts are re-verified here from the pinned
            skeleton directly).
PUBLIC BASE Public Canon v36, main head 470d958 (merge PR #272).
SKELETON    notes/canon/P-DMATTER-TOTAL-1-COMPLETION-MANIFEST-SKELETON.json
            sha256 b19e073743fde8a71a18a9394c2c1bf71289ef515d626787ac290f6cfd57aa86
            (unchanged since census v1; still declares pin Public Canon v23)
NEW INPUT   notes/canon/P-DMATTER-TOTAL-1-EFFECT-SHADOW-MINIMAL-OWNER-FREEZE.md
            (owner freeze of 2026-08-04, PR #272)
FILES       census_dmatter_manifest_v2.py
            sha256 ccff30e9511764c4446406dde6cc8dd68a9bb993c68185a145f99e4ee05a0cb2
            census_dmatter_manifest_v2.stdout.txt
            sha256 5a04bb683bfe2343b4bccd2b85784d4a32c9483272c07d6a45ac6008b79c06ed
RUN         from repository root,
            LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
            python3 notes/canon/P-DMATTER-TOTAL-1-CENSUS-V2/census_dmatter_manifest_v2.py
```

## What v2 adds over v1

Census v1 counted the contract slots: 242 total, 38 carried, 204
UNRESOLVED (rule: leaf values of `contract_manifest`, underscore keys
excluded, UNRESOLVED literal or all-UNRESOLVED list). Census v2 pairs
each UNRESOLVED slot with a displayed value of `proposal_local_catalog`
where one exists, and classifies every one of the 204 into exactly one
class. The classification is judgment written as explicit rules in the
script; the machine guarantees coverage (204 of 204) and arithmetic. To
refute the census, point at a rule and the row text it contradicts.

## Result

```text
class      slots
O-FROZEN       2   effect_ids, born_pairing_id: decided by the
                   EFFECT_SHADOW_MINIMAL owner freeze of 2026-08-04;
                   the skeleton does not carry it yet (binding remains)
OWNER         13   genuine owner choices, see the decision list
S-AFTER        6   session derivations gated by a named dependency
                   (metrology after the METRO calculus, normalization
                   after measure_id, three physics ids after source_id,
                   terminality after the OWP dependency subtree)
S-BIND       165   binding and publication of already-displayed or
                   stale-local material (includes the v36 rebuild)
S-DERIVE       1   factorization_map_id (declared NOT an independent
                   factorization; governed by settled ruling 9.2)
S-EVAL        15   obligation value_states, after the rebuild
S-MECH         1   public_pin_id (resolved by the future pin itself)
S-NAME         1   candidate_id (naming act)
TOTAL        204
```

28 slots carry a directly displayed catalog value (X, K0, Veff, V_lin,
K_amp, QCarrier, CandidateQuadraticData, G, Q, dagger, transpose, Qcan,
iota_B0, beta, D_scoped, and the four identity values).

## The one number

Between the skeleton and a fillable manifest stand 13 owner slots,
composing FIVE owner decisions:

```text
D1  layer typing and gates of the three record bridges (beta, iota_B0,
    D_scoped_record): 9 slots, one declaration; the OD2 residue
    (layer_state, gate_state left UNRESOLVED by the ruling)
D2  measure_id: approve a successor L5 source
    (TM-SYM2-PHYSICAL-MEASURE, the one owner-STOP of the frontier)
D3  scheme_id: name the measurement scheme (SCHEME-DICTIONARY)
D4  source_id: choose and define the public source object (TT-SOURCE;
    a session can draft, the choice is the owner's)
D5  detector_id: instrument choice (OD4 requires separate
    predefinition)
```

Everything else in the 204 is session work. The D_matter corner's debt
is not missing mathematics; it is 81 percent binding and publication,
and its choices are counted: five. Whether each of the five is a real
modulus (NONUNIQUE), forced (UNIQUE), or empty is for later theorems;
the census gives the list, the moduli program gives the classification.

## Named missing objects OUTSIDE the 204 slots

```text
D_direct_state UNRESOLVED        the direct write; ruling 9.2 governs
QDD REQUIRES                     the DEF-DECODER-COMPLETION-CONTRACT
                                 dependency edge: ledger_state
                                 UNRESOLVED; a fold act
stream_extension, hybrid_extension   open boundaries of OD2 and OD3,
                                 outside the core scope by design
```

## Rebase state

The skeleton still declares pin Public Canon v23; the head is v36; the
factor-canonicity overlay (added at v24) is absent; the four local
binding artifacts are STALE_BASE per the 2026-08-04 freeze note and
need a rebuild on v36 before any S-EVAL slot can be filled. A
mechanical v36 rebase PROPOSAL accompanies this census (see
P-DMATTER-TOTAL-1-COMPLETION-MANIFEST-SKELETON-V36-REBASE-PROPOSAL.json
and the builder in this directory); it is additive and does not touch
the pinned original.

## Falsifier

Wrong if a re-run of the pinned script over the pinned skeleton gives
different counts; if any quoted pin disagrees with the head; if a
classification rule contradicts the text of its owning row (then the
rule is corrected, the census recomputed, and the correction recorded);
or if the freeze note does not say what the O-FROZEN class claims.
