# Result: a complete selected cosmological scalar comparison

PUBLIC; NON-CANONICAL. P-TT-SCALAR-COSMOLOGICAL-DICTIONARY-1.

```text
Status: PASS
Verdict: SELECTED-COSMOLOGICAL-DICTIONARY
Mathematical status: candidate-T, L1, conditional on ETH-COS-1
Physical model status: candidate-D selections, not adopted by this probe
Canon: Public Canon v90, unchanged
```

## Result and its actual input

ETH-COS-1 supplies a canonical scalar clock and comoving-curvature
perturbation zeta, the scalar and tensor quadratic actions, a complete
classical joint initial field/momentum law, and a common coordinate,
conformal/proper-time and scale dictionary. Its continuation of the
outgoing vector state has explicit covariance, pseudo-covariance and
all higher moments. Every declared input is present; no scalar dynamical
slot or relative normalization is left implicit in this selected model.

The scalar potential and homogeneous solution are

```text
V(phi)=3H_*^2/(2lambda) exp[-sqrt(3lambda) phi], lambda=216pi,
a(t)=(1+3H_*t/2)^(2/3), epsilon=3/2.
```

The scalar is a canonical clock field with sound speed one. This is a
decelerating background, not inflation or a pressureless-fluid perturbation
model. The continuum action is explicitly selected; it is not derived
from the earlier hybrid graph action or claimed to preserve its later
recurrence.

Both canonical sectors obey the same exact equation
`q''+[K_j^2-2/(eta+2/H_*)^2]q=0`, with the same launch momentum q/d.
The additional scalar is seeded by Pi_0 abs(Phi), but subsequently obeys
its own linear equation. It is not continuously reassigned to tensor
intensity. The relative preparation coefficient is fixed at one in
canonical variables, an explicit physical choice.

## Exact output

For the common continuum torus, the full metric tensor contraction and
the selected continuous translation law give

| Signed harmonics | Tensor seed T_j | Scalar seed J_j | r_T where P_S>0 |
| --- | --- | --- | --- |
| +1,-1 | (3+sqrt5)/24 | (5-sqrt5)/120 | 60+24 sqrt5 |
| +2,-2 | (3-sqrt5)/24 | (5+sqrt5)/120 | 60-24 sqrt5 |

The ratio is independent of the common perturbative amplitude A, H_*,
cell scale d and unit calibration ell_0, at every epoch with nonzero
mode power. Absolute powers and the placement of modes and epochs still
consume those inputs. At launch, the ratio of total powers in the four
modes is 36; this summed ratio need not be constant later.

The mode ratio already holds for each active source word at launch.
The fixed Thue-Morse law determines the absolute spectra and joint law,
but the selected seed shapes determine this ratio. That distinction is
part of the result, not hidden behind the source label.

The common transfer has isolated simple zeros and arbitrarily late nodes.
At a node both powers vanish and r_T is undefined. The zero mode and
all unprepared modes likewise have undefined ratios. The all-time proof
does not import the old discrete recurrence's nonvanishing theorem.

The previous finite intensity denominator is not this scalar denominator.
Uniform translation randomizes the entire prepared profile, including
its old mean; at each nonzero mode `J=I(old)+1/80`. The full metric
contraction and relative action normalization also supply a factor twelve.
All these conventions were frozen before the first scientific run.

## Evidence and boundary controls

The complete six-file pin is
`076308642a1286b3af3382526f5eac1b9cc0932d`. Public readback preceded
the first run. All ten exact audit groups passed on that first run with
exit zero and empty stderr; exact output and custody are EXPECTED.txt and
RUN.md. Verifier SHA-256 is
`3ba5b854f6febc7f976d7e5c7d4b88fee78d807e7413e89c89b0cdaa31a6e5c3`;
stdout SHA-256 is
`bdbcae255d757b73df6b160de1d720afa6e5e64710b8559ffa68a276790eafaa`.
Public architecture acceptance is separately recorded in ACCEPTANCE.md
and the pull request, without reclassifying this local record.

PROOF.md establishes the continuum background, reduced scalar action,
constraints, full state, unique future transfer, nodes and ratio.
REVIEW.md records an independent analytic review without reading the
verifier. A separate static code review preceded the pin. The verifier
audits exact ingredients; it does not turn a finite run into a proof of
all future times or certify physical adequacy.

Negative controls confirm that graph and continuum dispersion differ,
five discrete translations do not reproduce the full continuous phase
law, subtracting the word mean changes scalar power, an independent scalar
amplitude changes the ratio, a dust sound speed changes the equation and
omitting the tensor contraction factor changes normalization. No scientific
falsifier of the frozen conditional claims fired.

## Owner disposition proposed for a separate fold

The original positive clause of TT-VECTOR-STATE-NORMALIZATION asks for one
public vector-doublet normalization yielding numerical r_T(k). ETH-TT-1
plus ETH-COS-1 now supplies such a fully specified candidate. Subject to
public acceptance and explicit adoption of its physical dictionary and
layer gates, recommend positive closure at **D**, retaining the original
identifier and decision history. The exact conditional identities can be
recorded separately at T.

This is not a theorem that J uniquely selects the model. The numerical
output concerns a classical linear, anisotropic finite-band preparation
on a decelerating background with one occupied tensor polarization. Its
extra scalar preparation needs an energy source; microscopic preparation,
nonlinear accuracy, SI calibration and an observational cosmological
family are not supplied. None is silently inserted as a new requirement
of the original existential TT closure clause.

The proposed gates remain UNPASSED and unregistered until a reviewed fold.
This probe changes no Canon file or scientific ledger status. The exact
fold proposal is notes/canon/SELECTED-COSMO-SCALAR-FOLD-PROPOSAL.md.
