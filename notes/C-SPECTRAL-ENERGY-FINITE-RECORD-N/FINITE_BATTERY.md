# A finite coherent battery with a bounded spectral-energy resolution

**NON-CANONICAL, L1. Conditional analytical candidate; independent
mathematical acceptance pending.** Author: A. M. Thorn. License: Apache-2.0.
Public reservation: #1767. This extends the fixed first candidate
`dc42c14acdb51385a7385ef83ccecee6aeb59415` without changing its proofs.
No scientific executable, simulation or gate enumeration was run.

The continuous battery in [ENERGY.md](ENERGY.md) can be replaced by a
finite ladder if exact conservation is required for a declared rounded
energy. The original energy then has a uniform, nonaccumulating drift
bound. This changes the energy contract explicitly. It does not make an
arbitrary continuous spectral energy exactly compatible with a finite
battery, nor does it make the original object Hilbert space finite.

## 1. Rounded energy and complete finite total-charge sectors

Let the actual system energy be bounded and nonnegative,

    0 <= Q <= Delta I,                 Delta>0.

The system Hilbert space may be infinite dimensional. All finite
information registers and passive references can be included as tensor
factors on which Q is the identity times zero. Fix a resolution d>0 and
define by Borel functional calculus

    F=floor(Q/d),       Q_d=d F,       m=ceil(Delta/d),
    P_r=1_{r}(F),                     0<=r<=m,
    D=Q-Q_d,           0<=D<=d I.                         (F1)

Some P_r may vanish. In particular the upper endpoint convention at an
exact multiple of d is the one specified by floor. Although pointwise
remainders are less than d, their operator norm can equal d; the closed
operator inequality in (F1) is intentional. The P_r may have infinite
rank. A finite number of energy bins is not a finite-dimensional system.

Choose an integer N>=2m. The battery and its Hamiltonian are

    H_B=span{|n>:0<=n<=N},
    B=d sum_{n=0}^N n |n><n|,
    K_d=Q_d tensor I + I tensor B.                       (F2)

For an integer total charge k, its full eigenspace is

    H_k=direct-sum_{r:0<=r<=m, 0<=k-r<=N}
                  Ran(P_r) tensor |k-r>.

For every m<=k<=N this space contains every system energy sector. The map

    J_k psi=sum_{r=0}^m P_r psi tensor |k-r>             (F3)

is an isometry from the entire system onto H_k. Different J_k have
orthogonal ranges. Let P_good=sum_{k=m}^N J_k J_k^*. For any system
unitary U, define the full finite-battery lift

    Gamma(U)=sum_{k=m}^N J_k U J_k^* + (I-P_good).       (F4)

It is unitary on every raw state: it acts unitarily on each complete
sector and identically on every remaining sector. No out-of-range
battery shift is projected away. Direct block multiplication gives

    [Gamma(U),K_d]=0,
    Gamma(U)Gamma(V)=Gamma(UV),
    Gamma(U)^*=Gamma(U^*).                              (F5)

These are entire-space identities, not just statements about a prepared
input. For a finite word they use the same F, N and sector convention.
Consequently an error estimate for the full product need not be added
once per primitive gate. The exact coupling (F4), including its spectral
projectors, remains a supplied operation; locality is not proved.

## 2. An explicit finite coherent packet

Put

    L=N-2m+2,                  L>=2,
    eta_n=sqrt(2/L) sin(pi*(n-m+1)/L),  m<=n<=N-m,
    eta_n=0 otherwise.                                  (F6)

There are L-1 occupied ladder levels. The finite sine identity
sum_{j=1}^{L-1} sin^2(pi*j/L)=L/2 proves normalization. The support is
buffered on both sides: every initial system charge r and occupied
battery level n obey m<=r+n<=N. Thus every system/reference input with
this battery lies entirely in P_good, without restricting its spectral
support or postselecting a charge sector.

For the proof only, embed the battery in ell^2(Z). Write T_s|n>=|n+s>
for integer translations and extend eta by zero. Its nearest-neighbor
overlap is cos(pi/L). To verify this, the finite sine recurrence is

    eta_{n-1}+eta_{n+1}=2 cos(pi/L) eta_n

on its support, with zero Dirichlet endpoints. Multiply by eta_n and
sum. Normalization then gives

    a:=||(T_1-I)eta||=2 sin(pi/(2L)) <= pi/L.             (F7)

No periodic ladder or wraparound shift is used in the actual unitary.
The bilateral shift is only an auxiliary device for bounding its action
on the buffered input.

## 3. A reference-uniform bound with no parity loss

On the bilateral auxiliary battery define

    S=sum_{r=0}^m P_r tensor T_{-r}.

The compensated full-line unitary is S(U tensor I)S^*. A system matrix
element from charge r to charge r' shifts battery level n to n+r-r'.
On the input (F6), this action agrees exactly with (F4): the total
charge stays in [m,N] and the final battery level remains in [0,N].

The following elementary product proof yields m*a, including for odd m.
For j=1,...,m put

    Pi_j=1_{[j,infinity)}(F),
    S_j=(I-Pi_j) tensor I + Pi_j tensor T_{-1}.

All S_j are unitary, commute with one another, and

    S=S_1...S_m,
    [S_j,U tensor I]=[Pi_j,U] tensor (T_{-1}-I).          (F8)

For any orthogonal projection Pi and unitary U, ||[Pi,U]||<=1. In the
decomposition Ran(Pi) direct-sum Ker(Pi), this commutator has only two
off-diagonal blocks, each a compression of U of norm at most one.

Expand [S_1...S_m,U tensor I] as the sum of m terms, each with one
commutator (F8), preceded and followed by products of the S_j. The
battery difference T_{-1}-I commutes with every S_j and with S^*.
Therefore each such term, applied to S^*(psi tensor eta), has norm at
most ||(T_{-1}-I)eta||=a. This remains true when psi includes an arbitrary
passive reference, since the same operator identities are tensored with
its identity. Using Gamma(U)-U=(S U-U S)S^* on this input gives

    ||Gamma(U)(psi tensor eta) - U psi tensor eta||
       <= 2m sin(pi/(2L)) <= pi*m/L =: e_bound.           (F9)

In the middle expression U has its untouched battery and reference
identities. The estimate is a whole joint-vector comparison; it does
not assume that the actual battery returns or stays uncorrelated.

For trace distance D_tr(rho,sigma)=||rho-sigma||_1/2, the same bound,
capped at one, holds on the joint system/battery/reference densities.
Pure-state trace distance is bounded by the vector norm in (F9);
purifying a mixed system/reference input and tracing its purification
proves the general assertion. It also bounds half the diamond distance
of the reduced system channel from the target U channel.

For the entire finite word U_s...U_1 use (F5) first and apply (F9) to
that product once. Residual battery correlations at intermediate steps
are not replaced by fresh packets. No reuse or reset cost is suppressed.

If a common subsequent accepted-plus-rejected instrument has ideal
accepted probability p_0>e_bound, then

    |p_actual-p_0|<=e_bound,
    D_tr(rho_actual,acc,rho_ideal,acc)<=e_bound/p_0.       (F10)

The states in this formula are normalized and retain the specified
reference. Append a scalar rejection outcome before normalizing: trace
contractivity gives the accepted trace-norm difference plus the absolute
probability difference at most 2e_bound. The normalization triangle
inequality with the ideal denominator proves (F10). All rejected sectors
remain in the unconditioned dynamics.

## 4. Exact rounded conservation and bounded original-energy drift

Retain the original energy observable, including the same battery,

    E=Q tensor I + I tensor B=K_d+D tensor I.             (F11)

For any unitary Z satisfying [Z,K_d]=0, not just one lifted gate,

    Z^* E Z-E=Z^*(D tensor I)Z-D tensor I.

Both terms on the right lie between zero and dI. Their difference thus
lies between -dI and dI, proving the sharp uniform bound

    ||Z^* E Z-E||<=d.                                   (F12)

It follows for every input, with or without a reference, that the change
in the expectation of the original system-plus-battery energy is at
most d in absolute value. If a complete autonomous H commutes with K_d,
(F12) holds at every time and between every two times. It is independent
of elapsed time and of the number of compensated gates. It does not
assert a small instantaneous derivative or exact conservation of E.
This is an unconditioned comparison of the same global ensemble.
Conditioning on an accepted outcome changes that ensemble and does not
inherit the mean-energy bound merely by dividing by its probability.

This distinction cannot be removed by notation. For a sharp example take
Q as multiplication by x on L^2([0,d]), so Q_d=0 almost everywhere, and
take (U psi)(x)=psi(d-x). Then U preserves Q_d, but

    U^* Q U-Q=dI-2Q,       ||U^* Q U-Q||=d.              (F13)

The battery may remain an untouched spectator. Thus no smaller uniform
bound follows only from rounding and exact K_d conservation. The norm
is a supremum; an endpoint energy eigenvector is not needed.

The generator used in an application must be stated separately. Exact
conservation of K_d does not make its rounded Q_d term identical to Q.
Adding the residual D to a solvable history Hamiltonian can change its
time-dependent trajectory, even though (F12) still holds if that full
Hamiltonian commutes with K_d. Such a change needs its own dynamical error
bound; it is not covered merely by the energy-drift statement.

## 5. Explicit finite resources and parameter choices

For any chosen compensation tolerance 0<e<1, choose before evolution

    m=ceil(Delta/d),
    L=max{2,ceil(pi*m/e)},
    N=L+2m-2.                                          (F14)

Then (F9) is at most e. The added battery has exactly

    dim H_B=N+1=L+2m-1,
    capacity=dN,
    mean energy in eta=dN/2,
    Var_eta(B)<=(dN)^2/4.                               (F15)

The mean follows from eta_n=eta_{N-n}; the variance bound uses its bounded
spectrum. For these choices, dN<=(Delta+d)(2+pi/e)-d. This is a convenient
finite upper bound, not an optimum or a manufacturing-cost estimate.
At fixed e, improving the resolution d increases the dimension even
though this capacity estimate stays bounded as d tends to zero.

The cost also includes the pure coherent state (F6), exact spectral bins,
and the global couplings in (F4). The original object/carrier may remain
infinite dimensional. A separate finite-carrier approximation must give
its own state and energy interface, rather than identify that carrier
with the infinitely many original positions.

## 6. Why exact original-energy conservation is a different requirement

A finite battery cannot supply a universal replacement for the continuous
construction while preserving every continuous Q exactly. A precise
counterexample already uses Q=M_x on L^2([0,1]) and the fixed reflection
(U psi)(x)=psi(1-x).

Let an arbitrary finite-dimensional apparatus have energy eigenvalues
b_1,...,b_h and any fixed initial state, including energy coherence.
Suppose a joint unitary V exactly conserves Q+B. Its matrix blocks V_ji
in an apparatus energy basis obey

    Q V_ji-V_ji Q=(b_i-b_j)V_ji.                         (F16)

Functional calculus, or exponentiating this identity, shows that V_ji
maps system spectral support I into I+(b_i-b_j), intersected with [0,1].
Let D_B={b_i-b_j:1<=i,j<=h}; this is a finite set. Choose x_0 in (0,1)
with 1-2x_0 not in D_B. A sufficiently narrow nonempty interval I around
x_0 then satisfies

    (1-I) intersect union_{c in D_B}(I+c)=empty.         (F17)

For a normalized system vector supported in I, every actual output block
has support in the union in (F17), irrespective of apparatus coherence.
The desired reflection is supported in 1-I. The actual reduced output
and ideal pure output therefore have orthogonal support and trace
distance exactly one. Thus the worst-case channel error is maximal for
every finite apparatus satisfying this exact-energy contract.

This is a universal-input obstruction for this specified Q and U. It
does not exclude approximation on a restricted prepared source family,
an infinite-dimensional energy source, or the rounded contract proved
above. Increasing a finite apparatus does not fix the uniform statement:
one may always choose a sufficiently narrow input after its finite set
D_B has been specified. The example does not assert that every unitary
needs a continuous battery; energy-preserving ones need none.

## 7. The packet's coherence is an additional preparation resource

The ladder B in (F2) is nondegenerate. Every stationary battery state
sigma_B, including every normalizable Gibbs state, is diagonal in its
energy basis.
For the pure packet (F6),

    <eta|sigma_B|eta><=max_n |eta_n|^2<=2/L,
    D_tr(sigma_B,|eta><eta|)>=1-2/L.                     (F18)

The second inequality follows by measuring the projector |eta><eta|.
Large L therefore improves compensation while making a stationary
substitute far from the required packet. A small thermal defect promise
cannot simply be substituted for its energy coherence.

More generally, let all preparation systems have additive energy H_A+B.
If their complete initial density commutes with that sum and the
preparation unitary conserves the sum, the final complete density also
commutes with it. Partial trace then makes the battery marginal commute
with B. Such a preparation cannot produce the coherent packet to an
accuracy contradicting (F18). Products of normalizable Gibbs factors at different
temperatures still commute with their additive energy; temperature
contrast alone does not remove this stationarity premise.

This does not say that temperature contrast cannot drive energy transfer.
It concerns production of bare-energy coherence by that conserving law.
A nonstationary source, coherent reference, nonconserving external control
or an interaction-energy boundary can change the premise and must be
included explicitly. In particular a spatial object input may itself
carry asymmetry; spending it to prepare eta would require a proved joint
preparation and continuation contract, which is not supplied here.

There is a stronger limitation even if one bounded source supplies
asymmetry. Let its Hamiltonian q_src have spectral width at most m*d.
Prepare that source independently of all remaining preparation resources,
whose complete density is stationary for their additive energy, including
the initial battery. Allow any unitary conserving the entire additive
preparation energy. Consider its complete unconditional battery output
sigma, without postselection or an external phase reference.

The induced source-to-battery channel is energy-covariant: invariance of
the other input factors and commutation of the preparation unitary give
covariance directly. Therefore its output matrix entry sigma_nn' can use
only a source Bohr frequency (n-n')d. More formally the dual image of the
battery matrix unit is an eigenoperator of commutation with q_src with
that frequency, up to sign. For any bounded A,

    ||[q_src,A]||<=m*d*||A||,

by subtracting the midpoint of the source spectrum. Consequently that
dual image is zero for |n-n'|>m. The output satisfies exactly

    sigma_nn'=0 whenever |n-n'|>m.                       (F19)

This argument also covers a continuous bounded source spectrum. A
passive reference initially entangled with the source does not change
the statement: trace it to obtain the same source-to-battery channel.

Put p_n=sigma_nn and x_n=sqrt(p_n), so sum_n x_n^2=1. Positivity gives
|sigma_nn'|<=x_n*x_n'. With A_nn'=|eta_n eta_n'| for |n-n'|<=m and zero
otherwise, (F19) implies <eta|sigma|eta><=x^T A x. Every row of this real
symmetric nonnegative matrix has at most 2m+1 terms, each at most 2/L.
Its operator norm is at most its maximum row sum. Hence

    <eta|sigma|eta><=(4m+2)/L,
    D_tr(sigma,|eta><eta|)>=max{0,1-(4m+2)/L}.            (F20)

Thus one source of this bounded spectral width cannot prepare the broad
packet to arbitrary accuracy from otherwise stationary resources. This
does not exclude many sources with a wider aggregate coherent spectrum,
another nonstationary resource, external phase control, a different
preparation-energy contract or a conditioned protocol. It is not a claim
that all energy flow is impossible. None of these additional resources
or protocols is supplied by the finite-battery replacement itself.

## 8. Failure conditions and remaining boundary

The candidate fails if the rounded spectral sectors do not define the
entire-space unitary (F4), if an admitted reference input violates (F9),
if exact K_d conservation violates (F12), if the spectral-support argument
(F16)-(F17) fails for the stated reflection, if a stationary battery
violates (F18), or if the specified conserving one-source preparation
violates (F19)-(F20). These are distinct mathematical obligations.

The positive result is a finite coherent battery with explicit dimension,
capacity and uniform channel error, exact rounded conservation and a
uniform original-energy drift bound. Exact original-energy conservation,
spatially local couplings, thermal preparation of coherence, a finite
representation of the original full spatial carrier, reusable reset,
material calibration and independent mathematical acceptance remain
outside this result.
