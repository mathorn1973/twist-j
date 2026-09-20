# Public acceptance

Status: **PUBLIC TWO-ARCHITECTURE PASS; candidate-T; NON-CANONICAL**.

The complete result commit tested by the public workflow was
`2dd4f335a4cad2f2461f8d436d4b519ed866ba22`, based on public main
`c7223ba461e264bde96eaedee4430704580235d3`. All five scientific files
remain byte identical to the pre-execution pin
`8b434780ac9cc5c730a2ff4ef3c8ac57273d7bf3`.

Public workflow: [policy run 35500142002](https://github.com/mathorn1973/twist-j/actions/runs/35500142002),
completed successfully on 2026-09-20.

| Required job | Result | Evidence |
| --- | --- | --- |
| architecture-x86_64 | success | [job 106050350916](https://github.com/mathorn1973/twist-j/actions/runs/35500142002/job/106050350916) |
| architecture-aarch64 | success | [job 106050350729](https://github.com/mathorn1973/twist-j/actions/runs/35500142002/job/106050350729) |
| check | success | [job 106050395068](https://github.com/mathorn1973/twist-j/actions/runs/35500142002/job/106050395068) |

Both architecture logs explicitly identify the probe and report the same
verifier and stdout SHA-256 values:

```text
verifier_sha256: f218660199821a73e3a6117abe8e2ba60f86335eb7c1a4ebbbee8b1470ffb5a8
stdout_sha256: e63aee0b6e4141b53bb54635fc874b7e1352c8ad807ac071dea36d8de84aa0a7
```

These values match the first local run and committed EXPECTED.txt.
Each public architecture ran Python 3.12.14. The publication job was
skipped for this probe pull request; it is not a scientific failure.

The independent breaker is separately recorded in BREAKER-RUN.md as one
local x86_64 execution. This record does not claim a public aarch64
execution of break.py.

This acceptance record is a neutral descendant of the tested result
commit. Before merging, the final PR head must pass the same required
jobs again. Acceptance establishes public probe evidence, not a Canon
promotion. ENTROPY-LAYER-BRIDGE remains O until a separate declared fold
adopts the precisely scoped disposition in FOLD-PROPOSAL.md.
