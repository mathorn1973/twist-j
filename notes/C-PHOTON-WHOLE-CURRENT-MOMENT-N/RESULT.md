# RESULT — C-PHOTON-WHOLE-CURRENT-MOMENT-N

**Verdict:** PASS at the frozen NON-CANONICAL deterministic scope.
**Ceiling:** candidate-T written theorem; candidate-C finite audit.
**Canon:** unchanged.

## Closed inside this candidate

For every charged augmented component K, with M_K its number of current edges,

\[
\boxed{
\ell_K
\le
\frac{M_0^2}{16}+\frac{M_w^2}{8}
\le
\frac{M_K^2}{8}.
}
\]

If the chosen unit-cycle decomposition has no winding cycle,

\[
\boxed{\ell_K\le M_K^2/16.}
\]

The winding term is handled collectively. Since the total homology of K is
zero, a nonempty winding block has total length at least 2L.

For the larger class of homologically trivial unit flows the constant 1/8 is
sharp: two opposite coordinate winding loops separated by L/2 have

\[
M=2L,\qquad \ell=L^2/2=M^2/8.
\]

This candidate does not claim the sharp witness is itself one ternary
augmented surface component.

## Full-current reduction

The exact signed susceptibility majorant now obeys

\[
\Xi_L
\le
\frac1{64V}
\mathbb E_{\rm aug}\sum_K M_K^4.
\]

Rooting on all 4V positive lattice edges gives the exact counting identity

\[
\sum_KM_K^4
=
\sum_e
{\bf1}_{\{e\ {\rm charged}\}}M_{K(e)}^3.
\]

With

\[
R_3(L)=
\frac1{4V}\sum_e
\mathbb E_{\rm aug}
[{\bf1}_{\{e\ {\rm charged}\}}M_{K(e)}^3],
\]

the whole current problem reduces to

\[
\boxed{\Xi_L\le R_3(L)/16.}
\]

No rotational equality is used.

The exact tail formula is

\[
R_3(L)
=
\frac14\sum_{i=0}^3\sum_{r\ge1}
(3r^2-3r+1)
P_{\rm aug}(e_i\ {\rm charged},M_{K(e_i)}\ge r).
\]

So an exponential tail, or uniformly a tail O(r^(-3-epsilon)), is sufficient
for bounded Xi.

## Why this is a real reduction

Earlier neutral-polymer attempts control the size of neutral surface
structures. That variable can grow while the current remains fixed. The new
owner is the rooted **current-edge** component size, not neutral area.

The remaining probabilistic obligation is therefore narrower than the failed
surface-tree majorants.

## Prime relation

Under the purely mathematical comparison family K_p=Q(zeta_p),

\[
D=[K_p:Q]=p-1.
\]

A one-hole current edge has p occupied plaquettes out of an edge star of size
p+1, so

\[
p+1=2(D-1)=2(p-2),
\]

equivalently

\[
\boxed{(p-2)/(p+1)=1/2}.
\]

This is exactly the equation of public P5-ROOT-SELECTION [T], hence p=5 and
D=4. It gives a combinatorial interpretation of the same equation inside the
declared comparison family. It is not a new unconditional physical selector.

## What remains open

- a uniform bound on R3(L);
- full Xi_L as an evaluated number;
- the strict positive b-25 chi margin;
- P1;
- the massless phase and physical photon.

Primitive-cycle zeta or Euler-product language remains only a possible future
organization. Neutral joining, hard-core edge capacity and nonunique cycle
decomposition prevent treating the full measure as an independent loop gas.
