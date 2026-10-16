# Exact finite census of the conditional native-classical two-cut contact

PUBLIC NON-CANONICAL. Conditional L1 finite audit of a published proof.
Formal preregistration; frozen by the first publicly pushed source pin.
The public claim precedes this commit and every formal execution.

```text
probe_id: P-NATIVE-CLASSICAL-CONTACT-CENSUS-1
branch: probe/P-NATIVE-CLASSICAL-CONTACT-CENSUS-1
public_issue: https://github.com/mathorn1973/twist-j/issues/1491
authority_base: 5f54015ed8361e3a64cb10894397020ddfadd104 (Public Canon v101 ACTIVE)
audited_sources: notes/C-NATIVE-CLASSICAL-TWO-CUT-CONTACT-N at
                 ea924e214ec3c29009fd4590f294954d3e5ad43f (contract pin
                 7b3fa47c0223bd99fce977de6ea58d484e257033), building on the
                 classical contract 4302c31f07823b2a843e3702ca14620c1917b853
                 and O/R results at 1b69563af4018b08d7dc75781b12e9553a8c19c3,
                 all on public branches
owner: A. M. Thorn
```

## Frozen six fields

```text
equation:         the five canonical generators g0..g4 on F5^6; selector
                  j = sum(x) + 2*theta_n mod 5, theta_n = popcount(n) mod 2;
                  eta(q,r) = (ell(q)/2, (ell(r)+1)/2, 0, 0),
                  ell = (0,1,2,-2,-1); contact C and its inverse as in the
                  audited PROOF sections 2-3; classical stencil B, Dirichlet
                  L_D, Couple, tape transition F and inverses as in the
                  frozen classical CONTRACT sections 1-4 and lane R
                  equations (4),(5),(9),(10); energies E_D, E_full, q_g.
code:             verify.py, Python standard library only (fractions,
                  itertools). Exact rational arithmetic; no floats anywhere.
carrier or data:  all 625 preparations p in F5^4 with common receiver (0,1);
                  all 15625 native checkpoints for generator identities;
                  the five induced encodings; basis sources e_j in Q^4;
                  one frozen occupied test family (section 4); five frozen
                  negative controls (section 5). No external data.
systematics:      native tables, induced-encoding agreement and complete
                  endpoint recovery are evaluated for all 625 inputs.
                  Classical trajectories factor through the encoding z and
                  the common blank state by construction of the schedule,
                  so each distinct trajectory is computed once and its
                  classical assertions are checked once per encoding; the
                  per-preparation endpoint is then assembled and inverted
                  for every input. Sparse exact-rational wave vectors on
                  the finite set D; zero extension outside D.
                  Lexicographic stencil-offset enumeration; exact sparse arithmetic.
failure threshold: exact equality, tolerance zero, for every assertion in
                  section 3. One failed assertion fails the run (nonzero
                  exit, no PASS token). No threshold may move after the pin.
action layer:     L1 (state). No layer lift is asserted or implied.
```

## 1. Frozen question

Do the finite, fully explicit claims of the conditional contact package —
native branch schedule, induced five-class encoding and its work values,
contact and coupler/tape inverses, both signed cut outputs, energy
identities, and the prepared-image inverse with its recognition recipe —
hold exactly as published, when every quantity is recomputed from the
frozen definitions rather than inherited response matrices?

This probe audits a result-exposed conditional construction. It does not
test the admission of the transducer, any physical realization, any
Canon owner, or any statement beyond the finite content below. Universal
statements over the rational carrier remain with the written proof; the
verifier checks them on the frozen finite families named here.
Prior exposure before this formal pin: two non-formal development replays
on Windows x86_64 / CPython 3.12.10 returned the proposed PASS counter line
with exit 0 and empty stderr. The first preparation verifier was SHA-256
`4a67b07ca36c71808412b66a61c9a17085878d5bbf81e4a2a0a307c73e85c2be`
(18586 bytes); the repaired preparation verifier was
`796dd1171e45dc5558d6a022da1e8c14983804220f28a3bfb23af0ef7d8cc15c`
(19961 bytes). Their preregistration drafts respectively had SHA-256
`c01e9f53e5b15947bd57b023db2be7c307e2ee75037d031d670d211fc3cbdf37`
and `ffb19feec4d0eb96bd99ac9bf96d83abb8fdf803a0c89c61fc4d5d3c34112d4c`.
The author also tested that removing the piston-sum guard admits the
fabricated X1 endpoint and that the guarded recipe rejects it. These are
disclosed implementation development and prior knowledge, not formal
evidence, an independent architecture or blind prediction. Formal source
labeling and LF normalization receive their own hashes in RUN.md.

## 2. Inputs frozen by value

Native generators, the branch/receiver/piston tables by `h`, the five
encodings with work values `0, 1/10, 3/20, 2/5, 2/5`, and the integer
output tables `12960*b0` and `1399680*b1` are taken from the audited
PROOF and embedded in `verify.py` as comparison targets only. The
stencil shells `|d|^2 in {2,4,8,10,16}` with weights `(6,1,15,1,1)/324`,
marked sites `y0..y4`, port order `R=(y0,y1,y2,y3)`, conductances
`g_j=2`, and `D = Y+B_zero+B_zero` are taken from the frozen classical
contract. The verifier never reads the audited branch at run time.

## 3. Assertions (all exact; counters printed)

```text
N1  each g_j is an involution on all 15625 checkpoints, and its total-sum
    map is (z,-z,2-z,2-z,3-z) respectively, for every checkpoint.
N2  theta_0,theta_1,theta_2 = 0,1,1 by popcount parity.
N3  for all 625 p: selector word, receivers C1,C2,C3, final piston formula
    and final total sum 1 match the published table for h(p); each h-fibre
    has exactly 125 elements; x1,x2,x3 equal the composed generators.
E1  for all 625 p: eta(C1(p)) equals the published encoding for h(p),
    hence encodings coincide iff h coincides. Once per encoding: it lies
    in Z_op (max coordinate <= 1), and the wave energy E_D(0,S z),
    computed from the Dirichlet definition, equals
    (sum z_i^2 - (sum z_i)^2/5)/2 and the published work value.
C1  contact C from the blank state yields X0 and w as published; C
    followed by its published inverse, and the inverse followed by C, are
    the identity on every prepared contact state and on the occupied
    test family of section 4.
W1  stencil shell multiplicities are (12,6,12,24,6); every L_D diagonal
    entry is 8/9; marked sites are distinct members of D with P^T P = I;
    supports obey supp(Sz) subset Y, supp(v1) subset Y+B_zero,
    supp(v2) subset D.
W2  Couple roundtrips (4)/(5) and the per-cut energy identity
    E_D(v,w)+q_g(b) = E_D(u,v)+q_g(a) on both cuts of (a) every occupied
    test-family case and (b) each of the five prepared encoding
    trajectories, whose couple outputs are also checked against the
    trajectory waves and signed cuts.
W3  F roundtrips (9)/(10) in both compositions, E_full at every boundary
    state, two-step formula (13) and complete prepared states (16)
    including tape slots and pointer, on (a) the occupied family and
    (b) each of the five prepared encoding trajectories. For all 625
    preparations the assembled endpoint is additionally inverted by the
    R1 recipe, which applies F^-1 twice.
W4  for the five encodings: 12960*b0 and 1399680*b1 equal the published
    integer tables; the five b0 are pairwise distinct; response maps
    derived from basis runs satisfy b0 = -M z/4, b1 = R1 z on basis and
    encodings; det(M) != 0; the decoder z = -4 M^-1 b0 (exact solve)
    recovers every encoding; two-cut balance
    E_D(v1,v2)+q_g(b0)+q_g(b1) = E_D(0,Sz) holds.
R1  for all 625 p: the published prepared-image inverse and recognition
    recipe (endpoint n=3, stage 4, fixed program; decoded h selects the
    branch word; recovered x0 has receiver (0,1) and piston sum h; after
    F^-1 twice and C^-1 the origin is X_blank with w=0) accepts the true
    endpoint and recovers the exact initial state.
R2  each frozen negative control of section 5 is rejected by the recipe.
S1  exactly one stdout line is printed: the PASS token with all counters.
```

## 4. Frozen occupied test family

For inverse and energy assertions beyond prepared runs: sources
`z in {0, +-e_j}` (9 values); occupied outgoing tapes
`(c0,c1) in {(0,0), (e0,0), (0,-e3), (e1+e2, e0-e3)}`; contact test waves
are the prepared waves `(0,Sz)`, `(Sz,v1)`, `(v1,v2)` for the five
encodings. This finite family never substitutes for the proof's
universal statements.

## 5. Frozen negative controls (each must be rejected)

```text
X1  fabricated native endpoint isolating the piston-sum guard corrected
    during the package's own review: x0=(0,0,0,1,0,1) (piston sum 1)
    driven by the fixed h=2 word (g3,g1,g3) instead of its selector word,
    giving (0,4,0,0,2,1), paired with the true h=2 classical endpoint and
    ledger. Decoding and readiness pass; only the piston-sum guard
    rejects. Deliberately not a true native trajectory endpoint.
X2  true h=3 endpoint with outgoing tape slots swapped to (b0,b1).
X3  true h=4 endpoint with b0 first coordinate increased by 1/12960.
X4  true h=2 endpoint with native counter replaced by 2.
X5  true h=1 endpoint with work ledger w replaced by 0.
```

## 6. Decisions and disposition

`PASS` requires exit 0, empty stderr, and the single stdout line
`NATIVE_CLASSICAL_CONTACT_CENSUS_PASS` with counters
`preparations=625 checkpoints=15625 encodings=5 occupied=51 rejected=5`
(occupied = 36 source/tape cases plus 15 contact states, section 4). Any assertion failure exits nonzero with no PASS token. Preserve the
first outcome and its exact finding; never move a target or tolerance.
A run that does not complete and supplies no completed EXPECTED.txt/RUN.md
record is closed ABANDONED under POLICY.md, with the identifier consumed
and no scientific conclusion inferred merely from technical failure.
Any separately established exact counterexample is preserved and assessed
at its actual scope; a fired scientific falsifier is not hidden by an
abandonment label. A completed successful audit receives its exact stdout,
run record and scoped result.
Passing earns at most computation-grade audit support for the finite
statements at this scope; the conditional theorem remains candidate-T on
its proof, the transducer remains an unadmitted premise, physical status
remains NOT_READY, and QUADRATIC-MEMORY-NATIVE-CONTACT [O] and
QDD-INSTRUMENT-APPARATUS [O] are untouched. No Canon, registry, gate, or
workflow change is performed by this probe. The sealed identifier is
never reused or resumed.
