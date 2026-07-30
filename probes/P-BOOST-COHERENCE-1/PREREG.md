# PREREG P-BOOST-COHERENCE-1

```text
probe          P-BOOST-COHERENCE-1
public lock    issue #206
owner          A. M. Thorn, 2026-07-29 session
parent rows    BOOST-READING-SPLIT [T], BOOST-COUNT-LADDER [D]
target         exact alternator-coherence and conditional-selection evidence
layers         L5 stream with an exact L1 coin carrier; no L6 claim
formal runs    zero before this two-file pin
```

Basis: Public Canon v26, tag `canon-v26`, public `main`
`48213275d0ace92d8f034166179a9fee4d53d908`, content commit
`138eec5b22a823469e1fa651505815a3d5b36761`, and
`canon/CANON.md` SHA-256
`3a62711e30b1f3e9c4ade71533354fdf669266f60f4a57ade84e31a8f2878cfd`
with 141941 bytes.

## Prospective pin and known-result disclosure

Prior incubation work and a notes-only owner disposition exist. They are
known-result audit inputs, not public evidence. No incubation script, stdout,
failed-run diary, amendment narrative, private path, or architecture record
is imported into this probe.

`PREREG.md` and `verify.py` in this directory are newly authored public
files. Before their first common commit they may receive source review, AST
parsing, compilation, and other non-executing static checks only. The
scientific assertions in `verify.py` must not be executed until the accepted
two-file pin is committed, pushed, and read back publicly. Any differing
result, fired threshold, code defect, or environment failure after that pin
must be preserved. No threshold, carrier, endpoint convention, premise, or
scope may move.

This probe tests the exact mathematical ranking of coin selectors. It does
not adopt `MINIMAL-READ`, add `COIN-MINIMAL-READ [H]`, or add
`MINIMAL-READ-DERIVATION [O]`.

## 1. Equation

### 1.1 Public basis and positive-orientation integer coins

Put

```text
phi = (1 + sqrt5)/2,
beta_n = tanh(n log phi),
z = exp(i k),
Sigma = diag(-1, 1).
```

For positive odd `n`, the public `BOOST-READING-SPLIT` identity gives

```text
beta_n = L_n/(sqrt5 F_n),
1 - beta_n^2 = 4/(5 F_n^2).
```

The positive-orientation rung coin is therefore

```text
A_n = 1/(sqrt5 F_n) [[L_n, 2], [2, -L_n]].
```

An integer-normalized alternator coin means that

```text
A(a,b) = 1/sqrt5 [[a,b],[b,-a]],
a,b positive integers,
a^2 + b^2 = 5,
```

and its coherent half-width is `c=a/sqrt5=beta_n` for a positive odd rung.
Equivalently on the rung form, both `L_n/F_n` and `2/F_n` are integers.

The frozen completeness claim is:

```text
(a,b,n) = (1,2,1) or (2,1,3).
```

There are two exact proof routes.

1. Positivity and `a^2+b^2=5` bound `a,b` by `2`; direct exhaustion gives
   only `(1,2)` and `(2,1)`.
2. If `F_n | L_n`, then
   `L_n^2-5F_n^2=-4` for odd `n` gives `F_n^2 | 4`. Hence
   `F_n in {1,2}`; monotonicity of positive Fibonacci numbers from `n=1`
   onward gives `n in {1,3}`. The factor `2/F_n` is then integral as well.

This is an all-index claim. Any finite Fibonacci loop in `verify.py` audits
the implementation only.

Write

```text
A_1 = 1/sqrt5 [[1,2],[2,-1]],
A_3 = 1/sqrt5 [[2,1],[1,-2]],
c_1 = beta_1 = 1/sqrt5,
c_3 = beta_3 = 2/sqrt5.
```

### 1.2 Endpoint-qualified composed cover

Use rapidity coordinate `x=eta/log(phi)`, so ladder rungs are the integers.
For half-width `w>0` and center `n in Z`, freeze two related families:

```text
C_(n,w) = [n-w, n+w]       closed range, used for completeness
I_(n,w) = (n-w, n+w)       open band, used for multiplicity cost.
```

The meanings are intentionally distinct.

```text
complete closed cover:
  union_(n in Z) C_(n,w) = R  iff  w >= 1/2.

open-band multiplicity:
  m_w(x) = #{n in Z : x in I_(n,w)}.
```

For integer `w>=1`,

```text
x not in Z:  m_w(x)=2w,
x in Z:      m_w(x)=2w-1.
```

Thus the two admissible coins have:

```text
coin       w    generic open-band multiplicity    rung open-band multiplicity
beta_1    1    2                                 1
beta_3    3    6                                 5.
```

For the comparison width `w=1/2`, the closed intervals cover the line,
generic non-seam points have open-band multiplicity `1`, and every seam
`x in Z+1/2` has open-band multiplicity `0` and closed-cover multiplicity
`2`. It is therefore a generic single tiling, not a pointwise open cover.
Its velocity is

```text
tanh(log(phi)/2) = sqrt5 - 2 = phi^-3,
```

which is not integer-admissible. The phrase `integrality minimum` refers only
to the generic open-band cost among the two complete integer-admissible
coins. No endpoint is hidden or counted under two conventions at once.

Because rapidities add under the registered Einstein composition law and
`tanh:R -> (-1,1)` is strictly increasing, the closed rapidity cover maps to
a complete composed velocity cover of `(-1,1)`.

### 1.3 T1, per-tick velocity operator

For a coin

```text
A(c,s) = [[c,s],[s,-c]],    c^2+s^2=1,
S(z) = diag(z,z^-1),        W(z)=S(z)A,
```

the `beta_1` values are `c=1/sqrt5`, `s=2/sqrt5`. Freeze

```text
D = A Sigma A = 1/5 [[3,-4],[-4,-3]],
D^2=I,   tr(D)=0,   spec(D)={-1,+1}.
```

This is the exact per-tick velocity operator at L5. The spectrum statement
is operator light-likeness only; it is not a continuum or measurement claim.

### 1.4 T2, division-free spectral skeleton

Work in

```text
R = Q(sqrt5)[z,z^-1,r] /
    (r^2 - (18+z^2+z^-2)/20),
```

with the unit-circle involution `z -> z^-1`, `r -> r`. Put

```text
t = tr(W) = (z-z^-1)/sqrt5,
h = t/2,
lambda_+ = h+r,
lambda_- = h-r,
p_+ = W-lambda_- I,
p_- = W-lambda_+ I.
```

Freeze the following division-free identities:

```text
W^2=tW+I,                         W^-1=W-tI,
lambda_+ lambda_-=-1,
r^2-h^2=1,

p_+^2= 2r p_+,                    p_-^2=-2r p_-,
p_+p_-=p_-p_+=0,                  p_+-p_-=2rI,
Wp_+=lambda_+p_+,                 Wp_-=lambda_-p_-,

lambda_pm conjugate(lambda_pm)=1.
```

For

```text
rho = lambda_-/lambda_+ = -lambda_-^2,
```

freeze

```text
|1-rho|^2 = (1-rho) conjugate(1-rho) = 4r^2,
r^2 - 4/5 = cos^2(k)/5.
```

Hence the squared step-operator gap never closes and has minimum `16/5`
at `cos(k)=0`.

### 1.5 T3, division-free drift

Freeze

```text
tr(WD) = -(z+z^-1)/sqrt5,

p_+ D p_+ = -(z+z^-1)/sqrt5 p_+,
p_- D p_- = -(z+z^-1)/sqrt5 p_-.
```

With

```text
G = p_+Dp_+ + p_-Dp_-,
```

freeze

```text
G = -(z+z^-1)/sqrt5 (2W-tI),
(2W-tI)^2=4r^2 I,
V_inf = G/(4r^2),
V_inf^2 = v_g^2 I,
v_g^2 = c_1^2 cos^2(k)/(1-c_1^2 sin^2(k)).
```

At `z=1`, freeze the zero-mode identity

```text
V_inf(1) = -beta_1 A_1.
```

The spectrum of `V_inf` fills exactly `[-beta_1,beta_1]`. The range proof
uses continuity and

```text
c^2-v_g^2 =
c^2 sin^2(k)(1-c^2)/(1-c^2 sin^2(k)) >= 0,
```

with equality at `sin(k)=0` and zero drift at `cos(k)=0`.

### 1.6 T4, all-N uniform ergodic read

Let

```text
P_+ = p_+/(2r),   P_- = -p_-/(2r),
X = p_+Dp_-,
Y = p_-Dp_+.
```

The verifier freezes the division-free induction kernel:

```text
4r^2D = G-X-Y,
W^-1 G W = G,
W^-1 X W = rho X,
W^-1 Y W = conjugate(rho) Y.
```

It follows by induction for every `j>=0` that the diagonal part is fixed and
the two off-band blocks acquire the phases `rho^j` and
`conjugate(rho)^j`.

For

```text
V_bar_N = (1/N) sum_(j=0)^(N-1) W^-j D W^j,
```

the off-band blocks are adjoints. The norm of the resulting self-adjoint
off-band matrix is bounded by the modulus of one geometric coefficient,
not by the sum of two separate triangle bounds. Since `D` has norm `1`,

```text
||V_bar_N-V_inf||
  <= (1/N) |sum_(j=0)^(N-1) rho^j|
  <= 2/(N|1-rho|)
  = 1/(Nr)
  <= sqrt5/(2N).
```

The last inequality uses `r^2>=4/5`. It is uniform in momentum and input
state. The minimum denominator occurs at the zone edge; no claim that every
finite-`N` error saturates the final inequality is made.

The physical reading remains conditional on two declared premises:

```text
P1  the read is translation covariant and acts fiberwise in k;
P2  the read window spans N>>1 ticks.
```

The theorem says what such a read returns. It does not derive P1, P2,
decoherence, an environment, collapse, or a Born coupling.

### 1.7 T5, exact conditional selector ranking

For the `beta_3` coin, replace `c_1^2=1/5` by `c_3^2=4/5`. The same spectral
calculation gives:

```text
coin       r_min^2     uniform constant 1/r_min    min |1-rho|^2
beta_1    4/5         sqrt5/2                    16/5
beta_3    1/5         sqrt5                      4/5.
```

Freeze the conditional selectors on the complete admissible pair:

```text
S1  minimum generic open-band multiplicity  -> beta_1 uniquely,
S2  minimum worst-case uniform constant      -> beta_1 uniquely,
S3  maximum coherent half-width              -> beta_3 uniquely.
```

`S1` and `S2` are distinct cost definitions that agree on the frozen pair.
They are not asserted to be generally equivalent or experimentally
independent. `S3` is preserved as the exact counter-ranking.

This is a conditional mathematical theorem. It neither adopts S1/S2 as the
Canon dictionary nor falsifies S3 by naming it.

## 2. Code

`verify.py` in this directory is the accepted exact verifier. It uses only
the Python standard library and `fractions.Fraction`. Its symbolic carrier is
the division-free ring `R` above, implemented as reduced pairs of Laurent
polynomials. It also audits the exact integer carrier, cover conventions,
half-rung identity, coherent-width formula, read-rate constants, and selector
rankings.

The verifier uses no float, randomness, clock, filesystem access, network
access, subprocess, dynamic evaluation, or external data.

After public commit, push, and readback of this two-file pin, the first formal
run command is:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-BOOST-COHERENCE-1/verify.py
```

External budget: under 120 seconds.

No `EXPECTED.txt`, `RUN.md`, or `RESULT.md` exists at the preregistration
pin.

## 3. Carrier or data

There are no experimental data.

The exact carriers are:

```text
K1  Q(sqrt5), represented by rational pairs a+b sqrt5.

K2  Q(sqrt5)[z,z^-1], represented by finite Laurent coefficient maps.

K3  R=K2[r]/(r^2-(18+z^2+z^-2)/20), represented by p_0+p_1 r.

K4  2x2 matrices over R.

K5  positive integer pairs (a,b) with a^2+b^2=5 and positive odd
    Fibonacci/Lucas rung indices.

K6  exact rational rapidity points for open and closed interval counts.
```

The finite audits are:

```text
FIB    odd n through 101, auditing the all-index rigidity proof.

COVER  centers and rational points in a symmetric finite window for
       w in {1/2,1,3}, including integers and half-integer seams.

RING   complete coefficient equality for every frozen Laurent-ring identity;
       this is symbolic in z and therefore all-momentum, not a grid.
```

Finite `FIB` and `COVER` loops audit their implementations and frozen boundary
witnesses. They do not replace the all-index integer and interval-counting
proofs in Field 1.

## 4. Systematics

```text
S1  The public coin class is positive-orientation A(a,b) with a,b>0 and
    a^2+b^2=5, linked to positive odd ladder rungs. Sign changes, basis
    swaps, and negative velocities are symmetries, not additional coins.

S2  Completeness uses closed intervals C_(n,w). Multiplicity cost uses open
    bands I_(n,w). Generic, rung, and seam counts remain separately labeled.

S3  The all-index rigidity proof is mathematical. The FIB loop is only an
    implementation audit and cannot by itself earn completeness.

S4  The RING identities are coefficient equalities in the frozen quotient
    ring and are valid for all formal z. Positivity and norm statements are
    restricted to the unit circle z=exp(ik) with the positive branch r>0.

S5  Labeled standard proof steps, not machine-proved: monotonicity and
    continuity of tanh; every real point lies within 1/2 of an integer;
    monotonicity of positive Fibonacci numbers; nonnegativity of sin^2 and
    cos^2; the two-band spectral theorem on the unit circle; the induction
    from the frozen conjugation kernel; the geometric-sum inequality; and
    the self-adjoint off-band block norm.

S6  P1 and P2 are declared reading premises. The probe neither derives nor
    physically anchors them.

S7  The factor-four comparison is only for |1-rho|^2. The uniform constants
    differ by a factor two.

S8  The proof is self-contained and all-index/all-momentum at its stated
    mathematical scope. Architecture runs audit the implementation; a
    same-architecture byte match does not by itself promote a
    computation-only claim.

S9  No decoder-completion, no-feedback, output-redundancy, L5-to-L1, L6,
    SI, empirical, or unique-physics claim is included.

S10 Prior incubation results are disclosed known results but are not public
    evidence and supply no accepted bytes to this probe.
```

## 5. Failure threshold

```text
F1  Fire if the positive integer solutions of a^2+b^2=5 are not exactly
    (1,2) and (2,1), if the odd-rung all-index proof admits n outside
    {1,3}, or if either stated coin does not equal beta_1 or beta_3.

F2  Fire if the closed-cover completeness threshold is not w=1/2, if any
    frozen generic, rung, or seam multiplicity differs, or if the half-rung
    velocity is not sqrt5-2=phi^-3.

F3  Fire if D differs from the 3-4-5 reflection, if D^2 differs from I, or
    if its trace or spectrum differs from the frozen T1 statement.

F4  Fire if any Cayley-Hamilton, inverse, eigenvalue, projector-numerator,
    orthogonality, unitarity, or all-momentum gap identity of T2 fails.

F5  Fire if any Hellmann-Feynman numerator, G closed form, drift-square,
    coherent-width, or zero-mode identity of T3 fails.

F6  Fire if the division-free base decomposition or any conjugation
    recurrence kernel of T4 fails, or if the stated all-N geometric bound
    does not follow from the frozen unit-circle hypotheses and standard
    steps.

F7  Fire if r_min^2, either uniform constant, or either minimum squared gap
    differs from the T5 table.

F8  Fire if S1 or S2 does not select beta_1 uniquely, if S3 does not select
    beta_3 uniquely, or if a third admissible positive-orientation integer
    coin exists.

F9  STOP if the public pin, command, environment, stdout, stderr, hash,
    endpoint convention, carrier, proof step, or action-layer boundary is
    malformed or incomplete. A code defect is STOP, not scientific F.
```

Any one fired scientific threshold fails the proposed theorem at its frozen
scope and must be recorded. `STOP` preserves the pin and authorizes no
threshold repair, hidden rerun, or reinterpretation.

## 6. Action layer

```text
T1-T4 mathematical carrier   L5 stream over an exact L1 coin.
T5 coin classification       L1 carrier with L5 read-cost comparisons.
P1/P2                        declared L5 reading premises.
L6                           excluded.
L5-to-L1 feedback            excluded.
```

On success, the result may propose evidence for the status-neutral future
rows:

```text
TICK-VELOCITY-OPERATOR
WALK-SPECTRAL-SKELETON
DRIFT-IS-THE-READ
COIN-SELECTION-CONDITIONAL
```

Their earned statuses, exact scopes, evidence tuple, dependencies, gates, and
release inclusion are decided only after the public result. This probe does
not edit `canon/`, `reproduce/`, workflows, release-form files, issue #199,
or PR #205. It does not add the owner-approved H/O rows. Any later Canon v27
change requires a separately sealed composed fold from the then-current
public `main`.
