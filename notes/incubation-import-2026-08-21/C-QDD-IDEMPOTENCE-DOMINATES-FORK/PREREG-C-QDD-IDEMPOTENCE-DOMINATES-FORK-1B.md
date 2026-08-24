# PREREG-C-QDD-IDEMPOTENCE-DOMINATES-FORK-1B (correction and strengthening)

```text
CANDIDATE: C-QDD-IDEMPOTENCE-DOMINATES-FORK-1B
SUPERSEDES: nothing. C-QDD-IDEMPOTENCE-DOMINATES-FORK-1 stands as run, with
           CF4 FIRED. Its prereg (sha256 8bec4313..), its verifier
           (ARCHIVE_verify_qdd_idem_dominates_1_FIRED.py) and its stdout are
           archived unchanged. No threshold moved. This is a new
           preregistration, frozen before the new run.
KIND:      incubation-lane candidate. NON-CANONICAL. No authority, no repo
           edit, no registry motion, no canon change, no fold.
TARGET:    public line, mathorn1973/twist-j.
BASIS:     Public Canon v57 ACTIVE, gate passed this session, clone HEAD
           d44645a2, canon/SHA256SUMS 5 of 5 OK.
LAYER:     L4 apparatus and support only. No lift. O1 untouched.
DATE:      2026-08-20
```

## What fired in run 1, exactly

```text
CF4 FIRED at gate CA6-02. The gate compared PARAMETER TUPLES (h, e, r, s) of
the enlarged family rho(h) X and required the survivor set to be exactly
{(identity, +1, 1, 0), (identity, -1, -1, 0)}. It is not. At every token six
parameter tuples survive, not two, because the map (h, X) -> rho(h) X is not
injective: 432 tuples give 240 distinct matrices. The four affine stabilizer
elements are themselves units of the C_4 centralizer algebra
Q direct-sum Q(i), so rho(g^m) X is again a centralizer element and the same
matrix is reached from several tuples.

Diagnosed, not repaired: the surviving MATRIX set at every token is exactly
{+Q_k, -Q_k}, and every surviving tuple has h affine. The defect was in the
preregistered wording of the gate, not in the physics. The physics claim is
restated below as a statement about operators, which is the physically
meaningful object, and is then strengthened past the frozen family.
```

## Falsifiers first. Each is a first class outcome if it fires.

```text
DF1  GENERAL dead: some operator T on the carrier with T^sharp T = Q_k and
     Q_k T = T, other than +Q_k and -Q_k, satisfies T^2 = +T or T^2 = -T
     exactly, at any token, anywhere in the swept family.
DF2  STRUCTURE dead: some T with T^sharp T = Q_k and Q_k T = T is not of the
     form O Q_k with O the restriction of T to W_k and O rational
     G-orthogonal on W_k; or some swept O fails O^sharp O = Q_k.
DF3  ENLARGED dead: in the enlarged fork family {rho(h) X} the set of
     surviving MATRICES is not exactly {+Q_k, -Q_k} at some token.
DF4  CEILING dead: as CF2 and CF3 of run 1 (already passed there; re-run
     here as regression, and a disagreement between the two runs is itself a
     fired falsifier).
DF5  SAMPLE dead: the Cayley sweep produces an operator that is not rational,
     not G-orthogonal on W_k, or fails the effect equation, so the sweep does
     not certify what it claims to sweep.
DF6  INTEGRITY: any float in any assertion, nondeterministic output, any
     dependency outside the Python standard library, any runtime above 120
     seconds per program, or any comparison against the target effects before
     the last gate.
```

## Field 1. Equation (claims and grades)

The lemma, derived by hand before this freeze and to be certified by exact
witnesses, not re-proved by the machine:

```text
LEMMA. Let Q_k be the rank three HIGH projector and W_k = Q_k V. Let T
satisfy the effect equation T^sharp T = Q_k and the support condition
Q_k T = T. Then T restricted to W_k is a G-orthogonal automorphism O of W_k
and T = O Q_k. Hence T^2 = O^2 Q_k, and T^2 = delta T with delta = +-1 forces
O^2 = delta O on W_k, so O = delta identity, so T = delta Q_k. Conversely
+Q_k and -Q_k both satisfy it. No symmetry group enters the argument.
```

```text
DA1 regression   CA1 to CA5 and CA9 of run 1 re-run unchanged: carrier from
                 the axiom, the ceiling certificate (20 of 120 relabelings
                 are J-motions, no transposition is affine), the index six
                 statement, centralizer dimensions one and three, the
                 48-member normalizer with 24 sign classes, exhaustive class
                 level idempotence on it, the fork breaker properties, and
                 the target gate last.                          [candidate-T]

DA2 enlarged     In the enlarged fork family {rho(h) X : h in S_k, X in the
                 C_4 centralizer with X^sharp X = Q_k, frozen circle list},
                 the surviving MATRIX set is exactly {+Q_k, -Q_k} at every
                 token; the parametrization is 432 tuples to 240 matrices;
                 every surviving tuple has h affine.            [candidate-T]

DA3 GENERAL      Exact certification of the LEMMA by sweep: for every swept
                 T with T^sharp T = Q_k and Q_k T = T, class level
                 idempotence T^2 = +-T holds exactly at T = +-Q_k. The sweep
                 covers, at every token: the 48 normalizer members; the 240
                 enlarged-family matrices; and a Cayley sample of the
                 rational G-orthogonal group of W_k built from G-skew
                 generators, together with their products against the
                 normalizer members. Sampled, therefore finite range.
                                                                [candidate-C]

DA4 structure    Every swept T factors as O Q_k with O = T on W_k rational
                 and G-orthogonal, and O^2 = delta O implies O = delta
                 identity on the sweep, which is the machine-checkable half
                 of the LEMMA.                                  [candidate-T]

DA5 breaker      An independent second code path reproduces DA1, DA2 and DA3
                 without the 4x4 G-kernel: label-basis 5x5 rational
                 operators, equality tested on differences u_x - u_y, plus
                 the Q direct-sum Q(i) coordinate algebra. It also runs an
                 adversarial search declared in advance: all 48 normalizer
                 members times a wider circle list, and random-free
                 systematic Cayley sweep over a declared integer grid.
                                                                [candidate-T]
```

Consequence to be stated, not computed, carrying no grade: the naturality
fork is orthogonal to the selection question. The centralizer branch, the
normalizer branch, the enlarged family and the full effect-compatible family
are all cut to the single Lueder class by one group-free equation. A positive
closure of O2 therefore does not require choosing between strict S_4
naturality and +-S_4 gauge enlargement. It requires exactly one thing, a
derivation or a falsification of class level idempotence from the record
writing protocol.

## Field 2. Code

```text
verify_qdd_idem_dominates_1b.py   gates DA1 to DA4, own Fraction kernel, no
                                  import from any probe directory, target
                                  gate last.
breaker_qdd_idem_dominates_1b.py  DA5, independent representation, declares
                                  what was attempted and what it failed to
                                  break.
```

Python standard library only, Fraction and int only, no float anywhere,
deterministic, exit nonzero on any FAIL, each under 120 seconds, run from
repository root under
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

## Field 3. Carrier and frozen lists

```text
carrier         (Q^4, G), G = I - (1/5) one one^T, simplex from D powers.
tokens          all five, exhaustive.
normalizer      all 48 members per token, exhaustive.
circle list     t in 0, 1, -1, 1/2, -2, 3, 1/3, -1/5, 7/2 (as in run 1).
wide circle     additionally t = p/q for p in -4..4, q in 1..4, gcd free,
                deduplicated, breaker only.
Cayley sweep    A = sum over the declared skew basis with integer
                coefficients from the grid -2, -1, 0, 1, 2, skipping any A
                with I + A singular on W_k; O = (I - A)(I + A)^{-1} on W_k,
                extended by zero on the P_k line; T = O Q_k. Skew basis:
                J_k, and X - X^sharp for X = rho(h) Q_k over a declared
                ordered list of stabilizer elements, reduced to a basis of
                the three dimensional G-skew space on W_k.
products        every Cayley O composed with every one of the 48 normalizer
                members, at every token.
```

## Field 4. Systematics

```text
S1 parametrization mistaken for the object -> every survivor statement is a
                                              statement about matrices, and
                                              the tuple-to-matrix collapse is
                                              itself a reported gate.
S2 sampling mistaken for exhaustion        -> DA3 is labeled candidate-C and
                                              names its grid; the LEMMA is
                                              the general statement and is
                                              carried as a written derivation,
                                              not as a machine theorem.
S3 confirmation by target proximity        -> target gate last.
S4 sealed code reuse                       -> own kernel; the reproduction
                                              leg is a subprocess only.
S5 threshold movement                      -> forbidden. CF4 of run 1 stays
                                              fired and archived.
```

## Field 5. Failure threshold

Exact, byte level, no tolerance, no retry. PASS only if every declared gate
passes exactly. Any FAIL fires the matching DF, is archived, and becomes the
result. No threshold moves after execution.

## Field 6. Action layer

L4 apparatus and support. No lift. The only permitted output on success is
PROMO-C-QDD-IDEMPOTENCE-DOMINATES-FORK-1, a promotion proposal for a later
public probe and a later sealed fold.
