# K1 homogeneous FRW output at one marked point

**NON-CANONICAL / SELECTED WORKING DICTIONARY / ANALYTIC DERIVATION / NO FORMAL RUN**

```text
NOTE OBJECT:       V82-FRW-K1-HOMOGENEOUS-2JET-COMPOSITION-1
AUTHORITY BASIS:   Public Canon v82
BASE MAIN:         c596bfebd12bde3b15a3c3d378ca6b0f9c94608f
CANON TAG:         canon-v82
CONTENT COMMIT:    4e65adf0b483311d2a031cf2a23a65f2caf5af8a
CONNECTED OWNER:   FRW-INHOM [O], unchanged
OTHER OWNERS:      TT-SOURCE [O], TT-VECTOR-STATE-NORMALIZATION [O], unchanged
FORMAL PROBE:      NONE owned or executed by this note
RESULT:            a complete selected homogeneous 2-jet map and its proof
STATUS MOVE:       NONE
```

This independently scoped note completes the homogeneous *output* at one
marked FRW point. It does not retain an arbitrary old Hubble value while adding
positive K1 energy to its constraint. The additional homogeneous reading is
chosen explicitly below; it is not attributed to the frozen probe.

The separate probe `P-FRW-INHOM-K1-BACKREACTION-3`, issue #923, is pinned at
`1f3a3d5b074547991919ad52824d6c7f6f591550`. This note changes neither that pin,
its verifier, its gates, nor its ownership. Its eventual result must be read
from its own public records. No PASS or FAIL is assigned to it here.

## 1. Inputs and the composition problem

Use exactly `DEF-K1-LINEAR-METRIC`: the ten marked four-bit words, their two
unit-amplitude initial squares, and the recurrence

```text
h_(n+1) = (2I-L)h_n-h_(n-1),
L = [188I-29(S+S^-1)-65(S^2+S^-2)]/324.
```

For a selected adjacent pair, define the exact charge

```text
E(w) = (1/2)[ ||h_(n+1)-h_n||^2 + <h_(n+1),L h_n> ].
```

The recurrence and symmetry of L imply conservation. Indeed, put
`q=h_(n+1)-h_(n-1)` and `R=h_(n+1)-2h_n+h_(n-1)+Lh_n`. Polarization gives

```text
E_(n+1/2)-E_(n-1/2) = (1/2)<q,R> = 0.
```

For the unchanged K1 inputs, direct substitution in the displayed quadratic
form gives

| abs(u_1-u_0) | E(w) |
| --- | --- |
| 0 | 53/432 |
| 1 | 713/2592 |
| 2 | 67/162 |

For example, for `0011`, `h_0=h_1=f=(delta_1+delta_2)/2`. Thus
`<f,Lf>=(188/2-29/2)/324=53/216` and `E=53/432`.
For a displacement of one, `||h_1-h_0||^2=1/2` and
`<h_1,Lh_0>=65/1296`, giving `713/2592`. For a displacement of two,
these values are `1` and `-14/81`, giving `67/162`.
No weighted average or physical occurrence law is used.

The typed 3D embedding from the predefinition has `V0=<1,1>_V=5` and
preserves this E exactly. Its homogeneous source is `bar_e=E/V0`.
Consequently an unchanged vacuum background `H=rho_m=0` cannot absorb a
nonzero K1 word: the proposed lapse equation would read `0=E/(2V0)`.

The input here is therefore matter data and a source, not an independently
fixed Hubble value. Freeze the exact input domain

```text
(w, m, M, Q),
w one of the ten unchanged K1 words,
m in N_0 marks the adjacent source pair (h_m,h_(m+1)),
M in Q_(>=0), Q in Q,
M = lambda rho_m*, Q = lambda (partial_chi rho_m)*,
lambda = 216 pi, chi = log a.
```

The two matter jet entries are supplied independently of the target output.
No matter source is manufactured by adjusting them to a desired H. The
nonnegativity assumption is at the marked point; no energy condition on an
unspecified time neighbourhood is asserted. Neither a negative nor a positive
input H is carried over. A supplied negative-branch background belongs to a
different context, not to this selected reading.

The formal source-off restriction sets the TT field and E to zero. It is
used only to state the homogeneous restriction. It is not an eleventh K1
word, a changed source law, or an adjustable amplitude in the K1 domain.

## 2. The one new homogeneous variation rule

Choose a marked FRW point with `a*=1`, `chi*=0` and local proper-time gauge
`nu(t)=1`. This is a chart and lapse convention at the output. It does not
identify the discrete counter with measured cosmic time. Only the selected
half-slice label `m+1/2` is attached to the one output point `t=0`.

**Selected homogeneous dictionary rule:** in this variation, hold the marked
K1 packet, its reference stencil and normalization, and its derived charge E
fixed. Read the homogeneous TT lapse variation as a source variation in the
public FRW action. In particular `partial_chi E=0` in this comparison.
This is an added reading rule, not a theorem forcing how a physical TT field
changes under expansion.

The predefinition's homogeneous source term is
`-ell_0 E/(2 lambda)`, where `ell_0=nu-1` at the marked point. With the stated
rule, its homogeneous first variation at `ell_0=0` is

```text
delta S_K = -[E/(2 lambda)] delta nu + 0 delta chi.
```

The corresponding homogeneous FRW density term is
`-V0 nu exp(3chi) rho_K(chi)`. Write its density jet as `(C,C_chi)`.
At `chi=0,nu=1` its first variation is

```text
delta S_K = -V0 [ C delta nu + (3C+C_chi) delta chi ].
```

Matching the two coefficients uniquely gives

```text
C = E/(2 lambda V0) = E/(10 lambda),
C_chi = -3C,
p_K* = -C-C_chi/3 = 0.
```

Thus the derivative and the zero homogeneous pressure are consequences of
the chosen variation rule, not independently adjustable coefficients. They
are local data. This note does not adopt `rho_K=C a^(-3)` as an all-epoch
law, nor infer the pressure of physical gravitational radiation from it.
Enforcing the fixed-charge rule at every scale would be an additional dust
continuation, with exactly that pressure consequence.

This is equality of the two **homogeneous first variations**. It is not a
Routh reduction or equality of complete off-shell actions when h is varied.
In particular, do not add `-nu E/(2 lambda)` to a theory already containing
`-ell_0 E/(2 lambda)`: that would count the lapse source twice. The density
jet represents the same source once, in the homogeneous comparison.

## 3. Exact output and equality

Let `R` and `R_chi` denote total homogeneous density data, not the TT
recurrence residual from section 1. Set

```text
R = (M+E/10)/lambda,
R_chi = (Q-3E/10)/lambda,
p* = -R-R_chi/3 = -(M+Q/3)/lambda,

Z = (M+E/10)/3,
H* = the nonnegative real square root of Z,
K* = dot H* = (Q-3E/10)/6.
```

Since `M>=0` and `E>=0`, Z is nonnegative. The selected square root is
an explicit branch choice, not a consequence of the source energy. It is
the sign choice at the point only, not a promise of future expansion.
No formula divides by H, so the source-off case `M=0,H=0` is included.

The complete normalized geometric output is the following 2-jet:

```text
chi:  (chi*, dot chi*, ddot chi*) = (0,H*,K*),
a:    (a*, dot a*, ddot a*) = (1,H*,H*^2+K*),
nu:   (nu*, dot nu*, ddot nu*) = (1,0,0).
```

Equivalently, in the marked spatial frame,

```text
g_00 = -1, g_0i=0,
g_ij(t) = [1+2H*t+(K*+2H*^2)t^2] delta_ij mod t^3.
```

The output also carries `(R,R_chi,p*)`, the time-density derivative
`dot R*=H* R_chi`, and the canonical data

```text
pi_chi* = -6 V0 H*/lambda,
dot pi_chi* = -V0(6R+R_chi).
```

Equality is equality of all marked jet components and attached source-point
labels in the fixed chart. Use the nonnegative root of the exact rational Z;
no sign quotient or floating-point equality is admitted. The geometry may
coincide for different words with the same energy; injectivity is not claimed.
After factoring out the displayed powers of the fixed lambda, the output
coefficients lie in the exact real field `Q(sqrt(Z))`.

A 2-jet is the equivalence class of local smooth fields with these values
and first two derivatives. It is not a selected entire time history. Since
the spatial metric at the point is positive and the lapse is one, a local
Lorentzian representative exists. This asserts no uniform time interval.
Repeated applications at different counter labels are not claimed to form
one integrable cosmological trajectory.

## 4. Proof against the public FRW equations

The public rank-one action is

```text
S_FRW = V0 integral dt nu exp(3chi)
          [ -(3/lambda)(dot chi/nu)^2 - rho_total(chi) ].
```

Its homogeneous variations at the marked point depend only on the supplied
density jet. Any local density representative with values `(R,R_chi)` gives
the same equations there; higher density derivatives are not inputs to this
claim.

**Lapse.** Direct substitution gives

```text
3H*^2 = lambda R = M+E/10.
```

**Scale variation and pressure.** Since `K*=lambda R_chi/6`,

```text
(6/lambda)K*+(9/lambda)H*^2-3R-R_chi = 0,
2K*+3H*^2 = -lambda p*,
2K* = -lambda(R+p*).
```

Thus both the lapse equation and the independent scale-factor
Euler-Lagrange equation hold, with the derived local pressure.

**Continuity and first constraint propagation.** The time-density
derivative is `H* R_chi`, not `R_chi`. Therefore

```text
dot R* = H* R_chi = -3H*(R+p*),
d_t(3H^2-lambda rho_total)*
  = 6H*K* - lambda H* R_chi = 0.
```

Both equalities hold also at H=0 without division by H.

**Hamiltonian.** The public canonical constraint is

```text
C_H = -lambda pi_chi^2/[12 V0 exp(3chi)]
      + V0 exp(3chi) rho_total(chi).
```

At the output, `C_H*=0`,
`partial_(pi_chi) C_H*=H*`, and
`-partial_chi C_H*=-V0(6R+R_chi)=dot pi_chi*`.
The latter also equals the time derivative of
`pi_chi=-6V0 exp(3chi)H/lambda` using the output jet. Both canonical equations
therefore agree with the same geometry and source.

**Homogeneous restriction and fixed constants.** Setting E=0 recovers
exactly the nonnegative-point branch of the public matter FRW jet:
`H*^2=M/3`, `K*=Q/6`. The value `lambda=216 pi`, `lambda/3=72 pi`,
the chain `864=12*72=4*216` and its previously proved fiber identity are
unchanged public dependencies. This note does not rederive the fiber theorem.

These are equations evaluated at the specified jet, including the first
constraint derivative. They do not assert that the residuals of all field
equations are `O(t^3)`; that stronger statement would consume higher jets.

## 5. The former vacuum obstruction now has a determined output

For the fixed vacuum matter input `M=Q=0`, every K1 word gives

```text
H*^2=E/30, K*=-E/20, ddot a*=-E/60,
g_ij(t)=[1+2sqrt(E/30)t+(E/60)t^2] delta_ij mod t^3.
```

| abs(u_1-u_0) | H*^2 | K* |
| --- | --- | --- |
| 0 | 53/12960 | -53/8640 |
| 1 | 713/77760 | -713/51840 |
| 2 | 67/4860 | -67/3240 |

In particular `0011` no longer demands `0=53/4320`: it produces
`3H*^2=53/4320`. Removing the TT source as well as the vacuum matter gives
the Minkowski jet. This is a solved local output, not an adjustment of the
input source to a target observation.

For a perturbative order audit only, writing `h=epsilon h_bar` gives
`E=epsilon^2 E_bar`. At the vacuum point `H*=O(abs(epsilon))`, whereas
`K*=O(epsilon^2)`. One must not describe H as a purely second-order
correction about a background H=0. Epsilon is not an added K1 amplitude
parameter in this note's input domain.

## 6. Attachment to the inhomogeneous records and promotion boundary

At the selected half-slice, the homogeneous output uses exactly
`E=<1,e>_V`, hence the same `bar_e=E/5` as the mean-zero split. If the
predefinition's typed local construction is certified, its

```text
L3 tau = Pi_0 e/2,
p_perp = -j/2-WB Delta tau,
B^T p_perp=0, 2P+j=0
```

can be attached with their original integer/half-integer labels. None of
these local records is projected away or recomputed from H. This note
supplies their formerly unspecified homogeneous output, conditional on the
explicit first-variation dictionary. It does not claim a common off-shell
action certificate for every inhomogeneous and homogeneous field together,
a map from tau into all physical metric components, or a discrete-to-cosmic
time evolution law.

The immediate delivery is the total local homogeneous map above, including
the source jet, pressure, branch, equality, zero case and all displayed FRW
checks. Its scope must remain explicit in any later proposal to decide the
historical positive clause of `FRW-INHOM`.

Before a status move, the public work must assemble the actual result of
#923, the analytical support for all consumed source identities, this
separately adopted reading, and the named L1-to-L2 dictionary gate. It must
then decide whether the combined *claimed* construction satisfies the
unchanged owner clause. In particular it must not promote a local jet to an
entire nonlinearly coupled spacetime by wording alone. No gate is registered
or declared passed by this note.

`TT-SOURCE` still owns the physical emission map and source dependency.
`TT-VECTOR-STATE-NORMALIZATION` still owns the scalar comparison, action-unit
normalization and numerical `r_T(k)`. Zero homogeneous pressure in this
chosen source jet is not a cosmological scalar power spectrum. Wider
inhomogeneous scalar-action claims, including the boundary of
`CONFORMAL-PREFACTOR`, are not discharged by the homogeneous result here.

## Public inputs

- `canon/CANON.md`, `DEF-K1-LINEAR-METRIC` and its conditional completion
  theorem, at `canon-v82`.
- `reproduce/gravity-chain/verify.py`, lapse, Friedmann and Hamiltonian
  clauses of `FRW-CANONICAL-FORM`, at the stated main basis.
- `notes/canon/C-FRW-INHOM-TYPED-ADM-PREDEFINITION-N.md`, especially sections
  7, 9, 11 and 13, merged by #918.
- `probes/P-FRW-INHOM-K1-BACKREACTION-3/PREREG.md` at the pin stated above:
  the frozen source conventions and the explicit separation of a later D
  fold from its L1 computational result.

No measured constant, archive, fitted coefficient, new K1 word, occurrence
law, K2/K3 source, or new scientific probe is introduced.
