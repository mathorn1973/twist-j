# P-QDD-PASSIVE-THRESHOLD-MOMENT-1

Owner: A. M. Thorn, assisted by the Codex threshold-moment session,
2026-09-16. Public reservation:
[issue #1024](https://github.com/mathorn1973/twist-j/issues/1024).

The authority baseline is ACTIVE Public Canon v87, public main and activation
commit `fd512f50d90382124e7c00afa926c8083fd56e06`, tag `canon-v87`, content
commit `41c8d4229b71437f09957d959975dc1772e95806`, Canon SHA-256
`a2517c6d8efb1969a7258f94d9874cca3b5b9beb1aecdfd2e39b56f33961a917`,
634207 bytes. Authority, ancestry, hashes, required checks and remote
collision scans were confirmed by the coordinator before this preparation.
This file claims neither a public pin nor a completed run before the separate
pin and run records exist.

**Prior exposure.** The endpoint ensembles, coefficient, histogram segment
and fourth-moment repair were obtained in explicitly non-canonical exact
exploration on 2026-09-16 before this preregistration. They are disclosed
inputs to a proof-first mathematical audit, not blind predictions against
unseen data. The new verifier has not been executed before its public pin.
No external experimental payload is used or opened.

## 1. Equation

Use the existing balanced head grid `Z={-2,-1,0,1,2}^4`, coordinates indexed
0 through 3, and the selected passive atom weights

```text
t(z)=(z0+z1+z2+z3)^2/20,
l(z)=(z0-z1-z2+z3)^2/4,
r(z)=((z0-z3)^2+(z1-z2)^2)/2.
```

All five literal passive records have exactly the existing fields, orders
and zero rule. Freeze `F={z in Z:(t,l,r)=(0,1,5)}` and the raw second moment

```text
Sigma = [[1,0,-1/2,-1/2], [0,3/2,-3/2,0],
         [-1/2,-3/2,5/2,-1/2], [-1/2,0,-1/2,1]].
```

The class E consists of every rational probability assignment to Z with full
passive-record pushforward equal to the point record law of F and raw
second moment Sigma. In this finite L1 statement a probability assignment is
specified rational input data, not a law derived from U or a physical
occurrence claim. The condition on the full law is equivalent to support
in F, since PI-ATOMS is one of the selected records. Arbitrary such
assignments are admitted; no parametric mixture ansatz defines E.

Freeze the inherited centered five-site source, five-shell wave operator,
one cold origin port of conductance one, zero initial heat and one update.
Its signed response is `b0=-h0 z/3`, where
`h0=(1421,-349,-349,-349)/1620`. The deposit is `D0=(h0 z)^2/9`.
Freeze threshold `q=1/10` and count `C=floor(D0/q)`, including C=0.
On F, `sum z_i=0` and

```text
D0=c z0^2, c=3481/26244;
z0^2 in {0,1,4} gives C in {0,1,5} respectively.
```

The asserted complete attainable count-law set for E is

```text
(Pr(C=0),Pr(C=1),Pr(C=5))=(3a,1-4a,a),
a rational, 0<=a<=1/4.
```

All other count masses vanish. The exact bounds are
`1/4<=Pr(C>0)<=1` and `1<=E[C]<=5/4`. Real probability assignments give
the same segment with real a. With `M4=E[z0^4]`, exactly one additional
scalar expectation is sufficient and necessary for identifying this law:

```text
1<=M4<=4,
a=(M4-1)/12,
Pr(C>0)=(5-M4)/4,
E[C]=(11+M4)/12,
M4=(26244/3481)^2 E[D0^2].
```

The minimality is zero versus one extra scalar expectation on this fixed
class, after the complete passive law and raw Sigma are supplied. It is not
a universal detector calibration count or a claim about physical access to
that extra observable.

## 2. Code

The accepted exact verifier is
`probes/P-QDD-PASSIVE-THRESHOLD-MOMENT-1/verify.py`; the universal written
argument is `PROOF.md`. The verifier is standalone Python standard library
with Fraction arithmetic, integer enumeration and exact flooring. It imports
no scientific verifier or repository data and performs no network or file
writes. It rejects optimized Python before any scientific gate.

This complete three-file package must be committed, pushed and read back
from its immutable public pin before the first formal execution. The formal
command from the repository root is

```text
python3 probes/P-QDD-PASSIVE-THRESHOLD-MOMENT-1/verify.py
```

Local formal execution is planned for Ubuntu 22.04 on x86_64 with its
recorded CPython version; the required GitHub jobs use Python 3.12 on
x86_64 and aarch64. Success requires exit zero, empty stderr and deterministic
LF stdout. Both required architecture jobs must reproduce one committed
EXPECTED.txt byte-for-byte. Pin, code/preregistration hashes and neutral
environment metadata belong to the subsequent RUN.md. Compilation and
static review are permitted before the pin; executing this verifier is not.

## 3. Carrier or data

The ambient finite source is all 625 balanced vectors, including zero.
Each is represented by a genuine K_QDD head at counter zero with these
balanced first four coordinates and last two coordinates zero. Fixing that
representative does not claim uniqueness or physical preparation.

The six endpoint sources and their exact masses are:

| P source | P weight | Q source | Q weight |
|---|---:|---|---:|
| (0,1,-2,1) | 1/2 | (1,-2,1,0) | 1/4 |
| (0,2,-1,-1) | 1/4 | (1,0,1,-2) | 1/4 |
| (2,0,-1,-1) | 1/4 | (1,1,-2,0) | 1/2 |

P and Q must have identical complete passive-record laws and raw Sigma but
count laws `(3/4,0,1/4)` and `(0,1,0)`. Their means are allowed to differ:
Sigma is not called a centered covariance. Independently symmetrizing each
source into z and -z with half its weight must preserve the passive law,
Sigma, deposit/count law and M4 while giving mean zero.

The first-step coefficient is independently rebuilt from the source sites
`(0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0)` and all displacements of squared
norm `2,4,8,10,16`, with respective weights `(6,1,15,1,1)/324` on D3.

Frozen audit gates:

| Label | Audit |
|---|---|
| G1-RECORDS | All 625 sources and five coherent literal records each; native balanced representatives; all explicit zero records; exact F definition |
| G2-ORIGIN | 60-vector stencil, total weight 8/9, independently reconstructed h0, and exact D0/count/polynomial identities at every F source |
| G3-ENDPOINTS | P/Q normalization, full record laws, raw Sigma, distinct count laws, and centered sign symmetrizations |
| G4-SHARP-SET | Pointwise indicator identities, both attained endpoints and convex-construction audits at a=0,1/16,1/8,3/16,1/4; the written affine proof covers every rational/real a |
| G5-MOMENT-REPAIR | Exact M4, E[D0^2], whole histogram and bound formulas; endpoint necessity and one-expectation sufficiency |
| G6-TYPE-AND-ZERO | Rejection of ill-typed/out-of-grid, duplicate, negative or non-normalized ensembles; explicit ambient zero counted as zero without renormalization |

The finite checks audit the proof; five convex samples are not the basis of
the universal attainable-set assertion.

## 4. Systematics and scope controls

- Preserve literal partition IDs, block order, five coherent fields and the
  zero-support tag. A full passive law is stronger than equality of passive
  means. The endpoint law is a point mass for every chosen partition.
- Keep the raw second moment distinct from centered covariance. Both the
  asymmetric and explicitly centered versions are audited.
- Keep the threshold exactly 1/10, the port at the origin, conductance one,
  the cold initial slot, source marking and single update fixed. No result
  at another threshold or physical detector is silently substituted.
- Include every count and every source permitted by E. The zero source is
  part of Z and is handled explicitly; it receives zero weight in E because
  its passive record differs from the specified point law, not because a
  no-detection event was discarded. Sources with C=0 remain in every law.
- Do not infer iid trials, actual occurrence, empirical convergence, a U
  preparation law, physical source/port/clock calibration or an L6 measure.
  The ensemble is drawn once as stipulated mathematical input.
- Minimal one means one extra scalar expectation to determine this fixed
  count law. It neither identifies the whole source distribution nor states
  that M4 or D0^2 has an admitted physical realization.

## 5. Failure threshold and dispositions

One exact admitted failure of any frozen record equality, coefficient,
endpoint moment/law, pointwise count identity, claimed attainable histogram,
sharp bound, moment-repair equation or necessity/sufficiency statement is a
scientific FAIL for the affected assertion. An omitted admissible law or an
asserted attainable law with no admitted ensemble is likewise a failure.
Tolerance is zero; there is no fit, numerical epsilon or movable threshold.

Malformed/out-of-class ensembles are expected rejections, not admitted
counterexamples. Authority, reservation, pin, bundle, runtime, optimization,
stdout custody or architecture defects are STOP, not mathematical refutation.
A verifier defect or incomplete execution gives no completed scientific
disposition. Completed failures are preserved; no scope or gate may move
after the immutable public pin.

## 6. Action layer and proposed consequence

All source, record, rational ensemble, deposit and count calculations are
conditional L1 mathematics. The proof may support
`QDD-PASSIVE-THRESHOLD-MOMENT-COMPLETION [T]` at this exact finite source and
selected coupling scope after independent review. It establishes a limitation
and a smallest mathematical repair of specified observational information.

The existing passive-family D is an input, not newly adopted here. None of
QDD-INSTRUMENT-APPARATUS, QDD-TERMINAL-EVENT-SEMANTICS,
QDD-INSTRUMENT-CLASS-COMPLETENESS or BELL-CAUSAL-ACCOUNTING is closed or
partially satisfied. No physical post-state, apparatus family, reset,
sampling law or cross-layer L1-to-L4/L5/L6 gate is supplied. Any Canon fold
is a separately reviewed operation.
