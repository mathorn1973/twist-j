# The complete stationary relation at the physical spatial cut

**[candidate-T, NON-CANONICAL, L1]**

This is an analytical derivation from the [homogeneous capture and receiver
law](https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/homogeneous_source.md),
equations (1)–(12), (27), and (43)–(46). The source is fixed at
`0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8`.

The complete encoded active space and its actual native-charge continuity
law are specified in [PROOF_CURRENT.md](PROOF_CURRENT.md). The larger native
occupied-state circuit, including its full object SWAP and the uncoded
receiver-memory complement, is treated in [PROOF_NATIVE.md](PROOF_NATIVE.md).
The four-species coordinates below apply to the declared encoded sector;
they do not replace the full native charge on arbitrary occupied codes.

## 1. Exact stationary network, with every source channel retained

Put the physical cut between `ell=99` and `ell+1=100`. All formulas hold for
arbitrary integer ell and arbitrary receiver position z. Fixing z=100 is the
original preparation, not a constant in the law.

Write t for the carrier position: y in the token arrangement and x in the
pulse arrangement. Keep all positions `(x_A,x_B)` in their common-parity
sector, all four object coins, both arrangements, both pulse banks, all
26 carrier labels, all 26 memory labels, and every unchanged auxiliary
factor. In the encoded receiver sector define

\[
J_n=\mathbf1_{z\ne n}I+\mathbf1_{z=n}\mathsf J,
\qquad J_n^\dagger=J_n,\qquad J_n^2=I.
\tag{R1}
\]

The involution J swaps carrier and memory labels, never their positions.

Let `U_rec psi=lambda psi`. The following intermediate fields specify the
entire stationary equation, not just its transmitting bright part.

**Contact:** `chi=C psi`. At every site n, receiver position and pair of
labels, the coefficients on the source contact vectors
`|x_A=x_B=t=n;iB;T>` and `|x_A=x_B=t=n;A;p_a>` obey

\[
\binom{\alpha'}{\delta'}=
\begin{pmatrix}3/5&-4/5\\4/5&3/5\end{pmatrix}
\binom\alpha\delta.
\tag{R2}
\]

Here `A=(e_1-e_4)/sqrt(2)`, `B=(e_2-e_3)/sqrt(2)`. C is identity on the
whole orthogonal complement. Reverse conversion and every complementary
direction remain in the equation.

**Coins:** `xi=D_0 chi`, where identities on all spectator factors are
understood and

\[
D_0=M_2\otimes(I_T\oplus Q),\qquad
M_2={1\over5}\begin{pmatrix}
1&2i&2i&-4\\2i&1&-4&2i\\2i&-4&1&2i\\-4&2i&2i&1
\end{pmatrix},
\quad Q=\begin{pmatrix}c&-s\\s&c\end{pmatrix},
\quad c={1\over\sqrt5},\quad s={2\over\sqrt5}.
\tag{R3}
\]

**Object streaming:** `eta=S xi`. In coin order `00,01,10,11`,

\[
v_A=(-1,-1,+1,+1),\quad v_B=(-1,+1,-1,+1),\qquad
\eta_d(x_A,x_B,t,z)=
\xi_d(x_A-v_A(d),x_B-v_B(d),t,z).
\tag{R4}
\]

These signs use the source convention
`psi_hat(P)=sum_R exp(-iPR) psi(R)`: the symbol `exp(+iP)` shifts a ket to
the left.

**Pulse edges:** `theta=E_rec eta`. Tokens stand, and

\[
\theta_T(t)=\eta_T(t),\qquad
\theta_a(t)=c\eta_a(t)-sJ_{t+1}\eta_b(t+1),\qquad
\theta_b(t)=sJ_t\eta_a(t-1)+c\eta_b(t).
\tag{R5}
\]

**Stationary closure:**

\[
\boxed{\lambda\psi(x_A,x_B,t,z)
=e^{-i\beta}e^{-ig\mathbf1_{x_A=x_B}}\theta(x_A,x_B,t,z),
\qquad \beta={4\pi\over5},\quad g={2\pi\over5}.}
\tag{R6}
\]

The object and pulse edge layers commute, so this ordering gives exactly
the source `U_rec=U_0,rec C`. Neither an asymptotic calibration nor a
momentum selection has been used.

## 2. Physical crossing ports

At the cut let
`a=eta_a(99)`, `b=eta_b(100)`, `A=theta_a(99)`, `B=theta_b(100)`.
Each is a vector in the full pulse port space

\[
\mathcal K_p=
\ell^2\{(x_A,x_B):x_A\equiv x_B\pmod2\}\otimes\mathbb C^4
\otimes\ell^2(\mathbb Z_z)\otimes\mathbb C^{26}\otimes\mathbb C^{26}
\otimes\mathcal H_{\rm aux}.
\tag{R7}
\]

The actual pulse edge and its spatial regrouping are

\[
\binom A B=\begin{pmatrix}cI&-sJ_{100}\\sJ_{100}&cI\end{pmatrix}\binom a b,
\qquad
\boxed{\binom B b=T_E\binom a A,\quad
T_E={1\over s}\begin{pmatrix}J_{100}&-cJ_{100}\\cJ_{100}&-J_{100}\end{pmatrix}.}
\tag{R8}
\]

For `Sigma=diag(I,-I)`, multiplication gives

\[
T_E^\dagger\Sigma T_E=\Sigma,\qquad T_E^2=I,
\qquad
4(\|a\|^2-\|A\|^2)=4(\|B\|^2-\|b\|^2).
\tag{R9}
\]

The factor 4 is the native carrier charge. All 676 label pairs and their
coherences remain. Moreover

\[
T_E^\dagger T_E=
\begin{pmatrix}3/2&-\sqrt5/2\\-\sqrt5/2&3/2\end{pmatrix}\otimes I,
\tag{R10}
\]

so its positive singular factors are phi and phi inverse. Equations
(R8)–(R10) describe one physical edge, before closing the whole period.

For constituent A let `L_in,+` denote xi at `x_A=99,v_A=+1`,
`R_out,+` its eta output at `x_A=100`, and let `R_in,-`, `L_out,-`
be the corresponding negative-velocity input and output. Every other
coordinate, carrier arrangement, bank, label and auxiliary state remains
in the port. With `S_B` the conditional one-step shift of the other
constituent between the appropriate parity fibres,

\[
R_{\rm out,+}^A=S_B L_{\rm in,+}^A,\qquad
L_{\rm out,-}^A=S_B R_{\rm in,-}^A,
\]

\[
\boxed{\binom{R_{\rm out,+}^A}{R_{\rm in,-}^A}
=\operatorname{diag}(S_B,S_B^\dagger)
\binom{L_{\rm in,+}^A}{L_{\rm out,-}^A}.}
\tag{R11}
\]

This preserves `2 Sigma`. Exchanging A and B gives
`diag(S_A,S_A^dagger)` and another `2 Sigma`. A simultaneous passage of both
constituents therefore carries 4. These marked port fields are restrictions
of the same physical amplitude, not independent particles invented at the
boundary. Standing token and receiver fields remain in (R2)–(R6), even
though they have no independent moving edge port.

## 3. Charge marking and the compatibility constraint

The active half-space charge of [PROOF_CURRENT.md](PROOF_CURRENT.md) is an
additive operator, not a projector onto configurations wholly on one side.
An exact bookkeeping lift is

\[
D\psi=(\sqrt2\psi,\sqrt2\psi,2\psi,\sqrt2\psi),\qquad
\widetilde U=U_{\rm rec}^{\oplus4},\qquad
P_R=\operatorname{diag}(\mathbf1_{x_A>\ell},\mathbf1_{x_B>\ell},
                         \mathbf1_{t>\ell},\mathbf1_{z>\ell}).
\tag{R12}
\]

Then `D^dagger D=10I`, `U_tilde D=D U_rec`, and
`D^dagger P_R D=N_R-N_R,aux`. The unchanged auxiliary charge has zero
current. Thus `D/sqrt(10)` is an isometry recovering the physical weights
2,2,4,2.

The physical subspace is `ran D`. It is invariant under U_tilde but generally
not under P_R. Left and right boundary fields must jointly arise from one
common psi. Dropping that condition gives a larger, different problem.
The complete native occupied-state relation uses the actual gate tensors
and native charge of [PROOF_NATIVE.md](PROOF_NATIVE.md), not this four-mark
formula outside its declared sector.

## 4. Full operator-valued carrier matching

Fix carrier position n and retain the whole object space. Put

\[
\alpha_n=|R=n,r=0;iB\rangle,\quad \beta_n=|R=n,r=0;A\rangle,
\quad P_{\alpha,n}=|\alpha_n\rangle\langle\alpha_n|,
\quad P_{\beta,n}=|\beta_n\rangle\langle\beta_n|,
\quad K_n=|\beta_n\rangle\langle\alpha_n|.
\tag{R13}
\]

Let `h=2/5`, `kappa=4/5`. In carrier order `(token,pulse a,pulse b)`, the
complete contact followed by the free object and onsite pulse steps is

\[
\boxed{F_n=\operatorname{diag}(W,W,W)
\begin{pmatrix}
I-hP_{\alpha,n}&-\kappa K_n^\dagger&0\\
c\kappa K_n&c(I-hP_{\beta,n})&-sI\\
s\kappa K_n&s(I-hP_{\beta,n})&cI
\end{pmatrix}.}
\tag{R14}
\]

Each entry is tensored with every label and auxiliary identity. This is a
unitary operator on the infinite-dimensional carrier slice. It retains all
directions complementary to the contact vectors; W is still the whole
operator `Gamma S M_2`.

Set `zeta=lambda exp(i beta)`, without replacing W by a scalar. The complete
stationary matching is

\[
\boxed{F_n\begin{pmatrix}\tau_n\\a_n\\b_n\end{pmatrix}
=\begin{pmatrix}\zeta\tau_n\\u_n\\v_n\end{pmatrix},\qquad
\binom{\zeta b_{n+1}}{v_{n+1}}
={1\over s}\begin{pmatrix}J_{n+1}&-cJ_{n+1}\\cJ_{n+1}&-J_{n+1}\end{pmatrix}
\binom{u_n}{\zeta a_n}.}
\tag{R15}
\]

The first row is the explicit standing-token constraint

\[
\boxed{[\zeta I-W(I-hP_{\alpha,n})]\tau_n
=-\kappa W K_n^\dagger a_n.}
\tag{R16}
\]

No inverse is assumed. Equations (R14)–(R16), with the object-marked
passages and common-state compatibility, are the spatial relation of the
complete source sector.

For Hilbert slice data, or convergent mixed pairings, unitarity of F_n and
`|zeta|=1` give

\[
\|\tau_n\|^2+\|a_n\|^2+\|b_n\|^2
=\|\zeta\tau_n\|^2+\|u_n\|^2+\|v_n\|^2,
\]

\[
\boxed{\|u_n\|^2-\|\zeta a_n\|^2
=\|\zeta b_n\|^2-\|v_n\|^2.}
\tag{R17}
\]

Polarization yields the Hermitian bilinear identity. The onsite relation
between `f_n=(u_n,zeta a_n)` and `g_n=(zeta b_n,v_n)` preserves Sigma, as
does the edge map `g_{n+1}=T_E f_n`. Multiplication by 4 gives the carrier
current. The A/B marked relations provide the additional native weights 2+2.

For a generalized incoming object continuum, (R17) is not an authorization
to subtract infinite norms. A finite object-coordinate window retains its
boundary-face terms; an outgoing pulse-only reduction can lose flux into
the open object/token arrangement. The exact physical current in
[PROOF_CURRENT.md](PROOF_CURRENT.md) holds on normalizable packets;
generalized stationary use requires defined traces or an explicit limiting
procedure.

## 5. The standing-token inverse fails on the complete energy window

Writing F in token/pulse blocks, a regular elimination would require a
bounded inverse of `zeta I-F_TT`, before one could form

\[
S_{\rm eff,n}(\zeta)=F_{PP}
+F_{PT}(\zeta I-F_{TT})^{-1}F_{TP},\qquad
F_{TT}=W(I-\tfrac25P_{\alpha,n}).
\tag{R18}
\]

Where this inverse and unique feedback exist on the unit circle, the
effective pulse coin is unitary. A total spatial transfer then needs its
relevant pulse transmission block to be invertible as a separate condition.
Neither condition may be inserted into (R15) by assumption.

In the source window

\[
E={8\pi\over5}+\delta,\qquad |\delta|\le {1\over1000},\qquad
\zeta=e^{-i(E-\beta)},
\tag{R19}
\]

the first bounded inverse does not exist on the whole object slice. Here
is a direct algebraic and Weyl-sequence proof.

At P=0, the free object symbol is `W_f(0,q)=S(0,q)M_2`. In the Bell basis,
the vector `A=(e_1-e_4)/sqrt(2)` is fixed. In its complement ordered
`S_0=(e_1+e_4)/sqrt(2)`, `T_0=(e_2+e_3)/sqrt(2)`, `B`, the symbol is

\[
B_f(q)=\begin{pmatrix}
d&it_0&0\\
it_0\cos q&d\cos q&i\sin q\\
-t_0\sin q&id\sin q&\cos q
\end{pmatrix},\qquad d=-{3\over5},\quad t_0={4\over5}.
\tag{R20}
\]

Conjugation by `diag(i,1,i)` makes this a real matrix in SO(3), since its
two factors are the real plane rotations obtained from the two displayed
coin/shift factors. Hence it has one eigenvalue 1. Its trace is
`d+(d+1)cos q=(2cos q-3)/5`. Equivalently, expanding the determinant using
`d^2+t_0^2=1` and `cos^2 q+sin^2 q=1` gives the exact polynomial

\[
\boxed{\det[\xi I-W_f(0,q)]
=(\xi-1)^2\left[\xi^2-{2(\cos q-4)\over5}\xi+1\right].}
\tag{R21}
\]

Choose real `q in (0,pi)` by

\[
\cos q=4+5\cos(E-\beta).
\tag{R22}
\]

This choice exists for every E in (R19). With
`phi=(1+sqrt(5))/2`, `cos beta=-phi/2`, and the 1-Lipschitz bound for cosine,

\[
4+5\cos(E-\beta)\in
\left[4-{5\varphi\over2}-{1\over200},
      4-{5\varphi\over2}+{1\over200}\right]\subset(-1,1).
\tag{R23}
\]

The containment follows, for example, already from `3/2<phi<7/4`.
Now `zeta+zeta^(-1)=2cos(E-beta)=2(cos q-4)/5`, so (R21) proves
`det[zeta I-W_f(0,q)]=0`. Let v be a normalized eigenvector for that exact
symbol and eigenvalue; no numerically fitted dispersion is used.

For integer N at least 2 define

\[
\psi_N(R,r)={1\over N}\mathbf1_{\{N\le R,r<2N\}}e^{iqr}v.
\tag{R24}
\]

It has norm 1. Its support and one-step neighbourhood avoid r=0, so Gamma
acts identically there; `P_alpha,n psi_N=0`. The free-symbol eigen-equation
cancels exactly in the interior. Only O(N) boundary sites remain, each of
amplitude O(1/N), whence

\[
\boxed{\|[\zeta I-W(I-\tfrac25P_{\alpha,n})]\psi_N\|
=O(N^{-1/2})\longrightarrow0.}
\tag{R25}
\]

Thus `zeta I-F_TT` is not bounded below and has no bounded inverse on the
complete object slice throughout (R19). Physically, the standing token is
accompanied by an open moving-object continuum. Its entire arrangement
cannot be deleted as a closed internal memory by a regular matrix inverse.
Outgoing resolvent boundary values, weighted spaces or a proved quotient
are additional constructions; (R25) does not rule them out.

## 6. Exact spatial relation and its Hermitian Green identity

For each marked coordinate, decompose its copy as `directsum_n h_n`, with
all spectator coordinates retained. The source unitary has range at most
one. Write its hopping blocks as

\[
\mathsf A_n=U_{n,n-1},\quad \mathsf B_n=U_{n,n},\quad
\mathsf C_n=U_{n,n+1}.
\]

The exact adjacent-slice relation is

\[
\boxed{\mathsf C_n\psi_{n+1}
=(\lambda I-\mathsf B_n)\psi_n-\mathsf A_n\psi_{n-1}.}
\tag{R26}
\]

These hopping symbols are distinct from the physical contact C. In the
carrier slices, (R14) gives explicit coefficients

\[
\begin{aligned}
\mathsf A_n&=e^{-i\beta}s|b\rangle J_n\langle a|F_{n-1},\\
\mathsf B_n&=e^{-i\beta}(P_T+cP_a+cP_b)F_n,\\
\mathsf C_n&=-e^{-i\beta}s|a\rangle J_{n+1}\langle b|F_{n+1}.
\end{aligned}
\tag{R27}
\]

For an object mark alpha=A or B, put
`F_n^alpha=(M_2 tensor V_carrier,rec) C_n^loc,alpha`, with
`V_carrier,rec=I_T directsum(E_rec Q)`. Let
`T_alpha,+/-=S P_alpha,+/-` be the actual two-constituent shifts restricted
between the appropriate slices. Then

\[
\mathsf A_n=e^{-i\beta}\Gamma_nT_{\alpha,+}F_{n-1}^\alpha,
\quad \mathsf B_n=0,
\quad \mathsf C_n=e^{-i\beta}\Gamma_nT_{\alpha,-}F_{n+1}^\alpha.
\tag{R28}
\]

The receiver copy has zero hopping and keeps the full stationary constraint
in its diagonal block. The unchanged auxiliary coordinates have zero flux.

For `b_ell=(psi_ell,psi_{ell+1})`, define

\[
H_\ell=\begin{pmatrix}
\mathsf A_{\ell+1}^\dagger\mathsf A_{\ell+1}&
\mathsf A_{\ell+1}^\dagger\mathsf B_{\ell+1}\\
\mathsf B_{\ell+1}^\dagger\mathsf A_{\ell+1}&
-\mathsf C_\ell^\dagger\mathsf C_\ell
\end{pmatrix},\qquad
j_\ell(\psi,\phi)=\langle b_\ell(\psi),H_\ell b_\ell(\phi)\rangle.
\tag{R29}
\]

Unitarity and bandwidth one imply

\[
\mathsf A_n^\dagger\mathsf C_n=0,\quad
\mathsf C_{n-1}^\dagger\mathsf C_{n-1}+
\mathsf B_n^\dagger\mathsf B_n+
\mathsf A_{n+1}^\dagger\mathsf A_{n+1}=I,
\quad
\mathsf B_n^\dagger\mathsf C_n+
\mathsf A_{n+1}^\dagger\mathsf B_{n+1}=0.
\tag{R30}
\]

Expanding both sides with (R30) proves

\[
\boxed{j_{n-1}(\psi,\phi)-j_n(\psi,\phi)
=\langle(U\psi)_n,(U\phi)_n\rangle-\langle\psi_n,\phi_n\rangle.}
\tag{R31}
\]

For stationary eigenvalues lambda and mu, the right side is
`(conjugate(lambda) mu-1)<psi_n,phi_n>`. In particular it vanishes for the
same unit-modulus eigenvalue. Thus (R26) preserves its actual Hermitian
boundary form without any hopping inverse.

For the carrier, the blocks of H are explicitly
`s^2 F_ell^dagger P_a F_ell`,
`sc F_ell^dagger |a>J_(ell+1)<b| F_(ell+1)`, its adjoint, and
`-s^2 F_(ell+1)^dagger P_b F_(ell+1)`.
The common W cancels from this current. For each object mark, H is diagonal
with blocks `F_ell^dagger P_alpha,+ F_ell` and
`-F_(ell+1)^dagger P_alpha,- F_(ell+1)`; its spectator carrier unitary
cancels. Multiplying the three moving contributions by 2,2,4 and enforcing
(R12) therefore recovers exactly the current of
[PROOF_CURRENT.md](PROOF_CURRENT.md), including its coherent cross term.

All identities hold on finite-support fields and as bounded forms in the
fixed active charge sector. Generalized stationary fields need convergent
spectator pairings or retained finite-window boundary terms.

A total adjacent-slice matrix would require the right side of (R26) to be
in `ran mathsf C_n` and no nonzero kernel on its chosen domain. The full source
blocks have nontrivial kernels: object hopping contains a velocity
projection, carrier hopping reaches one pulse bank, and receiver hopping is
zero. Hence a global inverse on all adjacent-slice amplitudes is not
justified. This does not forbid a separately proved reduced transfer.
Indeed, if `k in ker mathsf C_n`, then (R30) gives
`H_n(0,k)=0`; a flux quotient is a possible further construction, with its
domain and common-state compatibility still to be established.

## 7. A whole-period control: even the free transfer differs from one edge

This paragraph concerns a decoupled free channel only. If the object factor
has eigenvalue w, write `rho=lambda exp(i beta)/w`, so the pulse obeys
`E Q p=rho p`. Let `u_n=c a_n-s b_n`, `v_n=s a_n+c b_n` and
`f_n=(u_n,rho a_n)`. For `|rho|=1`, onsite matching is

\[
\binom{u_n}{\rho a_n}=L_\rho\binom{\rho b_n}{v_n},\qquad
L_\rho={1\over s}\begin{pmatrix}-\rho^{-1}&c\\-c&\rho\end{pmatrix},
\qquad L_\rho^\dagger\Sigma L_\rho=\Sigma.
\tag{R32}
\]

Composing this with the actual edge gives the complete free-period spatial
transfer

\[
\boxed{f_{n+1}=M_\rho f_n,\qquad
M_\rho={1\over s^2}
\begin{pmatrix}
c^2-\rho^{-1}&c(\rho^{-1}-1)\\
c(\rho-1)&c^2-\rho
\end{pmatrix}\otimes J_{n+1}.}
\tag{R33}
\]

Away from the receiver, its two-by-two determinant is one. For
`rho=exp(-i epsilon)`,

\[
\operatorname{tr}M_\rho={1-5\cos\varepsilon\over2}=2\cos k,
\tag{R34}
\]

using exactly the source pulse dispersion
`cos epsilon=(1-4cos k)/5`. On a propagating band its eigenvalues are
`exp(+ik)` and `exp(-ik)`, despite the golden positive singular factors of
one edge. This is an explicit control against dropping stationary closure.
In the actual capture relation (R14), W and C remain operators; a scalar
w reduction is not available without its own invariant-domain proof.

## 8. Scope of the conclusion

The physical cut gives a complete explicit stationary relation, all its
source channels, and the source-derived native-charge form. It does not yet
give the requested four-dimensional Hodge action or its metric. In
particular, the real involution (R8) does not remove the complex object coin,
the phases g and beta, or the stationary parameter from (R2)–(R6).

The next target test must specify a physical invariant transmitting domain
of this relation, justify its elimination or quotient, and transport both
the full action and the induced native flux form. A finite bright transfer,
an added phase, or agreement of singular factors is insufficient.
