# Exact readout, resource calibration and the native boundary

**NON-CANONICAL / NO AUTHORITY. Conditional candidate-T, L1.**
This is an analytical proof, not a scientific execution record. Literal
configuration equality is used throughout. Mathematical energy accounts are
not identified with measured energy or SI units. The pinned authority and
external comparison notes are listed in [SOURCES.md](SOURCES.md).

## R1. Reading an observable is weaker than reconstructing a state

Let X be a set, R:X->Y a specified reader, and W:X->Z a specified target.
There exists w:R(X)->Z with W=w R if and only if

```text
R(s)=R(t) implies W(s)=W(t), for all s,t in X.                 (R1)
```

Necessity follows by applying w. For sufficiency, define w(y) to be the
common W-value on the nonempty fibre R^(-1)(y). The assumption makes this
well-defined and unique. No arbitrary extension outside R(X) is implied.

In particular, complete reconstruction requires the same criterion for
W=id_X, namely injectivity of R. Reconstruction of one observable does
not require that stronger condition. For example, T(a,b)=(b,a), energy
E1(a,b)=a, and R(a,b)=a-b on nonnegative integer pairs give
E1(s)-E1(T^(-1)s)=R(s), although R is not injective.

For a bijection T:X->X and a fixed energy E1, the last-step change as a
function of the output is

```text
W_T(s') = E1(s') - E1(T^(-1)s').                             (R2)
```

Equation (R1) is necessary and sufficient for its exact instantaneous
readout. The same theorem applies to a tuple containing a prior local
state, an event bit and W_T. On a declared initial state T^(-1)s' is only
the mathematical predecessor; it is a past occurrence only after an
actual step. A function w alone is not a physical apparatus implementing it.

For an affine Gauss fibre E0+K, full-field reconstruction needs K={0};
observable reconstruction only needs the particular W_T to be constant
on that fibre, including its other frozen coordinates. A cycle that changes
energy need not change an energy DIFFERENCE under every possible T. Thus
the static Gauss obstruction in source B does not by itself decide R2.

## R2. Autonomous observed dynamics and finite histories

For any T:X->X, an update V:R(X)->R(X) satisfying R T=V R exists exactly
when R(s)=R(t) implies R(Ts)=R(Tt). This is R1 applied to W=R T. It need
not imply state reconstruction or locality of V. When R is injective,
V=R T R^(-1) on the image; its inverse exists if T is bijective.

For m>=1, define the forward observation block

```text
R_m(s)=(R(s),R(Ts),...,R(T^(m-1)s)).
```

It has an autonomous update exactly when equal R_m blocks also have equal
R(T^m s). Indeed, the first m-1 entries of the next block are already
known and only its final entry needs to factor through R_m. More recorded
history is therefore a testable new interface, not an automatic solution.
This forward-block statement makes no claim of instantaneous physical
access to future data.

## R3. The fixed two-cell interface

Use source A's full cell c_i=(m_i,b_i,z_i,r_i), z_i=(E_i,M_i), r_i>=0;
a neutral intercell store eta>=0; and pointer p in Z/5Z of constant cost 1.
Let E_i be its prescribed nonnegative cell energy and

```text
Hhat=E_0+E_1+eta+1.
T=F B A Ghat,  A=swap(r0,eta),  B=swap(eta,r1).
```

The chronological order is Ghat;A;B;F. The cell reaction G is the complete
energy-preserving involution of CONTACT section 1; F acts by the known
invertible field map T_f and preserves cell energy. The receiver pointer
adds e(c1), which equals 1 exactly for an accepted literal R->AM reaction.
Ghat is not being called an involution; its inverse subtracts the event
computed on the reconstructed input. The neutral link is not an electric
edge between cells.

After local reactions, denote the stocks by rtilde0,rtilde1. Direct
composition of the two complete swaps gives

```text
(r0',r1',eta')=(eta,rtilde0,rtilde1).
Delta E0=r0'-r1',  Delta E1=r1'-eta',  Delta eta=eta'-r0'.     (R3)
```

The three changes sum to zero. The proof uses conservation by G and F,
not successful reaction admission. All occupied stocks are included.

From the output interface (c1',eta',p') construct

```text
d=(m1',b1',T_f^(-1)z1',eta'),
c1_before=G(d),
e_last=e(c1_before),  p_before=p'-e_last mod 5.               (R4)
```

The original post-reaction receiver stock is precisely eta', while
contacts left its other cell coordinates untouched. Inverting F and G
therefore proves R4 on the full carrier. Together with R3 this gives the
exact target tuple. The full law is a bijection of the product carrier;
every admissible interface value occurs as the projection of some full
output. Hence any other exact reader of the SAME tuple and SAME energy
on this interface agrees everywhere on that interface.

Additional B;B swaps the pair (a,b)=(r1',eta') to (b,a) and back, including
occupied inputs. During the middle state the receiver holds the original
eta'. The first B changes E1 by b-a, the negative of its preceding R3
change; the second restores it. B commutes with F, so B T=F A Ghat and
B^2 T=T. These identities contain no extra recording operation. A single
middle receiver snapshot has lost a to the link. Recording a-b requires
both readings or retained information. Independent scheduling and access
to the intermediate state are additional premises if only T is admitted.

## R4. A sharp information bound at fixed energy

For every integer h>=1, prepare zero matter, spectators and fields,
p=0, and (r0,r1,eta)=(0,k,h-1-k), where 0<=k<h. G is identity on the
literal zero matter triple, and F fixes the zero field. All states have
Hhat=h. Their outputs have stocks (h-1-k,0,k), the same complete receiver
and pointer, but Delta E1=-k.

An additional deterministic, exact one-shot code therefore requires at
least h distinguishable values even if h is known. This is sharp as an
abstract supplementary alphabet: nonnegativity gives 0<=eta'<=h-1 on
the whole shell, and recording eta' suffices with the existing receiver.
The binary lower bound is ceil(log2 h). This does not assign a cost to
the added memory, implement a writing gate, or prove that an apparatus
of that size can be added without changing the energy shell.

Without a fixed energy bound, the family (0,2k,0) gives identical receiver
outputs and changes -2k for arbitrarily large k. No fixed finite added
register, starting in one common state and leaving the stipulated cell/link
transition unchanged, can record every such change exactly in one step.
The claim is about complete deterministic outcomes, not merely a fitted
expectation, repeated experiments or a different growing memory carrier.

## R5. Exact scope of the reserve-profile family

Keep every nonstock energy term fixed, use one additive profile f on every
cell and link stock, impose f(0)=0, and require all old primitives to
preserve this energy on the full carrier. The literal R reaction at zero
field sends any r>=2 to r-2 and raises matter energy by 2. Thus necessarily
f(r+2)-f(r)=2 for all r>=0. Writing c=f(1) gives exactly

```text
f_c(r)=r+(c-1)(r mod 2).                                    (R5)
```

Conversely all G stock changes are even, all contacts are whole-stock
swaps with a common profile, and F changes no stock. Therefore every R5
profile preserves all old primitives. Nonnegative stock energy requires
c>=0; integral stock energies further require integral c. This classifies
this declared additive profile class, not every possible physical energy.

With Pi the number of odd stocks, Hhat_c=Hhat_1+(c-1)Pi. Consequently the
exact old receiver change is f_c(r1')-f_c(eta'). All c give the same
one-step value exactly when r1' and eta' have the same parity.

G preserves each stock parity, and the full contact rotates
(pi0,pi1,pieta) to (pieta,pi0,pi1). Three steps restore each block parity,
so every block's three-step energy change is independent of c. This is
the least universal positive window: suitable mixed parity triples change
a chosen block after one or two steps. It does not select the required
one-step energy or justify changing an apparatus's time resolution.

For any further map V that preserves Hhat_1,

```text
Hhat_c(Vs)-Hhat_c(s)=(c-1)(Pi(Vs)-Pi(s)).                    (R6)
```

Hence a single admitted parity-changing transition selects c=1 within
R5; a Pi-preserving map leaves the whole family. CONTACT constructs two
complete comparison laws with these different behaviours. Defining a
stock decrement to equal a PRESELECTED Hhat_1 difference is a valid
construction, not an independent physical selection of that energy.

If P,Q are bijective words of old primitives, then
Hhat_c P V Q=Hhat_c iff Hhat_c V=Hhat_c: remove P by invariance and Q by
surjectivity. This is an all-carrier statement, not an assertion for an
arbitrarily restricted ready-state subset. Also, a helper returned to
its original Pi cannot change the system's Pi if their total Pi is
conserved. Merely enlarging such a helper does not remove R6's obstruction.

## R6. Readout after a new local contact

Let V be a bijection of the receiver cell alone, preserving the fixed
cell energy and leaving eta,p fixed. For T_V=V T, let u=V^(-1)c1'. Then

```text
d=(m(u),b(u),T_f^(-1)z(u),eta'),  c1_before=G(d),
Delta E1=r(u)-eta',
Delta rho1=rho(c1')-rho(u).                                 (R7)
```

The pointer formulas R4 apply unchanged with this reconstructed input.
R7 follows by removing V first; its zero cell-energy change leaves R3's
transfer. The old layers preserve each actual node charge, which proves
the rho formula also for nonzero Gauss defects. For CONTACT's W_j,
V^(-1)=W_j. This supplies a mathematical readout for each chosen law;
the old pointer records G's event, not an additional charge-transfer event.

Without V's energy preservation the reconstruction still works, but the
energy change has the extra term E1(c1')-E1(u). If V accesses hidden blocks,
even the reconstruction may fail. For example, append old contact A to T.
On zero-matter/zero-field inputs (0,k,0), the stock history is
(0,k,0)->(0,0,k)->(k,0,0). The output receiver, link and pointer coincide
for all k but Delta E1=-k. A T is nevertheless a conservative bijection.

## R7. What the original native system can cover

The canonical U is defined on Omega=N_0 times F5^6. Let D be precisely
the states reachable from all time-zero preparations. Source A's theorem
U-COUNTER-REACHABLE-AMPLITUDE-CLASS says that for ANY target bijection L,
all R with R U=L R on D have the form

```text
R(n,x)=L^n G0(ell_n(x)),  G0:F5^5 -> target.
```

The counter is included and unbounded. Taking L=id proves the new
corollary that every conserved real-valued point readout on D has at
most 3125 values. Thus a surjection Phi from D onto a selected model with
infinitely many conserved energy values cannot satisfy both
Phi U=T Phi and E T=E: E Phi would have finite image although surjectivity
requires E's infinite image. The cell chain has arbitrarily high energies
already on zero-matter preparations with one variable reserve.

This excludes that particular onto, conserved, instantaneous bridge from
D. It does not exclude a selected finite energy sector, different permitted
preparations, history/ensemble interfaces, an extended native carrier or
other integer physics. No classification on the whole Omega is asserted
by this corollary; the canonical all-Omega separable theorem is different.

For a second boundary, set O=Z[zeta5], J=1+zeta5^2 and
S(alpha)=Tr(alpha conjugate(alpha))/2. If A U=J A on D, at most 3125
forward J-orbits occur. Since J^(-1)=-zeta5-zeta5^2 belongs to O, the
whole bilateral orbit stays integral. For nonzero beta the two conjugate complex pairs
give S(J^n beta)=a lambda^n+b lambda^(-n), a,b>0,
lambda=(3+sqrt5)/2. Hence the integer sequence satisfies
t_(n+2)=3t_(n+1)-t_n and tends to infinity in both directions. It has a
minimum t_k>=2: positivity and
2S=5 sum_i c_i^2-(sum_i c_i)^2, c in Z^4, imply integrality; S=1 is
excluded modulo 5 because 2S is the negative of a square.
From a minimum, recurrence gives t_(k+/-r)>=2^r for r>=1. Therefore

```text
#{n in Z: t_n<=B} <= 2 floor(log2 B)+1, B>=2.
#{S(A(D)) in [0,B]} <= 1+3125(2 floor(log2 B)+1).             (R8)
```

The zero orbit contributes at most one value. Thus S(A(D)) cannot contain
every 5N+2, N>=0. For example, at B=1,000,000 the upper bound is 121,876,
whereas there are 200,000 required values 5N+2 in that interval.
This conclusion does not need a
theorem identifying the complete arithmetic image S(O). In particular,
arithmetic availability of separate values and coverage by a prescribed
native trajectory are distinct questions. Exact J-equivariance alone
has solutions, such as A(n,x)=J^n; only the proposed joint coverage fails.

## R8. A representation is not a phase-sensitive instrument

This section restates the narrow mechanism of source Q in a finite
comparison space; it is not a derivation of a quantum state or Born law.
Write Delta for deleting off-diagonal matrix entries in a fixed complete
configuration basis. A monomial unitary M|a>=u_a|pi(a)> with |u_a|=1
obeys Delta(M rho M*)=M Delta(rho) M*. A diagonal outcome filter K has
Delta(K rho K*)=K Delta(rho) K*. Thus recorded basis outcomes depend only
on the initial diagonal. Induction on finite recorded histories preserves
this property under adaptive choices based on earlier records, classical
mixtures, tensoring a common independent auxiliary state and discarding
registers. For the auxiliary step the common full diagonals are equal
because Delta(rho tensor sigma)=Delta(rho) tensor Delta(sigma).

Let j=exp(2pi i/5) and let |f>, |g> be distinct configuration basis vectors.
Accordingly, the conditional quantum preparations
psi_+/-=(|f>+j^(+/-1)|g>)/sqrt2 have identical record laws in this class,
yet the comparison score W=[[0,-i/2],[i/2,0]] on their ordered span,
extended by zero on its orthogonal complement, has means +/-w,
w=sin(2pi/5)/2>0. A record estimator with finite expectation has one
common mean v, so max(|v-w|,|v+w|)>=w. Memory alone within this class
cannot supply this phase-sensitive score. Supplied coherence can still
be moved between registers; other integer encodings and different
microscopic preparation laws are outside the theorem.

Neither the two integer contacts in CONTACT nor the surface in GEOMETRY
is thereby identified with the Hilbert-space Hamiltonian of source H.
That identification requires its own complete state, dynamics and
observable map. Quadratic wave branches also do not prove a massless
phase of the full compact model. Those physical questions remain open.
