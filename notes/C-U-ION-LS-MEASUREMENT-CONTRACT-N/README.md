# Joint-shot readout, mean sufficiency and the missing physical selection

**NON-CANONICAL; L1; conditional analytical note.** Date: 2026-10-05.
This note specifies the operational meaning of nonlinear processing of the
six connected LS responses. It supplies a finite mixture theorem and a
conditional code-subspace extension, not a calibrated apparatus, selected
Hodge decoder, public preregistration or scientific execution. Physical HOLD
and Canon v97 remain unchanged.

The [response-fibre classification](../C-U-ION-LS-RESPONSE-FIBRES-N/README.md)
and [conditional calibration specification](../C-U-ION-LS-CONNECTED-READOUT-N/CALIBRATION.md)
are local analytical inputs. The public physical model is
[#1371 at 723fc7d8](https://github.com/mathorn1973/twist-j/blob/723fc7d8da6a3cb9b626da31bbea247d15666d41/probes/P-U-ION-NATIVE-COMPRESSION-1/MODEL.md).
Its sections 2 and 8 specify symbolic fixed optical parameters and outstanding
device obligations. They do not supply a numerical light-shift profile or a
physically selected four-coordinate reading.

## 1. Independent profile and fixed record

Retain the original physical level dictionary, seven observed internal ions
(M1 and the six R1 coordinates), and the same seventeen-ion apparatus.
For a fixed profile define

$$
a_j=d_j-d_0,\qquad B=\sum_{i<j}(d_i-d_j)^2>0.
$$

The profile is to be determined from independently specified optical
frequencies, polarizations, geometry, beam ratio and calibration. The inherited
model schedules a common intensity scale; it provides no independent control
of all five d_j. Neither algebraic example profile from the fibre audit is an
actual device calibration or a justified optical choice.

Let alpha=(m,x_1,...,x_6) be a joint level outcome and put

$$
P_\alpha=|m,x_1,\ldots,x_6\rangle\langle m,x_1,\ldots,x_6|
\otimes I_{\rm rest},\qquad
z_k(\alpha)=a_m a_{x_k}/B.
$$

The ideal level projectors are a conditional measurement specification.
Their physical instrument has not been established. The admitted decoder
input is only the single-shot six-vector z. In particular it does not receive
the underlying level labels, counter, preparation label, horizon index or
separate local populations. Those may be retained for independently declared
preparation/control checks, but may not affect the decoded value.

For the finite response spectrum S, define its exact coarse projectors

$$
Q_z=\sum_{\alpha:z(\alpha)=z}P_\alpha,\qquad z\in S.
$$

They are mutually orthogonal and sum to identity. The six response operators
are Z_k=sum_z z_k Q_z. A fine level measurement followed by discarding the
extra labels has these response probabilities. It need not implement the
Lueders instrument of Q_z: the detector/environment may retain the discarded
labels and cause additional disturbance. No archive protection or repeated
nondestructive measurement follows from the effects alone. Separate horizon
endpoints require separate complete preparations unless an adequate instrument
and its disturbance have been supplied.

## 2. Processing joint outcomes before averaging

Fix a real four-vector function f on the entire admitted response spectrum,
including outcomes outside the seventy-five ideal checkpoints. Its physical
origin, units, amplitude scale and treatment of nonideal records must be
specified independently of the Hodge residuals. Define four score observables

$$
O_j=\sum_{z\in S} f_j(z)Q_z,\qquad j=1,\ldots,4.
$$

These are commuting Hermitian bounded operators; boundedness here follows
from finitely many finite scores, even if the retained unmeasured remainder
is infinite dimensional. They can be read statistically by applying f to
each joint response record and averaging the resulting four-vectors:

$$
\mathcal R_{\rm shot}(\rho)
=\sum_z f(z)\operatorname{Tr}(\rho Q_z)
=\bigl(\operatorname{Tr}(\rho O_j)\bigr)_{j=1}^4.
$$

Thus arbitrary nonlinear f is compatible with ordinary mixture-linearity:

$$
\mathcal R_{\rm shot}\left(\sum_i p_i\rho_i\right)
=\sum_i p_i\mathcal R_{\rm shot}(\rho_i).
$$

This is an immediate consequence of the POVM probability rule, not an
additional restriction forcing f to be affine in z. See
[Watrous, TQI, chapter 2, sections 2.1.2 and 2.3.1](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf)
for the standard state-mixture and measurement definitions; the particular
LS score construction and the finite theorem below are derived here.
The probability rule Tr(rho Q_z) is an adopted quantum measurement law for
this conditional apparatus description. It is not derived from the native
U or from J by the response construction or the mixture theorem.

On an ideal basis checkpoint the response is deterministic, so this reading
is simply f(z(X)). Consequently the earlier response-fibre test applies to
this conditional measurement directly. Nonlinear processing does not, by
itself, add a new entangling gate. It still needs the joint detector, copies,
classical records, fixed scoring rule and their resource/error accounts.

For an already fixed f, computing its empirical mean does not require
permanent storage of every shot. Four running sums

$$
S_j^{(K)}=\sum_{r=1}^{K}f_j(z^{(r)}),\qquad
\widehat{\mathcal R}_j=S_j^{(K)}/K
$$

and the sample count K>0 suffice for this arithmetic task, within the declared
numerical precision. Separate test groups require separate accumulators;
invalid records follow the fixed rule and are not silently discarded.
The score must be evaluated before information needed
by it is discarded. This statement supplies neither independent identically
distributed trials, convergence to an ensemble expectation nor confidence
bounds. Those need a separate preparation/statistical account. Fixed-precision
accumulators also need overflow and error bounds.

For a finite response alphabet, a histogram preserves the empirical average
of any subsequently evaluated fixed score; its availability does not make a
score chosen after seeing the test data target-independent. A histogram loses
ordering and is not a full record of a continuing machine's memory dynamics.
The mean-sufficiency obstruction specifies no minimal replacement statistic:
second moments, all pair correlations or state tomography do not follow as
necessary from that theorem. Extra records may also be needed for a declared
audit, uncertainty estimate or resource account.

## 3. Processing six averages is a different contract

The alternative procedure keeps only

$$
\mu(\rho)=\bigl(\operatorname{Tr}(\rho Z_k)\bigr)_{k=1}^6,
\qquad \mathcal R_{\rm mean}(\rho)=g(\mu(\rho)).
$$

It may be a legitimate nonlinear ensemble parameter, but is not generally
the expectation of the preceding fixed score observables. Even after
extending f to conv(S) and taking g to be that extension, the two procedures
are not generally identical:

$$
f\bigl(\mathbb E[z]\bigr)\ne\mathbb E[f(z)]
$$

in general. If g agrees with f on the checkpoint responses, the two coincide
there, so the old seventy-five-point audit cannot distinguish their mixture
semantics.
A finite-sample plug-in g(sample mean) also needs its own estimation/bias
analysis; its expected value is not automatically g(true mean).

The calibration of a connected Ramsey phase is another ensemble protocol.
Access to that phase or to six estimated means alone does not supply a
simultaneous single-shot z record. The detector branch of this contract
must be established explicitly.

## 4. Exact theorem: when six means suffice for a shot-score expectation

List the distinct checkpoint response points z_1,...,z_N. Let h_i=f(z_i),
Z=[z_1 ... z_N], H=[h_1 ... h_N] and

$$
T=\begin{pmatrix}\mathbf1^T\\ Z\end{pmatrix}.
$$

Declare for this proposition the **full probability simplex** over this
finite family, including mixtures of different horizon checkpoints. The
following conditions are equivalent:

1. Some fixed function g satisfies Hp=g(Zp) for every such probability p.
2. ker(T) is contained in ker(H).
3. There exist common coefficients c in R^4 and A in R^(4x6) such that
   H=c*1^T+A*Z.

**Proof.** For v in ker(T), decompose v=v_+-v_- into nonnegative parts.
If v is nonzero, the parts have the same strictly positive mass t because
1^T v=0. The two probabilities p_+=v_+/t and p_-=v_-/t have the same
response mean. Condition 1 forces Hp_+=Hp_-, hence Hv=0. This proves
1=>2. The inclusion of kernels gives a linear map on im(T) sending Tp to
Hp; extend it linearly to R^7 to obtain [c A]. This proves 2=>3. Condition
3 supplies g(z)=c+Az on the convex hull and proves 3=>1. No continuity,
smoothness or other regularity assumption is used.

The affine conclusion is about these finite score values and g on their
convex hull. It does not constrain f outside the checkpoint set or assert
an operator identity on the whole Hilbert space.
The affine map is uniquely determined on aff{z_i}. Its extension coefficients
(c,A) on all of R^6 need not be unique: that uniqueness holds exactly when
aff{z_i}=R^6, equivalently rank(T)=7. Otherwise two extensions may differ by
any affine map vanishing on the affine hull. "Common" means shared across
all checkpoints, not uniquely determined outside their affine hull.

Apply the preceding affine obstruction at a fixed profile with

$$
a_1a_2(a_1-a_2)\ne0.
$$

If the scores satisfy all original two-step Hodge edge equations AND the
mean-sufficiency condition above, then h_i=0 at every checkpoint. Equivalently,
every compatible shot-score reading that is nonzero on this checkpoint family
in this profile class must
distinguish at least two mixtures having identical six response means.
The signed-kernel construction in the proof supplies such a pair once the
independently chosen scores are known.

This is a conditional consequence, not a reason to impose mean-sufficiency.
Quantum mixture-linearity alone never supplied condition 1.

Cross-boundary mixtures are a separately declared preparation domain; their
physical availability is not established by the ion first-step proof. If
mixtures are admitted only within each boundary n, the argument supplies
separate affine representations on those boundary-specific convex hulls,
with agreement on intersections when the same g is used. It need not supply
one global c,A, and the above affine no-go cannot then be invoked on that
basis alone. For example g(x)=|x| is affine on each of [0,1] and [-1,0],
but not on their combined interval.

## 5. Conditional extension from checkpoints to code states

Let C_n be the span of the twenty-five complete orthonormal internal basis
checkpoints at boundary n and let Pi_n project onto it. Suppose an actual
unitary coherent evolution has independently been established with

$$
V_n|X_n(s,t)\rangle=e^{i\theta_{n,s,t}}|X_{n+1}(s,t)\rangle,
\qquad n=1,2,
$$

and the stated treatment of the physical remainder. This is an additional
assumption: the passive-archive continuation is currently a mathematical
target, not a synthesized ion evolution.

The score operators are diagonal in these complete basis states. Therefore
the basis-value identities h_(n+1,s,t)=L_H h_(n,s,t) imply componentwise

$$
\Pi_n\left(V_n^\dagger O_j V_n-
\sum_k (L_H)_{jk}O_k\right)\Pi_n=0.
$$

Indeed all off-diagonal matrix elements vanish and the diagonal ones are
exactly the basis-value equations; the phases cancel. Expectations then
obey the same step for every density operator supported on C_n, including
coherences and mixtures. This extension is a consequence of the assumed
coherent basis mapping and diagonal measurement, not independent evidence
for either of them.

In fact the stronger restricted-action identity also follows:

$$
\left(V_n^\dagger O_jV_n-\sum_k(L_H)_{jk}O_k\right)\Pi_n=0.
$$

Each output basis vector is an eigenvector of O_j, and applying V_n^dagger
returns the corresponding input basis vector. Thus no off-code component
is left by this action. The restriction to Pi_n is essential. Diagonal score
measurements by themselves do not certify that coherence was preserved.

For correlated or retained remainder states an analogous claim needs the
corresponding joint support and joint evolution to be proved. The internal
formula alone cannot silently certify those physical degrees of freedom.
No global identity V^dagger O V=L_H O on the whole apparatus is asserted.
Thus the earlier bounded-observable global hyperbolic obstruction is not
evaded or contradicted by this finite code-domain statement.

### Instrument and retained record for a measured continuation

To continue the same apparatus after a measurement, supply a quantum
instrument: completely positive maps I_z whose sum is trace preserving,
with the declared input and output physical systems and

$$
\operatorname{Tr}\mathcal I_z(\rho)=\operatorname{Tr}(\rho Q_z).
$$

For p_z=Tr I_z(rho)>0, the conditional postmeasurement state is
rho'_z=I_z(rho)/p_z. Including a classical result register C gives the joint
output

$$
\Omega'=\sum_z\mathcal I_z(\rho)\otimes|z\rangle\langle z|_C.
$$

These are the standard instrument definitions in
[Watrous, chapter 2, section 2.3.2](https://cs.uwaterloo.ca/~watrous/TQI/TQI.2.pdf).
They specify a mathematical channel, not a free physical supply of blank
record registers, laser work, detector readiness or resets. The output
system must include the data, occupied archive and retained degrees needed
for the next physical step, or justify explicitly why a traced-out part is
irrelevant. Existing records and correlated inputs must be treated jointly.

The next apparatus map acts on this actual joint output and the explicitly
supplied resources. It cannot replace rho'_z by rho without a justified
operation or invariance statement. If later feedback uses C or the quantum
postmeasurement state, that dependence belongs to the declared dynamics;
faithfulness to the same native U must then be checked anew on the admitted
domain. Access to a record by a controller does not automatically authorize
its use by the restricted six-response decoder.

For illustration of the underdetermination by effects alone, both
I_z(rho)=Q_z rho Q_z and I_z(rho)=Tr(rho Q_z) sigma_z for any fixed output
states sigma_z have effects Q_z. Their postmeasurement behavior can differ
radically. These are mathematical examples, not proposed ion instruments;
in particular replacement states have preparation and reset costs.

Endpoint measurements on separately prepared copies and successive
measurements of one continuing apparatus are therefore distinct contracts.
The first can test endpoint response relations without establishing the
second. The code-domain identities above describe the unmeasured coherent
evolution under their assumptions; inserting an instrument requires an
additional argument for the actual measured sequence.

## 6. What can actually be fixed now

The following contract is operationally specified in form but has unresolved
physical inputs. It is **not** a completed preregistration ready for a run.

| Contract item | Present source support / missing input |
| --- | --- |
| Profile and geometry | Fixed symbolic d,c,eta,delta and intensity constraints; numerical calibration and its independent apparatus choice are missing |
| Observation | Conditional joint level effects, exact map alpha->z and no extra decoder inputs are specified; implemented detector/instrument and error model are missing |
| Postmeasurement continuation | Choose separate endpoint copies or the same continuing apparatus; for the latter supply I_z, joint record/output state, resources and the next map on that output |
| Processing | Joint-shot scoring and six-mean processing are now explicitly different contracts; neither supplies a privileged f or g |
| Physical coordinates | Their independent meaning, units, scale and rule choosing a decoder or equivalent family are missing |
| Continuation | The original first step is conditionally compiled; occupied-memory n=1->2->3 is still only a mathematical target |
| Test domain | Seventy-five checkpoints and fifty edges are fixed; mixtures, new preparations and longer histories require explicit separate domains |
| Statistical decision | A minimum nonzero axial signal, tolerated errors, calibration propagation, sample counts and fixed acceptance rule remain to be supplied |

An independently justified family of decoders is permitted. If its members
give physically different predictions in the same admitted context, selecting
one requires an independent rule, or a proof of physical equivalence, or an
explicitly unresolved/set-valued conclusion. The Hodge edge equations may
test the independently specified choices; they do not determine the optical
profile or initial score vectors as part of their calibration.

The complete score rule must cover all admitted detector outcomes, with a
fixed treatment of leakage and invalid records. Returning only a fitted
table of twelve scores, or adapting to n via an external lookup, does not
complete this physical specification. Analysis may group records by the
declared test preparation/boundary to compare predicted transitions; the
decoder itself remains fixed and cannot use those labels.

Once the missing physical inputs are supplied, the next comparison is
concrete: evaluate the fixed scores at the response classes and check all
fifty edge equations and the independently fixed nonzero-signal criterion.
One does not solve those equations to choose the scores. No such independent
numerical profile or score rule exists in the inspected source materials,
so this note reports the unresolved physical selection rather than inventing
one.

## 7. Generic algebra is distinct from admissible apparatus profiles

The positive rational example alone would not prove genericity. The earlier
note also supplied the symbolic argument: its twelve nonzero response rows
are distinct polynomials, as their simultaneous distinctness at the displayed
example confirms. Every undesired equality is therefore a proper polynomial
zero set. Outside their finite union there are four independent two-edge
paths and sixteen scalar degrees of finite compatible assignments. This
holds on an open dense, full-Lebesgue-measure subset of the unrestricted
four-dimensional centered-profile space.

A physically admissible family can lie entirely inside the exceptional
set, or the actual apparatus may have only one fixed profile. No generic
claim about those apparatus families follows without their independently
specified parameter map and domain.

## 8. Verification and status

The results above use only explicit operator definitions and finite linear
algebra. No scientific verifier, mixture experiment, calibration or pulse
compiler was executed. No public source, claim status, GitHub branch or
Canon file was changed. Static review is recorded in [REVIEW.md](REVIEW.md).
