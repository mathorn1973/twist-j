# P-BINARY-RECORD-QUADRATIC-SELECTION-1 preregistration

**FORMAL PREREGISTRATION / PROOF-FIRST / RESULT-EXPOSED.**
Author: A. M. Thorn. Date: 2026-09-07.
Public lock: [#885](https://github.com/mathorn1973/twist-j/issues/885).
Branch: `probe/P-BINARY-RECORD-QUADRATIC-SELECTION-1`.

## Authority and exposure

Basis: ACTIVE Public Canon v80, public main and tag
`4577448dba85c492b27773a64e5fd557abc02b30`; content
`b00171ef21ecb0d905593224f66f5e8a0f6c28e5`; Canon SHA-256
`8b076ee3d940e4a3639d3ffca06ae86e7df69dfc87f90d06ea99d4f9fca6b66c`,
541516 bytes. Required main, tag and release checks were green at claim time.
Remote heads, open PRs, issues and the probe/Registry namespace were scanned.
The identifier is fresh. Draft #884 is the motivating NON-CANONICAL program;
#812 concerns a distinct signed-incidence model and #539 the physical schema.

The elementary counterexamples and candidate proofs in PROOF.md were known
before this pin. This is an explicitly result-exposed theorem audit, not blind
discovery or empirical evidence. Commit and push PREREG.md, PROOF.md and the
accepted verify.py together; read their bytes back from that public commit
before the first formal execution. No verifier has been executed for this
identifier before the pin. Static syntax checks are permitted. After pinning,
do not amend, rebase, squash, rename, reuse or force-push the probe.

## Field 1: equations, targets and falsifiers

The full definitions and all-domain proofs are in PROOF.md, frozen with this
file. The targets are:

1. For every finite X, d=|X| and k>=1, simultaneous permutation orbits on X^k
   are exactly the equality partitions pi with b(pi)<=d, of size (d)_(b(pi)).
   All invariant supports are orbit unions. Every nonnegative integer atomic
   valuation stable under all injections has fixed coefficients c_pi>=0 and
   W_k(d)=sum_pi c_pi(d)_(b(pi)), and conversely. For a nonzero valuation its
   degree is the largest occupied block count. Full incidence gives d^k.
2. At k=2 the complete valuation class is W_2(d)=a*d+b*d*(d-1), a,b>=0.
   For all d>=0, W_2(d)=c*d^2 iff a=b=c. Independent relabeling of *unmarked*
   nonempty carriers has one orbit on their Cartesian product, whereas a
   marked matching retains diagonal and off-diagonal orbits.
3. For source s in S and record r in B={blank} disjoint-union S, the controlled
   transposition T(s,r)=(s,tau_s(r)) is a total involutive bijection, faithfully
   writes s to a blank cell, commutes with simultaneous relabeling, preserves
   the source and any other cells, and produces active graph cardinality d.
   Any finite sequence on fresh addressed cells preserves the older cells
   and has the reversed composition as inverse. For d=2, d differs from d^2.
4. On z in Z^4 and every integer p>=1, A_p=|sum z|^p and
   B_p=5*sum_(i<j)|z_i-z_j|^p give nonnegative integer weights, the stated
   LOW/HIGH/total zero classes, normalized rational ratios off zero,
   coordinate-permutation and global-sign invariance, degree-p homogeneity
   and nonzero-integer-scale-invariant normalized readings. At (1,1,0,0),
   LOW=2^p/(2^p+20); hence all p give distinct readings. p=1 gives 1/11 and
   p=2 gives 1/6. p=2 agrees with the adopted v80 quadratic channel formula.
5. Every nonnegative separately additive real-valued pairing on two abelian
   groups is zero. Nonzero signed bilinear forms and positive quadratic
   diagonals are outside the nonnegative-off-diagonal premise.

Exact admitted counterexamples to any target falsify that target. The
exhibited d versus d^2 and 1/11 versus 1/6 witnesses refute the stronger
quadratic-selection implications under the enumerated structural/scalar
premises, not the targets above. Physical admissibility is not tested.

## Field 2: accepted verifier and finite audit

Command from repository root:

```text
python3 probes/P-BINARY-RECORD-QUADRATIC-SELECTION-1/verify.py
```

The Python standard-library verifier uses integers and Fraction only. It
reads no repository files, external data, network, randomness or clocks.
Its accepted source is the verify.py committed in this pin.

Frozen finite domains:

- All tuples for k=1..4 and d=0..5; equality-pattern inventories and orbit
  sizes; adjacent label-transposition controls, shifted injections, full
  product identity and direct weighted sums with coefficients indexed by the
  lexicographically sorted partitions on k labels.
- Every binary subset on d=0..3 under simultaneous label permutations, and
  every subset of S x T for |S|,|T|=0..3 under independent permutations.
  Invariance is tested with adjacent-transposition generators; the generated
  groups are the full symmetric groups.
- a,b,c=0..4 and d=0..8 for the binary weight formula and square criterion;
  the strictly positive a=1,b=2 witness; triple supports for d=0..5.
- Every source/cell state for d=1..5 and every permutation of its labels;
  every two-cell tape and chosen address; every three-symbol input word on
  fresh cells and its reverse execution. Blank is represented by integer -1,
  outside the nonnegative symbol range.
- All 625 z in {-2,-1,0,1,2}^4, p=1..4, all 24 coordinate permutations and
  integer scalings -2,-1,0,1,2. The witness (1,1,0,0) is also checked at
  p=1..8. The zero case has no ratio. The universal claims rely on PROOF.md,
  not extrapolation from these finite samples.
- All 81 two-by-two matrices with coefficients in {-1,0,1}, evaluated on all
  signs of every basis pair; the only nonnegative survivor must be zero.
  Raw (+1,-1) pair count 4 versus reduced square 0 is an explicit control.

## Field 3: carrier and data

Mathematical carriers are finite equality-only sets and their products,
permutations/injections, nonnegative integer atomic weights, pointed finite
record cells and finite tapes, Z^4 sources, positive integer powers, rational
normalized pairs, and abelian groups for the written obstruction theorem.
There is no experimental dataset or fitted parameter. The coefficient 5 and
the native source channel forms are inherited *adopted* v80 choices; they
are not outputs of a new physical-selection proof. Comparison of powers is
declared in advance and supplies no replacement physical reading.

## Field 4: systematics and controls

Run in Linux or a Linux-compatible environment with
LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1.
Standard-library Python >=3.10 is sufficient for the accepted code; repository
CI uses Python 3.12. The local run record must state the actual interpreter.
Use a 600-second ceiling, require exit 0, empty stderr and deterministic exact
UTF-8 stdout. Counts depend only on fixed loops and integer comparisons.

Systematics include empty carriers, d=1 orbit collapse, blank versus active
record symbols, order-sensitive tuple positions, separate versus simultaneous
relabeling, explicit fresh-cell resources, stable versus size-dependent
weights, raw versus reduced signed fibres, and zero versus normalized support.
No post-hoc target-based exclusion of p=1 or a!=b is allowed.

## Field 5: threshold and disposition

Mismatch threshold is zero. Preserve exact counterexamples and distinguish
them from execution or custody failures. Timeout, pin mismatch, nonzero exit
without a completed result, source defect or platform-dependent bytes are
integrity STOP; they do not themselves falsify a mathematical theorem.
No failed identifier is repaired by changing the pinned verifier.

After the first completed execution add EXPECTED.txt, RUN.md and RESULT.md.
Both required GitHub architectures must reproduce the same pinned verifier
with exit 0, empty stderr and stdout byte-identical to EXPECTED.txt. The proof
is the all-domain mathematical argument; the verifier audits its frozen
consequences. No status promotion follows from a passing software check alone.

## Field 6: action layer and nonclaims

Action layer: **L1 exact mathematics and symbolic model only**. The references
to a writer mean finite reversible functions, not an L4/L5 physical apparatus.
No physical source map, effect, post-state law, preparation, native-U embedding,
record persistence mechanism, physical reset, realized event, onset law,
ensemble, sampling law or L6 measure is claimed. No cross-layer gate is run.

The native power family satisfies only the scalar laws listed above. It is not
claimed to satisfy full rational-frame additivity, the QDD density/record
contract, or any complete physical instrument class. The equality-pattern
census exhausts only equality-only structures; it is not an exhaustive census
of TWIST-J native invariants.

The result cannot falsify Born's empirical rule, v80's simplex theorem or the
physical QDD obligations. Those remain separate, and absent physical premises
remain STOP. No Canon, Registry, frontier, dependency or gate file is changed.
