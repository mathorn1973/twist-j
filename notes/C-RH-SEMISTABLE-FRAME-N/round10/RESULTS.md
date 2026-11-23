# Round 10 first-run results

**NON-CANONICAL. No authority. Status: candidate-C within the fixed finite domains.**

Both separately authored programs passed their first scientific execution.
Every preregistered assertion and count passed, both exits were zero, both
stderr files are empty, and neither run timed out. There was no scientific
retry, repaired run, changed threshold or edited frozen program.

## Exact finite coverage

| Part | Fixed domain | Both programs |
|---|---|---|
| A: compact word-prime cosets | 62 elements; 920 ordered pairs, including 62 diagonal and 858 off-diagonal | Pass |
| B: full ambient lattice neighbors | 290 neighbors; 21,614 ordered pairs, including 290 diagonal and 21,324 off-diagonal | Pass |
| C: rational two-eigenvalue Gram matrices | 7 parameter triples times 5 rational parameters, 35 cases | Pass |
| D: finite compact representation characters | 20,292 candidate matrices; 11,454 invertible matrices in four groups | Pass |
| E: stabilizer character obstruction | Every nonzero proper subspace in F_2^4, F_3^4 and F_2^5: 65 + 210 + 372 = 647 | Pass |

The seven triples in A-C are exactly (2,2,3), (2,2,5), (3,2,3),
(3,2,5), (2,3,4), (2,3,6), (3,3,4). The Gram parameter is in
{0, 1/4, 1/2, 3/4, 1}. Its value is not asserted to be a realizable
spherical Hecke parameter in every case.

In D the group orders are 6, 168, 48 and 11,232. The respective
irreducible-sector dimensions tested by exact character inner products
are (1,2), (1,6), (1,3,4) and (1,12,13). These character calculations
are over characteristic zero, using integer-valued functions on the
finite groups; they do not assume semisimplicity over their residue fields.

In E the two terminal character coefficients have nonzero product in
the finite field. This is an algebraic model of the trace-annihilator
argument, not reduction of the actual character modulo its word prime.
In the actual local field the incoming coefficient has valuation one
but is nonzero.

## Independent implementations of the fixed contract

The development program uses rational matrix inversion and finite-field
linear elimination, a complete exact eigenspace certificate in C, fixed
space dimensions in D, and canonical reduced-row-echelon subspaces with
linear constraint ranks in E.

The blind opponent uses explicit structured inverses and exact minor
tests in A, scaled integral inverse products in B, exact Gaussian rank
in C, direct vector permutations for the character counts in D, and
separately enumerated spans with explicit stabilizer witnesses in E.
Both programs are standalone standard-library Python. Their authoring
lanes did not read one another's implementation or output before freezing.

This is separate blind code authorship within one coordinated session.
It is not an external independent review and not two-architecture
validation. Different stdout formats are retained; both agree on all
mathematical counts and assertions.

## Immutable evidence

Contract public pin:
[4c3ff7a6c3003b8c102ce44eac6e1891b5a8c728](https://github.com/mathorn1973/twist-j/commit/4c3ff7a6c3003b8c102ce44eac6e1891b5a8c728).

Execution public pin:
[e4b7ee04b10e227fa7362b6578c9046dd1613b22](https://github.com/mathorn1973/twist-j/commit/e4b7ee04b10e227fa7362b6578c9046dd1613b22).

The contract and both code files were read back byte-for-byte at that
execution pin before either scientific run. Both executions used separate
clean detached worktrees, remained clean afterwards, and used the
repository root as working directory.

| File | Bytes | SHA-256 |
|---|---:|---|
| PREREG.md | 8966 | 7f8190d05f4269f8c9d43c6138a1812a5b82b1fae6a742f9ff777b67b3f8b5c9 |
| verify_r10.py | 15778 | 4dd909dfcd5dbe7715a1c20e0b49a7e57873248f894b371e771643870eb87dbe |
| break_r10.py | 17805 | 4506a754044c81234e4ddd732d95bc326494d2068419b8aa91cff6e759ce6353 |
| verify.stdout.txt | 226 | b1e9a39607a644c53ab2e7ba0bce109d66a7d061ea334196bbb9778f6bba1ce3 |
| break.stdout.txt | 571 | 2e4b75377002bb477110be90256e6b1b0f92dedcf3721c8ca5a9039b69488605 |
| verify.stderr.txt | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |
| break.stderr.txt | 0 | e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855 |

Both programs ran on x86_64, Debian GNU/Linux 13 (trixie), Python 3.12.14.
The environment fixed PYTHONHASHSEED=0, LC_ALL=C.UTF-8 and
PYTHONDONTWRITEBYTECODE=1. The preregistered wall limit was 240 seconds.

| Run | Start, UTC | Elapsed nanoseconds | Exit | Timeout |
|---|---|---:|---:|---|
| Development | 2026-11-23T20:14:09.530391+00:00 | 752608721 | 0 | No |
| Blind opponent | 2026-11-23T20:14:09.550086+00:00 | 867523529 | 0 | No |

The raw [development stdout](verify.stdout.txt),
[opposition stdout](break.stdout.txt),
[development receipt](verify.run.json) and
[opposition receipt](break.run.json) preserve the actual first runs.
Their outputs have not been normalized or rewritten. Any future execution
is reproduction of this frozen audit, not another first run.

## What these checks establish

Candidate-C: the finite algebraic statements in PREREG.md hold on exactly
the fixed exhaustive domains above. They support the hand derivations of
the compact coset geometry, its Gram decomposition, the compact character
inventory and the stabilizer obstruction.

The general source-counting theorem, the complete Fourier rank identity,
the local twisted-Jacquet argument and the absolute global unfolding
bridge remain paper deductions, candidate-D with the hypotheses in
PROOF.md. The finite success does not prove those infinite or global
statements.

No actual automorphic row, selected Bessel period, L-value, actual P_u
matrix or global concentration defect was computed. The exponential
intrinsic period-rank improvement remains open. No RH conclusion, Lean
verification, public computation-grade status or Canon change follows
from these runs.
