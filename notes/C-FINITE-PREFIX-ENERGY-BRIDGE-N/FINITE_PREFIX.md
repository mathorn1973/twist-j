# One finite generator for every declared prefix

**NON-CANONICAL, L1; analytical candidate, independent acceptance pending.**

## 1. Energy-bin orbit space

Use U,Q,E0,Delta,A0,I,N,d from CONTRACT.md and put

    m=ceil(Delta/d),
    l_j=jd,       u_j=min((j+1)d,Delta),
    I_j=[l_j,u_j), P_j=1_(I_j)(Q),       0<=j<m.

The P_j are mutually orthogonal and sum to I. Their commutation with U
follows from bounded Borel functional calculus. Set

    X_j=span{P_j U^n A0 v: v in I, 0<=n<=N},
    X=direct_sum_j X_j,       D=dim X<=m(N+1)a.       (F1)

Omit empty X_j. Let J:X->H be inclusion and alpha=J* A0. Then
J alpha=A0 and alpha is an isometry. Fix a basis of I, order the vectors
by (j,n,input label), and use Gram-Schmidt with zero residuals omitted.
This specifies the finite basis before evolution; it does not compute its
entries or supply a laboratory spectral projection.

The rounded original observable Q_d=sum_j l_j P_j satisfies

    Q_d J=J q_d,        q_d=direct_sum_j l_j I_(X_j).
    q_phys=J*QJ=q_d+r,       0<=r<=dI,       [q_d,r]=0. (F2)

The space X need not be invariant under Q or U. Its vectors generally
have infinite coordinate support, even if the input vectors are compact.

## 2. Cayley compression, with its sign and domain

On P_j H define

    c_j=(l_j+u_j)/2,
    T_j=tan((Q-c_j)/(2E0)),
    t_j=J_j* T_j J_j,
    h_j=c_j I+2E0 arctan(t_j),
    h_N=direct_sum_j h_j,        V=exp(-i h_N/E0).    (F3)

Here J_j is the inclusion X_j->P_j H. These are bounded self-adjoint
operators because (u_j-l_j)/(4E0)<pi/2. No tangent pole is compressed.
The scalar tangent is increasing on this interval; its endpoint bounds
pass to the compression. Applying the scalar arctangent to t_j gives

    l_j I<=h_j<=u_j I.                               (F4)

The upper bound is strict in each nonzero finite X_j. Indeed the positive
operator tan((u_j-c_j)/(2E0))I-T_j has trivial kernel, since Q restricted
to P_j H has no mass at the excluded upper endpoint. Its expectation in any nonzero
vector is positive. A finite compression is therefore positive definite.
Consequently h_j<u_j I, 0<=h_N<Delta I, and

    E0 f(V)=h_N,        d floor(h_N/d)=q_d.           (F5)

To prove the promised dynamics, define B_j=exp(ic_j/E0) U on P_j H.
The exact scalar Cayley identity is

    T_j(I+B_j)=-i(I-B_j).                            (F6)

For v in span{P_j U^n A0 I:0<=n<N}, both v and w=B_j v belong to X_j.
Compressing (F6) on v therefore yields

    t_j(v+w)=-i(v-w),
    (I+i t_j)w=(I-i t_j)v,
    w=(I+i t_j)^(-1)(I-i t_j)v.                     (F7)

The inverse exists for self-adjoint t_j. Its two factors commute, and
exp(-2i arctan t_j)=(I-i t_j)(I+i t_j)^(-1). Thus the block V_j agrees
with U on this entire prefix-domain subspace. Induction, followed by the
sum over bins, proves

    J V^n alpha=U^n A0,                  0<=n<=N.    (F8)

This is one fixed finite generator and one step law, not N independently
extended endpoint maps. The horizon is nevertheless a parameter of X
and h_N. A larger horizon generally means a different apparatus.

For any density rho_IR and any reference dimension, (F8) gives the exact
joint density identity after tensoring each isometry with I_R. It includes
coherences between every admitted input label and occupied-memory value.

## 3. Original-energy comparison

Both h_j and J_j*QJ_j lie in the same interval of width at most d. Hence

    ||q_phys-h_N||<=d,
    ||QJ-Jh_N||<=d.                                 (F9)

For the second inequality, subtract c_j on each block and use
|| (Q-c_j)J_j ||<=(u_j-l_j)/2 and
|| h_j-c_j ||<=(u_j-l_j)/2. Different bins have orthogonal images,
so no factor m is introduced. The first bound does not assume that the
two compressed operators commute.

The rounded part exactly intertwines. Therefore the leakage and second
moment obey

    ||(I-JJ*)QJ||<=d,
    0<=J*Q^2J-q_phys^2
       =J*Q(I-JJ*)QJ<=d^2 I.                         (F10)

For every real t, the elementary Duhamel integral using (F9) gives

    ||exp(-itQ/hbar)J-J exp(-it h_N/hbar)||
        <=min(2,|t|d/hbar).                          (F11)

At t=n hbar/E0, 0<=n<=N, the comparison is exactly zero on alpha I by
(F8). Equation (F11) is the weaker uniform statement on the whole code
at general times. It is not an exact continuous-time intertwiner.

Let Z(t)=exp(-it h_N/hbar). Since [h_N,q_d]=0 and 0<=r<=dI,

    -dI<=Z(t)*q_phys Z(t)-q_phys<=dI                 (F12)

for all t. This bound is not accumulated over steps. On admitted prefixes
the expectation of q_phys is in fact exactly constant: by (F8) it equals
the original Q expectation under U^n. The entire embedded distribution
of Q is constant for the same reason. This does not identify arbitrary
sharp intrabin events of Q with those of h_N. Coarse bin probabilities
agree on every code state by (F5); finer event probabilities need not.

## 4. Scope of the finite model

The finite matrix h_N is not the local thermal apparatus Hamiltonian.
Its code basis, spectral projections and exact coupling parameters are
mathematical specifications. The compilation below supplies another
generator realizing a specified terminal channel, with its own physical
time and energy account. Integer step time hbar/E0 must not be confused
with the compiler's completion latency.

The theorem does not assert an all-time finite model of an infinite cyclic
subspace. It does not automatically cover measurements or interventions
between steps: their branch vectors would need their own enlarged fixed
input/orbit contract. Nor does X automatically factor as spatial times
the original receiver. The next note supplies the required output map.

Falsifiers are failure of (F6)-(F8) on an admitted vector, an incorrect
bin endpoint or dimension, a violation of (F9)-(F12), or a claimed physical
or intervention scope broader than these hypotheses.
