# P-TM-MULTIPLICATION-CARRY-DEFECT-1 preregistration

Date: 2026-08-10

Author of record: A. M. Thorn

Status: preregistered protocol only. No scientific result is earned by this
file. No formal gate may run before this file and the accepted verifier are
both present at the immutable pin, that pin is pushed, and both files are read
back from the public remote.

Public claim lock: issue 331.

## Authority record

```text
STATE:          ACTIVE
CANON:          Public Canon v40
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v40
CONTENT_COMMIT: c34c04618d6ed4035266cd8ad6c27915536bebf5
CANON_SHA256:   54842ab0327b7c3be44242dbc6cbe52682e92aa2098978fcf4cd4727480d0d38
CANON_BYTES:    189737
BASE_COMMIT:    121f705d5fa4e7b1a09cd9e1977c1fb1346c01a9
```

The governing authority is `mathorn1973/twist-j` on `main`. This probe is L1
only. It opens no inter-layer gate.

## Collision and lineage disclosure

This probe is deliberately separate from the existing carry program.

- `CARRY-PENTAD [T]` and open issue 316
  `P-CARRY-QUADRATIC-SYMMETRY-1` concern the quadratic Boolean carry layer
  `e_2` on finite vector spaces and its symmetry geometry.
- issue 317 `C-BOOLEAN-CARRY-J-ORBIT-1` is NON-CANONICAL and concerns a
  conditional Boolean-to-J bridge.
- `RAMIFIED-TM-LIFT [T]` contains the chronological binary-addition carry
  cocycle `nu_2(n+1)`.
- The present object `kappa_2(a,b)` is instead the total unit-carry value in
  ordinary binary multiplication of positive integers.
- The completed public probe `P-MOBIUS-TM-PRIME2-1` is adjacent. Its theorem
  candidate `MOBIUS-TM-PRIME2-BRIDGE` is not yet a Canon row at this pin.
  Every use of `c=mu*tau` below is rederived directly, so this probe does not
  depend on an unregistered claim.

No exact issue, branch, probe path, or Registry row named
`TM-MULTIPLICATION-CARRY-DEFECT` or
`P-TM-MULTIPLICATION-CARRY-DEFECT-1` existed before issue 331.

## Mandatory result-exposure disclosure

The owner has already seen the formulas, examples, and the complete semiprime
truth table in conversational analysis before this public preregistration.
This is proof-first confirmation, not blind discovery.

No accepted verifier under this probe id existed or ran before the public
claim lock. Any prior conversational arithmetic is provenance only and is not
public evidence.

## Field 1: equation

### Fixed notation

For a positive integer `n`, let

```text
s2(n)  = binary digit sum (popcount)
tau(n) = (-1)^s2(n)
mu(n)  = Moebius function
c      = mu * tau
```

For bits, `XOR`, `AND`, and `OR` mean the ordinary Boolean operations with
values in `{0,1}`.

The theorem target is one L1 arithmetic package with five clauses.

### S1. Canonical binary multiplication carry mass

Write

```text
a = sum_i a_i 2^i,
b = sum_j b_j 2^j,
a_i,b_j in {0,1}.
```

Before carry normalization the schoolbook product has column multiplicities

```text
r_k = sum_(i+j=k) a_i b_j,
ab  = sum_k r_k 2^k,
sum_k r_k = s2(a)s2(b).
```

Set `q_-1=0`. For `k>=0`, with `r_k=0` beyond the last raw column, define

```text
u_k = r_k + q_(k-1),
z_k = u_k mod 2,
q_k = (u_k-z_k)/2,
```

and continue until both the raw columns and the carry vanish. Then `z_k` are
the binary digits of `ab`.

Define

```text
kappa_2(a,b) = sum_k q_k.
```

Summing the recurrence

```text
r_k + q_(k-1) = z_k + 2 q_k
```

over all `k` gives

```text
kappa_2(a,b)
  = sum_k r_k - sum_k z_k
  = s2(a)s2(b)-s2(ab) >= 0.
```

This is a canonical total **unit-carry value**. Equivalently, if normalization
is performed by elementary moves

```text
2 * 2^k -> 1 * 2^(k+1),
```

each move lowers the total coefficient mass by exactly one, and every complete
forward normalization ends at the unique binary expansion of `ab`. Hence every
such normalization uses exactly `kappa_2(a,b)` unit carry moves. This is not a
claim about an algorithm-dependent count of grouped carry events.

### S2. AND plus carry-XOR parity and the exact multiplicativity defect

Put

```text
P = s2(a) mod 2,
Q = s2(b) mod 2,
K = kappa_2(a,b) mod 2,
R = s2(ab) mod 2.
```

Reducing S1 modulo two gives

```text
R = (P AND Q) XOR K.
```

Since `tau(n)=(-1)^(s2(n) mod 2)`,

```text
tau(ab) tau(a) tau(b)
  = (-1)^(R XOR P XOR Q)
  = (-1)^((P OR Q) XOR K).
```

The Boolean identity used in the final step is

```text
(P AND Q) XOR P XOR Q = P OR Q.
```

Thus `tau` is multiplicative at `(a,b)` exactly when

```text
K = P OR Q.
```

This is an exact sign statement only. No physical interaction is inferred.

### S3. Complete semiprime shadow classification

Let `p` and `q` be distinct odd primes. Since

```text
mu(1)=1, mu(p)=mu(q)=-1, mu(pq)=1, tau(1)=-1,
```

one has

```text
c(pq) = tau(pq)-tau(p)-tau(q)-1.
```

Put

```text
P=s2(p) mod 2,
Q=s2(q) mod 2,
K=kappa_2(p,q) mod 2.
```

By S2,

```text
c(pq)
 = (-1)^((P AND Q) XOR K)-(-1)^P-(-1)^Q-1.
```

The complete eight-case table is frozen:

```text
P Q K | c(pq)
0 0 0 | -2
0 0 1 | -4
0 1 0 |  0
0 1 1 | -2
1 0 0 |  0
1 0 1 | -2
1 1 0 |  0
1 1 1 |  2
```

Therefore

```text
c(pq) in {-4,-2,0,2},
c(pq)=0 iff K=0 and (P OR Q)=1.
```

A zero `c(pq)` is a zero top Moebius mixed difference, not an absence of
carries. The fixed counter-control is

```text
p=3, q=11:
s2(3)=2, s2(11)=3, s2(33)=2,
kappa_2(3,11)=2*3-2=4,
c(33)=0.
```

For contrast, the zero-carry shadow `(p,q)=(7,17)` has
`kappa_2(7,17)=0` and `c(119)=0`, while `(3,113)` has
`kappa_2(3,113)=3` and `c(339)=-4`.

### S4. Prime-square shadow

For every prime `p`, only the divisors `1` and `p` contribute to
`c(p^2)` because `mu(p^2)=0`, so

```text
c(p^2)=tau(p^2)-tau(p).
```

Apply S2 with `a=b=p`. Since `P AND P=P`,

```text
s2(p^2) mod 2 = P XOR (kappa_2(p,p) mod 2).
```

Hence

```text
c(p^2)=0
iff s2(p^2)=s2(p) mod 2
iff kappa_2(p,p) is even.
```

### S5. Higher squarefree carry-field representation

Let

```text
n = product_(i=1)^m p_i
```

be odd and squarefree, with distinct primes `p_i`. For every subset
`S subseteq {1,...,m}`, define

```text
n_S     = product_(i in S) p_i,
A_S     = product_(i in S) s2(p_i),
kappa(S)= A_S-s2(n_S),
K(S)    = kappa(S) mod 2,
P_i     = s2(p_i) mod 2.
```

Use the empty conventions

```text
n_empty=1, A_empty=1, kappa(empty)=0,
AND_(i in empty) P_i = 1.
```

The raw multi-product has coefficient-mass `A_S`; binary normalization ends
with coefficient-mass `s2(n_S)`. The same unit-carry mass argument as S1 gives
`kappa(S)>=0`, and modulo two,

```text
s2(n_S) mod 2 = (AND_(i in S) P_i) XOR K(S).
```

Directly from the definition `c=mu*tau`, divisors of squarefree `n` are
subsets, so

```text
c(n)
 = sum_(S subseteq {1,...,m}) (-1)^(m-|S|) tau(n_S)
 = sum_(S subseteq {1,...,m}) (-1)^(m-|S|)
     (-1)^((AND_(i in S) P_i) XOR K(S)).
```

Thus the top Moebius mixed difference is exactly a signed sum over the complete
carry-parity field on the prime-divisor Boolean cube.

This is an arithmetic representation. It does not define physical curvature,
entanglement, vacuum, matter, or an interaction tensor.

## Field 2: code

Accepted verifier:

```text
probes/P-TM-MULTIPLICATION-CARRY-DEFECT-1/verify.py
```

The verifier is Python standard library only. It uses exact nonnegative
integers, bit operations, and finite exact enumeration. It contains no float,
complex approximation, tolerance, randomness, external data, web access, or
prior transcript.

The verifier audits finite instances of S1 through S5. The all-integer,
all-prime, and all-squarefree theorem scopes are carried by the written proofs
above, not by bounded enumeration.

## Field 3: carrier or data

Carrier only. No external data.

```text
positive integers with their unique binary expansions;
ordinary integer multiplication;
Moebius function and Dirichlet convolution on positive integers;
finite exact audit ranges generated internally by verify.py.
```

No measured data, zeta-zero data, imported sequence file, or prior probe output
is admissible.

## Field 4: systematics and completeness

There is no measurement systematic.

Completeness obligations are frozen:

```text
C1  S1 proves the carry identity from the exact column recurrence and also
    proves normalization-order independence for unit carry moves.
C2  S2 is a modulo-two consequence of S1 plus one complete Boolean identity.
C3  S3 exhausts all eight abstract (P,Q,K) states; the prime sweep is audit only.
C4  S4 is an exact two-term Moebius-convolution identity plus S2 at a=b.
C5  S5 expands every divisor of a squarefree integer as one subset of the
    complete prime set and substitutes the exact multi-product carry parity.
C6  The distinction from CARRY-PENTAD, issue 316, issue 317, and the
    chronological carry cocycle of RAMIFIED-TM-LIFT is preserved.
C7  No clause imports MOBIUS-TM-PRIME2-BRIDGE as a premise; the two proposed
    v41 theorems are logically standalone siblings.
```

Any hidden input, external data, floating tolerance, imported result, changed
carry definition, post-pin scope change, or unnamed layer lift is STOP.

## Field 5: failure threshold and scientific routing

No tolerance exists.

```text
CARRY-PASS
  Every frozen exact audit gate passes and no written proof defect is found.

MISMATCH
  One exact counterexample to S1 through S5, or one audit mismatch, falsifies
  the affected clause. The exact witness is printed and preserved.

STOP
  Authority, collision, pin, verifier integrity, completeness, security,
  transcript, or layer discipline fails.
```

`CARRY-PASS` and `MISMATCH` are scientific outcomes and exit zero. `STOP` is an
integrity outcome and exits nonzero. Scope and thresholds may not move after
the pin.

## Field 6: action layer

```text
L1 only: exact arithmetic of binary expansions, integer multiplication,
Moebius convolution, and Boolean parity.
```

No L1-to-L2/L3/L4/L5/L6 lift is attempted or owned.

## Scope firewall

This probe does not:

- assert RH, a zeta-zero location, Nyman-Beurling, or Baez-Duarte;
- analytically continue any series;
- couple the theorem to J, select p=5, or consume the conditional J note;
- identify `kappa_2` with the finite-vector-space carry forms of CARRY-PENTAD
  or issue 316;
- identify multiplication carry with the chronological carry cocycle in
  RAMIFIED-TM-LIFT;
- claim that `c=0` means no carries, trivial multiplication, vacuum, or no
  internal structure;
- claim that `c` is multiplicative;
- derive a decoder, Born rule, observer, force, spacetime, SI statement,
  matter/light assignment, entanglement, or physical interaction;
- lift anything to L2-L6.

Any later RH, Hilbert, J, or physical interpretation requires a separately
named claim and the appropriate layer gate.

## Formal sequence after the pin

1. Read back this file and `verify.py` from the public remote at the immutable
   pin; record commit, SHA-256, and byte counts on issue 331.
2. Only then execute the accepted verifier for the first formal run.
3. Commit exact `EXPECTED.txt`, neutral `RUN.md`, and `RESULT.md` without
   changing the pinned preregistration or verifier.
4. Open one pull request changing only
   `probes/P-TM-MULTIPLICATION-CARRY-DEFECT-1/`.
5. Require GitHub x86_64 and aarch64 jobs to reproduce the same committed
   `EXPECTED.txt` byte for byte.
6. Because `T` is sought by written proof, the two-architecture run is an audit
   of the accepted verifier, not the source of the universal quantifiers.
7. Any Canon/Registry fold is a later separate reviewed action.
