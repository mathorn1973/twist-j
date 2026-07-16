# J-LI-SCHOENBERG-2 incubation bundle

```text
STATUS:          NON-CANONICAL INCUBATION
AUTHORITY:       none
BASE:            mathorn1973/twist-j main at 6bb013bafb2d1c06fcb295fdbfce0f86198fd685
PUBLIC CANON:    Public Canon v6, unchanged
PUBLIC CLAIMS:   none created by this bundle
DATE PRESERVED:  2026-07-16
```

This directory closes a provenance gap. The exact verifier audited in a
parallel owner-side analysis existed as a conversation attachment but was not
stored in the project or repository. It is preserved here byte for byte,
together with its expected output and the corrected mathematical candidate.

This is not a public probe and cannot retroactively turn earlier executions
into formal runs. A future public probe must start from a new preregistration
pin under `probes/P-J-LI-SCHOENBERG-2/` before its first formal execution.

The current cross-branch source of truth is
`LI-COCYCLE-LANE_CONSOLIDATION_2026-07-16.md`.

The next L6 shape protocol is preserved as
`P-J-LI-FEJER-CARRIER-1_PREREG_DRAFT.md`.  It remains
`BLOCKED-PREDEFINITION` until one explicit J-native carrier is frozen.

## 1. Preserved bytes and provenance

```text
verify.py
  sha256  170cb04a33a717e9f637b1948b81f01fba0414b86e0c082a2034bb398061bb8f
  bytes   8773
  lines   300

EXPECTED.txt
  sha256  1dff821424280361ec15ebbb2e405d7e6b4d452d820aeefcd2e8d966cb8992e3
  bytes   1057
  lines   18
```

The original attached result narrative had SHA-256
`a83075914bab2d09842b329366d35b385886263dbb8a27a049dd37ceed926892`,
8601 bytes, and 284 lines. It is superseded by this corrected document because
its complex-coefficient CND proof used one modulus where two are required.

The preserved verifier has no floating-point constants, network access,
subprocesses, file writes, random input, zero list, or prime table. Its positive
assertions use fixed-point integer interval arithmetic. A historical interval
appears only in the negative control `NC` and cannot make gates `S1` through
`S5` pass.

Audit reproductions of these exact bytes reported:

```text
Linux x86_64, Python 3.12.3:  exit 0, 6/6 PASS, stdout byte-identical
Linux aarch64, Python 3.12.3: exit 0, 6/6 PASS, stdout byte-identical
```

The final line inside `EXPECTED.txt` still says `single architecture` because
editing it would destroy the preserved hash. The surrounding provenance above
records the later second-architecture reproduction. This makes the finite
certificate candidate-T-ready under repository policy, not publicly T.

The separate rev3 amendment-2 verifier reported elsewhere with prefix
`38c0f823` is not claimed or reconstructed here. This directory preserves only
the exact `170cb04a` branch so another environment can cross-check it.

## 2. Normalized RH target

The analytic target is the normalized function

\[
Z_J(s)=\zeta(s),
\qquad
\xi_J(s)=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)Z_J(s)=\xi(s).
\]

The raw pentagon root-filter function is not used as the Weil carrier without
subtracting its filter divisor. This bundle begins after that normalization.

Define the Li coefficients by

\[
\lambda_n
=
\frac{1}{(n-1)!}
\left.
\frac{d^n}{ds^n}
\left(s^{n-1}\log\xi_J(s)\right)
\right|_{s=1},
\qquad n\ge1,
\]

and extend them by

\[
\lambda_0=0,
\qquad
\lambda_{-n}=\lambda_n.
\]

Li's criterion is imported in its standard form:

\[
\mathrm{RH}
\iff
\lambda_n\ge0
\quad\text{for every }n\ge1.
\]

Reference: Xian-Jin Li, *The Positivity of a Sequence of Numbers and the
Riemann Hypothesis*, Journal of Number Theory 65 (1997), 325-333,
doi:10.1006/jnth.1997.2137.

## 3. Conditional negative definiteness

Put

\[
c_n^{\mathrm{Li}}
:=
\lambda_{n+1}+\lambda_{n-1}-2\lambda_n.
\]

The following theorem is the positive normal form used by this candidate:

\[
\boxed{
\begin{aligned}
\mathrm{RH}
&\iff (\lambda_n)_{n\in\mathbb Z}
       \text{ is conditionally negative definite}\\
&\iff K_N\succeq0\quad\text{for every }N\ge1\\
&\iff (c_n^{\mathrm{Li}})_{n\in\mathbb Z}
       \text{ is positive definite}\\
&\iff T_N\succeq0\quad\text{for every }N\ge0.
\end{aligned}}
\]

Here

\[
K_N(i,j)
=
\frac{\lambda_i+\lambda_j-\lambda_{|i-j|}}{2},
\qquad 1\le i,j\le N,
\]

and

\[
T_N(i,j)=c_{i-j}^{\mathrm{Li}},
\qquad 0\le i,j\le N.
\]

### RH implies CND

Under RH, for every nontrivial zero \(\rho\), counted with multiplicity,

\[
u_\rho=1-\frac1\rho
\]

has unit modulus. Pairing conjugate zeros gives, for each fixed \(n\),

\[
\lambda_n
=
2\sum_{\operatorname{Im}\rho>0}
\left(1-\cos(n\theta_\rho)\right).
\]

This paired sum is absolutely convergent under RH because

\[
2(1-\cos\theta_\rho)=|1-u_\rho|^2=|\rho|^{-2},
\]

\[
1-\cos(n\theta)\le n^2(1-\cos\theta),
\qquad
\sum_{\operatorname{Im}\rho>0}|\rho|^{-2}<\infty.
\]

For finitely supported complex coefficients with \(\sum_k a_k=0\), the exact
identity is

\[
\begin{aligned}
&\sum_{k,l}a_k\overline{a_l}
\left(1-\cos((k-l)\theta)\right)\\
&\quad=
-\frac12\left(
\left|\sum_k a_ke^{\mathrm i k\theta}\right|^2
+
\left|\sum_k a_ke^{-\mathrm i k\theta}\right|^2
\right)
\le0.
\end{aligned}
\]

The one-modulus version is valid only when the coefficients are real or obey
an equivalent symmetry. Therefore every summand is CND and so is
\((\lambda_n)\).

### CND implies RH

The two-point test on \(\{0,n\}\) with coefficients \((1,-1)\) gives

\[
-2\lambda_n\le0,
\]

hence \(\lambda_n\ge0\) for every \(n\). Li's criterion then gives RH.

### Discrete derivative and finite matrices

For a finitely supported sequence \(a\), set

\[
d_i=a_i-a_{i-1}.
\]

Then

\[
\sum_{i,j}d_i\overline{d_j}\lambda_{i-j}
=
-\sum_{i,j}a_i\overline{a_j}c_{i-j}^{\mathrm{Li}}.
\]

Every finitely supported zero-sum sequence \(d\) arises this way. This proves
the equivalence of CND for \(\lambda\) and positive definiteness for \(c\).

Let \(L_N\) be the invertible lower triangular \(N\times N\) matrix of ones.
The exact finite-level identity is

\[
\boxed{
K_N=\frac12L_NT_{N-1}L_N^*.
}
\]

Since \(L_N\) is unimodular,

\[
K_N\succeq0
\iff
T_{N-1}\succeq0.
\]

In particular, \(K_2\) and \(T_1\) are the same positivity gate under
congruence.

## 4. Unitary cocycle normal form

Positive definiteness of \(c^{\mathrm{Li}}\) gives a GNS representation. After
the normalization \(v=w/\sqrt2\), there are a Hilbert space \(\mathcal H\), a
unitary \(U\), and a vector \(v\) such that

\[
c_n^{\mathrm{Li}}
=
2\operatorname{Re}\langle v,U^n v\rangle.
\]

Define

\[
b(n)=\sum_{k=0}^{n-1}U^k v.
\]

The shared initial values and second differences give

\[
\boxed{
\lambda_n=\|b(n)\|^2
=
\left\|
\sum_{k=0}^{n-1}U^k v
\right\|^2
\quad\text{for every }n\ge1.
}
\]

Thus the bare existence of some such triple is equivalent to RH. The stronger
obligation to derive one uniformly and canonically from the declared
\(J\)-architecture, without inserting \(\zeta\), its zeros, a prime table, or
the standard Weil form, remains open:

```text
J-LI-COCYCLE-REALIZATION [O]
RH                      [O]
```

The adjective `J-native` is an additional construction requirement. It is not
part of the abstract GNS equivalence.

The cyclic carrier cannot be finite-dimensional. The proof and the sharper
spectral boundary are recorded in `CYCLIC_CARRIER_DIMENSION.md`: any uniform
all-\(n\) realization must have infinite cyclic spectral support, with \(1\)
as a non-atomic accumulation point. `ATOM_TEST.md` fixes the normalization
between the spectral measure \(\mu_v\) and its real-even symmetrization
\(\sigma\), and gives the exact equivalent tests

\[
\mu_v(\{1\})=0
\iff
\lambda_{N+1}-\lambda_N=o(N)
\iff
\lambda_n=o(n^2).
\]

It does not justify the stronger first-difference asymptotic
\(\lambda_{N+1}-\lambda_N\sim\tfrac12\log N\).
`FEJER_SCALING.md` records the correct stronger averaged statement: every
exact all-\(n\) Li cocycle has logarithmically divergent Fejér means, no atom
at \(1\), and non-\(\ell^1\) correlations.  A pointwise logarithmic density
requires an additional regularity ansatz.

## 5. First joint finite gate

The first nontrivial Schoenberg matrix and its Toeplitz counterpart are

\[
K_2=
\begin{pmatrix}
\lambda_1 & \lambda_2/2\\
\lambda_2/2 & \lambda_2
\end{pmatrix},
\]

\[
T_1=
\begin{pmatrix}
2\lambda_1 & \lambda_2-2\lambda_1\\
\lambda_2-2\lambda_1 & 2\lambda_1
\end{pmatrix}.
\]

The eigenvalues of \(T_1\) are

\[
\lambda_2,
\qquad
4\lambda_1-\lambda_2,
\]

and

\[
\det K_2
=
\frac{\lambda_2(4\lambda_1-\lambda_2)}4.
\]

The preserved verifier proves the outward-rounded intervals

\[
\lambda_1\in
[0.023095708961954367122470,
 0.023095708986954117175621],
\]

\[
\lambda_2\in
[0.092345734996397184208007,
 0.092345735454548522783894],
\]

\[
4\lambda_1-\lambda_2\in
[0.000037100393268945705986,
 0.000037100951419284494477],
\]

\[
\det K_2\in
[0.000000856515771269044502,
 0.000000856528661219325620].
\]

Both eigenvalues are strictly positive. This proves only the named finite
gate. No finite prefix is evidence for the all-\(n\) obligation.

## 6. The compact Phi_10 exemplar

For the four primitive tenth roots, define

\[
\psi_A(n)
=
\sum_{\zeta\text{ primitive }10}
\left(1-\operatorname{Re}\zeta^n\right).
\]

Then

\[
\psi_A(n)=4-c_{10}(n)\in\{0,3,5,8\}.
\]

This sequence is CND and all its Schoenberg matrices are positive
semidefinite. They are not generally positive definite because the sequence
is periodic and \(\psi_A(10)=0\). The algebraic statement is exact. Reading
this finite compact sector as an exemplar of the full Li wall is a derived
interpretation and supplies no lift to \(\xi\).

## 7. Artin determinant and Fock carrier

Let \(K=\mathbb Q(\zeta_5)\), \(G\cong C_4\), and
\(V=\mathbb C[C_4]\). For a rational prime \(\ell\ne5\), let \(F_\ell\)
be Frobenius in the regular representation and put

\[
f_\ell=\operatorname{ord}_5(\ell).
\]

Then

\[
\det(I-xF_\ell)
=(1-x^{f_\ell})^{4/f_\ell}
=
\prod_{\chi\in\widehat{C_4}}
(1-\chi(\ell)x).
\]

Thus the unramified local factors are

\[
\begin{array}{c|c}
\ell\bmod5 & \det(I-xF_\ell)^{-1}\\
\hline
1 & (1-x)^{-4}\\
4 & (1-x^2)^{-2}\\
2,3 & (1-x^4)^{-1}.
\end{array}
\]

At the ramified prime \(5\), the regular representation remains
four-dimensional, but

\[
V^{I_5}\cong\mathbb C.
\]

Frobenius acts trivially on this one-dimensional inertia-invariant block and
the local factor is

\[
(1-5^{-s})^{-1}.
\]

Write \(\mathbf1_G\) for the trivial Artin character of \(G\cong C_4\),
and write \(\chi_0^{(5)}\) for the principal Dirichlet character modulo \(5\).
They must not share one symbol:

\[
L(s,\mathbf1_G)=\zeta(s),
\qquad
L(s,\chi_0^{(5)})=(1-5^{-s})\zeta(s).
\]

The two equivalent global conventions are

\[
\zeta_K(s)
=
\zeta(s)\prod_{r=1}^3L(s,\chi_r),
\]

and, in the residue-character convention,

\[
\zeta_K(s)
=
(1-5^{-s})^{-1}
L(s,\chi_0^{(5)})\prod_{r=1}^3L(s,\chi_r).
\]

The connection with the additive root-filter correction
\(4\mathbf1_{5\mid n}\) is a structural analogy only. The two constructions
repair blindness to the ramified residue class, but their coefficients are not
the same local identity.

The symmetric-Fock and trace-log presentations are

\[
\operatorname{Tr}_{\operatorname{Sym}^{\bullet}V}
\left(x^{\mathsf N}\Gamma_s(F)\right)
=
\det(I-xF)^{-1},
\]

as a formal series, or analytically for \(|x|<1\), and

\[
\det(I-xF)^{-1}
=
\exp\left(
\sum_{m\ge1}\frac{x^m}{m}\operatorname{Tr}(F^m)
\right).
\]

Therefore a blanket no-go for trace realizations is false. The falsified
additive route is only

\[
\sum_\chi L(s,\chi)\ne\zeta_K(s).
\]

Its status-neutral identifier is

```text
IDEAL-PACKET-BY-ADDITIVE-SECTOR-SUM
```

with proposed mathematical classification `[F]` if later registered.

## 8. Sector boundary

The full Artin packet and the Riemann target must not share one ambiguous
Hilbert-space symbol. Use

\[
\mathcal H_K
\quad\text{for the full Dedekind or Artin packet},
\]

and

\[
\mathcal H_\xi=\mathcal H_{\mathbf1_G}
\quad\text{for the completed trivial Artin sector, including its block at }5.
\]

Over a real Hilbert space, the isotypic decomposition has the form

\[
\mathcal H_K
=
\mathcal H_{\mathbf1_G}
\oplus
\mathcal H_{\chi_2}
\oplus
\mathcal H_{\chi_1\oplus\chi_3}.
\]

The quartic characters are paired by the real structure and the requirement
of real moments, not by positivity itself. For a cocycle sector decomposition,
the \(C_4\) action must commute with the unitary dynamics and the sector
projections must preserve that dynamics.

Exact positivity of the correct global form for \(\zeta_K\) would imply RH for
\(\zeta\), since the Riemann factor occurs in the Artin product. It would not,
by itself, identify or construct the specific form \(W_\xi\) on the trivial
sector. Those are distinct targets.

## 9. Candidate ledger

Nothing in this table is publicly registered by this file.

| Identifier | Candidate classification | Exact scope |
| --- | ---: | --- |
| `J-LI-CND-EQUIVALENCE` | mathematical T | RH iff the even Li sequence is CND |
| `J-LI-TOEPLITZ-EQUIVALENCE` | mathematical T | RH iff every Li second-difference Toeplitz matrix is PSD |
| `J-LI-COCYCLE-NORMAL-FORM` | T as equivalence | abstract unitary cocycle norm form |
| `J-LI-CYCLIC-CARRIER-DIMENSION` | mathematical T | every uniform all-(n) unitary realization has infinite cyclic dimension |
| `J-LI-ATOM-TEST` | T as equivalence | atom at 1 iff the Li growth has a quadratic component; no atom iff increments are \(o(n)\) |
| `J-LI-FEJER-SCALING` | T as necessary implication | exact all-\(n\) Li cocycle forces logarithmic Fejér means and non-\(\ell^1\) moments |
| `J-LI-MOMENT-BRIDGE` | O | all-\(m\) identification of independently constructed J moments with Li second differences |
| `FEJER-SHAPE-IMPLIES-LI-MOMENTS` | proposed F | mass, atomlessness, and Fejér scaling do not determine the Fourier moment sequence |
| `COCYCLE-BY-FINITE-FIT` | proposed F, scoped | false only for one fixed finite spectral carrier claimed to realize every \(n\); finite-prefix fits remain allowed |
| `J-ARTIN-FROBENIUS-DETERMINANT` | mathematical T | unramified local determinant plus the separate inertia-invariant block at 5 |
| `J-ARTIN-SYMMETRIC-FOCK` | mathematical T | graded trace equals reciprocal determinant |
| `J-PHI10-SCHOENBERG-EXEMPLAR` | T algebraically, D as reading | finite compact exemplar only |
| `J-LI-SCHOENBERG-2` | candidate-T-ready | exact finite gate, two-architecture output reported and preserved |
| `J-LI-SCHOENBERG-3` | candidate-T-ready | exact \(T_2\)/\(K_3\) interval gate, two architectures; see `LAMBDA3_T2.md` |
| `J-LI-COCYCLE-REALIZATION` | O | uniform J-native construction without hidden import |
| `IDEAL-PACKET-BY-ADDITIVE-SECTOR-SUM` | proposed F | additive sum is not the Artin product |
| `RH` | O | all nontrivial zeta zeros on the critical line |

## 10. Live falsifiers and promotion boundary

The proposed realization fails if any of the following occurs:

1. a local determinant disagrees with the required Euler factor;
2. the ramified block at \(5\) is omitted or double-counted;
3. the trigonometric CND identity is used with one modulus for unrestricted
   complex coefficients;
4. the proposed trivial sector fails to reproduce \(\xi_J=\xi\), including
   the archimedean term, poles, trivial zeros, and von Mangoldt coefficients;
5. an exact admissible finite matrix is not positive semidefinite;
6. a proposed uniform all-\(n\) carrier has finite cyclic spectral support;
7. a proposed all-\(n\) carrier has positive spectral mass at \(1\), or fails
   the equivalent \(o(n)\) increment and \(o(n^2)\) growth tests;
8. \(\zeta\), a zero list, a prime table, or the standard Weil form enters as
   a hidden input to a claimed J-native realization.

A negative matrix before the exact sector identity is established falsifies
the proposed realization. A negative matrix after that identity is proved
would falsify the corresponding Li positivity statement and hence RH.

For public work, create a fresh branch and five-file probe bundle:

```text
branch: probe/P-J-LI-SCHOENBERG-2
path:   probes/P-J-LI-SCHOENBERG-2/

PREREG.md
verify.py
EXPECTED.txt
RUN.md
RESULT.md
```

`PREREG.md` and the accepted verifier must be committed and pushed before the
first formal execution. The runs recorded in this incubation bundle are audit
witnesses only and must not be relabeled as formal probe runs.

## Verdict

```text
POSITIVE NORMAL FORM              mathematical T as an RH equivalence
CYCLIC CARRIER DIMENSION          infinite in every all-n realization
ATOM AT 1                         absent in every all-n realization
FIRST JOINT SCHOENBERG GATE       exact two-architecture audit certificate
SECOND JOINT SCHOENBERG GATE      exact two-architecture incubation certificate
PUBLIC REGISTRATION               absent
J-NATIVE UNIFORM COCYCLE          O
RH                                O
```
