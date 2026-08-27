# P-J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL-1 result

Status: **PROVED AND AUDITED IN THE FROZEN L1 CLASS / PUBLIC REPLAY
PENDING / CANON UNCHANGED**

## Disposition

The result-exposed algebraic theorem package survives. The written universal
proof in PREREG.md is theorem-grade candidate-T evidence at L1; the accepted
post-pin exact audit returned 7/7 PASS, exit zero, empty stderr, and stdout
identical to EXPECTED.txt. A later sealed Canon fold may decide whether to
register J-RAPIDITY-GALOIS-EQUIVARIANT-PRIME-SHELL [T]. This probe itself
moves no public row.

Both required negative controls fired:

- at p=11, E_4 is the prime-ideal line cross-labelled by the other root 8,
  while the same-root label 4 is false;
- the unrefined scalar correction retains the nonzero tail
  (2-u-u^{-1})T/(1-T) before augmentation.

## Exact result

For a split prime p and t^2-t-1=0 modulo p,

\[
E_t=\mathbb F_p(1,t)=\mathfrak p_{1-t}/pO_F.
\]

The associated two-point object

\[
\mathscr S_p=
\{(E_t,\mathfrak p_{1-t},r_{\mathfrak p_{1-t}},2t-1)\}
\]

is equivariant under branch exchange: the prime-ideal direction, rapidity,
and finite odd coordinate all change together without selecting one branch.

The fixed-line coefficient algebra has one-dimensional odd subspace

\[
B_p^-=\mathbb F_p(2t-1),\qquad (2t-1)^2=5.
\]

This is an odd subspace, not an odd subalgebra. Wedge, tangent-multiplier,
Lefschetz, and 2A-I readings add no second independent local odd direction.

The integral two-point permutation module is a non-split extension

\[
0\longrightarrow\mathbb Z_{\rm sgn}\longrightarrow
\mathbb Ze_{\mathfrak p}\oplus\mathbb Ze_{\bar{\mathfrak p}}
\longrightarrow\mathbb Z_{\rm triv}\longrightarrow0.
\]

Its sum/difference lattice has index two, so normalized local invariant descent
requires one half. In the explicitly frozen class of two oriented resolvents,
independent relabelling and scalar augmentation uniquely force

\[
\widetilde C_p(T)=
\frac12\left((1-u_pT)^{-1}+(1-u_p^{-1}T)^{-1}\right),
\]

and

\[
(1-u_pT)(1-u_p^{-1}T)\widetilde C_p(T)
=1-\frac{u_p+u_p^{-1}}2T.
\]

No uniqueness outside this two-dimensional correction class is claimed.

Multiplying these local factors defines the squarefree group-ring lift

\[
\widetilde\mu(n)=
\frac{\mu(n)}{2^{|S(n)|}}
\sum_{\varepsilon_p=\pm1}
\prod_{p\in S(n)}u_p^{\varepsilon_p}
\]

for squarefree n, and zero otherwise. It satisfies

\[
\operatorname{aug}\widetilde\mu(n)=\mu(n),\qquad
\widetilde\mu(n)^*=\widetilde\mu(n),\qquad
\|\widetilde\mu(n)\|_1=|\mu(n)|.
\]

The factor 2^{-|S(n)|} is forced by local Euler multiplicativity, normalized
local Reynolds descent, and invariance under independent relabelling of each
split pair, namely (C_2)^{S(n)}. It is not claimed to follow from the single
global Gal(F/Q)=C_2 involution alone.

For

\[
P_N=\sum_{n\le N}\widetilde\mu(n),
\]

the two exact L1 functionals are

\[
\operatorname{aug}P_N=M(N)
\]

and

\[
\operatorname{CT}P_N=
\sum_{\substack{n\le N\\n\text{ has no split prime divisor}}}\mu(n).
\]

The second functional is called the constant term only.

## Gate readout

1. fixed-line census and cross-label: PASS for every prime p<=997;
2. odd-rank-one formulas: PASS on all 156 oriented split lines;
3. integral index-two obstruction: PASS;
4. frozen Reynolds uniqueness and local product: PASS through degree eight;
5. global lift: PASS through n=5000, with an independent convolution audit
   through n=2000;
6. augmentation and constant term: PASS at four independently accumulated
   checkpoints through N=5000;
7. scalar-correction tail breaker: FIRED-AS-EXPECTED in degrees two to eight.

These finite checks audit the universal written proofs. Their finite bounds
are not the scope of the theorem.

## Scope boundary

This result does not choose a global orientation, make J residue orders a
universal selector, define a probability measure, identify a Haar integral,
construct a Hecke character, perform automorphic induction, invoke
Selberg-Delange, estimate M(N), identify an L-function, claim square-root
cancellation, or prove or disprove RH.

In particular, the wider Hecke-mode analysis is not evidence for this result.
It belongs to a separate NON-CANONICAL synthesis Note. The Note must also keep
two distinctions explicit:

- zero mode is separated in the lattice of conductor-one Hecke infinity
  types, not topologically isolated in the full rapidity dual;
- a fixed nonzero mode has the wrong summatory scale, but this does not rule
  out a uniform growing-mode route.

## Evidence boundary

The accepted local formal leg is arm64, macOS 26.5.2, CPython 3.9.6. The
pull-request workflow reruns the unchanged pinned verifier on GitHub-hosted
x86_64 and aarch64 and requires both outputs to be byte-identical to the one
committed EXPECTED.txt. Until that workflow passes, public replay is pending.

The public Canon remains v66. No Canon, Registry, Frontier, gate, workflow, or
existing probe file is changed by this result.
