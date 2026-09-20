# Controlled QDD records through uninterrupted native evolution

**NON-CANONICAL; candidate-T; L1 conditional mathematical construction.**
Formal probe `P-QDD-UNINTERRUPTED-RECORD-1`, public lock
[#1085](https://github.com/mathorn1973/twist-j/issues/1085).
A. M. Thorn; original text Apache-2.0.

This proof formalizes the accepted
[uninterrupted-record note](../../notes/C-QDD-UNINTERRUPTED-RECORD-N/README.md)
and makes its source metric, coherent-state interpretation and readiness
conditions explicit. Its public basis is Public Canon v90 and main
`963cb34d6a68a09d93b611f32211d9a3bdc547b7`.
No Canon row or cross-layer gate is changed by this proof.

The entrance controlled displacement and the exit archive exchange are
declared operations. The theorem proves that arbitrarily many actual native
ticks may run between them without changing the source trajectory. It does
not derive physical implementations of either operation, preparation of their
inputs, a material archive, a selected event or an occurrence law.

## 1. Native points, sheets and time-local propagation

All point coordinates in this section are in the finite field F5. Put

\[
x=(a,b,c,d,q,r),\qquad p=(a,b,c,d),\qquad
s(p)=a+b+c+d,\qquad z=s(p)+q+r.
\]

The coordinates `(p;z,r)` specify the same point, since
`q=z-s(p)-r`. The canonical native generators are

\[
\begin{aligned}
g_a(x)&=(b,a,d,c,q,r),\\
g_b(x)&=(-c,-d,-a,-b,-q,-r),\\
g_c(x)&=(2-c,1-d+r,2-a,1-b-r,1-q,-r),\\
g_d(x)&=(2-a,1-b,3-c,4-d,1-q,1-r),\\
g_e(x)&=(2-a,1-b,3-c,4-d,2-q,1-r).
\end{aligned}
\tag{1}
\]

Each generator is an affine involution. Their respective trace maps are

\[
z,\quad -z,\quad 2-z,\quad 2-z,\quad 3-z.
\tag{2}
\]

For a driver bit `t` in `{0,1}`, define

\[
F_t(x)=g_{z+2t}(x),\qquad (g_0,g_1,g_2,g_3,g_4)
=(g_a,g_b,g_c,g_d,g_e).
\tag{3}
\]

Actual native evolution is
`U(n,x)=(n+1,F_{theta_n}(x))`, where `theta_n` is the fixed native
Thue--Morse driver. For a finite chronological word
`w=(t_0,...,t_{k-1})`, let

\[
N_w=F_{t_{k-1}}\circ\cdots\circ F_{t_0},\qquad
N_{\varnothing}=I.
\tag{4}
\]

The time-local propagator `N_{n,k}` uses
`w=(theta_n,...,theta_{n+k-1})`. It is not the origin-zero prefix
notation used in some earlier proofs.

Let `X_z` be a trace sheet and `X14=X_1 union X_4`. The complete selector
table on this union follows from (2)--(3):

| Current z | Driver t | Generator | Next z |
| --- | --- | --- | --- |
| 1 | 0 | b | 4 |
| 1 | 1 | d | 1 |
| 4 | 0 | e | 4 |
| 4 | 1 | b | 1 |

In particular, `X14` is forward invariant for every finite or infinite
driver word. On a fixed current sheet the selected step is one affine
involution restricted to that sheet, hence a bijection onto its next sheet.
The map on the union of sheets need not be injective. We shall use only
known-sheet injectivity and never an inverse of global free evolution.

## 2. All-word displacement theorem and the carried mark

Define, for every `delta` in F5, the global point permutation

\[
T_\delta(p;q,r)=(p;q-\delta,r+\delta).
\tag{5}
\]

It preserves `p,z`, has inverse `T_{-delta}`, and satisfies
`T_delta T_eta=T_{delta+eta}`. Substitution in (1) gives

\[
gT_\delta=T_{-\delta}g
\quad\text{for }g\in\{g_b,g_d,g_e\}.
\tag{6}
\]

Indeed, the source parts of these three generators are independent of
`q,r`, and both port coordinates have coefficient `-1`. Since `T_delta`
preserves the selector input `z`, both sides select the same generator.
Thus, pointwise on `X14`, for either driver bit,

\[
F_tT_\delta=T_{-\delta}F_t.
\tag{7}
\]

**Theorem 1.** For every word `w` of length `k`, every `delta` and every
`x in X14`,

\[
\boxed{N_wT_\delta x=T_{(-1)^k\delta}N_wx.}
\tag{8}
\]

**Proof.** The empty-word assertion is immediate. Suppose it holds for a
word of length `k`. Both propagated points remain in `X14`. Apply (7) with
displacement `(-1)^k delta` at the next bit to obtain (8) for length
`k+1`. This proves the assertion by induction, including every actual
word defining `N_{n,k}`. Applying the same assertion to each prefix also
proves equality of the source and trace at every intermediate tick, and
therefore equality of every selected generator. No finite run length is
used in this argument. QED.

In particular, if `x_j^0` is a reference free trajectory and the perturbed
one begins at `T_delta x_n^0`, then for all subsequent ticks

\[
p_j=p_j^0,\qquad z_j=z_j^0,\qquad
r_j-r_j^0=(-1)^{j-n}\delta,\qquad
q_j-q_j^0=-(-1)^{j-n}\delta.
\tag{9}
\]

For the source part of each of `b,d,e`,

\[
s(p')=-s(p).
\tag{10}
\]

For `d,e`, the constant terms sum to `2+1+3+4=0` in F5. For `n>=3`
define the time-dependent source mark

\[
h_n(p)=(-1)^{n-3}s(p).
\tag{11}
\]

Equation (10) implies `h_{n+1}(p')=h_n(p)` for either driver bit on
`X14`, so by induction

\[
h_{n+k}(p_{\mathrm{free}})=h_n(p)
\tag{12}
\]

for every waiting length and every word. Fix the declared coarse function

\[
f(0)=0,\qquad f(1)=1,\qquad f(2)=f(3)=f(4)=2.
\tag{13}
\]

The controlled entrance operation is the global permutation

\[
C_nx=T_{f(h_n(p))}x.
\tag{14}
\]

It fixes `p,z`; its inverse subtracts the same `f(h_n(p))`. This
definition admits the intended LOW/HIGH function and does not derive its
physical selection from native evolution. Combining (8) and (12), pointwise,

\[
N_{n,k}C_nx
=T_{\varepsilon f(h_{n+k}(p_{\mathrm{free}}))}N_{n,k}x,
\qquad \varepsilon=(-1)^k.
\tag{15}
\]

The source dependence in (15) is legitimate because the source paths on
its two sides agree. It is not an assumption that the displacement is an
independent random variable.

At time three this global map uses `f(a+b+c+d)`. On the four canonical
points `Y_h` in (28), `b=c=d=0`, so it agrees with the earlier entrance
formula using `f(a)`. The two global extensions are not the same away
from that code. Equation (14) declares the present extension explicitly;
it does not retroactively redefine the earlier global map.

## 3. Reference readiness, archive exchange and complete bookkeeping

Choose one initial stable sheet `X_{z_n}` and a reference port value
`r_n^0`. For a fixed driver word, the common sequence of sheets is fixed
by the selector table. On those sheets the `r` updates are

\[
r'=-r\quad(b),\qquad r'=1-r\quad(d,e).
\tag{16}
\]

They do not depend on `p`. Hence the propagated reference `r_j^0` is
common to every source point on the chosen initial sheet. An arbitrary
initial displacement `e=r_n-r_n^0` propagates freely as

\[
r_{n+k}-r_{n+k}^0=\varepsilon e.
\tag{17}
\]

Readiness means `r_n=r_n^0`, not generally `r_n=0`. In the canonical code
below the reference begins at `z_3=1,r_3^0=0` and follows the actual driver.

Add an explicitly admitted archive cell `m in F5`. During the waiting
interval this cell is passive: joint free evolution is `N_{n,k} x I_m`.
For `N=n+k`, define the exit map

\[
S_N^\varepsilon(p;z,r;m)
=\bigl(p;z,r_N^0+\varepsilon m;\,
              \varepsilon(r-r_N^0)\bigr).
\tag{18}
\]

The unshown coordinate `q` is reconstructed from `p,z,r`. For every fixed
reference and sign this is a global permutation, indeed an involution:
in coordinates `(e_N,m)=(r-r_N^0,m)` it is

\[
(e_N,m)\longmapsto(\varepsilon m,\varepsilon e_N).
\tag{19}
\]

It is a signed exchange of information, not erasure.

**Theorem 2.** On the selected initial sheet, for arbitrary initial
source `p`, port displacement `e` and archive content `m`, the composed
entrance, native waiting and exit act on port displacement and archive by

\[
\boxed{
(e,m)\ \xrightarrow{C_n}\ (e+f,m)
\ \xrightarrow{N_{n,k}\times I}\ (\varepsilon(e+f),m)
\ \xrightarrow{S_N^\varepsilon}\ (\varepsilon m,e+f),
\qquad f=f(h_n(p)).}
\tag{20}
\]

The source and trace at the output equal their freely evolved values.

**Proof.** The entrance operation adds `f` to `r`, subtracts it from `q`
and leaves `p,z` fixed. Equations (8)--(9) prove that the ensuing source
and trace paths are exactly free, while (17) gives the middle displacement
in (20). Substitution in (19), using `epsilon^2=1`, gives its final pair.
QED.

For ready input and a blank cell, (20) reduces to

\[
S_N^\varepsilon(N_{n,k}\times I)(C_n\times I)
\bigl((p;z_n,r_n^0);0\bigr)
=\bigl(N_{n,k}(p;z_n,r_n^0);f(h_n(p))\bigr).
\tag{21}
\]

Thus **each basis point has its entire free checkpoint restored**, including
`q` and `r`, after all `k` uninterrupted native ticks. This statement
requires ready input and a blank cell. For general `e,m`, the free input
would end with displacement `epsilon e`, whereas the protocol ends with
`epsilon m` and stores `e+f`. Formula (20) records this difference rather
than silently treating every input as prepared.

Set `B_n=S_n^+(C_n x I)`. The equivalent all-input delay identity is

\[
S_N^\varepsilon(N_{n,k}\times I)(C_n\times I)
=(N_{n,k}\times I)B_n
\tag{22}
\]

on the chosen initial sheet times the whole archive cell. The left side
has (20). On the right, `B_n` gives `(m,e+f)` immediately, and subsequent
native steps give `(epsilon m,e+f)` with the same source and trace.
This proves (22) without any inverse of `N_{n,k}`. A common incompatible
reference cannot be imposed on different initial sheets to extend (22).

For ready input the inserted mark has, throughout the holding interval,
the explicit native carrier

\[
\boxed{(-1)^{j-n}(r_j-r_j^0)=f(h_n(p)),\qquad n\le j\le N.}
\tag{23}
\]

At the completion counter N, (23) describes the point before the exit
exchange. After that exchange the mark is in the archive, not generally
in this port deviation. The reference trajectory and the counter are inputs
to this reading. It is
not a fixed checkpoint reader, and it is not an unbounded archive. Equation
(23) proves that the mark is present in the current native port, rather
than merely reconstructible from an inverse history. For nonready input
the same reading returns `e+f`, as already required by (20).

## 4. Exact canonical code, source metric and distinct projector bases

We now distinguish point coordinates over F5 from amplitude coefficients
in characteristic zero. Let `j=exp(2 pi i/5)`, `K=Q(j)` and

\[
g=1+2j+2j^4=\sqrt5,\qquad c_*=g/10=1/(2g).
\tag{24}
\]

Conjugation is `j -> j^4`. Use shifted rational source coordinates

\[
A(v)=\sum_{i=1}^{4}v_i j^i,
\qquad \langle A(v),A(w)\rangle
=\operatorname{Tr}_{K/\mathbb Q}(\overline{A(v)}A(w))/5.
\tag{25}
\]

Its Gram matrix is

\[
G=I_4-\tfrac15\mathbf1\mathbf1^T,
\qquad G^{-1}=I_4+\mathbf1\mathbf1^T.
\tag{26}
\]

This follows from `Tr(1)=4` and `Tr(j^m)=-1` for `m` not divisible by
five. The eigenvalues of `G` are `1/5` on the constant line and `1` on
its complement, so the source form is positive definite. The same matrix
defines the Hermitian inner product for the complex-linear extension of
the four source columns; that extension is distinct from K-linearity under
field multiplication.

Order both Galois exponents and endpoint labels as `(1,2,4,3)`. Set

\[
H=\begin{pmatrix}
1&1&1&1\\
1&-1&1&-1\\
1&1&-1&-1\\
1&-1&-1&1
\end{pmatrix},\qquad
M_{a,i}=j^{ai},\quad a\in(1,2,4,3),\quad i\in(1,2,3,4).
\tag{27}
\]

The exact endpoint amplitude matrix is

\[
W_3=c_*HM,
\qquad
W_3v=\sum_{h\in(1,2,4,3)}y_h(v)|Y_h\rangle,
\qquad Y_h=(h,0,0,0,1-h,0).
\tag{28}
\]

Equivalently `y_{h_k}(v)=c_* sum_a H_{k,a} sigma_a(A(v))` for rational
source coordinates, and (28) defines its complex-linear extension.
This is exactly the endpoint map of the public
[Galois-fiber-code proof](../P-U-GALOIS-FIBER-CODE-1/PROOF.md).
The present result assumes that declared code as its prepared input; it
does not supply the physical preparation of the antecedent correlations.

For completeness, `H^dagger H=4I`, while

\[
(M^\dagger M)_{i\ell}
=\sum_{a=1}^{4}j^{a(\ell-i)}
=\begin{cases}4&i=\ell,\\-1&i\ne\ell.\end{cases}
\]

Consequently

\[
W_3^\dagger W_3
=4c_*^2(5I-\mathbf1\mathbf1^T)=G.
\tag{29}
\]

In particular `W_3` is an isometry from the source with metric `G` onto
its four-dimensional endpoint amplitude space and is invertible there.
For a source operator `A`, its source adjoint is

\[
A^{\star_G}=G^{-1}A^\dagger G.
\tag{30}
\]

For the map from source to standard endpoint space its metric adjoint is
`W_3^sharp=G^{-1}W_3^dagger`, which equals `W_3^{-1}`. These inverse and
adjoint expressions are comparison maps, not executed native operations.

Define the source projectors and the endpoint selectors separately:

\[
P_L=\tfrac14\mathbf1\mathbf1^T,\qquad P_H=I-P_L,
\qquad D_L(3)=|Y_1\rangle\langle Y_1|,\qquad
D_H(3)=\sum_{h\in\{2,4,3\}}|Y_h\rangle\langle Y_h|.
\tag{31}
\]

The `P_o` commute with `G`; they are orthogonal projectors for its source
inner product. The first row of `HM` is `(-1,-1,-1,-1)`, and
`M 1=-1`, hence `HM 1=(-4,0,0,0)^T`. Therefore

\[
D_o(3)W_3=W_3P_o\quad(o=L,H),\qquad
W_3^\dagger D_o(3)W_3=GP_o.
\tag{32}
\]

Thus source LOW is the constant line, and source HIGH has coordinate sum
zero. After `W_3`, LOW is the single endpoint `Y_1`, and HIGH is the
span of the other three endpoints. Endpoint HIGH means `y_1=0`; it does
not mean that the sum of endpoint amplitudes is zero.

For `n>=3`, put

\[
Y_h(n)=N_{3,n-3}Y_h,\qquad W_n=\mathsf N_{3,n-3}W_3,
\tag{33}
\]

where the linear pushforward `mathsf N` sends each point basis vector to
the basis vector of its actual native image. Every endpoint begins on
`X_1` with `r_3^0=0`. The selector table and (16) give them a common
sheet and port at every later time. Known-sheet injectivity preserves their
distinctness. The four-point code space `mathcal C_n=span{|Y_h(n)>}` therefore
has its standard orthonormal point basis, and

\[
W_n^\dagger W_n=G,\qquad
h_n(p_h(n))=h.
\tag{34}
\]

Let `D_L(n)` select `Y_1(n)` and `D_H(n)` select its three-point
complement within `C_n`. Then

\[
D_o(n)W_n=W_nP_o,
\qquad W_n^\sharp=G^{-1}W_n^\dagger=W_n^{-1}\text{ on }C_n.
\tag{35}
\]

The free point pushforward is not asserted to be an isometry on the full
native amplitude space. Equations (34)--(35) use only its injective
restriction to the declared four-point code.

## 5. Delayed coherent record and the meaning of restoration

Extend the declared point permutations `C_n,S_N^epsilon` linearly to
amplitudes, and use the free point pushforward during the waiting interval.
For compactness let

\[
\mathcal V_{n,k}
=\mathsf S_N^\varepsilon
(\mathsf N_{n,k}\otimes I_m)
(\mathsf C_n\otimes I_m),\qquad N=n+k.
\tag{36}
\]

On the input code tensored with the blank archive basis vector, (21),
(34) and (13) give, for every complex source vector `v`,

\[
\boxed{
\mathcal V_{n,k}(W_nv\otimes|0\rangle)
=W_NP_Lv\otimes|1\rangle
 +W_NP_Hv\otimes|2\rangle.}
\tag{37}
\]

This follows first on every endpoint basis vector, then by linearity,
using (35). It holds for arbitrary superpositions and all waiting lengths,
not only for individual point inputs or normalized states.

The pointwise statement in (21) must not be confused with restoration of
the original uncorrelated joint amplitude. Define the code isometry

\[
J_N:\mathcal C_N\longrightarrow\mathcal C_N\otimes\mathbb C^5,
\qquad
J_N\psi=D_L(N)\psi\otimes|1\rangle
          +D_H(N)\psi\otimes|2\rangle.
\tag{38}
\]

The two archive vectors are orthonormal and the two projectors sum to the
identity on `C_N`, hence `J_N^dagger J_N=I`. The joint state generally
retains coherent LOW/HIGH correlations with the archive. It is not the
original native state tensored with one source-independent archive vector.

More precisely, for any density operator `sigma` supported on `C_N`,

\[
J_N\sigma J_N^\dagger
=\sum_{o,o'\in\{L,H\}}
D_o(N)\sigma D_{o'}(N)
\otimes|\ell_o\rangle\langle\ell_{o'}|,
\qquad (\ell_L,\ell_H)=(1,2).
\tag{39}
\]

Taking the formal partial trace over the archive gives

\[
\boxed{
\operatorname{Tr}_m(J_N\sigma J_N^\dagger)
=D_L(N)\sigma D_L(N)+D_H(N)\sigma D_H(N).}
\tag{40}
\]

Indeed, the partial trace of `|ell_o><ell_o'|` is `delta_{oo'}`.
Equation (40) removes only the LOW/HIGH cross blocks. In the endpoint
basis it leaves every entry between any two HIGH endpoints unchanged.
All three HIGH endpoints wrote the same archive vector, so no fine HIGH
label is present to remove their off-diagonal entries.

If `rho` is a source density operator with respect to the `G` inner
product, its free endpoint counterpart is
`sigma=W_N rho W_N^sharp`. Pulling (40) back with (35) yields

\[
\rho\longmapsto P_L\rho P_L+P_H\rho P_H.
\tag{41}
\]

The use of the metric adjoint is essential: the source coordinates have
Gram `G`, not the identity. In particular source positivity means
positivity for this declared inner product.

Equations (39)--(41) are identities in the admitted amplitude model.
Partial trace is a mathematical operation on that model. It does not by
itself establish a realized single outcome, a physical collapse mechanism,
Born occurrence frequencies, a material record or a probability/L6 lift.
The coherent joint correlation (39) remains the output proved here.
Zero input and zero-weight components are permitted throughout; no formula
divides by a branch weight.

## 6. Repeated records of the same transported observable

Suppose a finite succession of these protocols is applied at later native
times, with arbitrary nonnegative native waiting lengths, each using the
current reference port and a new blank archive cell. Previously used cells
are explicitly assumed passive. After each exit the native code points are
restored to their freely evolved checkpoints by (21), so the next protocol
has the same readiness property.

By induction on the number `r` of completed records, the output at final
native time `N` is

\[
\boxed{
W_NP_Lv\otimes|1\rangle^{\otimes r}
 +W_NP_Hv\otimes|2\rangle^{\otimes r}.}
\tag{42}
\]

For the induction step apply (37) to the current LOW and HIGH summands.
The identities `P_L^2=P_L`, `P_H^2=P_H` and `P_LP_H=P_HP_L=0` append
only the matching archive label to each existing string. Free evolution
between completed protocols transports the same code projectors by (35).
This proves (42) without an assumption of independent preparations.

The records are repeated records of the same transported observable. The
formula does not describe independent trials with new outcomes. A new
source, its preparation, and any law assigning a selected outcome are
separate requirements.

## 7. Exact scope witnesses and necessary input conditions

**Outside the stable union.** Directly from (1),

\[
g_aT_\delta=T_\delta g_a,\qquad
g_cT_\delta=V_\delta T_{-\delta}g_c,
\tag{43}
\]

where

\[
V_\delta(a,b,c,d,q,r)=(a,b+\delta,c,d-\delta,q,r).
\tag{44}
\]

For example, take `x=(0,0,0,0,0,0)`, `t=1`, `delta=1`. Both `x`
and `T_1x` have trace zero and select `c`. In F5,

\[
F_1T_1x=(2,2,2,0,2,4),\qquad
T_{-1}F_1x=(2,1,2,1,2,4).
\tag{45}
\]

Their source components differ. Thus a temporary `r` displacement can
change the source outside `X14`; an all-state sign-reversal conjugacy is
false. Equation (43) also shows why `a` cannot be included indiscriminately
in the sign-reversing generator set.

**Odd waiting and omitted sign.** For ready input and a blank cell,
an odd waiting length leaves displacement `-f` before the exchange. If
one substitutes the unsigned exchange `S_N^+` for `S_N^-`, the archive
receives `-f`. For `f=1` that is `4`, not `1` in F5. The sign in (18)
is necessary.

**Nonready input.** With `e=1,m=0` and `f=1`, (20) stores `2`, not
the intended mark `1`. Restoring the reference port does not remove this
contamination from the archive. Readiness is an actual input condition.

**Occupied archive.** With `e=0,m=1`, the final port displacement is
`epsilon`, which is nonzero. The archive does receive `f`, but the old
cell content has returned to the native port. It has not been erased.
Exact restoration to the freely evolved ready checkpoint therefore requires
`m=0`, or an additional explicitly owned destination and operation for
that content.

These are exact algebraic witnesses, not extrapolations from numerical
trajectories. They delimit the positive theorem and are retained as part of
its statement.

## 8. Physical and architectural boundary

The proved construction consists of a declared controlled entrance write,
unchanged native evolution on `X14`, and a declared signed archive
exchange. Native `U` transports the already inserted mark exactly and
preserves the source path throughout the waiting interval. This does not
show that `U` implements the entrance or exit operation.

In particular, equality of source and selector paths is weaker than equality
of complete checkpoints during the holding interval. The `q,r` coordinates
have been changed until final restoration. Returning later to the free
checkpoint does not make the preceding intervention a read-only operation,
and does not establish the `feeds_U=false` architecture of
[#539](https://github.com/mathorn1973/twist-j/issues/539).

The pre-existing
[native no-write result](../P-U-NATIVE-MEMORY-EVENT-1/MEMORY-PROOF.md)
and [actual-clock recurrence proof](../P-U-NATIVE-MEMORY-EVENT-1/CLOCK-PROOF.md)
concern unchanged native dynamics with their specified fixed readers.
The present construction explicitly adds a controlled intervention, a
counter/reference-dependent reading and an extra archive carrier. It does
not contradict those results or alter their declared classes.

The following remain outside this theorem:

- a physical interaction implementing `C_n`, its carrier and preparation;
- the finite-duration entrance interaction law while native time passes;
- the corresponding physical implementation and duration of `S_N^epsilon`;
- a material archive with an independently justified passive evolution;
- physical selection of the source/port split and the admitted target `f`;
- physical code preparation, fresh archive supply, reset and new sources;
- a realized single event, an occurrence law and a complete physical family
  of apparatus;
- a passed L1-to-L5 bridge or a probability/L6 lift.

These obligations remain under `QDD-INSTRUMENT-APPARATUS` at the declared
public authority. The theorem closes the algebraic waiting question on its
specified stable area and all the conditional bookkeeping above. It does
not close the physical apparatus obligation.

The all-word and all-time conclusions follow from the written induction.
Exact finite verifier checks may audit its identities and scope witnesses;
they do not replace the induction or expand the physical scope.
