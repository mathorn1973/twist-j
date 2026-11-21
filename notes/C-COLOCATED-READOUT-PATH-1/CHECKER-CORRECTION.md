<!-- SPDX-License-Identifier: Apache-2.0 -->

# Disclosed correction of the reader comparison boundary

NON-CANONICAL / L1 / no authority. Administrative correction record after
first-run STOP. No corrected scientific result is asserted here.

## Preserved first run

The frozen preregistration was committed at `d8c7a28f`. Both original
implementations and the accompanying proofs were frozen at
`c84ee2ba587fbad2fb72015c2f1753df3d1d3e7d` before their first executions.
The independent original `break.py` stopped with exit code 1 at input
`(r,s,t)=(0,2,2)`, forward cut 160, on the check named
`positive final memory disturbed`. Its complete first failure is retained
in `BREAK_EXPECTED.txt`.

Original source SHA-256:
`fabd061f908caad1125502c47df4644e7db393efdbf8650ad24b3daac258295c`.

Original first-output SHA-256:
`14f81c48660cab5293618a6a307f2541c7662f2a3da37ae3bf9e1114ad8d4599`.

The original source and its first output remain unchanged. The first frozen
run failed; it cannot be relabelled PASS by this correction. The stronger
assertion that the memory after the complete writer-plus-reader word always
differs from its initial preparation remains falsified by this case.

## Exact boundary error and counterexample

The original assertion compared the final memory against `v[2:4]`, the
memory before the writer `W`. For the first failing case, the root-pair
phases at the three relevant boundaries are:

| Boundary | Memory phase | Memory pair |
| --- | ---: | --- |
| Before `W` | 2 | `(j^2,-j^2)` |
| Before `L`, after `W` | 0 | `(1,-1)` |
| After `L` | 2 | `(j^2,-j^2)` |

The pre-reader phase follows from the phase-matrix check already passed
before the failure. The final phase follows from the failed inequality:
the final pair equals the initial pair. Thus the reader changes its input
memory while the complete `W+L` word restores this initial memory pair.

The preregistration says that the memory pair is disturbed, but does not
explicitly name the comparison boundary in that sentence. In its reader
context, the intended comparison is across `L`. The original checker
instead imposed the stronger endpoint comparison across `W+L`. This
ambiguity and the post-failure interpretation are disclosed here; the
preregistration itself is not rewritten.

## Separate corrected audit

`break_reader_boundary.py` is an otherwise byte-identical copy of the
original source. Exactly one source line is replaced, including its check
label.

Original line 324:

```python
                    require(trial.v[2:4] != v[2:4], "positive final memory disturbed")
```

Replacement line 324:

```python
                    require(trial.v[2:4] != list(writer_state[0][2:4]), "positive reader memory disturbed")
```

Corrected source SHA-256:
`4ddb722421d5596079d1b7bbe6edd1c4e4f8c232d681704fad76a3f17ee8563e`.

The revised assertion explicitly tests memory change across the READER
boundary. It makes no assertion that the complete `W+L` word must change
the initially prepared memory. There are no other source changes. The
physical maps, carriers, input domain, source words, port timings,
predictions, exact arithmetic and zero-tolerance threshold are unchanged.
Every Gauss, full-account, residue, shadow, current, inverse, area,
determinant and causal-control check remains present without modification.
The stronger original assertion is retained in `break.py` together with
its falsifying first output.

This corrected audit is a post-first-failure revision. It is not a new
blind confirmation: its author has seen the original checker's failure
and the proposed boundary diagnosis. The author has not read the primary
implementation or its output. Any later corrected result must retain this
exposure and correction history and must be reported separately from the
failed first run. Local execution remains one architecture only.

At the writing of this record, the corrected scientific program has not
been executed. The separate corrected source and this disclosure must be
frozen in a new Git commit and disclosed in the public reservation before
its first corrected execution. The root session owns that freeze and run.
