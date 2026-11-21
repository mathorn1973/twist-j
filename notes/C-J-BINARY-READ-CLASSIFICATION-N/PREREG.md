# C-J-BINARY-READ-CLASSIFICATION-N: pre-execution contract

**PUBLIC notes incubation; NON-CANONICAL; L1. No Canon authority.**

Owner: A. M. Thorn / binary-read-classification session, 2026-10-23.
Reservation: https://github.com/mathorn1973/twist-j/issues/1728.

## 0. Exposure, stated first

This contract freezes a classification whose finite part was seen before
it was written. It is not an unexposed discovery.

- The census of draft pull request #1727 (head
  b1a8704934a813b5f27ea066f659d64383732160) reported binary feasibility for
  u=J and u=phi^-1 at every n=1,...,12.
- A review run by the same session that writes this contract reported that
  the construction inequality P_n>=n*2^n last fails at n=6 for J and at n=8
  for phi^-1, checked exactly for n<120.
- The four explicit certificates in section 3 have the same form as those
  reported by #1727.

What this contract adds is a complete all-n statement, a self-contained proof
(PROOF.md), and three newly written programs frozen before their first
execution. All three programs are by one session, so they are code-distinct,
not author-independent. A run on one architecture is a reproduction, not a
two-architecture gate.

## 1. Equation and complete carrier

O=Z[z]/(z^4+z^3+z^2+z+1), coefficient basis (1,z,z^2,z^3),
J=1+z^2, phi=-z^2-z^3, phi^-1=-1-z^2-z^3, and J=z*phi^-1 exactly.
For a unit u and n>=1, R_n(u)=O/(u^n-1) with tick T(x)=u*x.

A binary reader on R_n(u) is a nonempty T-invariant S in R_n(u) and a map
f:S->{0,1}. The initial state is uniform on S. The n-word
(f(x),f(Tx),...,f(T^(n-1)x)) must be uniform on all 2^n words. S and f may
depend on n. Nothing else is admitted: no counter input, extra memory,
native admission, equivariance or compatibility across horizons.

Notation: F_d=|N(u^d-1)|, P_d=sum_(e|d) mu(d/e) F_e, C_d=P_d/d,
W_d=sum_(e|d) mu(d/e) 2^e, B_d=W_d/d.

**Classification claim, frozen.** A binary reader on R_n(u) exists exactly
when:

```text
u = J        n not in {1, 5}
u = phi^-1   n not in {1, 2, 3, 4, 5, 7}
```

Proposed status: analytical candidate-T (PROOF.md) resting on an exact finite
audit for n<=30. The audit stays candidate-C until it is byte identical on a
second architecture.

## 2. Proof skeleton frozen with this contract

PROOF.md contains:

- L0, cardinality: c*2^n<=F_n with c>=1.
- L1, prime horizon with one fixed point: if n is prime, F_1=1 and
  floor(F_n/2^n)<n, there is no reader.
- L2, unit multiplicity: if floor(F_n/2^n)=1 and F_1<2, there is no reader.
- E1, construction: P_n>=n*2^n gives a reader with c=n.
- CERT: explicit integer assignments under the complete cycle criterion.
- TAIL: for every unit +/-zeta^a phi^(+/-1), P_n>=n*2^n for all n>=31,
  by integer inequalities at n=31 and monotone ratios.

The predicted decision of each n<=30 is:

```text
u = J        L0 at 1; E1 at 2,3; CERT at 4; L1 at 5; CERT at 6; E1 at 7..30
u = phi^-1   L0 at 1,2; L1 at 3; L2 at 4; L1 at 5; CERT at 6; L1 at 7;
             CERT at 8; E1 at 9..30
```

## 3. Frozen certificates

An entry `d: pattern x count` means `count` necklaces of least period d, each
receiving the pattern {e: number of e-cycles}. Each e-cycle contributes e/d
preimages per word.

```text
J, n=4, c=2       d=4: {4:2} x 3   d=2: {2:2} x 1   d=1: {2:1} x 2
J, n=6, c=2       d=6: {6:2} x 9   d=3: {3:2} x 2   d=2: {2:2} x 1
                  d=1: {2:1} x 2
phi^-1, n=6, c=3  d=6: {6:3} x 9   d=3: {3:1,6:1} x 2   d=2: {6:1} x 1
                  d=1: {3:1} x 2
phi^-1, n=8, c=4  d=8: {8:4} x 30  d=4: {4:4} x 1, {8:2} x 2
                  d=2: {8:1} x 1   d=1: {4:1} x 2
```

## 4. Code and data

No external data. Python standard library only, exact integers, no floats,
no randomness, no network.

**verify.py, the proof-structured audit.**

- Counts F_n for n=1..150 by two internal paths, which must agree:
  - V1, the relative norm to K+ in Z[phi] from u=eps*zeta^a*phi^k,
    N_(K/K+)(u^n-1)=(u*ubar)^n-(u^n+ubar^n)+1 with the two-term recurrence
    for u^n+ubar^n, then N(x+y*phi)=x^2+x*y-y^2;
  - V2, the fraction-free integer determinant of M_u^n-I.
- P_n by Mobius inversion, with integrality of C_n checked.
- For each n<=30 the first applicable rule in the order E1, CERT, L0, L1,
  L2. Lemma premises are checked exactly.
- Each certificate is checked for class counts, pattern values, divisibility
  d|e|n and capacities C_e, then realized on an abstract permutation with
  that cycle inventory, with all 2^n word counts checked.
- The TAIL integer inequalities are rechecked at n=31, together with the
  monotonicity thresholds.
- P_n>=n*2^n is audited for 31<=n<=150. That audit does not replace the
  proof.

**break.py, code-distinct paths.**

- B1 counts: the characteristic polynomial of M_u from traces by Newton
  identities, the trace recurrence, power sums t_(jn) for the n-th powers,
  elementary symmetric functions, then F_n=|prod(mu_i-1)| for n=1..150.
- B2 enumeration: for n=1..12 and both units, a lower-triangular column
  Hermite form of M_u^n-I with audited lattice equality, explicit
  enumeration of every class, explicit orbits of T, and cycle counts
  compared with B1 through the fixed-point identity.
- Exhaustive decision for n<=8 on the measured cycle counts, over every
  multiset of patterns per necklace class and every c<=floor(F_n/2^n).
  This uses no lemma.
- End-to-end realization on the enumerated quotient for every positive
  n<=12. A support and labeling are built from actual orbits; every
  n-word is computed by iterating the actual tick; all 2^n counts and
  invariance are checked.
- E1 from B1 counts for 9<=n<=30, and the tail audit for 31<=n<=150.

**compare.py** checks that the COUNT rows (n=1..150, both units) and the
CLASS rows (n<=30, both units) of the two stdouts are identical.

## 5. Systematics and scope

Freely selected S, free f, uniform start on S, and n-dependent readers are
part of the contract. Uniform sampling of all of R_n(u) is a different
contract.

The result is a preparation-capacity statement about finite closed J-worlds.
It is not a native-U sampler, Born occurrence law, apparatus, self-location
or physical tick. Other units with |k|=1 are outside the frozen claim; the
TAIL lemma covers them, their finite exceptions are not decided here. No
entropy bridge is reopened and no existing bank or native-reader theorem is
reinterpreted.

## 6. Failure threshold

Any one of the following fails the frozen classification at its stated
scope:

- V1, V2 and B1 disagree on any F_n;
- any C_n is non-integral;
- the enumerated cycle counts contradict B1;
- a lemma premise is false where the predicted decision uses it;
- a certificate fails any check;
- E1 fails at a predicted E1 horizon;
- the exhaustive search finds a reader at an excluded n, or none at a
  claimed positive n<=8;
- an end-to-end realization fails;
- the TAIL inequalities or thresholds fail, or the tail audit fails;
- compare.py reports any difference.

An execution or integrity defect is STOP. It is not repaired and resumed
under this contract. A mathematical mismatch is retained as a failed claim.
No threshold, horizon or certificate may change after the pin.

## 7. Action layer

L1 only. No L1-to-L5 or L5-to-L6 lift is named or used.

## 8. Freeze and execution

The following files are committed as A. M. Thorn <thorn@twistj.com>,
pushed, read back from the public remote, and hashed before any execution:

```text
PREREG.md, PROOF.md, README.md, verify.py, break.py, compare.py
```

Before the pin only text review, syntax compilation and repository integrity
checks are allowed. After the pin, each program runs exactly once from the
repository root:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
python3 notes/C-J-BINARY-READ-CLASSIFICATION-N/verify.py
python3 notes/C-J-BINARY-READ-CLASSIFICATION-N/break.py
python3 notes/C-J-BINARY-READ-CLASSIFICATION-N/compare.py
```

verify.py and break.py run under a 600-second limit each. Their first
stdout is written to EXPECTED.txt and BREAK_EXPECTED.txt in this directory;
compare.py then reads those two files and its stdout becomes COMPARE.txt.
Every first stdout, stderr and exit code is retained, with RUN.md and
RESULT.md. Delivery is a notes-only draft pull request. It makes no change
to the Canon, registry, frontier, probes, workflows or releases.
