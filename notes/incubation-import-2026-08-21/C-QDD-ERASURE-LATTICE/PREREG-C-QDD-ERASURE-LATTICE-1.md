# PREREG. C-QDD-ERASURE-LATTICE-1

Date: 2026-08-21

Status: CANDIDATE, NO AUTHORITY. Incubation-lane preregistration inside the
TWIST-J claude.ai project. This is not a public probe, edits no repository
file, and promotes nothing. One named candidate session. Target line on
promotion: Public Canon (mathorn1973/twist-j), row QDD-INSTRUMENT-APPARATUS
[O], blocker O2 only, at L4.

## Authority basis

```text
STATE:          ACTIVE
CANON:          Public Canon v58
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v58
CONTENT_COMMIT: 05a0749e95c1a3603a4ee8e3016d92b066d8c5e9
CANON_SHA256:   647822f56c807b6a49b069010b6ce968998f5543f568f230f6cdf2588be6acc1
CANON_BYTES:    304010
MAIN_AT_WRITE:  317d731 (merge of PR 486)
gate at start:  SHA256SUMS 5 of 5 OK; tag and content commit ancestors of main
```

## Result exposure and lineage

Result-exposed, proof-first work. Non-canonical reasoning in this session
identified the expected ladder before this freeze; those calculations are
discovery context only. Boundary lineage, none of it imported or executed:
the merged public probes P-QDD-J-CENTRALIZER-TERMINALITY-1 (rational-circle
nonselection of the H_k class and the terminality bifurcation),
P-QDD-RECORD-COMPLETE-STABILIZER-1 (S_4 completeness selection and the
affine boundary), P-QDD-RECORD-NATURALITY-FORK-1 (normalizer fork),
P-QDD-FRESH-RECORD-NOFEEDBACK-2 (record-sufficiency equivalence),
P-QDD-J-AFFINE-APPARATUS-1 (AGL_1(F_5) coupling nonuniqueness). This
candidate reconstructs every object from the axiom step map by fresh code.

Static parsing and syntax compilation of the verifier are allowed before the
freeze. No scientific execution before the freeze. No external data.

## Question

The sealed record lane leaves O2 in this state: the architecture-residual
symmetry premise (affine multipliers, C_4) leaves a continuum of physical
post-state classes; the full record-partition completeness premise (S_4)
selects the Lueders class uniquely; weaker record premises (fresh pointer,
append-only record, no feedback, reversibility) select nothing. The open
question frozen here: WHAT SITS BETWEEN, and what sits BELOW. Exactly which
symmetry premises between the architecture residual and full erasure exist
at all, what each one selects, and whether any reading can be equivariant
under the phase motor itself.

## Field 1: equation

All objects over Q, exact.

```text
V = Q^4,  one = (1,1,1,1)^T,  G = I_4 - (1/5) one one^T,
M_J = [[1,0,-1,1],[0,1,-1,0],[1,0,0,0],[0,1,-1,1]],
D = M_J - I_4                  (the phase motor),
u_x = D^x e_0, x in F_5        (the public J simplex),
X^sharp = G^-1 X^T G           (the G adjoint).
```

For every pi in S_5 the unique linear map rho(pi) u_x = u_(pi(x)) is
G-orthogonal and the representation is faithful. Fix the terminal record
token k = 2 (the sealed target token). Write

```text
S_k = {pi in S_5 : pi(k) = k}            ~= S_4   (record stabilizer),
H_k = {x -> k + a(x - k) : a in F_5^x}   ~= C_4   (architecture residual,
                                                   exactly AGL_1(F_5) cap S_k),
g   = rho of the multiplier a = 2,
P_k = (1/24) sum over S_k of rho,  Q_k = I - P_k,
R_k = (1/4)(I - g + g^2 - g^3),  C_k = Q_k - R_k,  J_k = g C_k.
```

An admitted law at token k is a rational T with

```text
T P_k = P_k T = 0,   T^sharp T = Q_k,
```

taken modulo the registered post-state equivalence T ~ -T. A symmetry
premise is a subgroup Gamma with H_k subset-of-or-equal Gamma
subset-of-or-equal S_k, and the Gamma class is the set of admitted laws
commuting with rho(Gamma). Below the stabilizer, the motor class is the set
of admitted laws commuting with D itself; note D = rho((01234)), so any
subgroup of S_5 containing the motor cycle has its commutant inside the
motor commutant.

Expected statements, each to be earned or fired by the run:

```text
E1 LATTICE. The complete list of subgroups Gamma with
   H_k <= Gamma <= S_k is exactly {H_k, D_k, S_k}, where D_k is the unique
   dihedral group of order 8 containing H_k. Proof shape: for every sigma
   in S_k minus H_k the closure <H_k, sigma> is D_k or S_k (20 exhaustive
   closures); for every sigma in S_k minus D_k the closure <D_k, sigma> is
   S_k (16 exhaustive closures).

E2 CENTRALIZER DIMENSIONS on the moving space Q_k V:
   dim End_{H_k} = 3 with basis {R_k, C_k, J_k},
   dim End_{D_k} = 2 with basis {R_k, C_k},
   dim End_{S_k} = 1 with basis {Q_k}.

E3 CLASS COUNT PER RUNG, target-independent, effects compared last:
   H_k rung: T = e R + r C + s J with e^2 = 1, r^2 + s^2 = 1, an injective
     rational family of physical classes (the sealed rational circle,
     re-derived independently); NONSELECTION with infinitely many classes.
   D_k rung: exactly four algebraic members {+-Q_k, +-(R_k - C_k)}, exactly
     two physical classes, the Lueders class [Q_k] and the nonterminal
     involution class [R_k - C_k]; the terminality bifurcation lives
     exactly on this rung.
   S_k rung: exactly one physical class [Q_k]; strict representative
     idempotence selects +Q_k.

E4 MOTOR EMPTINESS. The commutant of D in End(V) is the 4-dimensional
   algebra spanned by {I, D, D^2, D^3}; its intersection with
   {A : A P_k = 0} is {0}; hence the motor class is EMPTY, and by commutant
   containment the class is EMPTY for every subgroup of S_5 containing the
   motor cycle (machine witnesses: the cycle group, AGL_1(F_5), A_5, S_5).

E5 TRANSPORT. Conjugation by D carries the complete ladder of token k to
   token k+1: stabilizer, residual, dihedral rung, projectors, and all
   three centralizer dimensions, at all five tokens.
```

Reading, candidate-D, recorded only if E1 to E5 hold: within this frozen
class the reading interface has exactly one minimal selecting premise, full
record-partition erasure S_k; retaining even the single dihedral label
(D_k) retains exactly the known nonterminal class; the architecture residual
alone leaves a continuum; and no reading at all is equivariant under the
motor, so the selecting symmetry cannot come from the flow. The same motor
that admits no reading transports the reading ladder between tokens.

## Field 2: code

Accepted exact files, frozen together with this preregistration:

```text
verify_qdd_erasure_lattice_1.py    the verifier
breaker_qdd_erasure_lattice_1.py   the independent breaker
```

Requirements for both: Python standard library only; integers and Fraction
only; no float, complex, random, network, subprocess, or file write; zero
arguments; deterministic stdout; empty stderr; run from the working
directory with LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
TZ=UTC; under 120 seconds each. Fixed gate order, no fail-fast.

The breaker is an attack by independent method, not a replay: subgroup
census by breadth-first closure of the full subgroup lattice of S_k from
the trivial group (finds every subgroup, not only 2-generated ones);
centralizer dimensions by the rank of the exact group-averaging projector
on End(V) (16-dimensional Gaussian elimination), cross-checked against the
verifier's linear-system route; direct search for a nonzero motor-commutant
law; direct search for a D_k-covariant law with s != 0; full recompute at a
second token.

## Field 3: carrier

```text
system:          (Q^4, G), the public J simplex, tokens F_5
symmetry:        S_5 simplex group; motor D = rho((01234));
                 residual H_k = C_4; stabilizer S_k = S_4
record:          binary partition {k} | other, token k = 2 primary,
                 all five tokens for transport
post quotient:   T ~ -T (the registered sign equality, unchanged)
data:            none; no external input; no predecessor import
```

## Field 4: systematics and completeness

No tolerance anywhere; every assertion exact. Named obligations:

```text
C1  frozen literals: M_J, G, token, group definitions match this file;
C2  motor and simplex identities: D^5 = I, Phi_5(D) = 0, sum u_x = 0,
    Gram table, u_2 = -one, {I,D,D^2,D^3} independent;
C3  complete faithful G-orthogonal 120-member representation with the
    full 120 x 120 homomorphism table and the 600 vertex-action checks;
C4  P_k, Q_k projector identities, ranks 1 and 3;
C5  H_k is C_4 and equals AGL_1(F_5) cap S_k, membership exhaustive;
C6  E1 by the 20 + 16 exhaustive closures; D_k dihedral certificate
    (order 8, relation r g r^-1 = g^-1, four involutions outside H_k);
C7  E2 by exact nullspace computation over the full member lists;
C8  sharp calculus: R, C self-sharp, J^sharp = -J, and the six product
    identities reducing T^sharp T on each rung;
C9  E3: derived coefficient equations, member enumeration at D_k and S_k,
    the rational-circle witnesses at H_k (at least five pairwise distinct
    physical classes, injectivity identity s/(1+r) = t on the samples),
    nonterminality witness for R_k - C_k (first and second conditioned
    rays differ on an explicit rational state);
C10 E4 by exact solves, including the three larger transitive witnesses;
C11 E5 at all five tokens;
C12 target comparison LAST: P_2 = E_low = (1/4) one one^T,
    Q_2 = E_high = I - E_low, only after C1 to C11;
C13 firewalls printed: candidate labels only; O1 and O2 remain open;
    L4 only, no L5/L6 lift; SAMPLING NOT PROVIDED untouched; apparatus
    records not identified with public D_clock records; the lattice
    quantifies only over Gamma containing H_k, and premises discarding
    the architecture residual (for example the even subgroup A_4) are
    out of scope; naturality-versus-normalizer is a separate sealed axis.
```

## Field 5: failure threshold and decision

```text
ERASURE-LADDER   C1 to C13 all pass and E1 to E5 all hold.
LATTICE-F        E1 fails: an intermediate subgroup outside {H_k,D_k,S_k}.
CENTRALIZER-F    E2 fails: any dimension or basis differs.
CLASS-F          E3 fails: any rung class count or member list differs.
MOTOR-F          E4 fails: a nonzero motor-equivariant admitted law exists.
TRANSPORT-F      E5 fails at any token.
STOP             an integrity obligation fails, a float appears, a
                 threshold moves, or the breaker and verifier disagree
                 without an exact diagnosis. No scientific conclusion.
```

Any single fired falsifier is a first-class outcome and will be archived,
not deleted; no threshold moves after this freeze. The breaker finding a
counterexample fires the corresponding F label even if the verifier passes.

Maximum later public rows on ERASURE-LADDER, all restricted L4 statements:

```text
QDD-RECORD-SYMMETRY-LATTICE      [T]  (E1, E2)
QDD-ERASURE-RUNG-CLASSES         [T]  (E3)
QDD-MOTOR-EQUIVARIANCE-EMPTY     [T]  (E4, E5)
```

None closes O2. The added premise ranking (which rung physics actually
supplies) remains the open blocker; this candidate only proves the ladder
has no other rungs.

## Field 6: action layer

L4 apparatus/support only. No L5/L6 lift, no measure, no sampling, no
event stream, no Born claim beyond the registered target comparison. O1
untouched. SAMPLING NOT PROVIDED.

## Freeze order

1. Freeze this file and both programs together; record SHA-256 of all
   three in the freeze block below before any execution.
2. Execute the verifier exactly once; record stdout and its SHA-256.
3. Execute the breaker exactly once; record stdout and its SHA-256.
4. Write RESULT and, if earned, the PROMO package. Archive everything in
   the project claude/ lane regardless of outcome.
