# P-SPLIT-PRIME-INDEPENDENCE-1 preregistration

Two L1 claims about the rapidity classes of split rational primes in
F = Q(sqrt5): that they are linearly independent over Z modulo the class of
the fundamental unit, and that the generator reduced into the fundamental
half-period has absolute logarithmic height exactly one half the logarithm
of the prime. Both are proved below in writing. The verifier is an AUDIT of
those proofs at finite scope and carries no universal quantifier.

## Authority record

```text
STATE:          ACTIVE
CANON:          Public Canon v44
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v44
CONTENT_COMMIT: 9da73b96613eb0d6f8d0ec17a5ada3ee6f511a4a
CANON_SHA256:   c482aff6d0a01faab7fa8b92d2c485b39a8389f67ed99d79024a2878f35acd69
CANON_BYTES:    211566
BASE_COMMIT:    1417b533944e85106901079cc73ae7a0c3c42dc2
```

Currency gate run on a fresh clone at preregistration time: STATE ACTIVE,
tag `canon-v44` and the declared content commit both ancestors of `main`,
`canon/CANON.md` equal to the declared hash and byte count, `canon/SHA256SUMS`
5 of 5 OK. This probe is L1 only and opens no inter-layer gate.

## Source, claim lock, and disclosure

```text
SOURCE:  incubation candidate C-PRIME-ORDER-READING-1, stage A, accepted
         in the incubation lane with verifier sha256
         307dd0c17f922b46566f12ebf6af93b120f151004534d527c7cecae765a28b4c
         and stdout sha256
         f7b40278da52c642dd1ed1e2f4d77d505d44d9fdfd106b03b1e27575accddac5,
         8 of 8 PASS, byte-identical on x86_64 and aarch64. A four-part
         breaker survived with broken=0 on both architectures (breaker
         sha256
         594fcf4ba7940908a156d774ed4488190c2cf9282671f756a38c93d67d54c2c5,
         stdout sha256
         f77ecc9c2908f043856da3118d6e48cd5d4ad804cf1c6b4709bff04e52609a52).
         The claims below strictly generalise that stage: PROP-1 of the
         candidate is the case k = 2 of claim A, and the fixed-point
         clause is the case k = 1.
READINGS: claim A has three independent readings by three separate
         authors. The first proposed the torsion case, the second proved
         the general linear case and supplied the corrected coefficient
         bookkeeping, the third supplied the public-native proof adopted
         verbatim below, which runs through SPLIT-PRIME-RAPIDITY-CLASS
         and needs no auxiliary lemma and no normalisation convention.
         Corrections accepted from those readings and applied here: the
         zero class is carried by the CLASS and not by every generator;
         the statement is carried on the unordered class; a finite
         computation witnesses principality of the tested ideals and not
         a global class number; the free-subgroup reading requires a
         choice of orientation before it is a group statement.
ISSUE:   NOT OPENED FROM THIS SESSION. This session has repository push
         access by key but no GitHub API credential, so it could not open
         the public claim issue that POLICY step 2 requires before
         computation. This pin, pushed before first execution, is the
         operative public claim and carries the disclosure; the owner is
         asked to open the claim issue and record its number here in the
         fold. No other probe, branch, registry row or open item names
         these claims: probes/, the public branch list and the registry
         were checked at gate time and are clean.
OWNER:   one session; no other session claims this probe.
ADJACENT: LOG-AXES-INDEPENDENCE [T] states that pi and log phi are
         linearly independent over the algebraic numbers by Baker. It is
         a statement about the two archimedean axes of the program and
         shares no content with claim A, which is about split-prime
         rapidity classes and uses unique factorisation of ideals and no
         transcendence input whatsoever. The two must not be conflated.
NON-USE: nothing in this probe uses, assumes or concludes anything about
         the Riemann hypothesis, zeta zeros, Weil positivity, explicit
         formulae, Hecke L-functions, effective bounds on linear forms in
         logarithms, the decoder, any measure, Born, observer, force,
         spacetime, physical vacuum, any other physical reading, SI, or
         any L2 to L6 statement.
```

## The claims, with their proofs

Notation is that of `SPLIT-PRIME-RAPIDITY-CLASS [T]` and
`ARITHMETIC-RAPIDITY-DECOMPOSITION [T]` in Public Canon v44, section 10:
F = Q(sqrt5), O = Z[phi], conj the nontrivial automorphism, N(x) = x conj(x)
the signed norm, rho(x) = x/conj(x) the multiplicative avatar,
eta = (1/2) log|sigma+(rho)| the additive rapidity, L = log phi, and for a
rational prime p split in F with a prime ideal above it generated as (pi),
the class r = [eta(pi)] in R/LZ, with the canonical unordered pair
R(p) = {r, -r}.

### CLAIM A, SPLIT-PRIME-RAPIDITY-INDEPENDENCE

Let p_1, ..., p_k be pairwise distinct rational primes, all split in F, let
P_i = (pi_i) be a prime ideal above p_i with either orientation, and let
r_i = [eta(pi_i)]. If m_1, ..., m_k are integers with

```text
m_1 r_1 + ... + m_k r_k = 0   in   R/LZ,
```

then m_i = 0 for every i.

PROOF. Put x = prod_i pi_i^(m_i) in F. Since rho is multiplicative and eta
is additive, [eta(x)] = sum_i m_i r_i = 0. By the registered equivalence of
SPLIT-PRIME-RAPIDITY-CLASS, [eta(x)] = [eta(1)] holds exactly when
rho(x)/rho(1) = +-phi^(2n) for some integer n, and rho(1) = 1, so

```text
rho(x) = +-phi^(2n).
```

Pass to fractional ideals. Since phi is a unit, the right-hand side
generates the unit ideal, and rho(x) = x/conj(x) gives

```text
prod_i P_i^(m_i) conj(P_i)^(-m_i) = (1).
```

The 2k prime ideals P_1, conj(P_1), ..., P_k, conj(P_k) are pairwise
distinct: P_i differs from conj(P_i) because p_i splits, and ideals above
distinct rational primes differ because their residue characteristics
differ. The group of fractional ideals is free abelian on the prime ideals,
so every exponent vanishes and m_i = 0 for all i. QED

Equivalent real form: lifting r_i to any real representative t_i, the reals
t_1, ..., t_k, L are linearly independent over Q. A rational relation clears
denominators to an integral one and reduces modulo L to the statement just
proved.

Orientation independence: replacing P_i by conj(P_i) replaces t_i by -t_i,
and linear independence is invariant under sign changes of the variables,
so the claim needs no canonical orientation.

COROLLARIES carried inside the scope of the row and not as separate rows:

```text
A1  k = 1 gives that no class of a split prime is torsion: m r = 0 forces
    m = 0, so the split stream avoids the entire torsion subgroup of the
    circle, and in particular both fixed points of the involution.
A2  k = 2 with coefficients (m, -m) and (m, m) gives that for every m >= 1
    the map p -> m R(p) is injective on split rational primes and never
    equals the zero class.
A3  With alpha_i = t_i / L, claim A says that for every nonzero integer
    vector h the number sum_i h_i alpha_i is not an integer, hence Weyl's
    criterion gives that the integer-multiple orbit
    m -> (m alpha_1, ..., m alpha_k) mod 1 is equidistributed in the
    k-torus. This is equidistribution of the multiples of a fixed finite
    set of classes. It is NOT a statement about the distribution of primes
    as p grows, and it must not be quoted as one.
A4  After a choice of one orientation above each split rational prime, the
    classes generate a free abelian subgroup of R/LZ of infinite rank, the
    rank being infinite because infinitely many rational primes split.
    Changing an orientation replaces a generator by its negative and does
    not change the subgroup. The unordered pair R(p) itself lives modulo
    sign and is not a group element, so the choice of orientation is part
    of the statement.
```

### CLAIM B, REDUCED-SPLIT-GENERATOR-HEIGHT

Let p be split in F and P = (pi) a prime ideal above it. Among the
generators of P there is exactly one, up to sign and conjugation, whose
rapidity lies in the open fundamental half-period,

```text
eta(pi) in (-L/2, L/2),
```

the endpoints being unattainable. For that reduced generator both real
embeddings exceed one in absolute value, and consequently the absolute
logarithmic height is exactly

```text
h(pi) = (1/2) log p,
```

hence h(pi/conj(pi)) <= log p.

PROOF. Generators of P are exactly +-phi^n pi, and eta(+-phi^n pi) =
eta(pi) + nL, so exactly one integer n places the rapidity in the
half-open interval [-L/2, L/2). The endpoint eta = +-L/2 would give
2 eta(pi) = +-L, that is 2 r = 0 in R/LZ, which is the case k = 1, m = 2
of claim A and is therefore impossible; so the interval may be taken open
and the reduced generator is unique up to sign and conjugation, conjugation
negating eta.

For the reduced generator write s+ = |sigma+(pi)| and s- = |sigma-(pi)|.
Then s+ s- = |N(pi)| = p and eta = (1/2) log(s+/s-), so

```text
s+ = sqrt(p) e^(eta),   s- = sqrt(p) e^(-eta),   |eta| < L/2,
```

hence min(s+, s-) > sqrt(p) phi^(-1/2). The smallest rational prime split
in F is 11, and sqrt(11) phi^(-1/2) > 1, so both embeddings exceed one.

pi is an algebraic integer of degree two over Q, because P differs from
conj(P) and therefore pi is not rational, and its minimal polynomial is
monic. The absolute logarithmic height of an algebraic number of degree d
with monic minimal polynomial is the average of log max(1, |.|) over the
conjugates, so with both conjugates exceeding one,

```text
h(pi) = (1/2)(log s+ + log s-) = (1/2) log(s+ s-) = (1/2) log p.
```

Finally h(pi/conj(pi)) <= h(pi) + h(conj(pi)) = log p, the height being
invariant under conjugation. QED

Content note, so that the row is not read as more than it is: the whole
arithmetic content is that BOTH embeddings of the reduced generator exceed
one, which is an exact comparison in Z[phi]. The height value then follows
from the definition of the height and the norm identity. Without the
reduction the height is unbounded at fixed rapidity class, since
pi -> phi^a pi multiplies the avatar by (-1)^a phi^(2a) while leaving the
class unchanged.

## Field 1. EQUATION (the gated clauses; each check name states exactly its test)

All arithmetic is exact in Z[phi], elements represented as integer pairs
(a, b) meaning a + b phi with phi^2 = phi + 1. No logarithm and no float is
computed anywhere. The class decision is the registered log-free one.

```text
G1.split_census_matches_residue_rule
    the frozen prime list is exactly the rational primes below the frozen
    bound whose residue mod 5 lies in {1, 4}
G1.generators_have_absolute_norm_p
    every constructed generator w satisfies |N(w)| = p exactly
G1.tested_ideals_are_principal_by_exhibited_generator
    principality of each TESTED ideal is witnessed by the exhibited
    generator; no global class number is asserted by this computation
G2.class_zero_decision_two_independent_paths_agree
    for every decided instance, path A (exact divisibility in Z[phi]
    followed by the registered even-index Lucas trace test and an exact
    comparison) and path B (exponent enumeration with a certified
    magnitude crossing) return the same verdict; the frozen cross-check
    stride is every 7th instance plus every instance path A decides TRUE
G2.lucas_trace_test_matches_direct_power_comparison
    for norm-one integral w, the registered criterion |Tr(w)| = L_(2m)
    followed by exact comparison agrees with direct comparison against
    +-phi^(2m) on the frozen lattice of exponents
G3.no_integer_relation_in_the_frozen_boxes
    over the frozen families and coefficient boxes, no nonzero integer
    coefficient vector satisfies sum m_i r_i = 0; the count of relations
    found is exactly zero
G4.positive_controls_all_fire
    every frozen instance that MUST satisfy the class-zero condition does
    so under both paths: an inert rational prime, the ramified generator
    sqrt5, a split generator multiplied by its own conjugate, and a pure
    unit power. A verifier whose detector cannot fire is not acceptable
    and this gate exists to prove it can
G5.reduced_representative_exists_and_is_unique
    for every frozen split prime exactly one exponent in the frozen
    window places the rapidity in the open fundamental half-period
G5.half_period_endpoint_never_attained
    no frozen split prime attains the endpoint of the half-period
G5.reduced_generator_has_both_embeddings_above_one
    for every reduced generator both exact comparisons sigma+(pi)^2 > 1
    and sigma-(pi)^2 > 1 hold in Z[phi]
G5.height_identity_product_of_embeddings_equals_p
    for every reduced generator the exact identity |N(pi)| = p holds,
    which together with the preceding clause is the whole content of
    h(pi) = (1/2) log p
G5.unreduced_generator_fails_the_embedding_test
    for every frozen split prime and a frozen nonzero shift, the shifted
    generator fails the both-embeddings clause; the reduction is therefore
    doing work and the clause is not vacuous
G6.verdicts_are_invariant_under_the_declared_gauge
    over the frozen gauge sample, replacing generators by -w, by phi^j w
    for the frozen exponents, and by conj(w) with the matching coefficient
    sign change leaves every claim A verdict unchanged
```

Frozen scope. Split primes below 120, which is the list
11, 19, 29, 31, 41, 59, 61, 71, 79, 89, 101, 109. Families and boxes:
k = 1 over all twelve with coefficients in [-8, 8]; k = 2 over all sixty-six
unordered pairs with coefficients in [-4, 4]; k = 3 over all two hundred and
twenty unordered triples with coefficients in [-2, 2]; k = 4 over the
seventy unordered quadruples drawn from the first eight primes with
coefficients in [-1, 1]. The zero vector is excluded in each box. The gauge
sample is the first two hundred pair instances with exponents j in
{-2, -1, 1, 3}.

## Field 2. CODE

`probes/P-SPLIT-PRIME-INDEPENDENCE-1/verify.py`. Python standard library
only. Exact integers only; no `float`, no `Fraction` with inexact input, no
logarithm, no numerical eigenvalue, nothing inexact in any assertion or any
printed field. Runtime under 120 seconds. Run from the repository root as

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-SPLIT-PRIME-INDEPENDENCE-1/verify.py
```

Two structurally independent decision paths are required and are described
in G2. Generators are constructed by a bounded Diophantine sweep on
|a^2 + a b - b^2| = p. The verifier asserts the Field 1 clauses and nothing
else, and prints a check inventory so that the count of executed assertions
can be compared with the count of declared clauses.

## Field 3. CARRIER AND DATA

No external data. The split primes come from the residue rule alone and the
generators from exact integer search. Everything else is internal exact
arithmetic in Z[phi].

## Field 4. SYSTEMATICS

The generator ambiguity is the object of the claims, and it is removed by
the registered class equivalence rather than by a convention, so no
canonical section of the circle is used or needed anywhere. Vacuous PASS is
guarded by G4 for claim A and by the non-vacuity clause of G5 for claim B.
Single-path logic error is guarded by the two independent decision paths of
G2. Overflow cannot occur, Python integers being unbounded. Gate names are
required to state exactly what they assert, which is the lesson of the
integrity STOP that killed the first identity of the predecessor lane.
The finite scope is an audit: neither claim is established by this
computation, both are established by the written proofs above, and the row
must be read that way.

## Field 5. FAILURE THRESHOLD

Any nonzero integer coefficient vector inside the frozen boxes satisfying
the class-zero condition under both paths falsifies claim A, which then
becomes F, archived, with no threshold moved. Any reduced generator failing
either embedding comparison, or any split prime attaining the half-period
endpoint, falsifies claim B in the same way. A disagreement between the two
decision paths, a positive control that does not fire, a non-vacuity clause
that passes for the unreduced generator, or a check count differing from
the declared clause count is an integrity STOP and not a scientific
falsifier. A pinned-bundle, transcript, or architecture mismatch without an
exact mathematical negation is likewise an integrity STOP.

## Field 6. ACTION LAYER AND NON-CLAIMS

Layer L1, state arithmetic. No lift to L2 through L6 is claimed and no
inter-layer gate is opened. The falsifiers of Field 5 are the operative
ones. Explicitly not claimed anywhere in this probe: any statement about
the ordering of the primes, about any map from a machine to the primes,
about effective or quantitative separation, about heights of unreduced
generators, about the Riemann hypothesis or any L-function, and any
physical reading of any kind.
