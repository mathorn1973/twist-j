# Exact scale and active memory for the complete arithmetic step

**PUBLIC / NON-CANONICAL / L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Apache-2.0. Reserved in
[issue #1771](https://github.com/mathorn1973/twist-j/issues/1771).

These are mathematical results for the specified Canon v105 model. They
are not a derivation of its lattice, contacts or physical registers from
the original six-pentit update. No scientific executable was run. The
source and review boundaries are in [CONTRACT.md](CONTRACT.md) and
[ARITHMETIC_REVIEW.md](ARITHMETIC_REVIEW.md). The distinct spectral
statements are proved in [SPECTRAL.md](SPECTRAL.md).

## 1. Fixed model, notation and attribution

Use exactly HOMOGENEOUS-CAPTURE-CURRENT-RECORD in the
[pinned Public Canon v105](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md).
There is one object pair, one token or pulse, and an occupied receiver at
`z=100`. The object configuration is `(R,r)` with physical constituent
positions `x_A=R+r`, `x_B=R-r`. Coin order is `(++,+-,-+,--)`.
The token position is `y`; the pulse position is `x` and its bank is 1 or 2.
Both carrier labels and receiver labels range from 0 to 25.

Ignoring an identity reference factor temporarily, identify both
arrangements with the common configuration coordinate

\[
 q=(R,r,c)\in\mathbb Z^3,\qquad
 c=y\text{ for a token},\quad c=x\text{ for a pulse}.
\]

There are `4*(1+2)*26*26` internal basis states at each `q`. Let
`mathcal B` denote this entire fixed basis. The coefficient modules are

\[
 \mathcal O=\mathbb Z[t],\quad
 t=e^{i\pi/10},\quad t^8-t^6+t^4-t^2+1=0,
 \qquad
 M_{\rm raw}=\bigoplus_{b\in\mathcal B}\mathcal O,
 \quad M_{\rm amp}=\bigoplus_{b\in\mathcal B}\mathcal O[1/5].       \tag{1}
\]

Every coefficient in `O` has exactly eight integer coordinates in the
power basis `1,t,...,t^7`. Direct sum always means finite support.
The chosen complex embedding is denoted by `iota`; complex conjugation
is the algebraic involution `t -> t^(-1)`.

The Canon supplies

\[
 M=I+2iX,\quad M_2=(M\otimes M)/5,\quad
 W=\Gamma S M_2,\qquad i=t^5,\quad\zeta=t^4,\quad\beta=4\pi/5.
\]

Object streaming has increments
`(-1,0),(0,-1),(0,1),(1,0)` respectively. The phase `Gamma` is
`zeta^(-1)` at the output `r=0`, and one elsewhere. On pulses,

\[
 Q=\frac1{\sqrt5}\begin{pmatrix}1&-2\\2&1\end{pmatrix},\qquad
 E(k)=\frac1{\sqrt5}\begin{pmatrix}1&-2e^{ik}\\2e^{-ik}&1\end{pmatrix},
 \qquad V(k)=E(k)Q.                                             \tag{2}
\]

The Fourier convention is `|x> -> exp(-ikx)`. Thus `exp(-ik)` in
a matrix entry moves the pulse by `+1`.

Let `mathcal W` apply `W` in both arrangements and let
`mathcal R=I_T direct-sum V_P`. The contact `C` is the identity except
on the orthonormal pairs

\[
 \alpha_{s,j}=|R=s,r=0,i(e_2-e_3)/\sqrt2;y=s,t_j\rangle,
 \quad
 \gamma_{s,j}=|R=s,r=0,(e_1-e_4)/\sqrt2;x=s,1,p_j\rangle,
\]

on which its matrix is `[[3,-4],[4,3]]/5`. The rightmost factor acts first:

\[
 U=e^{-i\beta}\mathcal R\mathcal W C,\qquad
 U_{\rm rec}=\mathcal T(U\otimes I_{\rm mem})\mathcal T^*,\qquad
 \mathcal A=25U_{\rm rec}.                                     \tag{3}
\]

Here `T` exchanges carrier and memory labels precisely on `c>=100`.
It preserves coordinates and carrier type. It commutes with the contact
because both arrangements meet on the same side of the receiver and the
contact matrix is identical for every label.

The complete-step denominator result below was already established in
the public analytical record of
[#1741](https://github.com/mathorn1973/twist-j/issues/1741#issuecomment-6385322548)
and is also in the supplied proof. The per-coefficient localization method
for the isolated `W` is already in
[#1739 at its fixed head](https://github.com/mathorn1973/twist-j/blob/5ce14091995dfdc0e57fe7b256b72aed6f16ac3e/notes/canon/C-SOURCE-PHASE-NATIVE-1/PROPOSAL.md).
The new results here are the complete primitive-scale classification and
its nonlocality, full-apparatus exact precision growth, and the explicit
scope of additive residue obstruction. The full local coefficient rule is
a proved extension of the earlier method, not a new localization principle.

## 2. Recheck of the complete integer numerator

Put `D=5(C-I)`. At each contact pair,

\[
 D=-2(P_\alpha+P_\gamma)
       +4(|\gamma\rangle\langle\alpha|-|\alpha\rangle\langle\gamma|).
                                                                    \tag{4}
\]

Each outer product has denominator two, canceled by its displayed
coefficient. Thus `D` has entries in `O`. Put `a=e_1-e_4` and
`b=i(e_2-e_3)`. Expansion gives

\[
 M\otimes M=I+2i(X\otimes I+I\otimes X)-4X\otimes X.
\]

For either `a` or `b` the middle sum vanishes and `X tensor X` acts
as minus identity. Therefore `M_2 a=a` and `M_2 b=b`. Applying `W`
to the left vector of each outer product in (4) introduces only streaming
and a root-of-unity phase, so `mathcal W D` remains integral.
Also `5 mathcal W` and `5 mathcal R` are integral. Consequently

\[
 25U=e^{-i\beta}
       \bigl(25\mathcal R\mathcal W+5\mathcal R\mathcal W D\bigr)  \tag{5}
\]

has entries in `O`. The permutation `T` preserves this property. The
integer numerator covers the entire macrostep; this does not assert that
every intermediate physical factor is an integral matrix.

The row and column propagation radius of `A` in the configuration
`ell^1` distance is at most two. Contact changes no coordinate, object
streaming changes one of `R,r` by one, pulse edges change `c` by at most
one, and label calibration changes no coordinate. The same holds for
`A*`, with finite row and column support.

Unitarity and the faithful embedding imply the algebraic identity

\[
 \boxed{\mathcal A^*\mathcal A=\mathcal A\mathcal A^*=5^4I.}       \tag{6}
\]

All entries of these products are finite sums, so no summation-domain
issue occurs. Equation (6) uses algebraic conjugation of coefficients and
transposition of configuration indices, not Euclidean transpose in the
eight-integer power basis.

For sharpness choose a pulse basis input at `(R,r,x)=(0,10,0)`,
object coin 1 and pulse bank 1. The output `(-1,10,0)` in the same
coins has coefficient

\[
 \zeta^{-2}\,(1/5)\,(1/5)=\zeta^{-2}/25,
\]

since `V_11(k)=(1-4e^{ik})/5`. Contact and receiver do not intervene,
and no second path contributes to this entry. If a positive integer `d`
clears all coefficients, then `d/25` is a rational algebraic integer,
hence an integer. Thus 25 is the least such `d` in this fixed basis.

Every token-output row of `A` has a factor five: its free term is `25W`
and its contact term is `5(WD)_T`. This common rational-integer factor
is exactly five because a far token basis transition has coefficient
`5 zeta^(-2)`. It is not a factor 25 in every entry. Reduction modulo
five kills the whole token output, while its complex amplitude need not
vanish.

## 3. A unique primitive common-scale state and its exact inverse

For `0!=a in M_raw` define common five-divisibility

\[
 \nu_5(a)=\max\{k\ge0:a\in5^kM_{\rm raw}\}.
\]

This is the common integer content in the fixed power basis. It is not
a prime valuation of the number field; no general multiplicativity is
asserted. Call `a` primitive when `nu_5(a)=0`.

Every nonzero `b in M_amp` has a unique representation

\[
 b=5^{-m}a,\qquad m\in\mathbb Z,\quad a\in M_{\rm raw}
       \text{ primitive}.                                      \tag{7}
\]

Existence follows by clearing denominators and removing the full common
power of five. For uniqueness, if two such pairs differ in their exponent,
one primitive vector would be divisible by five. Keep a separate single
zero state if the zero vector is admitted.

**Theorem 1 (reversible common-scale chart).** For primitive `a`, put
`s=nu_5(Aa)`. Then

\[
 0\le s\le4,\qquad
 F(m,a)=\left(m+2-s,\frac{\mathcal Aa}{5^s}\right)                \tag{8}
\]

is a bijection on the nonzero chart. Under (7), it is precisely the
complete `U_rec`. Its inverse is the same construction with `A*`.
Every value `s=0,1,2,3,4` occurs.

**Proof.** The lower bound follows from integrality. If `Aa` were
divisible by `5^5`, (6) would make `5^4 a` divisible by `5^5`, contrary
to primitivity. The new numerator is primitive by definition and

\[
 5^{-(m+2-s)}\frac{\mathcal Aa}{5^s}
       =U_{\rm rec}(5^{-m}a).
\]

If `a'=Aa/5^s`, then

\[
 \mathcal A^*a'=5^{4-s}a,
 \qquad \nu_5(\mathcal A^*a')=4-s.                              \tag{9}
\]

The adjoint formula returns both the original numerator and exponent.
Conversely, the same argument from any output proves the other inverse
identity. The zero state is fixed.

To realize all cases, choose far token and pulse basis vectors `e_t,e_p`
whose complete forward and inverse neighborhoods avoid contact and
receiver. The unit coefficient in the sharpness example gives
`nu_5(Ae_p)=0`. The token example gives `nu_5(Ae_t)=1`.
A token with object vector `e_1-e_4` gives `s=2`, because `M_2`
fixes that vector and streaming only separates its two entries.
The adjoint has the analogous far coefficients, so
`A*e_t/5` and `A*e_p` are primitive. Equation (6) gives their
output contents three and four, respectively. This proves sharpness.

This chart retains the actual entire coefficient field. It does not
replace it by a fixed residue plus one integer. Active carrier and memory
labels remain part of the vector, and the scale is common to all coherent
branches. The step does not introduce an additional normalization at
capture or receiver crossing.

### The common normal form is not a bounded-range update

**Theorem 2.** The numerator part of (8), in this unique global chart,
cannot be computed by a fixed bounded-range rule on the configuration
coefficient field, even with the incoming common exponent supplied.

**Proof.** Start with a far token basis vector `a=e_t`, whose output
has content one. Add a pulse basis vector `p` arbitrarily far away, with
disjoint one-step output support. Then `a+p` is primitive, agrees with
`a` throughout any prescribed neighborhood of the token support, and
its output has content zero because of the unit pulse entry. The local
token numerator after canonical division is `Ae_t/5` in the first case
and `Ae_t` in the second. These differ. The exponent increments are also
one and two. No bounded local input neighborhood decides that difference.

The decoded amplitude update remains the original bounded-range linear
operator. The nonlocal operation is selecting one common primitive
representative. This distinction is why a local alternative is needed.

## 4. Exact local coefficient registers, including occupied memory

Define one coefficient register to be a pair

\[
 (p,e),\qquad p\in\mathcal O,\quad e\in\mathbb N_0,
\]

in the following canonical form:

- zero is exactly `(0,0)`;
- when `e=0`, any nonzero integral `p` is allowed;
- when `e>0`, `p` is not divisible by five.

Its reading is `p/5^e`. This is a bijection between the register alphabet
and `O[1/5]`. A register uses eight signed integer numerator coordinates
and one nonnegative integer exponent, of unbounded bit length.
The full register state has finite support, with `(0,0)` as its default.

**Theorem 3 (local reversible coefficient law).** In these registers,
`U_rec=A/25` is a total bijective update with forward and inverse
configuration radius at most two. It retains phase, relative scale and
every occupied carrier/memory label. The inverse uses `A*/25`.

**Explicit rule.** At output basis index `i`, inspect the finite stencil
`J_i={j:A_ij!=0}`. Let

\[
 E_i=\max\bigl(\{e_j:j\in J_i\}\cup\{0\}\bigr),\qquad
 N_i=\sum_{j\in J_i}\mathcal A_{ij}p_j5^{E_i-e_j}.               \tag{10}
\]

If `N_i=0`, output `(0,0)`. Otherwise put

\[
 c_i=\min\{E_i+2,\nu_5(N_i)\},\qquad
 (p'_i,e'_i)=\left(N_i/5^{c_i},E_i+2-c_i\right).                \tag{11}
\]

Here `nu_5` on one nonzero coefficient is the minimum integer
five-divisibility of its eight coordinates. Multiplications in `O`
are reduced using the fixed monic polynomial in (1). No square roots,
floating point, variable choice of a phase branch, or independent
normalization of a physical component occurs.

**Proof.** The numerator in (10) is integral and finite. The division
in (11) is exact in each integer coordinate. It leaves either exponent
zero or a primitive numerator, hence a canonical register. Its reading is

\[
 \frac{p'_i}{5^{e'_i}}
  =\frac{N_i}{5^{E_i+2}}
  =\frac1{25}\sum_j\mathcal A_{ij}\frac{p_j}{5^{e_j}}.           \tag{12}
\]

Thus the register rule is the conjugate of `U_rec` under a sitewise
bijection. Finite column support preserves finite-support states; finite
row support gives the stated radius. Applying the identical rule to
`A*` is the inverse by (6), because
`(A*/25)(A/25)=I` in `M_amp`. No previous state or retained history
is needed for the inverse.

The receiver action is already in the entries of `A`: at the crossing
it exchanges the two labels, including arbitrary old contents. The
decoded linear equality (12) extends after tensoring with identity on a finite
reference. The bounded complex operator equality then holds on arbitrary
admitted reference Hilbert spaces by density. This statement does not
give finite integer descriptions for every complex input or reference.

Changing a local pair `(5p,e+1)` to `(p,e)` preserves that coefficient
exactly. It is therefore different from dividing one physical branch by
its own norm. All interference and relative weights in (12) are retained.
For a normalized Hilbert preparation, one common constant
`1/||iota(b_0)||` multiplies the entire arithmetic state and is conserved
by unitary evolution. This constant need not belong to the arithmetic ring.

**Locality and resource boundary.** The theorem is locality on the
configuration lattice. A coefficient describes a configuration of both
object constituents, carrier and memory. Such coefficients have not been
identified with independent material registers at physical sites.
Furthermore, arbitrary-length integer addition, multiplication and
division are not shown to finish in one bounded physical tick. The fixed
radius is not a bound on digit operations, hardware size or propagation
in an additional digit coordinate. These remain separate requirements
for an original-native or physical implementation.

## 5. Exact precision grows at fixed conserved accounts

The raw integer numerator has growing trace height. Removing its common
scale preserves a finite amplitude account, but does not bound the
precision of its fractional coefficients.

**Theorem 4 (sharp all-time denominator).** Let `e` be a pulse basis
input with

\[
 R=0,\quad r=1,\quad\text{object coin }3,\quad
 x=0,\quad\text{pulse bank }2,
\]

with arbitrary carrier label `j` and occupied-memory label `k`.
After `n>=0` complete steps, the coefficient at

\[
 R=0,\quad r=n+1,\quad\text{object coin }3,\quad
 x=n,\quad\text{pulse bank }2
\]

and labels `(j,k)` for `n<100`, or `(k,j)` for `n>=100`, is exactly

\[
 \boxed{\frac{(-4\zeta^{-2})^n}{25^n}.}                        \tag{13}
\]

The least positive integer `d_n` with `d_n U_rec^n e in M_raw` is
exactly `25^n`. In the common primitive chart,

\[
 \nu_5(\mathcal A^ne)=0,\qquad m_n=2n.                         \tag{14}
\]

**Proof.** Every macrostep changes `r` by at most one. Reaching
`r=n+1` from one forces coin output 3 and increment `r -> r+1`
at every step. Hence `R` remains zero, all intermediate relative
positions are positive, and neither contact `C` nor phase `Gamma`
acts on any path contributing to this endpoint.

The carrier remains a pulse on these contributing paths. To reach
`x=n` from zero it must move `+1` at every step. Direct multiplication
of (2) gives

\[
 V(k)=\frac15\begin{pmatrix}
 1-4e^{ik}&-2-2e^{ik}\\
 2+2e^{-ik}&1-4e^{-ik}
 \end{pmatrix}.                                               \tag{15}
\]

Every `+1` output is in bank 2. Starting in bank 2 therefore fixes
the pulse coefficient to `-4/5` at every step. The forced object
diagonal coefficient is `1/5`. There is exactly one history in this
configuration basis, with phase `zeta^(-2)` at every macrostep.
Equation (13) follows before receiver calibration.

Finally `U_rec^n=T U^n T*` and the input lies left of the receiver.
The endpoint calibration is identity for `n<100` and exchanges labels
for `n>=100`. This proves the entire occupied-label statement without
assuming that the memory started empty.

Equation (5) shows that `25^n` clears all denominators. Conversely,
the coefficient (13) forces
`d_n(-4)^n/5^(2n)` to be a rational algebraic integer. Because four
is coprime to five, `5^(2n)` divides `d_n`. The numerator
`(-4 zeta^(-2))^n` is not divisible by five in `O`; multiplying by
a root-of-unity inverse reduces this assertion to the integer `4^n`.
This also proves (14).

### What is conserved while this denominator grows

For finite-support `b in M_amp`, define the rational quadratic account

\[
 \mathsf Q(b)=\operatorname{Tr}_{\mathbb Q(t)/\mathbb Q}
                  \sum_i\overline{b_i}b_i.                    \tag{16}
\]

Each embedding contributes a squared norm, so `Q(b)>0` for nonzero
`b`. Equation (6) implies `Q(U_rec b)=Q(b)` exactly. On the
trajectory of Theorem 4, `Q=8` for all times. Equivalently,

\[
 H_{\rm raw}(\mathcal A^ne)=8\cdot625^n,
 \qquad \mathsf Q(5^{-2n}\mathcal A^ne)=8.                     \tag{17}
\]

The declared active occupation charge is also constantly ten, and every
spectral distribution of the nominated `H_*` is conserved. None of these
accounts bounds the denominator depth. This is a counterexample within
the same complete model, not a transfer of a different model's precision
obstruction.

The input is a pulse basis state, not the specialized incoming capture
packet and not asserted to lie in the safe energy window. The extreme
amplitude has magnitude `(4/25)^n`, so the theorem does not establish a
lower bound on resources for any fixed nonzero approximation tolerance.
It also does not identify rational precision with thermodynamic work.
It proves exact denominator growth only.

The finite-memory and energy issues consequently separate: the algebraic
reading can conserve a positive account while exact register precision
grows without bound. Any finite-precision realization needs its own
specified error, preparation family and time domain; an all-time error
guarantee requires its own proof.

## 6. Why an additive characteristic-five shadow still cannot work

**Theorem 5 (additive factor obstruction).** Let `G` be any abelian
group killed by `5^r` for some finite `r>=1`. Every additive map

\[
 \Pi:M_{\rm amp}\longrightarrow G
\]

is zero. In particular, there is no nonzero additive full-amplitude
projection to a finite or infinite field of `F_5` cell values.

**Proof.** Multiplication by `5^r` is surjective on `M_amp`.
For every `b`, take `c=b/5^r`. Then
`Pi(b)=Pi(5^r c)=5^r Pi(c)=0`.

This is stronger than only excluding a unital ring homomorphism, but
still has a sharply limited scope. It excludes additive readings of the
entire localized amplitude module. It does not exclude a nonlinear
reading, a restricted preparation class, an unbounded digit representation,
a nonadditive scale-aware state, or a differently typed native construction.
The original six-pentit update is nonlinear and is not disposed of by
this theorem.

In particular, the primitive chart retains the full `a`, not merely
`a mod 5`. A nonzero residue at the common lowest level need not show
every coherent sector: the distant-pulse example in Theorem 2 leaves
the token contribution divisible by five. Canonicalizing a common scale
does not guarantee that a single residue sees active memory.

The earlier
[#1614 full-contact proof](https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/notes/C-SOURCE-RAMIFIED-CONTACT-CLOSURE-N/PROOF.md)
has its own stronger finite-reading counterexamples for a different
funded machine, even with exact energy and ramified valuation. No
assumption that an exponent alone repairs residue loss is made here.

## 7. Exact statement of the advance and remaining task

The complete chosen apparatus now has an explicit total reversible
integer-register representation with finite range in configuration
coordinates. Its scale, phase, source content and occupied memory are
part of the same state and evolve under one fixed rule. The proof handles
arbitrary admitted next inputs and the actual inverse, not only one
prepared trajectory.

It is a representation of the existing full `U_rec`. The numerator 25
and localized-ring principle are inherited; the sharp primitive chart,
its locality obstruction and the full-model all-time precision witness
specify the new boundary. The independently proved spectral boundary
in [SPECTRAL.md](SPECTRAL.md) shows that the nominated positive scalar
logarithm is not uniformly exponentially local in configuration space.

The next native construction must supply a material carrier for those
digits, explicit allowed arithmetic/carry gates and their timing, a
fixed reading intertwining the entire active law, and a compatible
resource account. Its gates cannot be admitted merely because they
simulate the desired answer. The original six-pentit law, a new network
coupling and this exact coefficient representation remain distinct
objects until that bridge is proved. No existing public obligation is
closed by this note.
