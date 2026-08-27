# P-O5-EULER-INCIDENCE-TRIANGLE-NOGO-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / UNRUN / CANON UNCHANGED**

```text
issue:          #597
branch:         probe/P-O5-EULER-INCIDENCE-TRIANGLE-NOGO-1
path:           probes/P-O5-EULER-INCIDENCE-TRIANGLE-NOGO-1/
basis main:     b66ea7eda80e0028c74c7b71b70205db9566c37b
canon:          Public Canon v67, tag canon-v67
CONTENT_COMMIT: f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:   b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:    351502
action layer:   NOT_APPLICABLE
layer lift:     none
authority:      none before a later sealed fold
```

The v67 activation and content commits are ancestors of the basis.

## Predecessor

This fresh successor names consumed probe
`P-O5-ORIENTED-EULER-MORSE-BOUNDARY-1`, proposed row
`O5-ORIENTED-EULER-MORSE-BOUNDARY`, issue #594, pin
`4726319ddc8c4acbe5267badb39b0761554aa086`, terminal commit
`17d6e71f85e505af62389ef4c256a71cf886bf42`, and merged abandonment PR #596.
The predecessor stopped before preflight on a PREREG blob mismatch and earned
no scientific result. No equation, witness, threshold, carrier, or breaker is
changed here.

## Frozen candidate

```text
O5-EULER-INCIDENCE-TRIANGLE-NOGO [candidate-T]
```

For `N>=1`, let `K_5(N)` have vertices `(p,+),(p,-)` for rational split primes
`p<=N`. A face contains at most one orientation above each `p` and the product
of its underlying primes is at most `N`. The empty face has product one. Put

```text
s_5(n)=(-2)^omega(n)
```

on squarefree integers supported only on split primes, zero otherwise, and
`S_5^sum(N)=sum_(n<=N)s_5(n)`.

The frozen theorem package is:

```text
1. K_5(N) is a finite simplicial complex.
2. S_5^sum(N)=-reduced_Euler_characteristic(K_5(N)).
3. Every split p with 11p>N gives two isolated vertices.
4. If I_5(N)=#{split p<=N:11p>N}, every one-vertex-incidence matching
   leaves at least max(0,2I_5(N)-1) unmatched faces when the empty face
   may be used, and at least 2I_5(N) when it may not.
5. Therefore cancellation of matched opposite-parity faces followed only by
   the unmatched-face triangle count cannot prove the all-epsilon square-root
   bound. Classical PNT in classes 1 and 4 modulo 5 gives I_5(N) of order
   N/log N.
```

Statements 1-4 are exact. Statement 5 is `candidate-T on [T-lit] PNT-AP`.
This is only a no-go for that triangle-count endpoint. Signed critical-cell,
Morse-boundary, homological, weighted, nonlocal, growing-mode, and spectral
cancellation remain open.

## Proof

Split primes are congruent to 1 or 4 modulo 5; the smallest is 11. If `F` is a
face, every subset has a prime product dividing that of `F`, proving downward
closure.

A squarefree split integer with `k` prime factors has exactly `2^k` oriented
faces of cardinality `k`, and every such face has one such support. With
`f_(-1)=1`,

```text
f_(k-1)(N)=sum_(n<=N, squarefree split, omega(n)=k)2^k,
S_5^sum(N)=sum_(k>=0)(-1)^k f_(k-1)(N)
          =-reduced_Euler_characteristic(K_5(N)).
```

If `11p>N`, every distinct split `q` satisfies `q>=11`, hence `pq>N`; both
vertices above `p` are isolated. Strictness matters: for `N=209=11*19`,
`{11,19}` is a valid support.

An isolated vertex has no two-face coface. In the augmented incidence poset its
only possible partner is the empty face, which a matching uses at most once.
The two unmatched-face floors follow. Acyclic Morse matchings are a subclass.
Matched opposite-parity faces cancel in the augmented Euler sum. A final bound
using only the number of unmatched faces cannot beat the isolated-vertex
floor. PNT-AP gives order `N/log N`, which is not
`O(N^(1/2+epsilon))` for fixed `epsilon<1/2`. This is not a lower bound for the
signed sum.

## Frozen contract

```text
EQUATION:   the five statements above.
CODE:       verify.py; stdlib, exact integers, deterministic faces and exact
            finite bipartite matching; no floats, network, random, zero data.
CARRIER:    chi_5 split primes, two formal orientations, finite faces,
            augmented parity, one-vertex incidence.
SYSTEMATICS: unordered orientation pair; at most one per valid face; empty
             face included and usable at most once.
THRESHOLD:  G01-G08 pass; B1-B5 first fire at 11,121,2,(209,19),1; one LF
            EXPECTED.txt, exit zero, empty stderr, byte identity.
LAYER:      NOT_APPLICABLE; no L1-L6, physical, decoder, probability, or SI.
```

Falsifiers are an exact failure of downward closure, Euler identity, strict
isolation, matching floor, or PNT consequence, or an orientation selection,
inert/ramified contamination, target import, or scope widening. Integrity
mismatch, stale basis, changed pin, failed preflight, process or architecture
failure is STOP, not a scientific counterexample.

Negative controls:

```text
B1 one orientation only: N=11.
B2 allow both conjugate orientations: N=121.
B3 inert 2 as split: N=2.
B4 replace 11p>N by 11p>=N: N=209,p=19.
B5 drop the empty face: N=1.
```

Verifier gates are the split census, simplicial faces, Euler identity,
dimension counts, strict isolation, exact maximum matching floors, all five
breakers, and a stdlib exact-integer source firewall.

## Pin and run discipline

Before the pin, server blobs for `PREREG.md` and `verify.py` must equal local
`git hash-object` identities. Then one commit containing exactly those files is
pushed and read back. Only after exact readback run the clean preflight

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
```

and, if it passes with empty stderr, the single scientific command

```text
env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 probes/P-O5-EULER-INCIDENCE-TRIANGLE-NOGO-1/verify.py
```

No RH, GRH, continuation, zero, cancellation estimate, Hecke/automorphic,
orientation selector, physics, or L1-L6 claim is made. The candidate probes
#592 and #593 and draft Notes PR #595 are not evidence inputs.
