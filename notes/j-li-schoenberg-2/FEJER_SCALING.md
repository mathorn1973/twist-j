# Fejér scaling for an exact Li cocycle

```text
IDENTIFIER:      J-LI-FEJER-SCALING
MATH STATUS:    T as a necessary implication inside the exact all-n frame
PUBLIC STATUS:  unregistered
REALIZATION:    O
RH:             O
DATE:           2026-07-16
```

This note sharpens the atom and finite-carrier tests.  It gives a necessary
spectral shape for any one fixed unitary cocycle that realizes the actual Li
coefficients for every \(n\).  It is not sufficient for such a realization:
many unrelated measures have the same leading Fejér growth.

## 0. Hypotheses and falsifier

Assume one Hilbert-space triple \((\mathcal H,U,v)\), with \(U\) unitary,
satisfies

\[
\lambda_n(\xi)
=
\left\|\sum_{k=0}^{n-1}U^kv\right\|^2
\qquad(n\ge1),
\]

where the left side is the standard Li sequence of the normalized Riemann
\(\xi\)-function.  Let \(\mu_v\) be the spectral measure of \(v\), let
\(\iota(z)=\overline z\), and put

\[
\sigma=\mu_v+\iota_*\mu_v.
\]

The proposed all-\(n\) realization fails if any exact identity below fails.
It also fails if its Fejér means stay bounded, grow linearly, or have a leading
coefficient different from one.  Before the exact Li moment bridge is proved,
such a failure kills only the proposed carrier, not RH.

## 1. Exact Fejér identity

Define

\[
t_m
:=
\lambda_{m+1}+\lambda_{m-1}-2\lambda_m,
\qquad
\lambda_0=0,
\qquad
\lambda_{-m}=\lambda_m.
\]

The spectral theorem and conjugation symmetry give

\[
\widehat\sigma(m)=t_m,
\qquad
\sigma(\mathbb T)=2\lambda_1.
\]

For

\[
F_{n-1}(z)
:=
\frac1n\left|\sum_{k=0}^{n-1}z^k\right|^2,
\]

one has exactly

\[
\boxed{
\frac{2\lambda_n}{n}
=
\int_{\mathbb T}F_{n-1}(z)\,d\sigma(z)
=
\sum_{|m|<n}
\left(1-\frac{|m|}{n}\right)t_m.
}
\]

There is no missing factor of two: \(\sigma\) is the symmetrization of
\(\mu_v\), while the integrand is invariant under conjugation.

## 2. Necessary logarithmic scaling

The norm identity makes every \(\lambda_n\) nonnegative.  Li's criterion
therefore gives RH inside the implication.  The imported Lagarias asymptotic
under RH is

\[
\lambda_n
=
\frac12n\log n
+\frac12\bigl(\gamma-1-\log(2\pi)\bigr)n
+O(\!\sqrt n\log n).
\]

Consequently every exact all-\(n\) realization satisfies

\[
\boxed{
\int_{\mathbb T}F_{n-1}\,d\sigma
=
\log n+\gamma-1-\log(2\pi)
+O\!\left(\frac{\log n}{\sqrt n}\right).
}
\]

This is an unconditional implication from the stated realization premise: RH
is derived inside the proof and is not assumed as an external axiom.  The
premise itself remains open.

## 3. Exact consequences

### No atom at the identity

An atom of mass \(a>0\) at \(1\) contributes \(an\) to the Fejér integral
and \(an^2/2\) to \(\lambda_n\).  Hence

\[
\boxed{\sigma(\{1\})=0,\qquad\mu_v(\{1\})=0.}
\]

This agrees with `ATOM_TEST.md`.

### Correlations are not absolutely summable

If

\[
\sum_{m\in\mathbb Z}|t_m|<\infty,
\]

then every Fejér sum is bounded by that fixed \(\ell^1\)-norm.  This
contradicts the logarithmic divergence.  Therefore

\[
\boxed{(t_m)\notin\ell^1(\mathbb Z).}
\]

### A locally bounded density is impossible

Suppose \(\sigma\) is absolutely continuous on an open arc containing
\(1\), with essentially bounded density there.  Allow an arbitrary finite
measure outside a smaller arc.  The local contribution to the Fejér integral
is bounded by the density norm because \(\int F_{n-1}=1\); away from \(1\),

\[
F_{n-1}(z)
\le
\frac4{n|1-z|^2},
\]

so the remaining contribution is \(O(1/n)\).  Thus the Fejér means would be
bounded and \(\lambda_n=O(n)\), a contradiction.

The phrase "bounded density at the point" is not sufficient: the hypothesis
must include local absolute continuity and the absence of a singular component
on an arc.

## 4. What is and is not forced near \(1\)

The theorem forces logarithmic **Fejér concentration** near the identity.  It
does not by itself force a pointwise density asymptotic.  Singular-continuous
measures, oscillatory densities, or narrow irregular spikes can have the same
averaged growth.

Under the additional density ansatz

\[
d\sigma(e^{i\theta})
=
w_\sigma(\theta)\frac{d\theta}{2\pi},
\qquad
w_\sigma(\theta)
=
a\log\frac1{|\theta|}+O(1),
\]

the Fejér scaling forces

\[
\boxed{a=1.}
\]

If the stronger regular expansion

\[
w_\sigma(\theta)
=
\log\frac1{|\theta|}+B+o(1)
\]

holds, then

\[
\int F_{n-1}(e^{i\theta})
\log\frac1{|\theta|}\frac{d\theta}{2\pi}
=
\log n+\gamma-1+o(1),
\]

and comparison with the required constant gives

\[
\boxed{B=-\log(2\pi).}
\]

For a locally symmetric representative \(\mu_v\), the leading density
coefficient is \(1/2\).  Without that symmetry, only

\[
w_{\mu_v}(\theta)+w_{\mu_v}(-\theta)
\]

has coefficient one; neither side is individually fixed.

Thus the pointwise logarithmic spike is a conditional density model, not an
unconditional consequence of Fejér scaling.

## 5. Carrier implications

1. A finite spectrum without an atom at \(1\) gives bounded cocycle norms;
   with such an atom it gives quadratic growth.  Neither matches
   \(n\log n\).
2. A carrier whose correlations are in \(\ell^1\) gives at most linear norm
   growth and is excluded.
3. A determinant or Fock carrier must create an infinite spectral accumulation
   near the identity whose Fejér averages grow logarithmically.
4. The finite \(K_2,K_3,\ldots\) gates test moment consistency and can kill a
   proposal, but no finite prefix certifies this asymptotic concentration.

## 6. Circularity guard

Defining \(\sigma_J\) from the Li moments \(t_m\), from \(\xi\), from its
zeros, or from the standard Weil/Herglotz form merely renames the target.  A
J-native construction must instead:

1. produce a positive measure by a rule stated only in terms of the declared
   J-architecture;
2. prove its normalization and Fejér scaling without inserting the desired Li
   sequence;
3. establish the exact Li moment bridge as a separate all-\(n\) theorem.

Fejér scaling alone is only a necessary shape test and is far weaker than the
moment bridge.

## 7. Status

```text
J-LI-FEJER-SCALING          T as a necessary implication in the exact all-n frame
J-LI-FEJER-LOG-DENSITY      conditional T under the stated density ansatz
J-LI-COCYCLE-REALIZATION    O
J-LI-MOMENT-BRIDGE          O
RH                          O
PUBLIC REGISTRATION         absent
```

Classical import: Jeffrey C. Lagarias, *Li Coefficients for Automorphic
L-Functions*, Annales de l'Institut Fourier 57 (2007), Theorem 1.1,
[arXiv:math/0404394](https://arxiv.org/abs/math/0404394).
