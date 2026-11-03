# Funded two-pass renewal: fixed exact replay

**NON-CANONICAL / L1. Result-exposed finite replay specification.**

The analytical construction and its fixed-cylinder identities precede
this verifier. This is not a blind discovery experiment. The complete
source and this specification must be publicly committed and read back
before the first execution of the new scientific verifier. No adaptive
extension or undisclosed discovery search is part of this replay.

## 1. Exact carrier and declared input family

Work in O=Z[rho], with rho^5=1 and

    1+rho+rho^2+rho^3+rho^4=0.

Represent elements by four integer coefficients in the basis
(1,rho,rho^2,rho^3). Write

    U_d=1-rho^d, J_d=1+rho^d, d in {1,2,3,4},
    F_(3,d)(n)=(U_d*n,(12-J_d)*n,2J_d).

Native C is the identity on a pair whose difference is not in 2O.
Otherwise it preserves the center and multiplies the relative
coordinate by rho. Every C^e means e actual consecutive applications
of this same primitive, with 1<=e<=4. A powered contact is not
implemented by substituting the expected final formula.

For h>=0 define the fixed infinite arithmetic cylinder

    n0=64h+3,
    n1=96h+5,
    n2=18h+1.

Its prescribed two accelerated steps have valuations one and four:

    3n0+1=2n1,
    3n1+1=16n2.

The source charts are d0=d, d1=4d mod 5 and d2=3d mod 5, with
nonzero residues represented in {1,2,3,4}. These identities specify
the analytical contract. Actual contact evolution, current-state
reading and independent closed output formulas must agree with them.

This is a fixed known valuation cylinder. The verifier does not
claim that the apparatus selects an unknown valuation branch or
chooses its own initial chart.

## 2. All resources are present in the initial state

Each case has exactly 33 core slots and two literal old archives,
for a complete state of 35 ring elements.

| Slots | Initially supplied contents |
|---|---|
| 0,1,2 | F_(3,d)(n0) |
| 3 through 15 | Thirteen zeros for the first division archive |
| 16 through 28 | Thirteen zeros for the second division archive |
| 29,30 | Two first-renewal donor banks |
| 31,32 | Two second-renewal donor banks |
| 33,34 | Literal old archives rho and 1+rho^3 |

The four donor banks use the declared affine loading formulas in h,
with fixed ring coefficients determined by d. The loading interface
receives h and d only. It must not call an accelerated Collatz
routine, read a computed odd part or depth, inspect an intermediate
apparatus output, or insert a donor after execution has started.

The corresponding closed formula supplies an independent check of
those affine donors. If a current port is a, its required target is
y, and the reset uses C^e, its donor is

    D_e(a,y)=a+2(y-a)/U_e.

The quotient must be exact in O. In the literal native contact this
gives

    C^e(a,D_e(a,y))=(y,a+D_e(a,y)-y).

The second component is the actual occupied waste bank and remains
in the complete state. No clearing or overwrite outside native
contacts is allowed. This formula is the independent oracle for the
predeclared donor coefficients and their spent outputs, not a
runtime resource-loading operation.

Both old archives contribute to the initial account and must stay
literally equal to their initial values. New records from the first
pass must remain literally unchanged during the entire second pass.
Spent first-renewal donors likewise remain present and untouched
after their use.

## 3. Fixed complete native word

Let W_d use the two powered prefix contacts C_(01)^d C_(02)^d,
followed by thirteen powered contacts from slot 0 to successive
fresh-zero targets. For target stage s=1,...,13 its exponent is

    e_s=2^s*d mod 5 in {1,2,3,4}.

The new complete word is:

1. W_d on slots 0,1,2 and first targets 3,...,15.
2. C_(1,29)^d and C_(2,30)^d, renewing the two occupied source ports.
3. W_(4d) on slots 0,1,2 and second targets 16,...,28.
4. C_(1,31)^(4d) and C_(2,32)^(4d), with each exponent reduced to
   {1,2,3,4}, renewing the source a second time.

No edge, exponent, stopping rule or port is selected from an
observed intermediate result. The first chart d is a supplied
interface parameter. Each case executes the whole corresponding
word, including all refused contacts after each finite division
prefix.

There are 34 powered-contact macros. Their primitive lengths are

| Initial d | First pass plus renewal | Second pass plus renewal | Total |
|---:|---:|---:|---:|
| 1 | 36 | 49 | 85 |
| 2 | 42 | 43 | 85 |
| 3 | 43 | 42 | 85 |
| 4 | 49 | 36 | 85 |

The complete native inverse reverses those 34 macros and replaces
each C^e by C^(5-e). It uses another 85 primitive applications and
must restore all 35 initial slots exactly.

## 4. Fixed finite corpus

Every bound below is inclusive. Run the following two groups in the
listed order, and each group in the stated parameter order.

### A. Consecutive cylinder parameters

For h=0,...,1023, in increasing order, run d=1,2,3,4 in increasing
order. This gives 4096 complete cases and their complete inverses.

### B. Fixed large integer parameters

For k in (32,64,128,256), in that order, and a in (-1,0,1,7), in
that order, set

    h=2^k+a.

For each of these sixteen parameters run d=1,2,3,4, in increasing
order. This gives another 64 complete cases and their inverses.
These are exact integer cases, not floating-point scale tests.

The total is 4160 complete forward cases and 4160 native inverse
restorations. Every case has the same scalar valuations (1,4),
but different inputs, supplied charts and fully occupied outputs.

## 5. Assertions and independent descriptions

### A. Every actual native primitive

For each accepted primitive pair, check its ring sum, real-quadratic
Hermitian account a*bar(a)+b*bar(b), positive integer account and
both labelled residues before and after the literal coordinate
transformation. Here conjugation is sigma_4(rho)=rho^4; the
Hermitian account is checked as an exact ring element, not only
after taking its trace. Refused primitives leave the pair
unchanged. The integer account and residue are

    Q(z)=(5*sum_i zi^2-(sum_i zi)^2)/2,
    epsilon(z)=sum_i zi mod 5.

The code must keep explicit integer counters for accepted,
refused and total primitive applications. Within each powered
macro, the enabled/refused status must remain constant.

### B. Actual affine prefixes and division archives

For each pass, compare both powered prefix boundaries with their
independent ring formulas. If the pass starts in chart e with
integer n, the prefix leaves

    active=U_(2e)*(3n+1),
    slot1=2(3J_e-rho^e)*n,
    slot2=3U_e^2*n+J_e^2.

Compute the actual accepted/refused powered cascade prefix and
require depths one and four for the two passes respectively. The
full thirteen-port output must agree with

    record_s=U_(2^s e)^2*2^(v-s)*m  for 1<=s<=v,
    record_s=0                    for v<s<=13,
    active=U_(2^(v+1)e)*m.

Read the scalar and chart from the current active coefficient
shape, and the depth from the present nonzero target prefix.
Require the first read to be (n1,4d,1) and the second to be
(n2,3d,4), with charts reduced modulo five. The reader may not
obtain its result from the closed oracle or source leftovers.

### C. Both actual renewals and the complete final state

Immediately before each reset, compare the literal loaded donor
against D_e(a,y) using the actual occupied old port a and the
declared target y. Check integral divisibility by U_e. Execute
the actual powered contact and require both its output port and
its spent donor bank to equal the independent formulas.

After the first reset, slots 0,1,2 must be exactly
F_(3,4d)(n1). After the second reset they must be exactly
F_(3,3d)(n2). The active port must be unchanged by each two-port
reset. Compare all 35 final slots with an independently assembled
closed oracle containing the renewed source, both complete new
archives, all four actual spent banks, and both old archives.

Check the complete sum, account and every labelled residue
against the initial 35-slot state. In particular, all donors
are funded in that initial state; no record, leftover, second
pass bank or old archive is omitted from the accounting.

Also audit the explicit scalar-account polynomials of the
33-slot core, with the two unchanged old archives counted
separately in the complete invariant:

    initial four donors: 5422160h^2+555480h+14368,
    final four spent banks: 5851540h^2+585660h+14798,
    both fresh archives: 551340h^2+60300h+1650,
    complete core: 6487120h^2+655320h+16720.

For h=0, the explicit scalar path is 3->5->1. The first two
donors have account 10504 initially and 5969 after their use;
all four final banks have account 14798. These are accounted
supplied resources and occupied outputs, not minimum-funding
or bank-restoration claims.

### D. Galois covariance and literal old archives

For each fixed h, compare the four chart runs at every one of
their 34 corresponding forward powered-contact boundaries.
Their 33-slot cores must satisfy sigma_d(z), where
sigma_d(rho)=rho^d, relative to the d=1 case.

The old archives at slots 33 and 34 are supplied as the same
literal values rho and 1+rho^3 in every case. They are therefore
checked for literal retention and are excluded from the Galois
core comparison. No physical Galois transformation is executed.

### E. Complete native inverses and call counts

The inverse executes the reversed native powers, rather than
assigning saved initial values. Require exact equality of all
35 slots to the initial state after it finishes.

Each case uses 85 forward and 85 inverse primitives. It has
thirteen accepted forward macros: five in the first pass with
reset and eight in the second. A macro and its inverse together
use five primitives with the same enabled/refused status.
Consequently the exact per-case counts are

    65 accepted + 105 refused = 170 primitives.

Across all 4160 cases the required totals are

    accepted: 270400,
    refused:  436800,
    total:    707200.

These counts are analytical consequences of the frozen word and
valuation cylinder, not values guessed from an unrecorded run.

## 6. Output, pin and preservation contract

Run the publicly pinned verifier from the repository root with
Python >=3.12, assertions enabled and no arguments:

    python3 -I notes/C-CONTACT-FUNDED-TWO-PASS-RENEWAL-N/verify.py

All scientific arithmetic is integer or exact ring arithmetic.
No floating-point tolerance, randomness, external input file,
network lookup or adaptive search is part of this verifier.

The complete-output SHA-256 fingerprint covers the ordered
sequence of all 35-slot forward final states, including spent
banks and literal old archives. Serialize each record as the
compact JSON array [tag,h,d,state], with separators (",",":"),
encode it as ASCII, and append one newline. The group tags are
"dense" and "large", in the corpus order fixed above. Update
the hash before inverting each state. Do not guess or fabricate
the fingerprint before first execution.

Success requires every assertion, exit zero and empty stderr.
Preserve the actual first stdout before adopting it unchanged
as EXPECTED.txt. Record the public source pin, verifier and
specification hashes, command, exact Python version, neutral
operating system and architecture, exit code, byte counts and
stdout/stderr hashes. A failure or mismatch must be preserved;
it must not be silently converted into an expected success.
Any verifier or scientific scope correction requires a new
explicit public pin and new execution evidence.

The mathematical claim quantified over all h>=0 belongs to the
companion analytical proof. This finite corpus does not prove
an infinite family by extrapolation. It realizes two explicitly
funded renewals on one predeclared valuation cylinder, with four
initially supplied chart-indexed words. It does not supply a
general branch selector, an autonomous source-renewal law,
unlimited bank reuse, free erasure, or Collatz convergence.

The general finite-itinerary compilation corollary is also
proof-only here. The verifier does not enumerate additional
valuation words: its entire corpus remains the 4160 cases of
the single word (1,4) specified above.

The initial donors are affine encodings designed for this known
two-step cylinder. They are declared resources, not an emergent
loading mechanism or a proof of preparation from one raw scalar
port. A scientific execution on one architecture has only its
stated candidate-C scope. Ordinary repository architecture CI
does not execute this notes-only verifier and cannot be counted
as an additional scientific implementation or architecture.
