# Decoder-completion manifest instance (diagnostic draft against Public Canon v60)

**NON-CANONICAL.** Audit-only diagnostic instrument, no authority, no Canon
change, no file under `canon/` touched. Per `canon/CANON.md` 634-645 a
submitted candidate is not evidence and cannot change a public status.
Paths of the form `C:/j/twist-j-manifest/...` refer to the author's local
working area and are not part of this repository.

## 0. Header — status of this document

**UNOFFICIAL INDEPENDENT DRAFT.** This document instantiates the manifest schema of
`DEF-DECODER-COMPLETION-CONTRACT` (`canon/CANON.md` lines 489–645, factor-canonicity
overlay to 1090 — the overlay's closing forbidden-outputs paragraph ends at CANON.md
1090; READING-SPLIT begins at 1092) against **Public Canon v60** (tag `canon-v60`, content commit
`18b21bdaf2c2236c9444b120900277ccfb63e050`, `canon/CANON.md` SHA-256
`9387b75f2036ac6aff5737255956b93fb9b906511b8184ae4c1c999e8ed46db0`, per `STATUS.md`
lines 3–11). It is:

- **audit-only and diagnostic** — drafted as an instrument to measure the distance
  between v60 and a complete decoder, not as a submission;
- **status-neutral** — it changes no status, closes no gate, opens no probe, and
  authorizes no verifier, per the contract's own clauses: "Syntactic conformance, a
  resolved identifier, or a submitted candidate is not evidence and cannot change a
  public status" and "The contract neither opens nor authorizes a verifier or probe"
  (CANON.md 634–645);
- **non-evidential** — every property named below "remains owned by its registered
  claim and evidence, and every cross-layer lift remains owned by its public gate"
  (CANON.md 641–643). If this draft ever migrated into the repo it would belong in
  the `notes/` lane with a `NON-CANONICAL` banner (AGENTS.md 391–393).

**Reading convention for the blocks below.** Two different things can be true of a slot
and are kept separate throughout:

1. **Identifier resolution** (what this manifest reports): the slot cites a public
   identifier that resolves in v60 (a claim ID from `canon/REGISTRY.tsv`, a `DEF-*`
   item, a named map/object, or a `gate_id` from `canon/GATES.tsv`) → marked
   `RESOLVED` with the basis cited as `# basis:`. Where v60 supplies nothing, the slot
   carries the literal `UNRESOLVED` and an `obligation_manifest[]` row names the owning
   live frontier row — **except for two ownerless holes surfaced by this instance**
   (the linear/binary record- and stage-ownership holes of §3.2, and the physical
   photon propagator, §8), which **no live frontier row owns**; each is carried as an
   `obligation_manifest[]` row (OB-31, OB-32) with `owning_item_id: UNRESOLVED`
   (legal for identifier slots) and is itself a primary diagnostic finding.
   `NOT_APPLICABLE` appears only with a resolvable basis item; bases are cited
   item-first, lines second — `# basis: ITEM (CANON.md nnn–nnn)` — throughout.
   Objects coined by this draft (no public v60 referent) carry **draft-local**
   identifiers defined once in the Draft-local identifier lexicon (Appendix A),
   mirroring the treatment of `candidate_id`; draft-local slots are counted
   separately in §12.1, never as `RESOLVED`. Ambient standard mathematical objects
   (see the §2 note) are cited, not declared.
2. **Canon-side adoption/closure** (what this manifest cannot report as done): citing
   a resolvable referent does **not** mean the canon has adopted it as the decoder's
   registered action. In particular, the entire QDD Route A corpus "fill[s] no
   decoder-completion-contract field" (CANON.md 1618–1619); wherever this draft cites
   DEF-QDD-* referents as candidate declarations, the adoption/closure question stays
   with `QUADRATIC-DECODER-DATA` [O] and is carried explicitly in
   `obligation_manifest[]`.

Statuses: [T] theorem, [D] dictionary, [C] computation, [H] hypothesis, [O] open,
[F] falsified — cited from `canon/REGISTRY.tsv`. Line numbers refer to
`C:/j/twist-j/canon/CANON.md` unless another file is named.

---

## 1. Top-level scalar slots

```yaml
candidate_id: DRAFT-TWISTJ-DECODER-MANIFEST-2026-08-22
  # Self-identifier of this diagnostic draft. NON-CANONICAL: resolves only to this
  # document (C:/j/twist-j-manifest/work/S2_manifest_draft.md), not to any public
  # canon item. Under a strict public-resolvability reading of CANON.md 618, a
  # would-be submitter must first give the candidate a public home.

public_pin_id: RESOLVED: canon-v60 @ 18b21bdaf2c2236c9444b120900277ccfb63e050
  # basis: STATUS.md L4-11 (STATE ACTIVE, Public Canon v60, CANON_SHA256
  # 9387b75f...46db0, 329876 bytes). Authority = public main at the declared tag
  # (AGENTS.md L17-18).

read_convention_id: RESOLVED: COIN-MINIMAL-READ [D]
  # basis: CANON.md 4500-4517 — the canon's adopted read convention (MINIMAL-READ,
  # selecting w = 1 and the beta_1 = 1/sqrt5 alternator coin).
  # NOT forced: whether the registered architecture forces this convention is the
  # open selection MINIMAL-READ-DERIVATION [O] (CANON.md 4519-4530) behind
  # GATE-L5-L1-MINIMAL-READ (OPEN_SELECTION) -> obligation row OB-14.

history_equivalence_id: literal-forward-orbit-equality
  # draft-local identifier (as candidate_id; Appendix A), grounded in CANON.md 455 +
  # DEF-QDD-DOMAIN-K0 — the name resolves only in this draft, so it is counted
  # draft-local in section 12.1, not RESOLVED.
  # basis: CANON.md L455 (K = set of forward U-orbits; equality of elements of K is
  # literal sequence equality — no coarser equivalence is registered or adopted);
  # pointed refinement on the quadratic leg: DEF-QDD-DOMAIN-K0 (CANON.md 1138-1141),
  # "equality of complete pointed forward sequences, distinguished head n = 0".
  # This candidate adopts the finest (literal) equivalence and claims nothing extra.

region_id: RESOLVED: K (CANON.md L455), with quadratic-leg subregion K_QDD
  # basis: K = forward U-orbits of Omega = N_0 x F_5^6 (CANON.md 295-313, 455);
  # K_QDD = {kappa_x = (U^n(0,x))_{n>=0} : x in F_5^6} (DEF-QDD-DOMAIN-K0,
  # 1138-1141), 15625 pointed orbits. Totality claims below are stated only
  # relative to these named domains (CANON.md 623-624).

coarse_graining_id: UNRESOLVED
  # No coarse-graining is registered or adopted in v60. The equivalence under which
  # coarse-grainings would even be comparable ("reduction equivalence") is itself the
  # open obligation METRO-REDUCTION-CALCULUS [O] -> obligation row OB-06.
```

---

## 2. carrier_manifest[]

Slots per row: `carrier_id, parent_carrier_id, inclusion_or_quotient_map_id,
equality_id, coefficient_object_id` (CANON.md 518–523).

**Ambient-objects note.** Ambient standard mathematical objects — `Z_2, Q, Q^4,
Q_{>=0}, Q_{>=0}^2, Z[zeta_8], Z[i], M_4(Q), M_4(Q) x M_4(Q), F_5, F_5^6, F_p, N_0,
{0,1}^2, {0,1}^N_0`, and the trace Gram carrier `G_p` (= p I - J_n,
TRACEKERNEL-RESIDUAL-FORM [T]) — are **cited as standard objects, not declared** by
rows of their own (explicitness per CANON.md 622–623). Every other non-public object
below carries a draft-local `dl-*` identifier defined in Appendix A.

```yaml
- carrier_id: Omega                       # Omega = N_0 x F_5^6
  parent_carrier_id: NOT_APPLICABLE       # basis: DEF-AUTONOMOUS-STATE (CANON.md
                                          # 295-313) — Omega is the declared
                                          # autonomous state, a root carrier
  inclusion_or_quotient_map_id: NOT_APPLICABLE   # basis: same (root)
  equality_id: dl-eq-omega                # draft-local (Appendix A): componentwise —
                                          # n literal in N_0, psi componentwise F_5^6
  coefficient_object_id: dl-coeff-omega   # draft-local (Appendix A): the pair
                                          # F_5 (fiber), N_0 (counter), named once
  # basis: DEF-AUTONOMOUS-STATE (CANON.md 295-313); kernel declaration 1861-1864
  # ("No derivation or uniqueness of this architecture from J or M_J is claimed").

- carrier_id: N_0                         # clock coordinate
  parent_carrier_id: Z_2
  inclusion_or_quotient_map_id: dl-map-odometer-embedding
    # draft-local (Appendix A): distinguished forward orbit 0,1,2,... of the 2-adic
    # odometer embedded in Z_2
  equality_id: dl-eq-integer              # draft-local (Appendix A): integer equality
  coefficient_object_id: NOT_APPLICABLE   # basis: DEF-AUTONOMOUS-STATE (CANON.md
                                          # 305-308; no Thue-Morse parity asserted
                                          # on all of Z_2)
  # basis: DEF-AUTONOMOUS-STATE (CANON.md 305-308); ODOMETER-INTERNALIZED [D] 315-321.

- carrier_id: F_5^6                       # checkpoint fiber
  parent_carrier_id: Omega
  inclusion_or_quotient_map_id: dl-map-pr-checkpoint
    # draft-local (Appendix A): pr_checkpoint(n, psi) = psi
  equality_id: dl-eq-f5-componentwise     # draft-local (Appendix A)
  coefficient_object_id: F_5
  # basis: CANON.md 308-310; psi alone is NOT claimed autonomous.

- carrier_id: K                           # decoder base set
  parent_carrier_id: Omega                # as orbit space
  inclusion_or_quotient_map_id: dl-map-orbit-embedding
    # draft-local (Appendix A): omega_0 -> (U^k omega_0)_{k>=0}
  equality_id: literal-forward-orbit-equality   # draft-local (Appendix A; section 1)
  coefficient_object_id: NOT_APPLICABLE   # basis: the K definition in the decoder
                                          # interface declaration (CANON.md 455; K is
                                          # a set of orbits, no coefficient structure
                                          # claimed)
  # basis: the K definition in the decoder interface declaration (CANON.md 455).

- carrier_id: K_QDD                       # pointed quadratic-leg domain
  parent_carrier_id: K
  inclusion_or_quotient_map_id: dl-map-pointed-orbit-inclusion
    # draft-local (Appendix A): inclusion of pointed orbits started at counter 0
    # (head n = 0)
  equality_id: DEF-QDD-DOMAIN-K0          # equality of complete pointed forward
                                          # sequences, defined therein
  coefficient_object_id: NOT_APPLICABLE   # basis: DEF-QDD-DOMAIN-K0 (set of orbits)
  # basis: DEF-QDD-DOMAIN-K0, CANON.md 1138-1141; 15625 orbits.

- carrier_id: V_eff                       # balanced piston carrier, ell(F_5)^4
  parent_carrier_id: Q^4
  inclusion_or_quotient_map_id: DEF-QDD-BALANCED-PISTON
    # inclusion V_eff = ell(F_5)^4 subset Q^4, balanced lift
    # ell(0,1,2,3,4) = (0,1,2,-2,-1), defined therein
  equality_id: dl-eq-q4-componentwise     # draft-local (Appendix A): componentwise
                                          # rational equality
  coefficient_object_id: Q
  # basis: DEF-QDD-BALANCED-PISTON, CANON.md 1136-1224 block (beta_QDD forbidden
  # inputs: q, r, later checkpoints, counter, environment, randomness).

- carrier_id: K_amp                       # amplitude field K = Q(zeta_5)
  parent_carrier_id: Q
  inclusion_or_quotient_map_id: dl-map-qzeta5-extension
    # draft-local (Appendix A): the field extension Q -> Q(zeta_5)
  equality_id: dl-eq-qzeta5-field         # draft-local (Appendix A)
  coefficient_object_id: DEF-QDD-COEFFICIENT-Q
    # Q with involution bar = sigma_4, Tr = Tr_{K/Q}, defined therein
  # basis: DEF-QDD-AMPLITUDE-B0 (B0 = (1, zeta, zeta^2, zeta^3)),
  # DEF-QDD-COEFFICIENT-Q ("inv_Q, bar and the Gram adjoint are three distinct
  # typed operations").

- carrier_id: QCarrier_QDD
  parent_carrier_id: M_4(Q) x M_4(Q)
  inclusion_or_quotient_map_id: dl-map-qcarrier-image
    # draft-local (Appendix A): image inclusion im(Q_QDD|V_eff)
  equality_id: DEF-QDD-QCARRIER-EQUALITY
    # ordered componentwise rational matrix equality; equal coordinate values do
    # not collapse the two typed slots
  coefficient_object_id: Q
  # basis: DEF-QDD-QCARRIER-EQUALITY; |QCarrier_QDD| = 313 (QDD-ALGEBRAIC-
  # FACTORIZATION [T], CANON.md 1230-1241; disclosure 1741-1748).

- carrier_id: MatterData_QDD              # the one concrete record carrier
  parent_carrier_id: NOT_APPLICABLE       # basis: DEF-QDD-MATTER-RECORD — a record
                                          # type schema, not a subobject
  inclusion_or_quotient_map_id: NOT_APPLICABLE   # basis: same
  equality_id: DEF-QDD-MATTER-RECORD
    # tagged componentwise equality per the record schema (tags ZERO_SUPPORT/
    # SUPPORTED, ZERO_DENOMINATOR/DENSITY, ZERO_DENOMINATOR/NORMALIZED; branch
    # order fixed, "no swap")
  coefficient_object_id: dl-coeff-qdd-record
    # draft-local (Appendix A): Q with typed components Q_{>=0}, Q^2, M_4(Q)
  # basis: DEF-QDD-MATTER-RECORD, CANON.md 1192-1204.
  # Relation to the open record type MatterData: candidate concrete schema for the
  # D_quadratic-leg restriction of the open record type MatterData (carrier row
  # below); the identification is part of the OB-01 adoption question.

- carrier_id: A_8                         # Born residual carrier Z[zeta_8]/5
  parent_carrier_id: Z[zeta_8]
  inclusion_or_quotient_map_id: dl-map-mod5-reduction
    # draft-local (Appendix A): reduction mod 5 on the parent ring
  equality_id: dl-eq-a8-ring              # draft-local (Appendix A): ring equality
                                          # in Z[zeta_8]/5
  coefficient_object_id: dl-coeff-a8-born # draft-local (Appendix A): F_25-side
                                          # residue ring; Born involution =
                                          # conjugation
  # basis: BORN-HALF-ANGLE [T] (CANON.md 3638-3646, unit group cyclic of order 24),
  # BORN-RESIDUAL-SPLIT [T] (3646-3649; also A_4 = Z[i]/5).

- carrier_id: A_4                         # Born residual carrier Z[i]/5
  parent_carrier_id: Z[i]
  inclusion_or_quotient_map_id: dl-map-mod5-reduction   # draft-local (Appendix A)
  equality_id: dl-eq-a4-ring              # draft-local (Appendix A): ring equality
                                          # in Z[i]/5
  coefficient_object_id: dl-coeff-a4-born # draft-local (Appendix A): residue ring;
                                          # conjugation = Born involution
  # basis: BORN-RESIDUAL-SPLIT [T], CANON.md 3646-3649.

- carrier_id: (W_p, g_p)                  # trace-kernel carrier (geometry side)
  parent_carrier_id: G_p                  # trace Gram carrier G_p = p I - J_n
                                          # (ambient-objects note above;
                                          # TRACEKERNEL-RESIDUAL-FORM [T])
  inclusion_or_quotient_map_id: dl-map-trace-radical
    # draft-local (Appendix A): passage to the radical of the residual trace form
  equality_id: dl-eq-wp-linear            # draft-local (Appendix A): F_p-linear
                                          # equality with form g_p
  coefficient_object_id: F_p              # physical branch p = 5, dim W_5 = 3
  # basis: TRACEKERNEL-RESIDUAL-FORM [T] (CANON.md 1866-1912);
  # TRACEKERNEL-HOME-DIMENSION [T] (1914-1942). Used by the D_geom candidate
  # material only; no canonical D_geom operator is selected (see OB-12, OB-13).

- carrier_id: MatterData                  # open record type; D_matter stage codomain
  parent_carrier_id: NOT_APPLICABLE       # basis: the decoder interface declaration
                                          # (CANON.md 455-457; open record type)
  inclusion_or_quotient_map_id: NOT_APPLICABLE   # basis: same
  equality_id: UNRESOLVED                 # no stage-wide field schema registered
                                          # in v60
  coefficient_object_id: UNRESOLVED
  # basis for the name: CANON.md 455-457 ("Let MatterData, GeometryData, and
  # ObservableHistory denote records whose fields exist only where a registered
  # claim defines them"). Adoption of a stage-wide schema -> OB-01; MatterData_QDD
  # above is a candidate concrete schema for the D_quadratic-leg restriction only.

- carrier_id: GeometryData
  parent_carrier_id: NOT_APPLICABLE       # basis: the decoder interface declaration
                                          # (CANON.md 455-457; open record type)
  inclusion_or_quotient_map_id: NOT_APPLICABLE   # basis: same
  equality_id: UNRESOLVED                 # no field schema registered in v60
  coefficient_object_id: UNRESOLVED
  # basis for the name: CANON.md 455-457. Schema absent -> OB-12 (owner
  # CURVATURE-OPERATOR-CANONICAL) and OB-13 (TRACEKERNEL-CURVATURE-FORCING).

- carrier_id: ObservableHistory
  parent_carrier_id: NOT_APPLICABLE       # basis: the decoder interface declaration
                                          # (CANON.md 455-457; open record type)
  inclusion_or_quotient_map_id: NOT_APPLICABLE   # basis: same
  equality_id: UNRESOLVED                 # no field schema registered in v60
  coefficient_object_id: UNRESOLVED
  # basis for the name: CANON.md 455-457. Schema absent -> OB-15 (owner
  # SQRT-PHI-TIME-GRAVITY) and OB-02 (ENTROPY-LAYER-BRIDGE for any measure-bearing
  # history field).
```

---

## 3. record_field_manifest[]

Slots per row: `record_id, field_id, field_type_id, role, carrier_id, domain_id,
normalization_id, equality_id, source_item_id, write_map_id, presence_state,
absence_basis_item_id, emit_rule_id, stage_id, leg_id` (CANON.md 525–540).

Rules honored: exactly one record owner and one stage owner per output field; a
READOUT field resolves exactly one leg; AUXILIARY uses NOT_APPLICABLE with a basis
item; relations between legs only via bridge rows, never inherited (CANON.md 609–616).

### 3.1 MatterData_QDD — the five registered fields (the only concrete schema in v60)

Common to all five rows below:
`record_id: MatterData_QDD; domain_id: K_QDD (DEF-QDD-DOMAIN-K0); stage_id: D_matter;
leg_id: D_quadratic; role: READOUT; source_item_id: DEF-QDD-MATTER-RECORD
(CANON.md 1192-1204); emit_rule_id: dl-emit-per-pointed-orbit (draft-local,
Appendix A: one record per pointed orbit at head n = 0, DEF-QDD-DOMAIN-K0);
write_map_id: DEF-QDD-DIRECT-WRITE (D_QDD_direct = R_cyc o
iota_B0 o beta_QDD) — candidate declaration; canon-side adoption open -> OB-01.`

**Convention (normative for this block):** the eight preamble slots above are
normative parts of each of the five rows below; expanded per row for machine audit,
they complete every row to the full fifteen-slot schema of CANON.md 525–540, and
they are counted per row in section 12.1.

```yaml
- field_id: support_state
  field_type_id: dl-type-support-tag      # draft-local (Appendix A): tag in
                                          # {ZERO_SUPPORT, SUPPORTED}
  carrier_id: dl-carrier-tag2             # draft-local (Appendix A): the 2-element
                                          # tag set
  normalization_id: NOT_APPLICABLE        # basis: DEF-QDD-MATTER-RECORD (schema
                                          # names no normalization for this field;
                                          # ZERO branch fixed, no division performed)
  absence_basis_item_id: NOT_APPLICABLE   # basis: DEF-QDD-MATTER-RECORD (field 1
                                          # present; presence_state is RESOLVED)
  equality_id: dl-eq-tag                  # draft-local (Appendix A)
  presence_state: RESOLVED
  # basis: DEF-QDD-MATTER-RECORD field 1; record total 25 ZERO_SUPPORT + 15600
  # SUPPORTED on all 15625 checkpoints (QDD-ALGEBRAIC-FACTORIZATION [T], 1230-1241).

- field_id: total_weight
  field_type_id: Q_{>=0}
  carrier_id: Q_{>=0}
  normalization_id: NOT_APPLICABLE        # basis: DEF-QDD-MATTER-RECORD (raw
                                          # weight; normalization lives in
                                          # normalized_weight_state only)
  absence_basis_item_id: NOT_APPLICABLE   # basis: DEF-QDD-MATTER-RECORD (field 2
                                          # present; presence_state is RESOLVED)
  equality_id: dl-eq-rational             # draft-local (Appendix A)
  presence_state: RESOLVED
  # basis: DEF-QDD-MATTER-RECORD field 2; closed form m = |v|^2 - s^2/5
  # (QDD-PROJECTOR-PAIR-TR4 [T], 1242-1252).

- field_id: branch_weights
  field_type_id: dl-type-branch-pair      # draft-local (Appendix A): ordered pair
                                          # (LOW, HIGH) in Q_{>=0}^2, "no swap"
  carrier_id: Q_{>=0}^2
  normalization_id: NOT_APPLICABLE        # basis: DEF-QDD-MATTER-RECORD (ordered
                                          # raw pair)
  absence_basis_item_id: NOT_APPLICABLE   # basis: DEF-QDD-MATTER-RECORD (field 3
                                          # present; presence_state is RESOLVED)
  equality_id: dl-eq-branch-pair          # draft-local (Appendix A)
  presence_state: RESOLVED
  # basis: DEF-QDD-MATTER-RECORD field 3; w_low = Tr(E_low A_T G), w_high =
  # Tr(E_high A_T G) (DEF-QDD-BRANCH-WEIGHT-PAIRING); closed forms w_low = s^2/20,
  # w_high = |v|^2 - s^2/4 (QDD-PROJECTOR-PAIR-TR4 [T]).

- field_id: density_state
  field_type_id: dl-type-density-state    # draft-local (Appendix A): tag
                                          # ZERO_DENOMINATOR | tag DENSITY carrying
                                          # a 4x4 rational matrix
  carrier_id: dl-carrier-tagged-m4q       # draft-local (Appendix A): tagged M_4(Q)
  normalization_id: DEF-QDD-BRANCH-WEIGHT-PAIRING
    # density = A_T G / m(A_T) on the DENSITY branch, defined therein
  absence_basis_item_id: NOT_APPLICABLE   # basis: DEF-QDD-MATTER-RECORD (field 4
                                          # present; presence_state is RESOLVED)
  equality_id: dl-eq-density-tagged       # draft-local (Appendix A): tagged matrix
                                          # equality
  presence_state: RESOLVED
  # basis: DEF-QDD-MATTER-RECORD field 4; DEF-QDD-BRANCH-WEIGHT-PAIRING ("an adopted
  # dictionary input, not derived from J").

- field_id: normalized_weight_state
  field_type_id: dl-type-normweight-state # draft-local (Appendix A): tag
                                          # ZERO_DENOMINATOR | tag NORMALIZED
                                          # carrying a rational pair
  carrier_id: dl-carrier-tagged-q2        # draft-local (Appendix A): tagged Q^2
  normalization_id: DEF-QDD-MATTER-RECORD
    # exact division by total weight on the NORMALIZED branch (field 5 schema)
  absence_basis_item_id: NOT_APPLICABLE   # basis: DEF-QDD-MATTER-RECORD (field 5
                                          # present; presence_state is RESOLVED)
  equality_id: dl-eq-normweight-tagged    # draft-local (Appendix A): tagged pair
                                          # equality
  presence_state: RESOLVED
  # basis: DEF-QDD-MATTER-RECORD field 5; "exactly normalized" on all supported
  # checkpoints (QDD-ALGEBRAIC-FACTORIZATION [T]). NOTE: all five fields are L1
  # exact data; NO L6 measure reading of this field is claimed (CANON.md 1203-1204)
  # -> the L6 reading is owned by OB-02/OB-17.
```

### 3.2 Non-manifest commentary: registered maps / typed record names with no owning record — holes, not rows

**This block is NOT part of `record_field_manifest[]` and contains no manifest
rows.** The contract's enums are closed (CANON.md 609–613): `stage_id` takes exactly
`D_matter | D_geom | D_clock`, `role` takes exactly `READOUT | AUXILIARY`, with no
`UNRESOLVED` form, and every output field has exactly one record owner and one stage
owner. The four items below therefore **cannot be stated as contract-legal rows at
all** — v60 supplies no record owner and no stage owner for the linear/binary
readouts, and no field schema for the two open record types. That impossibility is
the finding; it is recorded here as commentary, not as rows.

**Hole H1 — D_linear readout: registered map, no owning record.** The canon
registers the linear readout algebra in full — CODEC-TR4 [T] (CANON.md 2137–2149;
Tr_4(M_J x) = 2 Tr_4(x) − 5 x_c; scalar multiples of Tr_4 are the only covectors
reading any multiplier) and READING-SPLIT [D] ("the linear readout is CODEC-TR4",
1092–1096). A candidate field is fully typeable (draft-local name
`linear_readout_tr4`, Appendix A: an F_5-valued covector reading on checkpoints via
`dl-map-pr-checkpoint`), but **no registered record owns this output and no
registered claim assigns it a stage owner**: the stage and leg axes are independent
(CANON.md 504–505), and inferring an owner would be forbidden inheritance. No live
frontier row owns this hole (nearest owners are the D_geom consumers, see
stage_manifest) → ownerless-hole obligation row **OB-31** (`owning_item_id:
UNRESOLVED`).

**Hole H2 — D_binary readout: registered reading, no owning record.** Registered
material: TIME-CUT-READING [D] (theta cut and knot bracketing 1 00 1, CANON.md
1103–1121), GYRON-DENSITY [T] (rho = 1/6), CENSUS-313 [C] (2111–2118),
RAMIFIED-TM-LIFT [T] (2151–2220), with normalization the stationary TM
pair-substitution fixed point (TM-PAIR-SUBSTITUTION-FIXED-POINT [T]; c_00 density
exactly 1/6). A candidate field is fully typeable (draft-local name
`binary_cut_census`, Appendix A: the `dl-carrier-binary-pair-channel` reading on the
drive word derived from the counter, CANON.md 310–313), but again **no registered
record owner and no stage owner exist** → **OB-31**. NOTE: GYRON-DENSITY's 1/6 "is
not a ... Born multiplier ... physical probability, L5 stream, or L6 measure"
(CANON.md 2099–2102); the L6 reading is owned by OB-02. TIME-CUT-READING "claims no
forcing, uniqueness, or completeness" (1120–1121).

**Hole H3 — GeometryData: typed record name, no schema.** The open record type
GeometryData (CANON.md 455–457) is the D_geom stage codomain (459–467), but v60
registers no field, type, role, or leg for it. Candidate geometry material exists —
(W_5, g_5), K_hist with Tr_V(K_hist^2) = −881/8 (CURVATURE-HISTORICAL-TRACE [T],
349–370) — but is "one historical construction", not a selection. This hole is
owned: → OB-12 (CURVATURE-OPERATOR-CANONICAL), OB-13
(TRACEKERNEL-CURVATURE-FORCING).

**Hole H4 — ObservableHistory: typed record name, no schema.** The open record type
ObservableHistory (CANON.md 455–457) is the D_clock stage codomain (459–467); no
field schema is registered. A terminal emit rule is distinct from a write target and
does not by itself establish no-feed (CANON.md 626–627). This hole is owned: →
OB-15 (SQRT-PHI-TIME-GRAVITY: the Y-to-D_clock bridge), OB-10
(QDD-TERMINAL-EVENT-SEMANTICS: physical meaning of terminal events).

H3 and H4 have live frontier owners and appear in `obligation_manifest[]` under
those owners; H1 and H2 are **ownerless** and are carried there as OB-31 with
`owning_item_id: UNRESOLVED` — see also §12.3 point 3.

### 3.3 Auxiliary derived records (not decoder outputs)

```yaml
- record_id: derived-orbit-logs           # driver word and registered event logs
                                          # (draft-local record name, Appendix A)
  field_id: log_lambda
  field_type_id: dl-type-log-stream       # draft-local (Appendix A):
                                          # (lambda(U^k omega_0))_{k>=0} for a
                                          # registered binary observable
  role: AUXILIARY
  carrier_id: {0,1}^N_0
  domain_id: K
  normalization_id: NOT_APPLICABLE        # basis: DEF-LOG-STREAM (logs are raw
                                          # projections; no normalization declared)
  equality_id: dl-eq-sequence             # draft-local (Appendix A)
  source_item_id: DEF-LOG-STREAM
    # owner of GATE-L1-L5-LOG-PROJECTION; CANON.md 310-313 ("derived orbit records,
    # not additional state variables")
  write_map_id: DEF-LOG-STREAM            # the Log projection — deterministic typed
                                          # map, L1 -> L5
  presence_state: RESOLVED
  absence_basis_item_id: DEF-LOG-STREAM   # CANON.md 310-313; NORMATIVE.tsv L28
                                          # (logs are derived records, owned by no
                                          # reading leg; AUXILIARY uses
                                          # NOT_APPLICABLE with this basis item,
                                          # CANON.md 613-614)
  emit_rule_id: dl-emit-log-definitional  # draft-local (Appendix A): definitional
                                          # projection, gate closed by construction
  stage_id: NOT_APPLICABLE                # basis: DEF-LOG-STREAM (CANON.md 310-313:
                                          # logs are derived records, not stage
                                          # outputs — not an output field, so the
                                          # one-stage-owner rule of CANON.md 612-613
                                          # does not attach; AUXILIARY per 613-614)
  leg_id: NOT_APPLICABLE                  # basis: DEF-LOG-STREAM (AUXILIARY per
                                          # CANON.md 613-614; owned by no reading
                                          # leg)
  # bridge: BR-01 (GATE-L1-L5-LOG-PROJECTION, closed by construction).
```

---

## 4. stage_manifest[]

Slots per row: `stage_id, domain_id, codomain_id, map_id, totality_domain_id,
dependency_item_ids` (CANON.md 542–548). Signatures verbatim from CANON.md 459–467;
stage contracts 469–478. "Totality, uniqueness, and completeness of D are not
claimed" (474–475); "No umbrella full-decoder completeness claim is registered"
(477–478).

```yaml
- stage_id: D_matter
  domain_id: dom(D_matter)                # subset of K; partial by declaration
                                          # (CANON.md 459)
  codomain_id: MatterData                 # carrier row, section 2 (open record type)
  map_id: UNRESOLVED
    # No stage-wide D_matter map is registered. Candidate referent for the
    # quadratic-leg restriction: DEF-QDD-DIRECT-WRITE (D_QDD_direct), exact on all
    # of K_QDD (QDD-ALGEBRAIC-FACTORIZATION [T], 15625/15625) — but the typed
    # decoder action "including its exact factorization through the declared
    # quadratic pair, remains in QUADRATIC-DECODER-DATA [O]" (CANON.md 475-477)
    # -> OB-01.
  totality_domain_id: K_QDD               # quadratic-leg restriction only
                                          # (DEF-QDD-DOMAIN-K0)
    # Totality stated only relative to this named domain (CANON.md 623-624).
    # Stage-wide totality: UNRESOLVED.
  dependency_item_ids: [DEF-AUTONOMOUS-STATE, DEF-QDD-DIRECT-WRITE, DEF-QDD-QPAIR,
    DEF-QDD-MATTER-RECORD, BORN-FACE-WEIGHTS [T], MEASURE-BORN-VERB [D]]
    # basis: CANON.md 470-471 ("the orbit; registered quadratic/Born maps;
    # registered matter maps"); the DEF-QDD-* entries are candidate declarations,
    # adoption -> OB-01
  # Stage owner of output fields: the five MatterData_QDD rows in section 3.1.

- stage_id: D_geom
  domain_id: dom(D_geom)                  # subset of K x MatterData (CANON.md 459-467)
  codomain_id: GeometryData               # carrier row, section 2 (open record type)
  map_id: UNRESOLVED
    # No D_geom map is registered. The historical curvature construction is typed
    # exactly (CURVATURE-HISTORICAL-TRACE [T] 349-370, CURVATURE-HISTORICAL-
    # GAUSS-SPLIT [T] 372-399) but canonical selection is open:
    # CURVATURE-OPERATOR-CANONICAL [O] (400-404) -> OB-12; refinement
    # TRACEKERNEL-CURVATURE-FORCING [O] (426-452) -> OB-13.
  totality_domain_id: UNRESOLVED
  dependency_item_ids: [DEF-AUTONOMOUS-STATE, MatterData, CODEC-TR4 [T],
    HYPERPLANE-BOUNDARY-CLASS [T], DEF-PISTON-WEDGE, MAXWELL-BIANCHI [T],
    MAXWELL-GAUSS-CHAIN [T], MAXWELL-AMPERE-CHAIN [T]]
    # plus the registered wedge maps of the KERNEL-WEDGE-* [T] family
  # basis: CANON.md 471-472 ("D_geom reads the orbit plus MatterData and the
  # registered linear, boundary, wedge, and chain maps").

- stage_id: D_clock
  domain_id: dom(D_clock)                 # subset of K x MatterData x GeometryData
                                          # (CANON.md 459-467)
  codomain_id: ObservableHistory          # carrier row, section 2 (open record type)
  map_id: UNRESOLVED
    # No D_clock map is registered. The dimensionless tick is fixed (METRO-TICK [T],
    # delta tau hat = 2 pi/5 per tick, CANON.md 1119-1120) but the typed
    # clock-and-gravity bridge is SQRT-PHI-TIME-GRAVITY [O] (2391, 2445-2446)
    # -> OB-15.
  totality_domain_id: UNRESOLVED
  dependency_item_ids: [dl-map-counter-projection, MatterData, GeometryData,
    METRO-TICK [T]]
    # dl-map-counter-projection draft-local (Appendix A); accumulated MatterData
    # and GeometryData records
  # basis: CANON.md 472-473 ("D_clock reads the counter projection plus the
  # accumulated records and is terminal"). Terminality of the stage is a declared
  # interface property (CANON.md 473); its PHYSICAL basis is open -> OB-10.
```

---

## 5. leg_manifest[]

Slots per row: `leg_id, owned_field_ids, domain_id, codomain_id, map_id`
(CANON.md 550–555). Legs and stages are independent axes; nothing below transfers
between legs (READING-SPLIT [D], CANON.md 1092–1096; rules 614–616).

```yaml
- leg_id: D_linear
  owned_field_ids: [linear_readout_tr4]   # draft-local candidate name (Appendix A;
                                          # section 3.2 hole H1); registered record
                                          # owner UNRESOLVED -> OB-31
  domain_id: F_5^6                        # checkpoints via dl-map-pr-checkpoint
  codomain_id: F_5
  map_id: RESOLVED: CODEC-TR4 [T]
  # basis: READING-SPLIT [D] ("the linear readout is CODEC-TR4"); CODEC-TR4 [T]
  # CANON.md 2137-2149 — Tr_4(M_J x) = 2 Tr_4(x) - 5 x_c; scalar multiples of Tr_4
  # are the only covectors reading any multiplier.

- leg_id: D_binary
  owned_field_ids: [binary_cut_census]    # draft-local candidate name (Appendix A;
                                          # section 3.2 hole H2); registered record
                                          # owner UNRESOLVED -> OB-31
  domain_id: K                            # derived drive word (CANON.md 310-313)
  codomain_id: dl-carrier-binary-pair-channel
    # draft-local (Appendix A): binary pair channel with exact census densities
  map_id: RESOLVED: TIME-CUT-READING [D]
    # composed dictionary, over RAMIFIED-TM-LIFT [T] (sign quotient of the
    # four-phase J-channel), GYRON-DENSITY [T] (rho = 1/6), CENSUS-313 [C]
  # basis: READING-SPLIT [D] ("the binary cut drives the census"); CANON.md
  # 1103-1121. No forcing/uniqueness/completeness claimed (1120-1121).

- leg_id: D_quadratic
  owned_field_ids: [support_state, total_weight, branch_weights, density_state,
    normalized_weight_state]              # the five MatterData_QDD fields, 3.1
  domain_id: K_QDD                        # DEF-QDD-DOMAIN-K0
  codomain_id: MatterData_QDD
  map_id: DEF-QDD-DIRECT-WRITE
    # candidate declaration — canon-side adoption open -> OB-01; factored as
    # D_QDD_direct = F_QDD o Q_QDD o beta_QDD (QDD-ALGEBRAIC-FACTORIZATION [T])
  # basis: READING-SPLIT [D] ("the quadratic registration is the Born square");
  # Born chain: BORN-FACE-WEIGHTS [T] (3508-3518) -> MEASURE-BORN-VERB [D]
  # (3660-3663) with BORN-HALF-ANGLE [T] / BORN-RESIDUAL-SPLIT [T] fixing the Born
  # involution carriers A_8, A_4. Canon-side adoption of the leg map is open:
  # QUADRATIC-DECODER-DATA [O] -> OB-01. Scoping rule honored: only D_quadratic
  # fields are tested for factorization through Q; nothing transfers to
  # D_linear/D_binary (CANON.md 629-632).
```

---

## 6. bridge_manifest[]

Slots per row: `bridge_id, source_id, target_id, domain_id, codomain_id, map_id,
dependency_item_ids, from_layer, to_layer, gate_ids` (CANON.md 557–567). Rule: "A
declared cross-layer map records its public gate identifier; absence of that gate
leaves the requirement unresolved" (624–626). All gate ids below are verbatim from
`canon/GATES.tsv` (11 gates).

### 6.1 Bridges with closed or dictionary-closed gates (citable now)

```yaml
- bridge_id: BR-01-log-projection
  source_id: Omega orbit (L1)             target_id: read-only log stream (L5)
  domain_id: K                            codomain_id: derived log records
  map_id: RESOLVED: the Log projection (DEF-LOG-STREAM)
  dependency_item_ids: [DEF-LOG-STREAM]   # basis: DEF-LOG-STREAM (CANON.md 310-313)
  from_layer: L1                          to_layer: L5
  gate_ids: [GATE-L1-L5-LOG-PROJECTION]   # DEFINITION_PROJECTION, closed by
                                          # construction; owner DEF-LOG-STREAM

- bridge_id: BR-02-born-reading
  source_id: exact face weights (L5)      target_id: Born-square measure reading (L6)
  domain_id: five-face verb channel       codomain_id: mu(k) = |1 + zeta^k|^2 / 10
  map_id: RESOLVED: MEASURE-BORN-VERB [D] over BORN-FACE-WEIGHTS [T]
  dependency_item_ids: [BORN-FACE-WEIGHTS [T] 3508-3518; BORN-HALF-ANGLE [T];
    BORN-RESIDUAL-SPLIT [T]]
  from_layer: L5                          to_layer: L6
  gate_ids: [GATE-L5-L6-BORN-READING]     # DICTIONARY_LIFT (declared reading);
                                          # owner MEASURE-BORN-VERB [D]. "No
                                          # positivity is claimed in the finite
                                          # algebra" (CANON.md 3656).

- bridge_id: BR-03-tm-sym2-born-measure
  source_id: frozen 48-selector stream (L5)  target_id: normalized L6 measure on the
                                             frozen class
  domain_id: all 48 frozen selectors      codomain_id: mu_B(w) = 1/6, total normalized
  map_id: RESOLVED: TM-SYM2-PHYSICAL-MEASURE [D] (monomial J-verb lift, frozen as
    typed bridge input, "not selected from all same-modulus lifts")
  dependency_item_ids: [TM-SYM2-* [T] rows 6274-6329; circularity fence: 1/6, M_TM,
    GYRON-DENSITY forbidden as selection inputs (gate decision text)]
  from_layer: L5                          to_layer: L6
  gate_ids: [GATE-L5-L6-TM-SYM2-BORN-MEASURE]  # DICTIONARY_LIFT closed at D on the
                                               # frozen class only; no all-lift
                                               # uniqueness (CANON.md 6421-6426)
```

### 6.2 Bridges whose gates exist but are open — maps and endpoints UNRESOLVED

The open gates declare no endpoints either; every slot v60 does not supply carries
the literal `UNRESOLVED`, which is itself diagnostic payload.

```yaml
- bridge_id: BR-04-curvature-canonical
  source_id: UNRESOLVED            target_id: UNRESOLVED
  domain_id: UNRESOLVED            codomain_id: UNRESOLVED
  from_layer: L1   to_layer: L2   gate_ids: [GATE-L1-L2-CURVATURE-CANONICAL]
  map_id: UNRESOLVED               # owner CURVATURE-OPERATOR-CANONICAL [O] -> OB-12
  dependency_item_ids: [CURVATURE-HISTORICAL-TRACE [T]]
    # the one typed historical construction (CANON.md 349-370)
  # verdict alphabet UNIQUE / NONUNIQUE / EMPTY / STOP — the literal forced-decoder
  # instrument for the geometry stage.

- bridge_id: BR-05-tracekernel-hodge-home
  source_id: UNRESOLVED            target_id: UNRESOLVED
  domain_id: UNRESOLVED            codomain_id: UNRESOLVED
  from_layer: L2   to_layer: L1   gate_ids: [GATE-L2-L1-TRACEKERNEL-HODGE-HOME]
  map_id: UNRESOLVED               # owner TRACEKERNEL-CURVATURE-FORCING [O] -> OB-13
  dependency_item_ids: [DEF-EXACT-HODGE-HOME-CLOSURE]   # CANON.md 408-424
  # "the gate adds no carrier identification and selects no curvature operator"
  # (CANON.md 448).

- bridge_id: BR-06-generations
  source_id: UNRESOLVED            target_id: UNRESOLVED
  domain_id: UNRESOLVED            codomain_id: UNRESOLVED
  from_layer: L2   to_layer: L3   gate_ids: [GATE-L2-L3-GENERATIONS]
  map_id: UNRESOLVED               # owner GENERATIONS-L3 [O] -> OB-19
  dependency_item_ids: UNRESOLVED

- bridge_id: BR-07-color-measure
  source_id: UNRESOLVED            target_id: UNRESOLVED
  domain_id: UNRESOLVED            codomain_id: UNRESOLVED
  from_layer: L4   to_layer: L6   gate_ids: [GATE-L4-L6-COLOR-MEASURE]
  map_id: UNRESOLVED               # owner COLOR-MEASURE-SELECTION [O] -> OB-03
  dependency_item_ids: UNRESOLVED

- bridge_id: BR-08-metro-normalization
  source_id: UNRESOLVED            target_id: UNRESOLVED
  domain_id: UNRESOLVED            codomain_id: UNRESOLVED
  from_layer: L5   to_layer: L6   gate_ids: [GATE-L5-L6-METRO-NORMALIZATION]
  map_id: UNRESOLVED               # owner METRO-ADMISSIBILITY-DIM [O] -> OB-08
  dependency_item_ids: UNRESOLVED

- bridge_id: BR-09-entropy-bridge
  source_id: UNRESOLVED            target_id: UNRESOLVED
  domain_id: UNRESOLVED            codomain_id: UNRESOLVED
  from_layer: L2   to_layer: L5   gate_ids: [GATE-L2-L5-ENTROPY-BRIDGE]
  map_id: UNRESOLVED               # owner ENTROPY-LAYER-BRIDGE [O] -> OB-02
  dependency_item_ids: UNRESOLVED
  # POS closure = A_A proved nonempty by one exhibited exact map of the registered
  # P_5 type (no P_5 has been exhibited) with mu-a.e. equivariance and pushforward
  # Law_W on [512, 2048).

- bridge_id: BR-10-minimal-read
  source_id: UNRESOLVED            target_id: UNRESOLVED
  domain_id: UNRESOLVED            codomain_id: UNRESOLVED
  from_layer: L5   to_layer: L1   gate_ids: [GATE-L5-L1-MINIMAL-READ]
  map_id: UNRESOLVED               # owner MINIMAL-READ-DERIVATION [O] -> OB-14
  dependency_item_ids: UNRESOLVED
  # would decide whether read_convention_id (section 1) is forced.
```

### 6.3 Bridges the candidate needs but for which NO gate exists

```yaml
- bridge_id: BR-11-pure-record-port
  source_id: quadratic pure record (L4)   target_id: direct read-only source port (L1)
  domain_id: UNRESOLVED                   # no source ownership adopted (see gate_ids)
  codomain_id: UNRESOLVED                 # no registered port codomain; no encoding
                                          # into K is selected
  map_id: b_W
    # registered referent: b_W([v]) = (v^T G v, vv^T G/(v^T G v)) — forced
    # singleton in its frozen direct class (QDD-PURE-RECORD-PORT-UNIQUENESS [T],
    # 1503-1514), feeds_U = false. Canon-side adoption is UNRESOLVED and is
    # tracked in obligation_manifest[] (OB-09 family), not in this slot.
  dependency_item_ids: [QDD-PURE-RECORD-TYPED-BRIDGE-BOUNDARY [T],
    QDD-PURE-RECORD-PORT-UNIQUENESS [T]]
  from_layer: L4                          to_layer: L1
  gate_ids: UNRESOLVED                    # "no source ownership, equality or
                                          # registered L4-to-L1 gate is adopted"
                                          # (QDD-PURE-RECORD-TYPED-BRIDGE-BOUNDARY
                                          # [T], 1490-1502) -> OB-09 family
                                          # (editorial routing, not registered
                                          # ownership)
  # Also: no encoding into K is selected — two disjoint exact static encodings
  # decode the same records; no faithful injective bridge intertwines the
  # order-five projective motor with a nonnegative U-tail lag (1495-1501).

- bridge_id: BR-12-event-context-bank
  source_id: 22-context carry bank (L1)   target_id: realized event stream (L5)
  domain_id: C_bank
    # registered referent: the exact minimal carry bank C_bank = prod_p Z/b_p Z,
    # |C_bank| = B = 19702414515172535913561087541248 = 2^66 3^2 7^4 11 13^2 17^2 23
    # (QDD-EVENT-CONTEXT-BANK [T], 1560-1579)
  codomain_id: UNRESOLVED                 # no realized event stream type is
                                          # registered
  map_id: UNRESOLVED
    # the sampling law itself is NOT PROVIDED (SAMPLING NOT PROVIDED, 1576-1579);
    # QDD-EVENT-CONTEXT-BANK [T] supplies the exact class-relative normal form of
    # the carrier only. Canon-side adoption -> OB-09.
  dependency_item_ids: [QDD-EVENT-CONTEXT-BANK [T]]
  from_layer: L1                          to_layer: L5
  gate_ids: UNRESOLVED                    # "The active architecture contains neither
                                          # the probability-keyed rank vector nor a
                                          # physical reduced-p context law, selected
                                          # ready phase, persistent update or
                                          # registered L1-to-L5 gate" (1576-1579).
                                          # SAMPLING NOT PROVIDED -> OB-09.
```

### 6.4 Declared non-bridges (compliance notes, no rows)

- **No cross-leg bridge row is declared.** The candidate claims no relation between
  `D_linear`, `D_binary`, `D_quadratic`. In particular the numeric coincidence
  `|QCarrier_QDD| = 313 = |CENSUS-313 attractors|` is NOT a bridge: the partitions
  share no block and "No cross-leg identity is claimed" (CANON.md 1741–1748);
  "common numeric value -/-> typed bridge" is forbidden inheritance (1078).
- **No bridge routes through GATE-L1-L5-TM-SYM2-SELECTOR-STREAM**: FIRED_NEGATIVE,
  terminal (owner TM-SYM2-MEASURE [F]); later actions "do not reopen, move, or
  repair this terminal gate".
- **No writeback bridge exists or is claimed**: any observer-output-to-U extension
  requires seven new public artifacts and a separately registered claim
  (CANON.md 480–487). See closure_manifest.

---

## 7. quadratic_manifest

Slots: `coefficient_ring_id, effective_carrier_id, orbit_to_amplitude_bridge_id,
gram_id, dagger_id, transpose_id, qcarrier_id, q_equality_id, q_map_id, effect_ids,
born_pairing_id, factorization_map_id` (CANON.md 569–581).

Every slot below cites a public DEF-QDD-* referent (CANON.md 1136–1224) as a
**candidate declaration**. The canon itself has filled none of them ("These results
fill no decoder-completion-contract field", 1618–1619); the registered adoption of
this data as *the* typed D_matter action is exactly QUADRATIC-DECODER-DATA [O]
(REGISTRY row 173) → **OB-01**, which is the single owning frontier row for this
entire block.

```yaml
coefficient_ring_id: RESOLVED: DEF-QDD-COEFFICIENT-Q
  # ring Q, trivial involution matrix-side; amplitude field K = Q(zeta_5) with
  # bar = sigma_4, Tr = Tr_{K/Q}.

effective_carrier_id: RESOLVED: DEF-QDD-BALANCED-PISTON
  # beta_QDD : kappa_x -> (ell(p1), ell(p4), ell(p1'), ell(p4'))^T in V_eff =
  # ell(F_5)^4 subset Q^4; balanced lift ell(0,1,2,3,4) = (0,1,2,-2,-1).

orbit_to_amplitude_bridge_id: RESOLVED: DEF-QDD-AMPLITUDE-B0
  # B0 = (1, zeta, zeta^2, zeta^3); iota_B0 into K; Amp_QDD = iota_B0 o beta_QDD.

gram_id: RESOLVED: DEF-QDD-GRAM
  # G = I_4 - (1/5) 11^T; G^-1 = I_4 + 11^T; Gram adjoint A^sharp = G^-1 A^T G;
  # fed by DEF-QDD-TRACE-PAIRING (<x,y>_tr = (1/5) Tr(x sigma_4(y))).

dagger_id: RESOLVED: DEF-QDD-DAGGER          # v^dagger = v^T on Q^4
transpose_id: RESOLVED: DEF-QDD-TRANSPOSE    # transpose(A) = A^T on M_4(Q)

qcarrier_id: RESOLVED: QCarrier_QDD = im(Q_QDD|V_eff) subset M_4(Q) x M_4(Q)
  # basis: DEF-QDD-QCARRIER-EQUALITY; 313 elements.
q_equality_id: RESOLVED: DEF-QDD-QCARRIER-EQUALITY
  # ordered componentwise rational matrix equality; the two typed slots never
  # collapse (QDD-QCARRIER-DIAGONAL-BOUNDARY [T]: on V_eff, A_dagger = A_T = vv^T,
  # yet both slots remain typed; 90 Hermitian slots, 313 pairs).

q_map_id: RESOLVED: DEF-QDD-QPAIR
  # Q_QDD(v) = (A_dagger, A_T) = (v v^dagger, v v^T), ordered pair of typed slots.

effect_ids: RESOLVED: [DEF-QDD-PROJECTOR-LOW (E_low = (1/4) 11^T),
  DEF-QDD-PROJECTOR-HIGH (E_high = I_4 - E_low)], on the LOW LINE
  DEF-QDD-LOW-LINE (Q lambda_B, lambda_B = -zeta^4)
  # Frozen ordered effect pair of the EFFECT_SHADOW_MINIMAL owner freeze;
  # "ALGEBRAIC_READOUT, not a physical apparatus selection ... not claimed to be
  # forced by J" (CANON.md 1189-1190). Physical instrument realization -> OB-09.

born_pairing_id: RESOLVED: DEF-QDD-BRANCH-WEIGHT-PAIRING
  # on the transpose slot: m(A_T) = Tr(A_T G); w_low = Tr(E_low A_T G); w_high =
  # Tr(E_high A_T G); density A_T G / m(A_T). "An adopted dictionary input, not
  # derived from J."

factorization_map_id: RESOLVED: DEF-QDD-FACTOR-MAP
  # F_QDD : QCarrier_QDD -> MatterData_QDD; keystone identity
  # D_QDD_direct = F_QDD o Q_QDD o beta_QDD field by field on all 15625 checkpoints,
  # constant on each of the 313 Q_QDD-fibres, injective on QCarrier_QDD
  # (QDD-ALGEBRAIC-FACTORIZATION [T], 1230-1241; evidence reproduce/qdd-route-a,
  # 15/15 ALL PASS, byte-identical x86_64/aarch64).
```

Scoping rule honored (CANON.md 629–632): only fields owned by `D_quadratic` under
QUADRATIC-DECODER-DATA are tested for factorization through `Q`; no factorization,
status, evidence, or closure is inherited by `D_linear` or `D_binary`, or transferred
between `D_matter`, `D_geom`, `D_clock`.

---

## 8. physics_manifest

Slots: `source_id, current_id, conservation_id, propagator_id, detector_id`
(CANON.md 583–588). The contract "does not establish ... [the]
source-current-conservation-propagator-detector chain" (637–641); everything below
is finite-chain / dictionary scope, with no continuum limit claimed anywhere
(MAXWELL-CLOSED [D], REGISTRY row: "no continuum limit is claimed").

```yaml
source_id: MAXWELL-GAUSS-CHAIN [T]
  # scope: finite chain only — Gauss as boundary equation on the closed spatial
  # torus, constructive dipole (CANON.md 3493-3495); solvable iff total charge =
  # 0 mod 5 (MAXWELL-OBSTRUCTION-P [T], 3497-3500).
  # NOT covered by this identifier: the tensor emission source (TT-SOURCE [O]
  # -> OB-16), the gravity source channel (SQRT-PHI-TIME-GRAVITY [O] -> OB-15),
  # the inhomogeneous cosmological source (FRW-INHOM [O] -> OB-24).

current_id: MAXWELL-AMPERE-CHAIN [T]
  # scope: finite chain only — inhomogeneous pair in 96 face symbols (3495-3497);
  # currents solvable iff conserved and 4 winding numbers = 0 mod 5
  # (MAXWELL-OBSTRUCTION-P [T]).

conservation_id: MAXWELL-AMPERE-CHAIN [T]
  # scope: finite chain only — the conservation identity clause of that item; with
  # the homogeneous identity MAXWELL-BIANCHI [T] (dF = 0 identically in 32 edge
  # symbols, 3491-3493; gauge invariance an identity).

propagator_id: COULOMB-GREEN-COMPUTATION [C]
  # scope: finite graph only — Moore-Penrose Green kernel on the finite decoder
  # graph C4: 16 G = circ(5,-1,-3,-1), zero row sum (3474-3481); continuum
  # 1/(4 pi r) enters only as the COULOMB-PROJECTION [D] dictionary with "no value
  # on finite C4".
  # NOTE: the physical PHOTON propagator has no route in v60 — the frozen compound
  # route is falsified (PHOTON-KAPPA-LEMMA [F], PHOTON-WINDOW-PROOF [F],
  # 3700-3710); "no ... continuum limit, photon propagator, or physical-photon
  # conclusion follows" (3711-3714). No live frontier row exists for it (the route
  # is [F], not [O]); this ownerless hole is carried as obligation row OB-32
  # (owning_item_id: UNRESOLVED). A new route would need a new registered claim.

detector_id: UNRESOLVED
  # SAMPLING NOT PROVIDED (CANON.md 1283, 1620-1621; FRONTIER.md L39). Owner:
  # QDD-INSTRUMENT-APPARATUS [O] (parent, -> OB-09) with children
  # QDD-TERMINAL-EVENT-SEMANTICS [O] (O2a, -> OB-10) and
  # QDD-INSTRUMENT-CLASS-COMPLETENESS [O] (O2b, -> OB-11); parent closes only when
  # O1 sampling and both O2 children close compatibly (1599-1621).
  # Existing referent NOT adoptable as detector: QDD-INSTRUMENT-NONSELECTION [T]
  # proves instrument existence is not a selection principle (1260-1283).
```

---

## 9. measure_manifest

Slots: `measure_id, normalization_id, metrology_id, scheme_id` (CANON.md 590–594).

```yaml
measure_id: UNRESOLVED
  # No L6 physical measure is registered. Owners: ENTROPY-LAYER-BRIDGE [O]
  # (binary/census leg, GATE-L2-L5-ENTROPY-BRIDGE; -> OB-02) and
  # COLOR-MEASURE-SELECTION [O] (color sector, GATE-L4-L6-COLOR-MEASURE; -> OB-03).
  # The only closed L6 item, TM-SYM2-PHYSICAL-MEASURE [D] (mu_B = 1/6 on the frozen
  # 48-selector class, GATE-L5-L6-TM-SYM2-BORN-MEASURE closed at D), is NOT adopted
  # here as THE measure: it is scope-limited to one frozen class, carries no
  # all-lift uniqueness (6421-6426), and its selector-stream predecessor gate is
  # terminal negative. It is cited as bridge BR-03 only.
  # Explicit firewall honored: "No identification of the toral rate with the
  # declared architecture's tick is made here: that identification is exactly the
  # open obligation ENTROPY-LAYER-BRIDGE [O]" (1826-1829).

normalization_id: UNRESOLVED
  # L6 normalization for metrology streams is owned by METRO-ADMISSIBILITY-DIM [O]
  # ("total tagged L6 normalization Y_r"; GATE-L5-L6-METRO-NORMALIZATION; -> OB-08)
  # under parent METRO-ADMISSIBILITY [O] (-> OB-07) and the reduction calculus
  # METRO-REDUCTION-CALCULUS [O] (-> OB-06). Local exact normalizations exist
  # (DEF-QDD-BRANCH-WEIGHT-PAIRING; DEWITT-TWELVES [T] dressing chain) but none is
  # a registered L6 normalization.

metrology_id: GRAVITY-BRIDGE-LAW [D]
  # scope: dimensionless layer only.
  # alpha B g = 1 identically, B = alpha^-1/g, g = 2^5 phi^2 sqrt(3 - phi),
  # G_T = (32/33)^2 alpha^20 / g, G_nat = 27 = d^3; single SI anchor m_e
  # (MASS-LADDER-FORMS [D], 3575-3591); dimensionless tick delta tau hat = 2 pi/5
  # (METRO-TICK [T], 6530-6532); alpha register committed D-form with fenced CODATA
  # witness alpha^-1 = 137.035999190 (ALPHA-FORM [D] / ALPHA-VALUE-DIGITS [C],
  # 3531-3542).
  # THE SI CLAUSE IS UNRESOLVED: "the SI value of G is not claimed and stays on the
  # frontier" (6155-6156; REGISTRY row 92); owner METRO-EDGE-SCALE [O] -> OB-04.
  # Nothing in section 15 converts a committed dimensionless form into an SI
  # quantity; physical units are residual clause R7 of METRO-ADMISSIBILITY (6758).

scheme_id: UNRESOLVED
  # Owner: SCHEME-DICTIONARY [O] (REGISTRY row 169; STOP until scheme/scale/
  # threshold conventions are public) -> OB-05. Blocks ALPHA-S-RUNNING [O]
  # downstream (-> OB-22).
```

---

## 10. closure_manifest

Slots: `write_target_ids, feeds_U, terminal_output_ids, terminality_basis_id`
(CANON.md 596–600). "There is no bare null" (621–622): absence is expressed through
declared states, not omission.

```yaml
write_target_ids: []                       # EXPLICITLY EMPTY BY CLAIM
  # basis: the read-only clause — "None of these outputs feeds U, so the declared
  # dependency graph is acyclic" (CANON.md 473-474); the writeback boundary: any
  # observer-output-to-U extension requires a newly typed architecture, output
  # schema, write-channel type, autonomous-state codomain, protocol class,
  # dependency graph, and a separately registered and preregistered claim
  # (480-487). No such extension is registered.

feeds_U: FALSE
  # basis: CANON.md 473-474 (declared acyclicity) + 480-487 (writeback boundary).
  # Theorem-grade supporting context: QDD-PURE-RECORD-TYPED-BRIDGE-BOUNDARY [T]
  # (1490-1502) exhibits the intended use of feeds_U = false on the direct
  # read-only port while adopting no ownership; QDD-PURE-RECORD-PORT-UNIQUENESS [T]
  # (1503-1514) proves that port is a forced singleton in its frozen class with
  # "no encoding into K or writeback to U".
  # Scope note: FALSE is a property of the DECLARED partial interface, not a
  # theorem about all conceivable extensions (480-482).

terminal_output_ids: [ObservableHistory]
  # basis: "D_clock ... is terminal" (CANON.md 473). Schema of the record itself is
  # UNRESOLVED (section 3.2, hole H4).

terminality_basis_id: dl-basis-interface-terminality
  # draft-local (Appendix A): the declared stage-contract terminality clause,
  # CANON.md 473 ("D_clock reads the counter projection plus the accumulated
  # records and is terminal"). Scope: interface layer only.
  # LIMIT: completion-wide terminality is explicitly among the things the contract
  # does not establish (640-641), and a terminal emit rule "does not by itself
  # establish that the output cannot feed U" (626-627). The PHYSICAL terminality
  # basis (what makes an event completed) is UNRESOLVED, owner
  # QDD-TERMINAL-EVENT-SEMANTICS [O] -> OB-10 — whose positive principle must be
  # stated WITHOUT COMM-SAT, Xi_T = 0, projective idempotence, +/-Q, Lueder, or the
  # target effects as construction inputs (1580-1588). This draft honors that
  # circularity fence by adopting none of those as a terminality basis.
```

---

## 11. obligation_manifest[]

Slots per row: `requirement_id, owning_item_id, value_state, basis_item_ids`
(CANON.md 602–606). One row per **live frontier row** of v60 (30 rows: 27 [O] + 3
[H]), so this block doubles as the complete open surface of the programme — **plus
two ownerless-hole rows (OB-31, OB-32)** surfaced by this instance, which
correspond to **no** live frontier row and carry `owning_item_id: UNRESOLVED`
(legal for identifier slots; see §12.3 point 3). Ownership never moves: "Each
property remains owned by its registered claim and evidence" (641–643). Queue
metadata from `canon/FRONTIER_PROGRAMS.tsv` via R4. `requirement_id` values are the
bare tokens `OB-nn` (draft-local numbering); requirement descriptions live in `#`
comments.

```yaml
# ---- Core decoder slots (owners of UNRESOLVED identifiers above) ----
- requirement_id: OB-01
  # quadratic D_matter action — registered adoption + closure of
  # the entire quadratic_manifest and the MatterData write maps
  owning_item_id: QUADRATIC-DECODER-DATA [O]      # ROOT; STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 475-477, 1618-1619; REGISTRY row 173; sections 3.1, 4,
    5, 7 above]

- requirement_id: OB-02
  # L6 physical measure, binary/census leg
  # (measure_manifest.measure_id, normalization for that leg)
  owning_item_id: ENTROPY-LAYER-BRIDGE [O]        # ROOT; STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 2630-2657, 2785-2791, 1826-1829;
    GATE-L2-L5-ENTROPY-BRIDGE; BR-09]

- requirement_id: OB-03
  # color-sector L4->L6 measure lift
  # (measure_manifest.measure_id, color)
  owning_item_id: COLOR-MEASURE-SELECTION [O]     # ROOT; STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 6140-6148; GATE-L4-L6-COLOR-MEASURE; BR-07]

- requirement_id: OB-04
  # SI clause + canonical phi-ladder selector
  # (measure_manifest.metrology_id SI half; every dimensionful statement)
  owning_item_id: METRO-EDGE-SCALE [O]            # FOLLOWUP; BLOCKED
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 6532-6533, 6155-6156; REGISTRY row 92 fence;
    DEPENDENCIES.tsv L354 (bounds SQRT-PHI-TIME-GRAVITY SI claims)]

- requirement_id: OB-05
  # scheme dictionary to measured couplings
  # (measure_manifest.scheme_id)
  owning_item_id: SCHEME-DICTIONARY [O]           # ROOT; STOP
  value_state: UNRESOLVED
  basis_item_ids: [REGISTRY row 169]

- requirement_id: OB-06
  # reduction-equivalence calculus (coarse_graining_id;
  # equivalence semantics behind every L5-consuming slot)
  owning_item_id: METRO-REDUCTION-CALCULUS [O]    # ROOT; STOP — deepest formal
                                                  # choke point (R4 §3.3)
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 6681-6688; METRO-REDUCTION-ARROWS [C] closed A and C
    only; METRO-FORBIDDEN-WITNESSES [C] discharged obligation B's five entries]

- requirement_id: OB-07
  # admissible protocol class, residual cover R1-R8
  # (totality quantifier for metrology-facing stage/bridge claims)
  owning_item_id: METRO-ADMISSIBILITY [O]         # FOLLOWUP; STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 6744-6763; R7 = physical units]

- requirement_id: OB-08
  # L5->L6 metrology normalization
  # (measure_manifest.normalization_id)
  owning_item_id: METRO-ADMISSIBILITY-DIM [O]     # FOLLOWUP; STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 6690-6742; GATE-L5-L6-METRO-NORMALIZATION; BR-08]

- requirement_id: OB-09
  # detector / realized-event sampling, O1
  # (physics_manifest.detector_id; gate for BR-12)
  owning_item_id: QDD-INSTRUMENT-APPARATUS [O]    # FOLLOWUP; STOP; parent
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 1599-1621; SAMPLING NOT PROVIDED 1576-1579 (and
    SAMPLING IMPOSSIBLE not claimed, 1620); QDD-EVENT-CONTEXT-BANK [T] as exact
    class-relative normal form only]

- requirement_id: OB-10
  # physical terminal-event semantics, O2a
  # (closure_manifest.terminality_basis_id physical half)
  owning_item_id: QDD-TERMINAL-EVENT-SEMANTICS [O]   # FOLLOWUP; STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 1580-1588; noncircularity fence part of the obligation
    itself]

- requirement_id: OB-11
  # complete apparatus preselection class + family equality, O2b
  # (completeness half of physics_manifest.detector_id)
  owning_item_id: QDD-INSTRUMENT-CLASS-COMPLETENESS [O]  # FOLLOWUP; STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 1589-1598; QDD-FINITE-MEMORY-O2B-BOUNDARY [T] gives
    pointwise fibres only]

- requirement_id: OB-12
  # canonical D_geom curvature operator
  # (stage_manifest[D_geom].map_id; GeometryData schema)
  owning_item_id: CURVATURE-OPERATOR-CANONICAL [O]   # ROOT; STOP; verdict alphabet
                                                     # UNIQUE/NONUNIQUE/EMPTY/STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 400-404; GATE-L1-L2-CURVATURE-CANONICAL; BR-04;
    CURVATURE-HISTORICAL-TRACE [T] as the one typed historical construction]

- requirement_id: OB-13
  # Hodge-home forcing through the complete L2 class
  # (refinement of OB-12; BR-05)
  owning_item_id: TRACEKERNEL-CURVATURE-FORCING [O]  # FOLLOWUP; BLOCKED by OB-12
                                                     # (DEPENDENCIES.tsv L561)
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 426-452; GATE-L2-L1-TRACEKERNEL-HODGE-HOME;
    DEF-EXACT-HODGE-HOME-CLOSURE 408-424]

- requirement_id: OB-14
  # forcing of the read convention (w = 1, beta_1)
  # (top-level read_convention_id forced-vs-free; BR-10)
  owning_item_id: MINIMAL-READ-DERIVATION [O]     # ROOT; STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 4519-4530; GATE-L5-L1-MINIMAL-READ;
    COIN-SELECTION-CONDITIONAL [T]; READ-REDUNDANCY-PRIME-SUPPORT [T] "closes
    nothing"]

- requirement_id: OB-15
  # typed clock-and-gravity bridge
  # (stage_manifest[D_clock].map_id; ObservableHistory schema;
  # gravity physics_manifest.source_id channel)
  owning_item_id: SQRT-PHI-TIME-GRAVITY [O]       # FOLLOWUP; STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 2391, 2445-2446; SQRT-PHI-DIGIT-LIFT [T]; METRO-TICK
    [T]; SI portion bounded by OB-04 (DEPENDENCIES.tsv L354)]

- requirement_id: OB-16
  # tensor emission map
  # (tensor-sector physics_manifest.source_id / current_id)
  owning_item_id: TT-SOURCE [O]                   # FOLLOWUP; BLOCKED
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 6514-6515; POL-READ bounded by it]

- requirement_id: OB-17
  # probability-bearing bridge gating (Bell/locality layer;
  # polices every probability-bearing bridge_manifest.gate_ids)
  owning_item_id: BELL-CAUSAL-ACCOUNTING [O]      # ROOT; STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 7296 ff.; semantically behind OB-09 (realized events)
    and an L6 measure (OB-02 or OB-03)]

# ---- Sector rows (no core manifest slot; sector fields and sufficiency tests) ----
- requirement_id: OB-18
  # substrate coupling realizing the Schwinger first-order
  # coefficient
  owning_item_id: QUANT-SUBSTRATE [O]             # ROOT; READY — workable now
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 3739, 7273-7275; QUANT-SCHWINGER-TARGET [T] supplies
    the exact target J Jbar/script-Q = 1/(2 pi) without realizing it]

- requirement_id: OB-19
  # generation count at the L3 boundary (BR-06)
  owning_item_id: GENERATIONS-L3 [O]              # ROOT; READY — workable now
  value_state: UNRESOLVED
  basis_item_ids: [GATE-L2-L3-GENERATIONS]

- requirement_id: OB-20
  # vector-doublet normalization yielding numerical r_T(k)
  # (tensor-sector record_field normalization_id)
  owning_item_id: TT-VECTOR-STATE-NORMALIZATION [O]  # ROOT; READY — workable now
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 6200-6201; TT-VECTOR-MOMENT-UNDERDETERMINATION [T]]

- requirement_id: OB-21
  # integer crossing count per observable
  owning_item_id: DRESS-CROSSCOUNT [O]            # FOLLOWUP; BLOCKED
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 6533-6536; armed witness 72 alpha^4, labeled]

- requirement_id: OB-22
  # strong-coupling running to a named scale
  owning_item_id: ALPHA-S-RUNNING [O]             # FOLLOWUP; BLOCKED
  value_state: UNRESOLVED
  basis_item_ids: [REGISTRY row 168; FRONTIER_PROGRAMS.tsv (work_state BLOCKED)]
  # BLOCKED is cited from FRONTIER_PROGRAMS.tsv, which names no blocker. The scheme
  # dependency (behind OB-05) is inferred from REGISTRY row 168's closure condition
  # — closure requires "matching the measured strong coupling at a named scale",
  # which presupposes the scheme dictionary — not from any ledger dependency edge
  # (DEPENDENCIES.tsv L125-126 bound STRONG-SEED, not this row).

- requirement_id: OB-23
  # neutron electromagnetic delta
  owning_item_id: NEUTRON-DELTA-EM [O]            # FOLLOWUP; BLOCKED
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 3587-3589; bounds MASS-LADDER-FORMS]

- requirement_id: OB-24
  # inhomogeneous FRW source construction
  owning_item_id: FRW-INHOM [O]                   # FOLLOWUP; BLOCKED
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 6432-6433]

- requirement_id: OB-25
  # proton residual under a future frozen QCD schema
  owning_item_id: PROTON-RESIDUAL-IS-QCD [O]      # FOLLOWUP; STOP (schema unfrozen)
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 3593-3605]

- requirement_id: OB-26
  # dark-energy conformal weight selection (circularity-fenced)
  owning_item_id: DE-CONFORMAL-WEIGHT [O]         # FOLLOWUP; STOP
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 6205-6209, 6224-6225; DE-TRACE-DENSITY-
    UNDERDETERMINATION [T]]

- requirement_id: OB-27
  # quasinormal mu decision (needs external shadow measurement
  # + public inference rule)
  owning_item_id: QNM-LEAVER-MU [O]               # FOLLOWUP; BLOCKED
  value_state: UNRESOLVED
  basis_item_ids: [CANON.md 6512-6515]

# ---- Empirical tripwires ([H]; own no manifest slot; cannot be worked, only fire) ----
- requirement_id: OB-28
  # dark-energy equation of state w = -14/15 constant
  owning_item_id: DE-W-CONSTANT [H]
  value_state: NOT_APPLICABLE
  basis_item_ids: [REGISTRY row 296 — empirical-fire-only falsifier (DESI/DES/
    Euclid/CMB-S4 rules, probes/P-DE-W-ARMING-1); owns no contract slot; current
    witnesses fire nothing (FRONTIER.md L66-68)]

- requirement_id: OB-29
  # scalar tilt n_s - 1 = -5 alpha
  owning_item_id: NS-TILT [H]
  value_state: NOT_APPLICABLE
  basis_item_ids: [REGISTRY row 166 — empirical-fire-only falsifier (CMB-S4); owns
    no contract slot]

- requirement_id: OB-30
  # lambda-adic cocycle angle grid (RH-adjacent carrier)
  owning_item_id: LAMBDA-COCYCLE-ANGLES [H]
  value_state: NOT_APPLICABLE
  basis_item_ids: [REGISTRY row 225 — ENRICHMENT lane, mathematical-fire-only; on
    no manifest-critical path (FRONTIER.md L117-119)]

# ---- Ownerless holes surfaced by this instance (NOT live frontier rows) ----
- requirement_id: OB-31
  # record and stage ownership for the registered linear/binary readouts
  # (section 3.2, holes H1-H2): no registered record owns either output and no
  # registered claim assigns a stage owner
  owning_item_id: UNRESOLVED                      # no registered owner exists —
                                                  # this ownerless hole is a primary
                                                  # diagnostic finding of this
                                                  # instance
  value_state: UNRESOLVED
  basis_item_ids: [READING-SPLIT [D] (CANON.md 1092-1096); CODEC-TR4 [T];
    TIME-CUT-READING [D]; CANON.md 504-505 (independent stage and leg axes)]

- requirement_id: OB-32
  # physical photon propagator: the only registered route is falsified
  # (physics_manifest.propagator_id NOTE, section 8) and no [O] successor exists
  owning_item_id: UNRESOLVED                      # no registered owner exists —
                                                  # this ownerless hole is a primary
                                                  # diagnostic finding of this
                                                  # instance
  value_state: UNRESOLVED
  basis_item_ids: [PHOTON-KAPPA-LEMMA [F]; PHOTON-WINDOW-PROOF [F] (CANON.md
    3700-3714); a new route requires a new registered claim]
```

---

## 12. RESOLUTION LEDGER

### 12.1 Counts per block

Counting convention — every slot value falls in exactly one of four value-classes:

- **public (counted RESOLVED)**: the slot cites a public v60 identifier (claim ID,
  `DEF-*` item, `gate_id`, the pinned tag, an allowed enum/state literal, an
  explicitly declared literal value such as `[]`/`FALSE`, or an ambient standard
  mathematical object per the §2 note). Scope-limited and candidate-declared
  citations count here, each flagged in `#` comments; canon-side adoption is
  tracked in `obligation_manifest[]`, never in this count.
- **draft-local**: the slot carries an identifier defined only in Appendix A
  (including `candidate_id` and `history_equivalence_id`). Counted separately —
  never as RESOLVED.
- **UNRESOLVED**: the literal.
- **NOT_APPLICABLE**: the literal, always with an item-first basis.

A list-valued slot is counted once, in the weakest class among its members
(UNRESOLVED < draft-local < public). The five §3.1 rows are counted at the full
fifteen slots each (eight preamble slots per row, per the §3.1 convention:
7 public + 1 draft-local each). `obligation_manifest[]` is counted per row by
`value_state`. Every figure below is reproducible by classifying the rows as
written under exactly these rules.

| Block | Rows / slots | public (RESOLVED) | draft-local | UNRESOLVED | NOT_APPLICABLE | Notes |
|---|---|---|---|---|---|---|
| top-level scalars | 6 slots | 3 | 2 (`candidate_id`, `history_equivalence_id`) | 1 (`coarse_graining_id`) | 0 | |
| carrier_manifest[] | 15 rows / 75 slots | 34 | 22 | 6 | 13 | UNRESOLVED = equality + coefficient of the three open record types MatterData/GeometryData/ObservableHistory |
| record_field_manifest[] | 6 rows / 90 slots | 57 | 22 | 0 | 11 | 5 MatterData_QDD rows + 1 auxiliary log row; the linear/binary/record-type holes are commentary (§3.2), not rows |
| stage_manifest[] | 3 rows / 18 slots | 12 | 1 | 5 | 0 | all three `map_id` + two totality domains UNRESOLVED; one totality domain named (K_QDD, restriction only) |
| leg_manifest[] | 3 rows / 15 slots | 12 | 3 | 0 | 0 | all three leg maps cite registered referents; D_linear/D_binary owned fields are draft-local candidates whose record owners are the OB-31 hole |
| bridge_manifest[] | 12 rows / 120 slots | 74 | 0 | 46 | 0 | BR-01..03 closed/dictionary; BR-04..10 open gates with undeclared endpoints; BR-11/12 gateless; plus 3 declared non-bridges (§6.4) |
| quadratic_manifest | 12 slots | 12 | 0 | 0 | 0 | candidate declarations via DEF-QDD-*; canon-side adoption wholly open under OB-01 |
| physics_manifest | 5 slots | 4 | 0 | 1 (`detector_id`) | 0 | finite-chain/graph scope flagged inline; photon propagator route [F] -> ownerless hole OB-32 |
| measure_manifest | 4 slots | 1 (`metrology_id`, dimensionless only) | 0 | 3 | 0 | SI clause inside metrology also open (OB-04) |
| closure_manifest | 4 slots | 3 | 1 (`terminality_basis_id`, interface clause CANON.md 473) | 0 | 0 | physical terminality basis open (OB-10) |
| obligation_manifest[] | 32 rows | 0 | 0 | 29 (27 [O] + 2 ownerless holes) | 3 ([H] tripwires) | complete cover of the v60 live frontier + OB-31/OB-32 with `owning_item_id: UNRESOLVED` |

Headline: **no block is fully closed at canon-adoption level.** The blocks that look
most resolved (quadratic_manifest 12/12, closure_manifest 3 public + 1 draft-local)
are resolved as *candidate declarations over public referents*; their canon-side
adoption is exactly rows OB-01 and OB-10 of the obligation manifest. Everything
probability-bearing, dimensionful, or detector-facing is UNRESOLVED with a named
owner — except the two ownerless holes OB-31/OB-32, which have none.

### 12.2 The diagnostic payload — unresolved slot → owning live frontier row

This table is the exact software backlog between Public Canon v60 and a fully
RESOLVED decoder-completion manifest (= this draft's operationalization of the
distance to "complete physics" at the interface level; the canon itself defines no
such distance).

| # | Unresolved manifest slot | Owning live frontier row | Queue (R4) |
|---|---|---|---|
| 1 | `quadratic_manifest` (adoption + closure of all 12 slots); `record_field_manifest[MatterData_QDD].write_map_id` adoption; `stage_manifest[D_matter].map_id` | QUADRATIC-DECODER-DATA [O] | ROOT; STOP |
| 2 | `measure_manifest.measure_id` (+ normalization, binary/census leg); BR-09 map | ENTROPY-LAYER-BRIDGE [O] | ROOT; STOP |
| 3 | `measure_manifest.measure_id` (color L4→L6); BR-07 map | COLOR-MEASURE-SELECTION [O] | ROOT; STOP |
| 4 | `measure_manifest.metrology_id` — SI clause; every dimensionful claim | METRO-EDGE-SCALE [O] | FOLLOWUP; BLOCKED |
| 5 | `measure_manifest.scheme_id` | SCHEME-DICTIONARY [O] | ROOT; STOP |
| 6 | `coarse_graining_id`; reduction-equivalence semantics of every L5-consuming slot | METRO-REDUCTION-CALCULUS [O] | ROOT; STOP — deepest choke point |
| 7 | admissible-class quantifier for metrology totality claims | METRO-ADMISSIBILITY [O] (R1–R8) | FOLLOWUP; STOP |
| 8 | `measure_manifest.normalization_id`; BR-08 map | METRO-ADMISSIBILITY-DIM [O] | FOLLOWUP; STOP |
| 9 | `physics_manifest.detector_id` (O1 sampling); BR-12 gate | QDD-INSTRUMENT-APPARATUS [O] | FOLLOWUP; STOP |
| 10 | `closure_manifest.terminality_basis_id` (physical half); `ObservableHistory.emit_rule` physics | QDD-TERMINAL-EVENT-SEMANTICS [O] (O2a) | FOLLOWUP; STOP |
| 11 | `physics_manifest.detector_id` (completeness half) | QDD-INSTRUMENT-CLASS-COMPLETENESS [O] (O2b) | FOLLOWUP; STOP |
| 12 | `stage_manifest[D_geom].map_id`; `GeometryData` schema; BR-04 | CURVATURE-OPERATOR-CANONICAL [O] | ROOT; STOP — literal UNIQUE/NONUNIQUE/EMPTY verdict |
| 13 | BR-05 (L2→L1 Hodge-home selection) | TRACEKERNEL-CURVATURE-FORCING [O] | FOLLOWUP; BLOCKED by #12 |
| 14 | `read_convention_id` forced-vs-free; BR-10 | MINIMAL-READ-DERIVATION [O] | ROOT; STOP |
| 15 | `stage_manifest[D_clock].map_id`; `ObservableHistory` schema; gravity `physics_manifest.source_id` channel | SQRT-PHI-TIME-GRAVITY [O] | FOLLOWUP; STOP |
| 16 | tensor `physics_manifest.source_id`/`current_id` | TT-SOURCE [O] | FOLLOWUP; BLOCKED |
| 17 | probability-bearing `bridge_manifest.gate_ids` (policing) | BELL-CAUSAL-ACCOUNTING [O] | ROOT; STOP |
| 18 | (sector) substrate coupling — sufficiency test | QUANT-SUBSTRATE [O] | ROOT; **READY** |
| 19 | (sector) generation count; BR-06 | GENERATIONS-L3 [O] | ROOT; **READY** |
| 20 | (sector) tensor normalization → numerical r_T(k) | TT-VECTOR-STATE-NORMALIZATION [O] | ROOT; **READY** |
| 21 | (sector) crossing count | DRESS-CROSSCOUNT [O] | FOLLOWUP; BLOCKED |
| 22 | (sector) alpha_s running (scheme dependency inferred from REGISTRY row 168's closure condition; see OB-22) | ALPHA-S-RUNNING [O] | FOLLOWUP; BLOCKED |
| 23 | (sector) neutron delta | NEUTRON-DELTA-EM [O] | FOLLOWUP; BLOCKED |
| 24 | (sector) inhomogeneous FRW source | FRW-INHOM [O] | FOLLOWUP; BLOCKED |
| 25 | (sector) proton residual (schema unfrozen) | PROTON-RESIDUAL-IS-QCD [O] | FOLLOWUP; STOP |
| 26 | (sector) DE conformal weight (circularity-fenced) | DE-CONFORMAL-WEIGHT [O] | FOLLOWUP; STOP |
| 27 | (sector) QNM mu (needs external measurement) | QNM-LEAVER-MU [O] | FOLLOWUP; BLOCKED |
| — | tripwires owning no slot | DE-W-CONSTANT [H], NS-TILT [H], LAMBDA-COCYCLE-ANGLES [H] | fire-only |

**Structure of the backlog** (consistent with R4 §3.3): rows 1–17 are the manifest-
critical core (12 core owners + TT-SOURCE + BELL-CAUSAL-ACCOUNTING + the two METRO
intermediates + the tracekernel refinement); rows 18–20 are the three READY ROOT
sufficiency tests that own sector slots only; rows 21–27 are sector fields blocked
on new constructions or external inputs. The single deepest formal dependency is
row 6 (METRO-REDUCTION-CALCULUS): rows 4, 7, 8, and the NEG branch of row 14 all
quantify over the equivalence/class it must define. The forced-decoder question of
the programme owner is natively instrumented in rows 12 (UNIQUE/NONUNIQUE/EMPTY),
14 (forced read), 4 (canonical selector NEG = "no canonical selector exists"), and
3 (no lift / more than one inequivalent lift). **Outside this table sit the two
ownerless holes OB-31 and OB-32** (sections 3.2 and 8): they map to no live
frontier row at all — see §12.3 point 3.

### 12.3 What this draft demonstrates

1. **The contract is instantiable today, with a disclosed residue.** Every block
   can be instantiated, and most slots can be filled contract-legally — no bare
   nulls, no invented public identifiers, totality only relative to named domains,
   all cross-layer rows carrying GATES.tsv ids or the literal UNRESOLVED. The
   residue that cannot be filled contract-legally — record and stage owners for
   the linear/binary readouts, whose enums and one-owner rule (CANON.md 609–613)
   admit no legal row — is itself the finding, and is stated as non-manifest
   commentary in §3.2, not as rows.
2. **The resolvable surface is real but one-legged.** The quadratic leg can cite a
   complete typed referent set (DEF-QDD-*, keystone QDD-ALGEBRAIC-FACTORIZATION [T]);
   the linear and binary legs have registered maps but no registered record fields;
   the geometry and clock stages have no registered maps at all.
3. **The UNRESOLVED set maps 1:1 onto the live frontier, with two disclosed
   exceptions.** All 27 [O] rows appear as owners of concrete manifest slots or
   sector fields; the 3 [H] rows own nothing (fire-only). No unresolved slot lacks
   an owner **except (i) the linear/binary record-ownership and stage-ownership
   holes of §3.2, which no live frontier row owns (OB-31, owning_item_id:
   UNRESOLVED), and (ii) the physical photon propagator, whose only registered
   route is [F] (PHOTON-WINDOW-PROOF, CANON.md 3700–3714) and which has no [O]
   successor (OB-32, owning_item_id: UNRESOLVED) — both ownerless holes are
   themselves primary diagnostic findings of this instance.** No owner lacks a
   slot except the three READY sufficiency tests — which is itself the diagnostic:
   the backlog is fully ledgered, and the interface bottleneck (measure, sampling,
   SI) is exactly where the canon says it is.
4. **Nothing here is evidence.** Per CANON.md 634–645, this instance asserts no
   existence, totality, uniqueness, canonicity, or completeness, and changes no
   status.

Points 1–3 are claims about this draft document, not about the canon; they carry
no status.

---

## Appendix A — Draft-local identifier lexicon

Every identifier below is **draft-local**: coined by this draft, resolving only to
the definition on this page and to no public v60 item (mirroring `candidate_id`,
section 1). Slots carrying one are counted **draft-local** in §12.1, never
RESOLVED. Each object is named exactly once here; grounding citations are to
CANON.md unless another file is named. Ambient standard mathematical objects are
covered by the §2 ambient-objects note, not by this lexicon.

**Top-level and field names**

- `DRAFT-TWISTJ-DECODER-MANIFEST-2026-08-22` — this document (`candidate_id`).
- `literal-forward-orbit-equality` — literal equality of forward orbit sequences;
  the finest equivalence on K. Grounded in CANON.md 455 + DEF-QDD-DOMAIN-K0.
- `linear_readout_tr4` — candidate field name, §3.2 hole H1: F_5-valued covector
  reading on checkpoints via `dl-map-pr-checkpoint` (CODEC-TR4 [T]).
- `binary_cut_census` — candidate field name, §3.2 hole H2: the
  `dl-carrier-binary-pair-channel` reading of the derived drive word
  (TIME-CUT-READING [D]).
- `derived-orbit-logs` — record name for the auxiliary log record, §3.3
  (DEF-LOG-STREAM; CANON.md 310-313).
- `log_lambda` — field name of the auxiliary log record, §3.3.

**Equalities**

- `dl-eq-omega` — componentwise equality on Omega = N_0 x F_5^6 (n literal, psi
  componentwise).
- `dl-eq-integer` — integer equality on N_0.
- `dl-eq-f5-componentwise` — componentwise F_5 equality on F_5^6.
- `dl-eq-q4-componentwise` — componentwise rational equality on Q^4 / V_eff.
- `dl-eq-qzeta5-field` — field equality in Q(zeta_5).
- `dl-eq-a8-ring` — ring equality in Z[zeta_8]/5.
- `dl-eq-a4-ring` — ring equality in Z[i]/5.
- `dl-eq-wp-linear` — F_p-linear equality with form g_p on (W_p, g_p).
- `dl-eq-tag` — tag equality on the 2-element tag set.
- `dl-eq-rational` — rational equality on Q_{>=0}.
- `dl-eq-branch-pair` — ordered componentwise rational equality on Q_{>=0}^2
  ("no swap", DEF-QDD-MATTER-RECORD).
- `dl-eq-density-tagged` — tagged matrix equality (ZERO_DENOMINATOR | DENSITY over
  M_4(Q), DEF-QDD-MATTER-RECORD).
- `dl-eq-normweight-tagged` — tagged pair equality (ZERO_DENOMINATOR | NORMALIZED
  over Q^2, DEF-QDD-MATTER-RECORD).
- `dl-eq-sequence` — sequence equality on {0,1}^N_0.

**Maps**

- `dl-map-odometer-embedding` — the distinguished forward orbit 0,1,2,... of the
  2-adic odometer embedded in Z_2 (ODOMETER-INTERNALIZED [D], 315-321).
- `dl-map-pr-checkpoint` — pr_checkpoint(n, psi) = psi (CANON.md 308-310).
- `dl-map-orbit-embedding` — omega_0 -> (U^k omega_0)_{k>=0}, Omega into K
  (CANON.md 455).
- `dl-map-pointed-orbit-inclusion` — inclusion of pointed orbits started at counter
  0 (head n = 0), K_QDD into K (DEF-QDD-DOMAIN-K0).
- `dl-map-qzeta5-extension` — the field extension Q -> Q(zeta_5).
- `dl-map-qcarrier-image` — the image inclusion im(Q_QDD|V_eff) into
  M_4(Q) x M_4(Q).
- `dl-map-mod5-reduction` — reduction modulo 5 on the respective parent ring
  (Z[zeta_8] -> A_8; Z[i] -> A_4).
- `dl-map-trace-radical` — passage to the radical of the residual trace form
  (TRACEKERNEL-RESIDUAL-FORM [T]).
- `dl-map-counter-projection` — the counter projection (n, psi) -> n ("D_clock
  reads the counter projection", CANON.md 472-473).

**Coefficient objects, carriers, field types**

- `dl-coeff-omega` — the coefficient pair F_5 (fiber), N_0 (counter); two objects,
  named once here.
- `dl-coeff-qdd-record` — Q with typed components Q_{>=0}, Q^2, M_4(Q)
  (DEF-QDD-MATTER-RECORD).
- `dl-coeff-a8-born` — F_25-side residue ring; Born involution = conjugation
  (BORN-HALF-ANGLE [T], BORN-RESIDUAL-SPLIT [T]).
- `dl-coeff-a4-born` — residue ring with conjugation = Born involution
  (BORN-RESIDUAL-SPLIT [T]).
- `dl-carrier-tag2` — the 2-element tag set {ZERO_SUPPORT, SUPPORTED}.
- `dl-carrier-tagged-m4q` — tagged M_4(Q) (ZERO_DENOMINATOR | DENSITY).
- `dl-carrier-tagged-q2` — tagged Q^2 (ZERO_DENOMINATOR | NORMALIZED).
- `dl-carrier-binary-pair-channel` — the binary pair channel
  (theta_{n-1}, theta_n) with exact census densities in Q (TIME-CUT-READING [D],
  CENSUS-313 [C]).
- `dl-type-support-tag` — field type: tag in {ZERO_SUPPORT, SUPPORTED}.
- `dl-type-branch-pair` — field type: ordered pair (LOW, HIGH) in Q_{>=0}^2,
  "no swap".
- `dl-type-density-state` — field type: tag ZERO_DENOMINATOR | tag DENSITY carrying
  a 4x4 rational matrix.
- `dl-type-normweight-state` — field type: tag ZERO_DENOMINATOR | tag NORMALIZED
  carrying a rational pair.
- `dl-type-log-stream` — field type: (lambda(U^k omega_0))_{k>=0} for a registered
  binary observable.

**Emit rules and bases**

- `dl-emit-per-pointed-orbit` — one record per pointed orbit at head n = 0
  (DEF-QDD-DOMAIN-K0).
- `dl-emit-log-definitional` — definitional projection; gate closed by construction
  (GATE-L1-L5-LOG-PROJECTION).
- `dl-basis-interface-terminality` — the declared stage-contract terminality clause
  "D_clock reads the counter projection plus the accumulated records and is
  terminal" (CANON.md 473); interface layer only.

---

**Revision note.** Rev 2, 2026-08-22: conformance fixes applied per adversarial
audit V1 (schema enums, bridge-row completeness, ownerless-hole disclosure, ledger
recount).
