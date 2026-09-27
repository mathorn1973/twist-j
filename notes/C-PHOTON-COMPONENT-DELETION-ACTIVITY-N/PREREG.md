# PREREG - C-PHOTON-COMPONENT-DELETION-ACTIVITY-N

**Status:** PUBLIC, NON-CANONICAL incubation. No Canon authority.
**Owner:** A. M. Thorn / photon-component-deletion-activity-20260927
**Date:** 2026-09-27
**Issue:** #1200
**Action layer:** L6 exact finite-measure / augmented-component combinatorics.
**Authority:** Public Canon v92. Normative files are unchanged.

## Frozen inputs

The exact one-copy paired augmentation from
\`notes/C-PHOTON-BCHI-DIRECT-BOUND-N/CONNECTED-CURRENT.md\` has unsigned
consistent structures \((S,\mathcal M)\) with

\[
\widetilde w(S,\mathcal M)
=
2^{k(S,\mathcal M)-|S|}
\prod_{e:d_e\ {\rm even}}\frac1{(d_e/2)!}.
\]

At a charged edge \(d_e=5\), all five occupied incidences lie in one
component. At a neutral edge the matching pairs positive and negative
incidences.

The public four-cup defect notation is

\[
U(x)
=
-c_{012}(x)+c_{012}(x-e_2)
-c_{013}(x)+c_{013}(x-e_3),
\]

\[
a(x)=\partial U(x)-5p_{01}(x),
\qquad
\partial a(x)=-5\partial p_{01}(x).
\]

## G1. Exact component-deletion ratio

Fix one complete augmented component \(K\) inside a consistent unsigned
structure. Let

- \(A_K\) be its number of faces;
- \(k\) be the original component count;
- at a neutral lattice edge \(e\), let the full structure have
  \(r_e=d_e/2\) matched pairs and let \(K\) use \(t_e\) of them.

Delete every face and every matching/link belonging to \(K\), retaining all
other components unchanged.

Prove:

1. the result is again a valid consistent augmented structure;
2. the component count is \(k-1\);
3. at every neutral edge the remaining pair count is \(r_e-t_e\);
4. the exact weight ratio is

\[
\boxed{
\frac{\widetilde w({\rm full})}
     {\widetilde w({\rm full}\setminus K)}
=
2^{1-A_K}
\prod_{e:t_e>0}
\frac{(r_e-t_e)!}{r_e!};
}
\]

5. since \(r_e\ge t_e\),

\[
\frac{(r_e-t_e)!}{r_e!}\le\frac1{t_e!},
\]

and therefore

\[
\boxed{
\frac{\widetilde w({\rm full})}
     {\widetilde w({\rm full}\setminus K)}
\le
z(K):=
2^{1-A_K}\prod_{e:t_e>0}\frac1{t_e!}.
}
\]

Here \(z(K)\) is the standalone unsigned activity of the same marked
component pattern.

## G2. Fixed marked-component occurrence bound

A marked component pattern includes its face set, internal neutral matching
pairs and degree-five links, hence its relative signing up to the one global
component reversal.

Deletion is injective on the event that this marked pattern occurs: the
remaining structure together with the fixed marked component reconstructs
the original structure uniquely.

Summing G1 over its deletion image proves

\[
\boxed{
P_{\rm aug}(K\ {\rm occurs})\le z(K).
}
\]

The exterior may contain arbitrary other charged and neutral components.
No empty-halo or zero-current exterior is assumed.

## G3. Generic face/current incidence floor

Let \(M_K\) be the number of charged current edges in \(K\). Every charged
edge has exactly five incident faces of \(K\), while every face has four
boundary edges. Therefore

\[
5M_K\le4A_K,
\qquad
\boxed{A_K\ge\frac54M_K.}
\]

This is only a generic floor and is not claimed sufficient for summing
component entropy.

## G4. Infinite defect-chain control

For \(N\ge1\), put

\[
x_i=-i(e_2+e_3),
\qquad
n_N=\sum_{i=0}^{N-1}(-1)^i a(x_i).
\]

Prove by one local translated motif plus induction:

1. adjacent defect supports intersect in exactly two \(01\)-faces, with equal
   coefficients before the alternating sign, so both cancel;
2. defects at separation at least two have disjoint face supports;
3. hence \(n_N\) is ternary and

\[
\boxed{|{\rm supp}\,n_N|=21N-4(N-1)=17N+4;}
\]

4. its current is

\[
j_N=\partial n_N/5
=
-\sum_{i=0}^{N-1}(-1)^i\partial p_{01}(x_i);
\]

5. the \(N\) central \(01\)-plaquette boundaries are pairwise edge-disjoint,
   hence

\[
\boxed{|{\rm supp}\,j_N|=4N;}
\]

6. every noncharged occupied edge has degree two, every charged edge degree
   five, so all neutral matchings are unique;
7. the resulting face-link graph is connected for every \(N\), hence \(n_N\)
   is one augmented component.

Therefore the component family has

\[
\boxed{
\frac{A_N}{M_N}
=
\frac{17N+4}{4N}
=
\frac{17}{4}+\frac1N
\longrightarrow\frac{17}{4}.
}
\]

Its standalone activity is exactly

\[
z_N=2^{1-(17N+4)}=2^{-17N-3},
\]

because every neutral matching has \(t_e=1\).

## G5. Falsified extrapolation

The elementary current loop has a 21-face minimum and \(M=4\), ratio \(21/4\).
G4 proves that the linear extrapolation

\[
A_K\ge\frac{21}{4}M_K
\]

is false for \(N\ge2\).

The family does **not** prove the general lower bound \(A_K\ge17M_K/4\).
It only proves that any valid universal asymptotic linear coefficient cannot
exceed \(17/4\).

## G6. R3 boundary

G2 controls each fixed marked augmented component after all exterior
components are summed. It does not sum the number of possible marked
components with a given current size.

Therefore this package does not prove a tail for

\[
R_3(L)
=
\frac1{4V}\sum_e
E_{\rm aug}[1_{\{e\ {\rm charged}\}}M_{K(e)}^3].
\]

A separate entropy, switching, or exact connected-component generating
theorem remains necessary.

## Audit

Only after this file is committed and publicly read back, a standard-library
exact verifier may:

- check the factorial ratio and bound for every \(0\le t\le r\le3\);
- derive the four-cup defect from cubical boundaries;
- verify the adjacent and nonadjacent support-intersection motifs;
- verify G4 for \(1\le N\le64\), including ternarity, support counts,
  current, edge degrees, unique neutral matching and component connectivity.

Finite execution is at most candidate-C. The all-\(N\) result rests on the
translated local motif and induction in the written proof.

## Falsifiers

Any exact counterexample to G1-G4 fires the corresponding candidate.
A component with \(A/M<17/4\) would not falsify this package; it would only
show that the displayed control family is not asymptotically extremal.

## Repository boundary

Only \`notes/C-PHOTON-COMPONENT-DELETION-ACTIVITY-N/\` may be added.

No Canon, Registry, Frontier, formal probe, gate, tool, workflow, release or
existing note may be changed.
