# C-COLLATZ-BLOCK-CARRY-PRIME-N

**NON-CANONICAL / L1. Author: A. M. Thorn.**

This research proposal formalizes exact initial blocks of the accelerated
Collatz map, their complete carry counts, and the information retained by an
output together with its division depth. It separates self-contained proofs
from finite computational audits. It is not a Canon promotion or a claim of
priority.

Reservation: [issue #1858](https://github.com/mathorn1973/twist-j/issues/1858).
Base: `0c33e2b281e39127c269ef5dd7f5b529a62e9e65` (Public Canon v107).

## Mathematical content

For positive odd integers, write

$$
v(n)=v_2(3n+1),\qquad T(n)=(3n+1)/2^{v(n)}.
$$

The proofs establish the following facts.

- The representations $n+1=2^k u$ and $n-1=2^r u$, with odd $u$,
  give complete initial blocks of valuations one and two, including their
  exact lengths and boundary steps. The two affine centers are $-1$ and $1$.
- Full propagated carries differ from initial overlapping ones. The corrected
  formulas include the boundary where a separating zero transmits a carry.
  The golden set consists of binary words without adjacent ones.
- A complete first Mersenne block, from $2^k-1$ through its boundary step,
  decreases its starting value exactly for $k=2,4,8$, equals it for $k=1$,
  and increases it for every other $k$. This classification has an elementary
  proof for all exponents.
- The exact witness $k=8$ produces the golden state $4373$ before the boundary
  step. It refutes an exhaustive last-state list containing only $1,2,3,5$.
- The output-depth pair reconstructs the input as $(2^v m-1)/3$.
  Complete output fibers are towers under $p\mapsto4p+1$, and the plus-one
  prefixes have an exact common-child relation with powers of three.
- Consecutive odd states are coprime. Every odd integer divides some one-step
  predecessor $(4^j-1)/3$ of one. Neither statement asserts convergence.
- A cycle must satisfy the full affine equation
  $(2^K-3^L)n_0=C$, including its offset and actual valuation itinerary.

The elementary carry identities are consistent with the existing
`TM-MULTIPLICATION-CARRY-DEFECT` claim. This note does not rename or alter that
claim or the separate cyclotomic $J/\lambda$ carry proposals.

## Evidence and reproduction

| File | Role |
| --- | --- |
| [PROOF.md](PROOF.md) | Self-contained proofs and explicit limits |
| [REPLAY-SPEC.md](REPLAY-SPEC.md) | Fixed finite domains and result-exposed execution contract |
| [verify.py](verify.py) | Deterministic standard-library integer verifier |
| [EXPECTED.txt](EXPECTED.txt) | Exact stdout retained from the first execution |
| [RUN.md](RUN.md) | Neutral environment, source pin, hashes, and execution result |
| [SHA256SUMS](SHA256SUMS) | File custody manifest, excluding itself |

The results were known before this integrated verifier was written. The public
source pin precedes its first execution, but does not retroactively make the
work a blind preregistration. The first execution at
[`3c75ff72c452692747836f374ed0babcc1b9abb7`](https://github.com/mathorn1973/twist-j/commit/3c75ff72c452692747836f374ed0babcc1b9abb7)
passed on Linux x86_64 with Python 3.13.5, exit zero and empty stderr.
Its actual 1,075-byte stdout and neutral run record were appended after that
pin. Source and scope changes require a new pin.

From the repository root, using Python 3.12 or later with assertions enabled:

```sh
python3 -I notes/C-COLLATZ-BLOCK-CARRY-PRIME-N/verify.py
```

The verifier uses only exact integers and has no input files, network access,
randomness, floating arithmetic, or file writes. Its stdout contains no host,
path, timestamp, or environment data. The fixed audit includes exponents
$0\le m\le100000$; a passing finite search does not establish a global
classification of golden powers or their transformed words.

Repository CI checks policy and integrity on its required architectures.
Its `probes/` and `reproduce/` selectors do **not** execute this `notes/`
verifier. A passing repository check is therefore not a two-architecture
scientific replay of this note. Each separately performed execution must be
identified by its actual environment and exact output.

## Status boundary

The proof statements are L1 candidate-T material awaiting review; the finite
inventory is candidate-C evidence over its declared domains. This note makes
no universal Collatz convergence claim, no global classification of golden
exponents, no new cycle-length bound, no physical claim, and no cross-layer
inference. The conjectural golden-power statement is explicitly left unproved.

The proposal changes only this notes directory. Any later Canon inclusion or
formal probe would require its own review under the repository policy.
