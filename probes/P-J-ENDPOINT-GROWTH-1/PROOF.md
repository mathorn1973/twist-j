# Exact growth of the chosen J-carrier endpoint set

**Probe:** P-J-ENDPOINT-GROWTH-1  
**Status:** candidate-T proof; public probe, not a Canon fold  
**Author:** A. M. Thorn  
**Date:** 29 September 2026  
**Layer:** L1, exact algebraic carrier and its mathematical embeddings

## Statement

Let \(\zeta=e^{2\pi i/5}\), \(O=\mathbb Z[\zeta]\),
\(J=1+\zeta^2\) and \(\varphi=(1+\sqrt5)/2\). Fix

\[
D=\{u+v\zeta:u,v\in\{-2,-1,0,1,2\}\},\qquad
A_n=\left\{\sum_{k=0}^{n-1}J^k d_k:d_k\in D\right\},\qquad A_0=\{0\}.
\]

These are exactly the endpoints after \(n\) steps of
\(\alpha_{t+1}=J\alpha_t+d_t\), starting at zero. Reversing the order of the
independent digit choices identifies the two expressions for the endpoint.
All \(25^n\) input words are admitted, and equality of endpoints is equality
in \(O\).

**Theorem [candidate-T].** For every integer \(n\ge0\),

\[
\boxed{\varphi^{2n}\le |A_n|\le C\varphi^{2n},
\qquad C=93890+41760\sqrt5.}
\]

Consequently,

\[
\boxed{\lim_{n\to\infty}\frac{\log|A_n|}{n}=2\log\varphi.}
\]

The lower bound is new to this follow-up. The upper bound is the predecessor's
Theorem C, restated with its proof below to make the mathematical argument
self-contained. No computation is needed for either all-\(n\) bound.

## 1. The expanding embedding

Use the field embedding \(\sigma(\zeta)=\eta=\zeta^2\), and put
\(\beta=\sigma(J)=1+\eta^2\). In this complex plane \(\varphi\) denotes the
positive real number \((1+\sqrt5)/2\), not \(\sigma(\varphi)\).

The fifth-root relation gives
\(\eta+\overline\eta=-\varphi\), hence

\[
\eta^2+\varphi\eta+1=0,\qquad
\beta=-\varphi\eta,\qquad |\beta|=\varphi.
\]

For completeness, if \(t=\zeta+\zeta^{-1}\), dividing the fifth-root
relation by \(\zeta^2\) gives \(t^2+t-1=0\). Since \(t>0\),
\(t=\varphi-1\). Thus
\(\eta+\eta^{-1}=t^2-2=-\varphi\), proving the stated identity.

Since \(\eta\) is nonreal, \((1,\eta)\) is a real basis of \(\mathbb C\).
For real \(a,b\),

\[
\beta(a+b\eta)=\varphi b+(-\varphi a+\varphi^2b)\eta.
\]

The coordinate matrix and determinant are therefore

\[
B=\begin{pmatrix}0&\varphi\\-\varphi&\varphi^2\end{pmatrix},
\qquad \det B=\varphi^2.
\]

## 2. A finite covering certificate

Let

\[
P=\{a+b\eta:|a|,|b|\le\tfrac12\},\qquad D'=\sigma(D).
\]

It is essential that the following equality is an equality of actual sets,
not merely of their convex hulls:

\[
\boxed{D'+P=\{a+b\eta:|a|,|b|\le\tfrac52\}=5P.}
\]

Indeed, the five intervals \(u+[-1/2,1/2]\), for \(u=-2,-1,0,1,2\),
cover \([-5/2,5/2]\) with only endpoint overlaps, independently in the two
real coordinates.

For a point of \(P\), multiplication by \(\beta\) produces coordinates
bounded by

\[
\frac\varphi2,\qquad
\frac{\varphi+\varphi^2}{2}.
\]

Both are strictly smaller than \(5/2\):
\(\varphi<5\) and
\(\varphi+\varphi^2=2+\sqrt5<5\).
Therefore

\[
\boxed{\beta P\subseteq D'+P.}
\]

This covering, rather than a lattice-density hypothesis, is the missing
ingredient in the lower bound.

## 3. Iterate the covering and compare areas

Write \(S_n=\sigma(A_n)\). Then \(S_0=\{0\}\) and
\(S_{n+1}=\beta S_n+D'\). The previous inclusion gives, by induction,

\[
\beta^nP\subseteq S_n+P
=\bigcup_{s\in S_n}(s+P).
\]

The base case is equality. If the assertion holds at \(n\), multiplication
by \(\beta\) and the one-step covering give
\(\beta^{n+1}P\subseteq\beta S_n+\beta P
\subseteq\beta S_n+D'+P=S_{n+1}+P\).

The planar area of \(P\) is \(|\operatorname{Im}\eta|>0\).
Multiplication by \(\beta^n\) multiplies area by
\(|\beta|^{2n}=\varphi^{2n}\). Finite subadditivity of area therefore gives

\[
\varphi^{2n}\operatorname{area}(P)
\le\operatorname{area}(S_n+P)
\le |S_n|\operatorname{area}(P).
\]

A field embedding is injective, so \(|S_n|=|A_n|\). Cancelling the positive
area proves

\[
\boxed{|A_n|\ge\varphi^{2n}\quad(n\ge0).}
\]

Overlap among translated parallelograms does not harm the argument: the
required inequality is subadditivity, not disjointness. The rank-four
module \(\sigma(O)\) need not be a discrete planar lattice. Only the finite
set \(S_n\), injectivity and the displayed covering are used.

## 4. The upper bound, recalled with proof

Let \(\sigma_1(\zeta)=\zeta\) and \(\sigma_2=\sigma\). Their sizes are
\(|\sigma_1(J)|=\varphi^{-1}\) and \(|\sigma_2(J)|=\varphi\).
The first follows from \(J\varphi=\zeta\), and the second was proved above.
Every digit satisfies \(|\sigma_i(d)|\le4\). Consequently every endpoint
satisfies

\[
|\sigma_1(\alpha)|\le4\varphi^2=:R,
\qquad |\sigma_2(\alpha)|\le4\varphi(\varphi^n-1)=:T_n.
\]

For distinct algebraic integers their difference \(\gamma\ne0\) has positive
integral norm
\(N(\gamma)=|\sigma_1\gamma|^2|\sigma_2\gamma|^2\ge1\).
Thus \(|\sigma_1\gamma|^2+|\sigma_2\gamma|^2\ge2\). In
\(\mathbb C^2\simeq\mathbb R^4\), balls of radius \(1/2\) about distinct
embedded endpoints are disjoint. They lie in the product of discs with
radii \(R+1/2\) and \(T_n+1/2\).

A radius-\(1/2\) four-ball has volume \(\pi^2/32\). Comparing volumes gives

\[
|A_n|\le32(R+1/2)^2(T_n+1/2)^2
\le32(4\varphi^2+1/2)^2(4\varphi+1/2)^2\varphi^{2n}.
\]

The constant equals \(93890+41760\sqrt5\). This also holds at \(n=0\).
Together with the lower bound it proves the theorem. For \(n\ge1\),

\[
2\log\varphi\le\frac{\log|A_n|}{n}
\le2\log\varphi+\frac{\log C}{n},
\]

which proves the limit directly. Any other fixed initial carrier adds the
common translate \(J^n\alpha_0\), leaving the cardinality unchanged.

## 5. What is, and is not, decided

**[candidate-T]** The exact lower-bound question
`O-J-ENDPOINT-GROWTH-LOWER-BOUND` in the predecessor note has a positive
mathematical answer at its stated full-alphabet scope, with \(c=1,n_0=0\).
That identifier is not a normative Frontier row. Its public text and status
have not been changed by this public proof candidate.

The argument proves exponential growth of the number of attainable exact
endpoints. The exponent equals the already registered toral value
\(h=2\log\varphi\) because the same expanding complex plane multiplies
area by \(\varphi^2\) per step. The finite covering shows that the chosen
digit alphabet supplies enough translations to attain that rate.

It does not prove that every lattice point in a four-dimensional strip is
reachable, that endpoints have a uniform probability distribution, or that
their Shannon entropy has rate \(h\). It does not prove that a port of the
native update admits all words in \(D^n\). In particular, a fixed
deterministic input word has one endpoint at each time even though the
controlled family has exponentially many endpoints.

If an independent uniform 25-symbol source is additionally chosen, then the
existing information inequality remains
\(H(\alpha_n)\le\log|A_n|\) and
\(H(S^n\mid\alpha_n)\ge n(\log25-2\log\varphi)-\log C\).
The new cardinality lower bound alone does not turn the first inequality
into equality. Physical occurrence, apparatus, preparation, memory, reset
and any L1-to-L6 interpretation remain separate questions.

## 6. Public basis and review boundary

The full-alphabet construction is the [predecessor note at the fixed public commit](https://github.com/mathorn1973/twist-j/blob/c1cfe0751c65ce9ffb680aa7decd99d83600409f/notes/C-J-SOURCE-PHASE-READOUT-MEMORY-N/README.md).
Its PR #1277 merged as c1cfe0751c65ce9ffb680aa7decd99d83600409f.
Both all-n bounds are proved in this document, so the theorem does not rely
on an unpromoted candidate as scientific authority.

Public Canon v92 is the basis. The target and the local finite counts were
exposed during incubation; this public probe is confirmatory and proof-first,
not a blind discovery or a priority claim. The public preregistration and
accepted verifier are frozen before formal execution under this identifier.
The repository run record and required architecture jobs govern the finite
replay. The theorem's universal quantifier rests on the written proof.

No native source, probability law, physical entropy or cross-layer lift is
adopted. This probe does not modify any Canon, Registry, Frontier or GATES row.
