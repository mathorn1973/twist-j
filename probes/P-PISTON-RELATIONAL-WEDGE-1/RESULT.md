# P-PISTON-RELATIONAL-WEDGE-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS;
PUBLIC CANON UNCHANGED

The immutable preregistration pin
`348c3c3ea65b0dbc79052a70482eba690e82b145` (base `91e11e4`, Public Canon
v52, claim lock #425) was executed exactly once on native Linux/aarch64
after public remote readback. The verifier exited zero, wrote no stderr,
and produced the exact 4431-byte output recorded in `EXPECTED.txt` with
SHA-256 `c41fe236222402f35d678316e3180b651a8c51da600135bc3dda78071e4337b0`.
All forty-eight gates passed: the two integrity gates, the factor-local
form of `a` and `b` under the frozen reshape with lift compatibility, the
non-linearity of `c, d, e`, the labeling census (8 of 24, one class, common
`|D_Z|`), the sign characters and `<a,b>`-invariance, the transpose-slot
functional and the `kappa` consistency over `Q`, the singular-matrix count
145 modulo 5, the frozen `Tr_4` closed forms and their dependence on
`(s, |v|^2)` alone, the non-separating witness pair, the recovery of `D_Z`
from total weight and density on all 625 records with the density-only
scale witness, the two guards, and the lift census (8 at `|D_Z| = 8`, 16 at
`|D_Z| = 5` all with `c_Z = 1`, 129 with `D_Z = 0`, 48 with `c_Z = 1`,
bounds on all 624 nonzero pistons). No counterexample was emitted; no
falsifier fired.

## Verdict

```text
PISTON-2X2-RESHAPE-WEDGE               proposed [T]  written proof R3; gates PASS
QDD-TR4-OCCURRENCE-WEIGHT-WEDGE-BLIND  proposed [T]  boundary row; written proof R4;
                                                     REQUIRES QDD-PROJECTOR-PAIR-TR4,
                                                     QDD-ALGEBRAIC-FACTORIZATION,
                                                     PISTON-2X2-RESHAPE-WEDGE
PISTON-WEDGE-LIFT-CENSUS               proposed [T]  R5.i to R5.iv, written proof
                                                     and exact counts PASS
R4.v, R5.v REPORT lines                audit output only; no row, no status
G1, G2                                 guards, integrity only; no claim
QUADRATIC-DECODER-DATA                 [O] / STOP, untouched
QDD-INSTRUMENT-APPARATUS               [O], untouched
```

Under `DEF-PISTON-2X2-RESHAPE`, `X_p = ((ell p1, ell p4), (ell p1p, ell p4p))`
is the unique labeling class in which both linear kernel generators are
factor-local: `a = 1 tensor sigma`, `b = -(sigma tensor 1)`, exactly 8 of
24 labelings, one class under bit relabeling and factor exchange. The piston
wedge `D_Z = det X_p` is odd under `a` and under `b`, so `|D_Z|` and
`c_Z = 2|D_Z|/|v|^2` are `<a,b>`-invariants; `D_Z` is the linear functional
`(A_T)_14 - (A_T)_23` on the transpose slot, `det(X_p X_p^T) = D_Z^2`, and
`D_Z/2` is the `kappa` coefficient of `QPAIR-SYM2-TENSOR-DEFECT` specialized
to `K = Q` (named consistency clause, no carrier bridge). `D_5 = 0` on
exactly 145 pistons.

The frozen `Tr_4` occurrence-weight map `(m, w_low, w_high)` and its
normalized pair depend on `(s, |v|^2)` alone and are not separating for the
wedge: `(1,0,0,1)` and `(1,1,0,0)` share `(6/5, 1/5, 1)` and `(1/6, 5/6)`
while `D_Z = 1` against `0`. The full public record is not blind: on
SUPPORTED records total weight and density together recover
`v v^T = m rho G^-1` and hence `D_Z` on all 625 pistons, while density alone
is scale-blind (`(1,0,0,1)` and `(2,0,0,2)`). The relational information of
the piston lies in the public quadratic carrier; only the frozen occurrence
weights fail to separate it. Nothing is said about what a decoder should
read.

The `F_5` wedge and its balanced `Z` lift disagree on exactly 16 pistons:
singular modulo 5, `|D_Z| = 5`, `|v|^2 = 10`, `c_Z = 1`; hence
`145 = 129 + 16`, because `ell` is not a ring homomorphism. Exactly 48
pistons have `c_Z = 1`, namely those with `X_p X_p^T = lambda I`; the
maximum `|D_Z| = 8` is attained by 8 pistons.

REPORT-only audit output: 63 classes of `(s, |v|^2)`, 32 of them carrying
more than one `|D_Z|`; `d` changes `|D_Z|` on 508 pistons; twelve values of
`c_Z`, namely `0, 2/7, 4/13, 1/3, 4/9, 3/5, 2/3, 4/5, 6/7, 8/9, 12/13, 1`,
with multiplicities `128, 32, 32, 32, 64, 16, 128, 48, 32, 32, 32, 48`.
These reports agree with the drafting expectations exposed in `PREREG.md`;
they are not fields of any target row.

## Evidence

```text
PREREG.md    sha256 2467e6847229ca829989e6929342d0f0200249b064245d880f8beb1ad6c28001  29137 B
verify.py    sha256 74940cbf4482abb7541fafc1b1e2262410533472a81dc0e07672bfb91bae52b4  18812 B
EXPECTED.txt sha256 c41fe236222402f35d678316e3180b651a8c51da600135bc3dda78071e4337b0   4431 B
```

The accepted local leg is the single formal execution on Linux/aarch64,
CPython 3.12.3, deterministic environment, exit zero, empty stderr, with the
raw stdout returned on issue #425 before this record was written. The
first clean GitHub Linux/x86_64 pull-request replay (pull request #427)
used the identical pinned verifier at tested merge commit
`98e26368c5325a9f8add1ad4d8f1bc8ed532d590`: workflow run `32219987568`, job
`95968523697`, exit zero, empty stderr, `EXPECTED.txt` reproduced byte for
byte; the parallel GitHub Linux/aarch64 job `95968523721` replayed
identically and the aggregate check job `95968573327` passed. The
two-architecture computation gate is PASS.

## Scope firewall

"Piston wedge" names `D_Z` and `D_5`, a wedge inside one checkpoint, not
the cell-pair wedge of the `KERNEL-WEDGE-*` rows. "Not separating" means
equal values on the exhibited pair with unequal `D_Z`; the sentence "the
decoder does not read the wedge" is forbidden and false, since the record is
injective on `QCarrier_QDD` and its total-weight and density fields recover
`D_Z`. `c_Z` is a normalized wedge ratio; "concurrence", "entanglement",
"joint state", "two-qubit" and "measurable" do not occur in the theorem
layer. The reshape is an arrangement selected by `a` and `b`, unique within
the declared admissibility class only; no physical systems are named for
the two factors. `c_Z` is normalized by the coordinate form; guard G1
records that `G` is not a product metric and no `G`-normalized wedge is
defined. The consistency clause applies a characteristic-not-two theorem to
`K = Q` and imports nothing from the integral cyclotomic carrier. The probe
creates no edge to `QUADRATIC-DECODER-DATA` or `QDD-INSTRUMENT-APPARATUS`,
no `BELL-CAUSAL-ACCOUNTING` row, no effect identifier, no instrument, no
event stream, no measure, and no L2 to L6 or physical statement.

## Recorded decision

```text
run integrity:       PASS
counterexample:      NONE
result:              PASS
architecture gate:   PASS (local aarch64, GitHub x86_64, GitHub aarch64)
scope:               R3, R4, R5 of PREREG.md, layer L1, frozen public
                     piston carrier V_eff
status discipline:   the probe result stands at its evidential grade; the
                     registry rows PISTON-2X2-RESHAPE-WEDGE,
                     QDD-TR4-OCCURRENCE-WEIGHT-WEDGE-BLIND and
                     PISTON-WEDGE-LIFT-CENSUS with their REQUIRES edges and
                     the Canon fold are a separate sealed integer-versioned
                     step and are not made by this probe
```
