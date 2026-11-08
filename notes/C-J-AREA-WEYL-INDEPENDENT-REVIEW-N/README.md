# Independent review of J/phi area and Weyl covariance

PUBLIC / NON-CANONICAL / L1. A. M. Thorn. Apache-2.0.
Review session: Codex-R1-20261017-b053a37f.
Assignment: [R1, issue #1587](https://github.com/mathorn1973/twist-j/issues/1587).
Target: [PR #1583](https://github.com/mathorn1973/twist-j/pull/1583),
head `e40b637b81f1a6fca99a543e970c83a4e0d45ebc`.

This is a separate review of one declared L1 construction. It starts from
the original source preregistration and registered Canon dependencies.
The source author's implementation, proof and results are withheld until
the independent proof and breaker are publicly frozen and initially run.
The hypotheses are disclosed, so the review is method-blind, not result-blind.
[EXPOSURE.md](EXPOSURE.md) records the actual boundary.

[PREREG.md](PREREG.md) specifies the independent attacks and exact thresholds;
[PROOF.md](PROOF.md) gives the unbounded arguments;
[break.py](break.py) audits the frozen finite classes without importing the
author's verifier; [SOURCES.tsv](SOURCES.tsv) binds the allowed source bytes.
Execution and the subsequent author comparison are recorded separately
in RUN.md, EXPECTED.txt, REVIEW.md, RESULT.md and PROMO.md after the pin.

Run from the repository root, only after the public pin:

```sh
LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
python3 notes/C-J-AREA-WEYL-INDEPENDENT-REVIEW-N/break.py
```

The standard notes-only PR checks do not execute this breaker. Its exact
execution evidence must be read from the explicit run record. Scientific
PASS requires the actual output, not merely exit code zero or green CI.

The review owns no native realization, physical character selection,
energy scale, action quantum, SI bridge or Canon promotion. R2 and N are
separate tasks.
