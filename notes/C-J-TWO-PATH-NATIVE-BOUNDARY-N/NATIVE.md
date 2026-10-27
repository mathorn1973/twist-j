# Native realization boundary for the two-path contact

Status: NON-CANONICAL. Layer: L1. Conditional analytical candidate only;
no new public claim status or physical realization is asserted.
Reservation: [issue #1806](https://github.com/mathorn1973/twist-j/issues/1806).
Author: A. M. Thorn <thorn@twistj.com>. Original text: Apache-2.0.

Public basis: ACTIVE Canon v105, immutable main/tag target
`892a0b11089d34e241e1eb76d2c03247022d18e6`. Existing claim identifiers below
refer to that tree. No scientific executable or formal gate is run here.

## 1. The conditional coherent construction

Let `H_S = C^5` have counting-orthonormal basis `|j>`, `j in Z/5`, and
`Z|j> = |j+1>`. On an added two-path space define

\[
C=|0\rangle\langle0|\otimes I+|1\rangle\langle1|\otimes Z^2.
\]

This C is a permutation of ten basis points. With the separately supplied
ready vector `|+>=(|0>+|1>)/sqrt(2)` and coherent output reading in the
plus/minus basis, the two branch operators are exactly

\[
K_0=\langle+|C|+\rangle=(I+Z^2)/2,\qquad
K_1=\langle-|C|+\rangle=(I-Z^2)/2.
\]

They obey `K_0^dagger K_0 + K_1^dagger K_1 = I`. A computational-basis
ready bit and a computational-basis read do not supply these operators.
Equivalently, preparing and recombining with a Hadamard makes the displayed
contact on a computational ready slice, but then those two coherent
operations are explicit resources. Classical random selection between I
and Z^2 gives a mixture of channels and lacks the cross terms in
`K_0 rho K_0^dagger`.

Write `V=1^perp` and `Pi=I-11^T/5`. Z preserves this faithful subspace.
For `phi^2=phi+1`, `phi>1`, the effect

\[
E_0=K_0^\dagger K_0=(2I+Z^2+Z^{-2})/4
\]

has eigenvalues `phi^(-2)/4` on characters k=1,4 and `phi^2/4` on k=2,3.
On the omitted constant character k=0 its eigenvalue is 1. Thus restricting
to V is a substantive source/code condition. These are effect weights;
neither physical energies nor event probabilities follow without their
separate reading and occurrence premises.

## 2. A genuine native word is not an actual-U schedule

The public native generators act on `x=(p1,p4,p1p,p4p,q,r)` in F5^6.
Their complete affine definitions, with every component taken modulo five,
are

```text
c=(2,1,3,4,1,1),       v=(0,0,0,0,1,0),
d(x)=c-x,             e(x)=c+v-x.
```

They are the definitions in the immutable [native verifier source][defs],
which is read here as source and is not re-executed. Direct substitution
gives `(e o d)(x)=x+v`, hence `(e o d)^2(x)=x+2v` for every checkpoint.

Canon section 2 gives `[d,e]=T_(0,0,0,0,3,0)`, with composition right to
left. Consequently the reverse commutator gives the desired translation:

\[
W=[e,d]=e\circ d\circ e\circ d
       =T_{(0,0,0,0,2,0)}.
\]

Its chronological command word is `d,e,d,e`. Explicitly the q coordinate
passes through `q, 1-q, 1+q, -q, q+2`. The four piston coordinates and r
have identical involutive transformations under d and e, so four such
letters restore them. This proves the word on every checkpoint, not only
on a five-state orbit. A unit q translation is `[d,e]^2`, so W is its
square. No word-length minimum is claimed.

This is a construction in the freely commanded alphabet
`Gamma=<a,b,c,d,e>`. Actual native evolution is instead

\[
U(n,x)=(n+1,g_{z(x)+2\theta_n}(x)),\quad
\theta_n=\operatorname{popcount}(n)\bmod2,
\quad(g_0,g_1,g_2,g_3,g_4)=(a,b,c,d,e).
\]

The selector is part of the law. One cannot replace its selected letter
by a desired command without supplying that intervention. In particular,
q translations change z; a word in Gamma need not be a valid continuation
of the synchronized native sheets. A controlled use of W on one path and
an identity action on the other is an additional control obligation, even
though the abstract ten-point controlled shift is a permutation.

Sources: [native law, Canon line 462][native-law],
[commutators, line 501][commutators], and
`QDD-PORT-QUOTIENT-ORIGIN-BOUNDARY [T]` at [line 6780][port-boundary].
The last claim explicitly distinguishes a constant commanded word from
source-dependent control and actual native commandability.

## 3. Exact point-preparation obstruction

Freeze the literal point encoding: a logical ready basis state is one
native basis point, and deterministic native evolution is represented by
`N_f|x>=|f(x)>`. Enlarged deterministic history labels are allowed, but no
coherent preparation is silently introduced in the encoder or decoder.

Then a single ready point remains one point after every finite protocol.
It cannot become the sum of two distinct encoded path points. This remains
true if f has collisions: one occupied input basis point still has one
image. Monomial phases change only its phase. Independent classical
mixtures of point preparations and monomial operations remain diagonal
and likewise do not create the missing off-diagonal path coherence.

This is a precise impossibility for that point encoding and gate class.
It is not an impossibility theorem for arbitrary coherent encodings,
pre-existing coherent auxiliaries, or non-diagonal coherent output maps.
Nor does an odd cycle alone exclude a two-valued reading: the native
alphabet has involutions, and the complete U has an unbounded counter.
The two classes in `QUBIT-FROM-F5 [T]` are a sign quotient, not an admitted
preparation of a coherent `|+>` state.

## 4. Complete classical-endpoint obstruction for this unsharp effect

Take five distinct point preparations at one common clock phase and any
finite deterministic native protocol with complete endpoints f(j). Use
the free counting representation on C^5, source subspace V, and a final
classical endpoint effect `0<=D<=I` diagonal in the endpoint basis.
This is the class of `U-POINT-SOURCE-SHARP-READOUT-NOGO [T]`, but the
following argument addresses the present unsharp E_0 directly.

If `f(j)=f(k)` for j!=k, then `v=|j>-|k>` belongs to V, has norm squared
2, and satisfies `N_f v=0`. Thus the complete code norm is not preserved.
Every subsequent linear endpoint branch also kills v; the pulled-back
effect has zero weight on it. In contrast K_0 is invertible even on C^5:
`1+zeta^(2k)` is nonzero for every fifth root zeta^k, since -1 is not a
fifth root. Therefore `v^dagger E_0 v>0`, excluding equality in this case.

If f is injective, its five output points are orthonormal and N_f is an
isometry. The complete endpoint-effect class on V is then

\[
F(w)=\Pi\operatorname{diag}(w_0,\ldots,w_4)\Pi\big|_V,
\qquad 0\le w_j\le1.
\]

Every w is possible by assigning those responses to the distinct endpoint
points. This includes classical randomized processing and arbitrary
deterministically supplied endpoint histories.

Suppose `F(w)=E_0|_V`. Since Pi commutes with Z and E_0 is a polynomial
in Z, average the equality over conjugation by Z^m, m=0,...,4. Cyclic
averaging makes every diagonal entry equal to `w_bar=(sum_j w_j)/5`:

\[
E_0|_V=\frac15\sum_{m=0}^4 Z^mF(w)Z^{-m}
      =\bar w I_V.
\]

This contradicts the two distinct golden eigenvalues in section 1.
Hence neither injective nor noninjective f realizes E_0 in this complete
point/free-representation/classical-endpoint class. The proof is not a
claim that E_0 is sharp, and does not misuse the earlier sharp-projector
conclusion. Changing the encoding or allowing a coherent endpoint read
changes the hypotheses. No complete physical apparatus class is excluded.

The canonical endpoint classification is at [Canon line 3225][point-nogo].
`U-GALOIS-FIBER-CODE [T]` supplies an explicit compatible alternative:
actual U transports a separately prepared correlated coherent code
isometrically in the declared free representation. Its source correlations
are substantive inputs, not a derivation of their preparation. See
[Canon line 3108][coherent-code].

## 5. Minimal positive native-realization contract

A positive successor should freeze the following before testing the target.

1. **Carrier and independent code.** Give all native coordinates, path
   states, source states, controller, counter, records and resource slots.
   Declare C^5 or V, the norm, and fixed encoding/decoding rules. A code or
   ready state defined afterwards by the desired K_0 is not its derivation.
2. **Ready preparation.** Exhibit how the coherent path state is prepared,
   or declare it supplied. State all initial source/path correlations.
   For a common-ready claim, the entire auxiliary ready state is independent
   of the source, including hidden coordinates and retained history.
3. **Actual controlled program.** Exhibit actual selected native histories
   or a declared enlarged law implementing I versus Z^2 at a common final
   counter. List every actuator and control predicate. A free phase factor
   `Y(U omega)=Z Y(omega)` rotates both paths and does not itself supply
   their relative control. The full native counter never returns after
   five steps, even when a five-phase factor does.
4. **Whole-code equality.** Prove an intertwining with the declared contact
   on the entire admitted source/path code, with one common phase, all
   reachable auxiliary states and every required continuation. Verify each
   prefix's norm and coherence, or supply the full instrument if a prefix
   is nonunitary. Basis output labels alone are insufficient if phases,
   discarded coordinates or normalization are unspecified. Do not define
   the output code as the desired inverse applied after the calculation.
5. **Complete instrument and records.** Supply both branches, their actual
   post-states, orthogonal output records, persistence interval and occupied
   memory behavior. Distinguish coherent path recombination from forgetting
   a fine path record. A no-click branch is a selected branch of a complete
   instrument, not an absent accounting obligation.
6. **Renewal, funding and occurrence.** Identify fresh ready slots, resets,
   retained records and any paid control. A finite-horizon or repeatable
   device must state its horizon and capacity. A conserved account or
   Hamiltonian is separate from the Hilbert norm. Finally declare the
   event/occurrence rule separately from the amplitude identity.

`QDD-SELECTED-SOURCE [D]` and `QDD-SELECTED-BORN [D]` already distinguish
adopted coherent preparation/control from adopted Born occurrence; neither
is derived merely by the native code transport. See [line 18727][source]
and [line 18784][born]. The conditional two-path contact is constructive
once its coherent interfaces are supplied. Its realization by unchanged U
remains open under the complete contract above.

[native-law]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L462
[defs]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/probes/P-FIRED-COMMUTATOR-NOGO-1/verify.py#L28
[commutators]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L501
[port-boundary]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L6780
[point-nogo]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L3225
[coherent-code]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L3108
[source]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L18727
[born]: https://github.com/mathorn1973/twist-j/blob/892a0b11089d34e241e1eb76d2c03247022d18e6/canon/CANON.md#L18784
