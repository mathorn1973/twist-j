# Exact finite-center source bridge: frozen audit contract

**PUBLIC-source, NON-CANONICAL; no authority.**
Candidate: C-PHOTON-U1-FINITE-CENTER-N. Owner issue: #1715.
Owner: A. M. Thorn / Codex-20261023-u1-finite-center.
Date: 2026-10-23. Original work: Apache-2.0.

## 1. Authority, attribution and scope

Public authority is Canon v104, main/tag activation
`e6240e2689bb22aab5f02bad90b75d3692bb96d9`, content
`4a50e527d20018839f006ed312454b710e6486b4`. STATUS was read first;
POLICY and AGENTS govern. All five normative hashes and required checks
were verified and the unchanged main reread before this item was claimed.
The declared CANON has 1262204 bytes and SHA-256
`c8d0cfadb44cf882af9f8ac303ba558b232663451d634d99467ce6d2c4a6814d`.

One notes-only scope: finite-volume mathematical L4 action/source identities
and explicitly selected finite normalized measures. Their prospective L6
thermodynamic interpretation remains conditional and unadopted. No physical
carrier or native-U derivation, canonical phase, continuum, photon,
polarization, SI, or Z5 phase conclusion is included.

Collision scan covered 278 actual remote heads, current notes/probes/registry,
the exact candidate identifier and photon issues. The local incidence bound
is inherited from `notes/C-CURRENT-PRIME-GATE-N/PROOF.md` (#1196), not new.
#1111 owns binary pairs, #1119 charge-five U(1) Wilson sector ratios,
#1217 the Z5 seam-source relation, and #1116 the unexecuted Z5 axis test.
Their files, owners, pins and thresholds remain untouched.

## 2. Complete mathematical contract

Let B be an integer face-to-edge boundary matrix of a finite cell complex.
All edges are integrated with normalized Haar measure, no fixed boundary
links and no gauge quotient. For G=U(1) or the Nth roots of unity, define

    Z_G[a,J] = E_A exp(i<J,A>) product_p [2+2cos((dA)_p+a_p)],

where a is any real face cochain and J any integer edge cochain. Equality
means literal equality of these finite source functions, with the same B,
a, J, orientations and normalized measures. J=0 is the partition function;
J!=0 is an inserted numerator, not automatically the same observable class.

The Fourier coefficients are c_0=2, c_1=c_-1=1. Character integration
selects Bn+J=0 for U(1) and Bn+J=0 modulo N for Z_N, with n in {-1,0,1}^P.
The sufficient bound is N > max_e(sum_p |B_ep|+|J_e|).
In ordinary four-dimensional cubical boxes and periodic tori L_mu>=2,
sum_p|B_ep|<=6. All integer-closed cycles, including winding cycles,
remain in the sum. We assert exact equality for N>=7 at J=0, and for
N>=8 for all currents with ||J||_infinity<=1. No primal-field bijection,
arbitrary link-observable equivalence, or smaller-group equality is asserted.

### Known analytical sharpness witnesses, exposed before execution

On an even four-torus L>=4 let s(x)=(-1)^(x_1+x_2+x_3) and j_0(x)=s(x),
j_nu=0 for nu>0. For N=2,...,6 choose the lexicographically first triple
(a_1,a_2,a_3) in {0,1,2}^3 of sum N, put

    f_0(s)=0, f_1(s)=(1+s)/2, f_2(s)=s,
    n_(0,nu)(x)=f_(a_nu)(s(x)), other n=0.

The proposed exact facts are Bn=N j, boundary j=0, and
|supp n|=N L^4/2. Positive character weights then give Z_N[0,0]>Z_U1[0,0].
For N=6's n and inserted J=j, Bn+J=7j: Z7 and U1 inserted numerators
differ although the denominators agree. This is a product of winding-loop
characters, not a counterexample for one simple contractible Wilson loop.

### Flux and topology contract

On a periodic torus choose orientation mu<nu. A source stack has value one
on mu,nu plaquettes with x_mu=x_nu=0 and zero elsewhere. For integer-closed
n, W=<n,stack> is integer, independent of the stack position, and

    sum_x n_(mu,nu)(x) = L_mu L_nu W.

Thus stack source alpha and uniform source alpha/(L_mu L_nu) give the same
partition function, for all real alpha, in U1 and Z_N with N>=7. Define
F(alpha)=-log[Z(alpha)/Z(0)] near zero. The proposed identity is
F''(0)=Var(W). It is a finite identity, not a uniform positive limit bound.
Local cube-boundary updates preserve W; flat primal holonomy updates
preserve plaquettes and do not certify magnetic-sector mixing.

### Exact bounded Z7 source-Hessian reader

Let x=2cos(2pi/7), with x^3+x^2-2x-1=0 and 1<x<3/2. Use Q(x), represented
by exact rational triples in basis (1,x,x^2), at this specified real root.

    weights at 0,+/-1,+/-2,+/-3: 4, 2+x, x^2, 3-x-x^2;
    r=(2-x)/(2+x);
    G(0)=0, G(+/-1)=+/-1,
    G(+/-2)=+/-(2+x)/x, G(+/-3)=+/-(1+x)/(x-1).

The physical score for this source is X=sqrt(r)G. For one orientation,
with A=L_mu L_nu, the uniform-source estimator is

    H = [V/2 + (r/2) sum_x G(f_x)^2 - r(sum_x G(f_x))^2]/A^2.

The full finite Z7 expectation of H must equal F''(0). The negative term
is essential. H itself need not be positive. Use the true plaquette curls
f=dA modulo seven, not independent plaquettes except in the explicitly
proved two-dimensional constrained-plaquette test. The sampler's finite
irreducibility does not certify practical mixing or thermodynamic limits.

## 3. Frozen finite audit A

No new scientific program has run. Formulas above and in the preceding
conversation are exposed analytical predictions. Code independence does
not mean blindness to those predictions.

Primary `verify.py` may import only the new `z7_exact.py` and the standard
library. Independent `break.py` must not read either implementation or
their output before its own source is frozen. It uses a separately written
cyclotomic Q[z]/(1+z+...+z^6) implementation for the algebraic comparisons.
Both sources and this contract must be committed, pushed and publicly read
back before either scientific run or cross-comparison. Static AST parsing
and compilation are permitted before that pin.

The following finite tests are fixed, not selected from their outputs:

1. Enumerate all incidence words in {-1,0,1}^m for m=0,...,6. Compare
   integer-zero selection with modulo N for N=7,8,13. Retain modulo-five
   and modulo-six local alias counts as controls, without calling local
   counts a full-lattice probability.
2. Build the actual oriented four-torus incidence at L=4 and 6. Check
   every edge of the N=2,...,6 witnesses, every vertex's current conservation,
   every support count, and the separate inserted-current N7 witness.
3. Construct the six fundamental wrapping sheets at L=4, check closure,
   all stack positions and uniform pairing. Check elementary cube boundaries
   have zero winding. A restriction to only boundaries must fail the 2D
   nonzero-winding control below.
4. In Q(x), independently audit the minimal polynomial, seven weights,
   all score identities, exact positivity, and all 924 weak compositions
   c_0+...+c_6=6. For each, compute all seven conditional masses
   M_a=product_(k=0)^6 w_(a+k mod7)^c_k. Normalize with their exact sum.
   Every mass must be strictly positive. No decimal categorical decisions.
5. Enumerate all 7^(A-1) plaquette assignments on the 2D periodic 2x2 and
   3x2 tori (A=4 and 6), with the last plaquette minus the preceding sum
   modulo seven. Each has the same gauge multiplicity. Exact normalized
   partition: 2^A+2. Exact mean uniform and stack source-Hessian readers:
   2/(2^A+2). One discrete stack source alpha=2pi/7 gives partition
   2^A+x, hence ratio (2^A+x)/(2^A+2). Retain the full wrapping sectors.
6. Independently enumerate ternary fields on a single three-cube boundary:
   only 0,+/-oriented boundary survive integer closure. With the original
   weight its partition is 2^6+2=66. A single plaquette disk gives 2.
7. Run an exact-operation-only primal sampler exercise at D=4, L=2 and 3,
   two sequential full sweeps from each of cold and hot starts. Seeds in
   order (L2 cold,L2 hot,L3 cold,L3 hot) are 230701,230702,230703,230704.
   Check cached curls against complete recomputation after each sweep,
   Bianchi modulo seven and exact reader serialization. Freeze zero phase
   decision weight for this exercise. It supplies no equilibrium estimate,
   thermalization, sector-weight, mass or mixing conclusion. Breaker need
   not reproduce the PRNG trajectory; it independently checks the reader
   and transition-weight algebra.

### Cross-implementation comparison bytes

Print one line per count vector in lexicographic order of (c0,...,c6), then
a=0,...,6. Each line is the compact JSON array [c_vector,a,coefficients],
where coefficients are the three integer coefficients of unnormalized M_a
in basis (1,x,x^2). No spaces, UTF-8 ASCII subset, one LF per line.
Hash the 6468 lines with SHA-256. Both implementations must derive the
coefficients; neither may import a table or the other's implementation.
Also compare exact rational partition/helicity controls and witness counts.
Ordinary stdout may differ; only the declared comparison contract is shared.

## 4. Failure and reporting rules

Exact mathematical discrepancy: preserve the witness and FAIL the specific
identity, do not adjust it. Infrastructure or code defect: STOP_INTEGRITY,
preserve the first run and use a separately identified successor execution
contract if a repair is necessary; do not overwrite a failed transcript.
Runtime budget: 180 seconds per exact audit; the operation-only sampler
exercise may run separately for 180 seconds. Timeout is STOP_RESOURCE,
not a phase result or mathematical counterexample. Empty stderr and exit
zero are required for PASS. No floating-point scientific assertion.

Record source hashes, immutable pin, commands, environment, stdout and
stderr bytes/hashes, all failures and review limitations in RUN/RESULT.
Local x86_64 checks are candidate-C only. Notes CI does not rerun these
scientific audits automatically and is not a computation-grade T gate.
Analytical proof conclusions remain candidate-T until public acceptance.

The delivered `MEASUREMENT.md` will specify the next full-measure finite-size
test and unresolved mixing/resource qualifications. This audit does not
authorize unpinned production, reinterpret #1116, or choose a phase from a
finite control. A prospective simulation needs its own complete code, fresh
seeds, sampling law, uncertainty rule, stop conditions and public readback.
