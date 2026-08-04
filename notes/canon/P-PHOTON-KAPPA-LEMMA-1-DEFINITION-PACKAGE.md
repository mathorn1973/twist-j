# P-PHOTON-KAPPA-LEMMA-1 definition package (NON-CANONICAL)

Status: `DRAFT / DEFINITION PACKAGE / ISSUE-200 REVIEW INPUT / NO PROBE
RUN / NO FORMAL PIN / NO CANON CHANGE`

Date: 2026-08-04

This package proposes the complete negative-certificate `S_kappa`
resolution that issue
[#200] and `notes/canon/P-PHOTON-KAPPA-LEMMA-1-PREDEFINITION.md`
(sections 4, 10, 11) require before the reserved probe
`P-PHOTON-KAPPA-LEMMA-1` may be pinned. It is review material: it
authorizes no branch, no probe directory, no formal execution, and no
Canon edit. Every labeled status below is candidate vocabulary.

## 1. Authority, routing, and review pin

```text
Canon:                    Public Canon v35
state:                    ACTIVE
authority:                mathorn1973/twist-j main
base main:                7c5e1560d56ddf801bf55079674a90682c4b58ee
tag:                      canon-v35
content commit:           c94fc18ed3b5be1706397e4cc8666b6123858918
Canon SHA-256:            f301ba047ddd3ce1a17d155baed7506a2f889ac48f660797c666b422b49be099
Canon bytes:              173294
parent owner:             PHOTON-WINDOW-PROOF [O], unchanged in v35
reservation:              issue #200 (collision lock, OPEN)
sibling lock:             issue #201 (roughening), untouched here
reserved probe:           P-PHOTON-KAPPA-LEMMA-1
reserved branch/path:     probe/P-PHOTON-KAPPA-LEMMA-1,
                          probes/P-PHOTON-KAPPA-LEMMA-1/
this file:                notes/canon/P-PHOTON-KAPPA-LEMMA-1-DEFINITION-PACKAGE.md
witness input (data):     notes/kappa-witness-2026-08-03/witness_6_3_6_6.json
witness SHA-256:          9b664f16830d2b562949933e40b4f1460d9da5645a88beff7bca347b70320313
witness bytes:            280106
formal pin/run/result:    ABSENT / NOT AUTHORIZED
target release for fold:  first unsealed release after the probe merges
                          (v36 or later; v35 is activated and immutable)
```

The owner disposition R0A-R5B (predefinition section 9) is inherited
unchanged and is the basis of every proposed ruling below. The exact
negative-certificate surface is complete by value; the load-bearing
subset inclusion and the lane-versus-probe outcome ruling become an
owner freeze only through explicit approval in issue #200. All counts
and hashes must be revalidated at pin time against the then-current
public `main`.

## 2. Complete negative-certificate S_kappa resolution

Every slot of the predefinition section 4 tuple consumed by this
negative-certificate probe is exact. No slot on this probe surface
remains `UNRESOLVED`; explicit owner acceptance is still pending. No
positive universal proof or classification is claimed here.

```text
lattice             infinite Z^4; finite-support cubical chains        (R2A)
cells               vertices v; edges e = (v, d), d in 0..3; faces
                    f = (v, a, b), a < b; all coordinates integers
orientations        the public convention of
                    reproduce/photon-electron/verify.py:
                    partial f_(a,b)(v) = e_a(v) + e_b(v+e_a)
                                        - e_a(v+e_b) - e_b(v);
                    edge (v, d) runs v -> v+e_d with vertex boundary
                    (v+e_d) - (v)
partial             as above; coefficientwise over Z; partial o
                    partial = 0

face_alphabet       {0, +1, -1}                                        (R0A)
BaseCurrent         { j in C_1^c(Z^4; {0,+1,-1}) :
                      j != 0 and partial j = 0 }
Fill(j)             { n in C_2^c(Z^4; {0,+1,-1}) :
                                partial n = 5j }
ParentWorldline     { j in BaseCurrent : Fill(j) != empty }.
                    This is the complete owner-selected chain carrier
                    quantified by (K1).  Its support may have any
                    finite number of connected components; no
                    connectedness, degree-2, or vertex-simplicity
                    condition is imposed here.  The registered public
                    parent status and scope remain unchanged.
CertificateCurrent  { j in ParentWorldline : supp(j) is connected as
                    an undirected graph }.  This is R3A's first
                    falsifier subclass, not a replacement for or
                    narrowing of ParentWorldline.  Repeated vertices
                    and every even support degree up to 8 are
                    admissible; repeated support edges are excluded by
                    the coefficient alphabet.
certificate_pair    (j,n) with j in CertificateCurrent and n in
                    Fill(j); the serialized n witnesses membership in
                    ParentWorldline.
subset_inclusion    CertificateCurrent is explicitly a subset of
                    ParentWorldline.  Because a ternary closed current
                    has balanced directed support, connectedness gives
                    an orientation-matching closed Hierholzer traversal
                    using every support edge exactly once.  Explicit
                    owner approval of this carrier and inclusion in
                    issue #200 is required before the formal pin.
worldline_equality  coefficientwise chain equality over Z; translated
                    currents are distinct chains, while every predicate
                    used here is translation invariant
components          unrestricted finite component count on
                    ParentWorldline; exactly one connected support
                    component on CertificateCurrent
multiplicity        |j_e| <= 1 by the alphabet (edge-simplicity);
                    no other multiplicity notion exists on this
                    surface
backtracks          chains are primary.  Walk backtracks, repeated
                    traversal, and coefficients outside {0,+1,-1}
                    are not part of this carrier
repetitions         repeated traversal not part of the carrier;
                    repeated vertices admissible as stated
crossings           admissible (repeated vertices)
winding             trivial: finite support in Z^4
walk_to_chain       none.  The checker derives a Hierholzer traversal
                    only for CertificateCurrent as a membership
                    certificate; it is never input and makes no
                    one-walk assertion about a disconnected
                    ParentWorldline

L                   L(j) = |supp(j)|                                   (R1A)
L_domain            positive integers; on the ternary surface the
                    support and l1 gradings coincide

charge_equation     partial n = 5j, coefficientwise equality over Z,
                    not merely mod 5.  "Charge 5" in the parent scope
                    is read exactly as this equation, consistent with
                    MONOPOLE-FIFTHS [T]
filling_existence   required by membership in ParentWorldline and
                    witnessed by the serialized n for every admitted
                    certificate pair
empty_filling_rule  a BaseCurrent with Fill(j)=empty is outside
                    ParentWorldline.  F_occ is not evaluated outside
                    its domain and no extended-integer value is
                    introduced
face_support        supp(n)
F                   F(n) = |supp(n)|
F_occ               F_occ(j) = min { |supp(n)| : n in Fill(j) } for
                    j in ParentWorldline, a positive integer by
                    well-ordering.  The
                    certificate route uses only the exact upper bound
                    F_occ(j) <= |supp(n)| for the exhibited n; no
                    minimum solver is used or claimed               (predef. 9)

kappa_domain        kappa = a/b with a, b coprime positive integers
coefficient_normalization
                    integer gate forms, frozen:
                    (K1)  b F_occ(j) >= a L(j) for every j in
                          ParentWorldline
                    (K2)  2^(4a) > 2401^b        (2401 = 7^4)
                    No decimal approximation of log2(7) is a
                    threshold certificate

universal_reduction not required for the negative route; one accepted
                    certificate pair (j,n), with j in
                    CertificateCurrent and n in Fill(j), is enough to
                    refute universal K1 on ParentWorldline by subset
                    inclusion.  The
                    completeness burden of the counterexample method
                    is carried entirely by the exclusion lemma of
                    section 3, which covers every admissible (a, b)
                    at once.  No positive universal proof or
                    reduction is claimed or attempted here
completeness_method for this probe: exact certificate verification
                    plus the exclusion lemma; both are total and
                    deterministic on the frozen inputs

counterexample_family
                    by owner definition for this lane, any finite
                    nonempty set W of pairs (j_i,n_i) with j_i in
                    CertificateCurrent, n_i in Fill(j_i), and
                        2^(|supp n_i|) <= 7^L(j_i)
                    as exact integers.  Singleton families are
                    expressly admitted.  The pinned family is
                    W={(j_*,n_*)}, the archived pair with L=3240,
                    F=7993, SHA-256 and byte count from section 1.
                    No pump, asymptotic sequence, or second member is
                    required
deterministic_order the pinned witness has j entries sorted strictly
                    lexicographically by (vertex, direction) and n
                    entries by (vertex, a, b); C1 checks this raw-list
                    order and the complete canonical JSON encoding.
                    C6 independently freezes the fixture byte count and
                    SHA-256.  The canonical fixture has no terminal LF;
                    the transcript is line-deterministic and does have
                    one terminal LF
certificate_schema  section 5
certificate_checker section 6
```

## 3. The exclusion lemma

**Lemma (integer-exact).** Let `j` be in `ParentWorldline` and let
`n` be in `Fill(j)` with `2^F <= 7^L`, where `L=L(j)>=1` and
`F=|supp(n)|`. For every coprime positive integer pair `(a,b)`
satisfying (K2), (K1) fails at this `j`.

**Proof.** Since `n in Fill(j)`, `F_occ(j) <= F`. Assume (K1); then
`b F >= b F_occ(j) >= a L`. Assume (K2); since the fourth power is
strictly increasing on positive integers, `2^(4a) > 7^(4b)` is
equivalent to `2^a > 7^b`. Raising to the L-th power,
`2^(aL) > 7^(bL)`. Then

```text
2^(bF) >= 2^(aL) > 7^(bL) = (7^L)^b,
```

so `(2^F)^b > (7^L)^b`, hence `2^F > 7^L`, contradicting the
certificate inequality. Every step is a comparison of positive
integers. QED.

Consequence: one admitted pair, and therefore the pinned singleton
family, excludes **every** admissible `kappa` with
`2^(4 kappa)>2401` from obeying universal (K1) on ParentWorldline.
Connectedness is used only to certify membership in the explicit
falsifier subclass.  This is exactly the predicate issue #200
requires the preregistration to fix ("including how it excludes every
admissible kappa").

## 4. Outcome predicates and this probe's decision map

Proposed owner ruling on predefinition section 11 item 7: the four
outcome predicates are lane-wide.  "Remain reachable" means that this
negative-certificate probe neither deletes nor redefines the positive
and candidate-refutation routes; it does not require every individual
probe to emit every lane outcome.  This ruling must be approved
explicitly in issue #200 before the formal pin.

The lane predicates are frozen at least as strong as the issue #200
block:

```text
KAPPA-PROVED       a complete exact universal proof supplies one
                   admissible a/b satisfying (K1) on all of
                   ParentWorldline and satisfying (K2)
BELOW-THRESHOLD    an exact admitted counterexample family (section
                   2; singleton allowed) excludes every admissible
                   a/b satisfying (K2) from universal (K1)
CANDIDATE-REFUTED  a separately pinned proposed coefficient,
                   reduction, or positive proof fails, but the exact
                   result does not exclude every a/b satisfying (K2)
STOP               authority, collision, carrier membership, typing,
                   pin, proof-completeness, security, hash,
                   transcript, or reproduction requirements fail
```

`P-PHOTON-KAPPA-LEMMA-1` is specifically a pinned
negative-certificate verification probe.  Its complete decision map,
frozen before any run, is:

```text
C1-C7 and S1-S5 PASS on the pinned singleton witness and every
required execution, transcript, and reproduction gate passes
    -> BELOW-THRESHOLD

any schema, carrier, boundary, count, inequality, hash, systematics,
execution, transcript, or reproduction failure
    -> STOP
```

This probe cannot emit KAPPA-PROVED or CANDIDATE-REFUTED.  Those
remain lane-wide outcomes available only to separately reserved,
defined, and pinned future work; this package creates or authorizes no
such work.  A missing, altered, or failing pinned witness is not a
scientific refutation of another coefficient or proof and therefore
lands on STOP, never CANDIDATE-REFUTED.  This asymmetry prevents
outcome shopping.

## 5. Certificate schema

One canonical JSON file, UTF-8 without BOM, no floating point anywhere:

```text
{
  "P": int, "m": int, "C": int, "D": int,   inert construction
                                            metadata: schema-checked and
                                            byte-pinned, but not used as
                                            scientific content
  "L": int, "F": int,                       declared counts
  "j": [ [[x0,x1,x2,x3], d, c], ... ],      edges: base vertex,
                                            direction 0..3,
                                            coefficient in {-1,+1}
  "n": [ [[x0,x1,x2,x3], a, b, c], ... ]    faces: base vertex,
                                            0 <= a < b <= 3,
                                            coefficient in {-1,+1}
}
```

The top-level key order is exactly `P, m, C, D, L, F, j, n`; no other
key or duplicate JSON object name is allowed.  Every numeric atom has
strict Python type `int`, so booleans and floating-point values are
rejected.  After parsing, the raw bytes must equal exactly

```text
json.dumps(parsed, ensure_ascii=True, allow_nan=False,
           separators=(", ", ": ")).encode("ascii")
```

This canonical encoding has no terminal newline.  It fixes key order,
list order, whitespace, ASCII escaping, and numeric spelling before C6
applies the independent full-file byte-count and SHA-256 pin.

Scope block (normative for admissibility):

```text
edge coefficients: {-1,0,+1}; zero entries must not be serialized
repeated edges:    forbidden (keys unique)
repeated vertices: allowed
vertex degree:     even, not necessarily 2
connectivity:      support graph of j connected
```

## 6. Certificate checker

`verify.py`, Python standard library only.  The formal command from the
repository root is exactly

```text
python3 -B probes/P-PHOTON-KAPPA-LEMMA-1/verify.py
```

The verifier accepts no arguments and locates the adjacent pinned JSON
relative to `__file__`.  Any argument emits exactly `usage: verify.py`
plus LF on stderr and exits 2; this is a usage error, not a scientific
outcome.  PASS buffers deterministic ASCII/LF stdout, exits 0, and has
empty stderr; a gate failure emits no scientific outcome on stdout.
Checks, each of which must attempt refutation and abort on failure:

```text
C1  canonical JSON: UTF-8 without BOM; exact ordered top-level keys;
    no duplicate object names; every numeric atom has type(x) is int;
    exact list shapes;
    a < b and d in 0..3; unique edge and face keys; coefficients exactly
    in {-1,+1}; raw j keys strictly lexicographically increasing by
    (vertex,direction), raw n keys by (vertex,a,b); raw bytes equal the
    canonical encoder of section 5
C2  j ternary and nonzero; partial j = 0 at every vertex
C3  support graph of j connected; every vertex degree even; a
    Hierholzer closed traversal using every support edge exactly
    once with orientation matching the sign (the worldline
    realization certificate)
C4  n ternary with support cardinality 7993
C5  partial n = 5j coefficientwise on every edge of Z^4: exactly the
    support edges receive +-5 with the correct sign, and no other
    edge receives a nonzero value.  Two separately implemented boundary
    paths must agree on partial j, partial n, support counts, and the
    equation; an independent expansion also verifies partial(partial n)=0
C6  declared L and F equal the computed counts and the pinned values
    L = 3240, F = 7993; raw byte count is 280106 and the file's SHA-256
    equals the pinned value of section 1
C7  2^F <= 7^L compared as exact big integers; additionally
    B = max{m : 2^m <= 7^L} is printed as 9095 with F <= B and
    slack B-F = 1102
```

The two reference implementations are the reviewed copies on public
`main` (merged through pull request #266), pinned by content hash:

```text
notes/kappa-witness-2026-08-03/verify_witness.py
  SHA-256 ff462d724f8c724e5df1987d32bbfa3e71518fbec547b00bc1195b567d9c74c0
notes/kappa-witness-2026-08-03/adversarial_check_fresh.py
  SHA-256 c6ae055d30aaf8ec55020db4df1e250f5a65f805b73e521b3db52b59f5c7b9cb
```

Both PASS on the pinned witness. Any branch-local pre-review copies
are superseded by these. The accepted probe verifier is to be
assembled from them and then separately reviewed, per issue #200
item 10.

## 7. Systematics and negative controls

To be executed by the accepted verifier or recorded as reviewed
sublemmas, all exact:

```text
S1  regression: embed the nine KAPPA-SHAPES loops and the public
    face-incidence algorithm.  Require closed edge-simple loops, the
    exact (name,L,LB) rows
      (square-1x1,4,17), (ladder-1x2,6,26),
      (ladder-1x3,8,35), (ladder-1x4,10,44),
      (ladder-1x5,12,53), (ladder-1x6,14,62),
      (square-2x2,8,36), (skew-hexagon,6,24),
      (staircase,8,31),
    exact 2^LB > 7^L for every row, and min(LB/L)=31/8
S2  out-of-carrier control: on periods (3,4,4,4), set
    sigma(x)=(-1)^(x1+x2+x3), j0(x)=sigma(x),
    n01(x)=sigma(x), n02(x)=sigma(x), and
    n03(x)=(sigma(x)-1)/2.  Require the modular torus calculation to
    give partial n=5j and partial j=0 with 64 support components.
    Reinterpret the same representative keys with ordinary
    nonperiodic Z^4 boundaries and require partial j != 0.  The control
    is rejected both by the ambient carrier and by connectivity
S3  five in-memory mutation controls, bypassing only the raw C6 pin and
    exposing no bypass through the CLI.  Flip first face
    [[0,-2,-1,0],0,2,+1] to coefficient -1; require C1-C4 PASS, then
    C5_BOUNDARY.  Delete first edge [[0,-2,0,0],0,-1]; require C1 PASS,
    then C2_NOT_CLOSED.  Duplicate the first face immediately adjacent;
    require C1_DUPLICATE_FACE.  Change the first edge coefficient to 2;
    require C1_COEFFICIENT.  The exact fifth control uses the
    first bridge descriptor ((1,1,0,0),d01=0,d23=3): delete bridge
    edges ((1,1,0,0),3,+1) and ((2,1,0,0),3,-1), then restore the
    canceled in-plane edges ((1,1,0,0),0,+1) and
    ((1,1,0,1),0,-1), and re-sort j.  Require C1-C2 PASS; this inverse
    reroute preserves partial j=0 and must fail exactly C3_DISCONNECTED
S4  determinism: read and evaluate the pinned raw input twice; compare
    immutable result records and rendered transcripts byte for byte.
    The committed EXPECTED.txt and both architecture jobs later provide
    the stronger cross-process and cross-architecture check
S5  vocabulary control: the successful transcript contains exactly one
    outcome line, exactly `OUTCOME BELOW-THRESHOLD`, and contains none of
    the superseded alternative outcome vocabulary, including no
    `CANDIDATE-REFUTED` token
```

Vocabulary history: a pre-review branch version of the work note
`notes/KAPPA-CHECKERBOARD-ATTACK-2026-08-03.md` named the target
outcome CANDIDATE-REFUTED. The reviewed copy on public `main`
(merged through pull request #266) already targets BELOW-THRESHOLD
and asserts no outcome; no erratum against the public record is
needed. S5 remains as a checker-level control so the superseded
vocabulary cannot reappear in probe output.

## 8. PREREG.md skeleton (six fields, not yet committable)

```text
EQUATION:    (K1) b F_occ(j) >= a L(j) for every j in
             ParentWorldline;
             (K2) 2^(4a) > 2401^b; the exclusion lemma of section 3
             with its integer-exact proof; L, F, Fill, F_occ as in
             section 2
CODE:        the accepted verify.py of section 6, reviewed and
             committed with this preregistration before any formal
             gate execution
CARRIER:     BaseCurrent, Fill, ParentWorldline, and
             CertificateCurrent exactly by value; the explicit
             subset inclusion; the pinned singleton witness JSON
             with its SHA-256 and byte count as frozen input data
SYSTEMATICS: S1-S5 of section 7
THRESHOLD:   the lane-wide four-predicate owner ruling and the
             probe-local PASS -> BELOW-THRESHOLD / failure -> STOP
             map of section 4, frozen before output
LAYER:       L4 support only; no tick, stream, or measure quantity
             is consumed; no cross-layer lift; no named gate
```

## 9. What follows this package (for orientation, not authorized here)

1. Review and merge this package; public readback.
2. The owner records explicit approval in issue #200 of
   ParentWorldline, CertificateCurrent and its subset inclusion,
   repeated vertices, singleton counterexample families, the
   Fill(j)!=empty rule, and the lane-wide versus probe-local outcome
   ruling.  This authorizes only preparation of the accepted verifier,
   not a formal branch, pin, or run.
3. Assemble the exact accepted verifier at
   `notes/kappa-witness-2026-08-03/verify_probe_candidate.py` on a
   separately reviewed non-formal notes surface, merge it, and read
   back its public bytes and SHA-256.  Run only non-formal review
   checks there.
4. The owner accepts that exact verifier hash in issue #200 and
   explicitly authorizes creation of the reserved formal branch and
   preregistration pin.  Formal execution remains forbidden before
   remote pin readback.
5. Re-check authority, collisions, branch/issue/path locks
   (predefinition section 11 item 9) against then-current `main`.
6. Create `probe/P-PHOTON-KAPPA-LEMMA-1` and
   `probes/P-PHOTON-KAPPA-LEMMA-1/`; commit PREREG.md, the accepted
   verifier copied byte-identically at its owner-accepted public hash,
   and the witness JSON; push; confirm remote hashes, byte counts, and
   LF-normalized readback before any run.
7. Formal execution; EXPECTED.txt; RUN.md with neutral descriptors;
   RESULT.md with the decision-map outcome; one-probe pull request;
   the two GitHub architecture jobs supply the two-architecture
   record.
8. A later reviewed fold (v36 or later) would register whatever the
   frozen decision map output; only if that output is
   BELOW-THRESHOLD and every gate passes would the kappa route of
   PHOTON-WINDOW-PROOF close negatively per its registered
   falsifier, with the owner's separate disposition on the parent
   row's terminal state and on the sibling lock #201. No outcome is
   asserted here. A one-machine finite result enters at most at
   `C`; the exclusion lemma may be registered at theorem grade
   separately if reviewed as such.

## 10. Scope and safety firewall

This package:

- runs no verifier and executes no formal gate;
- creates no branch, probe directory, PREREG, claim, gate,
  dependency, or evidence record;
- changes no public Canon byte and no status;
- does not decide the parent row's terminal disposition and does not
  touch the roughening obligation or issue #201;
- claims no satisfaction of any Froehlich-Spencer import hypothesis;
- claims no massless phase, Coulomb window, continuum limit, photon
  propagator, or physical photon statement;
- registers no new physical photon carrier and introduces no carrier
  beyond the owner-selected R0A-R5B L4 chain surface; it introduces no
  spatial lift, FCC lattice, displacement support, shell weights,
  polarization, holonomy, time bridge, measure, or SI statement;
- does not equate the greedy incidence bound LB with F_occ (S1 uses
  LB only as a registered regression control);
- does not change CENTER-SPLIT-SELECTION;
- does not promote KAPPA-SHAPES [C], MONOPOLE-COST [C], or the
  archived witness beyond candidate standing;
- records no secret, credential, private path, machine nickname, or
  personal datum.

Public Canon v35 remains fully authoritative while this package is
reviewed.

[#200]: https://github.com/mathorn1973/twist-j/issues/200
