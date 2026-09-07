# P-U-FINITE-READER-INDEPENDENCE-1

The actual native U trajectory has a precise independence boundary for fixed
finite-window readers: accepted word complexity grows at most linearly, while
deliberately chosen readers can match any preselected finite fair horizon.

- [PREREG.md](PREREG.md): immutable class, audit ranges and decision threshold.
- [PROOF.md](PROOF.md): full native language and accepted-word bounds, empty
  acceptance, finite unions, and finite-horizon positive construction.
- [RESULT.md](RESULT.md): mathematical conclusions and physical limits.
- [RUN.md](RUN.md): public pin custody and first local execution.

Replay from the repository root in the preregistered Linux environment:

```text
python3 probes/P-U-FINITE-READER-INDEPENDENCE-1/verify.py
```

Requires Python >=3.10 and the standard library only; CI uses Python 3.12.
Exit must be zero, stderr empty, and stdout byte-identical to
[EXPECTED.txt](EXPECTED.txt). Both required architectures remain separate
reviewed-head evidence. The finite audit supports the written proofs; it
supplies neither a physical occurrence mechanism nor a Born falsification.
