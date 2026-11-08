# Exact energy extensions and a local-support admission test

**NON-CANONICAL. L1. Conditional analytical candidate-T. Independent
acceptance pending.** Author: A. M. Thorn. Apache-2.0.

This is new analytical work attached to the consolidation. Its eight review
obligations below are separate from the unchanged predecessor's twenty and
the autonomous source package's twenty-one. No feasibility solver,
scientific executable or simulation was run. The elementary lemmas make an
energy admission test precise; they do not complete the original-energy
bridge or establish a material implementation.

## 1. Fixed problem and sources

The public authority is Canon v105 at
`892a0b11089d34e241e1eb76d2c03247022d18e6`. The source construction conserves
the complete bare energy built from the occupation charge
`H_N=2 sum h^2`, reservoirs, donors, fuel, flags and cursors. Its
[energy account, section 6](../C-AUTONOMOUS-ORIGINAL-PORT-SOURCE-N/ENERGY_ACCOUNT.md)
explicitly leaves open the identification with the nominated original
spectral energy `Q=E_0 f(U_rec)`, including its extension to vacuum and
invalid occupation codes. The
[fixed occupation encoding](../C-ORIGINAL-PORT-SOURCE-PREPARATION-N/LOCAL_REALIZATION.md)
includes the diagonal gauge `I_0=Emb Gamma^(-1) D_2*` and the whole unknown
memory code. These are not freely adjustable after a desired output is
chosen.

Two distinct targets must be kept separate:

1. An extension of a bounded self-adjoint operator on an admitted invariant
   sector, preserving its entire action.
2. A finite model of a non-invariant family in the original Hilbert space.
   Compressing `Q` to that family does not preserve its entire action.

For the finite apparatus let

\[
 \mathcal D=\bigotimes_{i\in\Lambda}\mathcal D_i,
 \qquad J:\mathcal C\longrightarrow\mathcal D,
 \qquad J^*J=I,\quad P=JJ^*,\quad q=q^*\text{ on }\mathcal C.
 \tag{X1}
\]

The finite sites, their dimensions, the code isometry `J`, the target `q`,
the allowed site supports and their norm bounds are fixed input to the
test. If `q` is meant to represent the original `Q`, that identification
needs the invariant-sector hypothesis or the leakage account of section 3.
All statements extend by the identity on a passive reference; they do not
replace that reference by a finite table.

## 2. Algebraic extension exists, without a locality conclusion

**Lemma 1 (all exact reducing extensions).** A self-adjoint operator
`Q_tilde` on `D` satisfies

\[
 \widetilde QJ=Jq                                             \tag{X2}
\]

if and only if, in `D=Ran J direct_sum (Ran J)^perp`, it has the form

\[
 \boxed{\widetilde Q=JqJ^*+B,\qquad
        B=B^*,\quad B=(I-P)B(I-P).}                         \tag{X3}
\]

It is positive if and only if both `q` and the complementary block `B`
are positive, and its norm is `max(||q||,||B||)`.

**Proof.** Equation (X2) gives `(I-P) Q_tilde P=0` and
`P Q_tilde P=JqJ*`. Taking the adjoint gives
`P Q_tilde (I-P)=0`. Thus the off-diagonal blocks vanish and the remaining
block is precisely `B=(I-P) Q_tilde (I-P)`. Conversely (X3) immediately
gives (X2). Positivity and the norm formula are those of an orthogonal
direct sum. QED.

In particular, if `q>=0` and the vacuum vector `v` is orthogonal to the
code, choosing `B=0` supplies a bounded positive extension with
`Q_tilde v=0`. Prescribed nonnegative energies on an orthonormal collection
of complementary vacuum or invalid-code states can instead be inserted
into `B`. This demonstrates algebraic freedom only. The projectors `P`
and `|v><v|`, and the block `JqJ*`, may themselves be nonlocal.

If a self-adjoint charge `N` satisfies `NJ=n_0 J`, then the code reduces
`N`. For every complementary `B` commuting with the complementary block
of `N`, (X3) also commutes with `N`. Thus constant occupation charge does
not by itself obstruct a nontrivial spectral energy inside the code.
It also does not make that energy local or ensure that the existing
preparation dynamics conserves it.

The same block argument applies to a bounded `q` and an infinite
isometrically embedded invariant sector. A finite apparatus, however,
cannot contain an isometric copy of an infinite-dimensional sector merely
by assigning additional energies to its finitely many invalid states.

## 3. A finite compression has an irreducible leakage error

Let `Q=Q*` be bounded on the original Hilbert space `H`, and let
`A:C->H` be a specified finite-dimensional isometry. Put

\[
 q=A^*QA,\qquad P_A=AA^*,\qquad
 L=(I-P_A)QA,\qquad \ell=\|L\|.                          \tag{X4}
\]

**Lemma 2 (compression versus action).** For any self-adjoint operator
`h` on `C`,

\[
 QA-Ah=A(q-h)+L,
\]
\[
 \boxed{(QA-Ah)^*(QA-Ah)=(q-h)^2+L^*L.}                 \tag{X5}
\]

Consequently

\[
 \|QA-Ah\|\ge\max\{\ell,\|q-h\|\},\qquad
 \|QA-Ah\|\le\sqrt{\ell^2+\|q-h\|^2},
\]
\[
 \boxed{\inf_{h=h^*}\|QA-Ah\|=\ell,}
 \quad\text{with equality at }h=q.                     \tag{X6}
\]

**Proof.** Insert `P_A+(I-P_A)` before `QA`. The two resulting ranges are
orthogonal, and `A*L=0`, so the mixed terms in the square vanish. The
operator `(q-h)^2+L*L` is greater than or equal to each of its positive
summands; this gives both lower bounds. The triangle inequality for the
positive summands gives the upper bound. For `h=q`, the residual is
exactly `L`, proving the infimum. QED.

In particular, an exact finite action `QA=Ah` exists precisely when the
family reduces `Q`; in that case `h=q`. Extending the finite matrix `q`
by Lemma 1 does not remove a nonzero `ell` in the original carrier.
Equality of energy expectations on the family is weaker than equality
of energy action, spectral events or continuous-time evolution.

The pinned
[#1774 finite-prefix construction](https://github.com/mathorn1973/twist-j/blob/3de02b0eb898f1756e3626ee2881d596c72d0094/notes/C-FINITE-PREFIX-ENERGY-BRIDGE-N/FINITE_PREFIX.md)
already supplies a different, energy-binned finite family and explicit
leakage and real-time bounds. Lemma 2 does not replace its construction.
It states the additional check required whenever a new finite source
family is used in (X1).

## 4. The exact local extension is a finite feasibility problem

Fix a finite family `S` of allowed supports `X subset Lambda`. Each
support has a prescribed norm cap `J_X`; geometric range and incidence
bounds belong to this specification. The proposed raw operator has the
form

\[
 \widetilde Q=\sum_{X\in\mathcal S}
       h_X\otimes I_{\Lambda\setminus X},\qquad h_X=h_X^*.
 \tag{X7}
\]

Once `J`, `q`, `S`, the caps and the vacuum energy `E_v` are fixed, exact
local admission means finding actual matrices `h_X` satisfying

\[
 \widetilde QJ=Jq,\qquad
 \widetilde Qv=E_vv,\qquad
 -J_XI\le h_X\le J_XI,\qquad \widetilde Q\ge0.           \tag{X8}
\]

If preservation of a specified raw charge is required, add
`[Q_tilde,N]=0`. Prescribed actions on further invalid sectors add their
own equations. Positivity of each individual term may also be required,
but it is a stronger condition and must be declared before the test.
These are finitely many linear matrix equations and semidefinite
inequalities. This formulation is an exact finite criterion, not a
report that the particular TWIST instance is feasible or has been solved.

The compression equation `J* Q_tilde J=q` alone is insufficient. It omits

\[
 (I-P)\widetilde QJ=0.                                 \tag{X9}
\]

For example, take `C=span{|0>}`, `D=span{|0>,|1>}`, `q=1` and
`Q_tilde=I+X`. This positive operator has the requested scalar
compression, yet `Q_tilde|0>=|0>+|1>` leaks out of the code. The full
intertwining equation in (X8) detects the defect.

For approximate admission one may replace its first equation by
`||Q_tilde J-Jq||<=delta`, with the error norm and `delta` fixed in
advance. If `q` came from (X4), the separate original-space leakage
`ell` remains part of the comparison. A proof of approximate admission
does not automatically preserve exact charge commutation or positivity
under unspecified changes of the couplings.

## 5. A support witness that no invalid-sector choice can repair

Assume the two specified code vectors are represented by phase-weighted
product basis kets in the fixed raw occupation encoding:

\[
 J|a\rangle=e^{i\theta_a}\bigotimes_i|a_i\rangle,
 \qquad
 J|b\rangle=e^{i\theta_b}\bigotimes_i|b_i\rangle.
 \tag{X10}
\]

Define their set of differing physical factors by
`D(a,b)={i:a_i != b_i}`. A diagonal phase gauge changes neither this set
nor a vanishing matrix element.

**Lemma 3 (local-support witness).** If `D(a,b)` is not contained in any
allowed support `X in S`, every operator of the form (X7) obeys

\[
 \langle Ja|\widetilde Q|Jb\rangle=0.                  \tag{X11}
\]

If `q_ab=<a|q|b> !=0`, no such operator can satisfy (X2), and every one
has the quantitative residual

\[
 \boxed{\|\widetilde QJ-Jq\|\ge |q_{ab}|.}             \tag{X12}
\]

**Proof.** For each term choose `i in D(a,b)\X`. That term acts as the
identity on factor `i`; its matrix element contains the vanishing factor
`<a_i|b_i>=0`. Sum over the finite family of terms. Taking the residual
matrix element between `Ja` and `b` then gives `-q_ab`; normalized
vectors bound its absolute value by the residual norm. QED.

More generally, let `A_0,B_0` be orthogonal projections onto two spans of
code basis vectors, with the same exclusion holding for every cross pair.
Then

\[
 \|\widetilde QJ-Jq\|\ge\|A_0qB_0\|.                 \tag{X13}
\]

Indeed `A_0 J* Q_tilde J B_0=0`; compress the residual by these
projections. This can use a whole forbidden block rather than one entry.

A fixed additional ancillary state cannot change (X11) when, for each
allowed support, a differing source factor outside it still supplies the
orthogonal product factor in the proof. An arbitrary reference tensored with the
code also cannot remove it. A code represented by genuinely different
dressed or nonproduct source states is a different admission problem;
(X10) must then be checked again, not presumed.

**Exact illustrative example.** Take two qubit sites `L,R` whose distance
exceeds the maximum diameter of an allowed support. Thus no allowed support
contains both. Set

\[
 J|l\rangle=|10\rangle,\qquad J|r\rangle=|01\rangle,
 \qquad
 q=\kappa\begin{pmatrix}1&-1\\-1&1\end{pmatrix},
 \quad\kappa>0.                                        \tag{X14}
\]

The matrix `q` is positive, with eigenvalues `0,2 kappa`, and both code
vectors have the same excitation number. Lemma 1 supplies a positive
extension with zero vacuum energy, for example
`Q_tilde=kappa(|10>-|01>)(<10|-<01|)`, zero on `|00>,|11>`.
It preserves excitation number. Nevertheless every operator satisfying
the declared support restriction has residual at least `kappa`, by
(X12). Choosing different energies or couplings entirely inside the
vacuum/invalid complement cannot repair that missing code matrix element.
This is a general two-site witness, not a computed counterexample to the
actual TWIST spectral energy on its admitted source family.

## 6. Application boundary and next exact target

The existing occupation code makes the algebraic part of extension
particularly transparent: the ready source and memory sector has a fixed
occupation charge. A nontrivial `q` on that sector can coexist algebraically
with that charge, and the complement can contain vacuum and `h=2` states.
The unresolved work is to supply the right `q` or original `Q` sector and
a realization meeting the actual local and dynamical conditions.

The
[#1772 locality result](https://github.com/mathorn1973/twist-j/blob/3abf054e435e31c51e6e50528b09fe3cf7cffe13/notes/C-FULL-RECORD-SCALE-LIFT-N/SPECTRAL.md)
concerns uniform exponential decay in the configuration coordinates
`(R,r,c)` for one fixed Borel logarithm. That result is not, by itself, a
proof that every allowed occupation-space term violates (X7). To apply
Lemma 3 to the original `Q`, one must exhibit the actual two code kets or
two code subspaces, prove their physical support exclusion and evaluate
the nominated spectral matrix element or block. The full infinite class,
a selected invariant channel and a non-invariant finite source family
remain different targets.

The next bounded task is therefore to freeze one such target and its
physical support family, then provide either:

- explicit `h_X` satisfying the full equations (X8), with all stated
  bounds and the appropriate original-energy leakage account; or
- one nonzero forbidden matrix element/block yielding (X12)/(X13), or
  another exact infeasibility certificate for those same frozen equations.

Even a successful extension would not transfer the old thermal proof
automatically. States thermal for the original onsite occupation
Hamiltonians need not be thermal for `Q_tilde`; the complete funded gate
word need not conserve a new total energy containing `Q_tilde`. Those
state, interaction and resource requirements remain separate admissions.
There is no assertion here that the old term
`epsilon H_N-Q_tilde` has become a permitted local interaction.

## 7. Separate review obligations

1. **X-R1, fixed input.** Check the exact code, gauge, original-space
   identification, reference convention and frozen allowed supports. A
   finite compression must not be relabelled an invariant original sector.
2. **X-R2, extension.** Verify both directions of (X3), positivity, norm,
   complementary vacuum energies and the constant-charge commutation
   statement, including every raw sector.
3. **X-R3, leakage.** Verify (X4)-(X6), the exact minimum and the claim
   that bounded self-adjoint invariance implies reduction. Check that
   original leakage is retained in every finite approximation claim.
4. **X-R4, local admission.** Check the complete equations and inequalities
   in (X7)-(X9), including support, norm, positivity and vacuum conditions.
   Verify the positive compression-only counterexample.
5. **X-R5, support witness.** Verify (X10)-(X12) in the fixed physical
   tensor product, including the phase gauge and the qualifications on
   ancillary and reference states.
6. **X-R6, quantitative scope.** Verify the forbidden-block bound (X13)
   and the exact two-site example (X14). Do not label that example an
   evaluated TWIST matrix element.
7. **X-R7, prior results.** Check the distinct scope of pinned #1772 and
   #1774. Neither configuration locality nor a finite spectral compression
   may be silently substituted for the occupation-space admission problem.
8. **X-R8, physical boundary.** Check that this note claims no achieved
   local extension for the actual target, no new thermal preparation,
   no conservation under the existing controller, and no completed
   original-energy bridge or independent acceptance.

An invalid identity or false support implication falsifies the corresponding
lemma. Failure to solve the frozen local-admission instance leaves that
instance open; it is not an unrestricted impossibility theorem for TWIST.
