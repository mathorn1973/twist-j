### DEF-U-ION-HODGE-READOUT-DOMAIN

The following L1 statements compare specified readings with the native law
and one fixed marked Hodge direction. They distinguish an exact algebraic
comparison from the availability of its physical preparation, interaction,
measurement and decoder. The source native law in section 2 is retained.
For x=(p1,p4,p1p,p4p,q,r), all checkpoint arithmetic is in F5:

```text
theta_n=popcount(n) mod2,
j_n(x)=p1+p4+p1p+p4p+q+r+2theta_n mod5,
U(n,x)=(n+1,g_(j_n(x))(x)),
(g_0,g_1,g_2,g_3,g_4)=(a,b,c,d,e),
a(x)=(p4,p1,p4p,p1p,q,r),
b(x)=(-p1p,-p4p,-p1,-p4,-q,-r),
c(x)=(2-p1p,1-p4p+r,2-p1,1-p4-r,1-q,-r),
d(x)=(2-p1,1-p4,3-p1p,4-p4p,1-q,1-r),
e(x)=(2-p1,1-p4,3-p1p,4-p4p,2-q,1-r).
```

Use the seventeen five-level ion factors in the fixed order

```text
0:S1, 1:S2,
2:R1.p1, 3:R1.p4, 4:R1.p1p, 5:R1.p4p, 6:R1.q, 7:R1.r,
8:R2.p1, 9:R2.p4, 10:R2.p1p, 11:R2.p4p, 12:R2.y, 13:R2.r,
14:M1, 15:M2, 16:N.
```

The R2 dictionary is y=q-1 mod5, so its physical selector is
sum(P)+y+r+1+2theta_n and its branches are obtained by conjugating the
displayed maps by this fixed shift. All other labels are direct. The
supplied ready-memory family is
I(s,t)=(1,t,(0,0,0,0,s,0),(0,0,0,0,0,0),0,0,0), s,t in F5.
The comparison family X_n(s,t), n=1,2,3, is specified completely below.
Each R column contains six coordinates in the displayed order; every
row includes all seventeen ion factors. Each allowed s and t is
expanded separately, including rows with identical receiver tuples.

| n | s | S1 | S2 | R1 | R2 in physical labels | M1 | M2 | N |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 0 | 1 | t | (0,0,0,0,0,0) | (0,0,0,0,3,0) | 0 | 1 | 1 |
| 1 | 1 | 1 | t | (0,0,0,0,4,0) | (0,0,0,0,3,0) | 1 | 1 | 1 |
| 1 | 2 | 1 | t | (2,1,2,1,4,0) | (0,0,0,0,3,0) | 2 | 1 | 1 |
| 1 | 3,4 | 1 | t | (2,1,3,4,3,1) | (0,0,0,0,3,0) | s | 1 | 1 |
| 2 | 0 | 1 | t | (2,1,2,1,1,0) | (0,0,0,0,0,0) | 0 | 1 | 2 |
| 2 | 1 | 1 | t | (0,0,0,0,1,0) | (0,0,0,0,0,0) | 1 | 1 | 2 |
| 2 | 2 | 1 | t | (0,0,0,0,2,0) | (0,0,0,0,0,0) | 2 | 1 | 2 |
| 2 | 3,4 | 1 | t | (2,1,3,4,2,4) | (0,0,0,0,0,0) | s | 1 | 2 |
| 3 | 0 | 1 | t | (0,0,1,3,1,1) | (2,1,3,4,4,1) | 0 | 1 | 3 |
| 3 | 1,2 | 1 | t | (2,1,3,4,0,1) | (2,1,3,4,4,1) | s | 1 | 3 |
| 3 | 3,4 | 1 | t | (0,0,0,0,4,2) | (2,1,3,4,4,1) | s | 1 | 3 |

The n=1 receiver tuples follow from the actual selectors at theta_0=0;
the table's next two transitions follow by substitution at theta_1=
theta_2=1. Its fifty edges are X_n(s,t)->X_(n+1)(s,t), n=1,2.
There is no closing n=3->1 edge or intervening contact. The extended
map F on this domain applies native U to both receivers, retains S1,S2,
M1,M2 and advances the displayed counter. Its seventy-five states remain
distinct because M1=s, S2=t and N=n. This is a partial mathematical
continuation with occupied archive, not a synthesized ion operation.
The finite physical N does not supply the source's unbounded counter.

Let L_H denote the four-dimensional restriction in
J-HODGE-PREDICTIVE-CLOSURE, J-HODGE-HERM2-LOXODROME and
J-HODGE-SEMILINEAR-MEMORY, rather than the full exterior operator L.
Over K=Q(sqrt5), and in its real embedding, a suitable basis gives

```text
L_H = [[phi,-1,0,0], [1,0,0,0], [0,0,3,-1], [0,0,1,0]],
phi=(1+sqrt5)/2,
char(L_H)=(z^2-phi*z+1)(z^2-3z+1).
```

The periodic eigenvalues are exp(+/-i*pi/5), of order ten, and the axial
eigenvalues are (3+/-sqrt5)/2. Thus L_H and L_H^q-I for nonzero integers
|q|<=9 are invertible. The four-dimensional predictive minimum concerns
the stated K-linear class and fixed marked direction. It is not an
unrestricted encoding bound, physical dimension or physical-time claim.

### U-HODGE-FAITHFUL-DIRECT-MEMORY [T]

Let pi:X->D forget added state while retaining the complete original data
and counter. Let F:X->X, U:D->D and Omega subset X satisfy
pi(Fx)=U(pi x) on Omega. For fixed r:D->K, let the axial present reading
y_ax=r pi hold on Omega union F(Omega), and let m:X->K be fixed.
Then on Omega

```text
y_ax(Fx)=3y_ax(x)-m(x)
    if and only if
m(x)=bar_m(pi x), where bar_m(d)=3r(d)-r(Ud).
```

**Proof.** Substitute y_ax=r pi and pi F=U pi in the first equation to
obtain m=3r pi-r U pi. Conversely that formula gives the first equation
by the same substitutions. Therefore m is constant on every pi-fibre
within Omega. No linearity, injectivity, reversibility or unitary premise
is used. State semantics must remain fixed; forgetting configuration
entries is not silently identified with a Hilbert projection or partial
trace.

If both axial equations y_ax F=3y_ax-m and m F=y_ax hold on Omega, put
Omega_2={x in Omega:F(x) in Omega}. Applying the forced formula at Fx
and the second equation at x gives, with d=pi x,

```text
3r(Ud)-r(U^2d)=m(Fx)=r(d),
r(U^2d)-3r(Ud)+r(d)=0 on pi(Omega_2).
```

No two-step condition outside that domain follows. On a partial domain
the recurrence alone need not make boundary values of m compatible.
In the specified ion family, X_n(3,t) and X_n(4,t) have equal original
data and counter but distinct archive labels. Direct identification is
excluded only if both belong to the faithful continuation domain and a
declared K-valued reading distinguishes their m values. Distinct physical
levels 3 and 4 do not themselves define those Hodge values. The axial
variable y_ax is unrelated to the label called R2.y. This result restricts
direct identification, not retained history or every memory-dependent
reading of the present. It does not establish the other Hodge coordinates.

### ION-LS-CONNECTED-RESPONSE [T]

Adopt the conditional diagonal completed-loop model on the seventeen
factors, with real nonscalar profile D_i=diag(d_0,...,d_4), fixed complex
geometric factors c_i, eta,delta>0 and intensity lambda>0:

```text
A=lambda*sum_i c_i D_i,
kappa=pi*eta^2/(2delta^2),
Theta=kappa*A A^dagger+sum_i L_i,
U_loop=exp(-i Theta) tensor I_motion.
```

The L_i are fixed integrated diagonal local residuals. The duration is
2pi/delta. This is an adopted harmonic single-mode, phase-tracked
effective model, not a calibrated all-mode apparatus. On the six required
edges {14,i_k}, use response indices k=1,...,6 and physical ion indices
i_k=k+1, so g_k=Re(c_14 conjugate(c_(i_k)))!=0. Geometry,
profile and optical settings are independent physical inputs, not knobs
fitted to the Hodge target. Put a_j=d_j-d_0 and

```text
B=5sum_j d_j^2-(sum_j d_j)^2=sum_(i<j)(d_i-d_j)^2>0,
Z_k=(D_M1-d_0 I)(D_R1,k-d_0 I)/B.
```

For memory label u and partner label x, hold all other labels, optical
settings and local profiles fixed. The exact connected phase is

```text
C_k(u,x)=Theta(u,x)-Theta(u,0)-Theta(0,x)+Theta(0,0)
        =2*kappa*lambda^2*g_k*a_u*a_x.
```

**Proof.** Expand
AA^dagger=lambda^2[sum_i |c_i|^2D_i^2+
2sum_(i<j)Re(c_i conjugate(c_j))D_iD_j]. The four-setting subtraction
cancels every self term, local residual, spectator term and other pair
term. The selected product leaves exactly (d_u-d_0)(d_x-d_0).
This is a contrast across settings, not an isolated interaction in one
raw loop. Its formula selects the response independently of L_H.

If the independently admitted intensity is
lambda_k=delta/[eta sqrt(50B|g_k|)], then

```text
C_k(u,x)=pi*sign(g_k)*Z_k(u,x)/50,     |Z_k(u,x)|<=1.
```

Indeed a_j^2<=B, so |a_u a_x|<=B. The unitary phase is -C_k; its
principal value has no modulo-2pi ambiguity at this intensity. No
measurement precision or device-error bound follows. Also
B=5sum_j(d_j-bar_d)^2, bar_d=sum_j d_j/5, and Z is invariant under
d_j->alpha*d_j+beta, alpha!=0. This preserves the response, not the
whole Hamiltonian, excursions, stationary phases or intensity constraints.
The full refocused equality-phase observable is a different response.
Its additional subtraction introduces zero-level populations and is not
silently included in this six-response class.

### U-ION-HODGE-AFFINE-OBSTRUCTION [T]

On the specified checkpoints Z_k=a_s a_(R1,k)/B. Allow all fixed real
affine four-vector readings

```text
R(X)=v_0+sum_(k=1)^6 v_k a_s a_(R1,k),      v_0,...,v_6 in R^4.
```

The common B and known nonzero edge factors are absorbed into the
coefficients. They may depend on a calibrated profile but are fixed
across inputs and boundaries. If a_1*a_2*(a_1-a_2)!=0, requiring
R(FX)=L_H R(X) on all fifty edges forces R=0 at all seventy-five
checkpoints. It does not force every coefficient or the global observable
to vanish, and it does not cover nonlinear processing.

**Proof.** At s=0 all three readings are v_0, hence v_0=0 because I-L_H
is invertible. Define H=a_2v_1+a_1v_2+a_3v_3+a_4v_4+a_1v_6.
For s=1,2 the readings at n=2,3 are respectively
(a_1^2v_5,a_1H) and (a_2^2v_5,a_2H). The two edge equations give
H=a_1L_Hv_5=a_2L_Hv_5. Nondegeneracy and invertibility force v_5=H=0.
Both histories vanish at all boundaries, using invertibility backwards
to n=1. For s=3,4 the n=1 reading is a_s(H+a_3v_5)=0; intertwining
propagates zero through their next two boundaries. This covers every s,t.

A sharper necessary condition follows when a_1!=0. Its first edge gives
(a_1I-a_4L_H)v_5=0. If this matrix is invertible, the same reasoning
forces all checkpoint readings to zero. Its periodic eigenvalues are
nonreal; consequently a nonzero reading with a_1!=0 requires

```text
a_4!=0,  a_1^2-3a_1a_4+a_4^2=0,  a_2 in {0,a_1}.
```

These conditions are necessary, not sufficient. Nonscalarity of d alone
does not imply affine nondegeneracy. The exceptions cannot be dropped:
for a=(0,0,0,1,2) and arbitrary w in R^4, the coefficients

```text
v_0=v_1=v_2=v_4=0,
v_5=L_H^2w/2, v_3=w-L_H^2w/2,
v_6=(L_Hw-w+L_H^2w/2)/2
```

give zero on s=0,1,2, the sequence (w,L_Hw,L_H^2w) on s=3 and twice
that sequence on s=4. Substitution into the checkpoint table proves this
example. Its coefficients encode the target; it supplies an algebraic
counterexample to an all-profile prohibition, not a physical decoder.

For any fixed profile covered by the obstruction, let E_val map the 28
coefficients to the 300 checkpoint components, and E_step map them to
the 200 edge residuals. The theorem is ker(E_step) subset ker(E_val).
The Moore-Penrose inverse therefore gives

```text
E_val=E_val E_step^+ E_step,
||E_step theta||_2 >= eta_res ||E_val theta||_2,
eta_res=||E_val E_step^+||_2^(-1)>0.
```

E_val is nonzero because constant scores have nonzero checkpoint values;
the factor is consequently nonzero and finite. This is a relative bound
in the declared real coordinates and stacking, not a universal numerical
error floor. An absolute floor needs a separately fixed output norm.
Continuity also extends zero to an exceptional limiting profile with
B_*>0 when each checkpoint reading is continuous at that limit and the
approaching admissible readings are affine, satisfy every exact edge
equation and have nondegenerate profiles tending to it. A physically
restricted profile family need not provide such an approach.

### U-ION-HODGE-RESPONSE-FIBRE-CLASSIFICATION [T]

Let f be any fixed function of the six-vector Z alone, with values in
R^4. It receives no level labels, t, counter, history or extra detector
record. For a fixed profile, its possible checkpoint values are classified
exactly as follows. With a=a_1,b=a_2,c=a_3,d=a_4, the thirteen response
rows, before dividing by their common B, are

| s | n | B Z(X_n(s,t)) |
| --- | --- | --- |
| 0 | 1,2,3 | (0,0,0,0,0,0) |
| 1 | 1 | (0,0,0,0,ad,0) |
| 1 | 2 | (0,0,0,0,a^2,0) |
| 1 | 3 | (ab,a^2,ac,ad,0,a^2) |
| 2 | 1 | (b^2,ab,b^2,ab,bd,0) |
| 2 | 2 | (0,0,0,0,b^2,0) |
| 2 | 3 | (b^2,ab,bc,bd,0,ab) |
| 3 | 1 | (bc,ac,c^2,cd,c^2,ac) |
| 3 | 2 | (bc,ac,c^2,cd,bc,cd) |
| 3 | 3 | (0,0,0,0,cd,bc) |
| 4 | 1 | (bd,ad,cd,d^2,cd,ad) |
| 4 | 2 | (bd,ad,cd,d^2,bd,d^2) |
| 4 | 3 | (0,0,0,0,d^2,bd) |

These follow by substitution into the complete checkpoint table. The
five t values only repeat observations and edges. Merge exactly equal
rows into vertices and retain each distinct directed edge induced by
the native transitions, including self-loops and distinct outgoing edges.
The quotient is not assumed to have a single-valued update. If q counts
its connected components admitting integer heights h_v with
h_v=h_u+1 on every edge u->v, the compatible reading-value space has
dimension 4q. Every other component is zero, including the component
containing the zero response. A nonzero axial value exists exactly if q>0.

**Proof.** A fixed f gives one vector r_v per response vertex. Its full
condition is r_v=L_Hr_u on every edge, which is also sufficient to define
f on the finite response set. On an undirected spanning tree,
invertibility gives r_v=L_H^(h_v)w. Each additional edge imposes
(L_H^(h_u+1-h_v)-I)w=0. Zero defects permit any w in R^4. A nonzero
defect has magnitude at most its fundamental cycle length. There are
at most nine distinct edges: one zero self-loop and eight edges from
the other four histories. Hence its magnitude is at most nine, and
the stated spectrum forces w=0. Parallel copies add no equations;
opposite edges and loops are included. The zero vertex's self-loop
kills its component. Independent components contribute independent w,
which may have nonzero axial part. This proves the classification.

Generically the twelve other rows are nonzero and pairwise distinct.
For example a=(0,1,2,3,5), B=74, gives distinct rows directly in the
displayed table. Therefore every undesired equality is a proper
polynomial zero set. Off their finite union, the graph is the zero
self-loop and four disjoint two-edge paths, so q=4 and the dimension
is sixteen. This is open dense and full Lebesgue measure in the
unrestricted four-dimensional parameter space, not a physical occurrence
law or a statement about the admissible optical parameter family.

The contrasting profile a=(0,1,-1,-1,1), B=20, satisfies the same affine
nondegeneracy condition but has q=0. The first two s=1 responses coincide
at e_q/20, and the middle s=2 response is the same point. Its self-loop
kills both paths. The first two s=3 responses coincide at
(1,-1,1,-1,1,-1)/20; those of s=4 coincide at its negative. These two
loops kill both remaining paths, and s=0 is zero. Thus every compatible
f vanishes on this family. These profiles are algebraic witnesses, not
calibrated devices or prescriptions for tuning to a target.

A same-history return Z(X_3)=Z(X_1) would force zero through L_H^2-I.
Under a_1a_2(a_1-a_2)!=0 no nonzero such return occurs: the first
coordinate distinguishes s=1, the last distinguishes s=2, and the first
coordinate forces a_3=0 or a_4=0 for s=3 or s=4. Those latter histories
are then entirely zero. Outside that condition a=(0,0,1,1,0), B=6,
has s=2 endpoints (1,0,1,0,0,0)/6 and middle e_q/6, a literal two-cycle.

Every assignment at distinct response points p_i extends to a polynomial,
for example f(z)=sum_i r_i product_(j!=i)
||z-p_j||_2^2/||p_i-p_j||_2^2. This interpolation demonstrates only finite
compatibility. It supplies no independent selection of scores. The
dimension counts concern observed values, not arbitrary extensions away
from them. Exact equality cannot be replaced by a noise tolerance without
a new error contract. The nine-edge rule does not extend unchanged to
longer graphs: a defect of ten can preserve the periodic plane.

### U-ION-HODGE-MEAN-SUFFICIENCY [T]

For the conditional joint level measurement on M1 and R1, define on the
ion-state Hilbert space H_int=(C^5)^tensor17

```text
P_alpha=|u,x_1,...,x_6><u,x_1,...,x_6| tensor I_other,
z_k(alpha)=a_u a_(x_k)/B,
Q_z=sum_(alpha:z(alpha)=z) P_alpha,
O_j=sum_z f_j(z)Q_z,                         j=1,...,4.
```

The finite scores are fixed on the entire admitted response spectrum,
not only at checkpoints. The Q_z are orthogonal and sum to identity;
the O_j are commuting bounded Hermitian operators. Under the adopted
quantum probability rule Tr(rho Q_z), scoring each joint shot and then
averaging gives R_shot(rho)=(Tr(rho O_j))_j. It is mixture-linear for
every nonlinear f. The Born rule here is an external measurement premise,
not a consequence of native U or J. Replacing this procedure by
g((Tr(rho Z_k))_k) is a distinct ensemble contract.

Let z_1,...,z_N be the distinct checkpoint responses, h_i=f(z_i),
Z=[z_1 ... z_N] and H=[h_1 ... h_N]. Form S by stacking a row of ones
above Z. On the full probability
simplex of these points, including cross-boundary mixtures, the following
are equivalent:

```text
Hp=g(Zp) for some fixed g and every probability p;
ker(S) subset ker(H);
H=c*1^T+A*Z for common c in R^4 and A in R^(4x6).
```

**Proof.** For nonzero v in ker(S), its positive and negative parts have
the same positive mass t. The probabilities v_+/t and v_-/t have the
same Z mean. Mean sufficiency forces their H means equal, so Hv=0.
Kernel inclusion then factors H linearly through im(S); extending this
map to R^7 gives [c A]. Conversely an affine map supplies g on the convex
hull. No regularity assumption is needed. This affine map is unique on
aff{z_i}; its coefficients on R^6 are unique exactly when rank(S)=7.

Consequently, at a profile with a_1a_2(a_1-a_2)!=0, a score reading that
satisfies every Hodge edge equation and is sufficient from the six means
must vanish at every checkpoint, by the affine obstruction. A compatible
reading nonzero on this family therefore distinguishes some two mixtures
with the same six means. Ordinary quantum mixture-linearity alone does
not impose mean sufficiency. If only within-boundary mixtures are
admitted, separate affine representations may suffice; no common global
affine coefficients follow on that basis alone. Availability of the full
cross-boundary mixture domain is a separate preparation assumption.

For fixed f, four running sums of f_j(z) and a positive sample count
suffice to compute its empirical average within specified numerical
precision; grouped tests use separate accumulators. This implies no
independence, confidence bound, minimal statistic or complete retained
history. A histogram permits later arithmetic but cannot make a score
chosen from target data independently selected. Finite-precision error,
overflow, invalid-record treatment and classical storage remain explicit.

### U-ION-HODGE-SCORED-CODE-TRANSPORT [T]

Let C_n span the twenty-five complete orthonormal checkpoints at boundary
n and let Pi_n be its projector in H_int. Suppose a unitary V_n has the
independently specified action

```text
V_n|X_n(s,t)>=exp(i theta_(n,s,t))|X_(n+1)(s,t)>,     n=1,2.
```

For the fixed diagonal score operators above, the basis-value equations
f(Z(X_(n+1)))=L_H f(Z(X_n)) imply the restricted operator-action identity

```text
(V_n^dagger O_j V_n-sum_k (L_H)_(j,k) O_k) Pi_n=0.
```

**Proof.** Every output checkpoint is an eigenvector of O_j with
eigenvalue f_j(Z(X_(n+1))). Applying V_n^dagger returns its input
checkpoint with the phases cancelled. The right-hand combination acts
on that same input with eigenvalue sum_k(L_H)_(j,k)f_k(Z(X_n)). These
values agree by hypothesis; linearity proves the identity on C_n.
Compression on both sides follows, and expectations obey the same
step for every density operator supported on C_n, including coherences
and mixtures. Diagonal scores cannot themselves verify that coherence
was preserved. The identity is not asserted outside the input code.

Tensoring scores with identity on a retained remainder keeps them bounded,
but a correlated physical remainder requires a specified joint support
and evolution before making the corresponding transport claim. No fresh
common remainder or restored work source is inferred. The unitary
hypothesis is not supplied by merely writing the partial native table.
There is no global all-time identity V^dagger O V=L_H O and no conflict
with the bounded-observable obstruction to such hyperbolic identities.

For a measured continuation, effects Q_z alone are insufficient. One
must declare completely positive instrument maps I_z whose sum is trace
preserving, their physical input/output systems, and

```text
Tr I_z(rho)=Tr(rho Q_z),
rho'_z=I_z(rho)/p_z for p_z=Tr I_z(rho)>0,
Omega'=sum_z I_z(rho) tensor |z><z|_C.
```

The next apparatus map acts on this actual postmeasurement state and
retained record, not automatically on rho. Both Q_z rho Q_z and
Tr(rho Q_z)*sigma_z for fixed normalized output states have effects Q_z
but different disturbance. These mathematical instruments provide no
free blank records, detectors, work, resets or nondemolition property.
Feedback and any traced-out degrees require their own faithful-domain
account. Separate endpoint preparations and one measured continuing
apparatus are distinct contracts. The code theorem describes unmeasured
coherent evolution unless insertion of an instrument is separately justified.

All six claims retain the stated mathematical or conditional effective-model
scope. No numerical profile, jointly calibrated geometry, implemented
instrument, selected four-coordinate decoder, continuation pulse word or
accumulated error bound is established. Preparation, admitted remainder,
finite work/controller resources and independently fixed statistical tests
remain physical obligations. Existing physical-HOLD owners and their scope
are unchanged; none of these statements identifies physical time or derives
the adopted apparatus and measurement laws from native U or J.
