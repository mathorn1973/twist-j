# Exact finite boost-completion audit

Status: prospective, NON-CANONICAL, NEW_DECLARED L1.
Probe: P-RELATIONAL-MASS-BOOST-COMPLETION-1, ownership issue #1692.
This is a newly declared action and center metric, not an algebraic rewriting
or a derived physical completion of the unreduced #1689 action.

`verify.py` is standalone Python standard-library code. Its Fraction matrix
and degree-two formal-jet utilities are adapted from
P-RELATIONAL-MASS-INERTIAL-RESPONSE-1; no old probe is imported or executed.
All tested square roots are exact positive rationals. There is no floating
point, numerical orbit integration, external input, network, subprocess,
randomness or file output. Static parsing is permitted before the pin;
scientific execution is not. The accepted command is
`python3 probes/P-RELATIONAL-MASS-BOOST-COMPLETION-1/verify.py`.

## Frozen action and coordinate convention

The fourteen coordinates are
`(G11,G12,G22,Pi11,Pi12,Pi22,X1,X2,P1,P2,r1,r2,rho1,rho2)`.
The canonical one-form is `tr(Pi dG)+P.dX+rho.dr`. Off-diagonal metric
Hamilton equations consequently contain the factor 1/2. Automatic
differentiation varies all fourteen coordinates, including the actual
internal angular charge. No derivative treats that charge as an external
constant.

Fix kappa=3, independent center metric I and c>0. The declared functions are

```
h = tr(G Pi G Pi)/2 + sqrt(rho^T G rho) + 3 r^T G^-1 r,
j = 2 G Pi + r rho^T,
S = j12-j21,
H = sqrt(h^2+c^2 P.P),
L = X1 P2-X2 P1+S,
R P = (-P2,P1),
K_i = H X_i/c^2-S(RP)_i/(H+h).
```

The Poisson bracket is computed from automatic gradients and the complete
canonical matrix, not from a preinstalled abstract charge algebra.

## Complete finite inventory

1. **36 complete algebra cases.** Three internal preparations:
   - G=I, Pi=[[0,-1],[-1,0]], r=(1,0), rho=(0,6), h=10;
   - G=I, Pi=[[1,-1],[-1,0]], r=(1,1), rho=(3,4), h=25/2;
   - the first preparation transformed internally by A=[[1,1],[0,1]]:
     G->AGA^T, Pi->A^-T Pi A^-1, r->Ar, rho->A^-T rho.

   For each internal preparation use c in `{1,2}`, t in `{0,1/4,1/2}`
   and the two direction/center pairs
   `d=(1,0), X=(1,-2)` and `d=(3/5,4/5), X=(-2,1)`.
   Set `P=(h/c) 2t/(1-t^2) d`. Thus
   `H=h(1+t^2)/(1-t^2)` is rational. Distinct centers avoid duplicate
   full-phase preparations at t=0. Not all internal preparations have the
   predecessor's elliptic charge; the universal algebra does not require
   that hypothesis, while stability claims retain their separate scope.

   Audit all of
   `{Ki,Pj}=delta_ij H/c^2`, `{Ki,H}=Pi`, `{K1,K2}=-L/c^2`,
   `{L,P1}=P2`, `{L,P2}=-P1`, `{L,K1}=K2`, `{L,K2}=-K1`,
   `{h,Ki}={S,Ki}=0`, `{P1,P2}=0`, and
   `{H,P1}={H,P2}={H,L}={H,h}={H,j_ab}=0`.
   Check both exact Casimir identities `H^2-c^2 P.P=h^2` and
   `H L-c^2(K1 P2-K2 P1)=h S` on the same 36 cases.
   Check every internal Hamilton equation is multiplied by h/H and the
   center equations are `Xdot=c^2P/H`, `Pdot=0`.
2. **36 force cases at exactly the same phase points.** Declare separately
   `W=-f.X`, `f=(1,2)`. Check `{P,H+W}=f`, `{h,H+W}=0` and both components
   of
   `Vdot=(c^2/H I-c^4 PP^T/H^3)f`, with `V=c^2 P/H`.
   This is a prescribed uniform external-force comparison, not an internal
   interaction or a closed isolated energy-conservation claim.
3. **18 rest Hessian directions.** For the same three internal states and
   two c values, at X=P=0 use P directions `(1,0),(0,1),(1,1)`.
   Exact degree-two Taylor expansion must give zero linear term and Hessian
   `(c^2/h)I`.
4. **One explicit moving witness.** With the first internal preparation,
   c=1, X=0 and P=(15/2,0), require h=10, H=25/2, V=(3/5,0),
   internal clock factor 4/5 and velocity derivative matrix
   `diag(32/625,2/25)`.
5. **Four original-action transport cases.** These deliberately use the
   unchanged original unreduced Hamiltonian from #1689, not the new H.
   Keep the first internal preparation, X=0, and take
   `t in {1/10,1/4,1/2,1/5}`, `P=12t/(1-t^2)e1`.
   Audit its full Hamiltonian gradient and verify
   `E=6(1+t^2)/(1-t^2)`, `H_old=4+E`,
   `Xdot=2t/(1+t^2)e1`,
   `D=P.Xdot=E Xdot^T G^-1 Xdot>0`,
   `jdot=diag(-D,0)` and `tr(j)dot=-D`.
   At t=1/5 explicitly check P1=5/2, E=13/2, H_old=21/2,
   Xdot1=5/13 and D=25/26.

## Five negative controls

- At the moving witness, omitting the spin term from K must violate
  `{K1,K2}=-L`.
- Reversing only the spin term sign must also violate that equality.
- Replace H by `sqrt(h^2+4P.P)` at the first preparation, X=(1,-2),
  P=(15/4,0), c=1, and use the naive boost `K_i=H X_i`.
  Then `{K1,H}=4P1`, unequal to P1. This rejects selection of the coefficient
  from energy conservation alone; it does not classify every modified boost.
- At all 24 t>0 algebra cases, the actual relative-position velocity must
  differ from the unrescaled h-flow. This detects omission of the h/H clock.
- At all four old-action transport states, the internal trace derivative is
  nonzero. This detects an incorrectly frozen old internal charge. The
  all-time consequence of the bounded trace identity is proved in PROOF.md;
  finite phase samples alone do not establish an absence of ballistic motion.

## Frozen decision rule and output

Every equality is exact. A mismatch prints its named `FALSIFIER` and
`RESULT=FAIL` and exits with status 1; unexpected exceptions receive a
separate failure code and also exit with status 1. The
first result is retained with no corrected rerun under the same pin.
There is no tolerance, fit, adaptive fixture or optional case.

Successful stdout has eight lines: algebra cases 36; force cases 36;
rest-Hessian directions 18; old-transport cases 4; negative controls 5;
moving witness `10,25/2,3/5,4/5`; acceleration witness `32/625,2/25`;
`RESULT=PASS`. Actual stdout is captured only after public pin/readback.

The finite audit confirms these exact identities on its stated inventory.
All-state Poisson closure, the global bound-flow/stability conclusions,
selection assumptions and the original-action long-time obstruction rely
on the written proof. No physical realization, native U derivation, SI
calibration or empirical mass identification follows from a passing run.
