# Exact two-port lift of the bound-pair contact

**NON-CANONICAL / L1 / conditional analytical candidate.**
Author: A. M. Thorn <thorn@twistj.com>. SPDX-License-Identifier: Apache-2.0.
Reservation: [#1812](https://github.com/mathorn1973/twist-j/issues/1812).
This is a conditional construction, not a claim of native admission or
physical particle identification. No scientific executable was used to derive it.

## 1. Fixed source model and notation

Use the original two-constituent Hilbert space

\[
\mathcal H=\ell^2(\mathbb Z_R\times\mathbb Z_r)\otimes\mathbb C^4,
\qquad F=S M_2,
\qquad M_2=\frac{(I+2iX)\otimes(I+2iX)}5.
\]

Let \(P_0\) denote the orthogonal projection onto coincidence \(r=0\),
including all center positions and all four coin components. For a real
contact phase \(g\), set

\[
\Gamma_g=e^{-igP_0}=I+(e^{-ig}-1)P_0,
\qquad W_g=\Gamma_gF.
\tag{PB-1}
\]

The original bound-pair theorem uses \(g=2\pi/5\). Its statement and scope
are inherited unchanged: a simple localized relative bound branch at small
center momentum, its finite prepared wave packets, and its proved averaged
response to a momentum impulse. No new species, energy reading, or clock is
introduced by calling the same branch a branch of an enlarged operator.

Write \(\zeta=e^{ig}\), \(\varphi=(1+\sqrt5)/2\), and
\(J=1+\zeta^2=\zeta/\varphi\) at the nominated phase. The elementary
identity noted by the author is valid:

\[
t=\varphi^{-1},\quad t^2+t=1,
\qquad \tan(2\arctan t)=\frac{2t}{1-t^2}=2.
\tag{PB-2}
\]

This is a precise relation between the chosen parameters and the polar
data of \(J\). It does not select the Cayley transform or the carrier by
itself.

## 2. Symmetric common contact

Introduce one two-dimensional port with computational basis \(|0\rangle,
|1\rangle\), Pauli matrix \(X_p\), and normalized eigenvectors
\(|\pm\rangle=(|0\rangle\pm|1\rangle)/\sqrt2\). Write
\(\Pi_\pm=|\pm\rangle\langle\pm|\). Tensor order is port first.

Define the single contact and the single complete step by

\[
\mathbb C_g=\exp(igX_p\otimes P_0),
\qquad \mathbb W_g=\mathbb C_g(I_p\otimes F).
\tag{PB-3}
\]

The contact acts only at coincidence, has no spatial hopping, and is
unitary. Its exact spectral decomposition on the port is

\[
\mathbb C_g=\Pi_+\otimes\Gamma_g^\dagger
             +\Pi_-\otimes\Gamma_g,
\qquad
\boxed{\mathbb W_g=\Pi_+\otimes W_{-g}+\Pi_-\otimes W_g.}
\tag{PB-4}
\]

**Proof.** On a port eigenvector of \(X_p\) with eigenvalue \(s\), the
exponential in (PB-3) is \(e^{isgP_0}=\Gamma_{-sg}\). Multiplication by
\(I_p\otimes F\) proves (PB-4). Orthogonality of the two port projectors
then proves full unitarity and, for every integer \(n\),

\[
\mathbb W_g^n=\Pi_+\otimes W_{-g}^{n}
              +\Pi_-\otimes W_g^{n}.
\tag{PB-5}
\]

No commutation of \(F\) with \(P_0\) or \(\Gamma_g\) is assumed.

Thus one supplied local law contains the original binding walk as an
exact invariant port sector. The other sector has the opposite contact
phase. The enlargement supplies the port, its preparation and this local
interaction; it does not derive those resources from the original native
checkpoint update.

## 3. Exact sum/difference factorization and the golden coefficient

For any unitary \(R\), define

\[
V_R=\frac12\begin{pmatrix}I+R&I-R\\I-R&I+R\end{pmatrix}
    =\Pi_+\otimes I+\Pi_-\otimes R.
\tag{PB-6}
\]

The symmetric contact satisfies the exact full-space equality

\[
\boxed{\mathbb C_g=(I_p\otimes\Gamma_g^\dagger)V_{\Gamma_g^2}.}
\tag{PB-7}
\]

Indeed the two port sectors on the right are \(\Gamma_g^\dagger\) and
\(\Gamma_g^\dagger\Gamma_g^2=\Gamma_g\). The common factor
\(\Gamma_g^\dagger\) is a coincidence-local phase, not a scalar global
phase on \(\mathcal H\). It must remain part of the law. It cannot be
dropped when the state has both coincident and noncoincident components.

For port input \(|0\rangle\), the two output operators of the complete
step are

\[
\begin{aligned}
A_0&=\frac{W_{-g}+W_g}{2}
 =\bigl[(I-P_0)+\cos(g)P_0\bigr]F,\\
A_1&=\frac{W_{-g}-W_g}{2}
 =i\sin(g)P_0F.
\end{aligned}
\tag{PB-8}
\]

They obey

\[
A_0^\dagger A_0+A_1^\dagger A_1=I,
\quad A_1^\dagger A_1=\sin^2(g)F^\dagger P_0F.
\tag{PB-9}
\]

At \(g=2\pi/5\),

\[
\cos g=\frac1{2\varphi},\quad
\cos^2g=\frac{3-\sqrt5}{8},\quad
\sin^2g=\frac{5+\sqrt5}{8}.
\tag{PB-10}
\]

On the coincidence subspace, the plus branch of \(V_{\Gamma_g^2}\)
before the common factor is

\[
\frac{1+e^{-2ig}}2=\frac{\overline J}{2}
 =e^{-ig}\frac1{2\varphi}.
\tag{PB-11}
\]

The nominated orientation of the original contact produces \(\overline J\);
reversing that phase convention produces \(J\). Multiplication by the
retained factor \(\Gamma_g^\dagger\) gives the real coefficient
\(1/(2\varphi)\) in (PB-8). Thus the original contact phase \(g\), the
relative two-path phase \(2g\), and the principal golden output weight are
related exactly, without changing the original minus-sector walk to
\(W_{2g}\).

For any normalized input density operator \(\rho\), with arbitrary
passive references allowed, the declared Hilbert-space output rule gives

\[
p_1=\sin^2g\,\operatorname{Tr}(\rho F^\dagger P_0F),
\qquad p_0=1-p_1.
\tag{PB-12}
\]

The constant \((3-\sqrt5)/8\) is the conditional zero-port probability
for a state arriving entirely at coincidence. It is not the capture
probability of a general incoming packet. The output bit tests coincidence
through this chosen instrument; it does not by itself herald a bound pair.

## 4. Preservation of the original bound branch and impulse response

Define the isometry \(\iota_-\psi=|-\rangle\otimes\psi\). Then

\[
\mathbb W_g\iota_-=\iota_-W_g,
\qquad
\mathbb W_g^n\iota_-=\iota_-W_g^n.
\tag{PB-13}
\]

Consequently every statement about the original step, including arbitrary
finite or asymptotic histories, is retained exactly after embedding all
states and observables through \(\iota_-\). For example, if in the
center-momentum fiber

\[
W_g(P)\chi_P=e^{-i\Omega(P)}\chi_P,
\]

then

\[
\mathbb W_g(P)(|-\rangle\otimes\chi_P)
 =e^{-i\Omega(P)}|-\rangle\otimes\chi_P.
\tag{PB-14}
\]

The original dispersion, relative localization, and
\(\Omega''(0)=\sqrt{16\varphi+7}/20\) are unchanged. The original finite
packet/impulse theorem is unchanged because its object kicks and readers
can be tensored with \(I_p\), leaving the minus port invariant. This is
an exact embedding of the existing theorem, not a new derivation of its
curvature or a physical electron mass.

Reading the computational port of \(|-\rangle\otimes W_g\psi\) gives
probabilities \(1/2,1/2\), independently of the object. Conditioned on
either result the object is still \(W_g\psi\), but the port is now
\(|0\rangle\) or \(|1\rangle\), not \(|-\rangle\). A subsequent
unmodified step therefore follows both contact laws. Restoring the minus
port is an extra operation with its own record/resource contract.

## 5. Computational preparation compares two laws

For the different preparation \(|0\rangle\otimes\psi\), coherent reuse
of the same unmeasured port gives

\[
\mathbb W_g^n(|0\rangle\otimes\psi)
 =\frac{|+\rangle\otimes W_{-g}^{n}\psi
        +|-\rangle\otimes W_g^{n}\psi}{\sqrt2}.
\tag{PB-15}
\]

In computational output coordinates the two whole-history blocks are

\[
\frac{W_{-g}^{n}+W_g^{n}}2,
\qquad \frac{W_{-g}^{n}-W_g^{n}}2.
\tag{PB-16}
\]

They are not \(A_0^n,A_1^n\), nor do they describe fresh port measurements
at each tick. For one computational input with the output port ignored,
the reduced channel is

\[
\mathcal E_g(\rho)
 =A_0\rho A_0^\dagger+A_1\rho A_1^\dagger
 =\tfrac12\bigl(W_{-g}\rho W_{-g}^\dagger
                  +W_g\rho W_g^\dagger\bigr).
\tag{PB-17}
\]

Repeating this channel requires a fresh or reset port for every step.
Reusing one coherent port instead gives the two histories (PB-15).

There is also a sharp preparation boundary. Suppose a fixed port density
operator \(\tau\) makes the reduced object step equal to conjugation by
\(W_g\) for every object input. Put
\(p=\operatorname{Tr}(\tau\Pi_+)\). Partial tracing (PB-4) gives
\(p\,\mathrm{Ad}_{W_{-g}}+(1-p)\,\mathrm{Ad}_{W_g}\). If \(p>0\),
equality forces \(\mathrm{Ad}_{W_{-g}}=\mathrm{Ad}_{W_g}\), hence
\(W_{-g}W_g^\dagger=\Gamma_g^{-2}\) must be scalar. For a nontrivial
coincidence projection and \(g=2\pi/5\), its eigenvalues are
\(1,e^{2ig}\), which are distinct. Therefore \(p=0\), and positivity
of \(\tau\) gives \(\tau=\Pi_-\). The exact original all-input law
and the nontrivial golden computational-port instrument have different
ready preparations.

## 6. Exact one-step disturbance of a moving bound state

Fix a fiber where \(W_g(P)\) has its normalized rank-one bound state
\(\chi=\chi_P\), write \(B=|\chi\rangle\langle\chi|\), and put
\(w=\langle\chi,P_0\chi\rangle\). Equation (PB-1) gives

\[
W_{-g}\chi=\Gamma_g^{-2}W_g\chi
           =e^{-i\Omega(P)}\Gamma_g^{-2}\chi.
\]

For the computational-input channel (PB-17), the exact probability of
remaining in the original rank-one bound branch after one step is

\[
\begin{aligned}
\operatorname{Tr}\bigl(B\mathcal E_g(B)\bigr)
 &=\tfrac12\left(1+
       |(1-w)+e^{2ig}w|^2\right)\\
 &=1-2w(1-w)\sin^2g.
\end{aligned}
\tag{PB-18}
\]

For \(0<w<1\) and \(g=2\pi/5\), leakage from that nominated branch is
strictly positive. This is leakage from one selected bound projector;
it must not be called a complete breakup probability without excluding
all other bound sectors.

In fact the strict inequalities hold at every
\(0<|P|\le1/12\), without requiring the complete finite-strip
exceptional-set polynomial. The inherited uniform-gap proof gives

\[
|\langle b_0,\chi_P\rangle|^2
\ge\frac{8424}{11449}>\frac12,
\qquad b_0=\delta_{r=0}A.
\tag{PB-18a}
\]

Since \(P_0b_0=b_0\), Cauchy--Schwarz gives
\(w(P)\ge|\langle b_0,\chi_P\rangle|^2>0\).
To prove \(w(P)<1\), suppose otherwise. Then the normalized eigenstate
is supported only at \(r=0\), with coin vector \((a,b,c,d)^T\).
The second and third streaming rows have no incoming support at that
site, so the eigenvalue equations there force \(b=c=0\). Absence of
outgoing amplitudes at the neighboring relative sites further forces

\[
(M_2\chi)_2(0)=(M_2\chi)_3(0)
 =\frac{2i}{5}(a+d)=0.
\]

Hence \(d=-a\ne0\). The first and fourth coin rows then equal
\(a,d\), and their eigenvalue equations are

\[
e^{-ig}e^{iP}a=\lambda(P)a,
\qquad
e^{-ig}e^{-iP}d=\lambda(P)d.
\]

Thus \(e^{iP}=e^{-iP}\), so \(P=0\) or \(\pi\) modulo
\(2\pi\). Neither is in \(0<|P|\le1/12\). This contradiction
proves \(0<w(P)<1\) throughout that punctured interval and makes
(PB-18) strictly smaller than one there.

For a normalized packet \(\psi(P)=f(P)\chi_P\) supported in
the proved branch interval, the leakage measured by the direct-integral band projector
\(\mathcal B=\int^\oplus\Pi_b(P)\,dP/(2\pi)\), rather than
fidelity with the original packet, is exactly
\(2\sin^2g\int |f(P)|^2w(P)[1-w(P)]\,dP/(2\pi)\). No
plane-wave normalization is being assigned a physical probability.
Every such nonzero normalizable packet has strictly positive leakage:
its momentum weight cannot be supported only at the measure-zero
point \(P=0\). There is no positive bound uniform over all packets;
one may concentrate normalized packets arbitrarily near zero, where
continuity gives \(w(P)\to1\).

At \(P=0\) the original compact state is
\(\chi_0=\delta_{r=0}A\), \(A=(|++\rangle-|--\rangle)/\sqrt2\).
There \(w=1\), \(F(0)\chi_0=\chi_0\), and
\(W_{\pm g}(0)\chi_0=e^{\mp ig}\chi_0\). Hence both branches leave
the object ray unchanged, while the port evolves. This exceptional
fiber must not be used to claim non-disturbance for the moving family.

## 7. Plain identity/contact lift and the factor-of-two warning

The alternative contact \(V_{\Gamma_g}\) gives

\[
V_{\Gamma_g}(I_p\otimes F)
 =\Pi_+\otimes F+\Pi_-\otimes W_g.
\tag{PB-19}
\]

It also retains the original walk exactly in the minus sector. Its
computational branches are \((I\pm\Gamma_g)F/2\). On coincidence,
the zero-output probability is
\(\cos^2(g/2)=(3+\sqrt5)/8\), rather than the principal small golden
weight. Replacing \(\Gamma_g\) by \(\Gamma_g^2\) in (PB-19) alone
would change the interacting sector to \(W_{2g}\). The symmetric
construction (PB-7) avoids this replacement by retaining the common
local phase and adding the opposite \(-g\) sector.

## 8. Relation to the five-cycle instrument

The earlier cyclotomic instrument uses the regular five-cycle
\(C|r\rangle=|r+1\bmod5\rangle\), \(R=C^2\), and
\((I\pm R)/2\). Its full space has all five roots of unity as spectral
values; its balanced four-dimensional space has all four nontrivial
ones. In contrast, \(\Gamma_g^2\) has just
\(\{1,e^{-2ig}\}\). Therefore no full unitary equivalence of those
operators or of their complete instruments follows. Their spectra
already rule it out at the nominated carriers.

The identity (PB-11) identifies one scalar character, with its phase
orientation explicitly stated. The exact common-carrier statement here
is (PB-3)--(PB-14), not an identification of the original five-cycle
source with the two-constituent position space.

All displayed local matrices belong to the cyclotomic coefficient ring
\(\mathbb Z[\zeta_{20},1/10]\) on their complete finite-support module.
The displayed port blocks introduce halves; it would be false to call
them automorphisms of the original unlocalized integer module merely
because their entries are exact. Preparation of normalized
\(|-\rangle\) also retains its one fixed normalization scalar. No new
integer-residue realization is claimed.

## 9. Capture boundary and compatibility with the inherited apparatus

For the time-independent pair step \(W_g\), the fiberwise relative-bound
projector \(B=\int^\oplus\Pi_b(P)\,dP/(2\pi)\), set to zero outside
the nominated branch interval, commutes with the evolution. An initial
state with \(B\psi=0\) retains zero weight in that branch forever.
More generally the fiberwise full relative pure-point projection has
the same invariance. This is a relative-bound assertion at fixed center
momentum; the center may itself propagate, so global spectral type must
not be confused with relative binding. A proper incoming state in the
relative absolutely continuous channel cannot be permanently captured
into a relative bound branch by the isolated two-body law alone.

The same observation applies separately in each invariant port sector
of (PB-4). Preparing a vector which already has bound overlap is not
capture from an asymptotically unbound input. The port lift by itself
does not supply a channel that transports away binding energy.

The existing homogeneous capture-current-record model includes an
additional standing-token/moving-pulse arrangement. Its separate local
capture rotation has entries \(3/5,4/5\); it must not be conflated with
the internal \(\Gamma_g\) binding contact. That model already supplies
a route from a zero-bound-weight incoming arrangement to a bound pair
plus outgoing pulse and receiver record.

One may enlarge its whole carrier by the same port and replace each
internal object \(W_g\) by (PB-4), while tensoring the arrangement
contact and receiver gates with \(I_p\). The resulting minus-port
sector is exactly the original complete apparatus. For a ready minus
port and every original state \(\rho\), reader \(Q\), and integer
time, the lifted expectation equals the original expectation. The
same equality holds for the corresponding scattering construction
when all inherited wave-operator premises are retained. Thus the
original capture probability, including a future frozen momentum
family, can be used unchanged on that sector.

This equivalence does not extend to computational-port preparation
or repeated computational-port reading/reset. Those operations change
the dynamics as (PB-17)--(PB-18) show. The lift does not establish a
physical photon/electron identification, an occurrence law, or an
implementation by the original native checkpoint law.

## 10. Primary source links

- Original source definitions, bound response and homogeneous theorem:
  https://github.com/mathorn1973/twist-j/blob/a193e389fb1ddb0bdc89165b015c95a17eb1e425/canon/CORE.md
- Full homogeneous carrier, original W_g, token/pulse rotation, packet,
  bound projector and outgoing event:
  https://github.com/mathorn1973/twist-j/blob/a193e389fb1ddb0bdc89165b015c95a17eb1e425/notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/README.md
- The uniform overlap bound used in (PB-18a), proof section 4.3:
  https://github.com/mathorn1973/twist-j/blob/a193e389fb1ddb0bdc89165b015c95a17eb1e425/notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/PROOF_CAPTURE_SCATTERING.md
- Earlier complete five-cycle instrument, especially §§1--3 and 6:
  https://github.com/mathorn1973/twist-j/blob/a193e389fb1ddb0bdc89165b015c95a17eb1e425/notes/C-J-TWO-PATH-NATIVE-BOUNDARY-N/PROOF.md

The construction is general for projection-phase contacts; the golden
constants are the specialization at the existing chosen value of g.
No uniqueness or physical necessity is inferred from the ability to
write this unitary enlargement.
