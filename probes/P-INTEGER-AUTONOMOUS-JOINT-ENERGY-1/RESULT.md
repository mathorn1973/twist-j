# Result

Status: PASS  
Scope: NON-CANONICAL, L1  
Probe: P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1  
Ownership: https://github.com/mathorn1973/twist-j/issues/1649  
Pin: edfedd7e75c515d6d318032f526f381f66317da3

## Completed local gate

The first formal run completed with exit zero, empty stderr, no fired
falsifier and an exact match between the primary and separately authored
breaker's raw 768-byte, 27-line certificate. The primary appended two
terminal lines, giving the unmodified 808-byte, 29-line EXPECTED.txt:

    stdout SHA-256:
    ab1a15571a69961896471aa2212771fdf379afbc9a06837b1d4c3aa30ddad42e

The actual first run is documented in RUN.md. All six prospective files
remain unchanged from the public pin. This is a completed PASS gate,
not an abandoned or repaired pin. The two-architecture result must be
read from the actual draft PR workflow and its subsequent public receipt.

## What this construction closes

The predecessor #1648 has a counter-dependent reciprocal coupling and
a positive uncoupled-sector bond quantity with a nonzero work balance.
This successor uses the constant coupling g=1/324 and the constant
context force a/4, with a in {-1,0,1}, in one stationary joint action:

    (Delta_c^2+L)h_n = g chi_n ell,
    (Delta_c^2+1)chi_n = a/4 + g <ell,h_n>,

where ell=(1,-1,0,0,0), L=(648I-C)/324, and C has the circulant row
(460,29,65,65,29). The full quadratic metric action A2 is varied before
evaluation on its plus-TT representative. Both reduced kinetic terms
have the same positive sign. The law's coefficients do not depend on n.

Let x_n=(h_n,chi_n), let x_* be the actual coupled equilibrium at mean
sum h=1, and put z_n=x_n-x_*. The symmetric stiffness is

    K = [[L, -g ell], [-g ell^T, 1]].

The complete interaction-inclusive bond energy

    Htot_n = ||z_n-z_(n-1)||^2/2 + <z_(n-1),K z_n>/2

is exactly conserved. It is positive definite about the coupled
equilibrium on the fixed-mean two-slice space. On the unrestricted
physical space it has the constant spatial null mode and is therefore
semidefinite. PROOF.md sections 2-3 derive the equilibrium, spectral
bounds, conservation and both square completions. The result is an
exact quadratic invariant of this declared action and map; it is not
identified with native-U energy or SI energy.

The discrete Legendre map has p_n=x_n-x_(n-1) and

    p_(n+1)=p_n-K x_n+(a/4)e6,
    x_(n+1)=x_n+p_(n+1).

After equilibrium centering its type-II generating function is

    F2(z,pnew)=<z,pnew>+||pnew||^2/2+<z,Kz>/2.

This establishes a canonical physical map and a conserved alternating
form for tangent variations or commonly centered solutions, for every
fixed a. It does not assert that the bond invariant's own unit
continuous Hamiltonian flow is exactly this discrete map. An alternating
form has no positive quadratic signature. The full integer bank/monitor
carrier is not asserted to be a symplectic manifold.

## Exact integer realization and two invariants

The unrestricted 21-integer core is (Z,R,D,H), with two six-coordinate
slices Z=(P,Y), R=(Q,V), D>=1, and H in Herm_2(Z[j]), j a primitive
fifth root of unity. BOTH stored slices use the current common D.

    Z' = B Z - 324 R + 81 a D e6,
    R' = 324 Z, D' = 324 D,
    H' = M(Y'-Y) H M(Y'-Y)^dagger,

    B = [[C,ell],[ell^T,324]].

No separate history counter is stored and every coefficient is fixed.
The exact partial inverse has thirteen image divisibilities. The
Hermitian commutator M is one admitted compound gate here; its four
algebraic factors are not individually banked phases.

With the proper integer account

    E=1+D+||Z||^2+||R||^2+N(H),

a nonnegative bank and a direction flag complete the 23-coordinate
funded carrier. Domain or bank refusal reverses the direction at the
same core. PROOF.md sections 6-7 establish a total bijection

    F^-1 = Rev F Rev,

and separate conservation of E+b and the decoded Htot. F is generally
not an involution. H_c1=Y and the monitor shape hold on the prepared
family; H is an independent coordinate on the unrestricted carrier.

Finite E+b shells have finite path components and exact bounce cycles.
The sharp precision horizon is determined by the maximum cost over
the requested forward prefix, not by an assumed monotone cost at all
steps. The selected six complete cycles have least periods 2,4,2,4,2,4.

## All-counter preparation, signature and precision

The ten canonical word shapes are retained with a declared quarter
departure from their spatial mean:

    h_t = (1/5)1 + (h_t^can-(1/5)1)/4, t=0,1,
    chi_0=0, chi_1=a/4, D_1=40.

Thus initial occupied and empty field values are 11/40 and 6/40. The
source force is a/4. These changes are explicit model choices fixed
before execution. The new all-counter bound does not silently cover
the original unattenuated packet.

For all thirty prepared histories and all n>=0, the energy-ellipsoid
proof in section 5 gives

    0 < Htot_n = Htot_1 < 3/50       (bonds n>=1),
    |h_n(r)-1/5| < 9/20,
    -1/4 < h_n(r) < 13/20,
    |chi_n| < 3/4.

Consequently g_n(r)=diag(-1,1+h_n(r),1-h_n(r),1) has signature
(-,+,+,+) and det g_n(r)<-231/400 on this family at every counter.

For n>=1 the chosen common denominator is D_n=40*324^(n-1).
Section 8 proves the unconditional exact valuation

    v3(d_n)=4(n-1),

where d_n is the LEAST COMMON denominator of all SIX current readings
(h_n,chi_n). This is not a componentwise claim or a claim of complete
2-adic and 5-adic primitivity of D_n. For any exact common integer
representation (Pbar,Ybar,Dbar) of these readings,

    Dbar >= 3^(4(n-1)),
    ||Pbar||^2+Ybar^2+Dbar^2 >= (6/5)*3^(8(n-1)).

Thus bounded conserved quadratic energy coexists with unbounded exact
integer precision. A finite bank permits a finite exact forward segment
and a lossless reversal; it does not provide unlimited forward history.

## Concrete reciprocal and energy witnesses

For word0010 at counter 2, the negative and positive source contexts
give

    P2(-)=(4379,2779,794,2594,2414), Y2(-)=-6480,
    P2(+)=(4399,2759,794,2594,2414), Y2(+)=6480,
    D2=12960,
    h2(+)-h2(-)=ell/648.

These compare different initial source signs AND different constant a
contexts. Within the zero-source context a=0 at word0011:

    P1=(6,11,11,6,6), Y1=0, D1=40,
    P2=(2414,2769,2769,2414,2594), Y2=-5, D2=12960,
    P3=(973001,594836,594831,973006,1063366),
    Y3=-1975, D3=4199040.

The metric creates chi2=-1/2592, and the induced source then changes
the field at counter 3 relative to its free comparison by -ell/839808.
Keeping feedback only on the first step changes chi3 by 71/839808
relative to the continuously coupled law: the full-minus-first-only
contrast is -71/839808. This is continuing dynamical feedback.

For this a=0 witness, decompose Htot into field, source and interaction
bond quantities. Their exact increments from bond 1 to bond 2 are

    (Delta Hh, Delta Hchi, Delta I)
      = (0, 1/13436928, -1/13436928).

The first source gain is balanced by interaction; the field component
does not decrease in that first step. From bond 2 to bond 3 the increments
are

    (-180609, 28045, 152564) / (2*839808^2),

so the field now loses energy, the source gains energy, the interaction
also changes, and their total is still exactly 53/6912.

The sharp first bank is 70657245: E1=745 and E2=70657990. This bank
admits the first step with zero residual bank; one less reflects.
This is an arithmetic precision cost, not a physical energy value.

## Observed finite audit

| Check | Observed result |
| --- | --- |
| Actual normative files | 5 sizes and hashes match Public Canon v103 |
| Hermitian transports / commutator comparisons | 133 / 95 |
| Unrestricted core fixtures / funded cases | 172 / 4128; both inverse compositions and all five branches |
| Corrupt image coordinates | 2223 rejected by the exact image guard |
| Field/source/monitor history | 390 records through counter 12 across 30 histories |
| Joint reduced-action variations | 720 exact central derivatives vanish |
| Off-shell variations | 36 match independently written gradients; at least one nonzero per case |
| Positive Gram tests | 15 exact leading principal minors are positive |
| Energy bonds / joint precision valuations | 360 / 360 |
| Canonical steps | 330 complete kick-drift and generating-function vector checks |
| Symplectic checks | 1620 centered pair/bond checks plus the full matrix identity |
| Affine negative control | Uncentered Wronskian drift 1/10368, as predicted |
| Complete funded cycles | Least periods 2,4,2,4,2,4 |
| Seven disabled-law / domain controls | All behave as preregistered |
| Primary and breaker | All 768 raw certificate bytes identical |

The exact history payload SHA-256 is

    8e5c908f2b219bf76660f07b888a428529ae18eeee89123814115bdebbefa834

These finite checks audit the implementations and witnesses. They do
not replace the all-counter analytical proofs.

## Remaining obligations

This construction is an autonomous reciprocal LINEAR TT/scalar model
on five marked sites, with exact integer storage and a closed quadratic
energy account. Coupling g and ell, the preparation, monitor, denominator
register, bank and whole-step admission remain NEW_DECLARED L1 choices.

Full nonlinear Einstein dynamics, nonlinear Hamiltonian and momentum
constraint propagation with matter, three spatial dimensions, a continuum
manifold limit, native-U implementation, physical units and empirical
agreement remain open. No Canon admission or original-U dynamics claim
is made. Current-state autonomy of this declared map does not itself
derive native physical time.
