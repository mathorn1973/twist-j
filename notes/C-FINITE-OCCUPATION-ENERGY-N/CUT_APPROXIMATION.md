# Positive finite Laurent energies with the original cut value

**NON-CANONICAL. L1. Conditional analytical candidate-T.**
Author: A. M. Thorn. Date: 2026-10-26. License: Apache-2.0.
Reservation: [#1780](https://github.com/mathorn1973/twist-j/issues/1780).
The prospective [CONTRACT.md](CONTRACT.md) is frozen at
`9f7b175341e5267113dfbe42f96db47299e27f52`.
Independent scientific acceptance is not asserted.

The general approximation theorem below holds for every unitary. Its
application to the actual prepared pair remains conditional on the frozen
source identities of
[PR1777](https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-FINITE-PHASE-OCCUPIED-RECORD-N/ACTIVE_EQUAL_SPECTRUM.md).
The previous
[finite-source certificate](https://github.com/mathorn1973/twist-j/blob/c2b06d3ee52778f804da1f84ba9f963bae1ad46e/notes/C-COMPACT-ENERGY-RECORD-N/ENERGY_CERTIFICATE.md)
used an Abel approximation taking the value pi at the cut. Here a positive
notch preserves the nominated value zero there. No absence of a spectral
atom is assumed or proved. No moment computation, numerical search or
simulation has run for this note.

## 1. The fixed reading and an explicit polynomial sequence

Keep the original scalar reading

\[
 f(e^{-i\theta})=\theta\quad(0\le\theta<2\pi),
 \qquad f(1)=0.                                      \tag{C1}
\]

For every integer \(j\ge2\), put

\[
 r_j=1-\frac1j,\qquad N_j=j^2,\qquad
 \tau_j=\frac{2r_j^{N_j+1}}{(N_j+1)(1-r_j)},
 \qquad c_j=\frac{\pi}{\pi+\tau_j},                  \tag{C2}
\]
\[
 b_j(z)=\left(\frac{2+z+z^{-1}}4\right)^j,
 \qquad
 h_j(z)=\pi-i\sum_{k=1}^{N_j}
                  \frac{r_j^k}{k}(z^k-z^{-k}),
\]
\[
 \boxed{q_j(z)=c_j(1-b_j(z))(h_j(z)+\tau_j).}         \tag{C3}
\]

This is a finite Laurent polynomial of degree at most
\(D_j=N_j+j=j^2+j\). Its coefficients are specified finite expressions
in rational numbers, \(i\), and \(\pi\). The normalization does not claim
that these coefficients lie in the predecessor's finite cyclotomic
integer ring, or supply a native integer implementation of this energy.

**Lemma C1.** On the whole unit circle,

\[
 \boxed{0\le q_j(z)\le2\pi,\qquad q_j(1)=0.}         \tag{C4}
\]

**Proof.** Write

\[
 h_r(z)=\pi-i\sum_{k\ge1}\frac{r^k}{k}(z^k-z^{-k})
 \quad(0<r<1).
\]

The series is norm-convergent on the circle. For
\(z=e^{-i\theta}\), \(0<\theta<2\pi\), its sum is

\[
 h_r(e^{-i\theta})
 =\pi+2\arg(1-re^{i\theta})
 =\theta+2\arctan\left(
        \frac{1-r}{1+r}\cot\frac\theta2\right).
                                                               \tag{C5}
\]

The argument is in \((-\pi/2,\pi/2)\), since
\(\operatorname{Re}(1-re^{i\theta})>0\). Thus
\(0\le h_r\le2\pi\), including \(h_r(1)=\pi\).
The same geometric-tail bound as in the predecessor gives

\[
 \|h_{r_j}-h_j\|_\infty
 \le2\sum_{k>N_j}\frac{r_j^k}{k}
 \le\tau_j.                                        \tag{C6}
\]

Consequently \(0\le h_j+\tau_j\le2\pi+2\tau_j\).
On the unit circle
\((2+z+z^{-1})/4=|(1+z)/2|^2\in[0,1]\), so
\(0\le1-b_j\le1\). Multiplication by the positive scalar \(c_j\)
reduces the upper bound to
\(c_j(2\pi+2\tau_j)=2\pi\). All factors are real there.
Finally \(b_j(1)=1\), proving the exact cut value. QED.

## 2. Convergence including every possible atom

**Theorem C2.** The explicit sequence satisfies

\[
 q_j(z)\longrightarrow f(z)
 \quad\hbox{at every }z\in\mathbb T.                 \tag{C7}
\]

For every unitary \(V\), on any Hilbert space, and every vector \(v\),

\[
 \boxed{\|(q_j(V)-f(V))v\|\longrightarrow0.}          \tag{C8}
\]

In particular this includes vectors with a nonzero spectral component
at \(V=1\).

**Proof.** Since \(\log(1-1/j)\le-1/j\),

\[
 0<\tau_j\le\frac{2e^{-j}}j\longrightarrow0,
 \qquad c_j\longrightarrow1.
\]

For fixed \(z\ne1\), the base of \(b_j(z)\) is strictly less than
one, so \(b_j(z)\to0\). Formula (C5) gives
\(h_{r_j}(z)\to f(z)\); (C6) gives the same limit for \(h_j(z)\).
Equation (C3) therefore converges to \(f(z)\). At \(z=1\), equality
to \(f(1)=0\) already holds for every \(j\).

For the spectral measure \(\mu_v\) of \(V\),

\[
 \|(q_j(V)-f(V))v\|^2
 =\int_{\mathbb T}|q_j(z)-f(z)|^2\,d\mu_v(z).
\]

The integrand tends to zero at every point, and is at most
\((2\pi)^2\) by (C4). Dominated convergence proves (C8). On an atom
at one the integrand is exactly zero, not merely small. QED.

On every fixed finite-dimensional subspace, (C8) also converges in
operator norm after restriction to that subspace. For an orthonormal
basis \(v_1,\ldots,v_d\), the restricted norm is at most
\(\bigl(\sum_{a=1}^d\|(q_j(V)-f(V))v_a\|^2\bigr)^{1/2}\).
This observation does not supply a rate or a stopping index.

For the original finite-propagation \(U=U_{\rm rec}\), define
\(Q_j=E_0q_j(U)\). Then

\[
 0\le Q_j\le2\pi E_0I,\qquad [Q_j,U]=0,
 \qquad [Q_j,Q]=0,
 \qquad Q=E_0f(U).                                  \tag{C9}
\]

Each \(Q_j\) has finite propagation in the configuration coordinates,
bounded by \(D_j\) times that of one forward or inverse step. This
statement alone is not a decomposition into physical occupation
interactions of bounded diameter.

## 3. The actual source family, setting and unknown memory

Use the exact original pair

\[
 \psi_\pm(\Xi)=
 \frac{[I\pm(U^2-U^{-2})]\chi(\Xi)}{\sqrt Z},
 \qquad
 \chi(\Xi)=\alpha_{97,0}\otimes\Xi,
 \qquad Z=\frac{39521+154\sqrt5}{15625}.              \tag{C10}
\]

Preparation admits all 26 old-memory labels and every passive reference.
The inherited fresh-write contrast additionally restricts old memory
to \(\operatorname{span}(d_1,\ldots,d_{25})\).

The frozen source proof gives one common spectral measure
\(\mu=\mu_{\psi_+}=\mu_{\psi_-}\). It is independent of the normalized
old-memory/reference vector \(\Xi\). Explicitly, write the calibrated
operator as
\(U=\mathcal T(\widehat U\otimes I)\mathcal T^*\), with identity on
memory and references before calibration. The seed lies left of the
receiver, so \(\mathcal T^*\chi(\Xi)=\chi(\Xi)\). Its two-step
preparations also lie left of the receiver. Functional calculus and
unitarity of \(\mathcal T\) therefore reduce every spectral norm in
question to the source factor tensored with \(\Xi\). Crossings in
later powers of \(U\) are retained by this identity; they are not omitted.

Set

\[
 \delta_j^2=\int|q_j-f|^2\,d\mu.
                                                               \tag{C11}
\]

Then \(\delta_j\to0\), and for every admitted normalized \(\Xi\),

\[
 \|(q_j(U)-f(U))\psi_+(\Xi)\|
 =\|(q_j(U)-f(U))\psi_-(\Xi)\|=\delta_j.           \tag{C12}
\]

If the setting is retained in two orthogonal states, a general pure
admitted input has the form
\(|+\rangle\psi_+(\Xi_+)+|-\rangle\psi_-(\Xi_-)\), where
\(\|\Xi_+\|^2+\|\Xi_-\|^2=1\). The energy acts identically on the
setting register. Orthogonality makes the squared error the sum of the
two squared block errors, hence exactly \(\delta_j^2\). This covers
setting-memory-reference correlations and, by purification, mixed
inputs. It does not assert the same constant for an arbitrary unmarked
superposition of the two source vectors.

For every fixed \(j\), the two separate settings have identical complete
\(Q_j\) spectral laws: both are the pushforward of \(\mu\) under
\(E_0q_j\). They need not equal the entire original-\(Q\) law.

Writing \(s=E_0t/\hbar\), the scalar inequality
\(|e^{-isx}-e^{-isy}|\le|s||x-y|\) and commuting functional calculus give

\[
 \boxed{\|(e^{-itQ_j/\hbar}-e^{-itQ/\hbar})\psi\|
       \le |s|\delta_j.}                            \tag{C13}
\]

Thus the same index controls the complete evolution uniformly for
\(|s|\le3\), all admitted settings, memory and references. Trace distance
and every outcome probability after a common output instrument obey
the corresponding bound. At \(s=3\), the original evolution is \(U^3\),
and the inherited write contrast therefore obeys

\[
 \Delta p_j>1/50-6\delta_j.
                                                               \tag{C14}
\]

There exists a finite \(j\) with \(\delta_j\le1/1200\), yielding
\(\Delta p_j>3/200>1/100\) before additional implementation errors.
No particular such index has been certified or computed. This is an
existence conclusion for the unchanged prepared family and the unchanged
energy branch, not an effective finite experimental design.
The separate [actual-source certificate](SPECTRAL_CERTIFICATE.md) proves
absence of an atom for this particular source and certifies a different,
explicit normalized Abel polynomial. It does not supply a stopping index
for the general one-parameter notch sequence (C3).

## 4. A quantitative bound using a punctured cut neighborhood

The previous exact moment formula remains useful after distinguishing
the atom from its neighborhood. Define

\[
 p_n(z)=\frac1{n+1}\sum_{k=0}^n z^k,
 \qquad a_n=\int|p_n|^2\,d\mu,
 \qquad w=\mu(\{1\}),\qquad n\ge1.                 \tag{C15}
\]

Since \(p_n(1)=1\), while
\(|p_n(z)|\ge1/2\) on \(|1-z|\le1/n\),

\[
 \boxed{\mu\{0<|1-z|\le1/n\}\le4(a_n-w).}         \tag{C16}
\]

Indeed subtract the exact atomic contribution \(w\) from the integral
defining \(a_n\), and bound its remaining integrand on that punctured
neighborhood from below by \(1/4\). Also \(|p_n|\le1\), and
\(p_n(z)\to0\) for every \(z\ne1\). Dominated convergence proves
\(a_n\to w\), without a rate.

For general integers \(m,N,n\ge1\) and rational \(0<r<1\), use the
same construction with

\[
 \tau=\frac{2r^{N+1}}{(N+1)(1-r)},\quad
 b_m=\left(\frac{2+z+z^{-1}}4\right)^m,\quad
 q=\frac{\pi}{\pi+\tau}(1-b_m)(h_{r,N}+\tau).
\]

**Lemma C3.** On the actual source family, including retained settings,

\[
 \boxed{\|(q(U)-f(U))\psi\|
 \le 4n\frac{1-r}{1+r}
    +2\pi\left(1-\frac1{4n^2}\right)^m
    +4\pi\sqrt{a_n-w}+4\tau.}                     \tag{C17}
\]

**Proof.** First compare with \(q_0=(1-b_m)h_r\). Both \(q_0\) and
\(f\) lie in \([0,2\pi]\), and they agree exactly at one. On the
punctured neighborhood their difference has vector norm at most
\(2\pi\sqrt{4(a_n-w)}\), by (C16).

Outside \(|1-z|\le1/n\), formula (C5) and
\(|\cot(\theta/2)|\le2n\) give
\(|h_r-f|\le4n(1-r)/(1+r)\). Since
\((2+z+z^{-1})/4=1-|1-z|^2/4\), there also
\(b_m\le(1-1/(4n^2))^m\). Thus

\[
 |q_0-f|\le4n\frac{1-r}{1+r}
              +2\pi\left(1-\frac1{4n^2}\right)^m.
\]

Finally \(\|(1-b_m)(h_{r,N}+\tau)-q_0\|_\infty\le2\tau\).
The normalization changes \((1-b_m)(h_{r,N}+\tau)\) by at most
\((1-\pi/(\pi+\tau))(2\pi+2\tau)=2\tau\).
The triangle inequality proves (C17). QED.

All \(a_n\) are still determined by finite original seed moments. With
\(\mu_d=\langle\chi,U^d\chi\rangle\),
\(\mu_{-d}=\overline{\mu_d}\), the predecessor identity is

\[
 a_n=\frac{\displaystyle\sum_{d=-n}^n(n+1-|d|)
             (3\mu_d-\mu_{d+4}-\mu_{d-4})}
            {Z(n+1)^2}.                             \tag{C18}
\]

It needs moments only through \(n+4\). The source multiplier has value
\(1/Z\) at one, so \(w=\mu_\chi(\{1\})/Z\).
Neither this atomic weight nor the necessary moment values were
calculated here.
The companion SPECTRAL_CERTIFICATE.md obtains w=0 and an upper bound on
a_n analytically from the actual contact resolvent, without enumerating
moments. That model-specific input is separate from the general argument
of this section.

If an independent proof supplies \(0\le\ell\le w\), (C17) remains
valid with \(a_n-\ell\) in place of \(a_n-w\). Rational or algebraic
certified data, together with \(\pi<4\), then give the sufficient upper
bound

\[
 4n\frac{1-r}{1+r}
 +8\left(1-\frac1{4n^2}\right)^m
 +16\sqrt{a_n-\ell}+4\tau.                          \tag{C19}
\]

A strict gap between \(\ell\) and \(w\) can leave this particular
bound too large even though (C8) holds. Taking only \(\ell=0\) does not
resolve that issue in the presence of an atom. The exact finite moment
identity by itself supplies neither a quantitative spectral regularity
bound nor an effective convergence rate for the actual source. A useful
computed stopping certificate requires further proved input; none is
claimed here. A future scientific computation must have its own frozen
code, inputs, output and failure threshold before execution.

## 5. The global norm obstruction remains

The original full step has spectrum \(\mathbb T\), by the frozen
[full-spectrum result](https://github.com/mathorn1973/twist-j/blob/3abf054e435e31c51e6e50528b09fe3cf7cffe13/notes/C-FULL-RECORD-SCALE-LIFT-N/SPECTRAL.md).
For that operator, each finite member of this particular sequence obeys

\[
 \boxed{\|q_j(U)-f(U)\|=2\pi.}                     \tag{C20}
\]

The upper bound follows from (C4). To prove the lower bound, fix
\(\varepsilon>0\). Continuity of \(q_j\), with \(q_j(1)=0\), and
\(f(e^{-i\theta})=\theta\) for \(\theta<2\pi\), give an open arc
with \(\theta\) sufficiently close to \(2\pi\) on which
\(|q_j(e^{-i\theta})-f(e^{-i\theta})|>2\pi-\varepsilon\).
Every nonempty open arc has a nonzero spectral projection when
\(\sigma(U)=\mathbb T\): a zero projection would place every interior
point of that arc in the resolvent. Restricting to the nonzero projection
therefore gives norm at least \(2\pi-\varepsilon\). Let
\(\varepsilon\downarrow0\).

Thus pointwise convergence of the scalar readings and strong convergence
on the prepared family do not become convergence in the full operator
norm. In energy units (C20) is \(2\pi E_0\). This does not weaken the
predecessor's sharp \(\pi E_0\) lower bound for its broader comparison
class: the present notch sequence is not optimal for that global norm.
No claim of original occupation locality follows from this note alone.

## 6. Separate review obligations

1. Check the signs and branches in (C5), the geometric tail, and the
   positivity and exact \(2\pi\) bound after normalization.
2. Check the polynomial degree, coefficient specification and exact value
   at one for every finite index.
3. Check pointwise convergence at every spectral point, including an atom
   at one, and the dominated-convergence argument without separability
   or absence-of-atom assumptions.
4. Check the frozen source, all-26-label memory scope, calibration
   conjugation, equal full spectral laws and reference uniformity.
5. Check orthogonal retained-setting coherence, continuous-time bound and
   the two-setting contrast loss, without extending the constant to
   arbitrary unmarked superpositions.
6. Check subtraction of the exact atom in (C16), the normalization error
   and every constant in (C17)-(C19).
7. Check the inherited seed-moment formula, the role of a known lower
   atomic bound, and the absence of any asserted effective stopping index
   or executed certificate.
8. Check (C20) using nonzero open-arc projections and preserve the
   distinction between a fixed prepared family, global operator norm and
   physical occupation support.

These are same-session analytical claims. They do not select a different
energy branch, identify the compact apparatus Hamiltonian with the
original energy, or supply preparation, readout, renewal or native
six-pentit derivation.
