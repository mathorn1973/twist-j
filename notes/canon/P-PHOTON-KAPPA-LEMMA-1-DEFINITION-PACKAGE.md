# P-PHOTON-KAPPA-LEMMA-1 definition package (NON-CANONICAL)

Status: `DRAFT / DEFINITION PACKAGE / ISSUE-200 REVIEW INPUT / NO PROBE
RUN / NO FORMAL PIN / NO CANON CHANGE`

Date: 2026-08-04

This package proposes the complete `S_kappa` resolution that issue
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
unchanged and is the basis of every ruling below. All counts and
hashes must be revalidated at pin time against the then-current
public `main`.

## 2. Complete S_kappa resolution

Every slot of the predefinition section 4 tuple, in order. No slot
remains `UNRESOLVED`.

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

Worldline           admitted certificate current:
                    j in C_1^c(Z^4; {0,+1,-1}), j != 0,
                    partial j = 0, supp(j) connected as an undirected
                    graph.  Repeated vertices are admissible (any
                    even support degree, up to 8 in Z^4);
                    vertex-simplicity / degree-2 support is NOT
                    required.  This is the first falsifier subclass
                    of R3A and does not narrow the public parent.
worldline_equality  coefficientwise chain equality over Z
components          supp(j) connected (certificate subclass); the
                    parent's broader class is untouched; a
                    counterexample from a subclass of the admitted
                    class refutes the universal bound
multiplicity        |j_e| <= 1 by the alphabet (edge-simplicity);
                    no other multiplicity notion exists on this
                    surface
backtracks          not part of the carrier (predefinition section 9:
                    "Walk length, immediate backtracks, repeated
                    traversal, and coefficients outside {0,+1,-1}
                    are not part of this search carrier")
repetitions         repeated traversal not part of the carrier (same
                    sentence); repeated vertices admissible as
                    stated
crossings           admissible (repeated vertices)
winding             trivial: finite support in Z^4
walk_to_chain       none; chains are primary.  The optional
                    Hierholzer traversal in the checker is a derived
                    realization certificate (closed walk using every
                    support edge exactly once, orientations matching
                    the signs), exhibiting the current as one closed
                    edge-simple charge-5 worldline; it is output,
                    never input

L                   L(j) = |supp(j)|                                   (R1A)
L_domain            positive integers; on the ternary surface the
                    support and l1 gradings coincide

face_alphabet       {0, +1, -1}                                        (R0A)
Filling             Fill(j) = { n in C_2^c(Z^4; {0,+1,-1}) :
                                partial n = 5j }
charge_equation     partial n = 5j, coefficientwise equality over Z,
                    not merely mod 5.  "Charge 5" in the parent scope
                    is read exactly as this equation, consistent with
                    MONOPOLE-FIFTHS [T]
filling_existence   Fill(j) may be empty; no existence theorem is
                    assumed or needed
empty_filling_rule  F_occ(j) = +infinity when Fill(j) is empty; the
                    universal inequality b F_occ >= a L then holds
                    vacuously at j, so an unfillable current can
                    never serve as a counterexample (conservative)
face_support        supp(n)
F                   F(n) = |supp(n)|
F_occ               F_occ(j) = min { |supp(n)| : n in Fill(j) } when
                    Fill(j) != empty, else +infinity.  The
                    certificate route uses only the exact upper bound
                    F_occ(j) <= |supp(n)| for the exhibited n; no
                    minimum solver is used or claimed               (predef. 9)

kappa_domain        kappa = a/b with a, b coprime positive integers
coefficient_normalization
                    integer gate forms, frozen:
                    (K1)  b F_occ(j) >= a L(j) for every admitted j
                    (K2)  2^(4a) > 2401^b        (2401 = 7^4)
                    No decimal approximation of log2(7) is a
                    threshold certificate

universal_reduction not required for the negative route; the
                    completeness burden of the counterexample method
                    is carried entirely by the exclusion lemma of
                    section 3, which covers every admissible (a, b)
                    at once.  No positive universal proof or
                    reduction is claimed or attempted here
completeness_method for this probe: exact certificate verification
                    plus the exclusion lemma; both are total and
                    deterministic on the frozen inputs

counterexample_family
                    a finite nonempty set W of admitted pairs
                    (j_i, n_i), each satisfying
                        partial n_i = 5 j_i   and
                        2^(|supp n_i|) <= 7^(|supp j_i|)
                    as exact integers.  By section 3, W != empty
                    excludes every admissible kappa passing (K2).
                    The pinned W for this probe is the single
                    archived pair (L = 3240, F = 7993) of section 1;
                    the checkerboard/slab pump families are optional
                    future strengthenings, not needed
deterministic_order the witness serialization is canonical: j entries
                    sorted lexicographically by (vertex, direction),
                    n entries by (vertex, a, b); the checker
                    transcript is line-deterministic
certificate_schema  section 5
certificate_checker section 6
```

## 3. The exclusion lemma

**Lemma (integer-exact).** Let `(j, n)` be an admitted pair with
`partial n = 5j` and `2^F <= 7^L`, where `L = |supp j| >= 1` and
`F = |supp n|`. Then no coprime positive integers `(a, b)` satisfy
both (K1) and (K2).

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

Consequence: one admitted certificate pair excludes **every**
admissible `kappa` with `2^(4 kappa) > 2401` simultaneously. This is
exactly the predicate issue #200 requires the preregistration to fix
("including how it excludes every admissible kappa").

## 4. Outcome predicates and this probe's decision map

The four lane outcomes, frozen at least as strong as the issue #200
block (issue wording lightly normalized; the issue itself requires
predicates "at least as strong as" its text):

```text
KAPPA-PROVED       complete exact universal proof plus one exact
                   admissible kappa satisfying both frozen
                   inequalities for every admitted worldline
BELOW-THRESHOLD    an exact admitted counterexample family (section
                   2, counterexample_family) proves that no
                   admissible kappa above the threshold can satisfy
                   the universal bound
CANDIDATE-REFUTED  a proposed kappa, reduction, or proof fails, but
                   the exact evidence does not exclude every
                   admissible kappa; the split remains open
STOP               authority, collision, typing, pin,
                   proof-completeness, security, or transcript
                   requirements fail
```

Decision map of THIS probe, frozen before any run:

```text
checker PASS on the pinned witness  ->  BELOW-THRESHOLD
any checker failure                 ->  STOP
```

This probe cannot emit KAPPA-PROVED or CANDIDATE-REFUTED; those
remain reachable in the lane only through other, separately pinned
future probes. This asymmetry is deliberate and prevents outcome
shopping: absence or corruption of the certificate proves nothing
about the universal bound and must land on STOP, never on a
scientific negative or positive.

Reviewers should confirm this reading of predefinition section 11
item 7 ("all four outcomes remain reachable"): reachability is a
property of the lane, not of each single probe. If review rejects
that reading, the alternative is to add a CANDIDATE-REFUTED branch
for a syntactically valid witness that fails only the threshold
inequality; the STOP mapping above is the stricter default. Note
that under the C6 hash pinning the alternative branch is unreachable
dead code for this probe anyway: a file matching the pinned SHA-256
has F = 7993 and L = 3240, for which the threshold inequality holds
as a mathematical fact, and any other file fails C6 and lands on
STOP first.

## 5. Certificate schema

One JSON file, UTF-8, no floating point anywhere:

```text
{
  "P": int, "m": int, "C": int, "D": int,   construction metadata,
                                            not verified content
  "L": int, "F": int,                       declared counts
  "j": [ [[x0,x1,x2,x3], d, c], ... ],      edges: base vertex,
                                            direction 0..3,
                                            coefficient in {-1,+1}
  "n": [ [[x0,x1,x2,x3], a, b, c], ... ]    faces: base vertex,
                                            0 <= a < b <= 3,
                                            coefficient in {-1,+1}
}
```

The top-level key set is exactly `{P, m, C, D, L, F, j, n}` and the
checker must reject any other set; this matches the reviewed
reference checker on public `main` (`EXPECTED_KEYS`).

```text
```

Scope block (normative for admissibility):

```text
edge coefficients: {-1,0,+1}; zero entries must not be serialized
repeated edges:    forbidden (keys unique)
repeated vertices: allowed
vertex degree:     even, not necessarily 2
connectivity:      support graph of j connected
```

## 6. Certificate checker

`verify.py`, Python standard library only, run from the probe
directory; deterministic stdout; exit 0 and empty stderr on PASS.
Checks, each of which must attempt refutation and abort on failure:

```text
C1  schema: shapes, integer types, a < b, d in 0..3; no duplicate
    edge or face keys; no zero coefficients
C2  j ternary and nonzero; partial j = 0 at every vertex
C3  support graph of j connected; every vertex degree even; a
    Hierholzer closed traversal using every support edge exactly
    once with orientation matching the sign (the worldline
    realization certificate)
C4  n ternary
C5  partial n = 5j coefficientwise on every edge of Z^4: exactly the
    support edges receive +-5 with the correct sign, and no other
    edge receives a nonzero value
C6  L and F equal the declared counts and the pinned values
    L = 3240, F = 7993; the file's SHA-256 equals the pinned value
    of section 1
C7  2^F <= 7^L compared as exact big integers; additionally
    B = max{m : 2^m <= 7^L} is printed with F <= B
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
S1  regression: each of the nine KAPPA-SHAPES loops keeps
    2^LB > 7^L (greedy bound above threshold); the certificate
    machinery must not disturb the registered library
S2  out-of-carrier control: the predefinition section 7.2 torus
    family is rejected by the finite-support Z^4 carrier and by
    the connectivity requirement (it is not admissible input)
S3  mutation controls on the pinned witness, each must FAIL the
    checker: flip one face coefficient (C5 fails); delete one edge
    entry (C2 or C5 fails); duplicate one face entry (C1 fails);
    inject a coefficient 2 (C1 fails); disconnect the support by
    removing one bridge pair (C3 fails)
S4  determinism: two consecutive runs produce byte-identical stdout
S5  vocabulary control: the checker output must label the outcome
    BELOW-THRESHOLD, not CANDIDATE-REFUTED; see the erratum below
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
EQUATION:    (K1) b F_occ(j) >= a L(j) for every admitted j;
             (K2) 2^(4a) > 2401^b; the exclusion lemma of section 3
             with its integer-exact proof; L, F, Fill, F_occ as in
             section 2
CODE:        the accepted verify.py of section 6, reviewed and
             committed with this preregistration before any formal
             gate execution
CARRIER:     the complete S_kappa tuple of section 2 (by value, not
             by reference, in the final PREREG); the pinned witness
             JSON with its SHA-256 and byte count as frozen input
             data
SYSTEMATICS: S1-S5 of section 7
THRESHOLD:   the outcome predicates and decision map of section 4,
             frozen before output
LAYER:       L4 support only; no tick, stream, or measure quantity
             is consumed; no cross-layer lift; no named gate
```

## 9. What follows the pin (for orientation, not authorized here)

1. Review and merge this package; public readback.
2. Re-check authority, collisions, branch/issue/path locks
   (predefinition section 11 item 9) against then-current `main`.
3. Create `probe/P-PHOTON-KAPPA-LEMMA-1` and
   `probes/P-PHOTON-KAPPA-LEMMA-1/`; commit PREREG.md, the accepted
   verifier, and the witness JSON; push; confirm remote hashes,
   byte counts, and LF-normalized readback before any run.
4. Formal execution; EXPECTED.txt; RUN.md with neutral descriptors;
   RESULT.md with the decision-map outcome; one-probe pull request;
   the two GitHub architecture jobs supply the two-architecture
   record.
5. A later reviewed fold (v36 or later) would register whatever the
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
- introduces no new photon carrier, spatial lift, FCC lattice,
  displacement support, shell weights, polarization, holonomy, time
  bridge, measure, or SI statement;
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
