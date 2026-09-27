# RUN — C-CURRENT-PRIME-GATE-N

**Status:** candidate-C audit only. This is not a formal public probe and not a two-architecture scientific gate.

## Frozen source

- branch: \`notes/current-prime-gate-20260927\`
- preregistration commit: \`a83d6bbace35990875a05544c913e789ac1816cf\`
- audited head: \`1de2eb03b947bc56d101cc9cef30ca86a14b926b\`
- verifier SHA-256: \`effb7f0f8d10f4e81a2cba91fec3df7be939f3744d19d1c62143bd3b0a34df34\`

The verifier was committed and read back from GitHub before execution.

## Clean-clone run

Neutral public descriptor:

\`\`\`text
architecture: aarch64
python: Python 3.11.2
head: 1de2eb03b947bc56d101cc9cef30ca86a14b926b
exit_code: 0
stdout_bytes: 429
stderr_bytes: 0
\`\`\`

Exact stdout:

\`\`\`text
PASS G1/G2: D=4 has six incident plaquettes per edge; odd-prime unit-current window is exactly {5}.
             p=3 alphabet = {-2,-1,0,1,2}; p=5 alphabet = {-1,0,1}; p>=7 alphabet = {0}.
PASS G3/G4 audit: Dsep=3..12 explicit p=5 family is ternary, |supp n_D|=4Dsep+40, and carries two edge-disjoint unit 4-cycles.
PASS boundary check: every audited j_D is exactly conserved.
ALL PASS: current prime-gate finite audit complete.
\`\`\`

A second clean-clone ARM run on a different connected host returned the same 429 stdout bytes with empty stderr. That is same-architecture reproduction only, not the repository two-architecture scientific gate.

## Breaker

A separately written in-session exhaustive local census checked all \(3^6\) incidence words at one four-dimensional edge. It found exactly twelve charged words at \(p=5\): six choices of the missing plaquette for positive current and six for negative current. Every charged word has exactly five occupied incidences, all aligned.

The first breaker expectation incorrectly anticipated two words by forgetting the six possible missing plaquettes. That expectation was not a frozen claim. The preregistered five-of-six theorem survived unchanged.

The breaker also checked the unit/zero window for \(2\le D\le12\) and every odd prime \(p\le31\), with no counterexample.

## Ceiling

Finite computation: candidate-C only.
Written proof: candidate-T pending separate review.
No Canon, Registry, Frontier, P1, massless-phase or physical-prime promotion is earned by this run.
