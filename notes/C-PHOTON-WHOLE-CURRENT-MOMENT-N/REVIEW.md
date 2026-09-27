# REVIEW - C-PHOTON-WHOLE-CURRENT-MOMENT-N

**Review type:** proof-aware same-session mathematical review.
**Status:** NON-CANONICAL. Not independent-agent confirmation.
**Date:** 2026-09-27.

## Verdict

The deterministic theorem package survives review at exactly its declared scope.

### 1. Subadditivity

Correct. The sum of two integer cyclic primitives is a primitive of the summed source, and the sum of two minimizing integer shifts is admissible. Triangle inequality gives the result.

### 2. Zero-winding block

Correct conditional on the already written single-cycle lemma. The deterministic inequality
\[
\ell(\gamma)\le m^2/16
\]
in the quarter-turn package does not itself require the quarter-turn restriction. The turn restriction enters only the probability summation.

### 3. Cyclic transport bound

Correct. For total positive mass \(P=\|B\|_1/2\), pairing unit positive and negative tokens and routing along shortest arcs costs at most
\[
P\lfloor L/2\rfloor\le L\|B\|_1/4.
\]
This constructs an admitted integer flow, so the minimizing cost cannot be larger.

### 4. Winding block

Correct. A cycle of winding vector \(w\) has length at least \(L\|w\|_1\). Since the augmented component is null-homologous, the nonzero winding vectors sum to zero. A nonempty integer family summing to zero has total L1 winding norm at least two, hence total winding-cycle length at least \(2L\).

The proof correctly treats winding cycles collectively rather than applying the zero-winding lemma to each.

### 5. Whole-component constant

Correct:
\[
\ell_K\le M_0^2/16+M_w^2/8\le M_K^2/8.
\]
The sharper \(1/16\) statement when \(M_w=0\) follows immediately.

### 6. Sharpness

Correct at the stated larger deterministic class. Two opposite coordinate winding loops at axial separation \(L/2\) give source
\[
L\delta_0-L\delta_{L/2},
\]
a primitive taking values \(0\) and \(L\) on equal half-cycles, and therefore
\[
\ell=L^2/2=(2L)^2/8.
\]
The note correctly refuses to claim that this sharp witness is realized by one ternary augmented component.

### 7. Rooting identity

Correct. Every component K contributes its value \(M_K^3\) once for each of its \(M_K\) nonzero current edges:
\[
\sum_e 1_{\{e\ {\rm charged}\}}M_{K(e)}^3
=\sum_K M_K^4.
\]
Using all \(4V\) canonical positive edges avoids any rotational-equality assumption.

### 8. Tail identity

Correct by telescoping:
\[
M^3=\sum_{r=1}^M(3r^2-3r+1).
\]
The sufficient polynomial tail exponent is also correctly stated: \(r^{-3-\epsilon}\) makes the weighted \(r^2\) series summable.

### 9. Old neutral-polymer attacks

The distinction is valid and important. The old tree grammars count neutral surface area. The new target counts only nonzero current edges in the augmented component. Existing long neutral-connector examples show directly that neutral area can diverge while current-edge count stays fixed, so failure of neutral-area majorants does not decide \(R_3\).

### 10. Prime/cyclotomic comparison

Inside the explicitly declared comparison family,
\[
D=[\mathbb Q(\zeta_p):\mathbb Q]=p-1.
\]
A one-hole current star has \(p\) occupied faces and one missing face, while a D-dimensional hypercubic edge star has \(2(D-1)\) faces. Thus
\[
p+1=2(D-1)=2(p-2),
\]
which is precisely
\[
(p-2)/(p+1)=1/2.
\]
This reproduces the equation of public P5-ROOT-SELECTION and gives \(p=5,D=4\).

The firewall is necessary and correctly present: this is a combinatorial interpretation inside a comparison family, not a second unconditional physical selector.

## Remaining blocker

Nothing in this package proves a uniform bound on
\[
R_3(L).
\]

That is now the correct next theorem target. A failed bound on neutral surface area is irrelevant unless it can be converted into a current-edge component tail.

## Review ceiling

Suitable to merge as NON-CANONICAL candidate-T with candidate-C audit after repository checks. No Canon promotion, P1 closure, massless-phase conclusion or Euler-product claim is justified.
