# P-SPLIT-RAPIDITY-QUANTITATIVE-SEPARATION-1 preregistration

Two L1 theorem claims are frozen here.  The first gives a quantitative
separation bound for every nonzero merged vector of split-prime rapidities.
The second is its finite Fejer-kernel operator corollary.  The written proofs
below carry the universal statements.  The verifier is an exact finite audit
and carries no universal quantifier.

## Authority record

```text
STATE:          ACTIVE
CANON:          Public Canon v45
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v45
CONTENT_COMMIT: cbd248274d67a861611787ba6e7be3e6a13b29f1
CANON_SHA256:   f3f8954bda620836e604d08d9088587ea84429ecdadfc27737e83b0f8031128b
CANON_BYTES:    214608
BASE_COMMIT:    84e7a81faaffa70d04398b4e535cf7b456624dc2
CLAIM_ISSUE:    https://github.com/mathorn1973/twist-j/issues/350
```

The currency gate was run before the claim issue and before this pin against
a freshly fetched public `main`.  `main` and the peeled `canon-v45` tag both
equal the base commit above; the declared content commit is their ancestor;
the Canon hash and byte count agree with `STATUS.md`; `canon/SHA256SUMS` is
5 of 5; and the public main, tag-publication, and release-readback workflows
are successful.  No matching public issue, branch, probe directory, pull
request, or registry identifier existed at claim time.

## Source and review boundary

The non-authoritative preparation input is the unchanged handoff commit
`3eb3edb18d9e32845b375eb15b18a5fc0fd054a4`, package
`v46-preparation-2026-08-12/`.  Its manifest contains 30 of 30 package files,
excludes itself, and has SHA-256
`af0949c445f6f810955af9516dc95fd8fe9ecb6b4704a8e98f9d0f76d35bb75d`.
The byte-preserving Linux aggregate audit reports 5 of 5 PASS.  Four frozen
programs exit zero, write no stderr, and reproduce their expected stdout byte
for byte.  Those facts are review inputs only; public authority starts with
this issue, pin, public run record, reviewed probe, and later Canon fold.

Two independent line-by-line proof reviews accepted the determinant theorem
and the Fejer corollary.  Their corrections are binding here:

- every displayed prime generator in the theorem has signed norm `+p`;
  consequently the discarded mixed-sign decimal comparison for `421/431` is
  not used.  In the positive-norm convention the corresponding controls are
  `d_L = 0.0011737895036417...` and
  `d_2L = 0.4800380355559618...`; the proof uses the stronger exact
  norm, trace, and half-band identities instead;
- the determinant lattice is parity-sensitive and uses absolute value:
  for even `n`, `|D_c|` lies in `sqrt(5) Z_{>0}`, while for odd `n`,
  `|D_c|` lies in `Z_{>0}`.  A negative determinant is valid and cannot be
  rejected merely for its sign.

The zeta and K4 preparation lanes are not part of this probe.  The abstract
Fejer character is not identified with a Hecke character or an `End` mode.

## Claim A: SPLIT-PRIME-RAPIDITY-QUANTITATIVE-SEPARATION

Put

```text
F = Q(sqrt5),  O_F = Z[phi],  phi = (1+sqrt5)/2,  L = log phi.
```

For every split rational prime `p`, fix an oriented prime ideal `P_p` above
`p`.  Class number one and the norm-minus-one fundamental unit permit a
generator `pi_p` with

```text
(pi_p) = P_p,  N(pi_p) = +p,
```

and a common sign makes both real embeddings positive.  Define

```text
eta_p = (1/2) log(pi_p / conj(pi_p)).
```

For any finite input list `(p_j, epsilon_j, a_j)`, with
`epsilon_j` in `{+1,-1}` and integer `a_j`, first merge every repetition and
conjugated orientation over the same rational prime:

```text
c_p = sum_{j:p_j=p} epsilon_j a_j.
```

Delete zero coefficients.  For the resulting nonzero vector `c`, put

```text
P(c) = product_p p^|c_p|.
```

The claim is

```text
dist(sum_p c_p eta_p, L Z)
    >= asinh(1 / (2 sqrt(P(c)))).
```

There is a parity refinement.  Let `S = sum_p c_p eta_p`, let `n` be the
unique nearest integer to `S/L`, and set `delta = S - nL`.  Then

```text
n even: |delta| >= asinh(sqrt(5) / (2 sqrt(P(c)))),
n odd:  |delta| >= asinh(1 / (2 sqrt(P(c)))).
```

If `n` is odd and `P(c) = -1 (mod 5)`, the numerator `1` improves to `2`.

### Proof of claim A

Form the totally positive element

```text
x = product_{c_p>0} pi_p^c_p
    product_{c_p<0} conj(pi_p)^(-c_p).
```

Then `N(x)=P(c)` and its rapidity is `S`.  Put `y=phi^(-n)x`.  Since
`N(phi)=-1`, its two embeddings are

```text
y  = sqrt(P(c)) exp(delta),
y' = (-1)^n sqrt(P(c)) exp(-delta).
```

Therefore the pre-trace determinant is exactly

```text
D_c = y - (-1)^n y' = 2 sqrt(P(c)) sinh(delta),
```

and hence

```text
sinh^2(dist(S,L Z)) = D_c^2 / (4 P(c)).
```

Write `y=a+b phi` and `T=Tr(y)=2a+b`.  If `n` is even then
`D_c=b sqrt(5)`; if `n` is odd then `D_c=T`.  The determinant does not
vanish.  If it did, `delta=0` and `x/x'=phi^(2n)`.  On fractional ideals the
right side is the unit ideal, whereas directly

```text
v_{P_p}((x/x')) = c_p.
```

Thus every `c_p=0`, contrary to the domain condition.  This proves the exact
positive lattices

```text
n even: |D_c| in sqrt(5) Z_{>0},
n odd:  |D_c| in Z_{>0},
```

and the stated lower bounds.  It also shows why the sign of `D_c` is not a
falsifier.

The nearest integer is unique: a tie would put `2S` in `L Z`, and the same
argument applied to `2c` would force `c=0`.  The norm equations are

```text
T^2 - 5b^2 = +4P(c)  for even n,
T^2 - 5b^2 = -4P(c)  for odd n.
```

In the odd branch with `P(c)=-1 (mod 5)`, the second equation gives
`T^2=4 (mod 5)`, so `|T|>=2`.

Changing a positive-norm lift on a fixed oriented ideal multiplies `pi_p` by
`phi^(2k)` up to common sign.  It changes `n` by an even integer and preserves
the parity branch, determinant lattice, and `D_c^2/P(c)`.  Conjugating an
orientation and reversing its coefficient also preserves the metric.  The
projected unordered public class does not select a global orientation or a
global parity sheet.

Two distinct public unordered split-prime classes have a unique minimizing
signed channel up to simultaneous conjugation.  Equality of the sum and
difference gaps would imply that twice one class vanishes, contradicting
`SPLIT-PRIME-RAPIDITY-INDEPENDENCE [T]`.

The universal numerator `1` is sharp.  With

```text
pi_11 = 3+phi,  pi_41 = 6+phi,
phi^(-1) pi_11 pi_41 = -9+19phi,
```

the translated element has norm `-451`, trace `1`, and lies in the exact open
half-band.  The second witness

```text
pi_421 = 19+4phi,  pi_431 = 19+5phi,
phi^(-1) pi_421 pi_431 = -190+381phi
```

has norm `-421*431`, trace `1`, and also lies in that half-band.  These are
finite equality witnesses for the constant, not an asymptotic least-gap law.

## Claim B: SPLIT-RAPIDITY-FEJER-GRAM-BOUND

Let `A` be a nonempty finite set of distinct oriented split prime-power
addresses

```text
a=(p,m,epsilon),  m>=1,  epsilon in {+1,-1},  p^m<=X,
beta_a = epsilon m eta_p in R/(L Z).
```

If `|A|>=2`, define

```text
delta_A = min_{a!=b} dist(beta_a-beta_b, L Z).
```

Merging an address difference gives a nonzero effective vector with product
budget at most `X^2`.  Claim A therefore gives

```text
delta_A >= asinh(1/(2X)).
```

For integer `K>=0`, define the normalized Fejer kernel and Gram matrix

```text
Phi_K(u) = 1/(K+1) sum_{|h|<=K} (1-|h|/(K+1)) exp(2 pi i h u)
         = 1/(K+1)^2 (sin(pi(K+1)u)/sin(pi u))^2,
(A_K)_{ab} = Phi_K((beta_a-beta_b)/L).
```

The continuous value of `Phi_K` at an integer is `1`.  The character family
`chi_h(a)=exp(2 pi i h beta_a/L)` is part of this definition and is abstract.

The claim is

```text
||A_K-I||_{2->2}
 <= pi^2 L^2 / (12 (K+1)^2 delta_A^2)
 <= pi^2 L^2 / (12 (K+1)^2 asinh^2(1/(2X))).
```

For a singleton, `A_K=[1]` and the norm is zero; no spacing minimum is needed.

### Proof of claim B

The normalized kernel satisfies

```text
0 <= Phi_K(u) <= min(1, 1/(4(K+1)^2 ||u||^2)).
```

For a fixed address, partition the other points into half-open circular
shells

```text
S_j = {b: j delta_A <= dist(beta_a,beta_b) < (j+1) delta_A}, j>=1.
```

Each shell has at most one point on either side of the circle and therefore
at most two points.  Hence every off-diagonal row sum is at most

```text
2 sum_{j>=1} L^2/(4(K+1)^2 j^2 delta_A^2)
 = pi^2 L^2/(12(K+1)^2 delta_A^2).
```

Schur's test gives the first bound, and the separation estimate gives the
second.  As `X` tends to infinity, this is

```text
[pi^2 L^2/3 + O(X^-2)] (X/(K+1))^2.
```

Thus `K(X)/X -> infinity` is sufficient uniformly over families of such
finite sets `A_X`.  The decimal value of `pi^2 L^2/3` is only an asymptotic
coefficient and is never substituted into the exact finite bound.

### Normalization firewall

No Hecke, `xi_k`, `xi_(2k)`, or `End` identification is made.  If an integral
phase multiplier `nu` is later pinned, then

```text
P(nu c) = P(c)^|nu|.
```

The budget is unchanged only for `|nu|=1`, `nu=0` is the excluded diagonal,
and `|nu|>=2` requires a new spacing derivation.  A nonintegral multiplier is
outside claim A's integer carrier.

The exact `491/1429` control keeps two facts separate.  The ordinary signed
channels have determinant rungs `22` and `182`; they are controls of the
base convention.  The actual doubled-phase negative control instead uses
the effective vector `(2,2)`.  With

```text
x = (20+7phi)(34+13phi),  P=491*1429,
phi^(-3)x^2 = -313768+627565phi,
```

the trace is `29` and

```text
sinh^2(d_2) = 841/(4P^2) < 1/(4*1429^2).
```

This falsifies reuse of the unchanged `X` spacing budget after phase
doubling.  It is not a counterexample to claim A, whose correct budget is
`P^2`, and it is not by itself a claim about a concrete operator-norm
violation.

## Field 1. EQUATION and gate inventory

The verifier maps exactly to these finite audit gates:

```text
G1 effective-vector merging is permutation invariant and removes the exact diagonal
G2 the norm -451 equality witness has trace 1 and is in the exact half-band
G3 the positive-norm 421/431 witness has trace 1 and is in the exact half-band
G4 every split prime below 2001 has an exhibited reduced exact generator
G5 all frozen pair readings have nonzero determinant and unique nearest channel
G6 both parity lattices satisfy their exact norm identities
G7 the frozen minimum is ordered by rational cross multiplication without logs
B1 an independent bounded four-prime relation breaker finds no zero or tie
B2 positive-norm even-unit gauge changes preserve the minimum and parity branch
B3 orientation reversal with coefficient reversal preserves the exact metric
F1 every frozen two-address difference has product budget at most X^2
F2 normalized Fejer coefficient weights sum to one for every frozen K
F3 every frozen separated circular set obeys the two-points-per-shell bound
F4 the singleton Gram matrix is the identity
N1 the 491 and 1429 generators have the declared positive norms
N2 the two ordinary signed channels have rungs 22 and 182
N3 the doubled vector has budget P^2, odd nearest shift, and trace 29
N4 numerator 841 violates reuse of the undoubled X spacing bound exactly
```

## Field 2. CODE

`probes/P-SPLIT-RAPIDITY-QUANTITATIVE-SEPARATION-1/verify.py`.  Python
standard library only; exact integers only; no floating point, logarithm,
trigonometric evaluation, or numerical eigensolver.  The B gates are an
independent bounded breaker embedded in the one accepted verifier.  The N
gates are the exact normalization negative control.  The command is

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-SPLIT-RAPIDITY-QUANTITATIVE-SEPARATION-1/verify.py
```

Runtime limit: 120 seconds.

## Field 3. CARRIER AND DATA

The carrier is `Z[phi]`, conjugation, signed norm, trace, fractional-ideal
valuations, and the circle `R/(log(phi))Z`.  There is no external dataset.
The finite determinant audit uses the 146 split primes below 2001 and 21,316
pair readings.  The breaker covers all 624 nonzero vectors in `[-2,2]^4`
over primes `11,19,29,41`, plus gauge and orientation variants.  The Fejer
audit uses exact coefficient counts and finite rational circle combinatorics.

## Field 4. SYSTEMATICS

- merge repeated and conjugated addresses before testing nonzero input;
- keep signed norm, nearest-shift parity, and determinant sign distinct;
- compare metric squares only by integer cross multiplication;
- require positive-norm even-unit gauge invariance and matched orientation
  reversal;
- use a finite address minimum, never an unrestricted integer-combination
  infimum;
- keep the exact `asinh` denominator in every finite bound;
- treat the decimal coefficient only asymptotically;
- keep phase normalization and every Hecke interpretation outside both rows.

## Field 5. FAILURE THRESHOLD

Claim A is falsified by one exact split-prime input with nonzero merged vector
and zero determinant, a violation of its bound, or a failure of the exact
parity rule

```text
n even: |D_c| in sqrt(5) Z_{>0}; n odd: |D_c| in Z_{>0}.
```

It is also falsified if a permitted positive-norm even-unit gauge change
changes the exact metric or parity branch.  A negative value of `D_c`, such
as the valid `-182 sqrt(5)` control, is not a failure.

Claim B is falsified if a finite nonempty set of distinct declared addresses
with `p^m<=X` has spacing below `asinh(1/(2X))`, or if for some integer
`K>=0` its defined matrix violates either displayed operator-norm bound.  For
a singleton it fires only if `A_K != [1]`.  A Hecke or `End` interpretation is
outside the row and remains a normalization STOP.

Any verifier/expected-output/hash mismatch, nonempty stderr, architecture
failure, undeclared check, changed threshold, or failed normalization
firewall without an exact mathematical negation is an integrity STOP, not a
scientific falsifier.

## Field 6. ACTION LAYER AND NON-CLAIMS

Layer L1 exact arithmetic and one finite split-address operator estimate.
No lift to L2 through L6 is claimed.  Explicitly not claimed: an unrestricted
least gap, an asymptotic least-gap law, prime distribution, Pell
parametrization, inert or ramified diagonalization, gamma or polar control,
completed-zeta compression, a Hecke-family identification, Weil positivity,
RH, zero simplicity, K4 classification, decoder movement, measure, observer,
physical interpretation, or SI statement.

## Formal sequence

This preregistration, `verify.py`, and the frozen expected stdout are committed
and pushed before the first formal execution.  The formal local leg must use a
clean pinned descendant, exit zero, write empty stderr, and match the expected
stdout byte for byte.  `RUN.md` and `RESULT.md` are then added without changing
these bytes.  The public pull request must reproduce the same output on the
required x86_64 and aarch64 jobs.  A later v46 fold is a separate reviewed
release transaction.
