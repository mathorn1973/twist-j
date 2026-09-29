# Exact discrete defect contrast for the two photon twist modes

**PUBLIC, NON-CANONICAL. Written proof candidate. Separate review required.**

- Claim: C-PHOTON-DISCRETE-DEFECT-CONTRAST-N
- Owner: #1220
- Basis: Public Canon v92 and the unchanged four-dimensional fixed weight used by the current photon notes
- Status: candidate-T
- Scope: finite-volume exact algebra only
- No claim: no positive thermodynamic floor, no P1 closure, no P2, S7, continuum, apparatus, PHOTON-MASSLESS-PHASE closure or physical photon

The point of this note is narrow. The two continuous twist derivatives that remain in the sufficient P1 route can be replaced exactly by one-plaquette discrete source defects. Pairing the two nontrivial real Galois modes then removes every golden irrational coefficient and leaves one rational ratio built from three integers.

## 1. Fixed source partition sum

Let

\[
\zeta=\zeta_5,\qquad \vartheta=\frac{2\pi}{5},
\qquad W(f)=2+\zeta^f+\zeta^{-f},
\]

for \(f\in\mathbb F_5\). Equivalently,

\[
W(0)=4,\qquad
W(\pm1)=\varphi^2=1+\varphi,\qquad
W(\pm2)=\varphi^{-2}=2-\varphi.
\]

For a discrete plaquette source \(b\in C^2(K_L;\mathbb F_5)\), define

\[
Z_L[b]
=
\sum_{a\in C^1(K_L;\mathbb F_5)}
\prod_p W((da)_p+b_p).
\tag{1}
\]

This is the discrete-source specialization of the real source partition function

\[
\mathcal Z_L(B)
=
\sum_a
\prod_p
w(\vartheta(da)_p+B_p),
\qquad
w(u)=2+2\cos u.
\tag{2}
\]

Thus

\[
Z_L[b]=\mathcal Z_L(\vartheta b).
\tag{3}
\]

Let \(\Sigma\) be one positively oriented 01 seam. It contains exactly \(L^2\) plaquettes. Fix \(p\in\Sigma\), and write \(\delta_p\) for the unit plaquette source there.

The same cut flux as in the preceding notes is

\[
F=\langle n,\Sigma\rangle.
\tag{4}
\]

For \(k=1,2\),

\[
\Psi_L(\theta_k)
=
\frac{Z_L[k\Sigma]}{Z_L[0]}
=
\mathbb E(e^{i\theta_k F}),
\qquad
\theta_k=k\vartheta,
\tag{5}
\]

and

\[
C_{L,k}
=
\Phi'_k(0)
=
\mathbb E(F e^{i\theta_kF}).
\tag{6}
\]

Hence

\[
\Psi_L'(\theta_k)=iC_{L,k}.
\tag{7}
\]

No positivity estimate is used below.

## 2. Local finite-difference identity

For every integer \(f\) and \(r\in\{1,2\}\),

\[
W(f+r)-W(f-r)
=
(\zeta^r-\zeta^{-r})(\zeta^f-\zeta^{-f}).
\tag{8}
\]

Indeed,

\[
\begin{aligned}
W(f+r)-W(f-r)
&=
\zeta^{f+r}+\zeta^{-f-r}
-\zeta^{f-r}-\zeta^{-f+r}\\
&=
(\zeta^r-\zeta^{-r})(\zeta^f-\zeta^{-f}).
\end{aligned}
\]

At \(u=\vartheta f\),

\[
w'(u)
=
i(\zeta^f-\zeta^{-f}),
\tag{9}
\]

while

\[
2\sin(r\vartheta)
=
\frac{\zeta^r-\zeta^{-r}}{i}.
\tag{10}
\]

Therefore

\[
\boxed{
w'(\vartheta f)
=
\frac{W(f+r)-W(f-r)}
     {2\sin(r\vartheta)}.
}
\tag{11}
\]

This is special to the present local weight. It is not a generic finite-difference approximation. It is an exact identity on all five local states.

Differentiate (2) with respect to one plaquette source at the discrete background \(B=\vartheta b\). Equation (11) gives

\[
\left.
\frac{\partial\mathcal Z_L(B)}
     {\partial B_p}
\right|_{B=\vartheta b}
=
\frac{
Z_L[b+r\delta_p]-Z_L[b-r\delta_p]
}{
2\sin(r\vartheta)
}.
\tag{12}
\]

At \(b=k\Sigma\), translations parallel to the seam act transitively on its \(L^2\) plaquettes and leave the background \(k\Sigma\) invariant. Therefore every plaquette derivative on the seam is equal, and

\[
\Psi_L'(\theta_k)
=
\frac{L^2}{2\sin(r\vartheta)}
\frac{
Z_L[k\Sigma+r\delta_p]
-
Z_L[k\Sigma-r\delta_p]
}{
Z_L[0]
}.
\tag{13}
\]

Combining (7) and (13) gives the exact defect formula

\[
\boxed{
C_{L,k}
=
i\,\frac{L^2}{2\sin(r\vartheta)}
\frac{
Z_L[k\Sigma-r\delta_p]
-
Z_L[k\Sigma+r\delta_p]
}{
Z_L[0]
}.
}
\tag{14}
\]

The sign and the factor \(i\) are fixed. Reversing the orientation of \(F\) reverses the sign of \(C_{L,k}\) but does not affect its squared modulus.

For the two modes below use

\[
(k,r)=(1,1),\qquad (k,r)=(2,2).
\tag{15}
\]

Thus the continuous derivative has disappeared. It is exactly one discrete one-plaquette defect contrast.

## 3. Binary-pair Gram identity

The local weight factors exactly:

\[
W(f)
=
(1+\zeta^f)(1+\zeta^{-f}).
\tag{16}
\]

Expand both binary factors independently on every plaquette. Let

\[
S,T\in\{0,1\}^{P(K_L)}.
\]

Then

\[
\prod_p W((da)_p+b_p)
=
\sum_{S,T}
\zeta^{\langle S-T,da+b\rangle}.
\tag{17}
\]

Using the cochain-chain pairing,

\[
\langle S-T,da\rangle
=
\langle\partial(S-T),a\rangle
\pmod5.
\tag{18}
\]

Summing independently over every link field \(a_e\in\mathbb F_5\) gives the finite character orthogonality relation

\[
\sum_{a\in C^1}
\zeta^{\langle\partial(S-T),a\rangle}
=
5^{|E|}
\,1_{\partial S=\partial T\pmod5}.
\tag{19}
\]

For every boundary value \(\beta\in C^1(K_L;\mathbb F_5)\), define

\[
\mathcal B_\beta
=
\{S\in\{0,1\}^{P(K_L)}:\partial S=\beta\pmod5\}
\tag{20}
\]

and

\[
A_\beta(b)
=
\sum_{S\in\mathcal B_\beta}
\zeta^{\langle S,b\rangle}.
\tag{21}
\]

Equations (17) to (21) give

\[
\begin{aligned}
Z_L[b]
&=
5^{|E|}
\sum_\beta
\sum_{S,T\in\mathcal B_\beta}
\zeta^{\langle S,b\rangle}
\zeta^{-\langle T,b\rangle}\\
&=
\boxed{
5^{|E|}
\sum_\beta
A_\beta(b)\overline{A_\beta(b)}.
}
\tag{22}
\end{aligned}
\]

This is an exact Gram-square representation for every discrete source, not only cocycles.

At \(b=0\), let

\[
m_\beta=|\mathcal B_\beta|.
\tag{23}
\]

Then

\[
\boxed{
N_L
:=
5^{-|E|}Z_L[0]
=
\sum_\beta m_\beta^2
\in\mathbb Z_{>0}.
}
\tag{24}
\]

For arbitrary \(b\), each term in (22) is fixed by complex conjugation. Hence

\[
5^{-|E|}Z_L[b]
\in
\mathbb Z[\zeta+\zeta^{-1}]
=
\mathbb Z[\varphi].
\tag{25}
\]

This integrality is important below.

Equation (22) is not a thermodynamic lower bound. Gram positivity by itself allows two nearby source norms to be equal.

## 4. Exact Galois covariance

Let

\[
\sigma_r(\zeta)=\zeta^r,
\qquad
r\in\mathbb F_5^\times.
\tag{26}
\]

Then

\[
\sigma_r(W(f))=W(rf).
\tag{27}
\]

Applying \(\sigma_r\) to (1),

\[
\sigma_r(Z_L[b])
=
\sum_a
\prod_p
W(r(da)_p+rb_p).
\tag{28}
\]

The change of link variable \(a'=ra\) is a bijection of \(C^1(K_L;\mathbb F_5)\), and \(d(ra)=r\,da\). Therefore

\[
\boxed{
\sigma_r(Z_L[b])=Z_L[rb].
}
\tag{29}
\]

In particular \(Z_L[0]\) is Galois fixed. Equation (24) already identifies its normalized value as a positive rational integer.

Define the normalized first defect

\[
\widehat\Delta_L
:=
5^{-|E|}
\left(
Z_L[\Sigma-\delta_p]
-
Z_L[\Sigma+\delta_p]
\right).
\tag{30}
\]

By (25), there are unique integers \(A_L,B_L\) such that

\[
\boxed{
\widehat\Delta_L=A_L+B_L\varphi.
}
\tag{31}
\]

The real nontrivial Galois automorphism is the restriction of \(\sigma_2\). Since

\[
\varphi=1+\zeta+\zeta^{-1},
\qquad
\sigma_2(\varphi)
=
1+\zeta^2+\zeta^{-2}
=
1-\varphi,
\tag{32}
\]

equation (29) gives

\[
\begin{aligned}
5^{-|E|}
\left(
Z_L[2\Sigma-2\delta_p]
-
Z_L[2\Sigma+2\delta_p]
\right)
&=
\sigma_2(\widehat\Delta_L)\\
&=
\boxed{
A_L+B_L(1-\varphi).
}
\tag{33}
\end{aligned}
\]

Thus the two defect contrasts required by (14) are a Galois pair.

## 5. The two-mode irrationality cancels exactly

From (14), (15), (24), (31) and (33),

\[
|C_{L,1}|^2
=
\frac{L^4}{N_L^2}
\frac{(A_L+B_L\varphi)^2}
     {4\sin^2(2\pi/5)},
\tag{34}
\]

and

\[
|C_{L,2}|^2
=
\frac{L^4}{N_L^2}
\frac{(A_L+B_L(1-\varphi))^2}
     {4\sin^2(4\pi/5)}.
\tag{35}
\]

The exact pentagonal values are

\[
4\sin^2(2\pi/5)=2+\varphi,
\qquad
4\sin^2(4\pi/5)=3-\varphi.
\tag{36}
\]

Also

\[
(2+\varphi)(3-\varphi)=5.
\tag{37}
\]

Put

\[
x=A+B\varphi,
\qquad
x^\sigma=A+B(1-\varphi).
\tag{38}
\]

Then

\[
\frac{x^2}{2+\varphi}
+
\frac{(x^\sigma)^2}{3-\varphi}
=
\frac{
(3-\varphi)x^2+(2+\varphi)(x^\sigma)^2
}{5}.
\tag{39}
\]

Using \(\varphi^2=\varphi+1\), the numerator in (39) is

\[
5A^2+5B^2.
\tag{40}
\]

The mixed \(AB\) term cancels exactly. Therefore

\[
\boxed{
\frac{(A+B\varphi)^2}{2+\varphi}
+
\frac{(A+B(1-\varphi))^2}{3-\varphi}
=
A^2+B^2.
}
\tag{41}
\]

Substitute \(A=A_L\), \(B=B_L\) into (34) and (35):

\[
\boxed{
|C_{L,1}|^2+|C_{L,2}|^2
=
L^4\frac{A_L^2+B_L^2}{N_L^2}.
}
\tag{42}
\]

This is the main result of the note.

The irrational local weights have not been approximated or removed from the model. Their two real Galois embeddings have combined into the Euclidean square of the two integer coefficients of one defect contrast.

## 6. Conditional P1 consequence

This section uses #1213 and #1216 only at their declared NON-CANONICAL candidate scope.

Their current sufficient chain is

\[
\Delta_L(q)
\ge
H_L
\ge
\frac45
\left(
|C_{L,1}|^2+|C_{L,2}|^2
\right)
\tag{43}
\]

for every admitted nonzero temporal character \(q\).

Equation (42) turns (43) into

\[
\boxed{
\Delta_L(q)
\ge
H_L
\ge
\frac45
L^4\frac{A_L^2+B_L^2}{N_L^2}.
}
\tag{44}
\]

No limit has been taken.

The sufficient fixed-model thermodynamic target is now exactly

\[
\boxed{
\liminf_{\substack{L\to\infty\\L\ {\rm even}}}
L^4\frac{A_L^2+B_L^2}{N_L^2}>0.
}
\tag{45}
\]

Equivalently, for some \(c>0\) and all sufficiently large even \(L\),

\[
\sqrt{A_L^2+B_L^2}
\ge
c\,\frac{N_L}{L^2}.
\tag{46}
\]

Equation (45) is not proved here.

If \(A_L\) and \(B_L\) are not both zero at a fixed volume, integrality gives only

\[
A_L^2+B_L^2\ge1.
\tag{47}
\]

That lower bound is exponentially too weak because \(N_L\) grows with the system size. It must not be presented as thermodynamic progress.

## 7. What changed and what did not

**candidate-T.** The remaining two-mode derivative signal has an exact integer form:

\[
\mathcal D_L
:=
|C_{L,1}|^2+|C_{L,2}|^2
=
L^4\frac{A_L^2+B_L^2}{N_L^2}.
\]

**candidate-T.** The integers have concrete meanings:

\[
N_L=\sum_\beta |\mathcal B_\beta|^2,
\]

while \(A_L+B_L\varphi\) is the normalized difference of two one-plaquette discrete-source partition sums.

**O.** No lower bound of order \(N_L/L^2\) for the defect coefficient vector has been proved.

Therefore P1 remains open. The value of the reduction is not a hidden proof of positivity. It is that the final sufficient positivity problem no longer involves a continuous source derivative, a twist free-energy factor, a trigonometric denominator, or an irrational norm. It is a concrete asymptotic integer counting imbalance.

## 8. Review boundary

A separate review should attack, in this order:

1. the sign and factor \(i\) in (14);
2. the seam transitivity factor \(L^2\);
3. the boundary convention in (18) and the factor \(5^{|E|}\) in (22);
4. the claim that (22) lies in \(\mathbb Z[\varphi]\);
5. the Galois transport from the \((1,1)\) defect to the \((2,2)\) defect;
6. the denominator identities in (36);
7. the exact cancellation in (41);
8. the dependency ceiling in (44).

A failure of any one item invalidates the candidate. A passing exact audit is evidence for the algebra only and is not an independent mathematical review.

Public Canon v92, the registry, frontier, formal probes, gates, runners and releases are unchanged.
