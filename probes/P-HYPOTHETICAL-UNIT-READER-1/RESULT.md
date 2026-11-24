# A complete working reader with conditional linear energy

Status: COMPLETE, NON-CANONICAL.
Mathematics: conditional candidate-T, L1.
Physical availability: working hypothesis H.
Owner: A. M. Thorn; reservation [#1431](https://github.com/mathorn1973/twist-j/issues/1431).

## Result

One explicit autonomous reversible law now provides two successive actual
unit writes into the same occupied receiver, an updated five-position
pointer, retained contact context, a fixed reader of the last transfer,
complete fault states and fixed disconnection switches. The amount-first
contact is a new hypothesis. Its code and consequences are fully specified.

The strongest conditional calibration result is:

\[
\mathcal E_{f,A}\circ T_R=\mathcal E_{f,A}
\quad\Longleftrightarrow\quad
f(n)=\varepsilon n\ \text{and}\ A(h(T_Rs))=A(h(s))
\]

on the complete declared carrier and in the separated common-profile
family \(f(r_1)+f(r_2)+f(y)+A(h)\), \(f(0)=0\).
When both contacts are enabled, this reduces to

\[
\mathcal E=\varepsilon(r_1+r_2+y)+C.
\]

The proof includes faulty raw flags. On the calibrated sector alone, the
exact stock-profile family is instead
\(f(n)=\varepsilon n+b[n>0]\); an apparatus occupancy cost can compensate b.
Two matched correctly flagged same-shell transitions already select c=1
in the earlier parity-price family. Energy is not used to set the transfer
amount in the new law.

The unit scale, common stock kind, availability of the contact, complete
apparatus description, preparation and additive energy class are physical
premises. They are not promoted by the mathematical result.

## What can be examined now

[model.py](model.py) is a standalone standard-library simulator with explicit
initial stocks, arbitrary complete raw states, contact disconnection,
forward/backward steps and table/JSON output. The [Czech guide](README.md)
gives runnable commands. [MODEL.md](MODEL.md) specifies every branch and
proves its infinite-domain scope.

For independent binary sources a,b and initial receiver t in {0,1,2}, the
actual receiver follows \(t\to t+a\to t+a+b\). The second operation consumes
the actual first output. For conserved N<=4 and an initially calibrated
pointer, p equals the full receiver stock throughout the orbit.

With t=1, source inputs 10 and 01 end at the same stock triple (0,0,2),
pointer 2, phase and flags but have last changes zero and one. The retained
directions distinguish them. A specifically wrong zero flag instead
reports minus one when actual transfer was zero; the model preserves that
fault rather than silently correcting it.

## Actual default trajectory

The table displays selected coordinates of the actual report. EXPECTED.txt
contains every complete twelve-coordinate boundary, including flags,
switches and phase. The complete state first returns at step twelve.

| Step | Source 1 | Source 2 | Receiver | Direction 1 | Direction 2 | Pointer | Actual receiver change |
|---:|---:|---:|---:|:---:|:---:|---:|---:|
| 0 | 2 | 1 | 1 | + | + | 1 | prepared |
| 1 | 1 | 1 | 2 | + | + | 2 | 1 |
| 2 | 1 | 0 | 3 | + | + | 3 | 1 |
| 3 | 0 | 0 | 4 | + | + | 4 | 1 |
| 4 | 0 | 0 | 4 | + | - | 4 | 0 |
| 5 | 0 | 0 | 4 | - | - | 4 | 0 |
| 6 | 0 | 1 | 3 | - | - | 3 | -1 |
| 7 | 1 | 1 | 2 | - | - | 2 | -1 |
| 8 | 1 | 2 | 1 | - | - | 1 | -1 |
| 9 | 2 | 2 | 0 | - | - | 0 | -1 |
| 10 | 2 | 2 | 0 | - | + | 0 | 0 |
| 11 | 2 | 2 | 0 | + | + | 0 | 0 |
| 12 | 2 | 1 | 1 | + | + | 1 | 1 |

This is a recurrent device with reverse flow, not an unlimited permanent
archive. Correctness of an event record depends on the declared interface,
and correctness of a full stock reading depends on its range/calibration.

## Frozen evidence and first execution

The complete nine-file input pin is
ceb9e07e0842b17086bc990547af3f04a1e66bc0.
All nine public files were fetched and compared byte for byte before the
first execution. [RUN.md](RUN.md) retains the exact first-run metadata;
[REVIEW.md](REVIEW.md) discloses separate mathematical, implementation and
public-safety review.

The first local execution on Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12
completed with exit zero, empty stderr and unchanged inputs. Both
separately authored programs produced exactly the same 2839-byte,
252-line output, now [EXPECTED.txt](EXPECTED.txt).

- Scientific stdout SHA-256:
  b0ddf5d82629e707ed9aafe9100e477100e75db5ea454fd277413d83d75f3745
- Accepted final verifier SHA-256:
  90a908b81d8cb7e71934fa3a83138ba30da5922441757d3db53ba6297f6b1478
- Complete ordered transition-table SHA-256:
  7c52a4fb34110c9edc53b72d28f65df689b5c7ba44d1bbc9ba450b6f456e19b7

The finite audits cover all 211200 complete states with N<=8, including
26400 correctly flagged states with arbitrary pointer offsets. All twelve
two-write preparations, six disconnection pairs at 78 compared boundaries,
the context/fault/energy witnesses and the complete return agree.

The primary code uses the explicit branches; the separately authored code
uses a cyclic coordinate. Shared specification and known expected witnesses
are disclosed limits. This is not a result-blind or experimental comparison.

## Falsifier dispositions

| Frozen item | Disposition |
|---|---|
| F1 complete inverse/carrier | No failure in the exhaustive finite audit; general inverse proved. |
| F2 accounts/locality/disabled branches | No failure in the finite audit; universal accounts proved. |
| F3 calibrated current reader | All 26400 correctly flagged inputs pass; general reader proved. |
| F4 consecutive writes | All twelve supported preparations pass. |
| F5 context and fault witnesses | Both expected negative controls occur exactly as declared. |
| F6 matched energy witnesses | Same-shell inputs and hardware changes agree; defects are (2,-2) and (0,0). |
| F7 return/disconnection | Twelve-step complete return and all 78 comparisons pass. |
| F8 independent exact output | Byte-identical complete reports, including transition hash. |
| F9 universal mathematical scope | Separate manual review ACCEPT at the written conditional scope; no counterexample found. |

No frozen falsifier fired. No input, code, predicate, bound or threshold
changed after the public pin. Universal energy and reading theorems depend
on their written proofs, not extrapolation from N<=8.

The existing required PR workflow replays this same verifier against this
same EXPECTED.txt on x86_64 and aarch64 under Python 3.12. Its live checks
supply the architecture gate; the first local record does not claim those
jobs had already run.

## Where this moves the physical question

The next implementation target is a concrete local contact B with actual
pointer and XOR flag updates, exercised on successive occupied outputs.
Disconnection, zero-donor reflection, faulty calibration and the equal-shell
energy comparison distinguish its predictions. The origin of a general
decoder is no longer the only object available for examination.

This is a new working interaction law. It does not close the native-U/J
realization question, implement the whole earlier Gauss shell, establish
commutation with G, derive a spatial metric or supply a laboratory energy
unit, physical tick, Hilbert coherence, photon phase or occurrence rule.
The existing packet/controller constructions are credited in MODEL.md.
Canon, registry, gates, policy, workflows and earlier probes are unchanged.
