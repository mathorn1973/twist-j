# Preparation status and execution boundary

Candidate: C-INTEGRAL-GRAM-CONTACT-ARCHIVE-N.
Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.
Status: NON-CANONICAL / L1 / PREPARATION_ONLY, 2026-10-31.
Reservation: [#1844](https://github.com/mathorn1973/twist-j/issues/1844).

## Actual state

The self-contained analytical argument and two independently structured
finite-audit implementations are prepared. Neither scientific program has
been executed or imported. No certificate output, scientific PASS, completed
run, public computation gate, accepted theorem or Canon promotion is claimed.
Consequently there is no EXPECTED.txt, RUN.md or RESULT.md.

The public basis is a193e389fb1ddb0bdc89165b015c95a17eb1e425,
Public Canon v106. The local preparation branch is
`notes/c-integral-gram-contact-archive-n`. Its source commits are:

| Local preparation commit | Content |
| --- | --- |
| c6e7eaef4741d7ec36bfb2e96d0e5831ea9295be | Preregistration, builder source, analytical proof, references, overview and promotion boundary |
| 4d14f9fab8c0baae6c2e808c43b28f08a9d72926 | Independent breaker; formatting-only proof/reference corrections |

These are local preparation revisions. They are not a public preregistration
pin and are not represented as commits already available on GitHub.
Both use the prescribed author and committer identity.

| Frozen scientific input or code | SHA-256 |
| --- | --- |
| PREREG.md | 067115f7b1df57cf8475eceb3bbca7d4eb2b97ec940b6a2fe4798c5b520074a2 |
| verify.py | 71f0cd9f73cf6a1ae0cded830e575e043d8f70b9b065be806f7617929dd8e3e3 |
| break.py | a4f86eef9e3440c368f82a560bcad2bf762ac953c55d0fbf045a4b56cb987b42 |

## Implementation provenance and review

The builder represents elements in the fixed four-coefficient basis and
uses a sparse left-then-right Gram update with exact divisions.
The separate breaker received only the byte-identical PREREG.md from the
first local preparation commit. It did not inspect the builder source,
PROOF.md, other scientific sources or any computed output. It uses
variable-length polynomial convolution and general monic reduction modulo
Phi5, and a separately formed integer sandwich B*G*B^dagger/4, B=2A.
Every coefficient division is exact or becomes an integrity failure.

The breaker and its static reviewer addressed only the frozen inventory.
The breaker records its explicit interpretation of unqualified C as the
positive exponent, derives J's inverse by rational elimination, counts zero
VALID cases and boundaries separately, and also checks the negative contact
exponent. Its old-memory checks cover ticks 4 through 8. These do not change
the preregistered fixtures or certificate streams.

An authored static review of the analytical proof found no substantive
defect in A-D, including nonintegral norm-one fibres, refused branches and
the all-starting-clock return theorem. It had prior exposure to the argument
and is not independent theorem acceptance. Static review of both code paths
found no further concrete defect. Syntax-only compilation of both programs
succeeded using compile(source, filename, "exec"); it did not execute the
compiled code. Repository policy and whitespace checks are preparation
checks, not scientific evidence.

The semantic boundary is unchanged: on dirty inputs, VALID reports the
defined clock window only. It does not certify correct preparation or an
actual writing event. The prepared example has three read boundaries 6,7,8,
separated by two hold steps. It supplies finite-window retention.

## Public source pin and execution

On 2026-10-31 the author explicitly authorized the connected GitHub account's
default commit identity for publication of this candidate. This is the
author-approved exception permitted by AGENTS.md. Source-file authorship
remains A. M. Thorn. The three scientific input/code hashes above are unchanged.

The first public source commit will contain the complete preregistration,
proof and both implementations before either scientific run. Read back
their exact bytes and record the actual public commit and hashes before
execution. Local preparation commits alone do not satisfy this requirement.
Then run the two fixed sources, preserve actual stdout, stderr and exit
status, and compare the pair and program certificates. Record failures
without changing thresholds or retroactively modifying a pinned source.
Only actual completed runs can supply RUN.md, RESULT.md and expected stdout.
Architecture replay, independent mathematical acceptance and any future
promotion remain separately scoped obligations.
