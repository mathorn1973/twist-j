# C-JM-RETAINED-PAIR-SOURCE-N: frozen construction and tests

NON-CANONICAL, L1. Owner A. M. Thorn, session jm-retained-pair-source-2026-10-20,
issue #1680. This is a mathematical source construction, not native U or a
physical apparatus. Analytical predictions below are exposed before execution.
Public basis: 5f20429944b409d912202d141e158fdfec145c41, Canon v103, content
01fb76f6b3b14a6a5ec05d0017ea922390ab6f66, Canon SHA256
d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b.
Authority files, hashes, ancestry, required checks and relevant ledger/gates
were read and checked. PR #1679 at 87485fc66140a436bd6a337dd2ff452093ab607f
is an UNMERGED candidate input. Its required definitions are restated below.
No older claim, bound, or probe is reopened. No Born occurrence is derived.

## Carrier and chosen resources

Fix integers Q>=8 and K>=1. The digital program z has eight integer entries,
0<q(z)<=Q, with b1-b2-b3=0 mod3 in z=(a0..a3,b0..b3). The seam ell z=0 mod41,
ell=(1,10,18,16,-1,-27,-32,-3), is a comparison output, not an input to the
preparation gate. Choose G=diag(5I4-ones4,4I4), G0=diag(1,G),
y=(1,z), A=y^T G0 y=1+q(z), rho_z=y y^T G0/A. Program labels are orthogonal
classical controls; the reader has no access to them. The program is held.
No initial law on z is selected. Any supplied diagonal distribution pi is
allowed; offdiagonal program coherences have only the complete unitary scope.

One output cell has dimension9 with metric G0. One pair cell has dimension81
with metric L=G0 tensor G0 and common pure ready vector e=e0 tensor e0.
Initial purity/readiness, a reference coordinate, exact rational controlled
couplings, swaps, counter and finite capacity are supplied resources. They
are not derived from J, q is not physical energy, and probability norm is
not a thermodynamic energy account. No field-normalization roots are allowed
in executable arithmetic. Real/complex scalar extension is only the adopted
quantum comparison. Equality is literal vector/operator equality in fixed
coordinates; no source-dependent physical equality is imposed.

## Frozen construction

1. Pair synthesizer. For admitted z put w=y tensor y, v=A e-w,
d=A(A-1), r=L v=A e-(G0 y tensor G0 y),

    U_z=I-v r^T/d,  N_z=d I-v r^T.

Predict: v^T L v=2d; U_z^2=I; U_z^T L U_z=L; U_z e=w/A. Its normalized pure
output density is exactly rho_z tensor rho_z. No postselection or precomputed
Born probability is used. source.py must compute the full rational operation,
not merely print the desired density. Invalid programs use identity, with
NO_ADMITTED_OUTPUT semantics. The branch A=1 never divides by zero.

Integer certificates: N_z^2=d^2 I and N_z^T L N_z=d^2 L. All coefficients
are integers before division. Rational vectors are exactly encoded by integers
and a positive common denominator; a fixed-program stable lattice exists as
Lambda_z=Z^81+U_z Z^81, with U_z Lambda_z=Lambda_z. This compiled lattice is
not R and not a claim of one common integral lattice across program changes.

2. Pair parity boundary. A rational unit vector on the ray y^(tensor k)
exists iff A^k is a rational square. Thus for nonsquare A and no residual
program-dependent auxiliary output, odd k cannot be prepared from a rational
unit ready vector by a rational isometry. k=2 always works. Retaining an
unread partner permits delivery of an odd requested number of copies. No
minimal-ancilla claim outside this clean rational class.

3. Occupied-port continuation. The full carrier is digital program z, integer
counter n in Z, output pair P, K pair cells B0..B(K-1), and any spectator/
measurement record. On a tick with admitted z and 0<=n<K, apply U_z to B_n,
then SWAP(P,B_n); increment n. Outside that interval, act as identity on data
and increment n. This is one total reversible law, not an absorbing finite
halt. The inverse decrements n, then undoes the swap and U_z at the recovered
address. The unbounded counter is explicit, even though the supply is finite.

Supported start: n=0; every B_i is the SAME program-independent e and is
uncorrelated with the rest; P may be arbitrary and entangled with retained
spectators. For each fixed classical z, one round outputs rho_z^tensor2 and
moves the complete old port state and its correlations into B_n, unchanged.
Earlier archive cells are untouched. After K rounds exactly2K fresh copies
have been generated, the K stock cells archive successive old ports, and
no further output is claimed. Dirty stock is not silently reset or certified
by an occupancy label: the complete map is still reversible but fresh-output
guarantees require the stated initial ready bank.

4. HOLD consequence. With any classical program law pi, retaining emitted
pairs gives sum pi_z rho_z^tensor(2K). Using k<=2K outputs and keeping all
unused partners in the full state gives HOLD_k. Instruments applied to older
outputs do not change the next prepared pair conditional on z. Conditional
probabilities of those instruments remain the adopted Born rule, not a new
occurrence mechanism. Exact digital capture is COPY(X,P)=(X,P+X mod m),
m=2 floor(sqrt(Q))+1 in each coordinate. An occupied P is first swapped with
a fresh zero program archive; inverse subtraction/swap preserves old contents.
The source input X is supplied, not claimed loaded from native U.

5. Resource and reset boundaries. Each round uses one program-independent
ready pair and one archive address, implemented by the same physical pair
cell after the swap. Program and previous archives persist; arithmetic
scratch can be reversibly computed/uncomputed from the digital program.
A requested k uses ceil(k/2) pair cells and keeps one extra partner if k is
odd. Every unmeasured history is exactly undone by reversing the full law;
postmeasurement reset requires the measurement apparatus and records or a
new ready resource. A unitary reset of an arbitrary D-dimensional port to a
fixed pure output must move its old distinguishability to an environment of
dimension at least D. SWAP with one pair archive attains D=81 here. No
physical pulse/thermal cost or nondegenerate energy Hamiltonian is supplied.

## Failure thresholds and finite tests

Any exact counterexample to a displayed identity or supported-domain forward/
inverse, old-record preservation, HOLD factorization or resource boundary
fires the corresponding claim. Nonzero exit, stderr, changed code/hash or
nondeterministic output is integrity STOP until classified; never move a
threshold. No empirical data, fitted constant or float decisions.

Frozen tests: all admitted nonzero ternary z with q<=32 for rank-one integer
certificates and ready-vector identity; full matrices for z=e1, z=(1,0,0,0,
-1,0,0,0), t times that vector for t=40,41,42, and a dense admitted z; compare
partial traces and product density exactly. Test all81 occupied port basis
states on a sparse-program example, one explicitly correlated old-port/
spectator vector, three consecutive occupied-port rounds and their full
inverse, negative/after-capacity counters, invalid programs, and dirty stock
as a negative control. An integer dense-matrix computation independent of the
rank-one action audits selected full N_z certificates in the same session.
Audit the loader and inverse on complete small modular registers and named
occupied inputs. Confirm the q=4,A=5 odd-copy obstruction and pair solution;
check fixed-program lattice generators swap under U_z. A mixed-source control
must recover the two-copy reference gap15936/1210262180216419 from PREPARED
pair vectors, not import a probability generator.

All programs use Python stdlib ints/Fraction. One x86_64 run is planned, not
blind independent-agent or two-architecture confirmation. Pin these files
and source.py/verify.py publicly before execution. Produce actual stdout,
RUN, proof, result and PROMO. Ordinary notes-only CI does not execute them.

## External context (not imported algorithms)

Householder pure-state preparation is established mathematics: Ivanov,
Kyoseva, Vitanov, Phys. Rev. A74,022323 (2006), DOI10.1103/PhysRevA.74.022323.
The rational pair formula, complete integer certificates and finite resource
contract are proved directly. Wootters-Zurek, Nature299,802-803 (1982),
DOI10.1038/299802a0 supplies comparison context for unknown-state no-cloning.
Neither source supplies a native TWIST-J mechanism or physical resource budget.
New original code/text follows repository Apache-2.0; no vendored source.
