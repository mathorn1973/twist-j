<!-- SPDX-License-Identifier: Apache-2.0 -->
# Prepared plenum full-chain record reproduction

NON-CANONICAL / L1. Public intake reservation #1974. This is an exact,
result-exposed reproduction of a selected prepared record and its finite
escape certificate. The source and expected output are frozen publicly
before the new execution. The result was already known; this is not a blind
search, a new phase survey or a physical measurement.

## Frozen contract

Carrier: the integer line with values in O=Z[j], Phi_5(j)=0, represented in
the integral basis 1,j,j^2,j^3. Set rho=j^2, J=1+j^2, lambda=1-j,
phi=-j^2-j^3 and beta_even=0, beta_odd=j^4. Listed values replace beta.
Conjugation sends j to j^4. Put h(z)=z conjugate(z) and
Q(z)=(5 sum z_i^2-(sum z_i)^2)/2.

For x-y in 2O let d=(x-y)/2. The total contact is

    C_rho(x,y)=(x+(rho-1)d, y-(rho-1)d),

and otherwise it fixes (x,y). At letter a, apply it simultaneously to
every pair (i,i+1) with i congruent to a modulo 2. The supplied clock has
p(n)=1 iff v_2(n) is even, n>=1. Initial boundary is n0=1 and the applied
indices are 2 through 196608 inclusive, exactly 196607 updates per history.

The three inputs are declared independently of the expected endpoint:
q=j^3 at -23, X_j(0)=-2jJ at 49, and m_minus=(-8,-2,-4,-6) at 562.
WRITE additionally has X_1(0)=-2J at 1; FAR has that same value at -131073;
ABSENT omits it. All other sites equal beta. There is no finite ring,
deleted writer, absorbing boundary or packet-only replacement dynamics.

Exact output targets, guards and full analytical statements are in
PROOF.md and certificate.json. The selected field and certificate were
exposed before this implementation. PROVENANCE.md discloses the prior
receiver/site selection and the narrower additional finite switch checks.

## Evaluation inventory and failure rule

The verifier recomputes:

1. All three complete raw histories: 589821 full-field ticks in total,
   complete endpoints and initial/final excess S/H accounts, with Q checked
   against the exact half-trace of H.
2. All six stationary-component matching checks, including background
   neighbours, and exact decomposition of each terminal field into its
   retained stationary and outgoing parts.
3. A fresh breadth-first closure from each actual outgoing endpoint component
   under both tau^13(0) and tau^13(1), tau(0)=11,tau(1)=10. This yields
   34 rows and 278528 isolated-field ticks. Every start/end array, seed,
   even shift and all-intermediate min/max must match the fixture. Every
   reached normalized state must have both rows; every output is in that
   reached set. States are normalized by an even anchor.
4. Strict outward shifts and the one-background-site separation from the
   stationary interval, including every intermediate tick. Each component
   span is checked at every tick against 1024 and the closed-set size against 16.
   The expected maximum observed closure span is 1. Cell coefficients are
   bounded by 1000000 and every updated support by 10000 cells.
   Guards abort the run; they never clip integers, truncate the field or
   certify a partial closure. Exhausted limits remain unresolved.
5. Exact receiver difference 2Jlambda, common h=(72,0,44,44), Q=100, and
   equality of the two primary inputs' displayed excess accounts. A finite
   four-block clock-indexing audit checks the implementation convention.

Any mismatched endpoint, omitted defect, account, row, intermediate bound,
closure or required identity fails. Integrity mismatch, a guard failure,
nonzero exit, stderr, timeout or differing exact stdout prevents acceptance;
an operational failure is not automatically a scientific counterexample.
The existing minimal-reproduction runner's 120-second limit is unchanged.

The complete finite reference arrays are included so this reproduction
needs no access to historical archives. Expected output is a prediction
constructed from those exposed arrays, not a record of a run that has yet
occurred. A later RUN.md records the actual first execution and source pin.
Subsequent CI must run this same verifier and expected output on both
required architectures.

## Raw implementation and arithmetic

The field is a dictionary of every deviation from beta. Each matching
collects all pair anchors meeting that finite support before updating any
pair. Pairs are disjoint; every omitted pair has unequal background colours
and therefore refuses. Removing a dictionary entry only restores its exact
background value. No object is discarded from the field.

All integers are unbounded Python integers. Multiplication is integral
convolution reduced by 1+j+j^2+j^3+j^4=0. Rotation by rho is written as its
four integer coefficients. Pair memoization caches only this raw arithmetic
on exact input tuples; it does not cache or assume packet motion, clock
blocks, translations or endpoint classifications. Closure is generated
from computed endpoints, not from fixture start states.

Pair sum and h(x)+h(y) are algebraically conserved: on the admitted domain
x=c+d,y=c-d and rho conjugate(rho)=1; refusal is identity. Sparse finite
propagation therefore conserves the finite excess accounts at each tick.
The program compares full initial/final accounts; it does not claim to emit
or separately recompute every intermediate account.

## Scope of the future conclusion

The finite run is not a simulation of infinite time. The generic proof in
PROOF.md uses even translation, local matched-pair input equality, closed
outward transitions and induction over aligned blocks. The identity
v_2(2^18 h+k)=v_2(k),2<=k<=196608, extends the complete finite history to
every integer h>=0. It does not extend success to every initial clock phase.

The specific permanent-record consequence retains proposed status C because
its finite premise is computational. Its phase and all-future extension are
analytical. The generic implication is separately proposed T. No T item
requires a C item. Both remain noncanonical until a separately accepted fold.

Input equality concerns S,H,Q only; the reduced colour words differ. The
novelty is remote transfer of an existing pointer distinction. Receiver-only
invariant indistinguishability is compatible with distinct q positions and
outgoing signs in the whole field. Formation, later active reading, reuse,
full native U, occurrence and physical energy calibration are not established.

## Reproduction

From the repository root:

    python reproduce/plenum-full-chain-record/verify.py

Expected success: exit 0, empty stderr and stdout byte-identical to
EXPECTED.txt. The policy workflow's changed-reproduction step executes it
on x86_64 and aarch64; a notes-only green check is insufficient. The later
Canon fold must run the complete repository inventory on both architectures.

The intake manifest and reconciliation are under
legacy/plenum-full-chain-record-intake/. Source exposure and the separate
historical implementations are preserved there without importing their
development histories. Internal review is not an external-review claim.
