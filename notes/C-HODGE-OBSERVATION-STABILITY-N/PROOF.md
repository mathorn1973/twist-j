# Exact algebraic reading, real stability, and fixed-axis context changes

Status: PUBLIC-source, NON-CANONICAL. New deductions: candidate-T, pending
independent review. Finite local arithmetic: candidate-C, x86_64 only.
All mathematical work is L1. Real topology below is an explicitly added
mathematical comparison, not a physical L2 carrier or an apparatus assumption.

## 1. Inherited structure and what the signature means

The marked integral exterior lattice is W_Z=Lambda^2 A4, with rational span
W_Q and real scalar extension W_R in the selected positive real place.
Its wedge pairing beta is nondegenerate of signature (3,3). The scaled Hodge
operator K is integral, K^2=5I, and beta(.,K.) is the positive exterior Gram.
Consequently W_R=W_+ orthogonal_sum W_- with dimensions 3 and 3; beta is
positive on W_+ and negative on W_-.

For the fixed marked L, the accepted rank-one cross image T_a in W_- gives
E_a=W_+ orthogonal_sum T_a. Its signature is (3,1), and it is L-invariant.
This signature is inherited rather than fitted. However, the declared lattice,
Gram, observation, orientation, real place and admitted operation family are
load-bearing premises. It is not a theorem that physical Nature selects them.

More generally, inside this fixed split, any k-dimensional subspace M of W_-
gives signature (3,k) on W_+ direct_sum M. Thus the number of negative directions
of this chosen containing realization counts retained conjugate channels.
This is not a theorem equating memory bits, information dimension and time.

## 2. Exact conjugation is not a continuous one-place read

For rational w, the present plus output determines the exact entire source:

    w=P_+w+sigma(P_+w).

In an F=Q(sqrt(5)) basis this is the accepted semilinear update

    Gamma(x)=A_0 x+B_0 sigma(x),   rank B_0=1.

There is no information-theoretic contradiction: three F-coded numbers can
carry six rational coefficients. This is not a continuous injection of an
open six-dimensional real set into a three-dimensional real set.

Already for scalars alpha_n=phi^(-2n),

    alpha_n -> 0,    sigma(alpha_n)=phi^(2n) -> infinity.

Choose a rational coordinate vector v with B_0v nonzero. Then x_n=alpha_n v
is an allowed exact F-coordinate output, x_n -> 0, and

    Gamma(x_n)=alpha_n A_0v+phi^(2n) B_0v

is unbounded. Such an x_n corresponds to a rational source by the conjugate
basis reconstruction. Thus Gamma is not continuous at zero in the topology
of the principal real output. Additivity makes it discontinuous at every
point of this unbounded algebraic output domain.

### Integral-source version

The same obstruction does not require rational denominators that vary with n.
Put lambda_+=9+4sqrt(5)=phi^6 and lambda_-=9-4sqrt(5)=phi^(-6).
Let a_n,b_n be integers determined by

    a_n+b_n sqrt(5)=lambda_+^n,
    a_0=1, b_0=0,
    a_(n+1)=9a_n+20b_n,  b_(n+1)=4a_n+9b_n.

Their conjugate is a_n-b_n sqrt(5)=lambda_-^n and a_n^2-5b_n^2=1.
Choose an integral u for which B=P_+ L P_-u is nonzero. This exists because
the rank-one real cross operator is nonzero on some vector of an integral
basis. Define the integral sequence

    w_n=(a_n I-b_n K)u.

Since KP_+=sqrt(5)P_+ and KP_-=-sqrt(5)P_-,

    P_+w_n=lambda_-^n P_+u,
    P_-w_n=lambda_+^n P_-u,
    P_+Lw_n=lambda_-^n A+lambda_+^n B,
    A=P_+L P_+u.

Here 0<lambda_-<1, lambda_+>1 and B!=0. In any fixed real output norm,

    ||P_+Lw_n|| >= lambda_+^n ||B||-lambda_-^n ||A|| -> infinity,

while P_+w_n ->0. This proves the discontinuity on the integral-source output
domain itself, without a finite enumeration or a numerical limit estimate.

The local exact matrix construction chooses u=e_01, the first standard wedge
basis vector. It gives

    20 B=(sqrt(5), -5+2sqrt(5), 5-2sqrt(5),
          sqrt(5), -5+2sqrt(5), sqrt(5)).

The verifier audits the matrix and Pell identities at n=0,...,32. The argument
above, not that finite range, supplies the universal and limiting conclusions.

### Scope of the obstruction

This is a real one-place stability obstruction, NOT an obstruction to exact
integer arithmetic or exact algebraic-pair coding. It uses an unbounded family
of source coefficient heights. No energy bound or physical preparation for it
has been derived. On a fixed finite, bounded-height source class, injectivity
instead gives a positive minimum separation of the finitely many outputs.
No universal noise floor, detector limit, thermal law or physical impossibility
is claimed.

Adding one previous axial value gives a continuous finite-dimensional linear
state update at the accepted fixed-axis scope. In the axial pair,

    (y,m) -> (3y-m,y).

Input errors bounded by epsilon in both coordinates give next axial output
error at most 4epsilon. This is a one-step estimate; hyperbolic iteration still
amplifies some errors over long times. Continuity does not mean absence of
dynamical sensitivity, nor does it establish an unrestricted nonlinear minimum.

## 3. The six predictive carriers are not automatically coordinate charts

The accepted atlas gives six distinct negative lines T_a with, in the positive
metric <.,.>_-=-beta|W_-,

    cos^2(T_a,T_b)=1/5 for a!=b,
    sum_a Pi_a=2I on W_-.

Define a same-source compression on the full real source carrier by

    pi_a(w)=P_+w+Pi_a P_-w in E_a=W_+ direct_sum T_a.

For the fixed corresponding L_a, E_a is invariant. Beta preservation makes
E_a^perp invariant too, and E_a^perp lies in W_-. Therefore its two-dimensional
orthogonal complement is invisible to every fixed-L_a future plus output.
By the accepted rank-four theorem it is exactly the future-invisible space.
Hence pi_a is a representative of that predictive quotient.

Take a nonzero t_b in T_b for distinct a,b, and define

    d=t_b-Pi_a t_b.

Then pi_a(d)=0. Orthogonal line projections satisfy

    Pi_b Pi_a t_b=(1/5)t_b,

so

    pi_b(d)=(4/5)t_b !=0.

Consequently there is no function, linear or nonlinear,

    h_ab:pi_a(W_R)->pi_b(W_R),    pi_b=h_ab composed with pi_a

on all unchanged real source states: it would need to send pi_a(0)=pi_a(d)=0
to both zero and (4/5)t_b.

This is a factorization theorem at the stated full-real domain. On exact
rational or integral sources, P_+ alone is injective and this particular
collision is unavailable; symbolic reconstruction is a different class, as
section 2 explains. The theorem must not be advertised as a set-theoretic
obstruction on that injective algebraic class.

It also does NOT forbid simultaneous symmetry transport of source and context.
For g in the marked A5,

    pi_(g a)(g w)=g pi_a(w).

This transports w as well as its label; it is not a reconstruction of pi_b(w)
from pi_a(w) for the same unchanged w. Restricted preparations, explicit extra
state, another physical rotation representation or another reading family
remain separate possibilities.

Finally E_a intersect E_b=W_+ for a!=b, of dimension three. These linear
subspaces are not by themselves overlapping open coordinate patches of a
four-manifold. The word 'atlas' in the source denotes the classified family of
mathematical predictive carriers, not an already constructed spacetime atlas.

## 4. How much joint directional information is retained

For any one of these readings, rank pi_a=4. Two distinct negative lines span
a two-plane, so the joint read (pi_a,pi_b) has rank 3+2=5.

Choose unit representatives t_a,t_b,t_c of any three distinct lines. Every
pairwise inner product is plus or minus 1/sqrt(5), so their Gram determinant is

    det Gram = 1-3/5+2<t_a,t_b><t_b,t_c><t_c,t_a>
             = 2/5 plus or minus 2/(5sqrt(5))
             = 2/5 plus or minus 2sqrt(5)/25.

Both values are strictly positive. Thus ANY three distinct lines span W_- and
ANY corresponding three joint reads have rank six. Their repeated W_+ component
is counted only once. The information counts are therefore

    one direction: 4; two directions: 5; any three directions: 6.

This is simultaneous same-source mathematical information, not a theorem that
such reads are simultaneously available to a native apparatus. It is also not
the same test as the accepted time-ordered future-word rank sequence 3,4,5,6,
although both delimit the same missing information in this representation.

All six negative projections recover the negative source component by

    P_-w=(1/2) sum_a Pi_a P_-w.

A hidden difference at fixed direction is therefore not automatically a gauge
equivalence for the enlarged operation/observation family. Conversely the
six-dimensional complete predictive state need not be six-dimensional physical
space: event coordinates need not encode all internal states and responses.

## 5. Synthesis boundaries

The inherited Lorentzian fixed-axis geometry remains valid. Exact conjugation
shows that its fourth coordinate is not unconditional missing information;
section 2 shows that dispensing with it has a nontrivial one-place stability
cost on an unbounded integral source family. These statements are compatible.

The atlas obstruction says that a lossless single four-coordinate complete
state cannot be obtained by simply changing fixed-axis labels on the full real
class. It does not rule out a four-dimensional event geometry accompanied by
additional physical internal state. Confusing a complete predictive state with
an event was the original unearned step.

The earlier candidate shows beta((L-I)v,(L-I)v)=-beta(v,v) on the primary plane.
Therefore a timelike state can have a spacelike increment under L. A Lorentz
state transformation is not automatically time advancement of an event.
A separate trajectory law, such as X_(n+1)=X_n+v_n, needs its own justification.

A counter-assisted equality alone cannot select a physical target: if
U(n,psi)=(n+1,...), then D(n,psi)=L^n v satisfies D U=L D for any stipulated L
and v. The target and amplitude have been supplied, not derived. This elementary
observation is consistent with the inherited native-reader classification.

What remains open is a target-independent realized contact/event/readout family
and a proof that its influence relation supports one common geometric reading,
with declared internal-state content, equality, contexts, accuracy and overlap
rules. Multiple equivalent readings are permitted by policy; uniqueness of all
coordinate descriptions is neither needed nor asserted. No native-U, physical
clock, arrow, apparatus, dimension or causal-cone owner is closed here.
