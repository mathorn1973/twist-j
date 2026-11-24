# Authority, ownership and sources

NON-CANONICAL. This manifest records the basis of the incubation; it
confers no scientific status.

## Public authority

The selected line is PUBLIC. The authoritative repository is
[mathorn1973/twist-j](https://github.com/mathorn1973/twist-j).
The basis is main at
26bd3b935272ac6ff35591f50be616473a54ef7a, Public Canon v116.
The head was read again after drafting and was unchanged.

STATUS.md was read first, followed by POLICY.md and AGENTS.md.
CORE, FRONTIER, relevant registry rows, source proofs and evidence paths
were read at the same pinned content. Declared tag/content ancestry,
all five normative hashes and the exact-main workflow were verified.
Workflow run 45358869683 records the x86_64 and aarch64 checks and the
aggregate check. This authority readback is not a new scientific replay.

Normative SHA-256 values at this basis:

| File | SHA-256 |
| --- | --- |
| CANON.md | ea4f924dc02838fcfe47d9b983bc0be929da7378ee9278c48831f34a5c393695 |
| CORE.md | f41407b96706513e772a09660b746e0cd0e5574e796f291698c9eccf66ddaa32 |
| FRONTIER.md | 2720c8032a31a4a0c3a704b00ca462f6e5faad6696958c0e4e03e3b7b74658cd |
| REGISTRY.tsv | 740774deb54a761b459a3dd09fd287646386f197adceada7f2194adab56ee058 |
| CHANGELOG.md | 2e03900a71752a782586982d78b548556a8a7fffb7dc66fb331ee2b5f9c69266 |

Uploaded snapshots and conversation notes are references, not public
authority. The source note supplied by the owner introduced the defect
and the reduced character interpretation; those contributions are
credited as the starting point.

## Existing canonical ownership

All paths in this table refer to the pinned public basis.
The registry, not an older proposed status in a probe result, determines
the current public status.

| Existing item | Status used | Exact input used here |
| --- | --- | --- |
| J-BINARY-NORM-INDEX | T | O/(2)=F16, J has order fifteen; binary norm-index scope only |
| RECORD-QUOTIENT-CALCULUS and the inline unit-decomposition synthesis | T premises | The reduced product F16 x F5 and its C60 unit carrier |
| C20-TEICHMULLER-SPLIT | T | O/(5)=F5[lambda]/lambda^4 and J of order twenty |
| J-RESIDUE-PERIOD | T | Residue periods of j, phi and J at rational moduli, within its rational-modulus scope |
| RAMIFIED-TM-LIFT | T | Theta_n=2^{s_2(n)} mod5 and its binary sign quotient |
| CARRY-J-CHECKPOINT | T | psi_4=psi_6 for every origin-zero seed, despite different lifted phases |
| KERNEL-Z6-SYNCHRONIZATION, S1 | T | Every initial sheet maps bijectively to X_(4+2 theta_(n-1)) for n>=3 |
| U-FINITE-HISTORY-CLOCK-PHASE | T | A sufficient fixed history for every fixed dyadic phase, with its endpoint correction and buffer scope |
| COMPLETE-STATE-OBSERVATION-CONTRACT | T | Exact factorization through declared observation fibres |
| READING-SPLIT | D | The existing partial reading split, not global decoder completeness |

Primary repository locations:

- [Registry](https://github.com/mathorn1973/twist-j/blob/26bd3b935272ac6ff35591f50be616473a54ef7a/canon/REGISTRY.tsv),
  especially rows 19, 66, 203, 296-298, 306, 389, 391 and 624.
- [Canonical synchronization proof and inline two-place synthesis](https://github.com/mathorn1973/twist-j/blob/26bd3b935272ac6ff35591f50be616473a54ef7a/canon/CANON.md):
  KERNEL-Z6-SYNCHRONIZATION around lines 18039-18115;
  the unit decomposition and two-place C60 synthesis around 19958-20049.
- [Native selector and same-seed collision](https://github.com/mathorn1973/twist-j/blob/26bd3b935272ac6ff35591f50be616473a54ef7a/probes/P-CARRY-J-CHECKPOINT-1/PREREG.md).
- [Synchronization evidence](https://github.com/mathorn1973/twist-j/blob/26bd3b935272ac6ff35591f50be616473a54ef7a/probes/P-KERNEL-Z6-SYNCHRONIZATION-1/RESULT.md).
- [Finite-history evidence](https://github.com/mathorn1973/twist-j/blob/26bd3b935272ac6ff35591f50be616473a54ef7a/probes/P-U-FINITE-HISTORY-EVENT-1/RESULT.md).
- [Boolean carry and J orbit note, section 14](https://github.com/mathorn1973/twist-j/blob/26bd3b935272ac6ff35591f50be616473a54ef7a/notes/C-BOOLEAN-CARRY-J-ORBIT-1.md):
  original noncanonical synthesis of the inherited two-place identities.

No existing claim is re-registered, no sealed probe is reopened, and no
inheritance is extended to a physical decoder or a higher layer.

## Classical literature

The abstract closure of automatic sequences under fixed finite-state
transductions is classical. The proof in DECODER.md is a self-contained
specialization to the declared native update. The no-primes result is
also classical; its short finite-automaton proof is included there.

- Juris Hartmanis and H. Shank, *On the Recognition of Primes by Automata*,
  Cornell technical report, February 1968:
  [primary repository record](https://ecommons.cornell.edu/entities/publication/a065595f-9181-4c54-833f-dd743aff69e3).
  Its abstract explicitly states the exclusion of every infinite prime
  subset for finite automata. The record was read; direct retrieval of
  its PDF returned HTTP 405 in this session. The proof here does not
  depend on an unread passage of that PDF.
- Alan Cobham, *Uniform tag sequences*, Mathematical Systems Theory 6
  (1972), 164-192:
  [DOI](https://doi.org/10.1007/BF01706087).
  This is historical attribution for the transduction closure theorem.
- Jeffrey Shallit and Anatoly Zavyalov, *Transduction of Automatic
  Sequences and Applications*:
  [arXiv:2303.15203](https://arxiv.org/abs/2303.15203).
- Jason P. Bell and Jeffrey Shallit, *Automatic sequences of rank two*,
  RAIRO-Theoretical Informatics and Applications 56 (2022), article 7:
  [primary open article](https://www.numdam.org/item/10.1051/ita/2022006.pdf),
  Lemma 6.2, for the state-stream use of finite transduction.
- Jon Grantham, *Frobenius Pseudoprimes*, Mathematics of Computation 70
  (2001), 873-891:
  [author's arXiv record](https://arxiv.org/abs/1903.06820),
  [DOI](https://doi.org/10.1090/S0025-5718-00-01197-2).
  It supplies the classical context for polynomial and recurrence-based
  probable-prime tests. The explicit universal counterexample and
  criteria in OBSTRUCTIONS.md are proved in this bundle.

No external implementation or dataset is incorporated. Mathematical
arguments are written out here; literature links provide attribution and
context, not substituted evidence for an unstated theorem.

## Collision search

The exact new identifier was absent from issue and local source search.
Relevant issues/PRs, current remote heads and notes/probes/registry were
inspected. The following ownership is preserved:

- #2077 and draft #2078: scale-character arithmetic, separately frozen.
- #2070 and draft #2071: RH concentration and period-map work.
- The existing Boolean-carry, binary-norm, ramified-split, source-phase
  and native finite-history lanes.

This bundle studies the single defect reading and its observation
boundary. It does not import its results into any of those lanes.
