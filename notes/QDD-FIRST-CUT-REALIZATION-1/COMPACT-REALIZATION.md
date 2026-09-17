# A twelve-mode first-cut analogue

**NON-CANONICAL / EXACT DESIGN EXPLORATION / NO HARDWARE OR MEASUREMENT.**
These calculations were explored before any formal pin. They are not a new
formal probe and change no sealed probe or Canon. `explore.py` is a standalone
standard-library exploratory script; its exact output is
`exploration-results.json`. The inherited signed response is from
P-QDD-PASSIVE-QUADRATIC-CALIBRATION-1, proof at public commit
`757492055ab5a0a39e14a4089650f3f76ed9cf47`. Physical energy normalization
follows the proposal in `notes/DECODER-PASSIVE-REALIZATION-BRIDGE-1.md` (#832).

**Result:** for the fixed four-dimensional prepared-source subspace and one
cold cut, eight specified signed outputs admit a real twelve-mode passive
completion. Four residual modes are necessary and sufficient in the fixed
energy-coordinate isometry class. The standard sufficient full Dirichlet
buffer has 189 sites and 386 wave-plus-port modes. The reduction is obtained
by restricting both the prepared subspace and the observation time; it does
not implement the general wave state or establish a multi-time dynamics.

## 1. Fixed input and output energies

Keep `u=(1,1,1,1)^T`, `G=I-uu^T/5` and the prepared wave `(0,S(z))`.
Its dimensionless energy is

```
q(z)=z^T P z, P=G/2=I/2-uu^T/10.
```

Use the seven calibration sites followed by the origin, in this order:

```
(110),(101),(011),(200),(-1,-1,0),(-1,0,-1),(-1,0,1),(000).
```

All conductances are one and all incoming ports are cold. The signed
first-cut output is `b=Bz`, where `B=-H/4860` and

```
H = [ -354  1416  -354  -354
      -354  -354  1416  -354
      -348  -348  -348  1422
      -368  -343  -343  -373
         8    53   -22   -22
         8   -22    53   -22
        16   -14    -9    16
      1421  -349  -349  -349 ].
```

These rows are independently reconstructed from the centered five-site
injection and the sixty displacement weights by the exploratory script.
The eight deposited energies are `D_j=(Bz)_j^2`, not normalized probabilities.
For the proposed independently calibrated optical scale E_star in joules,
input pulse energy is `E_star*q` and output j has energy `E_star*D_j`.
The input norm is **G/2**, not G; omitting this factor would misstate passivity.

## 2. Exact contraction and a strict energy margin

Set `R=P-B^T B`. Exact arithmetic gives `R=N/23619600`, with

```
N = [ 6921055 -1737435 -1737515 -1758975
     -1737435  6953425 -1717780 -1739990
     -1737515 -1717780  6953540 -1740070
     -1758975 -1739990 -1740070  6912970 ].
```

Its leading principal minors are

```
Delta1 = 6921055,
Delta2 = 45106356484150,
Delta3 = 261862989829018704375,
Delta4 = 1121922794892170797383656250.
```

They are all positive. An exact LDL factorization, independently multiplied
back in the script, therefore proves `R>0` and `rank R=4`. In particular
`B^T B<P=G/2` for every real source, not merely for the balanced finite grid.
The same real symmetric matrix inequality holds under Hermitian pairing
for the mathematical complex extension.

There is a useful stronger rational certificate. The leading minors of
`23619600(10R-7P)` are

```
3075670,
9748681531000,
28556753551527975000,
41962619167921990732500000.
```

Thus `R>(7/10)P` and `B^T B<(3/10)P`. With normalized input coordinates
`s=P^(1/2)z`, the eight-output transfer `A=B P^(-1/2)` has
`||A||_2<sqrt(3/10)`. The eight outputs jointly carry less than 30 percent
of the initial energy; the residual carries more than 70 percent for every
nonzero source. This is an exact conservative bound, not a measured efficiency
or a claim that 30 percent is the optimal constant.

## 3. Four residual channels: an exact radical construction

Write `N=L diag(d) L^T`, with L unit lower triangular. The exact rational
data can be constructed without an eigensolver by

```
d_j=N_jj-sum_(k<j) L_jk^2 d_k,
L_ij=[N_ij-sum_(k<j) L_ik L_jk d_k]/d_j, i>j.
```

The positive diagonal is

```
d=(6921055,
   9021271296830/1384211,
   10474519593160748175/1804254259366,
   598358823942491091937950/139660261242143309).
```

The complete rational L is in the JSON output, and the displayed recurrence
and N specify it uniquely. Define the explicit four-by-four radical matrix

```
C=diag(sqrt(d_j))*L^T/4860.
```

Then `C^T C=R` by multiplication. The twelve outputs
`V z=(Bz,Cz)` obey `V^T V=P`, exactly conserving the chosen input energy.

This residual dimension is minimal. If k real residual output rows K
conserve that same energy with the same eight labelled signed outputs,
then `K^T K=R`, so `k>=rank R=4`; C attains four. The statement also holds
for complex-linear optical isometries with the **same fixed four energy
coordinates**: the residual block must have Hermitian Gram matrix of rank
four. It is not a universal count across altered input encodings, different
observables or schemes that relabel time/frequency modes. Twelve counts
separately orthogonal modes, not necessarily twelve spatial beam paths.
An apparatus may expose only eight monitored outputs and discard residual
energy into unmonitored channels; this does not constitute a complete
eight-mode energy-conserving realization in the stated class.
The completion is not unique. Rotating the four residual modes or changing
the extension on unused input modes preserves these eight responses; the
LDL factor and construction below select one explicit mathematical design.

## 4. Explicit completion to a twelve-by-twelve orthogonal matrix

Let `P_t=uu^T/4`. A particularly simple source-energy encoder is

```
J=P^(1/2)=(I-P_t+P_t/sqrt(5))/sqrt(2),
J^-1=sqrt(2)*(I-P_t+sqrt(5)*P_t).
W=[B; C] J^-1,       W^T W=I_4.
```

This uses only rational arithmetic and specified positive square roots.
The following four-reflection procedure is a complete exact construction
of a real orthogonal U whose first four columns are W:

1. Start `Q=I_12`.
2. For j=1,2,3,4 let `v=Q e_j-W_j`, where W_j is column j.
3. If v=0 keep Q. Otherwise set `H_j=I_12-2vv^T/(v^T v)` and replace
   `Q` by `H_j Q`.
4. Return `U=Q`.

At step j, both vectors in v have norm one and are perpendicular to all
previously fixed W_i. Thus the reflection sends `Q e_j` to W_j and fixes
those earlier columns. Induction proves `U^T U=I_12` and its first four
columns equal W. No unspecified matrix square root or arbitrary eigenvector
choice remains. The zero branch prevents division by zero. All entries
are exact real radical expressions determined by the displayed data.
For convenience, `engineering_completion.py` renders the resulting full
twelve-by-twelve matrix in `engineering-completion.json`. Its numerical
entries and rounding diagnostics are explicitly engineering approximations;
the exact identities are established by the preceding rational/radical proof.

For an elementary plane-rotation description, eliminate the subdiagonal
entries of the twelve-by-four W column by column using Givens rotations,
then retain their inverse product and diagonal signs. At most
`11+10+9+8=38` real two-mode rotations are sufficient. A Householder
reflection is not being counted as one ordinary optical component. This
is a mathematical synthesis upper bound, not a built or optimized layout.

Prepare the twelve-mode input
`alpha_in=sqrt(E_star)*(Jz,0_8)` and propagate through U. Its output is
`alpha_out=sqrt(E_star)*(Bz,Cz)`. This is consistent with #832's energy
normalization and uses four populated input modes plus eight nominated
dark modes. Actual source encoding, darkness, phase and component transfer
remain physical calibration obligations.
Signed rows and complex transfer deviations refer to a fixed input/output
mode basis and a common calibrated phase reference. Power readings alone
do not verify those signs or phases.

## 5. What the compact device does and does not represent

The one-cut full Dirichlet construction in #832 can take
`D=(source sites union eight ports)+B_stencil`, of size 189. Its unrestricted
pair-plus-port space has `2*189+8=386` coordinates. This is a specific
sufficient buffer, not a lower bound on every full-wave implementation.
The twelve-mode map deliberately retains only the four-dimensional prepared
source image and its eight outputs at one cut.

The residual Cz has the correct remaining *energy form*. It has not been
identified here with every lattice field coordinate, spatial locality or a
source-independent future state-update rule. Because C is invertible, a
known source z can in principle be recovered from it and the corresponding
prepared-subspace wave calculated. That algebraic recovery is not a
certificate that feeding these four residual modes into the same device
performs the next physical wave step. A multi-time implementation needs
explicit subsequent encoding and intertwining maps, fresh ports and
their own context/energy certificates. No impossibility of such a further
compression is asserted; it is outside this first-cut construction.

Likewise, destructive observation of the twelve outputs does not preserve
an invertible optical tape. Recoverability of the ideal U requires retaining
the appropriate modes, including the residual and phase information.

## 6. Independent calibration witnesses and predictive meaning

Synthesizing U from B deliberately builds the target response into the
device. Its agreement would test fabrication, input/output metrology,
linearity, phase and loss control. It would **not** independently establish
that native U, the D3 wave rule or QDD describes an unengineered physical
system. Algebraic completion is a smaller analogue design, not a physical
selection or occurrence theorem.

Useful independent evidence for this limited analogue remains concrete:

- Calibrate source normalization and complex receivers with independent
  standards; never infer their gains or phases by imposing B or the
  origin residual zero.
- Prepare independently certified basis sources e_i, their sign reversals
  and a declared amplitude range. Record actual complex transfer columns,
  offsets and losses without constraining a fit to the target. Full complex
  carrier calibration may use phase-shifted inputs; that does not add them
  to the native balanced-source domain.
- Freeze components, encoder, phase conventions and fit on designated
  calibration records, then test withheld superpositions and source vectors
  in the balanced domain. Basis agreement alone does not exclude nonlinear
  response or drift between preparations.
- Keep an independent exported-energy measurement, all four residual energy
  channels, loss/ancilla background accounting and the input pulse-energy
  boundary. Squaring the fitted signed amplitudes is not an independent
  energy measurement.
- If the origin is claimed held out, exclude its validation records from
  device fitting and retuning. A fit of all output columns followed by a
  fresh superposition test checks a different, valid scope: transfer
  prediction/linearity, not an origin excluded from identification.

To obtain a claim about an independent physical realization of the source
and wave dynamics, those maps must be justified independently of installing
this response matrix. The compact device does not supply that additional
evidence. No actual apparatus, archive or numerical calibration budget has
been qualified here, and the existing public-archives-only work scope has
not been changed into permission for new acquisitions.

## 7. A concrete robust comparison once independent errors are supplied

The separate sensitivity derivation is independently checked here by direct
matrix inversion and multiplication in P. For normalized output row
`A_j=b_j J^-1`,

```
alpha_j^2=||A_j||^2=b_j P^-1 b_j^T
         =2[||H_j||^2+(sum_i H_ji)^2]/4860^2.
```

If independent calibration certifies the complex-linear row deviation
`||A_actual,j-A_j||<=eta_j` on the admitted domain, and `||s||^2<=q_max`,
then Cauchy-Schwarz and difference of squared magnitudes give

```
|D_actual,j-D_ideal,j|<=q_max(2 alpha_j eta_j+eta_j^2).
```

For the omitted-origin energy residual, use weights one on the origin and
absolute values of its seven deposit coefficients. With a common row bound
eta, exact upward rational bounds on the eight alpha_j give

```
S_transfer <= q_max(K1 eta+K2 eta^2),
K1=320403677788237/69393956250000,
K2=936962003/185050550.
```

The script independently checks all eight metric norms, the direction of
the square-root enclosures, and both coefficients. Combine this with the
separately proved readout allowance
`epsilon_origin+A epsilon_atom+B epsilon_deposit` and independently owned
remaining systematics. Nonlinearity, source leakage, background light,
unqualified timing and normalization do not disappear into eta unless its
certificate explicitly covers them. The bound is sufficient, not optimal
under joint passivity constraints, and assigns no distribution to errors.

On an *exactly admitted* balanced source, q<=8, attained by `(2,2,-2,-2)`.
Using eight as an experimental q_max still requires its source/energy
certificate; nominal settings alone are not that certificate. No eta,
physical tolerance, sample size, empirical agreement or failure is supplied.

The compact construction therefore reduces a concrete realization-design
problem to twelve modes and gives an explicit conditional comparison. It
leaves physical qualification, any independent theory test, and all
multi-time/occurrence claims unresolved.
