# Atom test for a Li cocycle carrier

```text
IDENTIFIER:      J-LI-ATOM-TEST
MATH STATUS:    T as an equivalence inside the positive-definite cocycle frame
PUBLIC STATUS:  unregistered
REALIZATION:    O
RH:             O
DATE:           2026-07-16
```

This note fixes the measure normalization and isolates a cheap necessary test
for every proposed all-\(n\) Li cocycle.  It neither constructs the measure nor
proves its positivity.  Those obligations remain equivalent to the open RH
gate described in `README.md`.

## 0. Scope and falsifier

Assume one fixed Hilbert-space triple \((\mathcal H,U,v)\), with \(U\)
unitary, satisfies

\[
\lambda_n
=
\left\|\sum_{k=0}^{n-1}U^k v\right\|^2
\qquad(n\ge1).
\]

Equivalently, assume the full two-sided second-difference sequence

\[
t_n
:=
\lambda_{n+1}+\lambda_{n-1}-2\lambda_n,
\qquad
\lambda_0=0,
\qquad
\lambda_{-n}=\lambda_n,
\]

is positive definite and is represented by this same triple for every
integer \(n\).  A finite fit at any cutoff does not meet this hypothesis.

The proposed realization fails immediately if its spectral measure has an
atom at \(1\), or if its Li increments do not satisfy the limits below.  A
failure before the exact identification with the Li sequence kills the
construction, not RH.

## 1. Two measures, not one

Let \(\mu_v\) be the spectral measure of \(v\):

\[
r_n
:=
\langle v,U^n v\rangle
=
\int_{\mathbb T}z^n\,d\mu_v(z).
\]

The cocycle second difference is

\[
t_n=2\operatorname{Re}r_n.
\]

Let \(\iota(z)=\overline z\), and define the canonical real-even measure

\[
\boxed{\sigma:=\mu_v+\iota_*\mu_v.}
\]

Then

\[
\widehat\sigma(n)=t_n.
\]

The normalization is therefore

\[
\boxed{
\mu_v(\mathbb T)=\|v\|^2=\lambda_1,
\qquad
\sigma(\mathbb T)=t_0=2\lambda_1.
}
\]

These measures must not be identified.  Since \(1\) is fixed by \(\iota\),

\[
\boxed{\sigma(\{1\})=2\mu_v(\{1\}).}
\]

## 2. Exact telescoping identity

For every \(N\ge1\),

\[
\sum_{m=1}^{N}t_m
=
(\lambda_{N+1}-\lambda_N)-\lambda_1.
\]

Since \(t_0=2\lambda_1\), this gives

\[
\boxed{
t_0+2\sum_{m=1}^{N}t_m
=
2(\lambda_{N+1}-\lambda_N).
}
\]

No asymptotic input is used here.

## 3. Dirichlet/Følner atom formula

The normalized symmetric Dirichlet averages obey

\[
\frac1{2N+1}
\sum_{m=-N}^{N}\widehat\sigma(m)
\longrightarrow
\sigma(\{1\}).
\]

Indeed, the normalized kernel has absolute value at most \(1\), equals \(1\)
at \(z=1\), and converges pointwise to \(0\) at every other point of the unit
circle.  Dominated convergence applies because \(\sigma\) is finite.

Combining this with the telescoping identity gives

\[
\boxed{
\sigma(\{1\})
=
\lim_{N\to\infty}
\frac{2(\lambda_{N+1}-\lambda_N)}{2N+1}.
}
\]

For the unsymmetrized spectral measure the corresponding identity is

\[
\boxed{
\mu_v(\{1\})
=
\lim_{N\to\infty}
\frac{\lambda_{N+1}-\lambda_N}{2N+1}.
}
\]

This is an elementary Dirichlet/Følner average.  Calling it Wiener's theorem
would be misleading: the standard Wiener lemma averages squared Fourier
coefficients.

## 4. Fejér form and the exact equivalence

The norm identity is the Fejér integral

\[
\lambda_n
=
\int_{\mathbb T}
\left|\sum_{k=0}^{n-1}z^k\right|^2d\mu_v(z).
\]

After division by \(n^2\), the integrand is bounded by \(1\) and converges
pointwise to \(\mathbf1_{\{1\}}\).  Hence

\[
\boxed{
\mu_v(\{1\})
=
\lim_{n\to\infty}\frac{\lambda_n}{n^2},
\qquad
\sigma(\{1\})
=
2\lim_{n\to\infty}\frac{\lambda_n}{n^2}.
}
\]

Within the full positive-definite cocycle framework, the atom test is exactly

\[
\boxed{
\mu_v(\{1\})=0
\iff
\sigma(\{1\})=0
\iff
\lambda_{N+1}-\lambda_N=o(N)
\iff
\lambda_n=o(n^2).
}
\]

For the actual Li sequence, any norm realization first implies RH by Li's
criterion.  Lagarias's RH asymptotic then supplies \(\lambda_n=o(n^2)\), so
every exact realization must pass this atom test.

## 5. What the atom test does not prove

The standard RH estimate

\[
\lambda_n
=
\frac12n\log n
+
\frac12\bigl(\gamma-1-\log(2\pi)\bigr)n
+O(\sqrt n\log n)
\]

cannot simply be differenced to conclude

\[
\lambda_{n+1}-\lambda_n\sim\frac12\log n.
\]

Its error term does not control first differences at that scale.  The
rigorous consequence needed here is only \(o(n)\), obtained from the atom
formula (or from positivity plus the spectral representation), not the
stronger displayed asymptotic.  Bounded increments are compatible with a
non-atomic measure; they are not killed by the atom test alone.

The sharper Fejér target for the actual Li sequence is still

\[
\frac{\lambda_n}{n}
=
\frac12\log n
+
\frac12\bigl(\gamma-1-\log(2\pi)\bigr)
+O\!\left(\frac{\log n}{\sqrt n}\right),
\]

but that is a global all-\(n\) target, not an increment theorem.

## 6. Status

```text
J-LI-ATOM-TEST             T as an equivalence inside the PD/cocycle frame
J-LI-CYCLIC-CARRIER-DIMENSION
                           mathematical T candidate; public unregistered
J-LI-COCYCLE-REALIZATION   O
RH                         O
```

Classical import: Jeffrey C. Lagarias, *Li Coefficients for Automorphic
L-Functions*, Annales de l'Institut Fourier 57 (2007), Theorem 1.1,
[arXiv:math/0404394](https://arxiv.org/abs/math/0404394).
