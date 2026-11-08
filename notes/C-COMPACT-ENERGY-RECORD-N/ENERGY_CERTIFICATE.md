# An exact finite-source certificate for an approximate energy reading

**NON-CANONICAL, L1, conditional analytical candidate-T.**
Owner: A. M. Thorn / C-COMPACT-ENERGY-RECORD-N, issue #1778.
Apache-2.0. Independent scientific acceptance is not asserted.

This note supplies an explicit sufficient certificate for approximating the
nominated original spectral energy on the active finite source family.
No certificate value has been computed and no passing instance is claimed.
The constructed operator has finite configuration propagation. Its admission
as a sum of geometrically local physical occupation interactions is a
separate problem, not a consequence of this construction.

## 1. Fixed source and exact scalar certificate

Use the frozen active source in
[#1777 ACTIVE_EQUAL_SPECTRUM.md](https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-FINITE-PHASE-OCCUPIED-RECORD-N/ACTIVE_EQUAL_SPECTRUM.md):

\[
 U=U_{\rm rec},\quad \chi=\alpha_{97,0}\otimes\Xi,\quad
 D=U^2-U^{-2},\quad
 \psi_\pm=(I\pm D)\chi/\sqrt Z,
 \qquad Z=(39521+154\sqrt5)/15625.                    \tag{A1}
\]

Here \(\Xi\) is any normalized old-memory/reference input. Preparation
permits all 26 old-memory labels. The receiver-only fresh-write contrast
retains the restriction to the 25-dimensional old-memory subspace excluding
\(d_0\). Mixed inputs are covered by purification. The source identities
and contrast \(\Delta p>1/50\) remain conditional predecessor premises.

For an integer \(n\ge1\), define

\[
 p_n(z)=\frac1{n+1}\sum_{j=0}^{n}z^j,\qquad
 a_n=\|p_n(U)\psi_+\|^2=\|p_n(U)\psi_-\|^2.          \tag{A2}
\]

The equality follows from the sources' identical complete spectral laws.
For \(|z|=1\), telescoping gives \(|z^j-1|\le j|z-1|\). Thus
\(|p_n(z)-1|\le n|z-1|/2\), and

\[
 \boxed{\mu_{\psi_\pm}\{|1-z|\le1/n\}\le4a_n.}       \tag{A3}
\]

Indeed \(|p_n(z)|\ge1/2\) on the stated arc; integrate its square.
The arc includes \(z=1\). No assumption excluding an atom there is made.
In particular, neither \(a_n\to0\) nor eventual success of this
certificate is asserted.

Only finite exact seed moments are needed. Put
\(\mu_\ell=\langle\chi,U^\ell\chi\rangle\), with
\(\mu_{-\ell}=\overline{\mu_\ell}\). The multiplier of the common
source spectral measure is
\(|1\pm(z^2-z^{-2})|^2/Z=(3-z^4-z^{-4})/Z\). Therefore

\[
 \boxed{a_n=\frac{\displaystyle\sum_{d=-n}^{n}
 (n+1-|d|)(3\mu_d-\mu_{d+4}-\mu_{d-4})}
 {Z(n+1)^2}.}                                      \tag{A4}
\]

This requires moments only through \(n+4\). The original step's finite
propagation and algebraic coefficients make every such moment a finite
exact algebraic calculation. No such calculation was run for this note.

The quantities in (A2)-(A4) are independent of \(\Xi\). To see this,
write \(U_{\rm rec}=\mathcal T(U_{\rm src}\otimes I)\mathcal T^*\).
The initial source support lies strictly left of the receiver, so
\(\mathcal T^*\) is identity on it. For every polynomial, including
negative powers, the final \(\mathcal T\) preserves the norm, leaving
the source polynomial tensored with \(\Xi\). This argument does not
discard future crossings or old-memory correlations.

If the two settings are retained in an orthogonal setting register and
the energy acts identically on that register, their coherent superposition
also satisfies (A3): the two setting blocks have the same value \(a_n\),
and their squared norms add. This remains true when setting and old memory
are correlated with a passive reference. It does not identify an unmarked
arbitrary superposition of \(\psi_+\) and \(\psi_-\) with that contract.

## 2. A positive finite-propagation approximation

Let \(f(e^{-i\theta})=\theta\) for \(0\le\theta<2\pi\), including
\(f(1)=0\), and \(Q=E_0f(U)\), where \(E_0>0\) is the fixed energy
unit. For rational \(0<r<1\), define the norm-convergent series

\[
 h_r(U)=\pi I-i\sum_{k\ge1}\frac{r^k}{k}(U^k-U^{-k}). \tag{A5}
\]

For \(0<\theta<2\pi\), the logarithmic power series gives

\[
 h_r(e^{-i\theta})=\pi+2\arg(1-re^{i\theta})
 =\theta+2\arctan\!\left(
 \frac{1-r}{1+r}\cot\frac\theta2\right).             \tag{A6}
\]

The argument is the continuous branch in \((-\pi/2,\pi/2)\), since
\(\operatorname{Re}(1-re^{i\theta})>0\). Thus
\(0\le h_r\le2\pi\), and \(h_r(1)=\pi\). The latter differs from
\(f(1)=0\); the near-cut estimate (A3) explicitly pays for it.

For an integer \(N\ge1\), truncate (A5) after \(N\) and set

\[
 \tau=\frac{2r^{N+1}}{(N+1)(1-r)},\qquad
 q_{r,N}=h_{r,N}+\tau I,\qquad Q_{r,N}=E_0q_{r,N}.    \tag{A7}
\]

The geometric tail estimate gives \(\|h_r-h_{r,N}\|\le\tau\).
Consequently

\[
 0\le q_{r,N}\le(2\pi+2\tau)I,\qquad
 [q_{r,N},U]=[q_{r,N},f(U)]=0.                        \tag{A8}
\]

It is a Laurent polynomial of degree \(N\), hence has propagation at
most \(N\) times that of \(U\) in configuration coordinates. It is
conserved under the original discrete evolution. The two phase settings
have identical entire \(Q_{r,N}\) distributions, since this operator is
a fixed function of the same \(U\).

## 3. Action and continuous-time error on the actual source family

Outside the arc \(|1-e^{-i\theta}|\le1/n\), one has
\(|\cot(\theta/2)|\le2n\). Equations (A3) and (A6), together with
\(|\arctan x|\le|x|\), therefore give

\[
 \boxed{\|(q_{r,N}-f(U))\psi\|\le\delta,
 \quad \delta=4n\frac{1-r}{1+r}+4\pi\sqrt{a_n}+2\tau.} \tag{A9}
\]

Here \(\psi\) may include the retained setting and any admitted memory
and reference as above. On the arc, the scalar difference between \(h_r\)
and \(f\) is bounded by \(2\pi\); its vector contribution is at most
\(2\pi\sqrt{4a_n}\). Outside it use the uniform bound from (A6), then
add \(\|q_{r,N}-h_r\|\le2\tau\). This bounds the original energy
action, not merely its expectation or a finite compression.

Write physical time as \(s=E_0t/\hbar\). Commuting functional calculus
and \(|e^{-isx}-e^{-isy}|\le|s||x-y|\) give

\[
 \|(e^{-itQ_{r,N}/\hbar}-e^{-itQ/\hbar})\psi\|
 \le |s|\delta.                                     \tag{A10}
\]

Thus one certificate controls every real time \(|s|\le3\), not just
one endpoint. At integer \(s=m\), the original evolution is exactly
\(U^m\). The bound is uniform with a reference and hence also bounds
trace distance after any common complete output instrument.

For the two admitted phase settings at \(s=3\), each receiver
probability changes by at most \(3\delta\), so

\[
 \Delta p_{r,N}>1/50-6\delta.                        \tag{A11}
\]

A sufficient prospective target is \(\delta\le1/1200\), yielding
\(\Delta p_{r,N}>3/200>1/100\). For a purely rational-algebraic
certificate one may replace \(4\pi\sqrt{a_n}\) in (A9) by
\(16\sqrt{a_n}\), using \(\pi<4\), and require the resulting upper
bound to be at most \(1/1200\). Such a test must freeze \(n,r,N\) and
the exact arithmetic implementation before execution. It has not passed
or even been run here. Preparation, measurement and other implementation
errors would consume additional portions of the remaining contrast margin.

## 4. Admission boundaries and review targets

The actual source value \(a_n\), rather than a fitted spectral density,
decides the sufficient test. A nonzero atom at the branch cut can prevent
this particular test from succeeding. Failure at one finite \(n,r,N\)
does not prove an impossibility of approximation. Even without an atom,
the required \(n\) and polynomial degree may be large; this note supplies
no economical size estimate or shrinking hardware claim.

Finite configuration propagation does not imply bounded physical
interaction diameter. A term \(U^k\) may jointly move physically
separated occupation factors. The [global physical obstruction](ENERGY_BRIDGE.md)
therefore remains intact. No onsite energy, physical local decomposition,
thermal preparation, autonomous clock, funded detector, reset mechanism
or original-six-pentit derivation is supplied by (A5)-(A10). The existing
apparatus cannot be assigned \(Q_{r,N}\) as its energy without new
interaction and preparation accounts.

Separate review targets are: (i) the chord-arc bound including an atom at
one; (ii) the exact moment identity and setting/reference uniformity;
(iii) signs and branches in the Abel formula; (iv) positive truncation and
all error constants; (v) continuous-time transport and the contrast margin;
and (vi) preservation of the physical-locality and unexecuted-certificate
boundaries. These are same-session analytical statements awaiting external
acceptance, with no scientific executable or numerical experiment run.
