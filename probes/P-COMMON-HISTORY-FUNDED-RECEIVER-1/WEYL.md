# Actual accepted paths, transported Weyl labels and occupied records

PUBLIC / NON-CANONICAL / L1. Authored conditional analytical result.
A. M. Thorn. Apache-2.0.

This file fixes the algebraic part of the declared common-history machine.
It is not a physical phase detector, an independent review of #1585, or
an implementation of the O^2 step diag(J,phi) from #1583. The complete
funded controller, native ports and total cost are specified in the
companion contract and proof. No scientific execution supplies evidence
for the arguments below.

## 1. Exact finite phase type

Fix a primitive fifth root j and basis e_k, k in F5, with

    X e_k=e_(k+1),       Z e_k=j^k e_k,       ZX=jXZ.

A Weyl label w=(a,b,c) belongs to F5^3 and has literal operator reading

    R(a,b,c)=j^c Z^a X^b,
    R(a,b,c)e_k=j^(c+a(k+b)) e_(k+b).                    (1)

Equality means equality of operators, including their scalar phase.
It is not equality of rays or equality modulo scalar multiples. This
reading is faithful: the output basis index determines b, the phase
ratio at successive input indices determines a, and then c is fixed.

Direct use of ZX=jXZ gives the multiplication and inverse laws

    (a,b,c)*(A,B,C)=(a+A,b+B,c+C-b*A),
    (a,b,c)^(-1)=(-a,-b,-c-a*b).                        (2)

The identity is (0,0,0). Every coordinate in (1)--(2) is in F5.
Thus each bundle carries precisely 125 possible algebraic labels.
The label has zero assigned cost in this particular model; its finite
state capacity is nevertheless included in the complete state count.
It supplies neither an energy unit nor a physical phase observable.

## 2. Geometry and phase are updated by the same accepted edge

A bundle contains (q,p,u,v,w), with q,p,u,v in Z and w in F5^3.
These integer q,p are not the native cell's F5 control coordinates.
The requested geometric maps, for an integer h fixed by the current
retained source content, are

    Q_h:(q,p,u,v)->(q+h,p,u,v),
    P_h:(q,p,u,v)->(q,p+h,u+h*q,v+h*q).                 (3)

The complete Q_h gate simultaneously left-multiplies w by (0,h,0);
the complete P_h gate simultaneously left-multiplies w by (h,0,0).
In the coordinates of (1), their phase updates are therefore

    Q_h:(a,b,c)->(a,b+h,c-h*a),
    P_h:(a,b,c)->(a+h,b,c).                            (4)

Integer h is reduced modulo five only in (4). All integer coordinates
and energy changes in (3) retain their ordinary integer values.
The inverse of either complete gate replaces h by -h. The source
content selecting h is unchanged by that geometric gate, so the
inverse uses the same retained control value.

Equations (3)--(4) are one proposed transition on one complete state.
They are not two separately run trajectories later matched by an area
value. If the funding/capacity guard rejects the edge, neither (3) nor
(4) occurs. The geometric operator for a refused edge is I, even though
the controller changes its direction according to its separate law.
Backward traversal of an accepted edge uses its literal inverse in
both the integer and Weyl coordinates.

The requested native-content load, record copy and receiver exchange
do not change a bundle's geometric coordinates or Weyl label. Their
Weyl operator is I. Bundle transport requires the separate treatment
in section 4 and must not be classified as a geometric translation.

## 3. Exact path formula, including occupied starting labels

Consider a segment during which one bundle is geometrically active
without being exchanged with another bundle. Its initial integer
coordinates may be arbitrary (q_0,p_0,u_0,v_0), and its initial Weyl
operator W_0=R(w_0) may also be arbitrary. Let

    Delta q=q_N-q_0,       Delta p=p_N-p_0,
    A=sum_i q_i*(p_(i+1)-p_i).                        (5)

The sum uses actual accepted displacements. Refusals contribute zero;
accepted inverse edges contribute their actual signed displacements.
The record shears in (3) imply, by induction,

    u_N=u_0+A,       v_N=v_0+A.                       (6)

Let L_path be the chronological product of actual X and Z operators,
left-multiplying in time order. From (4), or directly on each basis
vector, its exact action is

    L_path e_k
      =j^(k*Delta p+A-q_0*Delta p) e_(k+Delta q).      (7)

One way to prove (7) is to note that each P displacement dp acts after
the accumulated Q displacement q_i-q_0 and hence adds
(k+q_i-q_0)*dp to the exponent. Q displacements change only the basis
index. Summing gives (7), including zero displacements at refusals.
In the convention (1), the same operator has label

    (Delta p,Delta q,A-q_0*Delta p-Delta p*Delta q).   (8)

The third component differs from A on a general open path because
Z^a X^b already contributes a*b when acting on e_k. Omitting that
term would mix two different ordering conventions.

The stored label satisfies the full occupied-label identity

    W_N=L_path W_0,
    W_N W_0^(-1)=L_path.                             (9)

Neither W_0 nor the origin in (5) needs to be an extra machine register.
They are the initial values of the retained bundle for this mathematical
segment. Equation (9) is a proof about the complete history, not a claim
that the current reader can recover a discarded initial value. In the
nominated preparation every fresh donor has q_0=p_0=0 and W_0=I, so
its current label itself equals L_path throughout its active segment.

For a closed integer base path Delta q=Delta p=0, (7) gives

    L_path=j^A I.                                    (10)

This remains true at arbitrary q_0,p_0. It is an algebraic character
of the actual path. It is not defined by setting a phase equal to a
desired area, and it is not the nominal requested word after a refusal.

## 4. Loading a fresh bundle transports the occupied history

The machine retains one working bundle and L donor/archive bundles.
The loading gate exchanges the entire working bundle with the chosen
donor, including all four integer coordinates and all three Weyl
coordinates. The displaced occupied bundle is retained in the donor
slot. It is not reset, discarded or reinitialized.

A numerical change in the working slot's q,p caused by this exchange
is transport of two retained bundles, not the Q/P motion of either
bundle. Applying (7) to the working slot across that exchange would
therefore be a type error. Instead, every retained bundle has its own
successive geometric segments, and its Weyl label follows its own
accepted edges through the exchanges. A fresh donor starts its new
segment with its actually prepared origin and identity label.

There is also an exact single-history operator description that includes
transport. Put M=L+1 and use the explicitly additional tensor carrier

    V=(Q(j)^5)^(tensor M).

The phase state is the ordered tuple (w_0,...,w_L). An accepted geometric
edge contributes X^h or Z^h on the working tensor factor. Exchanging
working bundle 0 and donor j contributes the tensor-factor permutation
S_(0j), not I. Refusals and nongeometric native-content gates contribute I.

For any fixed executed prefix, let pi be the ordered product of its
accepted bundle exchanges and set

    G=(tensor_i R(w_i)) P_pi.                         (11)

This global operator reading need not distinguish every retained tuple
of local central phases. No injectivity of the full tensor reading, or
identification with the complete machine state, is asserted.

Starting from the actual initial labels and pi=id, every accepted edge
left-multiplies G by precisely the corresponding operator just named.
For geometry this is (4) on one factor. For exchange it follows from

    S_(0j)(tensor_i R(w_i))
      =(tensor_i R(w'_i)) S_(0j),                    (12)

where w' exchanges the two labels, and pi'=(0j)pi. Both identities also
hold for backward traversal; a refused edge leaves G unchanged.

No extra permutation register is required for the specified finite-path
controller. If the program vertices are 0,...,M_prog and its edge gates
are g_0,...,g_(M_prog-1), then pi is the product of the bundle exchanges
in the unique program prefix ending at the current vertex. Every
backtrack traverses an edge and its inverse and cancels its permutation.
Thus pi is a fixed function of the already retained program vertex.
For a different controller with multiple paths this conclusion would
need a new proof or an explicitly retained transport label.

Equation (11) is only an algebraic description. No tensor-factor
apparatus, Born rule or physical SWAP operation is inferred from it.
It prevents the bookkeeping error of calling a loaded bundle's local
identity label the identity of the entire machine's operator history.

## 5. Five paid loops, actual orientation and an occupied receiver

The intended source has actual native content eta in {1,4}, read as
the integer +1 or -1. In one transaction the unchanged retained source
controls the twenty geometric edges consisting of five repetitions of

    Q_+, P_eta, Q_-, P_-eta.                          (13)

The fresh donor is literally

    q=p=0,       (u,v)=(1,-1),       w=(0,0,0).

Conditioned on acceptance of all twenty edges, each four-edge square
returns q,p to zero and adds eta to both u,v. Consequently after five
squares

    (q,p)=(0,0),
    (u,v)=(1+5*eta,-1+5*eta),
    A=5*eta,       R(w)=j^(5*eta) I=I.                (14)

For eta=+1 the ordered squared references are (36,16); for eta=-1
they are (16,36). The integer reference cost rises from 2 to 52,
so its paid increase is 50. At the preceding P edge the geometric
cost q^2+p^2+u^2+v^2 is 54. Thus the geometric segment requires a
bank headroom of 52 under the declared square account. The companion
proof includes the native write cost and all other transaction gates.

The fixed report function is computed from the actual current record:

    report(u,v)=sgn(u^2-v^2) mod 5.                   (15)

Here sgn is the integer sign, with sgn(0)=0. Equation (14) gives
u^2-v^2=20*eta, hence report=eta in F5. It is the integer record,
not the source label or the trivial fifth-order phase, that supplies
the report gate's input.

For the declared fresh report slot zeta=0, the reversible addition

    zeta <- zeta+report(u,v)

followed by its declared exchange with the actual occupied native
receiver content lambda_out gives

    lambda_out=eta,       zeta=old lambda_out.        (16)

On arbitrary zeta the addition and exchange remain full bijections;
the intended reading (16) requires the stated fresh slot preparation.
Every earlier receiver value is retained in its own finite report
slot. Every earlier integer record is retained by the next complete
bundle exchange. No claim of an indefinitely growing archive or an
unlimited source of independent inputs is made.

Five-loop closure in (14) concerns the local Weyl operator of that
bundle. The reference, bank, report slot, native receiver, program
vertex and possibly the transport permutation (11) have changed.
Thus it is explicitly not a return of the complete machine state.
The finite reversible controller can later retrace the segment and
undo its records; retention is asserted at the specified completed
transactions and through the specified later forward transactions,
not through every future reversal or finite-shell recurrence.

## 6. Native and O^2 interfaces remain separately typed

The input control and final receiver are actual prepared native-cell
contents, reconstructed by the declared native chart. The report addition,
occupied receiver exchange, integer loop gates and bank/controller law
are added transitions with explicit formulas. Original synchronized U
fixes prepared contents and does not itself execute these changes.
Using its real source and receiver coordinates does not derive the
added transition from U.

If desired, the integer base and record admit the total residue/chart
readings chi_gamma(q mod5,p mod5) and chi_gamma(u mod5,v mod5). These
are derived coordinates of the already retained integers, not additional
independently priced physical cells. Their update follows (3), not an
unproved original-native U law.

The compatible single geometric edge label for #1583's convention
W(a,b)=Z^a X^b is

    ell(dq,dp)=(dp mod5,dq mod5).

For the elementary Q/P edges one component is zero, so this agrees
literally with their operators. A macro changing both coordinates
must retain its actual ordered edges; its endpoint label alone omits
the central phase in (8).

The arithmetic injection (p,q)->(p*1_O,q*1_O) does not intertwine the
integer machine with T=diag(J,phi): its image is not T-invariant, since
T(1,0)=(1+j^2,0) is outside the constant-coordinate image. This existing
N obstruction is not removed by (1)--(16). The present positive result
is a coupled declared history with exact accepted-edge phase and an
occupied native output. Original-native occurrence, the O^2 dynamical
intertwiner, independently selected physical energy and physical phase
observation remain separate open obligations.
