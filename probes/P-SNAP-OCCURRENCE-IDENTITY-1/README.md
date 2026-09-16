# P-SNAP-OCCURRENCE-IDENTITY-1

When do equal payloads count as different occurrences? This proof-first
NON-CANONICAL probe separates address equality, recoverable formal logs,
native finite-window labels and atomic recording capacity.

- [PREREG.md](PREREG.md): frozen classes, audit ranges and threshold.
- [PROOF.md](PROOF.md): complete mathematical arguments and dependencies.
- [RESULT.md](RESULT.md): positive constructions, nonimplications and scope.
- [RUN.md](RUN.md): immutable public source custody and first local run.
- [Occurrence incubation](../../notes/C-SNAP-OCCURRENCE-IDENTITY-N.md):
  relation to the existing physical apparatus owner.

Replay from the repository root in the preregistered Linux environment:

```text
python3 probes/P-SNAP-OCCURRENCE-IDENTITY-1/verify.py
```

Python >=3.10, standard library only; required CI uses Python 3.12 on both
x86_64 and aarch64. Require exit 0, empty stderr and exact byte equality with
[EXPECTED.txt](EXPECTED.txt). The finite audit supports the written proofs;
it does not establish a physical Snap or material storage mechanism.
