# Conservative finite chain with a local reversible work record

NON-CANONICAL / proposed conditional L1 theorem. This is an editorial
consolidation and audit of exposed mathematics, not a new discovery, a new
formal experiment, or a statement of physical realization. Public Canon v95
remains authority. The exact source custody is in DEPENDENCIES.tsv; claim
dispositions and exclusions are in CLAIM_MAP.tsv and DELTA.md.

Three results suffice: the conservative full-state law (Sections 1-5, 9),
first transferred work on every finite chain with its controls (Sections 6-7),
and its reversible local record (Sections 4, 8). All assertions below are
proved from the displayed definitions. No predecessor executable, missing
archive, count of successful examples, or unstated quotient is a premise.
The definitions are selected architecture; their mathematical consequences
are theorems conditional on that architecture. They are not deductions of
the architecture from native U or the axiom J.

## 1. Complete carrier, actual charge, and energy

Fix an integer N>=2, with receiver t=N-1. Cell i stores

```text
ci=(mi,bi,zi,ri),
mi=(mi0,mi1,mi2) in (Z^4)^3,
bi=(bi0,bi1,bi2) in (Z^4)^3,
zi=(Ei,Mi) in Z^4 x Z^2, ri in Z_{>=0}.
```

The three reacting registers mi are ordered and reside at actual electric
vertex 0; spectator bij resides at vertex j. Each cell has its own disjoint
electric vertices. Its ordered edges are (0->1,0->1,0->2,2->1), the first
two being distinct, and its ordered faces are e0-e1 and -e0+e2+e3.
The additional neutral integer channels qj>=0, j=0,...,N-2, are stored
between cells. They are not electric edges or charge currents. In order,

```text
s=(c0,...,c(N-1),q0,...,q(N-2)) in X_N,
shat=(s,p) in Xhat_N=X_N x C5, C5=Z/5Z, p in {0,1,2,3,4}.
```

The pointer p belongs only to the receiver. Literal equality includes every
ordered register, raw-field component, spectator, resource, old channel
content, and p. There are 31N+N-1=32N-1 original coordinates: 30N unrestricted
integers and 2N-1 nonnegative integers. The extension has exactly 32N stored
coordinates, one restricted to C5. At N=3 these are 95 and 96, respectively.
There is no extra stored branch bit, clock, counter, or unbounded history.

Use the +tail/-head divergence convention and the following selected forms:

```text
C=[[1,-1],[-1,0],[0,1],[0,1]],
D=[[1,1,1,0],[-1,-1,0,-1],[0,0,-1,1]], DC=0,
K=[[6,2,-1,2],[2,6,2,-1],[-1,2,6,2],[2,-1,2,6]],
Q(v)=v^t K v, chi(v)=sum_j v_j,
Hraw(E,M)=E^t E+M^t M+E^t C M,
Hcell(m,b,z,r)=sum_j Q(mj)+sum_j Q(bj)+Hraw(z)+r,
H_N(s)=sum_i Hcell(ci)+sum_j qj,
E_p(p)=1 for every p, Hhat_N(s,p)=H_N(s)+1.
```

The actual cell charge and Gauss defect, with 3N entries each globally, are

```text
rho_i=(chi(bi0)+sum_j chi(mij),chi(bi1),chi(bi2)),
delta_i=D Ei-rho_i.
```

They are functions of complete stored coordinates; the Gauss subset has
delta_i=0. Defect preservation will also hold outside that subset. Constant
pointer energy and its neutral charge are definitions, not measured costs.

K has eigenvalues 9 on the constant vector, 1 on the alternating vector,
and 7 on their orthogonal complement. Hence Q(v)>=||v||^2. Also

```text
C^t C=[[2,-1],[-1,3]],
4Hraw(E,M)=||2E+CM||^2+M0^2+(M0+M1)^2.
```

Vanishing forces M0=M1=0 and E=0. Hraw and Q are positive definite,
and all displayed energy accounts are nonnegative integers on the carrier.
Static fields, spectators, and zero-energy blocks remain stored.

## 2. Exact raw split, image, and field inverse

Write A_f for the active field matrix, avoiding confusion with contact A.
For y=(a,b,c,d), sigma=(u,v), define

```text
P(a,b,c,d)=(a-b,-a,b,b,c,d), S(u,v)=(u,u,v,u-v,0,0),
A_f=[[1,0,1,0],[0,1,0,1],[-2,1,-1,1],[1,-3,1,-2]],
B_f=[[4,-2,2,-1],[-2,6,-1,3],[2,-1,2,0],[-1,3,0,2]],
H(y)=y^t B_f y/2
    =2a^2-2ab+3b^2+c^2+d^2+2ac-ad-bc+3bd,
L=[[1,-3,-1,-2],[-3,4,-2,1],[0,5,1,2],[5,-5,2,-1]],
Vinv=[[1,2,1,2],[2,-1,2,-1],[0,-5,1,-3],[-5,5,-3,4]].
```

Here Vinv is the matrix called N in the predecessor field certificate;
renaming it avoids collision with the chain length. It is not L inverse
on all integer inputs: L inverse over Q is Vinv/5.

Solving z=Py+S sigma over Q gives, uniquely,

```text
a=(2E0-3E1+E2+E3)/5, b=(-E0-E1+2E2+2E3)/5,
c=M0, d=M1,
u=(2E0+2E1+E2+E3)/5, v=(E0+E1+3E2-2E3)/5.
```

Substituting these formulas in E=(a-b+u,-a+u,b+v,b+u-v) verifies
both inverse identities. With g=2E0-3E1+E2+E3, their electric numerators
are g,2g,g,3g modulo 5. Thus the split is integral iff g=0 modulo 5.
The E2 coefficient makes this residue map surjective, so the split lattice
has index 5 in the raw lattice. No rounding is admitted. PZ^4 and SZ^2
are individually saturated: (-E1,E2,M0,M1) is an integer left inverse
on the rational span of P; a static vector necessarily has E0=E1=u,
E2=v,E3=u-v,M=0. Their direct sum is nevertheless only the split lattice.

Direct substitution gives

```text
DP_E=0, C^t S_E=0,
DS_E(u,v)=(2u+v,-3u+v,u-2v),
Hraw(Py+S(u,v))=H(y)+3u^2-2uv+2v^2.
```

The last expression retains the static energy. H is positive definite by
injectivity of P and positivity of Hraw, and is integer on Z^4.

Define the full raw-field bijection and its inverse by

```text
T_f(E,M)=(E+CM,M-C^t(E+CM)),
T_f^-1(E',M')=((I-CC^t)E'-CM',M'+C^t E').
```

They are inverse integer shears. Setting a0=E+CM shows
Hraw(E,M)=||a0||^2+||M||^2-a0^t CM
=Hraw(a0,M-C^t a0); hence energy is preserved. DC=0 gives divergence
preservation. Substitution yields T_f P=P A_f, T_f S=S and
A_f^t B_f A_f=B_f. For a finite-order certificate use

```text
Jcyc=[[0,1,0,0],[0,0,1,-1],[1,-1,0,-1],[0,1,-2,1]],
Zcyc=[[0,0,0,-1],[1,0,0,-1],[0,1,0,-1],[0,0,1,-1]],
det Jcyc=-1, A_f Jcyc=Jcyc Zcyc.
```

Zcyc represents multiplication by t in Z[t]/(1+t+t^2+t^3+t^4), so
A_f^5=I. Since P and S span the rational raw space, T_f^5=I there
and hence on all raw integer states, including nonsplit states. This field
identity is not a period assertion for the coupled chain.

Multiplication of the displayed matrices, or reduction in that polynomial
quotient, gives

```text
L=(I-A_f)(I-A_f^2), A_f L=L A_f,
L^2=5 A_f^3, Vinv=A_f^2 L, Vinv L=L Vinv=5I.
```

For the B_f adjoint, A_f^*=A_f^-1 and therefore
L^*=(I-A_f^-2)(I-A_f^-1)=A_f^-3 L=A_f^2 L=Vinv.
It follows that L^t B_f L=5B_f and H(Lx)=5H(x). This uses the
energy adjoint, not the ordinary Euclidean transpose.

The complete integer image is certified by

```text
Vh=[[1,1,1,1],[2,1,2,1],[0,-1,1,0],[-5,-2,-3,-1]], det Vh=1,
L Vh=[[5,3,0,0],[0,1,0,0],[0,0,5,3],[0,0,0,1]].
```

Thus det L=25 and

```text
y=(a,b,c,d) in L Z^4 iff a+2b=0 mod5 and c+2d=0 mod5.
```

Indeed a-3b and c-3d must be divisible by 5 in the triangular image
above, and its coefficients ((a-3b)/5,b,(c-3d)/5,d) suffice. On that
image x=Vinv y/5 is integral and uniquely solves Lx=y; either matrix
product with L proves the inverse assertion. There are exactly 25 image
residues among the 625 four-coordinate residues modulo 5. This is a
residue calculation, not a complete energy-shell claim.

## 3. Literal funded reaction and every rejected branch

Let Z4 be the zero vector and define ordered triples

```text
R=((1,-2,1,0),Z4,Z4),
AM=((1,0,0,0),(0,-1,0,0),(0,-1,1,0)),
ZM=(Z4,Z4,Z4).
```

Their matter energies are 18,20,0. The complete reacting-vector sums for
R and AM both equal (1,-2,1,0). Their total charge is zero, but the
individual register charges change from (0,0,0) to (1,-1,0). All three
registers share vertex 0, so actual node charge is unchanged. A permuted
triple is accepted only if it literally equals one of the displayed
ordered triples; there is no quotient by permutation or phase. ZM is
not a reaction endpoint.

The following algorithm defines G on every complete local input:

1. Reject and retain the entire input if matter is neither literal R nor AM.
2. Compute the rational split above. Reject in full if it is not integral.
3. On R, require both image congruences on y; reject in full if either fails,
   otherwise set x=Vinv y/5. On AM, set x=y without an image requirement.
4. Set h=H(x). On R require r+4h-2>=0; on AM require r+2-4h>=0.
   A failed guard retains the entire input. On acceptance perform exactly

```text
G(R,b,PLx+S sigma,r)=(AM,b,Px+S sigma,r+4H(x)-2),
G(AM,b,Px+S sigma,r)=(R,b,PLx+S sigma,r+2-4H(x)).
```

No proposed change is committed before all relevant guards pass. Spectators
are arbitrary throughout, including charged and non-Gauss inputs.

Unique split, injective L, and distinct ordered matter labels give disjoint
endpoint pairs. Each accepted R output has a funded AM inverse because
(r+4h-2)+2-4h=r>=0, and conversely. The inverse field uses L and its
admitted exact preimage. Accepted pairs are therefore transpositions;
rejected inputs are singleton fixed points and cannot be accepted outputs.
This proves G^2=I on the full local carrier.

The accepted energy identity, with all omitted-looking terms restored, is

```text
18+5h+sum_j Q(bj)+Hstatic(sigma)+r
 =20+h+sum_j Q(bj)+Hstatic(sigma)+(r+4h-2),
Hstatic(u,v)=3u^2-2uv+2v^2.
```

The AM branch reverses it. At h=0, R needs two stored resource units and
AM releases two; at h=1, R deposits two and AM needs two. Rejection is
identity, so conservation and nonnegativity hold on all inputs. G retains
every spectator and reacting-vector sum. Its field changes only by an
element of PZ^4, whose electric divergence vanishes. Hence rho_i, DE_i,
and every delta_i are each separately preserved. Define
F(ci)=(mi,bi,T_f zi,ri); Section 2 gives the same invariants and its
integer inverse. A state fixed by G may still change under F or contacts.

## 4. Stored event and its recovered-input inverse

On a complete receiver input put

```text
e(c)=1 if matter(c)=R and matter(Gc)=AM, otherwise 0,
Ghat_t(c,p)=(Gc,p+e(c) mod5),
Ghat_t^-1(c',p')=(Gc',p'-e(Gc') mod5).
```

Thus e tests the actual accepted R branch, including split, image, and
funding, not merely a label, arrival, or a command. Every other primitive
fixes p. Recovering c=Gc' in the inverse gives e(Gc')=e(c), so both
Ghat_t^-1 Ghat_t=I and Ghat_t Ghat_t^-1=I follow by cancellation in
C5. This holds for every p and for accepted and rejected inputs, without
an external forward log.

Ghat_t is not an involution. For an accepted pair c_R,c_A,

```text
(c_R,p) -> (c_A,p+1) -> (c_R,p+1) -> ... -> (c_R,p+5)=(c_R,p).
```

The local orbit has exact length 10: matter forces an even return 2a,
and then the pointer forces a=0 modulo 5. The forward AM branch does
not subtract the earlier write; only the mathematical inverse does.
Rejected c retains both c and its old p.

## 5. Four layers, occupied contacts, cuts, and full projection

For every j=0,...,N-2 define complete swaps

```text
A_j=swap(rj,qj), B_j=swap(qj,r(j+1)).
```

Both inputs may be occupied. The pair (r,q) becomes (q,r), with energy
increments (q-r,r-q); all old content survives and nonnegativity is
preserved. Each swap is an involution. Fields and matter are untouched,
so every actual charge and defect remains unchanged.

Let Ghat apply G at cells i<t and Ghat_t at t, A apply all A_j,
B apply all B_j, and F apply all F_i. Supports within each layer are
disjoint. With rightmost factors acting first,

```text
forward chronology: Ghat; A; B; F,
That_N=F B A Ghat,
inverse chronology: F^-1; B; A; Ghat^-1,
That_N^-1=Ghat^-1 A B F^-1.
```

Adjacent inverse factors cancel in either composition. No commutation of
contacts with reactions is used. Thus every primitive, layer, macrostep,
and inverse preserves full energy Hhat_N, all spectators, each reacting
vector sum, all 3N actual charges, all 3N divergences and defects, and
nonnegative resources. The new pointer's constant energy and neutrality
make these original accounts unchanged.

For the original law T_N=F B A G and projection pi(s,p)=s, each
extended primitive projects to its original primitive, including
pi Ghat_t^-1=G pi. Therefore each forward and inverse layer projects
exactly and pi That_N^k=T_N^k pi for every integer k. This statement
holds on the full carrier, not only a successful preparation.

For a fixed cut j, replace both A_j and B_j by identity at every step.
Keep the stored old qj, now fixed. These omissions give another complete
bijective law with the same proofs of inverse, invariants and projection
onto the corresponding original cut law. A cut neither erases qj nor
changes dynamically in response to a reader.

If rhat_i denotes post-G resources and qj the old channels, uncut contacts
give the exact resource permutation

```text
r'_0=q0,
r'_i=rhat_(i-1) for 1<=i<=N-1,
q'_j=q_(j+1) for 0<=j<=N-3,
q'_(N-2)=rhat_(N-1).
```

The middle channel range is empty at N=2. For N=3 this sends
(rhat0,rhat1,rhat2,q0,q1)=(a,b,c,u,v) to (u,a,b,v,c).
For example (0,1,2,3,4) goes to (3,0,1,4,2); no old value is lost.
Copying into an occupied channel or clearing it is a different, generally
noninjective operation. Interchanging A and B is also a different law.

On the stored-block path C0--Q0--C1--...--Q(N-2)--C(N-1), Ghat and F
have radius 0, and A,B are radius-1 matchings. Each complete step, in
either direction, has dependence radius at most two graph edges. The
sequential depth is four for every N. This is a support bound on declared
blocks, not a one-electric-edge implementation or physical speed theorem.

## 6. First arrival, first work, and old-receiver return for every N

For every integer w with H(w)=1 prepare

```text
c0(0)=(R,0,PLw,0),
ci(0)=(ZM,0,0,0) for 1<=i<=N-2,
ct(0)=(R,0,0,0), qj(0)=0 for all j, p(0)=0.
```

Zeros mean all relevant components, including spectators and raw fields.
This family is nonempty, e.g. w=(0,0,1,0). The source has energy
18+5=23 and the ready receiver 18, so H_N=41 and Hhat_N=42 for every
N. No energy proportional to distance is hidden; the stored dimension
does grow with N. All actual charges and defects are initially zero.

At step 1 the source's h=1 R branch produces AM, field Pw and resource
2. ZM intermediates reject. The receiver's h=0 R branch lacks the two
units and rejects. Contacts move the source's two units into r1 and F
sends its field to P A_f w. This includes N=2, where cell 1 is already
the receiver and its G has occurred before arrival.

Inductively, at each boundary 1<=k<=N-1 the complete original state is

```text
source matter AM, source field P A_f^k w, source resource 0;
intermediate matter ZM, receiver matter R;
all other fields and every spectator zero;
ri=2 exactly when i=k, all other ri and all qj zero.
```

For k<N-1 the loaded cell is intermediate and ZM cannot react. The
source's AM branch has H(A_f^k w)=1 and resource 0, so it rejects the
proposed resource -2. The receiver remains unfunded. The resource
permutation advances two units to r_(k+1), and F advances the source
phase. This proves the induction, including repeated field phases. At
N=2 its induction interval is empty and the initial step already suffices.

Boundary N-1 is the first positive receiver resource, still with matter R.
In step N its h=0 R branch consumes precisely two units, produces AM
and resource zero, and increments p to 1. All resources and channels are
then zero. Its first arrival is N-1 and first reaction/write is N. These
are exact first times for this preparation and schedule, not optimal times
over different architectures.

In step N+1 the receiver AM input has zero active field and resource 0.
Its inverse matter branch gives R and resource 2, with e=0. A never
touches the last cell's resource; B puts these units in q_(N-2). The
source's reverse is still unfunded during G. The complete boundary is

```text
source AM, field P A_f^(N+1) w, resource 0;
all intermediate ZM and receiver R;
all other raw fields and spectators zero;
all cell resources zero;
q_(N-2)=2, all other channels zero; p=1.
```

Thus the original receiver's entire 31-coordinate tuple has returned to
readiness at N+1. Its extended block differs by p=1. This also covers
N=2, with only q0 present. No closed formula beyond N+1 for every old
coordinate is needed or asserted; exact base projection continues to hold.

The full energy accounts are initially 23+18+1=42; during transfer
21+18+2+1=42; at arrival 21+(18+2)+1=42; after paid work 21+20+1=42;
after the local reversal 21+18+2+1=42, with 2 now in the last channel.
The pointer's constant unit does not finance receiver work. Positivity,
divergence-free active fields, and fixed reacting sums preserve all zero
charges and defects through each primitive.

The same algebra retains arbitrary admitted static fields and spectators.
For the pinned charged N=3 witness use S(1,0),S(1,0),S(0,1) and
spectators (2e0,-3e0,e0),(2e0,-3e0,e0),(e0,e0,-2e0), respectively.
Their spectator energies are 84,84,36, static energies 3,3,2, and charges
(2,-3,1),(2,-3,1),(1,1,-2), equal to their divergences. The original
energy vectors (H0,H1,H2,q0,q1) through k=3 are
(110,87,56,0,0), (108,89,56,0,0), (108,87,58,0,0),
(108,87,58,0,0), each totaling 253; with p they total 254.
This is retained evidence for the same invariant accounts, not a new
physical identification or a new general preparation claim.

## 7. All-time equal-energy offimage and every individual cut

Replace only the source active coordinate Lw in the neutral preparation by
y_minus=(0,0,1,-2). Direct substitution gives H(y_minus)=5, equal to
H(Lw), but c+2d=-3 is nonzero modulo 5. This is the specified offimage
control, not a choice among other energy-five vectors.

A_f is an integer automorphism commuting with L; A_f LZ^4=LZ^4 follows
using A_f^-1=A_f^4 for the reverse inclusion. Thus it also preserves
the complement. At each later source opportunity A_f^k y_minus remains
offimage and G rejects. All resources remain zero under contacts, every
ZM intermediate rejects, and the unfunded receiver R rejects. Therefore
the receiver and p=0 remain exactly ready for all k>=0. The source field
may change to P A_f^k y_minus; rejected G is not a fixed macrostep.

For the positive preparation and any one fixed j in 0,...,N-2, the
cut downstream component consists of cells j+1,...,N-1 and channels
q_(j+1),...,q_(N-2), with the receiver pointer. Its initial fields,
spectators, resources, channels and p vanish; intermediate matter is ZM
and receiver matter R. Every primitive fixes that prepared component:
ZM rejects, R lacks its h=0 funding, contacts exchange zeros, and F
fixes zero fields. No remaining contact joins it to the source or qj.
Induction over primitives, not a finite time search, proves it stays fixed
forever. The omitted qj remains separately stored and fixed. Empty ranges
at N=2 or the final cut cause no exception.

These are controls for the declared ready states. Preloading a receiver
resource can fund work independently of the source; a HIT is an accepted
local event record, not by itself a certificate of source provenance.
BLANK does not distinguish a cut from the offimage preparation.

## 8. The fixed reader and the exact retention bound

The local reader is O(p)=BLANK when p=0 and HIT otherwise. Its only
input is the current receiver p. It receives no macrostep, N, seed,
configuration, trajectory, or external log.

Start with p=0 and suppose the first accepted receiver R-to-AM event is
in step j. Before that step the pointer is zero; at j it is 1. After any
increment matter is AM. Neither contacts nor F change matter, and only
one Ghat_t occurs in a complete step. Another increment therefore needs
an intervening accepted AM-to-R step and is at least two steps later.
Rejections can only delay increments. If n_k is the number of accepted
R-to-AM events through boundary k, then p_k=n_k modulo 5 and

```text
1<=n_(j+ell)<=1+floor(ell/2)<=4 for 0<=ell<=7.
```

Each residue is nonzero. Thus HIT holds at all boundaries j,...,j+7:
eight boundaries spanning seven elapsed macrosteps. The first possible
fifth increment cannot precede j+8, but no fifth event or actual reset at
j+8 is asserted. n_k is a proof device, not a stored counter.

For Section 6 j=N, giving HIT at N,...,N+7 despite the old receiver's
return at N+1. Section 7 gives BLANK at every nonnegative boundary in
both negative families. The guarantee assumes p=0 initially and the
forward law. A preloaded p=4 could become BLANK at the next accepted
event, and applying the mathematical inverse can undo a write immediately.
Neither perturbation robustness, permanent memory, nor a reset protocol
follows from this finite residue argument.

## 9. Finite-energy recurrence and interpretation boundary

For fixed finite N and Hhat_N=E, positivity bounds every Q coordinate
by E-1. The square identity in Section 1 bounds M0 and M0+M1, hence
M1, and all components of 2E_i+CM_i, hence every E_i. Every cell and
channel resource is at most E-1. There are finitely many integer choices
and only five pointer values. Each energy shell is finite, including the
empty case, and the conserved-energy bijection restricts to a permutation.
Every actual orbit is therefore periodic from its initial state with no
transient, under either the full law or a fixed cut law. In particular
an orbit initially at p=0 eventually returns to that value. No uniform
period across N or energy, no chain period 5 or 10, and no preparation's
exact global period is inferred from the local field or gate cycles.

The fixed metric, graph, endpoints, image predicate, neutral resource
weights, selected layer schedule, source/receiver roles, ready states,
five-state degeneracy and reader are assumed definitions. C5 is not
derived from native J; Hhat_N=H_N+1 is not a measured preparation cost.
The device proposal's epsilon=0.500 J, banks, 10 s clock, controller,
and instruments are further realization choices outside this proof.
No physical loss bound, SI energy calibration, complete apparatus family,
native-U compatibility, sampling/Born law, occurrence law, or terminal
physical event is proved. No QDD or MINIMAL-READ parent is closed.
