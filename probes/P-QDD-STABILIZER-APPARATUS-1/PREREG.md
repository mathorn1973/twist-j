# P-QDD-STABILIZER-APPARATUS-1 preregistration

**PREREGISTERED PROTOCOL / NON-CANONICAL / RESULT-EXPOSED.**
Date: 2026-09-06. The author authorized this named probe and its execution.
Execution count at the accepted pin is zero. This frozen file does not claim
a scientific result; EXPECTED and RUN are recorded only after public pin
readback and execution. The supplied candidate and prior public work were
known before pinning; no blind discovery is asserted.

```text
probe: P-QDD-STABILIZER-APPARATUS-1
branch: probe/P-QDD-STABILIZER-APPARATUS-1
path: probes/P-QDD-STABILIZER-APPARATUS-1/
author: A. M. Thorn
public_reservation: https://github.com/mathorn1973/twist-j/issues/854
immutable_pin: initial seven-file commit; exact SHA and readback recorded on issue 854 before execution
mode: PROOF-FIRST / RESULT-EXPOSED
action_layer: L4 conditional mathematical apparatus/support
public_basis: ac435f84b646ce8cb9a6c1601886c4f298881285
canon: Public Canon v77
content_commit: f7da754ffbcc37f1cbe02746025279ebd029520d
canon_sha256: 63763a6adb6f61bb7a11b719ad61d55e2c26c6fdabd05b6bfe02b03ef1087969
canon_bytes: 462590
```

## 1. Equation

For k in F5, `g e_x=e_(k+2(x-k))`, W is the exact displayed Hadamard/2,
`V_k=W diag(I,g,g^2,g^3) W`, F flips a binary flag on paths r!=0,
`E_k=V_k^-1 F V_k`, and the R control retains the fine paths after V
(with F only a redundant binary label). The complete production maps are
40-dimensional rational routing operations, not calls to target projectors.
Prepared output and reduced-system maps are the equations (1)-(3) in PROOF.md.

The universal completion class is exactly every rational orthogonal A with
`(A e0)_r in {+1/2,-1/2}`, every permutation of all four powers of g, forward
mix A and backward mix A transpose, and the matching inverse in E. No general
apparatus or fine-path equality is asserted. The denominator/lattice theorem
uses the default W only. Supportive terminal-account equations and complete
reset/archive semantics are frozen by RECORD-CONTRACT.md.

## 2. Code

The following seven files are the accepted pin content. Their exact hashes,
byte counts and initial commit are recorded on issue 854 and read back from
the public remote before any execution. A self-referential commit/hash is
not embedded in this frozen file.

| File | Role |
|---|---|
| PREREG.md | Frozen six-field scope, exposure and decision contract |
| PROOF.md | General circuit, map, mixer and lattice proofs |
| apparatus.py | Direct rational 40-mode split/routing/flag implementation |
| verify.py | Independent five-cell matrix and complete-map audit |
| RECORD-CONTRACT.md | Selected terminal-buffer and archive-account semantics |
| record.py | Exact immutable supporting record implementation |
| record_audit.py | Independent cumulative-energy and ordinal audit |

Use Python standard library and Fraction only. Importing a module must not
execute scientific gates. Accepted command, only after public pin readback, is
`python3 probes/P-QDD-STABILIZER-APPARATUS-1/verify.py` from repository root.
The earlier notes-path program was not run and is not evidence. No network access,
experimental data, old stdout, random generator or optional skip is allowed.

## 3. Carrier and inputs

System `V={v in Q^5:sum v=0}`, q=sum squares, k=0,...,4. Full carrier has
path 0,...,3, flag 0,1 and cell 0,...,4, ordered `(path,flag,cell)`.
The selected invariant carrier is 32-dimensional; the direct extension has
40 coordinates. Prepared ancillas are both zero. Exact source zero remains
in the domain; normalized energy ratios at zero are undefined and unused.

Full-system operator equality is audited on all sixteen ordered matrices
`(e_i-e_4)(e_j-e_4)^T`, i,j<4. The independent basis Gram is `I+11^T`.
An arbitrary system operation may follow a coarse branch only if it does not
access retained fine paths or erase distinctions in past history. E has two
terminal amplitude channels; R has four, with HIGH grouping paths 1,2,3.
No direct source header is used as an observed channel.

The external decoder-source comparison uses the fixed site-to-phase transport
`beta=(0,1,3,4,2)` from `(Y0,...,Y4)`. It is separate from the circuit input
law and recovers LOW energy `(sum z)^2/20` at k=2. No identity relabeling or
source-specific target selection is permitted. G02 checks the four source
basis vectors and all sixteen full/LOW energy polars under this transport.

The test inputs are mathematical exact bases and disclosed controls: all
settings, both variants, all first and second binary branches, all ordered
two-setting/variant pairs, zero, simplex vectors and cycle-opposite differences.
Mixer controls use all 24 group orders, all 16 signed columns and rational
rotation parameters -2,-1/3,1/2,3 in separate finite control families.
Their finite audit is not an enumeration of the universal completion class.
Record fixtures and their immutable context are specified in RECORD-CONTRACT.
No new empirical source, calibration, archive, laboratory record or NIST tail
is an input. Existing NIST measurements do not identify this circuit.

## 4. Systematics and independent audit

The direct implementation performs path mixing and cell routing without P/Q.
The independent reference uses 5x5 `P_k=(5/4)u_k u_k^T`, its complement on V,
the alternating projector and the four-term group twirl. Complete maps, not
only the two familiar scalar contrasts, must agree on the full operator basis.
Both stages are also fed directly through the circuit on all four system
basis vectors, retaining every ordered fine-channel history.

Confounders explicitly excluded from positive inference are: treating I_5 as
identity on V when taking ranks; confusing the two rational basis metrics;
discarding fine paths and then coherently summing their amplitudes; confusing
intensity equality with full-state equality; retrofitting a mixer, setting,
flag rule or post-state map; treating finite controls as an infinite proof;
or counting stored amplitudes, energy ledger and threshold counts repeatedly.

Prior registered stabilizer averages, four pure affine alternatives, generic
dilation existence and general reservoir accounting are dependencies or
boundaries, not newly discovered results. The mixed R control is outside the
prior pure single-Kraus class. The additional physical choice of coherent
uncompute is not deduced from existence, involution, terminality or J alone.

## 5. Exact gates and failure threshold

Tolerance is exactly zero. All gates are required, with no fallback scope.

| Gate | Required decision |
|---|---|
| G01_FULL_CIRCUIT | All k: full 40-coordinate orthogonality/inverse, V fourth power, F and E involutions, denominator dividing 16; all 32 restricted ambient bases remain zero-sum |
| G02_PREPARED_COMPLETE_SYSTEM_MAPS | Actual E/R prepared outputs and all sixteen system-operator basis maps equal independent five-cell formulas; ranks 1/1/2, spectral identities, branch idempotence, cross-zero, completeness and fixed beta source-comparison polars |
| G03_ALL_TWO_STAGE_MAPS | All ordered k,l and E/R pairs, all four binary histories: whole composed maps equal independent references; actual serial circuit agrees on the entire V basis |
| G04_DISCRIMINATING_PREPARATIONS | All k: 0 vs 5/16 and 5/8 vs 5/16; all j!=k: 15/16 first HIGH, joint 225/256 vs 75/256 and conditional 15/16 vs 5/16 |
| G05_BALANCED_CLASS_AUDIT | Complete-map invariance in each declared finite mixer control; universal conclusion must separately survive the algebraic proof |
| G06_LATTICES_AND_POLYNOMIAL | H-conjugacy to integral controlled permutations, path-projection obstruction, all distinct-setting reflection planes and exact polynomial 4lambda^2+7lambda+4; nonintegrality conclusion by proof |
| G07_ZERO_AND_VALIDATION | Exact zero outputs; malformed setting, vector, variant or group order rejected |
| G08_RECORD_MODEL | Strict call to the independent record auditor; complete energy, lifetime ordinal, archive/reset, read/END, phase-period, grouping and ambiguity controls in RECORD-CONTRACT |

An exact mathematical counterexample or map mismatch is SCIENTIFIC-FIRED at
this frozen scope and must be retained. An unproven universal step is not
rescued by finite PASS rows. Missing reservation/pin/readback, changed source,
missing file, error, stderr, nonzero exit, or architecture byte mismatch is
STOP (or a later ABANDONED-PIN disposition when applicable), not a physical
negative conclusion. No apparatus-wide or Born falsifier is registered here.

## 6. Layer, remaining debt and formal sequence

Conditional mathematical L4 apparatus/support only, matching the inherited
apparatus claims. The supportive finite record protocol supplies no realized
L5 stream, physical reset, source identification, probability measure or
L6 law. There is no new L1-to-L4 or L4-to-L5 gate and no claim that the
circuit is induced by Omega,U. Physical carrier, calibrated implementation,
energy scales, pointer occurrence, full family equality and all relevant
QDD owner obligations remain unresolved. `feeds_U=false`.

Formal sequence: the authority/collision scan and issue 854 reservation
precede this pin. Commit and push the reviewed seven-file content, record and
read back its exact public bytes, then run once on Ubuntu 24.04.3 LTS under
WSL2 with CPython 3.12.3, x86_64, from the repository root. Set LC_ALL=C,
LANG=C, TZ=UTC, PYTHONHASHSEED=0 and PYTHONDONTWRITEBYTECODE=1; capture raw
stdout, stderr and exit code without a shell text conversion. Preserve real
EXPECTED and neutral RUN metadata, then require both architecture replays
and one-probe PR review. No post-pin rewrite, renamed failed pin or threshold
change is allowed. Any canonical T or other status would require a later
separate reviewed fold. This preregistration claims no passed gate or promotion.
