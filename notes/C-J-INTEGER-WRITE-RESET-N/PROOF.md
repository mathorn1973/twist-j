# Exact integer transaction and its resource boundary

**NON-CANONICAL / candidate-T / result-exposed / L1 only.**
Author: A. M. Thorn <thorn@twistj.com>. Owner #1292.

All new statements below are written analytical candidates. No finite
scientific computation is used as evidence.

## 1. Arithmetic and the finite-phase reader

Let O=Z[j], j^4+j^3+j^2+j+1=0, J=1+j^2. Its inverse is
J^-1=-j-j^2 in O. Let P=O/5O and let ell:P->O choose each coefficient in
{0,1,2,3,4} in the basis (1,j,j^2,j^3). Denote reduction by [x]_5 and put

    rho(x)=ell([x]_5),    quo(x)=(x-rho(x))/5.

These are unique for every x in O, including negative coefficients. P has
625 elements but is not the field F625. Its additive vector space is F5^4.

The registered J-RESIDUE-PERIOD theorem gives ord_5(J)=20. Here is a direct
check of this particular value. In P put epsilon=j-1, so epsilon^4=0 and
J=2+2epsilon+epsilon^2. Characteristic five gives J^5=2, hence J^20=1.
Since 2 has order four, ord(J) is either four or twenty. The coefficient of
epsilon in J^4 is 4*2^3*2=4 modulo five, so J^4!=1. Its order is twenty.

Consequently, for x_t=J^t ell(p) and s=t mod20,

    D([x_t]_5,s)=[J^-s x_t]_5=p.                         (1)

This uses 625 possible residue values and twenty clock phases, not the full
integer t. It returns p; ell(p) recovers the designated integer message.

**Sharpness in this observation class.** For a positive integer h, a reader of only
([x_t]_5,t mod h), valid for all 625 messages and all t>=0, exists iff 20|h.
For necessity compare time zero with initial residue r and time h with
initial residue J^-h r. Both observed pairs equal (r,0). They must be the
same message for every r, so J^h acts identically on P. Its order is twenty.
Conversely 20|h determines the phase in (1). No such lower bound is asserted
for exact integer observations or a restricted source alphabet.

More generally a finite source set P0 subset O, injective modulo q>=2, can
be read from (J^t p modq,t mod ord_q(J)) by inverse multiplication followed
by its fixed inverse codebook. A norm bound alone need not make P0 finite:
unit orbits preserve algebraic norm.

## 2. Complete carrier and source transfer

The full state is

    z=(p,a,M,b,c,E) in P x C2 x O x C2 x C20 x N0.

Here p is the source payload, a its occupancy, M the exact integer memory,
b its occupancy, c the phase and E the archive. All phase exponents mean
the representative c in {0,...,19}. The prepared source is (p,1), including
p=0. Source-ready is (0,0). Memory-ready is (M,b)=(0,0), for any c and E.
Dirty states with a=0,p!=0 or b=0,M!=0 remain in the complete carrier.

Define the **added** write map W by the unique decomposition

    J^-c M = 5Q + ell(r),    Q in O, r in P,

and set

    W(p,a,M,b,c,E)=(r,b,J^c(5Q+ell(p)),a,c,E).             (2)

On the second application the quotient is still Q and the residue is p;
the same phase is used and both occupancy flags are exchanged back.
Therefore W^2=id on the entire carrier. In particular

    (p,1,0,0,c,E) -> (0,0,J^c ell(p),1,c,E).              (3)

This is an actual change from a ready memory to an occupied one. The source
port is vacated and its information moves to memory. It is classical
information transfer, not a claim about copying unknown quantum states.
Source preparation and invocation of W are declared inputs. a=0 or p=0
alone is not used to detect a physical arrival.

The high quotient Q is preserved in (2); setting it to zero would destroy
global invertibility. W is a nonlinear digit operation in the marked basis,
not an operation derived from multiplication by J alone or from native U.

## 3. Holding and source-independent readback

Define

    H(p,a,M,b,c,E)=(p,a,JM,b,c+1 mod20,E).                 (4)

Its inverse multiplies M by J^-1 and decrements the phase. If (3) starts
at phase c0, after t>=0 holds

    M_t=J^(c0+t) ell(p),    c_t=(c0+t) mod20,    b=1.      (5)

The reader on all states is

    Read(M,b,c)=BLANK                 if b=0,
                PRESENT([J^-c M]_5)  if b=1.              (6)

Since c0+t-c_t is a multiple of twenty, (1) proves that (6) returns PRESENT(p)
for every t. The source port is already (0,0) and neither H nor Read accesses
it. PRESENT(0) is distinct from BLANK. The exact integer M is not reduced
modulo five by holding, even when the reader discards its higher digits.

H on a blank work register changes its phase but preserves M=0,b=0. An
unbounded holding duration requires no additional elapsed-time input to (6).
This is finite observation data, not a bound on the cost of physically
obtaining that data from a large integer register.

## 4. One integer as an exact finite stack

Fix the signed-coordinate bijection zeta:Z->N0 by

    zeta(k)=2k for k>=0,    zeta(k)=-2k-1 for k<0.

Use Cantor pairing

    pi(u,v)=(u+v)(u+v+1)/2+v.

For each n, the unique w with w(w+1)/2<=n<(w+1)(w+2)/2 gives
v=n-w(w+1)/2 and u=w-v. Thus pi is a bijection N0^2->N0 with a completely
specified inverse. Define, with exactly this parenthesization,

    nu(m0+m1*j+m2*j^2+m3*j^3)
      =pi(pi(zeta(m0),zeta(m1)),pi(zeta(m2),zeta(m3))).

It is a bijection O->N0. For c represented in 0,...,19 define

    Push(M,c,E)=1+pi(20nu(M)+c,E).                        (7)

This is a bijection O x C20 x N0 -> N_{>0}. Its inverse Pop(E') for E'>0
first unpairs E'-1 and then takes quotient/remainder modulo twenty.
Moreover pi(u,E)>=E, so Push(M,c,E)>E. Repeated Pop therefore reaches zero
after finitely many operations. Every E in N0 encodes one finite stack of
exact records (M,c), and E=0 denotes the empty stack. The value M=0 is a
record like any other and is never confused with the empty stack.

This is an explicitly chosen number-theoretic coding, not a physically
selected archive mechanism. One integer has unbounded capacity; pairing and
unpairing need not have bounded bit cost. No metric, spatial locality or heat
bound is inferred from the number of registers.

## 5. A total reversible reset

Leave (p,a) unchanged. Define R on every (M,b,c,E) by three disjoint cases:

    if b=1:
        (M,b,c,E) -> (0,0,c,Push(M,c,E));

    if b=0, M=0, E>0 and Pop(E)=(M0,c,E0):
        (0,0,c,E) -> (M0,1,c,E0);

    otherwise:
        (M,b,c,E) -> itself.                             (8)

The second branch requires the stored phase to equal the current phase.
Let A be all b=1 states and B all states satisfying that second branch.
A and B are disjoint. Equation (7) pairs A bijectively with B, with phase
and source coordinates preserved. Equation (8) uses that bijection in one
direction on A, its inverse on B, and the identity on their complement.
Therefore R^2=id on the complete carrier.

Operational reset requires b=1. It always returns work memory to exactly
M=0,b=0 and appends the complete old (M,c). It does not access the source,
the original payload or an elapsed-time counter. The old archive is an exact
tail of the new archive. A second immediate R undoes this reset; R is not an
idempotent operation and is not inactive on every ready state. This inverse
branch is necessary and is not hidden by restricting the state space.

For (5), the complete transaction is

    (p,1,0,0,c0,E)
       --W--> --H^t--> --R-->
    (0,0,0,0,c_t,Push(M_t,c_t,E)).                       (9)

It is a composition of full bijections. Both source and work ports end
ready; the record is now in the archive. Popping that record and applying
[J^-c_t M_t]_5 recovers p without the old source or full t. Later pushes
preserve this entry as an exact tail, though it may take growing work to
address an older entry. A fixed read address for every old record is not
asserted.

Each subsequent valid transaction can accept a newly prepared occupied
source. Any finite sequence of such transactions preserves every previous
archive entry, including repeated zero messages. Independent source loading
is a resource, not a silent assignment in the closed map. An external
decision to issue W/H/R is also a resource until its controller is supplied.

## 6. Autonomous control and the information not retained by a residue

For any fixed finite sequence of bijections F0,...,F_(r-1), introduce an
explicit program phase d in C_r and define

    T(d,z)=(d+1 mod r,F_d(z)).

Its inverse is (d',z')->(d'-1,F_(d'-1)^-1(z')). Choosing W, then t copies
of H, then R makes (9) one traversal of the program-phase cycle of an
autonomous reversible extended machine for a fixed chosen t. The program
phase returns; the complete data state need not. This standard construction
is not a new native U.
Repeated application does not guarantee new occupied sources or correct
invocations after input exhaustion. Variable waiting needs retained control
data or a specified controller; it is not supplied by this compilation.

Archive growth in valid forward transactions selects the occupied-to-ready
branch of R. The inverse branch remains available in the complete dynamics.
This protocol and its preparations do not derive a physical time arrow.

Finite-phase readback must not be mistaken for permission to discard the
entire exact state. At phase c=0, the two occupied states M=1 and M=J^20
have the same readout p=1 but different exact M. They are both obtained by
starting with p=1,c0=0 and holding respectively zero or twenty times. Their
inequality follows from J's infinite order (already from |J|=phi^-1<1
in the chosen complex embedding). A putative reset to ready whose only
remaining outputs depend on (p,c,E) identifies them and is not injective.

More explicitly every held state admits the unique decomposition

    J^-c M = ell(p)+5Q,    M=J^c(ell(p)+5Q).              (10)

The chosen reset retains all of Q by retaining M. Another construction may
retain equivalent information elsewhere; this does not require our specific
pairing. No separately supplied full counter is needed, but M may itself
encode holding-age information. The construction preserves rather than
denies that information.

## 7. Exact affine append criterion: the unit obstruction

Let a nonempty message set S be supplied with offsets c_p in Z^d and one
fixed integer matrix A. Admit every old archive e in Z^d and consider

    Append(e,p)=A e+c_p.                                 (11)

**Theorem.** This map is injective iff det A!=0 and the classes of c_p in
Z^d/AZ^d are pairwise distinct. In that case |S|<=|det A|, and the map is
bijective onto Z^d iff those classes form a complete residue system.

Proof: if A is singular it has a nonzero rational kernel vector, hence a
nonzero integer kernel vector after clearing denominators, which gives a
collision for any one message. If A is nonsingular, equality of two outputs
means c_p-c_q is in AZ^d. Distinct cosets force p=q and then e=f. Conversely
if c_p-c_q=A k with p!=q, outputs from (e,p) and (e+k,q) coincide. Finally
AZ^d has index |det A|, and each message fills precisely one of its cosets.
This proves the capacity and bijectivity statements. Surjectivity alone
does not exclude repeated cosets and is not claimed equivalent to equality
of the two cardinalities.

For multiplication by a nonzero algebraic integer alpha in O, the index is
|N(alpha)|, the determinant of its multiplication matrix. For alpha=J it is
one. Thus E->J E+c_p cannot append two independent messages for arbitrary
old E in O. For any distinct p,q its two images are the same entire lattice;
explicitly E'=E+J^-1(c_p-c_q) gives J E+c_p=J E'+c_q.

Archimedean expansion of some J coordinates does not alter this index.
The conclusion is restricted to (11) with unrestricted e. For example,
e restricted to 2Z and offsets 0,1 already permits an injective scalar
append with A=1. Nonlinear coding, restricted reachable archives or extra
retained outputs change the class. Therefore this is not a general no-go
for any system that uses J.

## 8. A radix comparison with its quotient visibly retained

Multiplication by five on O has index 5^4=625. Every element is uniquely
5E+ell(p), so the typed map O x P -> O, (E,p)->5E+ell(p), is a bijection.
It is not by itself a full-state operation that resets a retained input
register: its domain and codomain have different stated register types.

A genuine fixed-carrier realization on O^2 is

    B(E,X)=(5E+rho(X),quo(X)),
    B^-1(E',X')=(quo(E'),5X'+rho(E')).                    (12)

Substitution in each direction proves the inverse, including negative
coordinates. On prepared one-digit X=ell(p), it gives
(E,ell(p))->(5E+ell(p),0). On general X, the old quotient remains as X'.
For a preloaded finite word X0=sum_(i=0)^(k-1)5^i ell(p_i), E0=0,
the first k applications give X_k=0 and
E_k=sum_(i=0)^(k-1)5^(k-1-i) ell(p_i).

This transfers already supplied information; it does not manufacture fresh
independent inputs. Zero symbols and padding need an explicit length or
occupancy if a record of arrivals is intended. Indeed B(0,0)=(0,0).
Equation (12) is a comparison, not a replacement for the tagged reset (8),
and neither is derived as a native U update.

## 9. Capacity, recurrence, and what is still missing

A bijection on a finite complete state set has only periodic orbits. A fixed
observation eventually constant on an orbit was constant throughout that
orbit. Hence it cannot execute a new BLANK-to-permanent-PRESENT transition.
This excludes neither prepared static memory, finite retention, recurring
events, nor a ten-cycle. Native U is not a finite autonomous permutation:
its complete state includes N0. Its checkpoint recurrence needs its own
registered proof, not just this finite-set argument.

If k independently variable messages from an alphabet of size Q are reset
while all nonenvironment outputs are common, reversibility requires at least
Q^k distinct environment states. Otherwise two histories collide. With
common holding durations and initial phase, (9) puts all 625^k possible
message words into different E values while ending both ports ready.
Thus the archive needs at least ceil(k log2 625) bits of distinguishing
capacity. The chosen pairing is not claimed to attain this lower bound;
it also retains exact high digits and phases.

Ordinary scratch uncomputation using a still-retained source need not consume
new environment information every cycle. The bound concerns the stated
independent messages with other outputs reset, not every reversible action.
Nor is this an energy or entropy law without a physical carrier and measure.

The remaining obligations are concrete: justify the phased source coupling,
the marked digit operations, the occupancy distinction and arrivals, the
phase clock, the exact archive operation and preparation, their costs and
their connection to native U. This note supplies a complete mathematical
witness and a restricted unit-only obstruction. It selects no physical
completion and closes no existing H/O obligation.

## Public premises and related work

- [J-RESIDUE-PERIOD proof](../../probes/P-J-RESIDUE-PERIOD-1/PREREG.md):
  rational-modulus orders, including the inherited period used in section 1.
- [Native protected storage and no-write](../../probes/P-U-NATIVE-MEMORY-EVENT-1/MEMORY-PROOF.md):
  313 static messages and the fixed-checkpoint permanent-write boundary.
- [Common-ready source retention](../../probes/P-QDD-V80-CLOSURE-BOUNDARIES-1/NATIVE-PROOF.md):
  full current checkpoint plus native counter, not this integer apparatus.
- [Native apparatus history factor](../../probes/P-U-PREPARATION-EVENT-RECORD-1/NATIVE-PROOF.md):
  the separate five/four-class limitation of the native (q,r) port.
- Public issues [#976](https://github.com/mathorn1973/twist-j/issues/976),
  [#985](https://github.com/mathorn1973/twist-j/issues/985) and
  [#988](https://github.com/mathorn1973/twist-j/issues/988) already distinguish
  zero occupancy, added source/carry operations and reversible workspace
  uncomputation. Their native constructions are not premises of this proof.
