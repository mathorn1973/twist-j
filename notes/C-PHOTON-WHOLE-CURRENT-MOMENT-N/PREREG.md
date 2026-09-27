# PREREG - C-PHOTON-WHOLE-CURRENT-MOMENT-N

**Status:** PUBLIC, NON-CANONICAL incubation. No Canon authority.
**Owner:** A. M. Thorn / photon-whole-current-moment-20260927
**Date:** 2026-09-27
**Issue:** #1198
**Action layer:** L6 finite-measure / exact combinatorial current mathematics.
**Authority:** Public Canon v92. Normative files remain unchanged.

## Inputs, at their own stated status only

1. \`notes/C-PHOTON-BCHI-DIRECT-BOUND-N/SIGNED-SLICES.md\`:
   \[
   \ell_K=\min_{h\in\mathbb Z}\sum_r|H_K(r)-h|,
   \qquad
   \Xi_L=\frac1V\mathbb E_{\rm aug}\sum_K \ell_K^2.
   \]

2. \`notes/C-PHOTON-BCHI-DIRECT-BOUND-N/CONNECTED-CURRENT.md\`:
   each augmented component has integer conserved current
   \[
   J_K=\partial\eta_K/5.
   \]

3. \`notes/C-CURRENT-PRIME-GATE-N/PROOF.md\`:
   every finite \(p=5,D=4\) current is unit-capacity and decomposes into
   edge-disjoint oriented simple cycles; every augmented component has zero
   total homology.

4. \`notes/C-PHOTON-CONTACT-TURN-SKELETON-N/PROOF.md\`:
   for a zero-winding simple unit cycle of length \(m\),
   \[
   \ell(\gamma)\le m^2/16.
   \]

No source is promoted by reuse.

## Frozen notation

Let \(M_K\) be the number of nonzero current edges of \(J_K\).

Choose any edge-disjoint simple-cycle decomposition of \(J_K\). Let:

- \(M_0\): total length of the zero-winding cycles;
- \(M_w\): total length of the nonzero-winding cycles;

so \(M_K=M_0+M_w\).

For a projected zero-sum slice source \(B\), let \(\ell(B)\) be the minimum
L1 norm of an integer cyclic primitive, exactly as in SIGNED-SLICES.

## Frozen theorem package

### G1. Subadditivity

For zero-sum slice sources \(B_1,B_2\),

\[
\ell(B_1+B_2)\le \ell(B_1)+\ell(B_2).
\]

### G2. Zero-winding block

If the zero-winding cycles have lengths \(m_i\), then

\[
\ell_0\le\sum_i \frac{m_i^2}{16}
\le \frac{M_0^2}{16}.
\]

### G3. Universal cyclic transport bound

For any integer zero-sum source \(B\) on a cyclic coordinate of length \(L\),

\[
\ell(B)\le \frac{L}{4}\|B\|_1.
\]

The proof must be constructive: pair positive and negative unit masses and
route every pair along a shortest arc.

### G4. Winding block

For the winding block,

\[
\|B_w\|_1\le M_w.
\]

Because the total winding of the full augmented component is zero and every
cycle in the winding block has nonzero integer winding vector, either
\(M_w=0\) or

\[
M_w\ge2L.
\]

Hence

\[
\ell_w\le \frac{L M_w}{4}\le \frac{M_w^2}{8}.
\]

### G5. Whole-component bound

By G1 through G4,

\[
\boxed{
\ell_K
\le
\frac{M_0^2}{16}+\frac{M_w^2}{8}
\le
\frac{M_K^2}{8}.
}
\]

If \(M_w=0\),

\[
\boxed{\ell_K\le M_K^2/16.}
\]

### G6. Sharpness in the larger homologically-trivial unit-flow class

For even \(L\), take one \(+e_0\) coordinate loop at \(x_1=0\) and one
\(-e_0\) coordinate loop at \(x_1=L/2\). Then

\[
M=2L,\qquad
B=L\delta_0-L\delta_{L/2},
\qquad
\ell=L^2/2=M^2/8.
\]

This proves sharpness of \(1/8\) for homologically trivial unit flows.
It does **not** assert that this witness is one admissible ternary augmented
surface component.

### G7. Rooted third-moment reduction

From \(\Xi_L\),

\[
\Xi_L
\le
\frac1{64V}\mathbb E_{\rm aug}\sum_K M_K^4.
\]

Let \(E_L^+\) be the \(4V\) canonical positive lattice edges. Then exactly

\[
\sum_K M_K^4
=
\sum_{e\in E_L^+}
{\bf1}_{\{e\ {\rm charged}\}}M_{K(e)}^3.
\]

Define

\[
R_3(L):=
\frac1{4V}
\sum_{e\in E_L^+}
\mathbb E_{\rm aug}
\left[
{\bf1}_{\{e\ {\rm charged}\}}M_{K(e)}^3
\right].
\]

Then

\[
\boxed{\Xi_L\le R_3(L)/16.}
\]

No rotational equality is assumed.

### G8. Exact tail identity

For integer \(M\ge1\),

\[
M^3
=
\sum_{r=1}^M(3r^2-3r+1).
\]

Therefore

\[
R_3(L)
=
\frac14\sum_{i=0}^3
\sum_{r\ge1}
(3r^2-3r+1)
P_{\rm aug}
(e_i\ {\rm charged},\,M_{K(e_i)}\ge r),
\]

where \(e_i\) is one fixed positive edge of orientation \(i\).

Thus a uniform tail strong enough to make the weighted series finite gives a
uniform \(\Xi_L\) bound.

### G9. Prime/cycle boundary

The result from #1196 that \(p=5\) makes the current unit-capacity is an input
to the decomposition only. No ordinary-prime Euler product is allowed.

A primitive-cycle zeta interpretation requires a separately proved
multiplicative activity or determinant law. The present full augmented measure
contains at least three obstructions:

1. neutral surfaces can connect several current cycles into one component;
2. cycle decompositions can be nonunique at higher-valence current vertices;
3. unit edge capacity gives hard-core overlap constraints.

### G10. Comparison-family corollary

For the purely mathematical family \(K_p=\mathbb Q(\zeta_p)\) with odd prime
\(p\), set \(D=[K_p:\mathbb Q]=p-1\). If one also imposes the one-hole
current-star relation

\[
p=2D-3,
\]

then

\[
p=5,\qquad D=4.
\]

This is a comparison-family identity only. It does not identify physical
dimension with cyclotomic degree in a variable-\(p\) theory and does not
strengthen public P5-ROOT-SELECTION [T].

## Audit

After this preregistration is committed and read back, a small exact verifier
may audit:

- G3 on exhaustive small integer zero-sum cyclic sources;
- G6 for even \(L\) in a frozen finite range;
- G8 for integers in a frozen finite range;
- G10 by exact arithmetic.

Finite audits are at most candidate-C. Written proofs are candidate-T pending
separate review.

## Falsifiers

Any exact counterexample to G1 through G8 or G10 fires the corresponding
candidate. Failure to prove a uniform probabilistic bound on \(R_3(L)\) is
only a STOP for the next photon step, not a falsifier of this reduction.

## Repository boundary

Only \`notes/C-PHOTON-WHOLE-CURRENT-MOMENT-N/\` may be added.

No Canon, Registry, Frontier, gate, formal probe, tool, workflow, release or
existing note may be changed.
