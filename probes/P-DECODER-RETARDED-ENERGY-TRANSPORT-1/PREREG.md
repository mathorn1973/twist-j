# P-DECODER-RETARDED-ENERGY-TRANSPORT-1 preregistration

**FROZEN TARGET / NO FORMAL RUN AT PIN / PUBLIC STATUS NONE.**

Disclosure: **CHOICE-EXPLICIT / QDD-NORM-EXPOSED / PROOF-FIRST / L1 ONLY**.

```text
owner: A. M. Thorn
issue: https://github.com/mathorn1973/twist-j/issues/822
base: 2d33c38fc0e9a4cfb0e60062eb8d628d46ea9e97
authority: ACTIVE Public Canon v76
branch: probe/P-DECODER-RETARDED-ENERGY-TRANSPORT-1
claim: DECODER-RETARDED-LOCAL-ENERGY-TRANSPORT
formal runs at pin: 0
public status: NONE
```

## 1. Equation and sole target claim

Adopt the already selected flat D3 scalar operator `L` at F0=1, with every
vector in shells of squared norms `(2,4,8,10,16)`, weights `(6,1,15,1,1)`
and coefficient `c=w/324`. The total degree is `8/9`. On rational fields of
finite support, use the ordered pair `(u,v)=(previous,current)` and the
forced recurrence `w=2v-u-Lv+f`. The free rule has `f=0`.

The one proposed claim is the conjunction of the following conditional
mathematical statements, at exactly the chosen scope of CONTRACT.md:

1. The retarded solution from ready `(0,0)` exists uniquely at every finite
   cut. With `H=2I-L`, `G_r=sum_j (-1)^j binom(r-j,j)H^(r-2j)`, the current
   after n forced steps is `sum_(s=0)^(n-1) G_(n-1-s) f_s`. Support grows by
   at most the corresponding finite stencil Minkowski sums including zero.
2. `E(u,v)=||v-u||^2/2+<u,Lv>/2` is the sum of the nonnegative local density
   `e_x=5(v_x-u_x)^2/18 + sum_y c_xy[(v_y-u_x)^2+(u_y-v_x)^2]/8`.
   On finite supports, `E=0 iff u=v=0`. Free steps preserve E; forced steps
   change it by `<w-u,f>/2`.
3. The explicitly fixed antisymmetric current in PROOF.md section 3 gives
   `e_x(v,w)-e_x(u,v)+sum_y J_xy=(w_x-u_x)f_x/2`. Every finite aperture
   obeys the corresponding change plus outgoing flux equals signed work.
   Reading uses the aperture plus one stencil neighborhood of completed
   slices, with the declared overlap and zero rules.
4. At the five marked sites `(000),(110),(101),(011),(200)`, inject
   `(a,0)-(sum a)/5*1` for any `a in Q^4`. Its squared norm equals
   `m(a)=sum a_i^2-(sum a_i)^2/5`, and its zero fibre is exactly zero.
   From post-kick pair `(0,S(a))`, every free cut has `2E=m(a)` and every
   finite aperture has `0<=2E_R<=m(a)`.
5. The exact passive readout and immutable histories are well-defined on
   the generated compatible carriers. Histories agree under finite prefix
   restriction; the reader depends on actual local wave values, has no
   source-header reconstruction, no future-wave input and no feedback into
   the recurrence or autonomous U.

PROOF.md supplies a uniform proof, not an inference from a finite sample.
All clauses are required. This is not the complete physical decoder, a
uniqueness theorem for choices, or a physical source/photon/detector law.

## 2. Accepted code

The only scientific program is `verify.py` with same-directory dependencies
`transport.py` and `audit_transport.py`. It also checks the frozen byte hashes
of those dependencies and of `PROOF.md` and `CONTRACT.md`. The verifier's own
hash and all six other source-file hashes are recorded against the public
commit before execution. `README.md` and this preregistration are source
documents, not runtime scientific inputs. Accepted source files are exactly:

```text
PREREG.md  PROOF.md  CONTRACT.md  README.md
transport.py  audit_transport.py  verify.py
```

Only the Python standard library is used. Arithmetic is exact integer or
Fraction; no float, random seed, external data, subprocess, network, system
time or outcome target enters a scientific map. The audit independently
constructs signed shell permutations, pointwise recurrence, mixed energy and
the natural current plus redistribution. It does not infer correctness from
comparing a function to itself. The CLI serializes the same mathematical
records and is not a separate scientific gate.

Compile/AST/byte inspections are allowed before the pin. Neither the source
module nor the audit is imported or scientifically executed until the complete
candidate is committed, pushed and its exact bytes read back publicly. The
first formal command, from a clean Linux checkout of that pin, is:

```text
python3 probes/P-DECODER-RETARDED-ENERGY-TRANSPORT-1/verify.py
```

## 3. Carrier and finite audit set

The full carrier is `C_c(D3,Q)^2`, not a periodic finite box or every complex
field on D3. Fields are sorted distinct site/Fraction tuples with zeros
omitted. Apertures are finite sorted distinct site tuples, including empty.
Source domain is all Q^4; the balanced 625 QDD heads are a subset. Stored
records, equality, preparation and time slots are fixed in CONTRACT.md.

The exact finite audit is frozen in the accepted code. Its required gates are:

```text
G01_STENCIL       complete signed-permutation shells, symmetry, counts,
                  degree and halo
G02_SOURCE        all 625 balanced QDD vectors and declared rational vectors;
                  source norm, coefficient recovery and preparation energy
G03_ENERGY        zero, unit impulse and rational two-site pairs;
                  independent mixed energy, positive density sum and one free step
G04_LOCAL_BALANCE independent recurrence/current, antisymmetry, signed forcing,
                  every singleton in the declared active halo and aperture balance
G05_RETARDED      explicit Green polynomial versus successive forced steps;
                  finite-support and translated-impulse/prefix checks
G06_APERTURES     two-site rational pair, fixed disjoint/overlapping/empty/far
                  apertures, reading and balance invariance outside the footprint
G07_PREFIX        zero, unit and (1/2,-2,1,-1/3) sources; fixed three-site aperture;
                  lengths 0,1,2,3, manual continuation, append and frozen records
G08_TYPES         explicit invalid exact types, sites, fields, apertures, source
                  sizes, ages, prefix lengths and gapped/duplicate/changed contexts
G09_BOUNDARIES    naive amplitude norm is not energy; density has a one-hop halo;
                  corrupted update gives nonzero residual; reader dependency audit
```

No finite spatial bounding box is substituted for the wave carrier: audit
support sets include every nonzero value and the required energy halo. There
is no tolerance, sampling distribution, fit or data-dependent gate selection.

For explicit case identification, write `o=(0,0,0)`, `p=(1,1,0)`,
`q=(2,0,0)` and `z=(40,0,0)`. G02 supplements all625 balanced vectors with
`(1/2,-2/3,0,5/7)`, `(1/3,1/3,1/3,1/3)` and `(-7/5,0,2/9,4/11)`.
G03 pairs are zero, `(0,delta_o)` and
`(delta_o/2-delta_p/3,-2delta_o/5+3delta_p/7)`; the next slice is checked
against independent pointwise recurrence. G04 uses pairs zero and
`(delta_o/2,2delta_p/3)`, each with forcing `delta_o/3-2delta_q/5`.
Its regions are empty, `{o}`, `{o,p}`, `{q,z}`, `{o,p,q}` and the full
active halo; singleton balances cover that halo and current checks use
all60 offsets from each of o,p in both orientations, plus self/far nonedges.
G05 uses forcing `(delta_o,delta_p/2-delta_q/3,-delta_o)`, all prefixes
through three steps and recursive Green ages0..3 on the first two forces,
also translated by z. Replacing the last force by `7delta_z/9` tests that
earlier records do not change. Exact inputs and invalid cases in G06--G09
are enumerated literally in verify.py.

## 4. Systematics and explicit choices

The degree, energy factors and current signs use directed edge sums counting
each unoriented edge twice. Aperture boundaries and one-hop halo are literal;
the wave is neither cropped nor renormalized to the aperture. Time labels
distinguish ready from post-kick cut zero and pair energy from a completed
transition's flux. Source work is signed. Equal-slice constants on a periodic
carrier are outside the strict positive-energy claim; uniform amplitude-norm
coercivity is not claimed even on finite supports.

The centered source, five marked sites, one kick, exact finite-support domain,
energy-density/current representative, unit gain, fixed aperture, zero tag
and immutable passive history are explicit choices. The source was selected
with its QDD norm match exposed. It is not blind evidence or a certificate of
physical target independence. QDD LOW/HIGH weights, five-cell A-bank counts,
spatial energy and signed current remain distinct interfaces. No completed
probe is modified, resumed or recycled.

## 5. Failure threshold and terminal procedure

Threshold: **zero exceptions and exact equality**. One failed required clause
or any G01--G09 fires the sole claim. Assertion failures produce a completed
SCIENTIFIC-FIRED record, exit zero and exact stdout; such a result is preserved
and merged. Unexpected execution error, integrity failure or a run producing
no completed record disposes this identifier under the abandoned-pin rule.
Never edit the frozen sources, scope, choices, cases or thresholds to rescue
a result. A correction requires a new named probe and new preregistration.

Record exact stdout as EXPECTED.txt and neutral environment, pin, hashes,
byte counts and exit code in RUN.md. The public required workflow reruns the
unchanged verifier and compares exact bytes on its required architectures.
RESULT.md distinguishes proof scope, finite checks and architecture evidence.
Only an earned subsequent Canon fold may register a public claim.

## 6. Action layer and unchanged physical obligations

**L1 only: encoded mathematical conformance, propagation and local reading.**
This probe adds no passed L1-to-physical or L6 gate. Physical source/coupling,
photon interpretation, detector/post-state/absorption, calibration, occurrence,
apparatus class completeness, Born frequency, Bell accounting and L6 measure
remain unresolved. Positivity does not turn a scalar functional into a physical
effect or probability; summing passive readings through time is not absorption
or a count of distinct events.

Definition lane #539 remains STOP; #744's pole/polarization/normalization
requirements remain open; #756 retains F3 NOT_SATISFIED and production #742
FORBIDDEN. COINCIDENCE-RECORD-FREQUENCY remains UNTESTED / STOP. No photon
ensemble or production route is executed. **PUBLIC CLAIMS UNREGISTERED /
CANON UNCHANGED.**
