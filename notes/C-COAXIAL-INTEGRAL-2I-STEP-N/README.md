# C-COAXIAL-INTEGRAL-2I-STEP-N: first coaxial integral `2I` step

```text
STATUS:                 NON-CANONICAL INCUBATION
SCIENTIFIC STATUS:      candidate-T
ACTION LAYER:           L1 ALGEBRAIC STATE
AUTHORITY:              NO NORMATIVE AUTHORITY
FORMAL PUBLIC PROBE:    NONE
PREREGISTRATION:        NONE
PUBLIC OBJECT LOCK:     issue #680
CANON CHANGE:           NONE
REGISTRY CHANGE:        NONE
PROMOTION:              NONE
```

This note records a narrow exact result. It is not a formal public probe, it
does not earn a public computation gate, and it changes no Canon or Registry
row. The `candidate-T` label rests on the direct lattice argument below. The
companion program is an exact local audit of that argument, not its source of
theorem status.

## 1. Scope firewall

The diagonal lattice lemma applies only with all three of the following data
fixed:

1. one fixed, labeled binary icosahedral group `2I` in one fixed splitting
   \(B=(K/F,\sigma,-1)\);
2. the step is diagonal in the eigenbasis of one fixed fivefold element;
3. the lattice is the explicit orbit lattice
   \(\Lambda=F_\Lambda\mathcal O_K^2\) constructed below from the images of
   \(1\) and \(i\), and it is required to be preserved by both the labeled
   `2I` and the step.

The rapidity corollary adds a fourth condition: the step is the
determinant-one inverse pair \(\operatorname{diag}(q,q^{-1})\), and its phase
is matched to the selected fivefold tick. The lattice lemma itself applies to
arbitrary diagonal unit pairs in \(GL_2(\mathcal O_K)\); determinant one and
the tick phase enter only in the corollary.

Removing any applicable condition leaves the corresponding statement silent.
In particular, the result does not exclude a non-diagonal step, a non-coaxial
step, a similitude class in general, or a differently embedded or differently
labeled copy of `2I`. The fixed relative placement below does exclude the
specific similitude \(\operatorname{diag}(J,1)\). For the same labeled
embedding, one non-integral trace excludes every common
\(\mathcal O_K\)-lattice. That trace obstruction is general, but the positive
congruence criterion proved below is asserted only for the displayed orbit
lattice \(\Lambda\). Merely changing the basis of the same lattice is not an
escape.

**No transfer to the canonical update \(U\) is allowed.** Nothing here proves
that \(U\) is coaxial, diagonal, special-linear, or realized on this common
lattice. A separate named cross-layer construction would be required before
any statement about \(U\).

## 2. Compatibility with the existing incubation lanes

This result narrows one relative placement. It does not supersede any of the
following notes.

- [`C-COMMON-CARRIER-ICOSIAN-1`](../C-COMMON-CARRIER-ICOSIAN-1/C-COMMON-CARRIER-ICOSIAN-1.md)
  finds that the ramified icosian glue preserves the sign-twisted step
  \(\operatorname{diag}(J,-J^{-1})\). Its determinant is \(-1\), so it lies
  outside the inverse-pair \(SL_2\) rapidity corollary. The diagonal lattice
  lemma is compatible with its preservation. There is no contradiction.
- [`C-LORENTZ-HERM2-CARRIER-N`](../canon/C-LORENTZ-HERM2-CARRIER-N.md)
  retains the native Hermitian carrier and the normalized action of
  \(A_J=\operatorname{diag}(J,1)\).
- The accepted
  [`C-HERM2-BORN-CONE-1` audit](../C-HERM2-BORN-CONE-1/AUDIT-C-HERM2-BORN-CONE-1_2026-08-02.md)
  correctly observes that the standard free module
  \(\Lambda=\mathcal O_K^2\), with the registered integral `2I` lift and
  \(A_J\), is an integral common linear carrier.

The negative result below appears only after adding the same-axis condition
and the specific labeled icosian lattice placement. The standard
\(\mathcal O_K^2\) construction remains integral in its own frozen relative
placement. Thus the present obstruction is not a basis-independent statement
about every `2I` lift and not a no-go theorem for \(A_J\) in general.

## 3. Exact setting

Let

\[
K=\mathbb Q(\zeta_5),\qquad
F=\mathbb Q(\sqrt5),\qquad
\mathcal O_K=\mathbb Z[\zeta_5],\qquad
\mathfrak p_5=(1-\zeta_5).
\]

Choose the icosian order in the splitting

\[
B=K\oplus Ke,\qquad e x=\bar x e,\qquad e^2=-1,
\]

and a fivefold element \(\omega\) whose split matrix is

\[
M(\omega)=\operatorname{diag}(\zeta_5,\zeta_5^{-1}).
\]

The resulting labeled representation contains 120 determinant-one matrices.
The splitting basis itself is not integral: 100 of the 120 matrices have at
least one entry outside \(\mathcal O_K\). Conjugating by the explicit
orbit-lattice basis \(F_\Lambda\) gives an integral model
\(\rho'(2I)\subset M_2(\mathcal O_K)\). Its reduction modulo
\(\mathfrak p_5\) is faithful of order 120, and its
\(\mathbb F_5\)-linear span is all of \(M_2(\mathbb F_5)\).

## 4. The lattice criterion

In the fivefold eigenbasis, a basis matrix for the common lattice has the
triangular form

\[
F_\Lambda=
\begin{pmatrix}
1&a\\
0&b
\end{pmatrix},
\qquad
a=\frac{1+2\zeta_5+3\zeta_5^2-\zeta_5^3}{5}
=-\frac{\zeta_5^3}{1-\zeta_5},
\]

\[
b=\frac{2+4\zeta_5+\zeta_5^2+3\zeta_5^3}{5}.
\]

The two columns are exactly the split-coordinate images of the icosians
\(1\) and \(i\). Thus \(\Lambda=F_\Lambda\mathcal O_K^2\) is a named orbit
lattice, not an arbitrary common lattice.

For \(D=\operatorname{diag}(q_1,q_2)\),

\[
F_\Lambda^{-1} D F_\Lambda=
\begin{pmatrix}
q_1&a(q_1-q_2)\\
0&q_2
\end{pmatrix}.
\]

The only possible denominator in the off-diagonal entry is the single factor
\(1-\zeta_5\). Its determinant \(q_1q_2\) is a unit, so integral containment
already gives equality. Therefore, for units
\(q_1,q_2\in\mathcal O_K^\times\), on this explicit \(\Lambda\),

\[
\boxed{
D\Lambda=\Lambda
\quad\Longleftrightarrow\quad
q_1\equiv q_2\pmod{\mathfrak p_5}.}
\]

This is the direct proof. Finite sweeps over 1,600 unit pairs and 625 trace
tests in the companion program are audits only. The program also confirms
that the reduced integral `2I` image spans \(M_2(\mathbb F_5)\); that local
spanning check is supporting evidence for the integral model, not a second
proof of the displayed biconditional.

## 5. Determinant-one inverse pairs

Write

\[
D(q)=\operatorname{diag}(q,q^{-1}),\qquad
q=\zeta_{10}^{r}\varphi^n.
\]

Modulo \(\mathfrak p_5\), \(\zeta_{10}\equiv-1\) and
\(\varphi\equiv3\). Hence

\[
D(q)\Lambda=\Lambda
\Longleftrightarrow q\equiv q^{-1}
\Longleftrightarrow q^2\equiv1
\Longleftrightarrow n\equiv0\pmod2.
\]

The torsion exponent drops out. Since \(\varphi\) is real,

\[
\frac{q}{\bar q}=\zeta_5^r.
\]

Requiring the selected fivefold phase fixes \(r\equiv1\pmod5\). Up to the
center, inversion, and phase orientation, the first noncompact surviving
spinor step is

\[
q=\zeta_{10}\varphi^{-2}=-\zeta_5J^2,
\qquad J=\zeta_5\varphi^{-1}.
\]

Indeed, \(\zeta_{10}=-\zeta_5^3\), so the two expressions for \(q\) agree.
On diagonal light-cone coordinates the Hermitian action is

\[
D(q):(x_+,x_-)\longmapsto
(|q|^2x_+,|q|^{-2}x_-).
\]

Thus \(\eta=2\log|q|\) up to the chosen boost orientation. For
\(|q|=\varphi^{-2}\),

\[
|\eta|=4\log\varphi,
\qquad
\gamma=\cosh|\eta|
=\frac{\varphi^4+\varphi^{-4}}2=\frac72,
\]

\[
|v|=\tanh|\eta|
=\sqrt{1-\gamma^{-2}}=\frac{3\sqrt5}{7}.
\]

Equivalently, \(L_4=7\), \(F_4=3\), and
\(L_4^2-5F_4^2=49-45=4\).

The three levels must remain separate:

\[
q\in\mu_{10}\langle\varphi^2\rangle
\quad\text{on the spinor},
\]

\[
q^2\in\mu_5\langle\varphi^4\rangle
\quad\text{in the projective eigenvalue ratio},
\]

\[
\eta\in4\mathbb Z\log\varphi
\quad\text{in Lorentz rapidity}.
\]

For the primitive noncompact survivor,

\[
|\eta|=4\log\varphi,\qquad
\gamma=\frac72,\qquad
|v|=\frac{3\sqrt5}{7}.
\]

Within the frozen class, \(D_u\) with
\(u=\zeta_{10}\varphi^{-1}\) fails. The exact trace certificate includes

\[
\operatorname{tr}(gD_u)
=\frac{1-3\zeta_5+3\zeta_5^2+4\zeta_5^3}{5}
\notin\mathcal O_K
\]

for an explicitly enumerated \(g\in2I\). The same relative placement excludes
\(\operatorname{diag}(J,1)\). This does not touch its standard integral
\(\mathcal O_K^2\) realization described in section 2.

## 6. The spatial index is two-adic

Let \(\mathcal O^0\) be the trace-zero part of the chosen icosian order and
let \(L\) be the icosahedral vertex lattice. The audit constructs the full
order as the \(R\)-span of all 120 group elements, computes its exact trace
kernel, and verifies both that this kernel equals the \(R\)-span of the 30
trace-zero group elements and that \(L\subset\mathcal O^0\). The exact
inclusion has

\[
[\mathcal O^0:L]_{\mathbb Z}=16,\qquad
[\mathcal O^0:L]_{\mathbb Z[\varphi]}=(4),\qquad
N((4))=16.
\]

The integer inclusion matrix has determinantal divisors

\[
(1,1,2,4,8,16),
\]

and therefore integer Smith factors

\[
(1,1,2,2,2,2).
\]

Thus the quotient is killed by two and has 16 elements. Since
\(R=\mathbb Z[\varphi]\) is a PID and two is inert,
\(R/(2)\cong\mathbb F_4\); the quotient is a two-dimensional
\(\mathbb F_4\)-vector space. Hence

\[
\mathcal O^0/L\cong(R/(2))^2\cong(\mathbb Z/2)^4,
\qquad
\operatorname{SNF}_R=\operatorname{diag}(1,2,2).
\]

Equivalently, the determinantal ideals over \(R\) are
\(I_1=R\), \(I_2=(2)\), and \(I_3=(4)\).

The quotient is supported over two, so the current
\(\mathfrak p_5\)-adic criterion cannot distinguish \(L\) from
\(\mathcal O^0\). This does not make every boost intrinsically blind to the
two-adic difference. For the surviving element,

\[
q\bmod2=1+\zeta_5
\]

has order 15 in \(\mathbb F_{16}^\times\), and the induced matrix modulo two
is noncentral. A two-adic selector remains possible.

The next correct comparison must construct two complete four-dimensional
Hermitian or Clifford lattices whose spatial sections are respectively
\(L\) and \(\mathcal O^0\). Testing the spatial sections alone is not a
Lorentz-covariant comparison.

## 7. Hermitian compatibility and the trace-zero factor

For the surviving \(D=D(q)\), direct calculation in the lattice basis gives

\[
D\Lambda=D^*\Lambda=D^{-1}\Lambda=(D^*)^{-1}\Lambda=\Lambda,
\]

and

\[
D^*D^{-1}
=\operatorname{diag}(\zeta_5^{-1},\zeta_5)
=\rho(\omega^{-1})\in2I.
\]

Thus the concrete Hermitian constructions built from this lattice are
preserved. No definition-independent general identity for an unnamed
\(H(\Lambda)\) is asserted. For the column-tensor span one has
\(D H(\Lambda)D^*=H(D\Lambda)\); for the dual lattice of forms, the lattice
argument is \((D^*)^{-1}\Lambda\).

Let

\[
\delta=\zeta_5-\zeta_5^{-1},\qquad
\bar\delta=-\delta,\qquad
-\delta^2=2+\varphi.
\]

As an equality of vector spaces,

\[
\operatorname{Herm}_2^0=\delta M(B^0),
\]

and

\[
-\det(\delta M(x))=(2+\varphi)\operatorname{Nrd}(x),
\qquad x\in B^0.
\]

For the canonical involution, \(x\in B^0\) satisfies
\(M(x)^*=-M(x)\). Since \(\bar\delta=-\delta\), the matrix
\(\delta M(x)\) is Hermitian and traceless. Both sides have dimension three
over \(F\), so this injection is the stated vector-space equality. Moreover,

\[
-\det(\delta M(x))
=-\delta^2\det M(x)
=(2+\varphi)\operatorname{Nrd}(x).
\]

The companion audit checks the determinant identity on the 30 trace-zero
icosians. It does not prove equality of the corresponding integral lattices.
The factor \(2+\varphi=\varphi^2+1\) is also the quadratic norm of an
icosahedron vertex.

## 8. Candidate result

> **Diagonal lattice lemma [candidate-T / L1, frozen scope].** In the fixed
> split representation of the labeled `2I`, let \(F_\Lambda\) be the
> displayed matrix whose columns are the split images of \(1\) and \(i\),
> and set \(\Lambda=F_\Lambda\mathcal O_K^2\). In the eigenbasis of the fixed
> fivefold element, a diagonal unit step
> \(\operatorname{diag}(q_1,q_2)\in GL_2(\mathcal O_K)\) preserves this
> \(\Lambda\) exactly when
> \(q_1\equiv q_2\pmod{\mathfrak p_5}\).
>
> **Rapidity corollary [candidate-T / L1, additional frozen conditions].**
> Inside the determinant-one inverse pairs with the selected fivefold phase,
> the first noncompact survivor is
> \(q=\zeta_{10}\varphi^{-2}=-\zeta_5J^2\), with Lorentz rapidity magnitude
> \(4\log\varphi\). This selection is forced only up to the center, inversion,
> and phase orientation, and only after adding the fourth condition of section
> 1 to the three conditions of the lattice lemma.

This candidate does not alter the public meanings of
\(\log\varphi\) in `BOOST-COUNT-LADDER` or \(2\log\varphi\) in the regulator,
Mahler-measure, and toral-entropy statements. Those values concern different
objects.

## 9. Open obligations

- Decide whether the canonical update \(U\) belongs to the frozen class. Until
  then, the transfer prohibition remains absolute.
- Construct and compare complete four-dimensional lattices with spatial
  sections \(L\) and \(\mathcal O^0\) at the two-adic place.
- Prove or refute the integral-lattice version of
  \(\operatorname{Herm}_2^0=\delta M(B^0)\).
- Classify the admissible differently embedded or differently labeled `2I`
  placements before making any placement-independent statement.

## 10. Local audit program

The companion file is [`verify.py`](verify.py).
It uses only the Python standard library and exact arithmetic in
\(\mathbb Q(\zeta_5)\). Its 28 checks include exhaustive finite checks, direct
exact identities, and explicitly labeled finite audits. A failure exits with
status 1.

This local verifier is not a formal evidence directory, preregistration,
two-architecture computation gate, or probe. Any future public promotion must
start under a new formal `probes/P-NAME/` lane and follow `POLICY.md`; the
present files authorize no such move.
