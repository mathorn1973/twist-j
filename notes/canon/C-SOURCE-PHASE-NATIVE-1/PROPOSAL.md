# C-SOURCE-PHASE-NATIVE-1: chosen coherent spatial walk and native network

**Public candidate proposal. NON-CANONICAL. Mathematical action layer L1.**

This proposal gives an explicit coefficient model of the nominated contact
walk, a local factor into coupled native cells, and exact propagation in both
readings. The carrier, coin, routing, contact and coupling are construction
data. Their properties do not require a uniqueness or forcing theorem.

The candidate umbrella is `C-SOURCE-PHASE-NATIVE-1`. The seven statements
below request future status **T**, conditional on independent theorem-grade
reading and a separately authorized Canon fold. That independent reading
is pending. Displaying proofs or passing finite audits does not itself
establish T; earlier local audits and same-session reviews do not supply
that acceptance. This file assigns no public scientific status. Neither
the umbrella nor the proposed definition is a separate registered claim.
All statements remain mathematical L1 statements; no physical interpretation
at another action layer is included.

The source, phase and retained-memory scope is a thematic continuation of
closed issue [#866](https://github.com/mathorn1973/twist-j/issues/866),
`P-U-PREPARATION-EVENT-RECORD-1`: the native information boundary and an
explicit conditional record chain. It neither reopens that issue nor
reuses its sealed probe. The present carrier has an unbounded coefficient
field, retained clock and static labels; it is not identified with the
earlier finite apparatus-history/source-quotient construction or with an
event or occupied-record mechanism. Its separate fresh audit is
[P-SOURCE-PHASE-NATIVE-1](../../../probes/P-SOURCE-PHASE-NATIVE-1/PREREG.md),
with [verifier](../../../probes/P-SOURCE-PHASE-NATIVE-1/verify.py), under
public claim [#1738](https://github.com/mathorn1973/twist-j/issues/1738).

## Authority and placement

The authority base is `mathorn1973/twist-j`, public `main` at
`892a0b11089d34e241e1eb76d2c03247022d18e6`, Public Canon v105. Its declared
content commit is `b8cdfd6ea58ae798545bc6000c817147fa0f0dcc` and the Canon
has SHA256 `73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`
and 1295029 bytes. The annotated `canon-v105` tag peels to that main commit.

The proposed insertion belongs in **15. Couplings, instruments, and
metrology**, adjacent to `CONTACT-W-SPECTRAL-READING`. It consumes that
theorem's specified W and H, and the native chart theorem
`U-NATIVE-CHART-AND-QDD-READBACK` from section 2. All public dependencies
retain their existing scope. The complete proposed statements and proofs
follow. The public [STATUS.md](../../../STATUS.md) remains the authority
declaration; the candidate and its audit do not change it.

## Definition of the chosen architecture

Write X,Y,Z for the Pauli matrices, with
Y=[[0,-i],[i,0]]. Set t=exp(i*pi/10), i=t^5, zeta=t^4, and

    O=Z[t]=Z[t]/(t^8-t^6+t^4-t^2+1),
    M=I+2iX,
    H_space=ell2(Z_R x Z_r) tensor C^4,
    M_raw=direct_sum_(R,r) O^4,
    M_amp=direct_sum_(R,r) O[1/5]^4.

Use the displayed principal complex embedding iota. Direct sums mean
finite support. Algebraic zero is allowed; normalized readings and Rayleigh
quotients require a nonzero input. Arithmetic precision is unbounded.

In channel order (++,+-,-+,--), let

    delta_0=(-1,0), delta_1=(0,-1),
    delta_2=(0,1),  delta_3=(1,0).

The local raw update and its amplitude reading are

    (Aa)_(x,c)=g(x) sum_d (M tensor M)_(c,d) a_(x-delta_c,d),
    g(R,r)=zeta^(-1) if r=0, and 1 otherwise,
    W=A/5=Gamma S (M tensor M)/5.

Coin, streaming and target contact occur in that order. The Z^2 lattice is
the equal-parity two-particle configuration lattice:
R=(x_1+x_2)/2 and r=(x_1-x_2)/2. It is a stipulated infinite lattice.

The retained-phase variant uses

    p=1+2i, c=p/sqrt(5), theta=arg(c)=atan(2),
    A_LC=p^2 A, W_LC=A_LC/25=c^2 W.

Its LC designation refers to the stationary matrix S_1=(X+2Z)/(1-2i)
and the fixed port swap and basis change proved below. It does not identify
the discrete evolution with the full finite-pulse response of a dispersive
LC circuit.

For the raw cover, retain the clock n>=0, finite-support static label field
lambda_x in F_5^4 and a in M_raw. The clock increases by one; a is replaced
by A a precisely when n+1 is divisible by three. All other ticks leave a
unchanged. The LC variant substitutes A_LC. Put k(n)=floor(n/3).

The unnormalized linear reading on a fixed clock sheet is

    chi(n,a)=5^(-k(n)) iota(a),
    chi_LC(n,a)=25^(-k(n)) iota(a).

If a unit Hilbert vector is required, keep the raw preparation a_0 unchanged
and attach one fixed preparation parameter s=1/||iota(a_0)||. Read s chi or
s chi_LC along that trajectory. A coherent prepared superposition receives
one common s for the entire state. Normalized vectors need not belong to
M_amp: (1,1)/sqrt(2) is an example, since sqrt(2) is not in Q(zeta_20).
Indeed Gal(Q(zeta_20)/Q)=C4 x C2 has exactly three quadratic subfields,
Q(i), Q(sqrt(5)) and Q(sqrt(-5)). This normalization belongs to the Hilbert
reading, not to raw-register arithmetic. Across arbitrary preparations it
is nonlinear unless s is retained as a separate static parameter.

## Golden and Clifford coin identity

Proposed identifier: `GOLDEN-CLIFFORD-COIN-IDENTITY`.

Let

    L=[[0,1],[1,-1]], K=I+2L=2X+Z, N_1=X+2Z,
    T=[[1,2],[-2,1]], D_0=diag(1,i).

Then

    L^2+L=I, L^3=K-2I,
    K^2=N_1^2=5I,
    ZK=N_1 X=T, KZ=T^T,
    D_0^(-1) T D_0=M, M^dagger M=5I.

Consequently the ordered normalized reflections Z and K/sqrt(5), and the
routed normalized scattering numerator N_1 X/sqrt(5), give the same coin
up to the fixed D_0 basis change. Keeping the complete scattering phase gives

    D_0^(-1) [N_1/(1-2i)] X D_0=c M/sqrt(5).

**Proof.** Multiply the displayed two-by-two matrices. The mixed terms in
K^2 and N_1^2 vanish because XZ+ZX=0 and X^2=Z^2=I. Also
1/(1-2i)=p/5, which gives the phase identity. The reverse order of the
reflections is explicitly T^T. These are identities for the named matrices;
no weight-selection or spatial magnetic-flux statement follows from them.

**Falsifier.** An exact failure of one displayed identity with the declared
basis, signs and order.

## Spatial Clifford reading and amplitude propagation

Proposed identifier: `COHERENT-W-SPATIAL-CLIFFORD-PROPAGATION`.

For one particle let E|x>=|x-1>, so (Ef)(x)=f(x+1), and define

    C_s=(E+E^dagger)/2, P_s=(E-E^dagger)/(2i),
    V=diag(E,E^dagger) M/sqrt(5).

Then [C_s,P_s]=0, C_s^2+P_s^2=I, and

    V=I tensor C_s/sqrt(5)+iD,
    D=X tensor (2 C_s/sqrt(5))
      +[(Z-2Y)/sqrt(5)] tensor P_s.

Thus gamma_1=X and gamma_2=(Z-2Y)/sqrt(5) are anticommuting Hermitian
involutions, while P_1=2C_s/sqrt(5) and P_2=P_s commute. Their square is

    D^2=I tensor (4I+P_s^2)/5
       =I tensor [9I/10-(E^2+E^(-2))/20].

It is not a scalar spatial operator. For every n>=0,

    <-n,+|V^n|0,+>=5^(-n/2).

The dispersion is cos(omega(k))=cos(k)/sqrt(5), with
atan(2)<=omega<=pi-atan(2) and max |omega'(k)|=1/sqrt(5).
D=(V-V^dagger)/(2i) is the local sine part. The corresponding branch
generator is H_1(k)=-omega(k)D(k)/sin(omega(k)); D itself is not that
logarithmic generator.

For the specified two-particle W, write W_f=S(M tensor M)/5. Then

    ||[Gamma,W_f]||=|zeta^(-1)-1|=2 sin(pi/5).

For every n>=0 a separate two-particle witness is

    <R=0,r=n,c=2|W^n|R=0,r=0,c=2>=5^(-n).

**Proof.** Expanding V gives the displayed D. Pauli anticommutation cancels
its mixed terms and the shift identity gives its square. At the leftmost
point after n steps there is exactly one channel history; each diagonal
coin coefficient is 1/sqrt(5). The trace and determinant of the Fourier
matrix give its two eigenvalues exp(plus-or-minus i omega). Differentiation
gives |omega'|=|sin(k)|/sqrt(4+sin(k)^2), whose maximum is attained at
|sin(k)|=1.

Let P_0 be projection to r=0. The local coin commutes with P_0, so
[Gamma,W_f]=(zeta^(-1)-1)[P_0,S] (M tensor M)/5. On the two moving relative
channels, [P_0,S] is a signed partial permutation on the entering and
leaving contact edges. Its squared absolute value is a nonzero orthogonal
projection; its norm is one. The other two channels contribute zero. This
proves the norm on the infinite lattice as well as in each center-momentum
fiber. Finally the two-particle extreme site (0,n) has a unique all-c=2
history with diagonal coefficient 1/5; its target r is positive at every
positive step, so no contact phase occurs on that history.

The two particle factors commute across their tensor factors. This theorem
does not replace them by one anticommuting two-dimensional Dirac family.
The extreme-history witnesses establish unbounded support, without making
a claim that all states lack bound components.

**Falsifier.** An exact violation of the stated operator decomposition,
square, dispersion, contact norm or extreme-history amplitude.

## Localized coefficient carrier

Proposed identifier: `COHERENT-W-LOCALIZED-RING-CLOSURE`.

The chosen W is a finite-range automorphism of M_amp, with

    A^dagger A=AA^dagger=25I,
    W^(-1)=A^dagger/5,
    <W psi,W phi>=<psi,phi>.

Every output is an admissible next input. In the fixed eight-element basis
of O, each port can be represented by eight integer numerators and a
nonnegative denominator exponent. At a local node, align denominator
exponents, apply the fixed coin, increase the exponent by one, route, and
apply the target contact. Cancelling (5a,k+1) to (a,k) leaves that port's
amplitude identical. No per-port norming or global gcd operation is needed.

Among coefficient rings containing the declared O whose full free port
modules admit W, O[1/5] is minimal. The raw map A on M_raw is injective
but not onto, and must not be conflated with this amplitude automorphism.
There is no unital ring map O[1/5] -> F_5.

**Proof.** M^dagger M=5I makes the tensor coin a similitude of squared
norm gain 25. Streaming and Gamma are unitary and preserve the integral
coefficient module. The adjoint is also local and integral. Dividing A and
A^dagger by five proves the two-sided automorphism on the localization.
A unit ++ input at r!=0 has a neighboring ++ output exactly 1/5; every
ring in the declared full-module class must contain this scalar.

Injectivity of A follows from A^dagger A=25I. A unit output in a ++
port at r!=0 has an inverse A^dagger/25 with a coefficient 1/25, which is
not an algebraic integer, so it has no preimage in M_raw. Finally a unital
map to F_5 would imply 1=rho(5*1/5)=0. Hence the native residues below
belong to the raw cover with its retained scale; they do not descend to
localized amplitudes. The normalization convention in the definition
preserves this distinction.

**Falsifier.** A failure of the two-sided inverse, Hermitian identity,
finite-range closure, local arithmetic or stated minimality within the
declared full-module class.

## Local factor into native cells

Proposed identifier: `COHERENT-W-LOCAL-NATIVE-NETWORK`.

Define rho_j:O -> F_5 by t -> j for j=2,3. These are well-defined since
Phi_20(j)=0 modulo five. At rho_2, i maps to 2 and zeta maps to 1. With
h=(1,-1,-1,1)^T, direct reduction gives

    rho_2(M tensor M)=h h^T,
    q_x=h^T rho_2(a_x), z_x=sum_c rho_2(a_(x,c)),
    rho_2(Aa)_(x,c)=h_c q_(x-delta_c),
    q'=Adj q, epsilon_k=4^(-k)q_k,
    epsilon_(k+1)=B epsilon_k, B=4 Adj.

Here Adj is the sum over the four lattice neighbors. In F_5, four is its
own inverse and the sum of all epsilon labels is conserved.

We specify the native interfaces explicitly. For a head
x=(p_1,p_4,p'_1,p'_4,Q,r) in F_5^6, let theta_n be the binary digit-sum
parity of n, and set U_n(x)=g_j(x), j=(sum(x)+2theta_n) mod 5, where

    g_0(x)=(p_4,p_1,p'_4,p'_1,Q,r),
    g_1(x)=(-p'_1,-p'_4,-p_1,-p_4,-Q,-r),
    g_2(x)=(2-p'_1,1-p'_4+r,2-p_1,1-p_4-r,1-Q,-r),
    g_3(x)=(2-p_1,1-p_4,3-p'_1,4-p'_4,1-Q,1-r),
    g_4(x)=(2-p_1,1-p_4,3-p'_1,4-p'_4,2-Q,1-r).

Put F_n=U_(n-1)...U_0. For n>=3 the registered native chart J_n is the
inverse of the label chart in U-NATIVE-CHART-AND-QDD-READBACK. Explicitly,

    S(0)=0, S(m)=m-S(floor(m/2)),
    t_n=(-1)^(n-3), h_n=(-1)^(n+theta_(n-1)),
    N_n=S(floor((n-1)/2))-1,
    A_0=t_n alpha, B_0=t_n beta,
    C_0=2+h_n gamma, D_0=1+h_n delta,
    r=t_n(epsilon+N_n), Q=4-3theta_(n-1)-A_0-B_0-r,
    J_n(alpha,beta,gamma,delta,epsilon)
      =(3(A_0+C_0),3(B_0+D_0),3(A_0-C_0),3(B_0-D_0),Q,r).

Compute the clock functions, S and exponents on integers, and reduce the
displayed chart coordinates modulo five. The theorem gives U_n J_n=J_(n+1) and
bijectivity of J_n onto the synchronized sheet. For y on the sheet at
time 3, the actual antecedents from initial sheet z are

    x_0(y)=g_0 g_2 g_4(y), x_1(y)=g_3(y), x_2(y)=g_4(y),
    x_3(y)=g_3 g_1 g_3(y), x_4(y)=g_4 g_1 g_3(y),

with the rightmost map applied first. Substitution in the five displayed
native maps verifies sum(x_z)=z and F_3 x_z(y)=y. Each x_z is an affine
inverse on its sheet; together the five sheets exhaust F_5^6.

Prepare each cell by

    E_x=x_(z_x)(J_3(lambda_x,q_x)).

Every residue pair (q_x,z_x) is realized by the two channel residues
a_(x,0)=(q_x+z_x)/2, a_(x,1)=(z_x-q_x)/2, with the remaining two zero.
Together with lambda_x this prepares every local native head. On the
infinite lattice, the admissible network configurations have finitely many
deviations from the specified vacuum; the four lambda labels also have
finite support. If a nonzero raw amplitude is required, adding five to one
port realizes the same residues with a nonzero raw state. This construction
couples the amplitudes and native heads; they are not independently chosen.

Define U_net at tick n by first applying U_n to every cell and, when
n+1 is divisible by three, then replacing the attained chart labels by
(lambda_x,(B epsilon)_x). The first coupling occurs at the actual 2->3
transition, after F_3. Define

    (Pi_loc(n,lambda,a))_x=F_n E_x                         for n<3,
    (Pi_loc(n,lambda,a))_x=J_n(lambda_x,4^(-k(n))q_x)      for n>=3.

With the clock included in both source and target, this is a surjective
semiconjugacy:

    Pi_loc U_tilde = U_net Pi_loc.

For the unrestricted time-tagged target, its n=0,1,2 sheets are the actual
cellwise F_n images of the initial configuration space. Its n>=3 sheets
are finite deviations in J_n, relative to J_n(0,0). The earlier vacuum is
F_n x_0(J_3(0,0)); it need not be the zero head. Surjectivity on each such
sheet follows from the residue preparation above, including multiplication
of a desired late epsilon by 4^k to choose q. If only trajectories starting
at n=0 are admitted, restrict both systems to their reachable subsets;
surjectivity there follows by intertwining the surjective preparation.
This does not assert that all unrestricted late sheets are reachable from
time zero.

**Proof.** Rank-one reduction gives the channel formula. Multiplying by
h_c and summing uses h_c^2=1, hence q'=Adj q and the compensated B rule.
At ordinary ticks the raw field does not change and U_n J_n=J_(n+1).
At the first coupling F_3 E_x=J_3(lambda_x,q_x), while the raw update reads
4^(-1)Adj q=B q. At each later coupling,
4^(-(k+1))Adj q=B(4^(-k)q). These establish all ticks. The preparation
and the time-tagged domain statements give the asserted surjectivity.
For n=0,1 the raw field is unchanged and F_(n+1)E=U_n F_n E verifies
the two unsynchronized transitions directly. Conservation follows from
sum_x(B epsilon)_x=16 sum_x epsilon_x=sum_x
epsilon_x in F_5. No residue homomorphism on the localized ring is used.

**Falsifier.** An admitted exact failure of the residue channel law,
two-residue preparation, native antecedent, chart transport or all-tick
semiconjugacy on the stated target sheets.

## Native Frobenius propagation and reversibility boundary

Proposed identifier: `COHERENT-W-NATIVE-FROBENIUS-PROPAGATION`.

On finitely supported F_5 fields over Z^2, B is injective but not onto.
For the prepared label epsilon_0=delta_(0,0), every k>=1 has value 4^k
at the four extreme points (plus-or-minus k,0),(0,plus-or-minus k).
For every m>=0, with N=5^m, the stronger complete-support identity is

    epsilon_N=B^N delta_(0,0)
      =4[delta_(N,0)+delta_(-N,0)+delta_(0,N)+delta_(0,-N)].

These profiles occur at microscopic times n=3*5^m for preparation at n=0.
Since J_n is injective, each nonzero epsilon produces a head different from
the native vacuum when lambda=0. This proves unbounded native-label
propagation on the chosen infinite configuration lattice. The same result
holds in the retained-phase variant below.

The finite-support boundary has a precise formal alternative. Put
R=F_5[u,u^(-1)] and define R((v)) to consist of formal series
sum_(j>=j0) r_j v^j, with j0 an integer and each r_j in R. On this
one-sided Laurent-series completion b=4(u+u^(-1)+v+v^(-1)) is a unit:

    b^(-1)=4v [1+(u+u^(-1))v+v^2]^(-1)
          =4v sum_(j>=0) (-1)^j [(u+u^(-1))v+v^2]^j.

This inverse has infinite support. It is not an inverse on the original
direct sum, a finite-range operation, or a prescription for arbitrary
two-sided infinite fields. Choosing this completion changes the carrier.

The four-point cancellation is a characteristic-five assertion. For the
integer comparison B_Z=4 Adj, the coefficient at (3,0) in B_Z^5 delta_0
is 25600, rather than zero. This comparison operator is not the raw
coherent A or A_LC. Their coefficients lie in the characteristic-zero
ring O; the Frobenius cancellation belongs to their stated F_5 residue
readings, not to the raw amplitudes.

**Proof.** Identify finitely supported fields with Laurent polynomials over
F_5. Then B is multiplication by

    b(u,v)=4(u+u^(-1)+v+v^(-1))
          =4(uv)^(-1)(u+v)(uv+1).

The Laurent ring is an integral domain, so multiplication by nonzero b is
injective. It is not onto: evaluation at (u,v)=(1,-1) is defined on the
Laurent ring and gives b=0, whereas the unit impulse is the constant
polynomial 1. Thus no finite-support preimage of that impulse exists.

Define T_R delta_(R,r)=delta_(R+1,r) and
T_r delta_(R,r)=delta_(R,r+1). The four shifts commute. In characteristic
five the Frobenius map gives

    B^(5^m)=4^(5^m)[T_R^(5^m)+T_R^(-5^m)
                         +T_r^(5^m)+T_r^(-5^m)].

Since 4=-1 and 5^m is odd, 4^(5^m)=4. Applying this identity to delta_0
proves the four-point formula, including cancellation at every other site.
Their total label is 4*4=1. At general k, each extreme site has exactly one
length-k nearest-neighbor history, of weight 4^k. The first coupling is
at 2->3, so there have been exactly k couplings at microscopic time 3k.

Finite support is essential to the injectivity assertion: on all infinite
fields epsilon(R,r)=(-1)^R is a nonzero element of ker(B). This boundary
does not affect the theorem on the declared direct-sum carrier.

For the formal completion, factor
b=4v^(-1)[1+(u+u^(-1))v+v^2]. The term in brackets has constant
coefficient one, so its displayed geometric inverse is defined in R[[v]].
At each fixed v degree only finitely many terms contribute; each
coefficient remains a Laurent polynomial in u. The inverse of 4 is 4 in
F_5. The kernel example above has support unbounded below in the v
direction and is not an element of R((v)), so the two assertions are
compatible. Finally, over the integers, the five-step paths to (3,0)
consist of five arrangements of four right steps and one left step, and
twenty arrangements of three right steps, one up and one down. Each has
weight 4^5. Thus the coefficient is (5+20)4^5=25600, which vanishes
after reduction modulo five but not in characteristic zero.

**Falsifier.** An exact violation of the Laurent identity, finite-support
injectivity/non-surjectivity, extreme-site value, four-point formula or
specified clock conversion on the declared infinite lattice, or of the
formal inverse or characteristic-zero coefficient on their stated carriers.

## Retained scattering phase and the second residue place

Proposed identifier: `COHERENT-W-PHASE-RETAINED-LOCAL-FACTOR`.

The full-phase step is an automorphism of M_amp and satisfies

    A_LC^dagger A_LC=A_LC A_LC^dagger=625I,
    W_LC^(-1)=A_LC^dagger/25.

At rho_3, i maps to 3, zeta maps to 1, p^2 maps to 4, and
rho_3(M tensor M)=e e^T for e=(1,1,1,1)^T. Put

    q_x^+=e^T rho_3(a_x), z_x^+=h^T rho_3(a_x).

Then q^{+prime}=B q^+ with the very same B, without a clock compensation.
The local native preparation uses x_(z_x^+)(J_3(lambda_x,q_x^+)). At n>=3
the projection is J_n(lambda_x,q_x^+). At earlier ticks it is the actual
F_n of that preparation. It intertwines the retained-phase raw cover with
the same U_net at every tick and has the same sheetwise surjectivity.

**Proof.** p conjugate(p)=5, so |p^2|^2=25 and the raw squared gain is
625. The scalar commutes with A, proving the inverse and closure after
division by 25. Reduction at rho_3 gives each output channel
4 q^+_(x-delta_c); summing gives B q^+. The independent initial pair
(q^+,z^+) is obtained from channel residues (q^++z^+)/2 and
(q^+-z^+)/2. Apply the preceding native proof, with no 4^(-k) factor.
In contrast rho_2(p)=0, so using the old place would annihilate all new
raw output residues. The two residue maps are not star homomorphisms;
no Hilbert-norm interpretation over F_5 is claimed.

After k common steps the two complex evolutions differ by c^(2k).
For coherent alternatives with different passage counts this phase must
remain, for example in diag(W_LC,I). The latter controlled block is an
additional amplitude construction; the native factor above is not asserted
for that enlarged controlled carrier.

**Falsifier.** An exact violation of the gain, inverse, rho_3 identities,
preparation or all-tick local factor, or a failure of the retained phase
relative to a waiting branch.

## Spectral energy on the raw cover

Proposed identifier: `INTEGER-W-SPECTRAL-ENERGY-PULLBACK`.

Let H=i Log_alpha(W) be exactly the fixed reading of
CONTACT-W-SPECTRAL-READING, alpha=3pi/10, so exp(-iH)=W and
0<=H+alpha I<=2pi I. For nonzero a in M_raw define

    E_H(a)=<iota(a),(H+alpha I)iota(a)>/||iota(a)||^2.

Then 0<=E_H<=2pi and E_H(Aa)=E_H(a). More strongly every normalized
spectral measure of H is invariant under both A and A_LC. Also

    H_LC=H-2theta I,
    exp(-iH_LC)=W_LC,
    H_LC+(alpha+2theta)I=H+alpha I.

**Proof.** For a spectral projector E_H(Omega), functional calculus gives
W^dagger E_H(Omega)W=E_H(Omega). Both numerator and denominator of its
normalized expectation acquire the same factor 25 under A=5W. Under
A_LC=25c^2W the common factor is 625. This proves the whole spectral
measure identity and hence the energy statement. The scalar shift gives
the phase identity. Between raw macrosteps a is unchanged, so the reading
is invariant at every microscopic tick as well. Fixed preparation scalars
cancel from these quotients.

This is a conserved spectral reading, not a positive-definite quadratic
energy of unbounded integer registers. It gives no bound on their magnitude
or memory cost and includes no SI calibration.

**Falsifier.** An exact failure of the raw-to-unitary identities, the cited
spectral premise or one of the normalized spectral measure equalities.

## Proposed changes and evidence boundary

Subject to proof acceptance, insert the definition and seven statements
with their proofs above. Add the seven
rows in [REGISTRY.proposed.tsv](REGISTRY.proposed.tsv), the typed entries
in [NORMATIVE.proposed.tsv](NORMATIVE.proposed.tsv), and the dependency
edges in [DEPENDENCIES.proposed.tsv](DEPENDENCIES.proposed.tsv). The status
columns in these files specify requested post-review statuses, not current
registration. Definitions receive no registry claim row. Regenerate the
public EVIDENCE table and normative hashes using the target repository's
current tooling after the actual Canon text is settled.

The proposed short CORE addition is in [CORE.proposed.md](CORE.proposed.md).
No existing FRONTIER obligation is closed. In particular
MINIMAL-READ-DERIVATION, QUADRATIC-MEMORY-NATIVE-CONTACT and the photon
obligations retain their contracts. No version number, release form or
tag is assigned by this proposal. Direct LC cascades and compact-pulse
restoration are outside these seven statements.

The evidence submitted for future T is the exact proof text and its two
named public theorem dependencies. Independent theorem-grade reading is
pending. Previous local audits and same-session analytical reviews do not
establish T. The fresh
[preregistered audit](../../../probes/P-SOURCE-PHASE-NATIVE-1/PREREG.md)
states its own finite scope and falsifiers. Only its own pin and completed
public records may establish what that audit actually checked; it cannot
retroactively formalize earlier local executions or replace the pending
proof acceptance.

This directory is the public proposal surface for C-SOURCE-PHASE-NATIVE-1.
The proposed table fragments are not edits to the live Canon ledgers. A
later separately authorized fold must follow the then-current
[POLICY.md](../../../POLICY.md), claim and release procedure, as described
in [INTEGRATION.md](INTEGRATION.md).
