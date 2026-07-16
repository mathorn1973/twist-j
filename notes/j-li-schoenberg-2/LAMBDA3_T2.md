# The \(\sigma_3\), \(\lambda_3\), and \(T_2\) incubation gate

```text
IDENTIFIER:       J-LI-SCHOENBERG-3
MATH STATUS:     exact formulas and interval lemmas are T candidates
FINITE GATE:     candidate-T-ready, two architectures
PUBLIC STATUS:   unregistered
REALIZATION:     O
RH:              O
DATE:            2026-07-16
```

This note extends the preserved \(\lambda_1,\lambda_2\) certificate by one
joint moment level.  It is still a finite calibration gate.  It supplies no
evidence for the uniform all-\(n\) positivity required by RH.

## 0. Falsifier first

This candidate fails if any displayed analytic coefficient has the wrong
sign, if either elementary remainder enclosure is invalid, or if an outward
rounded interval misses its constant.  The matrix outcome has three distinct
cases:

1. an interval that intersects zero is merely inconclusive;
2. an exactly zero principal minor disproves this candidate's strict claim
   \(T_2\succ0\), but remains compatible with the RH requirement
   \(T_2\succeq0\);
3. an exactly negative principal minor disproves positivity at this level.

Before exact identification with the standard Li form, the third outcome
kills only the proposed construction.  After that identity and its arithmetic
implementation have independently passed, an exactly negative minor would
contradict Li positivity and hence RH.

## 1. Exact third power sum

Use the convention

\[
\zeta(1+t)
=
\frac1t+\gamma-\gamma_1t+\frac{\gamma_2}{2}t^2+O(t^3).
\]

Then

\[
\log\bigl(t\zeta(1+t)\bigr)
=
\gamma t
-\left(\gamma_1+\frac{\gamma^2}{2}\right)t^2
+\left(
\frac{\gamma_2}{2}
+\gamma\gamma_1
+\frac{\gamma^3}{3}
\right)t^3
+O(t^4).
\]

The imported half-argument polygamma values are

\[
\psi(1/2)=-\gamma-2\log2,
\qquad
\psi_1(1/2)=\frac{\pi^2}{2},
\qquad
\psi_2(1/2)=-14\zeta(3).
\]

Consequently,

\[
\log\Gamma\left(\frac12+\frac t2\right)
=C
-\frac{\gamma+2\log2}{2}t
+\frac{\pi^2}{16}t^2
-\frac{7\zeta(3)}{24}t^3
+O(t^4).
\]

For

\[
\sigma_k:=\sum_\rho\rho^{-k},
\]

where \(\sigma_1\) uses the standard symmetric interpretation and
\(k\ge2\) is absolutely convergent, the Hadamard expansion at \(s=1\) is

\[
\log\xi(1+t)
=
\log\xi(1)
+\sum_{k\ge1}\frac{(-1)^{k+1}}{k}\sigma_k t^k.
\]

Combining the preceding expansions gives

\[
\boxed{
\sigma_1
=1+\frac\gamma2-\frac12\log(4\pi),
}
\]

\[
\boxed{
\sigma_2
=1+\gamma^2+2\gamma_1-\frac{\pi^2}{8},
}
\]

and

\[
\boxed{
\sigma_3
=1+\gamma^3+3\gamma\gamma_1
+\frac32\gamma_2-\frac78\zeta(3).
}
\]

The Li binomial identity gives

\[
\boxed{\lambda_3=3\sigma_1-3\sigma_2+\sigma_3.}
\]

Equivalently,

\[
\begin{aligned}
\lambda_3={}&1+\frac32\gamma-3\gamma^2+\gamma^3
-6\gamma_1+3\gamma\gamma_1+\frac32\gamma_2\\
&+\frac{3\pi^2}{8}-\frac78\zeta(3)
-\frac32\log(4\pi).
\end{aligned}
\]

The verifier checks this coefficient vector exactly over
\(\mathbb Q\) before evaluating any interval.

## 2. Elementary enclosure of \(\gamma_2\)

Put

\[
f(x)=\frac{\log^2x}{x},
\qquad
A_N=\sum_{k=1}^{N}\frac{\log^2k}{k}-\frac{\log^3N}{3}.
\]

The standard defining limit is \(A_N\to\gamma_2\).  For \(N\ge32\), the
verifier proves \(\log N>3\).  On \([N,\infty)\),

\[
f'(x)=\frac{2\log x-\log^2x}{x^2}<0,
\]

and

\[
f''(x)=\frac{2(\log^2x-3\log x+1)}{x^3}>0.
\]

For the trapezoid error

\[
E_k
:=
\frac{f(k-1)+f(k)}2-
\int_{k-1}^{k}f(x)\,dx,
\]

convexity gives \(E_k\ge0\).  The Peano kernel has maximum \(1/8\), so

\[
\sum_{k>N}E_k
\le
\frac18\int_N^\infty f''(x)\,dx
=-\frac18f'(N).
\]

Telescoping yields

\[
A_N-\gamma_2
=
\frac{f(N)}2-\sum_{k>N}E_k.
\]

Therefore the exact enclosure used by the code is

\[
\boxed{
A_N-\frac{\log^2N}{2N}
\le\gamma_2\le
A_N-\frac{\log^2N}{2N}
+\frac{\log^2N-2\log N}{8N^2}.
}
\]

## 3. Elementary enclosure of \(\zeta(3)\)

For

\[
S_N=\sum_{k=1}^{N}\frac1{k^3},
\]

monotone integral comparison gives

\[
\boxed{
S_N+\frac1{2(N+1)^2}
\le\zeta(3)\le
S_N+\frac1{2N^2}.
}
\]

Thus neither \(\gamma_2\) nor \(\zeta(3)\) enters as an imported decimal.

## 4. Toeplitz gate without numerical eigenvalues

The first three second differences are most stably assembled directly from
the power sums:

\[
c_0=2\sigma_1,
\qquad
c_1=-\sigma_2,
\qquad
c_2=\sigma_3-\sigma_2.
\]

Hence

\[
T_2=
\begin{pmatrix}
c_0&c_1&c_2\\
c_1&c_0&c_1\\
c_2&c_1&c_0
\end{pmatrix}.
\]

The antisymmetric eigenvalue is

\[
A:=c_0-c_2=2\sigma_1+\sigma_2-\sigma_3.
\]

The remaining centrosymmetric block has determinant \(2Q\), where

\[
\boxed{
Q
:=
\sigma_1(2\sigma_1+\sigma_3-\sigma_2)-\sigma_2^2.
}
\]

Therefore

\[
\boxed{
T_2\succ0
\iff
c_0>0,
\quad A>0,
\quad Q>0.
}
\]

The determinant identities are

\[
\det T_2=2AQ.
\]

For the lower triangular matrix \(L_3\) of ones,

\[
K_3=\frac12L_3T_2L_3^*,
\]

so

\[
\boxed{\det K_3=\frac{AQ}{4}.}
\]

Explicitly,

\[
K_3=
\begin{pmatrix}
\lambda_1 & \lambda_2/2 & (\lambda_1+\lambda_3-\lambda_2)/2\\
\lambda_2/2 & \lambda_2 & (\lambda_2+\lambda_3-\lambda_1)/2\\
(\lambda_1+\lambda_3-\lambda_2)/2 &
(\lambda_2+\lambda_3-\lambda_1)/2 &
\lambda_3
\end{pmatrix}.
\]

## 5. First pinned incubation run

The verifier source was hashed before its first execution.

```text
source
  sha256  49cdaa5769104fda39a18d5a3e75dd4f2da6526e4a2e93201f89345058ebad2a
  bytes   10833
  lines   350

stdout / LAMBDA3_T2_EXPECTED.txt
  sha256  678bd1b4e88b12f074c5c46ed06c69f98984570cc3c312a64921a9ac4b0ef60a
  bytes   1542
  lines   28

environment
  Linux 6.12.47 x86_64
  Python 3.12.13

result
  11 PASS, 0 FAIL, exit 0
  rerun stdout byte-identical
```

The outward-rounded intervals at scale \(10^{24}\), with \(N=100000\), are

\[
\gamma_2\in
[-0.009690364105552333923998,
 -0.009690362736532310677668],
\]

\[
\zeta(3)\in
[1.202056903159593785362182,
 1.202056903159594785447129],
\]

\[
\sigma_3\in
[-0.000111159769609517915323,
 -0.000111157351768888104856],
\]

\[
\boxed{
\lambda_3\in
[0.207638918333718933341285,
 0.207638922051014328719963].
}
\]

The decisive strict intervals are

\[
A\in
[0.000148257795037333917144,
 0.000148260671029302303499],
\]

\[
Q\in
[0.000000001883563636456191,
 0.000000001989968490233267],
\]

\[
\det T_2\in
[0.000000000000558505983106,
 0.000000000000590068127380],
\]

and

\[
\boxed{
\det K_3\in
[0.000000000000069813247888,
 0.000000000000073758515923].
}
\]

Thus this one-architecture incubation run certifies

\[
\boxed{T_2\succ0\iff K_3\succ0}
\]

for the enclosed standard constants.

## 6. Second-architecture reproduction

The immutable source and expected output were subsequently executed on
Ubuntu 24.04.4 LTS AArch64 with Python 3.12.3.  The run returned exit code
zero, empty stderr, and the same 1542 stdout bytes with SHA-256
`678bd1b4e88b12f074c5c46ed06c69f98984570cc3c312a64921a9ac4b0ef60a`.
The neutral record is `LAMBDA3_T2_AARCH64_RUN.md`.

The preserved expected output still describes its historical first run as
`single architecture`; changing that line would invalidate the pin.  The
later record, rather than rewritten stdout, closes the second-architecture
audit gate.

## 7. Boundary

```text
J-LI-SCHOENBERG-3           candidate-T-ready; two architectures;
                            public unregistered
J-LI-COCYCLE-NORMAL-FORM    T as an equivalence
J-LI-COCYCLE-REALIZATION    O
RH                          O
```

The two-architecture incubation requirement is now met.  Public status would
still require a fresh preregistered probe and authoritative ledger
registration.
