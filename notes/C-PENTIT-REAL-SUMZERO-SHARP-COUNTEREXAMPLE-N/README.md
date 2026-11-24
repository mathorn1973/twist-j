# Real sum-zero pentit: a counterexample and stronger bounds

**NON-CANONICAL / candidate-T / L1 notes incubation.**
Follow-up to merged #1343, under object lock #1344. Public Canon remains v97.

The proposed extension of the 624-preparation minimum `phi/5` to every
real sum-zero pentit state is false. An explicit cosine state has

$$
\mathcal N=\frac{\sqrt{5+2\sqrt5}}{10}<\frac\varphi5.
$$

A separate proof improves the universal lower bound, leaving the still-open
global minimum in the interval

$$
\frac1{2\sqrt{5+2\sqrt5}}
\le\min\mathcal N
\le\frac{\sqrt{5+2\sqrt5}}{10}.
$$

Both results concern the declared normalized real sum-zero reading in the
original phase-point convention. The finite 624-state census remains intact;
the witness supplies no native preparation or actual occurrence law.

| File | Purpose |
| --- | --- |
| [PROOF.md](PROOF.md) | Witness, full Wigner table, strict comparison and real-source embedding |
| [LOWER-BOUND.md](LOWER-BOUND.md) | General analytical lower bound |
| [PREREG.md](PREREG.md) | Exposed targets, fixed scope, six fields and failure conditions |
| [verify.py](verify.py) | Exact cyclotomic-40 witness audit, standard library only |
| [EXPECTED.txt](EXPECTED.txt) | Exact stdout of the first pinned execution |
| [RUN.md](RUN.md) | Public pin, readback, environment and byte custody |
| [REVIEW.md](REVIEW.md) | Separate same-session proof/source/security review |
| [RESULT.md](RESULT.md) | Conclusions, fired falsifier and construction boundaries |
| [SHA256SUMS](SHA256SUMS) | File-content custody manifest |

The public input pin is `fd41b1cb5662983a34742829807d9c510014242c`.
The first post-readback audit passed **148 exact assertions**, on Linux
x86_64 with CPython 3.12.14. Targets were known before the pin. The audit
confirms one witness; the general lower bound has a separate proof.
This is not a blind test, external referee report, independently authored
second implementation, two-architecture scientific gate or Canon promotion.

`REVIEW.md` distinguishes its pre-run static disposition from subsequent
runtime custody. `RUN.md` and `RESULT.md` record the completed confirmation.
Notes-only repository CI does not replay `verify.py`; any green architecture
jobs must not be presented as a second-architecture run of this result.

The entire predecessor directory is an immutable input. All original files
are retained unchanged. Native preparation, context-dependent reading,
renewal and the actual occurrence law remain separate construction tasks.
