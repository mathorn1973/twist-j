# A connected light-shift response and its Hodge-reading boundary

**NON-CANONICAL; L1; candidate-T conditional analytical result.**
Date: 2026-10-05. This note derives six joint response observables from the
already adopted seventeen-ion Hamiltonian, without fitting the Hodge target.
For an explicitly stated nondegenerate light-shift profile, no fixed affine
conversion of these responses gives a nonzero four-dimensional Hodge reading
on the three-boundary passive-archive family. No new scientific program,
laboratory experiment or pulse compilation was run. Canon v97 and the
physical HOLD remain unchanged.

The native checkpoint family and Hodge target were already known before
this derivation. Target independence here means that the response formula
and calibration rule use the admitted physical quantities, not coefficients
fitted to that target. This is not a blind test or an unseen-data success.

The positive result is a physically specified *candidate response*, not a
constructed measurement apparatus or a successful Hodge identification.
[CALIBRATION.md](CALIBRATION.md) separates the response, its proposed
measurement and the unprovided device calibration. [REVIEW.md](REVIEW.md)
records the independent analytical checks and their limits.

## 1. Fixed inputs and source scope

The source model is [#1371 MODEL.md at its result pin](https://github.com/mathorn1973/twist-j/blob/723fc7d8da6a3cb9b626da31bbea247d15666d41/probes/P-U-ION-NATIVE-COMPRESSION-1/MODEL.md).
It adopts one real, fixed, nonscalar five-level light-shift profile
D_i=diag(d_0,...,d_4), complex geometric factors c_i, eta>0 and delta>0.
Ion 14 is M1, and ions 2,...,7 are the six R1 coordinates. On these edges
g_k=Re(c_14 conjugate(c_k)) is nonzero. A raw closed LS loop has

$$
A=\lambda\sum_i c_iD_i,\qquad
U_{\rm loop}=\exp[-i\Theta]\otimes I_{\rm motion},\qquad
\Theta=\kappa AA^\dagger+\sum_i L_i,
\quad \kappa=\frac{\pi\eta^2}{2\delta^2}.
$$

The L_i are the source's stationary integrated diagonal local residuals at
the chosen intensity. The loop lasts 2pi/delta and acts globally. Its pair
terms are not available as isolated interactions for free.

For the comparison dynamics, retain the source's original U on both
receivers, its fixed R2 dictionary y=q-1 mod5, passive M1=s and M2=1,
unchanged S1=1 and S2=t, and the boundaries N=1,2,3. The additional two
steps are a specified partial mathematical continuation, not an inherited
ion implementation. They are derived by substitution into the [pinned
native branches](https://github.com/mathorn1973/twist-j/blob/723fc7d8da6a3cb9b626da31bbea247d15666d41/probes/P-U-ION-NATIVE-COMPRESSION-1/PROOF.md#1-fixed-carrier-inputs-and-complete-target):

| s | R1 at n=1 | R1 at n=2 | R1 at n=3 |
| --- | --- | --- | --- |
| 0 | (0,0,0,0,0,0) | (2,1,2,1,1,0) | (0,0,1,3,1,1) |
| 1 | (0,0,0,0,4,0) | (0,0,0,0,1,0) | (2,1,3,4,0,1) |
| 2 | (2,1,2,1,4,0) | (0,0,0,0,2,0) | (2,1,3,4,0,1) |
| 3,4 | (2,1,3,4,3,1) | (2,1,3,4,2,4) | (0,0,0,0,4,2) |

For every s,t the R2 physical tuples are (0,0,0,0,3,0),
(0,0,0,0,0,0), (2,1,3,4,4,1). The response considered here does not read
S2, R2 or N; the five distinct s histories suffice for every fixed t.
The three times are not silently treated as one invariant state sector.

Use the fixed-direction Hodge restriction from [Canon v97](https://github.com/mathorn1973/twist-j/blob/82ecf0aac0ee79c947000968e71573d4c65d386d/canon/CANON.md#j-hodge-semilinear-memory-t).
In a real embedding and a suitable basis it is similar to

$$
\widehat L=
\begin{pmatrix}
\phi&-1&0&0\\1&0&0&0\\0&0&3&-1\\0&0&1&0
\end{pmatrix},\qquad \phi=(1+\sqrt5)/2.
$$

In particular L and I-L are invertible. The source's four-dimensional
minimum is for one marked direction and K-linear prediction, K=Q(sqrt5).
It is not a physical-time identification. The proof below permits arbitrary
real decoder coefficients, so it also covers K-valued specializations.

## 2. Derivation before the Hodge comparison

Expanding the phase generator gives

$$
AA^\dagger=\lambda^2\left[
\sum_i |c_i|^2D_i^2+
2\sum_{i<j}{\rm Re}(c_i\overline{c_j})D_iD_j\right].
$$

Fix a memory level m and a level x of one partner k; keep every other
label, intensity, duration and stationary local profile fixed. Let
Theta(m,x) denote the eigenvalue of the full generator for that setting.
The mixed contrast relative to the physically distinguished level 0 is

$$
\begin{aligned}
C_k(m,x)&=\Theta(m,x)-\Theta(m,0)-\Theta(0,x)+\Theta(0,0)\\
&=2\kappa\lambda^2g_k(d_m-d_0)(d_x-d_0).
\end{aligned}
$$

All single-ion, spectator and spectator-pair terms cancel. Local residuals
cancel too. This is an exact algebraic contrast across four settings;
it is not an assertion that one raw loop isolates the edge.

Set a_j=d_j-d_0, a_0=0, and

$$
B=5\sum_jd_j^2-\left(\sum_jd_j\right)^2
 =\sum_{i<j}(d_i-d_j)^2>0.
$$

A dimensionless connected-response observable is therefore

$$
\boxed{Z_k=\frac{(D_{M1}-d_0I)(D_{R1,k}-d_0I)}{B}.}
$$

The reference, common profile, geometric edge and normalization are fixed
by the model and calibration, independently of L. These six commuting
diagonal operators are generally not equality projectors. For example,
different nonzero levels need not give zero response.

At the source's allowed intensity
lambda_k=delta/[eta sqrt(50B|g_k|)],

$$
C_k(m,x)=\frac{\pi\,\operatorname{sgn}(g_k)}{50}
          \frac{a_ma_x}{B}.
$$

The unitary phase is -C_k under the exp(-iTheta) convention. Since
|a_j|^2<=B, |a_ma_x|/B<=1, so the ideal connected phase has magnitude at
most pi/50. Its principal phase has no modulo-2pi ambiguity at this
intensity. Extracting it with finite precision still requires a measurement
and error account; the bound does not supply those.

The already completed 500-loop refocusing block instead has generator
scalar plus pi sign(g_k) E_k/2, returning the equality-projector family.
A mixed contrast of that refocused generator also introduces local
zero-level indicators; it must not be called the same six-E affine class.
No new refocusing word is proposed here.

## 3. A fixed-profile obstruction for the entire affine decoder class

On the code states, Z_k=a_s a_(R1,k)/B. Consider the deliberately enlarged
class of all fixed affine conversions

$$
\mathcal R(X)=c+\sum_{k=1}^6 v_k a_s a_{R1,k},\qquad
c,v_k\in\mathbb R^4.
$$

The common B and any known nonzero edge response factors have been absorbed
into v_k. The coefficients may depend on an independently calibrated profile,
but are fixed across preparations and times. Allowing arbitrary coefficients
strengthens the negative result; solving for them is not proposed as an
acceptable physical calibration.

**Conditional proposition.** If

$$
\boxed{(d_1-d_0)(d_2-d_0)(d_1-d_2)\ne0,}
$$

then intertwining R(X_(n+1))=L R(X_n) for every s and n=1,2 forces
R=0 on all fifteen checkpoints at fixed t, hence on all seventy-five
supplied checkpoints. This is a pointwise condition on a single profile,
not a requirement that one decoder work uniformly over an open family.

**Proof.** The s=0 archive has a_s=0, hence R=c at every time. Since I-L
is invertible, c=0. Write

$$
H=a_2v_1+a_1v_2+a_3v_3+a_4v_4+a_1v_6.
$$

The s=1 and s=2 histories have the same R1 tuple at n=3. Their readings
at n=2 and n=3 are respectively

$$
(a_1^2v_5,a_1H),\qquad(a_2^2v_5,a_2H).
$$

Because a_1,a_2 are nonzero, both update equations imply

$$
H=a_1Lv_5=a_2Lv_5.
$$

Now a_1!=a_2 and invertibility of L give v_5=H=0. Those two histories
have zero readings at every boundary, using invertibility to go back to
n=1. For s=3,4 the first tuple is (2,1,3,4,3,1), giving

$$
\mathcal R(X_1^{(s)})=a_s(H+a_3v_5)=0.
$$

Their next two readings are zero by intertwining. Together with s=0 this
proves the assertion. No assumption about a_3-a_4 was needed.

The conclusion concerns values on the declared family. It does **not**
say that every coefficient v_k vanishes, or that the resulting observable
vanishes on the entire Hilbert space. It covers all four Hodge coordinates,
not only the axial recurrence.

## 4. Necessary qualifications and exceptional profiles

The source assumes only a nonscalar d. It does not imply the boxed
nondegeneracy condition. No numerical device profile has been supplied.
In particular, equal shifts of different D levels are admissible. If
d_3=d_4, these unrotated six responses cannot distinguish the archived
collision at any of the three times, irrespective of the affine decoder.

A further necessary condition follows without parameter-uniformity. If
a_1!=0, the s=1 first transition gives

$$
(a_1I-a_4L)v_5=0.
$$

If this matrix is invertible, the preceding proof again forces every
checkpoint reading to zero. The periodic eigenvalues of L are nonreal;
therefore a nonzero reading with a_1!=0 requires

$$
a_4\ne0,\qquad a_1^2-3a_1a_4+a_4^2=0,\qquad
a_2\in\{0,a_1\}.
$$

These are necessary, not sufficient, conditions. They do not authorize
tuning a light-shift ratio to the desired Hodge eigenvalue. Profiles with
a_1=0 or the other displayed degeneracies require a separately stated
analysis based on independently fixed calibration.

The qualification is real: there are target-fitted algebraic solutions.
For a=(0,0,0,1,2), arbitrary w in R^4 and the same L, choose

$$
c=v_1=v_2=v_4=0,\quad v_5=\tfrac12L^2w,\quad
v_3=w-\tfrac12L^2w,\quad
v_6=\tfrac12(Lw-w+\tfrac12L^2w).
$$

Hand substitution gives zero for s=0,1,2; for s=3 it gives
(w,Lw,L^2w), and for s=4 twice that sequence. This example uses
unnormalized a_sa_x; common B is absorbed into the coefficients. It proves
that an all-profile prohibition would be false. The coefficients explicitly
encode L and the target trajectory, so this is an interpolation control,
not a physically derived decoder or a claimed experimental profile.

Nonlinear conversions of responses, different fixed local frames,
additional observables, uncentered or unsubtracted local contributions,
and active predictive memory are outside the proposition. Any such
successor needs its own independent physical selection rule. The theorem
does not cover arbitrary sine/cosine Ramsey signals just because they
are functions of the same phase.

## 5. Consequence for the next decision

The adopted interaction supplies a natural joint response and an
independently defined normalization. It supplies no privileged four-vector
decoder. For profiles satisfying the boxed condition, even allowing every
affine decoder cannot produce a nonzero Hodge state on the stated horizon.
For degenerate profiles, algebraic solvability alone may be target fitting.

There is therefore no successful Hodge candidate here to send to pulse
compilation or to label a new preregistered success. A future device claim
must first provide the independent profile/geometry calibration and actual
measurement contract in CALIBRATION.md. If it uses a different response
class, that class and its decoder must be fixed before target comparisons.
All present results are analytical; no verifier stdout, calibration data,
resource count for a new apparatus, or completed scientific run is claimed.
