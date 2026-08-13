# C-GOLDEN-AME-vs-GG-ARTISANAL-F8-1-N

## Status and freeze boundary

This document specifies a third, independent exact attack on the pinned
golden AME(4,6) tensor.  It compares the tensor with the two direct
Gross–Goedicke artisanal $9+27$ constructions by the complete lowest-degree
family of closed LU invariants that is not forced by perfectness.

At preregistration time:

- no source tensor has been loaded by either program in this directory;
- no target tensor has been constructed by either CLI;
- no target invariant, modular or exact, has been evaluated;
- `diagram_classifier.py` has performed only a finite combinatorial census;
- `construction_skeleton.py --self-test` has checked only frozen arithmetic
  and label conventions.

After the public commit/hash, the definitions, descriptor order, field,
locator, target order, comparison order, gates and verdict grammar below are
immutable.  A result-dependent change requires a new named preregistration.

## Question and allowed equivalence

Let $A\in(\mathbb C^6)^{\otimes4}$ be the unitary-normalized tensor parsed
from the pinned `AME46_ORIGINAL.m`.  Let
$U_{\rm sym},U_{\rm sparse}$ be the two direct $U_\lambda$ tensors defined
below.

The question is whether, for either artisanal representative, there exist
$V_0,V_1,V_2,V_3\in U(6)$, a party permutation
$\pi\in S_4$, and a phase $e^{i\theta}$, such that

$$
A=e^{i\theta}(V_0\otimes V_1\otimes V_2\otimes V_3)\,\pi(U_\lambda).
$$

The balanced invariants below are insensitive to the global phase.  The
scope includes arbitrary local unitaries, not merely monomial or Clifford
ones, and all 24 labelled party permutations.

It does **not** claim to classify all AME(4,6) tensors.  It also does not test
the Hadamard tensor $G/6$ from Gross–Goedicke Theorem 2.  The direct
$U_\lambda$ of their Eq. (4) is mandatory: Theorem 2 passes through a
Fourier-transformed function and a partial transpose, and is not silently
substituted for the named $9+27$ representative.

## Immutable source pins

`SOURCE_PINS.json` is normative.  In particular:

- golden source: 8515 bytes, SHA-256
  `55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`,
  git blob `e0d0e171d58b3360c39595d677ffc401a466112d`;
- Gross–Goedicke: arXiv `2504.15401v2`; both the 32-page PDF and source
  archive have byte/SHA-256 pins in the manifest.

Post-lock code must reject a byte mismatch before parsing.  Source failure is
`INVALID`, not evidence for or against equivalence.

## Frozen artisanal construction

All indices in this section are residues.  Put
$\omega_6=e^{2\pi i/6}$, $\omega_3=\omega_6^2$.  For
$a=(p,q)\in\mathbb Z_6^2$, use the fixed CRT coordinates

$$
p\mapsto(k,x)=(p\bmod3,p\bmod2),\qquad
q\mapsto(\ell,y)=(q\bmod3,q\bmod2).
$$

If $(x,y)\ne(1,1)$, put $m=\widehat x-\widehat y\pmod3$, where
$0,1\in\mathbb Z_2$ are lifted to $0,1\in\mathbb Z_3$.  Define

$$
\lambda(a)=\omega_3^{\phi(a)},\qquad
\phi=\begin{cases}
P(k,\ell),&(x,y)=(1,1),\\
P(k,\ell)+Q(k,\ell,m),&(x,y)\ne(1,1),
\end{cases}
$$

with the two frozen representatives

$$
\begin{array}{c|c|c}
&P&Q\\ \hline
\mathrm{sym}&k^2+\ell^2&-(k+\ell+m)^2\\
\mathrm{sparse}&k^2+\ell^2&(\ell+m)^2.
\end{array}
$$

Using `row=6*i+j`, `col=6*k+ell`, the target tensor is reconstructed
directly as

$$
(U_\lambda)_{ijkl}
=\delta_{i-j,k-\ell}\frac1{6}
\sum_{p=0}^{5}\lambda(p,i-j)\omega_6^{p(i-k)}. \tag{T}
$$

This is the convention obtained from
$|\Phi_{p,q}\rangle=(Z^pX^q\otimes1)|\Phi\rangle$ in Gross–Goedicke
Eq. (16).  Formula (T), including its exponent sign and tensor index order,
is immutable.

Gross–Goedicke Theorem 1 gives two $GL(2,\mathbb F_3)$ orbits of 24
functions each and states that an orbit is implemented by local Cliffords
and possibly a flip.  Therefore the expensive fingerprint is evaluated only
on the two representatives.  The post-lock source audit must nevertheless
enumerate and deduplicate the 24+24 function tables before invoking that
theorem.

The audit action is also frozen.  Enumerate invertible matrices
$G\in M_2(\mathbb F_3)$ in lexicographic row-major order, set
$\widehat G=4G+3I\pmod6$, and use
$\lambda_G(a)=\lambda(\widehat G^{\mathsf T}a)$.  Equivalently, it sends
$(k,\ell)^{\mathsf T}$ to $G^{\mathsf T}(k,\ell)^{\mathsf T}$ while leaving $(x,y)$
fixed.  Applying all 48 matrices and exact-deduplicating must produce 24
tables for each representative.

The $9+27$ claim is audited independently.  In the WH basis put

$$
\Pi_9=\sum_{p,q\text{ odd}}|\Phi_{p,q}\rangle\langle\Phi_{p,q}|,
\qquad \Pi_{27}=I-\Pi_9.
$$

The exact checks are
$\operatorname{rank}\Pi_9=9$,
$\operatorname{rank}\Pi_{27}=27$, and
$[U_\lambda,\Pi_9]=0$.  Each representative must also pass exact
unitarity in all three $2|2$ flattenings.

## Frozen LU invariants

For $n\ge1$ and
$\boldsymbol\sigma=(\sigma_0,\sigma_1,\sigma_2,\sigma_3)\in S_n^4$,
let $x_{q,r}\in\{0,\ldots,5\}$.  The orientation convention is that the
colour-$q$ edge maps tensor copy $r$ to conjugate copy
$\sigma_q(r)$.  Thus

$$
I_T(\boldsymbol\sigma)=
\sum_{(x_{q,r})}
\prod_{r=0}^{n-1}T_{x_{0,r}x_{1,r}x_{2,r}x_{3,r}}
\prod_{s=0}^{n-1}
\overline{T}_{
x_{0,\sigma_0^{-1}(s)}
x_{1,\sigma_1^{-1}(s)}
x_{2,\sigma_2^{-1}(s)}
x_{3,\sigma_3^{-1}(s)}}. \tag{I}
$$

Every index appears once in a $T$ and once in a conjugate $T$, so (I) is
invariant under arbitrary $U(6)^4$.  Relabelling the tensor and conjugate
copies acts by

$$
\sigma_q\longmapsto\beta\sigma_q\alpha^{-1}.
$$

Set $\sigma_0=\mathrm{id}$; the residual redundancy is simultaneous
conjugation of $(\sigma_1,\sigma_2,\sigma_3)$ by $S_n$.

By the first fundamental theorem for unitary invariants, these contractions
span all balanced polynomial $U(6)^4$-invariants of bidegree $(n,n)$.
Here $n\le4\le6$, so no small-dimension exception is being used.

### Why $n=4$ is the first non-universal closed tier

If a tensor copy and a conjugate copy share at least two differently coloured
edges, perfectness cancels that pair by the corresponding exact $2|2$
unitarity and leaves a lower-degree closed diagram.  For $n\le3$, the
$4n$ edges occupy only $n^2$ vertex pairs and $4n>n^2$; a double edge
is forced.  Consequently every closed tier $n\le3$ is universal on perfect
tensors.

At $n=4$, after $\sigma_0=\mathrm{id}$, there are
$(4!)^3=13{,}824$ normalized diagrams.  A collision-free diagram uses every
one of the 16 tensor/conjugate vertex pairs once, equivalently an ordered
one-factorization of $K_{4,4}$.  The frozen exhaustive census gives:

- 13,800 double-edge-reducible diagrams;
- 24 collision-free labelled diagrams;
- four simultaneous-copy-conjugacy classes, each of size six.

Their lexicographically least representatives are, with each row listing
$(\sigma_1,\sigma_2,\sigma_3)$:

```text
D0 = (1032, 2301, 3210)
D1 = (1032, 2310, 3201)
D2 = (1230, 2301, 3012)
D3 = (1230, 3012, 2301)
```

The canonical representative serialization has SHA-256
`df5a7d9f6d3454119cc7eaf066a42e1382232c442f3ab69e6906319bde0f6134`.
The sorted 24 labelled diagrams have SHA-256
`a730158b96fd75d15f9c124c1a3383ed94dad7a16e94ecbbc4ddcd4f21fec4da`.

This is complete for the potentially non-universal closed bidegree-(4,4)
tier after perfect-tensor cancellations.  It is not a complete LU
classification over all polynomial degrees.

## Party action and fingerprint

The frozen party convention is `new colour q = old colour rho[q]`.  After a
party permutation, left-compose every matching by the inverse of the new
colour-0 matching, then quotient by simultaneous copy conjugation.

Exhaustion of all 24 parties gives an image of order six and kernel

$$
\{(),(01)(23),(02)(13),(03)(12)\}\cong V_4.
$$

It fixes $D_0$ and realizes the full $S_3$ on
$D_1,D_2,D_3$.  This is asserted by `diagram_classifier.py`, not assumed.

Put $v_j(T)=I_T(D_j)$.  The party-quotiented fingerprint is

$$
F_8(T)=(v_0,e_1,e_2,e_3),
$$

where

$$
e_1=v_1+v_2+v_3,\quad
e_2=v_1v_2+v_1v_3+v_2v_3,\quad
e_3=v_1v_2v_3.
$$

Equivalently it is
$(v_0,\{v_1,v_2,v_3\}_{\rm multiset})$.  The exact comparison order is
`v0,e1,e2,e3`.

## Exact field and finite-field locator

Use the common field

$$
K=\mathbb Q(\xi),\qquad \xi=\zeta_{120},\qquad [K:\mathbb Q]=32,
$$

in the rational power basis $1,\xi,\ldots,\xi^{31}$, with

$$
\Phi_{120}(X)=
X^{32}+X^{28}-X^{20}-X^{16}-X^{12}+X^4+1. \tag{P}
$$

The embeddings of all constants are fixed by

$$
\zeta_{40}=\xi^3,\quad
w=\zeta_{20}=\xi^6,\quad
\omega_6=\xi^{20},\quad
\omega_3=\xi^{40},\quad
\overline\xi=\xi^{-1}.
$$

For the golden source amplitudes:

$$
c=\frac{\xi^{15}+\xi^{-15}}2,\qquad
a=\frac{c}{\xi^6+\xi^{-6}},\qquad
b=(\xi^{12}+\xi^{-12})a. \tag{A}
$$

The sole frozen locator is $p=241$.  The least positive element of order
120 in $\mathbb F_{241}$ is 3, and
$\Phi_{120}(3)=0\pmod{241}$.  The algebraic denominator in (A) reduces to
$3^6+3^{-6}=207\ne0\pmod{241}$; the rational denominators 2, 3, 5, 6 and
10 are also units.  Thus substitution $\xi\mapsto3$ defines a reduction
homomorphism

$$
R_{241}:=\mathbb Z_{(241)}
[\xi,(\xi^6+\xi^{-6})^{-1}]\longrightarrow\mathbb F_{241}. \tag{R}
$$

It is deliberately **not** described as a field homomorphism
$K\to\mathbb F_{241}$, which cannot exist across characteristics.  Every
entry and every fingerprint coordinate computed here lies in $R_{241}$.
Equality of two such elements in $K$ implies equality after (R); therefore a
nonzero residue is a rigorous, non-probabilistic exact inequality
certificate.  A zero residue does not imply equality.  Conjugation is applied before reduction, so
$\overline\xi=\xi^{-1}$ maps to $3^{-1}=161\pmod{241}$.

## Post-lock gate sequence

### G0 — source integrity

1. Verify every byte count and hash in `SOURCE_PINS.json`.
2. Parse the golden source with the already audited label/exponent grammar.
3. Assert the expected 36-by-36 shape and exact three-way two-unitarity.
4. No result is reported if any check fails.

### G1 — construction integrity

1. Construct `sym` and `sparse` from formula (T), not $G/6$.
2. Enumerate the two sets of 24 distinct $GL(2,\mathbb F_3)$ images.
3. Verify the exact autocorrelation equations of Gross–Goedicke Eq. (7).
4. Verify the three exact unitary flattenings.
5. Verify the $9+27$ projector ranks and commutators.

Any failure is `INVALID`.

### G2 — diagram integrity

Run `diagram_classifier.py` twice in fresh processes.  Require byte-identical
stdout and all frozen counts, representatives, hashes, party image and party
kernel above.  Its frozen default stdout SHA-256 is
`e448f842db9cc6fe2a62e4ea0269da801cfcfb351ba7e27b1a4b898f47b3da82`.
The classifier accepts no source or tensor path.  The arithmetic-only
`construction_skeleton.py --self-test` stdout SHA-256 is
`54d878ce4445b5860b2b6eab17ea121a49ca1a45230b18f4fbd8dc9e6ab2f496`.

### G3 — modular locator scan

Target order is `golden`, `sym`, `sparse`; descriptor order is
`D0,D1,D2,D3`.  Construct the eight factor tables $A_0,\ldots,A_3$ and
$B_0,\ldots,B_3$, with $B=\overline A$, from the edge orientation in
(I).  The fixed generic binary path is

```text
(((((A0 JOIN B3) JOIN (A3 JOIN B2)) JOIN (A2 JOIN B1))
   JOIN B0) JOIN A1)
```

Every join contracts all common wire labels.  Table keys and loops are
lexicographic; reduction modulo 241 occurs after every addition and
multiplication.  Compute the four $v_j$, then
`(v0,e1,e2,e3)`.  Select the first differing fingerprint coordinate in the
frozen comparison order separately for `sym` and `sparse`.

A sparse support-join evaluator is primary.  A second evaluator with a
different factor order or direct compatible-tuple enumeration must replay
each prospective witness.

### G4 — exact reconstruction

Every published mismatch is replayed in $K$.

For the golden tensor, each nonzero source entry is a real amplitude label
(a,b,c) times (w^r).  Enumerate compatible eight-entry support tuples and
accumulate integer counts

$$
N(n_a,n_b,n_c,E),\qquad n_a+n_b+n_c=8,\quad E\in\mathbb Z_{20},
$$

where exponents from conjugate factors enter with the opposite sign.  The
exact scalar is then evaluated as

$$
\sum N(n_a,n_b,n_c,E)a^{n_a}b^{n_b}c^{n_c}\xi^{6E}
$$

using (P) and (A).

For an artisanal entry, precompute from (T)

$$
(U_\lambda)_{ijkl}=\frac{r+s\omega_6}{6},\qquad r,s\in\mathbb Z,
$$

with

$$
\omega_6^2=\omega_6-1,\qquad
\overline{\omega_6}=1-\omega_6.
$$

Accumulate products of eight entries in this two-dimensional exact basis and
embed with $\omega_6=\xi^{20}$.  Reduce the final difference to 32 rational
power-basis coefficients.  For an `e1`, `e2` or `e3` witness, reconstruct
all of (v_1,v_2,v_3) first and only then form the symmetric polynomial.

The published certificate contains the 32 coefficients and their reduction
under (R), which must reproduce the nonzero locator difference.  If all four
locator coordinates agree for an orbit, reconstruct its complete exact
fingerprint before choosing a verdict.

### G5 — independent replay and artifacts

Run the selected exact contraction by an independent factor ordering.
Publish deterministic stdout, a canonical JSON certificate, source hashes,
program hashes and artifact SHA-256 values.  A disagreement is `INVALID`.

## Hard verdict grammar

- `EXACT_NO_SYM`: the exact fingerprints of golden and `sym` differ.
- `EXACT_NO_SPARSE`: the exact fingerprints of golden and `sparse` differ.
- `EXACT_NO_GG_ARTISANAL_9PLUS27`: both preceding orbit verdicts hold.
  This excludes arbitrary (U(6)^4), global phase and all party
  permutations, hence all 48 Theorem-1 function tables.
- `F8_MATCH_INCONCLUSIVE_SYM` or `F8_MATCH_INCONCLUSIVE_SPARSE`: the complete
  frozen fingerprint agrees exactly for that orbit.
- If either orbit is inconclusive, the verdict for their union is
  `F8_MATCH_INCONCLUSIVE_GG_ARTISANAL_9PLUS27`.
- `INVALID`: a source, construction, census, arithmetic or replay gate fails.
- `NO_VERDICT`: the frozen computation does not finish within declared
  resources.

Exact fingerprint agreement is never called `YES` or LU equivalence.  No
positive LU witness is sought in this preregistration.

## Complexity and resource declaration

The authoritative verifier is Python 3 standard-library only.  Any optional
accelerated implementation is non-authoritative and must reproduce the
standard-library certificate byte for byte.  The frozen ceiling for one full
authoritative run is 72 wall-clock hours, at most eight worker processes and
64 GiB total resident memory.  Exceeding a ceiling gives `NO_VERDICT`; it
does not authorize a changed invariant, prime or target.

- Diagram census: 13,824 normalized diagrams; negligible memory.
- Expensive targets: three tensors (golden plus two orbit representatives),
  four closed cores each.
- Pinned golden support: 112 nonzero entries.  Direct $U_\lambda$ has at
  most 216 structural-support entries.
- For a direct $U_\lambda$, the eight structural support equations have
  rank seven over both $\mathbb F_2$ and $\mathbb F_3$; hence at most
  (6^9=10{,}077{,}696) compatible wire assignments per core.
- The fixed generic binary path has maximum intermediate rank eight,
  (6^8=1{,}679{,}616) scalar entries, and approximately 122,053,392
  multiply-add operations per core as a dense fallback.
- Exact artisanal accumulation uses only a two-dimensional coefficient ring;
  exact golden accumulation uses the finite amplitude/exponent signature
  table before one final (K)-evaluation.

Cores and the two artisanal representatives may run in parallel, but the
logical ordering and stdout merge order remain frozen as above.

## Firewalls

The following are forbidden inside this lock:

- adding $n\ge5$ invariants after seeing a result;
- switching to open-leg covariants or spectra;
- substituting the Hadamard (G/6) target;
- selecting a different prime because 241 happens to collide;
- shrinking or expanding the allowed local gauge group;
- inferring LU equivalence from an invariant match;
- connecting this result to unrelated TWIST-J bridges or to all AME(4,6)
  tensors.

Any such extension requires a new public preregistration.
