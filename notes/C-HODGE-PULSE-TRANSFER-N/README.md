# One local relation, two readings: pulse transfer and the Hodge carrier

**C-HODGE-PULSE-TRANSFER-N. NON-CANONICAL. L1 mathematical comparison.**

Author: A. M. Thorn. Publication lock: [#1712](https://github.com/mathorn1973/twist-j/issues/1712).
Proof-derived results below are **candidate-T** at their stated algebraic scope;
the local computational witnesses are **candidate-C**. This is a result-exposed
research note, not a public preregistration, a Canon fold, or a physical theorem.
The proposed extension in section 7 is a question, not an established result.

## 1. The proposed connection and its sources

The working thesis is that a local amplitude relation can have both a unitary
input/output description and a boundary-transfer description. The latter can
have a Lorentzian quadratic reading without being a new time-evolution law.
For the pulse block already supplied by the homogeneous-capture construction,
its marked positive transfer factor has exactly the hyperbolic factor of the
registered J-Hodge carrier. Separately, its finite reduction has an explicit
comparison with the registered trace-kernel grading and metric.

The demonstrated connection stops at these statements. We have not identified
the complete pulse or capture dynamics with the complete J-Hodge action.
In particular, the missing rotation must not be inserted to obtain the target.

Three sources are kept distinct:

* **Public Canon v104** supplies `J-HODGE-HERM2-LOXODROME [T]`, the marked
  `A4-RAMIFIED-HODGE-TRACEKERNEL [T]` construction, and the explicit finite
  bracket and grading of `TRACEKERNEL-F5-HODGE-BRACKET [T]`. The latter's
  architectural interpretation retains its registered closure premise.
* **Draft PR #1711**, at the pinned commit in [SOURCES.md](SOURCES.md), supplies
  the non-canonical first-order candidate `h_plus=3g5` for the **unimodular**
  wedge pairing and the real-field uniformizer `sqrt(5)`. It is not a new
  canonical input.
* **Handoff draft PR #33**, also pinned, supplies the chosen pulse block, the
  separate capture contact, and its receiver construction. Its packet theorem
  is not reproduced here. None of its physical or dynamical selection debts is
  discharged by this comparison.

No existing source, probe, reading family, or open owner is modified. The
identity of the symbol `J` in the arithmetic must not be confused with the
receiver's label-swap operator, which is an involution.

## 2. The pulse relation and the marked boundary regrouping

**[candidate-T, exact two-port algebra]** Let

$$
 c=\frac1{\sqrt5},\qquad s=\frac2{\sqrt5},\qquad
 Q=\begin{pmatrix}c&-s\\s&c\end{pmatrix}.
$$

These are the pulse coefficients of the pinned capture source, not values
chosen in this note to match the Hodge target. The complete free pulse step
there is `V(k)=E(k)Q`, with edge phases in `E(k)`; `Q` alone is not that step.

For arbitrary complex amplitudes, write the single relation

$$
 a_{\rm out}=c a_{\rm in}-s b_{\rm in},\qquad
 b_{\rm out}=s a_{\rm in}+c b_{\rm in}.
$$

Solving the same equations for a different pair of dependent variables gives

$$
 \binom{b_{\rm out}}{b_{\rm in}}
 =T\binom{a_{\rm in}}{a_{\rm out}},\qquad
 T=\frac1s\begin{pmatrix}1&-c\\c&-1\end{pmatrix}.
$$

This fixes the port ordering, signs, and which data are treated as dependent.
The equivalence uses `s != 0`; it neither adds a state nor advances a clock.
The two sides contain both incoming and outgoing amplitudes. Thus `T` is a
boundary relation, **not** the unitary time update `Q`, the pulse walk `V(k)`,
the scattering matrix, or the complete capture law.

Put

$$
 Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
 B=\frac12\begin{pmatrix}\sqrt5&-1\\-1&\sqrt5\end{pmatrix}.
$$

Direct multiplication proves

$$
 Q^\dagger Q=I,\quad T=ZB,\quad
 T^\dagger ZT=Z,\quad T^2=I,\quad \det T=-1,\quad
 T^\dagger T=B^2,\quad \det B=1.
$$

On the independent vectors `(1,-1)` and `(1,1)`, `B` acts respectively by
`phi=(1+sqrt(5))/2` and `phi^-1=(sqrt(5)-1)/2`. Both are positive, so `B`
is precisely the positive polar factor of this **marked** transfer matrix.
The full `T` is an involution: its eigenvalues are not `phi,phi^-1`.

## 3. What agrees with the Hodge action

**[candidate-T, specified Hermitian congruence]** Define

$$
 X(t,x,y,z)=\begin{pmatrix}t+z&x-iy\\x+iy&t-z\end{pmatrix},\qquad
 \det X=t^2-x^2-y^2-z^2.
$$

The specified action `X -> B X B^dagger` is

$$
 (t,x,y,z)\longmapsto
 \left(\frac{3t-\sqrt5x}{2},
       \frac{-\sqrt5t+3x}{2},y,z\right).
$$

Its coefficient matrix preserves `diag(1,-1,-1,-1)` and has polynomial

$$
 (\lambda^2-3\lambda+1)(\lambda-1)^2.
$$

Consequently its hyperbolic pair is `phi^2,phi^-2`. This is exactly the
hyperbolic factor of the registered J-Hodge action on the marked `E_J`, whose
**complete** polynomial is

$$
 (\lambda^2-3\lambda+1)(\lambda^2-\varphi\lambda+1).
$$

The compact factor, with eigenvalues `zeta_10,zeta_10^-1`, is absent from the
polar action. The whole `T` congruence is itself involutory, so it cannot be
conjugate to this loxodrome either. Multiplying a matrix by a unit-modulus
scalar does not supply the missing factor: that scalar cancels in
`X -> A X A^dagger`.

This is a factor comparison with the mathematical Hodge carrier, not a
canonical identification with a physical Hermitian carrier. No time or
spatial interpretation is assigned to `t,x,y,z` here.

## 4. The finite-field comparison is explicit, but is a different action

**[candidate-T, marked residual algebra]** Work over the real field
`F=Q(sqrt(5))` and the ring `Z[phi,1/2]`. The entries of `B` are in this ring.
Reduction at its ramified prime `(sqrt(5))` gives

$$
 \overline B=\begin{pmatrix}0&2\\2&0\end{pmatrix},\qquad
 \det\overline B=1,\qquad \overline B^2=-I.
$$

Conjugation `Ad(Bbar):Y -> Bbar Y Bbar^-1` on `sl_2(F5)` is an involution
with plus and minus dimensions one and two. To compare it with the registered
`W5`, use the difference-coordinate vectors

$$
 h=(1,0,1)^T,\quad e=(1,4,3)^T,\quad f=(3,4,1)^T,
 \qquad M=(h\ e\ f),
$$

and the registered Gram

$$
 G_5=\begin{pmatrix}2&4&0\\4&2&4\\0&4&2\end{pmatrix}.
$$

The explicit bracket `G5^-1(v cross w)` satisfies
`[h,e]=2e`, `[h,f]=-2f`, `[e,f]=h`. Define `Psi0` by sending this displayed
basis to `diag(1,-1), E12, E21`. Now set

$$
 P=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
 \Psi(v)=P\Psi_0(v)P^{-1}.
$$

All expressions in this paragraph are over `F5`. Direct computation gives

$$
 P^{-1}\overline B P=\operatorname{diag}(2,3),\qquad
 \operatorname{Ad}(\overline B)\Psi=\Psi\Phi,\qquad
 \Phi=\begin{pmatrix}0&4&1\\0&4&0\\1&4&0\end{pmatrix}.
$$

Thus the comparison uses a stated conjugacy, not equality of dimensions or
an inferred apparatus choice. **This is the registered `Phi` grading, not
the exterior-square J-step `D`.**

Also, the real Hermitian action in section 3 is a **congruence**; the action
here is an **adjoint conjugation**. This note does not identify them as one
star-preserving arithmetic reduction. A compatible lattice and reduction of
complex conjugation must be supplied before such an assertion. The displayed
real-field reduction of `B` alone is not that missing theorem.

## 5. The trace form meets the first-order candidate exactly

**[candidate-T, finite bilinear identity and conditional composition]** The
matrix-trace pairing in the `(h,e,f)` chart has Gram

$$
 G_{\rm tr}^{hef}=\begin{pmatrix}2&0&0\\0&0&1\\0&1&0\end{pmatrix}.
$$

Transforming to the public difference basis gives

$$
 M^{-T}G_{\rm tr}^{hef}M^{-1}
 =\begin{pmatrix}1&2&0\\2&1&2\\0&2&1\end{pmatrix}=3G_5.
$$

Therefore, for all `v,w in W5`,

$$
 \operatorname{tr}(\Psi(v)\Psi(w))=3g_5(v,w).
$$

Conjugating `Psi0` by `P` does not change the trace. Equality on all nine basis
pairs proves the displayed bilinear identity for all vectors. It also follows
from the existing marked `Killing=2g5` identity and the `sl2` identity
`Killing=4tr`, since `2/4=3` in `F5`.

Under the **candidate** first-order relation in PR #1711, this says

$$
 h_+(v,w)=\operatorname{tr}(\Psi(v)\Psi(w)).
$$

This last step retains that candidate's status and exact normalization:
unimodular wedge pairing, the real-field uniformizer `sqrt(5)`, and the
specified comparison with `W5`. It does not replace the similarity `h_+=3g5`
by an isometry with `g5`, and does not eliminate its uniformizer dependence.
Nor is it an identification with the positive native charge or apparatus
probability. These are two particular finite-field bilinear forms.

## 6. Negative controls that constrain the interpretation

**[candidate-T, exact limitations]** A different signed regrouping of the
same pulse equations is

$$
 \binom{a_{\rm in}}{-b_{\rm out}}
 =\frac1c\begin{pmatrix}1&-s\\-s&1\end{pmatrix}
  \binom{a_{\rm out}}{-b_{\rm in}}.
$$

Its positive eigenvalues are `phi^3,phi^-3`. The pulse by itself therefore
does not pick the first regrouping. The port convention is part of this
comparison and needs its own operational justification for a physical claim.

For the **new capture contact**, the source instead specifies
`c_*=3/5, s_*=4/5`. Applying the original regrouping gives

$$
 B_*=\frac14\begin{pmatrix}5&-3\\-3&5\end{pmatrix},\qquad
 \operatorname{Spec}(B_*)=\{2,1/2\}.
$$

The corresponding Hermitian polynomial is
`(lambda^2-(17/4)lambda+1)(lambda-1)^2`, not the Hodge factor. This does not
falsify the capture construction; it rules out this simple argument as a
selection of its new contact angle from J.

Finally, the capture model is one-dimensional in position. Three components
of a quadratic internal or boundary reading do not establish three physical
spatial coordinates. Positive charge `H_N`, Hilbert norm, boundary flux,
Lorentz determinant, and spectral energy `i Log W` are different objects.
No equality between them follows from the displayed local identities.

## 7. One formulated next question, not an extra conclusion

The source hypotheses motivate testing the following **unestablished**
connection: an independently specified boundary reading of actual pulse,
edge, contact, and receiver relations might realize the complete Hodge
modulus and relative phase, with compatible integral and residual forms.

A successor must freeze the source boundary-data carrier, port convention,
allowed gate words, phase data, observation context, and equality before
comparison. The transfer operator must be derived from those actual source
relations. Merely multiplying `B` by a target-designed rotation is not a
positive result. Discarding a polar factor, channel, or label also requires an
explicit source-side reading; it cannot be justified only by the match.

For a fixed declared context class, the test should seek an explicit map
`I` from the resulting four-coordinate boundary reading to the marked
`E_J`. It must check both an intertwining equation and a form equation,
with the target action and normalization fixed independently. In notation,

$$
 I\,R_{\rm boundary}(\xi)=L_J I,\qquad
 I^*\beta_{E_J}=q_{\rm boundary}
$$

on the **whole admitted context domain**, or a separately declared covariant
version with all context transports specified. The wedge signature is `(3,1)`,
whereas the displayed Hermitian determinant has signature `(1,3)`; the form
contract must fix the overall sign explicitly, not equate these unchanged
Grams. Matching just one selected
momentum or energy after seeing the target is not sufficient. Characteristic
polynomials are necessary tests, not substitutes for these maps. Reduction
at the designated prime must also transport the chosen lattice, form and
involution correctly, rather than substituting an adjoint for a congruence.

A finite exact counterexample can reject a frozen candidate map or word.
Rejection of the entire route requires a complete independently admitted
class. Missing definitions, an unselected phase, or failure of a particular
word is an unresolved test, not a new falsifier for the public frontier.

This is a test proposal, not an assertion that the map exists, is unique,
or acts as a clock. The capture receiver and occupied-record semantics must
remain intact. `TRACEKERNEL-CURVATURE-FORCING [O]` and all physical apparatus
owners retain their exact public scopes.

## 8. Reproduction and status

The two accompanying scripts are unchanged from the incoming local comparison
archive. `verify.py` audits nine exact groups with SymPy 1.14.0;
`trace_check.py` checks the nine bilinear basis pairs using integers.
Both were reviewed before execution and rerun on one Linux x86_64 lane, with
zero exit codes, empty stderr and byte-identical expected outputs. See
[RUN.md](RUN.md) and [SOURCES.md](SOURCES.md) for the exact custody record.

The signed alternative regrouping in section 6 is an explicit algebraic
expansion of the source note's convention caveat; it does not change its
operator or eigenvalues. The audit checks its stated matrix spectrum, while
the displayed two original equations provide its direct proof.

The scripts predate this publication. Their successful replay is
**reproduction, not independent confirmation**. No formal public probe pin or
two-architecture scientific gate is claimed. The notes-only repository checks
do not execute these scripts as registered scientific verifiers. The full
packet/scattering proof, the first-order candidate as a whole, and the future
map in section 7 are not rerun or proved here.

Run from the repository root in the documented environment:

```sh
python3 notes/C-HODGE-PULSE-TRANSFER-N/verify.py
python3 notes/C-HODGE-PULSE-TRANSFER-N/trace_check.py
```

A local script pass does not promote a candidate. Publication adds only this
note directory; Canon, registry, frontier, sealed probes and releases are
unchanged. [PROMO.md](PROMO.md) records the limited handoff and remaining debt.
