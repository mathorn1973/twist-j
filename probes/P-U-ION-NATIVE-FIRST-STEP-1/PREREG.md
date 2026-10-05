# P-U-ION-NATIVE-FIRST-STEP-1: prospective exact audit

**NON-CANONICAL, conditional ideal-model construction; L1 operator/state
audit.** Reservation [#1368](https://github.com/mathorn1973/twist-j/issues/1368).
No public scientific status or physical occurrence/measurement lift is
requested. Canon v97 remains authoritative. This document, both verifiers
and all scientific support files must be publicly pinned and byte-read back
before the first scientific execution. Static parsing and proof review are
allowed beforehand; importing or executing either verifier is not.

## 1. Frozen equation and target domain

The task is one complete first native step on the actual post-first-contact
family of #1367. It is not a general six-coordinate selector or a complete
preparation-to-nine apparatus. Keep the fixed dictionary of #1363, the
fourteen original data factors, two counted memory ions M1,M2 and one finite
counter ion N. The exact index order is

```text
0 S1; 1 S2; 2..7 R1=(p1,p4,p1p,p4p,q,r);
8..13 R2=(p1,p4,p1p,p4p,y,r); 14 M1; 15 M2; 16 N.
```

For every s,t in F5, the input and complete required output are

```text
I(s,t)=(S1=1,S2=t,R1=(0,0,0,0,s,0),R2=0^6,M1=0,M2=0,N=0),
O(s,t)=(S1=1,S2=t,R1=f(s),R2=(0,0,0,0,3,0),M1=s,M2=1,N=1),

f(0)=(0,0,0,0,0,0), f(1)=(0,0,0,0,4,0),
f(2)=(2,1,2,1,4,0), f(3)=f(4)=(2,1,3,4,3,1).
```

The target is U|I(s,t)>=Gamma|O(s,t)> in the declared interaction frame,
with one explicitly derived scalar Gamma independent of s,t. Linearity
therefore preserves coherence of this complete 25-dimensional subspace
and its correlations with an untouched reference. MODEL.md declares the
additional known laboratory phases. Success concerns every data coordinate,
both memory outputs and the counter, without postselection or coarse-reader
substitution. The occupied memory is not reset.

The mathematical target follows by the actual selectors at theta_0=0:
j1=s and j2=1. Neither s nor t nor a history label is an external program
input. The same finite physical instruction sequence is executed for all
25 preparations. M1,M2 and N are prepared and counted before the first
contact; this probe does not certify that preceding physical preparation
or contact embedding. The supplied post-contact family is its input domain.

## 2. Frozen carrier and physical-control class

MODEL.md and SOURCES.md define the fixed Ca40 S+4D levels, global diagonal
LS force, single ideal COM mode, individual resonant 729nm star carriers,
geometry and intensity admission, inherited-state and phase conventions.
These files are part of the accepted input, not optional commentary.

The Hamiltonian is a documented interaction type extended to the explicitly
adopted seventeen-ion effective model. No measured seventeen-ion device or
calibrated parameter/error box is claimed. Individual carrier addressing is
newly admitted and source-supported; pair-selective LS light is not assumed.
There are no independently adjustable five light shifts, arbitrary U(5)
gates, native controlled gates, SWAP primitives, fresh resets or incompatible
imported BSB operations in the instruction set.

Fix eta, delta>0, finite complex geometric/coupling factors c_i, one real
nonscalar profile d, B=5 sum(d_j^2)-(sum d_j)^2>0, finite lambda_max and
resolved positive carrier rates Omega_(i,j). On each of the six required
edges {14,k}, k=2,...,7, require g_e=Re(c_i conjugate(c_j)) nonzero and
lambda_e=delta/[eta sqrt(50B|g_e|)]<=lambda_max. These are independently
admitted model conditions, not fitted measurements. The only LS variation
is a common intensity scale chosen from these six fixed values.

Each loop has duration 2pi/delta. Its ideal motion endpoint is identity
on the untruncated oscillator, including inherited correlations. The
separately chosen comparison domain for a prospective physical-error claim
is input Fock support 0,...,10; actual preparation into that domain, the
whole-force Lamb-Dicke bound and all neglected modes remain physical debts.

## 3. Frozen synthesis algorithm

For each required unordered edge e, assign both active ions direction
(1,0,0) in F5^3. Enumerate lexicographically the 31 nonzero vectors whose
first nonzero coordinate is 1, remove (1,0,0), and assign the first fifteen
remaining directions to spectator ions in ascending index order.

The equality echo G_e comprises 500 framed global LS loops, in lexicographic
order (a,u), a=1,...,4, u in {0,...,4}^3. Before each loop implement on ion i
the monomial with label permutation p_i(x)=a*x+v_i dot u. Implement these
frames in ascending ion order, execute the full loop, then reverse all
frames in reverse ion and pulse order using true adjoints. The resulting
operator is Gamma_e exp[-i sign(g_e)pi E_e/2] tensor I_spectators; the
full scalar formula is frozen in PROOF.md. Each local stationary residual
loop profile is twirled to a scalar; carrier imperfections are not thereby
cancelled or declared physically zero.

The primary's canonical star compiler follows disjoint cycles, starting each
at its smallest unvisited label. A nontrivial cycle containing zero is
(0,a1,...,aL) and gives the chronological star list a1,...,aL. A cycle
(a1,...,aL) not containing zero gives a1,...,aL,a1. Singleton cycles give
no pulse. Every star is Rx_(0,j)(pi); an adjoint reverses the list and uses
Rx_(0,j)(-pi), implemented by a pi phase shift. The emitted objects are
monomials with their actual phases, not unphased abstract permutations.

Normalize only the analytically accounted global Gamma_e in the exact
matrix audit. Z_e=G_e^2 then has equal-label entry -1 and unequal entry +1
for either sign(g_e). For a control label j and target transition (0,k),
choose b,c as the two smallest labels different from j. Use the three masks
{j,b}, {j,c}, {b,c}, with beta=pi/4, pi/4, -pi/4 respectively. For each
mask its sorted two labels map to (0,k), and the remaining labels map in
ascending order to the remaining outputs. Compile that control monomial P.
The chronological mask is

```text
P_control; G_e; G_e; Ry_target(-beta); G_e; G_e;
Ry_target(+beta); P_control^dagger.
```

Thus every controlled Ry(pi) consists of twelve equality echoes plus
compiled control frames and six ordinary target star rotations. It is a
derived word, not a primitive. All rotations have explicitly specified
phases and finite positive durations.

The whole program is fixed chronologically:

1. For k=1,2,3,4: C_(R1.q=k)Ry_(M1;0,k)(pi), then
   C_(M1=k)Ry_(R1.q;0,k)(pi).
2. For j=1,2,3,4 and then each R1 coordinate in its index order: if the
   fixed design-table value f(j) is k!=0, execute C_(M1=j)Ry_(coordinate;0,k)(pi).
   The program contains all eighteen such blocks for every input; there is
   no software branch reading j from the original source label.
3. On M1 execute Rx_(0,k)(2pi) for k=1,2,3,4.
4. Execute Ry_(R2.y;0,3)(pi), Ry_(M2;0,1)(pi), Ry_(N;0,1)(pi).

The first eight controlled rotations transfer the current physical q label
to M1, with a known sign. The four 2pi pulses remove that sign. Sources
and other coordinates have their explicitly stated outputs.

## 4. Exact audits and independent implementation

verify.py is newly written with Python standard-library exact arithmetic in
Q(zeta_16), zeta_16^8=-1. It imports no predecessor scientific program.
It binds INPUTS.json by its embedded SHA-256; the manifest binds all seven
scientific support files by byte count and SHA-256. Git binds the primary
and manifest themselves, avoiding a self-hash cycle.

The primary must verify:

- all twenty affine monomial compilations, exact phases and true inverses;
- all six edge layouts, scalar spectator coefficient identities and the
  500-loop active-pair identities for all 25 label pairs, including all
  local-profile coverage; no numerical d or c_i substitution replaces this;
- all 500 distinct two-ion columns of the twenty controlled rotations,
  for both geometric signs, including false controls and target levels
  outside (0,k), with exact Q(zeta_16) arithmetic;
- all 25 complete seventeen-register input/output columns and their
  inverses, original native selector/generator agreement, unchanged
  source ports, physical counter, and distinct M1 for s=3 versus s=4;
- the derived primitive counts, positive angle budget and common schedule;
- the same-waiting omitted-LS control: every echo replaced by identity,
  carrier schedule retained, exactly five of 25 complete targets succeed
  (s=0, all t). Analytically every controlled word then cancels to identity.

The independent verifier is authored separately without reading the primary
implementation. It has separate exact arithmetic and permutation compilation,
checks the same finite identities and full input family, and emits compact
JSON with status PASS and matching actual_inputs=25, crot_columns=500,
echo_rows=500, ls_loops=156000 and omitted_ls_success=5. Its own compilation
counts need not equal the canonical primary count; only primary counts are
published as the declared program. No primary helper is imported by the
independent implementation. The primary invokes it with a 300-second
timeout, requires exit zero, empty stderr and those exact shared fields,
and records the SHA-256 of its actual stdout.

Operatorial motion closure and the global scalar derivation are analytical
proof obligations, not numerical finite-Fock simulations. Finite coefficient
checks audit that proof; they do not validate eliminated levels, omitted
modes or physical errors. The verifiers need not materialize 5^17 amplitudes
or millions of repeated pulses: complete elementary identities, the fixed
finite compiler and their exact composition establish the stated subspace
action. This structured representation is the complete word, not an
unconstrained existence oracle.

## 5. Pre-run expectations, resources and failure rule

Analytical expectations disclosed before execution: 26 controlled rotations,
312 equality echoes, 156000 global LS loops, and 61200 canonical carrier
pi pulses per equality echo. The complete frozen upper bounds are
19095499 carrier pulses, 19095386*pi total positive carrier angle and
19251500 switching-boundary intervals including both ends. The first run
will report the exact compiled total within these bounds. These large
finite counts are not claimed optimal, practical or compatible with a
small laboratory error.

PROOF.md and MODEL.md give the finite time and incident optical-energy
expressions, the retained memory and counter energies, and full-source
limitations. Preparation of the input sector and finite quantum
laser/controller/work-source dilation are not certified by classical
prescribed controls. A source experiment's short-gate fidelity is not
assigned to this word. No numerical fidelity, available battery capacity
or full-history error threshold is inferred.

Zero tolerance for every exact assertion. Any failed source scope, compiler,
phase, coefficient, state, inverse, count or independent-check assertion
rejects this candidate at its stated cause. A failed candidate is not a
no-go for all ion controls. No post-pin change of source, dictionary, word,
threshold, field arithmetic or target is allowed.

The first formal execution has an external 600-second timeout including
the independent subprocess. Record the public candidate commit, successful
byte readback, start/end, command, neutral OS/architecture/Python descriptors,
exit, stderr and output byte counts/hashes. EXPECTED.txt is created from
actual successful stdout only afterward. Preserve any failure and follow
the repository's failed/abandoned-pin disposition; never silently repair
the frozen candidate. Neutral records may be added after execution.
The required x86_64 and aarch64 PR jobs must reproduce the same verifier
and stdout bytes on one final PR head; independent static/post-run reviews
remain distinct checks. No merge or Canon promotion is included.
