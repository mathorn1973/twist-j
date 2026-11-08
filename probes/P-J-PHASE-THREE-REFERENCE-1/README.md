# P-J-PHASE-THREE-REFERENCE-1

PUBLIC / NON-CANONICAL / L1. Author: A. M. Thorn. Apache-2.0.
Claim: [issue #1580](https://github.com/mathorn1973/twist-j/issues/1580).
Public Canon v103, base `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`.

## Question and construction

Can all five prepared roots pass through fixed declared contacts into the
existing funded two-use receiver, using shared resources that are restored
between contacts? This successor to [PR #1579](https://github.com/mathorn1973/twist-j/pull/1579)
adds a complete five-phase code and a shared compute/copy/uncompute prefix.

Three fixed determinant-one references give binary predicates
`delta=1-h^4` with the following exact code in F5:

| Source | delta_A | delta_B | delta_C | M |
|---|---:|---:|---:|---:|
| 1 | 1 | 1 | 0 | 3 |
| j | 0 | 0 | 1 | 4 |
| j^2 | 0 | 0 | 0 | 0 |
| j^3 | 1 | 0 | 0 | 1 |
| j^4 | 0 | 1 | 0 | 2 |

Here `M=delta_A+2 delta_B+4 delta_C mod5`, so `k=(M+2) mod5`.
Three binary results are minimal in the specified bit-factor class. This
is not a minimum number of physical reference cells or a universal lower
bound for arbitrary source readers.

The actual 14-leaf CONTACT-RECORD word writes each predicate; complete-cell
CSUM adds the weighted reference to the actual apparatus head; the inverse
word restores the entire reference, source and shared bit. The same three
references and ONE bit serve both original sources. The 182-operation
prefix uses seven native cells in total, followed by the unchanged old
seven-step apparatus schedule. No prepared endpoint is loaded into it.

Both classical deposits use ONE budget B=5. The analytical upper bound is
23/5; it covers the two old classical inputs. It does not price the prefix
or preparation. The unchanged typed reader must recover both source vectors;
the fixed phase decoder must then recover both phase labels from retained
records with hidden buffer d omitted, on all 25 ordered pairs.

## Evidence and reproduction

[PREREG.md](PREREG.md) fixes the equation, full inventory, exact thresholds,
code and execution rules. [PROOF.md](PROOF.md) contains the authored global
arguments, reference census, shared inverse construction, energy proof and
record decoder. [SOURCES.tsv](SOURCES.tsv) binds the public dependencies.
The verifier includes a second wave/tape implementation directly from the
primary equations, specified to compare 200 complete state boundaries with
the old apparatus. Same-session dual implementation is not independent
authorship.

From the repository root, after the public pin:

```sh
python3 probes/P-J-PHASE-THREE-REFERENCE-1/verify.py
```

The scientific outcome, exact transcript and reproduction evidence are to
be recorded after execution in RESULT.md, EXPECTED.txt and RUN.md. The
preregistration and accepted verifier must remain identical to their pin.

## Scope

The conclusion is conditional transfer and retention in the declared
extended architecture. Native admission includes W_b, Ucal, reference and
bit preparation, and autonomous control; these remain open. Prefix energy,
physical source/contact realization and reference selection remain open.
Prepared phase orientation is not a derived frequency sign. Physical
reading has no status. Identity phase is present; a zero-piston control
outside the five-phase promise aliases j^4 and does not establish absence
detection. There is no Canon, registry or gate promotion.
