# The selected original energy has a sharp physical local-error floor

**NON-CANONICAL, L1, conditional analytical candidate-T.**
Owner: A. M. Thorn / C-COMPACT-ENERGY-RECORD-N, issue #1778.
Apache-2.0. Independent scientific acceptance is not asserted.

This note decides one concrete original-energy admission problem. It uses
the actual product occupation encoding, the complete one-pair/one-carrier
sector, the fixed positive scalar logarithm, and finite physical interaction
diameter. The answer is negative, with an exact uniform error floor. The
statement does not decide finite prepared families, other logarithms,
additional branch registers, or different dressed encodings.

No scientific executable, matrix enumeration, numerical search or simulation
was run. The proof is analytical. Its predecessor premises retain their own
conditional status.

## 1. Frozen target and physical support class

The authority is Public Canon v105 at
`892a0b11089d34e241e1eb76d2c03247022d18e6`. The operator and occupation
codes are those of `HOMOGENEOUS-CAPTURE-CURRENT-RECORD` there. The fixed
energy is

\[
 Q=E_0 f(U_{\rm rec}),\qquad E_0>0,\qquad
 e^{-if(z)}=z,\quad 0\le f(z)<2\pi,\quad f(1)=0.       \tag{E1}
\]

It is specifically this scalar Borel branch, not the occupation charge.
Its boundedness and full spectrum, and the translated free limit used
below, are the analytical premises in
[#1772 SPECTRAL.md](https://github.com/mathorn1973/twist-j/blob/3abf054e435e31c51e6e50528b09fe3cf7cffe13/notes/C-FULL-RECORD-SCALE-LIFT-N/SPECTRAL.md).
The extension-versus-compression distinction is the one in
[#1777 ENERGY_EXTENSION.md](https://github.com/mathorn1973/twist-j/blob/191ab035be823bd9d6fdc9effba81528fa026e49/notes/C-ORIGINAL-PORT-CONSOLIDATION-N/ENERGY_EXTENSION.md).

Let \(\mathcal I\) be the specified occupation isometry, with the object
gauge \(\mathsf{Emb}\Gamma^{-1}D_2^*\), the original receiver at 100,
and the given carrier and memory label codes. A pulse occupies exactly one
physical site \(x\). Its nonzero code lies in either \(h_7,\ldots,h_{11}\)
or \(h_{12},\ldots,h_{16}\), has two signed occupied coordinates, and has
charge four. Objects occupy \(h_1,\ldots,h_4\); the receiver occupies
\(h_{25},\ldots,h_{37}\). These subbanks are disjoint even at coincident
physical positions. The remaining spectator coordinates are fixed. All
26 carrier labels and all 26 receiver labels remain admitted.

The lower-bound proof fixes any one normalized passive-reference vector
and compresses every comparison to that vector. This does not enlarge
the error or alter a carrier support zero. The resulting original space
is separable with finite internal multiplicity, regardless of the size
of an optional reference. The bound therefore also holds for an operator
norm claimed uniformly with arbitrary references.

Fix a finite integer \(\rho\ge0\). A raw physical interaction in the
admitted class is a self-adjoint operator \(\widetilde Q\) whose
compression

\[
 K=\mathcal I^*\widetilde Q\mathcal I                 \tag{E2}
\]

is bounded, and whose coded basis matrix elements are given by sums of
terms supported on sets of physical sites of diameter at most \(\rho\).
For an infinite sum its coded matrix elements must be limits of the
corresponding finite partial sums. This includes finite sums and
well-defined locally finite interactions on finite-occupation sectors,
after any required vacuum-energy subtraction. The condition does not
presume translation invariance, positivity, conservation of occupation
charge, a bound on the number of factors in one support, or an onsite
spectral choice. Imposing any of these extra requirements only narrows
the class.

An exact energy extension would satisfy the stronger action equation
\(\widetilde Q\mathcal I=\mathcal I Q\), and therefore \(K=Q\).
For approximate action, compression gives

\[
 \|\widetilde Q\mathcal I-\mathcal I Q\|
 \ge \|K-Q\|.                                       \tag{E3}
\]

All norms here are uniform operator norms over the complete original
sector, not an error on one chosen input or a finite observation window.

## 2. Physical locality forces finite pulse displacement

**Lemma E1.** For two pulse code kets, every admitted \(K\) obeys

\[
 \langle R,r,x,\eta|K|R',r',x',\eta'\rangle=0
 \quad\hbox{whenever }|x-x'|>\rho.                    \tag{E4}
\]

The finite internal index \(\eta\) includes object coin, pulse bank,
carrier label and old-memory label. No condition on the object coordinates
or their displacements is needed.

**Proof.** Suppose \(x\ne x'\). At site \(x\), the first ket has a
nonzero pulse code in the carrier subbank, while the second has carrier
vacuum there. At \(x'\) their roles reverse. Object occupation, receiver
occupation and fixed spectators cannot remove either difference because
their factors are disjoint from that subbank. A local term with a nonzero
matrix element must therefore include both physical sites. Their distance
is greater than \(\rho\), so no allowed support can contain both. Every
term has zero matrix element, and so does its admitted sum.

The object gauge contributes only basis phases. Receiver calibration
permutes carrier and memory labels without moving the pulse or making its
code zero. Both preserve this argument. No indistinguishable-object
assumption or object-position allocation is used. QED.

The lemma concerns a generator matrix element. Intermediate transitions
through invalid codes, tokens or auxiliaries during an exponential do not
change it. A fixed auxiliary state also cannot repair the orthogonal
carrier factor outside the support. A different encoded source or a
dynamical energy-branch register would require a separate admission.

## 3. The relevant free-limit jump

Use the frozen configuration translations

\[
 S_N:(R,r,c)\mapsto(R,r+N,c-N).
\]

The predecessor proves, including the absence of a spectral atom at the
Borel cut in the free operator,

\[
 S_N^*Q S_N\longrightarrow Q_f:=E_0f(U_f)
 \quad\hbox{strongly}.                              \tag{E5}
\]

The pulse block of \(U_f\) has Fourier matrix
\(e^{-i\beta}W_f(P,q)\otimes V(k)\), with

\[
 a_p=2\arctan2,\quad b_p=\pi-a_p,\quad\beta=4\pi/5,
 \qquad \cos\varepsilon(k)=(1-4\cos k)/5.
\]

At \((P,q)=(\pi,\pi)\), \(W_f=-M_2\) has the simple eigenvalue
\(e^{ib_p}\). Combine its locally smooth normalized eigenvector with
the pulse eigenvector of eigenvalue \(e^{i\varepsilon(k)}\). Its energy
angle is

\[
 E(k)=\beta-b_p-\varepsilon(k).
\]

Since \(\beta-b_p=a_p-\pi/5\in(0,a_p)\), there is
\(k_0\in(0,\pi)\) with \(E(k_0)=0\). The derivative
\(\varepsilon'(k_0)=-4\sin k_0/(5\sin\varepsilon(k_0))\)
is nonzero. Simplicity and this transverse crossing persist throughout an
open neighborhood of \((\pi,\pi)\). Write the normalized product
eigenvector there as \(w(P,q,k)\), and its smooth energy angle as
\(E(P,q,k)\). On the two open sides of its zero surface,

\[
 \langle w,Q_f(P,q,k)w\rangle=
 \begin{cases}
 E_0 E(P,q,k),&E(P,q,k)>0,\\
 E_0(E(P,q,k)+2\pi),&E(P,q,k)<0.
 \end{cases}                                       \tag{E6}
\]

Thus the one-sided limits differ by exactly \(2\pi E_0\).
Possible degeneracy with another product eigenvalue does not affect
(E6): functional calculus acts by the same scalar on every vector in
the nominated eigenvalue space.

## 4. A sharp uniform lower bound

**Theorem E2.** Every bounded original-space operator \(K\) whose
pulse-to-pulse block satisfies (E4) for some finite \(\rho\) satisfies

\[
 \boxed{\|K-Q\|\ge\pi E_0.}                        \tag{E7}
\]

Self-adjointness is not needed for the lower bound. In particular every
physical interaction of Section 1 satisfies (E7) and the same lower
bound in (E3). An exact finite-diameter physical extension of this \(Q\)
on the entire original sector is impossible.

**Proof.** Put \(\delta=\|K-Q\|\) and compress to the pulse sector.
The translated operators \(S_N^*KS_N\) are uniformly bounded, and (E4)
is unchanged by these translations. On this separable Hilbert space a
subsequence of their pulse blocks has a weak-operator limit \(K_\infty\).
Its pulse displacement is still at most \(\rho\), because each forbidden
basis matrix element is zero throughout the sequence. Strong convergence
in (E5) and weak closedness of the norm ball imply

\[
 \|K_\infty-Q_{f,p}\|\le\delta,                     \tag{E8}
\]

where \(Q_{f,p}\) is the free pulse block.

Average \(K_\infty\) over conjugation by configuration translations
in finite cubes of \(\mathbb Z^3\). The averages retain the norm bound,
finite pulse displacement, and (E8), since \(Q_{f,p}\) is translation
invariant. A weak cluster point \(\overline K\) is translation invariant:
for each fixed translation the norm of the difference of the shifted and
unshifted averages is at most \(\|K_\infty\|\) times the relative
symmetric-difference size of the two cubes, which tends to zero.

Fourier transformation therefore makes \(\overline K\) a matrix-valued
multiplier. The finite pulse displacement implies the representation

\[
 B(P,q,k)=\sum_{n=-\rho}^{\rho} B_n(P,q)e^{ink},       \tag{E9}
\]

where the finitely many \(B_n\) are essentially bounded measurable
matrix functions. One way to see this is to take the carrier-coordinate
matrix blocks of \(\overline K\); they vanish outside these diagonals
and commute with both object-coordinate translations. Consequently
\(B(P,q,\cdot)\) is continuous for almost every \((P,q)\). No continuity
in \((P,q)\) is asserted or needed.

By the multiplication-operator norm and Fubini's theorem, for almost every
\((P,q)\) in the open crossing neighborhood,

\[
 \|B(P,q,k)-Q_{f,p}(P,q,k)\|\le\delta
 \quad\hbox{for almost every }k.                    \tag{E10}
\]

Choose one such pair. The scalar
\(b(k)=\langle w(P,q,k),B(P,q,k)w(P,q,k)\rangle\) is continuous near
its crossing. On each open side, (E6) and (E10) bound its distance from
the indicated continuous energy by \(\delta\). An almost-everywhere
bound between continuous functions on an open interval holds everywhere
on that interval. Taking the two one-sided limits at the crossing gives

\[
 |b(k_0)|\le\delta,\qquad
 |b(k_0)-2\pi E_0|\le\delta.
\]

The triangle inequality yields \(2\pi E_0\le2\delta\), proving (E7).
QED.

**Sharpness in the bounded comparison class.** Since the spectrum of
\(Q\) is \([0,2\pi E_0]\), the zero-displacement scalar comparison
\(K=\pi E_0 I\) obeys

\[
 \|Q-\pi E_0 I\|=\pi E_0.                          \tag{E11}
\]

Hence the infimum over all finite-pulse-displacement bounded comparisons,
even allowing arbitrarily large finite range, is exactly \(\pi E_0\).
The union of those classes cannot approach this global energy in uniform
operator norm. Equation (E11) is a sharp comparison bound, not a claim
that the scalar operator reproduces the original dynamics.

A scalar identity is itself an allowed empty-support raw term if the
vacuum energy is unrestricted. If zero vacuum energy is required, the
existing onsite active occupation charge gives another illustrative raw
comparison: \((\pi E_0/10)H_N\) is zero on the empty occupation state
and has compression \(\pi E_0 I\) on the fixed active charge-ten code.
Here the Canon's object, carrier and receiver charges are respectively
four, four and two; fixed spectator charge is excluded from this active
\(H_N\).
It is extensive and generally unbounded on the unrestricted raw space;
this observation does not assert admission when a globally bounded raw
operator is an additional requirement. It neither identifies charge
with \(Q\) nor removes the error in (E11).

## 5. Consequence for the smaller measurement model

The original energy cannot be made globally local in this fixed product
encoding merely by assigning energies to vacuum/invalid sectors,
increasing a finite support diameter, or shrinking numerical tolerances.
Even the weaker compression target has the nonzero floor (E7).

There are three distinct surviving tasks:

1. Freeze a finite prepared family and its observation horizon, retain
   \(\|(I-AA^*)QA\|\) as the original-energy leakage, and seek a
   family-specific error bound. Theorem E2 does not supply a floor for
   that restricted problem.
2. Restrict to a specified invariant safe channel, where the earlier
   energy intertwining applies. Its preparation and physical encoding
   still require their own proof.
3. Choose a different energy reading or an encoding with explicit
   energy-branch information, and state that change as new construction
   data. The theorem does not exclude that class.

This result therefore favors an honestly finite-family experiment for
the compact construction. It prevents describing that experiment as a
uniformly accurate local realization of the complete original scalar
energy. No thermal-source, detector, reset, or material-precision result
is automatically inherited through a changed energy target.

## 6. Separate analytical review obligations

1. Verify the frozen full-sector energy, occupation isometry, and exact
   pulse-code support, including all labels and the receiver gauge.
2. Verify (E4) from the two distinct physical pulse sites and the
   disjoint carrier subbank, without assuming an object allocation.
3. Check the allowed infinite interaction sums and bounded compression;
   distinguish complete action error from compressed error in (E3).
4. Check the inherited strong Borel limit (E5), including no atom at the
   cut; polynomial functional calculus alone is insufficient.
5. Verify the simple branch, transverse crossing, and open-neighborhood
   persistence used in (E6), rather than using one measure-zero slice.
6. Verify both weak limits, preservation of finite pulse range, the
   translation average, and the measurable-polynomial form (E9).
7. Verify Fubini, the one-sided scalar estimates, the exact floor, and
   the limited sharpness statements for the raw vacuum requirements.
8. Preserve the distinction between global uniform approximation and a
   finite-family experiment, and between this scalar logarithm and
   other generators/encodings. No unrestricted no-go or independent
   acceptance follows from this note.
