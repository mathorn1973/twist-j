# notes/QUANTUM-OPTIMIZATION-CLAIM-AUDIT-2026-08-27

NON-CANONICAL. Notes lane, no authority, no Canon change, no `canon/` file
touched, no probe directory, no registry row, no falsifier. This is an audit
of one external argument, kept here because it was decided with a checker
rather than with an opinion.

Subject: the "oq challenge" text of 2026-08-27 asserting that hybrid quantum
optimization delivers factory-scheduling results classical hardware cannot
match, illustrated against an Atari.

This directory is **not** TWIST-J science and makes no claim about the
Canon. It is filed under `notes/` per `AGENTS.md` section 6, which is the
correct home for material that carries no earned status. Placing it in
`probes/` would have been a scope violation: it is not a claim about J, it
has no preregistration, and it must never reach `canon/REGISTRY.tsv`.

## Contents

```text
README.md                  this manifest
AUDIT.md                   claim-by-claim audit, with source checks
check_quantum_claims.py    exact checker, 18 gates (16 exact, 2 model)
quantum_claims.stdout.txt  committed stdout of the checker
SHA256SUMS                 hashes of the files above
```

## Reproduction

From this directory:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 check_quantum_claims.py
```

Expected: exit 0, and stdout byte-identical to `quantum_claims.stdout.txt`.
Add `--timing` for wall-clock on stderr; stdout is unaffected, so the
comparison still holds.

Runtime is dominated by the exact 20-node Held-Karp solve, **19.7 s** in
interpreted Python on one core. Total script runtime is well under a minute.

Recorded leg: x86_64, Ubuntu 24.04.4 LTS, Python 3.11.15. One architecture.
This is a note, not a public probe; the `POLICY.md` section 4
two-architecture gate is **not** claimed and no status is earned.

Determinism: no floats appear in any gate. Distances use `math.isqrt`, the
instance comes from a pinned LCG (seed 20260827), and timing is confined to
stderr. Verified byte-identical across repeated runs.

## Result

18/18 gates pass. The four numerical assertions in the challenge text are
false as stated:

```text
A  "20 stops > atoms in the universe"
   20! = 2.43e18 is 61 orders of magnitude SMALLER than 1e80.
   n! first exceeds 1e80 at n = 59.

B  "classical must check pathways one by one"
   Held-Karp (1962) proves the optimum in 4.98e7 steps over a space of
   6.08e16 tours, a ratio of 1.22e9 : 1.

C  "amplifies the perfect schedule, revealing it instantly"
   Grover needs ~2.47e8 oracle queries here, and from n = 21 upward needs
   MORE queries than Held-Karp needs steps. D-Wave does not run Grover.
   Samplers return no optimality certificate; the DP returns a proof.

D  exact 20-node optimum, cost 33636, in 19.7 s on one core,
   cross-validated against exhaustive search at n = 10.
```

The Atari claim is directionally right for the wrong reason: brute force on
a 1.19 MHz 6507 takes ~1.6 million years, which is **8 512x shorter** than
the age of the universe. What stops it is the ~19.9 MB Held-Karp table
against 128 bytes of RAM.

## Scope limit, stated explicitly

The checker rules on **arithmetic only**. It does not and cannot decide
whether any vendor deployment occurred, and it takes no position on quantum
hardware roadmaps.

`AUDIT.md` handles the attributed industrial facts separately, by source
check. Its finding: the Ford Otosan and Pattison Food Group deployments are
**real** but restated inaccurately in the text, the "$300 million" is an
industry-wide BCG aggregate misattributed to three named firms, and every
cited speedup is measured against the customer's incumbent manual process
rather than against a tuned classical solver. No ablation arm has been
published, so the quantum contribution is not separable from the classical
heuristics that do the primary work in D-Wave's hybrid Metasolver.

The resulting status is **unproven**, not false — a verdict about evidence,
not about physics.

## Frozen pins

```text
e999078a8d17eaa1e7edda14dc74990613158f3699c2a29a269d01fd05addad7
  check_quantum_claims.py (14596 bytes)
a9edf02509f86b86360805e3fdb992a8f03f12ec4b1d35638a80dffdba3de0bb
  AUDIT.md (10803 bytes)
7ed5a3ebfd44b125750783f6e8a806a30e89f4c950e14e7a21eb5040c494f48e
  quantum_claims.stdout.txt (4797 bytes)
```
