# P-SNAP-INTERACTION-READBACK-1

This NON-CANONICAL probe tests new equal-payload arrivals against passive
readback. It supplies an exact erased-input counterexample, a complete
two-port loading classification, a rational fresh-space criterion and a
fixed bank construction with an explicit capacity limit.

- [PREREG.md](PREREG.md): accepted equations, finite ranges and threshold.
- [PROOF.md](PROOF.md): uniform proofs and inherited scope.
- [RESULT.md](RESULT.md): positive construction and excluded inferences.
- [RUN.md](RUN.md): public pin, byte custody and first local execution.

Replay from the repository root in the preregistered Linux environment:

```text
python3 probes/P-SNAP-INTERACTION-READBACK-1/verify.py
```

Python >=3.10 and standard library only; required CI uses Python 3.12 on
x86_64 and aarch64. Require exit 0, empty stderr and byte identity with
[EXPECTED.txt](EXPECTED.txt). The finite audit supports the proof, not an
unstated physical event or storage mechanism.
