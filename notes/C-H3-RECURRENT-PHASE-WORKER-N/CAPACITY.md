# Capacity of a collision-only matter register

**NON-CANONICAL, L1 analytical bound.** Suppose one site is intended to store an 85-valued answer in its pair \((r_0,r_2)=(m+d,m-d)\). Use the same initial matter pair for every input. Assume that transport leaves both of these coordinates unchanged at every step during the encoding. Radiation can arrive from other sites, and every native collision guard is allowed to depend on the input. Let \(Q\) bound the complete scalar account for every preparation.

Each collision keeps \(m\) fixed. Its effect on \(d\) is multiplication by \(1,J\), or \(J^{-1}\). If the initial matter difference is odd, the collision always refuses. If the initial half-difference is zero it remains zero. Otherwise \(d_0\in O\setminus\{0\}\), and every possible material output has the form \(d=J^e d_0\) for an integer \(e\). After \(t\) collisions there are at most \(2t+1\) such values. Conservation gives a time-independent bound as well.

In the embedding in which \(h(J)=\lambda=(3+\sqrt5)/2\), put \(A=|d_0|^2\). Put \(B=|d_0'|^2\) in the other inequivalent embedding, where \(h(J)'=\lambda^{-1}\). The algebraic norm \(N=AB\) is a positive rational integer. Positivity of all the rails at both embeddings and the identity \(h(m+d)+h(m-d)=2h(m)+2h(d)\) give
\[
Q\ge 2(A\lambda^e+B\lambda^{-e}).
\]
If two attainable exponents have span \(L\), add their inequalities and apply the arithmetic-geometric mean inequality at their midpoint. This gives
\[
Q\ \ge\ 2\sqrt{N}\,(\lambda^{L/2}+\lambda^{-L/2}).
\]
Let \(S_n=\lambda^n+\lambda^{-n}\), so \(S_0=2,\ S_1=3,\ S_{n+2}=3S_{n+1}-S_n\). Thus \(Q^2\ge4N(S_L+2)\). At either budget in this note \(Q^2<4(S_{39}+2)\). The exponent span is at most 38, so **at most 39 different matter pairs** can ever be encoded in the isolated site. To support 85 distinct values under these assumptions would require \(L\ge84\) and
\[
Q\ge 2S_{42}=717780700011756164.
\]
This is a necessary condition without an attainability assertion.

For the particular blank half-difference \(d_0=F=1025\) the bound is stronger. Here \(Q\ge2F^2 S_{|e|}\) and \(2F^2S_5=258453750\) exceeds both stock budgets. Only exponents from \(-4\) through \(4\) fit. Starting from \(JF\) gives the same nine-value upper bound after translating the exponent index.

The passive worker in the construction uses two-site matter transport and its midpoint changes. The bound explains why that feature matters for a successor design. Changes in a midpoint, imports of material half-difference from another site, or several jointly read sites all need to be included explicitly in the next receiver specification. The conclusion is confined to the isolated material channel above.
