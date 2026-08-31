# Photon Born-current observable lemma

Status: `NON-CANONICAL / RESULT-EXPOSED / CONDITIONAL MODEL / NO FORMAL RUN`

Date: 2026-08-30

Identity: `P-PHOTON-BORN-CURRENT-OBSERVABLE-1`.
Notes claim: [issue #711](https://github.com/mathorn1973/twist-j/issues/711).

This is a mathematical proof note, not Canon, formal evidence, a
preregistration, a verifier, a pin, a run or a result record. The formulas
and witnesses below were derived before any formal definition lock. They
are result-exposed conditional mathematics, not a blind preregistered
discovery. The notes issue claims only this document; it creates no probe
pin or execution authority.

## 1. Public boundary and the model selected for this calculation

```text
Public reference:       mathorn1973/twist-j main
Reference main commit:  cff4c896cbbaf63ebeeec5cf4f50c6fb57b64414
Canon:                  Public Canon v72, ACTIVE
Tag:                    canon-v72
Annotated tag object:   78fa07d8337649e4aba629e38adf23595fedb4bb
Activation/tag target:  0bc7a623627c4453cc94515ae92880ec75ae7d94
Content commit:         aac8a3a4aff027beb2b08edbde1ae8e59224914c
Canon SHA-256:          39ca6e5c49d3ec2b78464045312af75618c4601f87dfa178dfd689d8a4942c70
Canon bytes:            374406
Parent:                 PHOTON-MASSLESS-PHASE [O], MULTI
Parent state:           PHOTON_CONTINUUM / ROOT / STOP / FORMAL
Open gate:              GATE-L4-L6-PHOTON-MASSLESS-PHASE
```

The public one-face data are, with `zeta = exp(2 pi i/5)`,

```text
W(k) = 2 + zeta^k + zeta^(-k),
W    = (4, phi^2, phi^(-2), phi^(-2), phi^2),
FW   = 5(2,1,0,0,1).
```

`W` has full support. The vector `h=(2,1,0,0,1)` gives its character
coefficients; it must not silently replace `W` as the primal action.
An independently selected gauge model with primal plaquette factor `h`
would be a hard-constraint model. Relating that model to the one below
requires an explicit finite-volume duality, including boundary and
topological sectors. No such model identification is adopted here.

Canon does not select a complete product action, a thermodynamic state or a
real-source coupling from these five numbers. This draft selects a concrete
free-box product model and a particular source coupling solely to prove the
conditional identities below. Neither selection is a consequence of Canon.

Let `K` be a finite rectangular cubical box in `Z^4`, with all its cells and
free boundary conditions. Use one positive orientation for every cell, with
coordinate indices increasing. Write `E` and `P` for its positive edges and
plaquettes. Cochains extend to reversed orientations by a minus sign.
The coboundary is `d`; the integer chain boundary `partial` is its adjoint
under the cell pairing. Thus `d^2=0` and `partial^2=0`. Under the usual
chain/cochain identification, this boundary is also denoted `delta`.

The selected configuration space, gauge action and normalized measure are

```text
A in C^1(K; Z_5),              A -> A + d lambda,
q = dA in C^2(K; Z_5),

Z_K = 5^(-|E|) sum_A product_(p in P) W(q_p),
mu_K(A) = Z_K^(-1) 5^(-|E|) product_(p in P) W(q_p).
```

Every edge, including each boundary edge, is summed. No gauge quotient or
gauge fixing is used. The normalized Haar factor is explicit. Since every
`W(q_p)>0`, the partition function is positive and finite, and every edge
configuration has positive probability. The measure is gauge invariant and
invariant under charge conjugation `A -> -A`.

## 2. Exact character-current representation

For each plaquette use the finite identity

```text
W(q_p) = sum_(n_p in {-1,0,1}) a(n_p) zeta^(n_p q_p),
a(0)=2,                 a(+1)=a(-1)=1.
```

Here `n` is an integer 2-chain indexed by the same oriented plaquettes. It
is not the original field `q`, nor a principal real lift of `q`. The pairing
identity and finite Haar orthogonality give

```text
sum_p n_p (dA)_p = sum_e (partial n)_e A_e       modulo 5,

5^(-|E|) sum_A zeta^(<partial n,A>)
    = 1{partial n = 0 modulo 5}.
```

Consequently, exactly and without an approximation,

```text
Z_K = 2^|P| Q_K,

Q_K = sum_(n in {-1,0,1}^P; partial n=0 mod 5)
          2^(-|supp n|),

nu_K(n) = Q_K^(-1) 2^(-|supp n|)
          1{partial n=0 mod 5}.
```

`Q_K>0` because `n=0` is admitted. Thus `nu_K` is a genuine positive
finite probability measure. It is invariant under `n -> -n`.

The integer current

```text
j = (partial n)/5
```

is well-defined on its support and satisfies `partial j=0`. Integer closure
`partial n=0` is not imposed. The distinction between integer closure and
closure modulo five is essential below. This finite character representation
does not require a dual gauge potential or an infinite-volume limit.

## 3. Selected real twist and branch-free score

Select the bandlimited periodic extension

```text
W(theta) = 2 + 2 cos(theta).
```

At the five angles `theta=2 pi k/5` it agrees with the public vector. For
`q_p=dA_p`, choose any angle representative `theta_p=2 pi q_p/5`; periodicity
makes the formulas independent of that choice. For a real plaquette source
`eta`, define

```text
Z_K(eta) = 5^(-|E|) sum_A product_p W(theta_p + eta_p).
```

The same finite expansion proves, for every real `eta`,

```text
Z_K(eta)/Z_K(0) = E_(nu_K) exp(i sum_p n_p eta_p).       (T)
```

For `||eta||_infinity < pi/5`, every factor in the defining sum is strictly
positive. Hence `log Z_K(eta)` is well-defined near zero and differentiation
of the finite sums is legitimate.

Define the real score and its normalized version by

```text
X_p = -partial_theta log W(theta_p)
    = sin(theta_p)/(1+cos(theta_p)),

kappa = tan(pi/5) > 0,       kappa^2 = 5 - 2 sqrt(5),
G_p = X_p/kappa.
```

The denominator is strictly positive at all five roots. Therefore `X` and
`G` are total, bounded, real, local, gauge-invariant functions of the
plaquette holonomy `U_p=zeta^(q_p)`, without choosing a logarithm branch.
They reverse sign with plaquette orientation. Their exact values are

```text
q:       0       1          2              3          4
G(q):    0       1       2+sqrt(5)     -(2+sqrt(5))   -1.
```

Indeed `tan(2 pi/5)/tan(pi/5)=phi^3=2+sqrt(5)`. Charge conjugation implies
`E_mu X_p=E_mu G_p=0`; likewise `E_nu n_p=0`.

## 4. Full covariance identity, including the contact term

For a finite measure, covariance means
`Cov(Y,Z)=E[YZ]-E[Y]E[Z]`, without complex conjugation. All variables in
the next identity are real. Differentiating (T) twice at zero yields

```text
partial_(eta_p) partial_(eta_q) log Z_K(eta)|_0
    = -Cov_(nu_K)(n_p,n_q).                              (H1)
```

On the original side,

```text
partial_theta log W(theta) = -X(theta),
partial_theta^2 log W(theta) = -(1/2)(1+X(theta)^2).
```

Differentiating the normalized finite expectation, including the second
derivative of the individual plaquette factor when `p=q`, gives

```text
partial_(eta_p) partial_(eta_q) log Z_K(eta)|_0
  = Cov_(mu_K)(X_p,X_q)
    - delta_(pq) (1/2) E_(mu_K)[1+X_p^2].                (H2)
```

Equating (H1) and (H2) proves the exact covariance-contact identity

```text
Cov_mu(X_p,X_q) + Cov_nu(n_p,n_q)
    = delta_(pq) (1/2) E_mu[1+X_p^2].                   (C)
```

In particular, its diagonal and zero means imply

```text
E_mu X_p^2 + 2 E_nu n_p^2 = 1,

0 <= E_nu n_p^2 <= 1/2,
0 <= E_mu X_p^2 <= 1,
0 <= E_mu G_p^2 <= kappa^(-2).
```

Thus the right side of (C) also equals
`delta_(pq) [1-E_nu n_p^2]`. For every real test array `t` on `P`,

```text
kappa^2 Var_mu(sum_p t_p G_p) + Var_nu(sum_p t_p n_p)
    = sum_p t_p^2 [1-E_nu n_p^2].                       (V)
```

The right side lies between `(1/2) sum_p t_p^2` and `sum_p t_p^2`.
This bounds the sum of two variances; it supplies no positive lower bound
for either variance separately and no long-distance decay conclusion.

For distinct plaquettes the contact term vanishes, giving the particularly
useful exact identity

```text
Cov_mu(G_p,G_q) = -kappa^(-2) Cov_nu(n_p,n_q),  p != q. (O)
```

Dropping the contact term on the diagonal would be an error. Replacing the
real score `X` by the source convention `Phi=iX` also changes the sign of
the unconjugated product `Phi_p Phi_q`; the conventions must not be mixed.

## 5. Paired subsequential limits and summability equivalence

Take any exhaustion by finite free boxes `K_l` containing every fixed finite
cell set eventually. Extend the finite configurations by zero outside each
box for the purpose of placing their laws on countable product spaces.
The edge alphabet for `mu` is finite, as is the plaquette alphabet for `nu`.

Enumerate all finite cylinder events in both spaces. Each event probability
lies in `[0,1]`; repeated subsequence extraction followed by the diagonal
subsequence construction gives one common subsequence on which all these
probabilities converge. Finite-dimensional consistency is preserved in the
limit. The countable-product extension theorem gives probability measures
with these limiting cylinder probabilities, hence a paired local limit
`(mu,nu)` of the two families. Pairing
means the same volume subsequence, not a coupling of their random variables.

For any fixed pair of plaquettes, `X`, `G` and `n` are bounded cylinder
observables. Their expectations and products therefore converge along this
subsequence. Identities (C), (V) for finite-support `t`, and (O) pass to the
paired limit.

In particular, for any fixed plaquette `p`,

```text
sum_q |Cov_mu(G_p,G_q)| < infinity
    if and only if
sum_q |Cov_nu(n_p,n_q)| < infinity.                      (S)
```

The proof is simply (O), the fixed positive scale `kappa^(-2)`, and the one
finite diagonal term. The same equivalence holds for the corresponding
failure of absolute summability. A restricted common index set, such as
plaquettes of one orientation, has the same property.

This is an observable bridge, not a proof of nonsummability on either side.
No unique limit, full-sequence convergence, translation invariance, Gibbs
property, scaling limit, continuum propagator or physical photon is claimed.
No assertion about Fourier discontinuity is made without the additional
stationarity and Fourier hypotheses it requires.

## 6. Principal curvature is a different observable

Let `pr: Z_5 -> {-2,-1,0,1,2}` be the odd principal representative and set

```text
F_p = pr(q_p),
F(q) = (0,1,2,-2,-1).
```

This is also a bounded gauge-invariant local real observable, but it is not
`G`: `F(2)/F(1)=2`, whereas `G(2)/G(1)=2+sqrt(5)`. The space of real odd
functions on the full five-point carrier has dimension two. The covariance
identity for `G` cannot be relabelled as a covariance identity for `F`.

On the support of the separately selected hard-constraint primal factor
`h`, only `q=0,+1,-1` occur. There the odd space collapses to dimension one,
and exactly

```text
F_p = G_p = Im(U_p)/sin(2 pi/5).
```

That equality on a different model's support does not identify its law with
`mu_K` or with `nu_K`. In particular, the character variable `n` is not a
primal principal curvature merely because its alphabet is `{-1,0,1}`.

For any primal `Z_5` edge field, `dF` is divisible by five. The integer
3-cochain

```text
m = dF/5
```

satisfies `dm=0`, but need not vanish. Here is a completely explicit witness
on the unit four-dimensional box `K=[0,1]^4`. For positively oriented edges,
with the formulas evaluated at their base vertices, put

```text
A_1 = A_4 = 0,
A_2 = x_1 x_3,
A_3 = x_1 - x_2 - 2 x_1 x_2                         modulo 5.
```

These assignments are independent of `x_4`. Using
`(dA)_(ij)=Delta_i A_j-Delta_j A_i`, the principal plaquette values are

```text
F_12 = x_3,
F_13 = 1-2x_2,
F_23 = 2x_1-1,
F_i4 = 0.
```

For example, the raw residue formula for the third line is
`q_23=-1-3x_1 modulo 5`, whose principal representatives are `-1,+1`.
Consequently,

```text
(dF)_123 = Delta_1 F_23 - Delta_2 F_13 + Delta_3 F_12
         = 2 - (-2) + 1 = 5.
```

All residues in this witness are `0,+1,-1`. It therefore has strictly
positive weight for both the selected full-support `W` model and the
separately selected hard-constraint `h` model. In either case, principal
curvature is not an ordinary exact real curl on the entire measure support.
If `F=dB` for a real 1-form `B`, then `dF=d^2B=0`, contradicting the witness.
Gauge fixing cannot change this algebraic obstruction.

For an integer edge lift `A_tilde`, one instead has

```text
F = d A_tilde - 5D,       D an integer 2-cochain,
m = -dD.
```

The Dirac-sheet term is not optional in general. The raw real curl
`d A_tilde` is not itself invariant under changes of edge lifts or compact
gauge transformations; its residue is. This obstruction concerns literal
observable equality, not the existence or absence of a massless phase.

## 7. A positive-weight character sector is not a literal dual curl

The character measure has a separate exact obstruction. Choose an elementary
oriented plaquette `p` in the 12-plane, well inside a sufficiently large box.
For each `v` in `{+e_3,-e_3,+e_4,-e_4}`, choose the oriented elementary
3-cell prism `c_v` from `p` to its translate `p+v`. Orient it so that
`partial c_v` has coefficient `-1` on the base `p` and `+1` on its translated
cap. Define

```text
S_v = p + partial c_v.
```

The base cancels. Each `S_v` consists of its translated cap and four side
faces, all with coefficients `+1` or `-1`, and
`partial S_v=partial p`. The four cup supports are mutually disjoint:
opposite transverse translations use distinct cells, the 3-direction and
4-direction side faces have different coordinate planes, and all caps are
distinct. None contains `p`.

Therefore

```text
n_* = p + sum_v S_v
```

has exactly 21 distinct occupied faces, every coefficient is ternary, and

```text
partial n_* = 5 partial p != 0,
j_* = partial n_*/5 = partial p,
nu_K(n_*)/nu_K(0) = 2^(-21) > 0.
```

This is an explicit admissible current sector, not a claim that 21 is the
minimum filling cost. It is enough to refute a literal representation
`n=*d alpha` on the entire support of `nu_K` by an ordinary real or integer
dual 1-form `alpha`: with compatible standard dual orientations, such a
curl satisfies `partial(*d alpha)=0`, whereas `n_*` does not. The nonzero
boundary is already at the interior edges of `p`; an outer-boundary
completion cannot remove this local obstruction.

A representation with defects could instead involve
`n=*d alpha+5B_j`, with `partial B_j=j`, together with a declared choice of
Dirac surfaces and an induced coupled action. This draft constructs no such
full dual model and excludes no generalized duality or comparison. Even the
sector `j=0` here retains a hard cutoff on the character plaquette variable;
it is not identified with a Gaussian dual action.

## 8. Narrow FS comparison and source-selection nonuniqueness

The primary source is J. Froehlich and T. Spencer, IHES P/81/40 (1981),
*Massless phases and symmetry restoration in Abelian gauge theories and
spin systems*: [archive record](https://omeka.ihes.fr/document/P_81_40.pdf).
The [journal DOI](https://doi.org/10.1007/BF01213610) identifies the later
CMP 83 (1982), 411-454 publication; no page equivalence is assumed.

Only two visually checked FS-P locators are consumed here. Printed p.44,
equation (2.89), defines the original plaquette field using the derivative
of the logarithm of the action factor; its Wilson example is `i beta sin`.
Printed p.45 says that the corresponding dual observable is `(d alpha)_p*`,
and equation (2.90) concerns the dual potential paired with a coclosed
1-form. These are not definitions of the principal `Z_5` lift `F` above.

For the selected bandlimited extension, that original score prescription
has the convention `Phi=iX`. Identity (C) gives an exact finite-volume
score/current relation with its contact term; it does not establish any FS
hypothesis, its `N=5` regime, its Gaussian comparison or its masslessness
conclusion. The positive-weight current witness also prevents silently
using a defect-free literal dual curl for the full character support.

The source coupling itself is not forced by the discrete measure. For
`|epsilon|<1`, consider the alternative smooth periodic extension

```text
W_epsilon(theta)
    = W(theta) [1 + epsilon sin(5theta) sin(theta)].
```

Its multiplying factor is even and strictly positive, since it is at least
`1-|epsilon|`. It agrees with `W` at all five sampled angles, and therefore
defines exactly the same untwisted finite `Z_5` measure. Nevertheless, at
those angles its negative logarithmic derivative is

```text
X_epsilon(q) = X(q) - 5 epsilon sin(2 pi q/5).
```

Thus the five action values alone do not determine a unique derivative
observable or real-source response. The proof of (T)-(S) uses the stated
bandlimited source coupling; it does not claim that every interpolation
has the same score or character-source identity.

The [source-adequacy predefinition under issue #708](https://github.com/mathorn1973/twist-j/issues/708)
remains separate, notes-only and without a formal run. This draft neither
executes it nor resolves its field-target or source-hypothesis slots by
relabeling the conditional constructions above.

## 9. Future formal fields and debt firewall

A later public owner decision would have to freeze all six fields before a
fresh formal pin:

1. **Equation:** exact conditional statements (T)-(S), normalization,
   contact term, both witnesses and the selected observables; no added
   nonsummability conclusion.
2. **Code:** an accepted exact proof-audit/checking surface, if formalized;
   no checker, expected output or execution is provided here.
3. **Carrier/data:** the selected free boxes, orientations, coefficient
   rings, normalized Haar measure, current support, source coupling and
   paired-limit convention, with the selection-versus-Canon boundary intact.
4. **Systematics:** Fourier normalization, chain versus cochain typing,
   contact signs, lift/branch changes, boundary effects, source aliases,
   subsequence pairing and the separate `j` and `m` defects.
5. **Failure threshold:** exact theorem/counterexample predicates for this
   frozen algebraic scope; a failed identity or unresolved definition is
   not a negative closure of the parent phase obligation.
6. **Action layer:** the L4 conditional model/observable identities and
   the explicitly limited measure-limit statement, with a named owner
   disposition before any formal MULTI or L6 use. No gate is satisfied here.

The useful new endpoint is a typed covariance bridge whose two sides differ
off the diagonal only by a fixed nonzero scale and sign. Actual
nonsummability, a complete adopted TWIST-J action, an admissible source
comparison, control of the full defect-current ensemble, uniqueness of a
thermodynamic state and any physical interpretation remain unproved.
`PHOTON-MASSLESS-PHASE [O]` remains open. No Canon, registry, evidence,
dependency, gate, status or release change follows from this draft.
