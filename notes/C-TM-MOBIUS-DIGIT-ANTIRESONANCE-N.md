# C-TM-MOBIUS-DIGIT-ANTIRESONANCE-N

**Status:** NON-CANONICAL RESEARCH NOTE. No public scientific status is created by this file.  
**Date:** 12 September 2026  
**Author:** A. M. Thorn  
**Public authority at creation:** Public Canon v84  
**Object lock:** issue #965  
**Scope:** arithmetic and analytic number theory only. No L1 to L6 physical lift.

## 0. Purpose

This note separates three mechanisms that are easy to blur together:

1. exact digital cancellation in Thue-Morse;
2. arithmetic leakage carried by ordinary digit sums;
3. spectral cancellation of the Möbius and Liouville functions.

The useful organizing principle is **alignment of a character kernel with the filtration in which the sum is taken**.

- alignment with the counting filtration can produce an exact identity;
- alignment with a congruence filtration produces a clock;
- lack of such alignment leaves a spectral problem.

The note also records an elementary characterization of the Thue-Morse bit that appears useful for TWIST-J itself:

> among all nontrivial XOR characters on finite binary words, Thue-Morse is the unique one invariant under dyadic scale shift.

That theorem is exact. Its physical relevance is not.

Local labels used below are only note labels:

```text
[T, elementary]   proved in this note
[KNOWN]           established external mathematics or already public TWIST-J mathematics
[C, historical]   previously reported finite computation, not new evidence here
[H]               proposed research direction
[F]               route or implication explicitly broken
```

None of these labels changes `canon/REGISTRY.tsv`.

---

## 1. Public lineage and what is not new

Several nearby statements are already owned by the public program and must not be recounted here as discoveries.

**[KNOWN, TWIST-J] `MOBIUS-TM-PRIME2-BRIDGE [T]`.** The public v41 theorem proves the general prime-dilation/Möbius-support equivalence and, for

\[
\tau(n):=(-1)^{s_2(n)},
\]

uses \(\tau(2n)=\tau(n)\) to obtain exact exclusion of the prime-2 direction from the Möbius primitive \(\mu * \tau\), together with odd-supported reconstruction and related Boolean, Lambert and Dirichlet identities. See issue #326.

**[KNOWN, TWIST-J] `TM-MULTIPLICATION-CARRY-DEFECT [T]`.** The public v41 theorem gives the exact multiplication-carry quantity

\[
\kappa_2(a,b)=s_2(a)s_2(b)-s_2(ab)
\]

and the resulting Thue-Morse multiplicativity defect. See issue #331.

**[KNOWN, TWIST-J] `O5-WALSH-LINK-HOMOLOGY`.** The public O5 lane already uses an exact Walsh basis to decompose an oriented split-prime threshold complex. See issue #601 and its merged successor. The present note does not claim that introducing Walsh coordinates is new to TWIST-J.

**[KNOWN, external] Möbius-Walsh correlation.** Bourgain proved uniform small-correlation bounds between the Möbius function and the full Walsh system. Therefore the generic program “study Möbius in the Walsh basis” is prior art, not a new research claim here.

The fresh delta of this note is narrower:

1. an elementary uniqueness theorem for the Thue-Morse XOR character;
2. a clean leakage classification for ordinary digit sums;
3. a filtration-alignment formulation linking identity, clocks and spectrum;
4. a falsification of the naive TM-to-RH implication;
5. a proposal to use Walsh coordinates specifically on an unresolved common-sign Möbius channel, seeking an exact transfer law rather than another correlation estimate;
6. a concrete carry-defect successor question that respects the existing `TM-MULTIPLICATION-CARRY-DEFECT [T]` ownership.

---

## 2. Thue-Morse as the unique scale-invariant XOR character

Let

\[
V:=\bigoplus_{k\ge 0}\mathbb F_2 e_k,
\]

identified with the nonnegative integers through their finite binary expansions. Addition in \(V\) is bitwise XOR.

Let

\[
\varepsilon:V\to\mathbb F_2
\]

be a group homomorphism. Every such map has a unique coordinate form

\[
\varepsilon(n)=\sum_{k\ge 0} a_k n_k\pmod 2,
\qquad a_k\in\mathbb F_2,
\]

where \(n_k\) is the \(k\)-th binary digit of \(n\).

### Theorem 2.1

**[T, elementary]** If

\[
\varepsilon(2n)=\varepsilon(n)
\qquad\text{for every }n\ge 0,
\]

then either \(\varepsilon=0\), or

\[
\boxed{\varepsilon(n)=s_2(n)\pmod 2.}
\]

Equivalently, the only dyadic-scale-invariant XOR characters are the trivial character and the Thue-Morse parity character.

### Proof

Multiplication by two shifts every binary digit one place to the left:

\[
(2n)_{k+1}=n_k,
\qquad (2n)_0=0.
\]

Thus

\[
\varepsilon(2n)=\sum_{k\ge0}a_{k+1}n_k.
\]

Equality with

\[
\varepsilon(n)=\sum_{k\ge0}a_kn_k
\]

for every finite binary word forces

\[
a_{k+1}=a_k
\qquad\text{for every }k.
\]

Hence all coefficients are equal. If they are all zero, \(\varepsilon=0\). If they are all one,

\[
\varepsilon(n)=\sum_k n_k=s_2(n)\pmod2.
\]

This is Thue-Morse parity. \(\square\)

### Corollary 2.2

**[T, elementary]** The corresponding sign character

\[
\tau(n)=(-1)^{\varepsilon(n)}
\]

is uniquely characterized among nontrivial XOR characters by

\[
\tau(2n)=\tau(n).
\]

Its odd-step law is then forced:

\[
\tau(2n+1)=-\tau(n).
\]

### TWIST-J reading

**[H]** This suggests a possible driver-selection statement:

```text
XOR additivity
+ invariance under dyadic scale shift
+ nontriviality
=> Thue-Morse.
```

The theorem does not prove that XOR additivity and scale invariance are physically mandatory. A genuine TWIST-J reduction would have to derive those premises from already public architecture, or register them openly as additional selection conditions. Until then this is a mathematical characterization, not a derivation of the driver from `J`.

---

## 3. Kernel alignment with the dyadic counting filtration

For \(k\ge1\), the complete dyadic block

\[
\{0,1,\ldots,2^k-1\}
\]

is exactly the finite vector subspace

\[
V_k:=\operatorname{span}_{\mathbb F_2}\{e_0,\ldots,e_{k-1}\}.
\]

A nontrivial character on a finite abelian group sums to zero over the whole group. Since the Thue-Morse character is nontrivial on every \(V_k\),

\[
\boxed{\sum_{n<2^k}\tau(n)=0.}
\]

Equivalently, the first coordinate subgroup already gives the coset pairing

\[
\tau(2m)+\tau(2m+1)=0.
\]

Therefore

\[
S(N):=\sum_{n<N}\tau(n)
\]

satisfies

\[
S(2N)=0,
\qquad |S(N)|\le1.
\]

**[T, elementary]** The exact cancellation occurs because the summation blocks are themselves unions of complete cosets for the additive filtration on which the character is defined. The character kernel is aligned with the counting filtration.

This is stronger and more precise than saying merely that the mechanism is “local”.

---

## 4. A nonzero Fourier direction with exact growth

Define the Thue-Morse polynomial

\[
P_k(z):=\sum_{n<2^k}\tau(n)z^n.
\]

The binary recursion gives the exact product

\[
P_k(z)=\prod_{j=0}^{k-1}(1-z^{2^j}).
\]

Let \(\omega\) be a primitive cube root of unity. For \(k=2m\), powers of two alternate modulo three, so the factors occur in pairs:

\[
(1-\omega)(1-\omega^2)=3.
\]

Hence

\[
\boxed{P_{2m}(\omega)=3^m.}
\]

**[T, elementary]** Thus along this exact frequency and block length \(4^m\), the magnitude grows like

\[
3^m=(4^m)^{\log 3/\log 4}.
\]

The uniform Fourier norm of Thue-Morse has the classical Gelfond exponent

\[
\theta_{TM}=\frac{\log3}{\log4}\approx0.79248.
\]

The point \(\alpha=1/3\) is an exact witness for this exponent. It is not asserted here to be the exact finite-\(k\) maximizer.

**[C, historical]** A previously reported grid scan over \(2\cdot10^5\) frequencies gave

```text
k                    2       4       6       8       10      12
sup_grid/3^(k/2)   1.0264  1.0392  1.0432  1.0443  1.0446  1.0445
```

with maximizing frequency near \(0.3332\), not exactly \(1/3\). This is an engineering readout only. No finite-grid supremum claim is promoted.

The appearance of the integer three in \(3^m\) is a dyadic-product fact. It is not a consequence of the TWIST-J trace \(\operatorname{Tr}(J)=3\), nor evidence of a `p=5` mechanism.

---

## 5. The universal digit-sum leakage

Let \(s_q(n)\) denote the sum of the base-\(q\) digits of \(n\).

### Theorem 5.1

**[T, elementary]** For every integer \(q\ge2\),

\[
\boxed{s_q(n)\equiv n\pmod{q-1}.}
\]

### Proof

Write

\[
n=\sum_{j\ge0}d_jq^j.
\]

Since \(q\equiv1\pmod{q-1}\),

\[
n\equiv\sum_jd_j=s_q(n)\pmod{q-1}.
\]

\(\square\)

### Leakage quotient

Fix a digit-sum phase modulo \(m\). Put

\[
d:=\gcd(m,q-1).
\]

Then

\[
s_q(n)\equiv n\pmod d.
\]

Hence every nontrivial common quotient of \(\mathbb Z/m\mathbb Z\) and \(\mathbb Z/(q-1)\mathbb Z\) is an exact periodic clock already carried by \(n\).

**[T, elementary]** The digit module \(m\) is free of this universal \((q-1)\)-leakage exactly when

\[
\boxed{\gcd(m,q-1)=1.}
\]

This says only that the universal congruence leakage is absent. It does not say that the resulting digital observable has no other arithmetic structure.

### Base five

For \(q=5\),

\[
s_5(n)\equiv n\pmod4,
\]

so the quartic phase is exactly a clock:

\[
\boxed{i^{s_5(n)}=i^n.}
\]

A base-five mod-4 digit driver is therefore not an independent antirezonant degree of freedom.

### Four-phase guard

Take \(m=4\). Then

\[
\gcd(4,q-1)=1
\]

for every even base \(q\), while for every odd base \(q\),

\[
\gcd(4,q-1)\ge2.
\]

Thus a four-phase digit-sum reading can be fully free of the universal \((q-1)\) clock only in an even base. In base five the leakage is complete.

**[H, program use]** This is a useful scope guard for any four-phase binary-hull or `s_2 mod 4` construction. It does not by itself select base two among all even bases. Base two becomes unique only after an additional minimal-radix condition or an independently derived binary carrier.

---

## 6. Congruence alignment gives clocks

The preceding theorem has the same structural form as the dyadic cancellation theorem, but with a different filtration.

The quotient

\[
n\mapsto n\pmod{q-1}
\]

is aligned with the ordinary congruence filtration. Because

\[
s_q(n)\equiv n\pmod{q-1},
\]

a digit-sum character that factors through this quotient is not producing a new oscillation. It is reproducing a periodic clock already present in the counter.

Thus:

```text
alignment with dyadic additive blocks   -> exact zero;
alignment with congruence classes       -> clock;
```

and neither case requires spectral analysis.

---

## 7. Möbius and Liouville: multiplicative character, archimedean filtration

The earlier slogan “Möbius is not a character” is false and is retired.

Write

\[
\mu(n)=1_{\mathrm{squarefree}}(n)\,\lambda(n),
\qquad
\lambda(n)=(-1)^{\Omega(n)}.
\]

The Liouville function \(\lambda\) is completely multiplicative. It is the parity character of the total prime-factor multiplicity. Möbius is this multiplicative sign restricted by the squarefree projector.

The key difference from Thue-Morse is not character versus non-character. It is the relation between the character and the summation filtration.

The initial segment

\[
\{1,2,\ldots,N\}
\]

is not a multiplicative subgroup and is not a union of complete cosets of the kernel of \(\lambda\). Nor is the squarefree restriction aligned with the archimedean size cutoff.

The Dirichlet series

\[
\sum_{n\ge1}\frac{\mu(n)}{n^s}=\frac1{\zeta(s)}
\]

then transfers the cancellation problem into analytic spectral data. Nontrivial zeros of \(\zeta\) become poles of \(1/\zeta\), and their location governs the strength of Mertens-type cancellation.

The organizing principle is therefore:

\[
\boxed{\text{alignment with counting filtration} \to \text{identity},}
\]

\[
\boxed{\text{alignment with congruence filtration} \to \text{clock},}
\]

\[
\boxed{\text{no exact alignment with the archimedean cutoff} \to \text{spectral problem}.}
\]

The last arrow is an organizing description, not a theorem that every unaligned character must produce a zeta function.

---

## 8. Digital transversality at the primes is prior art

The base-five remainder after removing the obvious last-digit or congruence component should not be treated as an open finite independence test.

**[KNOWN]** Mauduit and Rivat proved the Gelfond prime digit-sum equidistribution theorem, with the expected degenerate congruence cases separated.

**[KNOWN]** Martin, Mauduit and Rivat proved a stronger prime-number theorem for digital functions, including uniform exponential sums of the form

\[
\sum_{n\le x}\Lambda(n)e(\alpha s_q(n)+\beta n)
\]

uniformly in \(\beta\).

Consequently, for \(q=5\), the mod-5 digit component after the explicit congruence bookkeeping is asymptotically transverse to the prime residue class in the precise Fourier sense supplied by their theorem.

This transversality is imported deep analytic mathematics. It is not derived from TWIST-J carry identities.

**[C, historical]** A previous one-lane finite readout reported, for cutoffs \(10^3\) through \(10^7\), normalized quadratic discrepancy \(\chi^2/\pi(x)\)

```text
0.1789, 0.0601, 0.01318, 0.004918, 0.000631
```

and maximum relative cell deviation

```text
0.740, 0.451, 0.177, 0.105, 0.0368.
```

The five-point log-log slope was about \(-0.33\). This is recorded only as a finite convergence profile. It is not a statistical independence test and no fit quality or asymptotic exponent is claimed.

---

## 9. Correlation is not a falsifier of common mechanism

A previous exploratory claim said that if Thue-Morse and Möbius were “the same antirezonance in two disguises”, they would have to correlate.

**[F]** This criterion is invalid.

Distinct characters of the same finite abelian group can be orthogonal while sharing exactly the same character mechanism. Lack of correlation therefore does not falsify a common structural origin.

The useful distinction is the filtration alignment described above.

**[KNOWN]** Möbius orthogonality to automatic sequences is itself deep prior art. In particular, Müllner proved the Sarnak conjecture for automatic sequences. A finite value of

\[
\sum_{n\le N}\mu(n)\tau(n)
\]

is therefore only a finite witness of an asymptotic theorem, not a new structural discriminator.

**[C, historical]** The previously reported exact one-lane values at \(N=10^6\) were

\[
M(10^6)=212,
\]

\[
\max_{n\le10^6}|M(n)|=368,
\]

first attained with negative sign at \(n=926265\), and attained at

```text
926265, 926278, 926279, 926280,
```

with

\[
\sum_{n\le10^6}\mu(n)\tau(n)=172.
\]

No public evidence credit is claimed here.

---

## 10. One common axis does exist: the uniform Fourier norm

The zero-frequency comparison and the uniform-frequency comparison must be kept distinct, but they can be placed on one common uniform Fourier axis.

For an arithmetic function \(a(n)\), define

\[
\mathcal F_a(x):=\sup_{\alpha\in\mathbb R}
\left|\sum_{n\le x}a(n)e(n\alpha)\right|.
\]

### Thue-Morse

**[KNOWN]** The uniform Thue-Morse Fourier growth has exponent

\[
\theta_{TM}=\frac{\log3}{\log4}.
\]

The exact \(\alpha=1/3\) witness in section 4 already gives the matching lower exponent along \(x=4^m\).

### Möbius, unconditional

**[KNOWN]** Davenport proved that for every fixed \(A>0\), uniformly in \(\alpha\),

\[
\sum_{n\le x}\mu(n)e(n\alpha)
\ll_A \frac{x}{(\log x)^A}.
\]

This gives strong sublinear cancellation but does not place Möbius below the Thue-Morse power exponent.

### Möbius, under GRH

**[KNOWN, conditional]** Baker and Harman proved under the generalized Riemann hypothesis for Dirichlet \(L\)-functions that for every \(\varepsilon>0\),

\[
\boxed{
\sup_{\alpha\in[0,1)}
\left|\sum_{n\le x}\mu(n)e(n\alpha)\right|
\ll_\varepsilon x^{3/4+\varepsilon}.
}
\]

Since

\[
\frac34<\frac{\log3}{\log4},
\]

this yields a genuine conditional ordering on the same norm: for sufficiently small fixed \(\varepsilon\), Möbius has a better power exponent than Thue-Morse.

At frequency zero the direction reverses dramatically. Thue-Morse has bounded partial sums, while RH gives only

\[
M(x)=O_\varepsilon(x^{1/2+\varepsilon}).
\]

So the sharp formulation is not “the two are incomparable”. It is:

> their ordering depends on the norm and on hypotheses. Thue-Morse wins exactly at zero frequency; under GRH Möbius wins on the common uniform Fourier exponent; unconditionally no such power-exponent ordering follows from Davenport alone.

---

## 11. A direct falsifier for the naive TM-to-RH route

Suppose one tried to infer a small zero-frequency sum from perfect Thue-Morse cancellation.

Take the constant function

\[
f(n)=1.
\]

Then on every complete dyadic block,

\[
\sum_{n<2^k}f(n)\tau(n)=0,
\]

while

\[
\sum_{n<2^k}f(n)=2^k.
\]

Therefore:

\[
\boxed{
\text{perfect Thue-Morse antirezonance does not imply small zero-frequency sum.}
}
\]

**[F]** Any RH route that uses only orthogonality to Thue-Morse, with no additional multiplicative structure, is dead.

This falsifier is deliberately stronger than a numerical noncorrelation test.

---

## 12. Exact first Walsh transfer for Möbius

The binary split of Möbius contains one exact piece.

For every \(n\ge1\),

\[
\mu(2n)=
\begin{cases}
-\mu(n),&n\text{ odd},\\
0,&n\text{ even}.
\end{cases}
\]

Equivalently,

\[
\boxed{
\mu(2n)
=-1_{n\text{ odd}}\mu(n)
=-\frac{1-(-1)^n}{2}\mu(n).
}
\]

**[T, elementary]** The even branch is therefore an exact transfer between two Walsh modes: the constant mode and the least-significant-bit parity mode.

The unresolved arithmetic is concentrated in

\[
\mu(2n+1).
\]

That suggests a more precise research question than generic Möbius-Walsh correlation.

### Research question RH-W1

**[H]** On dyadic blocks, can the Möbius recursion be organized into an exact transfer law for **Walsh spectral energy by degree**, with a closed or controlled remainder on the odd branch?

The target is not another estimate of one Walsh coefficient. The target is an exact identity or finite recursion that describes how spectral mass moves between degrees under the binary split.

A useful result would have to do more than restate Bourgain's correlation bound.

---

## 13. The RH connection: the constant Walsh mode

On the dyadic block \(0\le n<2^k\), define the normalized Walsh coefficient

\[
\widehat\mu_k(S)
:=2^{-k}\sum_{n<2^k}
\mu(n)(-1)^{\sum_{j\in S}n_j},
\qquad S\subseteq\{0,\ldots,k-1\}.
\]

The constant mode is

\[
\widehat\mu_k(\varnothing)
=2^{-k}M(2^k-1)
\]

up to the chosen endpoint convention.

RH asks, equivalently at the power-bound level,

\[
|\widehat\mu_k(\varnothing)|
\le 2^{-k/2+o(k)}.
\]

The full-parity mode

\[
S=\{0,\ldots,k-1\}
\]

is the Möbius-Thue-Morse correlation on the same block.

These are two coordinates of one Walsh spectrum, but control of the full-parity coordinate does not control the constant coordinate. Section 11 gives the simplest abstract counterexample.

### Research question RH-W2

**[H]** Is there an exact transfer mechanism, special to Möbius multiplicativity, that forces energy away from the constant Walsh mode as \(k\) grows?

A positive answer would still not prove RH unless it quantitatively forces the square-root scale. But it would isolate the missing mechanism in a concrete finite harmonic decomposition.

---

## 14. Connection to the current common-sign Möbius problem

The current RH research line has already learned that controlling individual absolute tails is insufficient. The remaining difficulty is joint sign cancellation among Möbius contributions before squaring or taking absolute values.

**[H]** Walsh coordinates are worth testing only if they preserve that joint sign information and simplify the common channel.

The admissible next analytic step is therefore:

1. keep the existing arithmetic carrier and norm unchanged;
2. decompose only its binary dependence into Walsh modes on dyadic blocks;
3. derive identities before computing large ranges;
4. determine whether the open common-sign contribution is concentrated in, or transferred among, a small number of modes;
5. stop immediately if the transform merely rewrites the same uncancelled terms.

No new sieve should be introduced merely to manufacture a better-looking Walsh spectrum.

---

## 15. Carry defect as the exact seam between additive identity and multiplication

The public theorem `TM-MULTIPLICATION-CARRY-DEFECT [T]` already supplies the canonical seam.

For binary multiplication, the carry mass

\[
\kappa_2(a,b)=s_2(a)s_2(b)-s_2(ab)
\]

measures the failure of the raw bit-product count to survive normalization into the binary digits of \(ab\). Its parity enters the exact Thue-Morse multiplicativity law.

This makes \(\kappa_2\) a natural object for the transition between:

```text
carryless additive character identity
and
multiplicative prime arithmetic.
```

The right successor question is not whether carry exists. That is already theorem-level public mathematics.

### Research question CD-1

**[H]** Does \(\kappa_2\), restricted to genuinely multiplicative data such as prime pairs, carry nontrivial spectral structure after all obvious low-modulus digital factors are removed?

A first finite experiment would compare the carry-mass distribution on a preregistered prime-pair ensemble with an unconditional reference ensemble.

### Mandatory confounder guard

Before any such computation, stratify by the already visible low-factor data, in particular the parity and the relevant digit-parity classes. Equivalently, the experiment must freeze in advance the small factors generated by the binary counter and \(\varepsilon(n)=s_2(n)\bmod2\).

Without that stratification, a detected association can be entirely generated by the known low-factor structure and has no evidential value.

This experiment is not executed here. A real run requires a fresh named public probe, frozen ensemble, statistic, null comparison and threshold.

---

## 16. Function-field control model

There is a clean model in which the transition from identity to spectrum is already mathematically visible.

For the affine line over \(\mathbb F_q\), the zeta function is

\[
\zeta_{\mathbb A^1}(u)=\frac1{1-qu},
\]

so the polynomial Möbius generating series is

\[
\sum_{f\text{ monic}}\mu(f)u^{\deg f}=1-qu.
\]

Therefore the complete degree-\(n\) Möbius sum vanishes exactly for every \(n\ge2\).

**[KNOWN]** This is identity-level cancellation in a genus-zero setting.

For a positive-genus curve, the numerator of the zeta function introduces Frobenius eigenvalues. Weil's Riemann hypothesis places those eigenvalues on the square-root circle.

The control picture is therefore:

```text
genus zero     -> exact cancellation;
positive genus -> Frobenius spectrum at square-root scale.
```

This is a rigorous function-field model. It is not a theorem that the classical integer problem is obtained by replacing genus with an integer statistic. Any such transfer would require its own construction.

The value of the model is methodological: it shows one precise way in which an exact combinatorial cancellation can turn into square-root spectral cancellation when a new geometric degree of freedom appears.

---

## 17. What survives for TWIST-J

The strongest TWIST-J consequence currently supported by the mathematics is modest but useful.

### Driver characterization

**[T, elementary inside this note]** Once the carrier is binary XOR and dyadic scale shift is required, the only nontrivial character is Thue-Morse.

### Four-phase scope guard

**[T, elementary inside this note]** A digit-sum phase modulo four is free of the universal \((q-1)\) leakage only for even bases. In every odd base at least a twofold clock is forced; in base five the mod-four phase is entirely the counter modulo four.

### What does not follow

The note does not derive:

- the binary carrier from `J`;
- dyadic scale invariance as a physical law;
- the four-phase hull from `J`;
- a preferred radix among all even bases without an additional minimality or architecture premise;
- RH or a new Möbius bound;
- a physical meaning for carry mass.

The useful programmatic question is whether existing public TWIST-J architecture already supplies the premises of Theorem 2.1 and the four-phase guard without adding a new physical postulate.

---

## 18. Decision tree for follow-up

The note suggests two independent future lanes.

### Lane A: driver selection

```text
Question:
Does the already registered architecture force
XOR additivity + dyadic scale invariance
for the driver character?

YES  -> candidate derivation of Thue-Morse from existing architecture.
NO   -> Theorem 2.1 remains a clean characterization only.
```

This is the higher-value TWIST-J lane because it can reduce architectural choice.

### Lane B: RH Walsh transfer

```text
Question:
Does the existing common-sign Möbius channel admit an exact
Walsh-degree transfer identity that preserves the required signs?

YES  -> derive the transfer before any large computation.
NO   -> close the route as a coordinate change with no gain.
```

A finite Walsh spectrum plot is not a success criterion.

### Lane C: carry-defect spectrum

```text
Question:
After preregistered low-factor stratification, does kappa_2 on prime pairs
retain a nontrivial spectral or distributional component?

YES  -> candidate-C only until a structural theorem is found.
NO   -> record the null result and stop the carry-spectrum branch.
```

This is cheaper and more empirical than Lane B. It should not displace the exact RH work.

---

## 19. References

Primary sources are preferred.

1. H. Davenport, **On some infinite series involving arithmetical functions (II)**, *Quarterly Journal of Mathematics*, os-8 (1937), 313-320. DOI: `10.1093/qmath/os-8.1.313`.
2. C. Mauduit and J. Rivat, **Sur un problème de Gelfond: la somme des chiffres des nombres premiers**, *Annals of Mathematics* 171 (2010), 1591-1646. DOI: `10.4007/annals.2010.171.1591`.
3. B. Martin, C. Mauduit and J. Rivat, **Théorème des nombres premiers pour les fonctions digitales**, *Acta Arithmetica* 165 (2014), 11-45. DOI: `10.4064/aa165-1-2`.
4. R. C. Baker and G. Harman, **Exponential Sums Formed with the Möbius Function**, *Journal of the London Mathematical Society* (2) 43 (1991), 193-198. DOI: `10.1112/jlms/s2-43.2.193`.
5. J. Bourgain, **Möbius-Walsh correlation bounds and an estimate of Mauduit and Rivat**, *Journal d'Analyse Mathématique* 119 (2013), 147-163.
6. C. Müllner, **Automatic sequences fulfill the Sarnak conjecture**, *Duke Mathematical Journal* 166 (2017), 3219-3290.
7. S. Porritt, **A note on exponential-Möbius sums over F_q[t]**, *Finite Fields and Their Applications* 51 (2018), 298-305. The paper explicitly records the Baker-Harman GRH bound and proves a function-field analogue.
8. A. M. Odlyzko and H. J. J. te Riele, **Disproof of the Mertens conjecture**, *Journal für die reine und angewandte Mathematik* 357 (1985), 138-160.

The present note claims no priority over these results.

---

## 20. Hard boundary

This file is a research map, not a promotion package.

It creates no Canon, Registry, Frontier, dependency, gate or evidence change. It supplies no public theorem row. It performs no computation. It does not claim RH, GRH, a new Mertens estimate, zero location, analytic continuation, physical probability, decoder closure, Born reading, force, spacetime, SI bridge, `J` coupling or `p=5` selection.

Any formal follow-up must receive a fresh identifier, collision scan, preregistration, falsifier, fixed scope and accepted verifier under the then-current `POLICY.md`.
