# C-J-POLYLOG-RENORMALIZED-SEAM-1-N

```text
STATUS:       NON-CANONICAL INCUBATION NOTE
AUTHORITY:    none
PUBLIC BASIS: Public Canon v46, mathorn1973/twist-j main
ISSUE LOCK:   #362
LAYER:        classical complex analysis and analytic number theory only;
              no L1-L6 lift
COMPUTATION:  none
PROMOTION:    none
```

This note records one exact coordinate package around the principal
polylogarithm, the projective map `z -> 1/(1-z)`, and the point

```text
j   = zeta_5,
phi = (1+sqrt(5))/2,
J   = 1+j^2 = j/phi.
```

It creates no public claim, Registry row, probe permission, evidence, or
status change. All candidate labels below are non-canonical working labels.
RH remains open.

The owner supplied the candidate derivation before issue #362 was opened.
That exposed preparation is disclosed rather than retroactively described as
preregistered work. The value of this note is its corrected scope, branch and
domain audit, and collision map.

## 1. Public basis and collision boundary

At the lock, `STATUS.md` declared:

```text
STATE:          ACTIVE
CANON:          Public Canon v46
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v46
CONTENT_COMMIT: 62628ca4da2d938e4e3a122d35c0d93a6debc27f
CANON_SHA256:   6c57e714c441bd679b9f6c673352cfae44ac993433d7c4624cd9c3c93df291ff
CANON_BYTES:    222760
main snapshot:  6545c1d0de61ff4696eb3de1a258139e8891f436
```

The tag resolves to the displayed activation commit, the content commit is
its ancestor, the Canon hash and byte count agree, and the policy, Canon, and
ledger checks pass.

This note must not absorb or silently restate the following public scopes.

[PUBLIC T] `PI-FROM-J` owns the principal-branch identity

```text
1-J = -j^2 = exp(-i pi/5),
Li_1(J) = -Log(1-J) = i pi/5.
```

[PUBLIC T] `J-HARMONIC-SEAM` owns the exact harmonic series, its torsion-axis
landings, the unit-group statement, and

```text
Log J = -log phi + 2 pi i/5.
```

It is not the public owner of `Li_1(J)`.

[PUBLIC T] `ELECTRON-G-RATIO` already owns the exact
`Li_{-1}, Li_0, Li_1` ladder at `J`. Consequently the low-order identities
below are collision context, not novelty.

[PUBLIC T] `WALL-LI2-RUNG` and `WALL-CIRCLE-LEMMA` own the principal
dilogarithm real-part identities, including

```text
Re Li_2(J) = pi^2/100,
```

and the corresponding algebraic-argument values. They make no
imaginary-part claim and no field-trace claim for transcendental values.

[PUBLIC T] `PENTAGON-NORMALIZATION` owns the exact root-filter identity

```text
P_0(s) = (5^(1-s)-1) zeta(s),   Re(s)>1,
```

and its named classical continuation and completion. It supplies no new
Mellin carrier, Weil positivity, or RH result.

[PUBLIC T/H] `LAMBDA-COCYCLE-GRID-EQUIVALENCE` and
`LAMBDA-COCYCLE-ANGLES` already own the exact lambda-adic grid and the
stronger cocycle-vector hypothesis. This note neither consumes nor
strengthens them.

[NON-CANONICAL SIBLING] `notes/C-J-DEDEKIND-WEIL-ROAD-N.md` already records
the branch-free defect `log|1-wx|` and its critical-line mirror. The present
note adds a typed polylogarithmic coordinate and edge renormalization; it does
not replace that roadmap.

Toeplitz positivity and the `Z_5` Fourier normal form are deliberately
excluded. They belong to issue #363 and its separate incubation path.

## 2. Frozen branches and notation

Use the standard archimedean embedding and the principal logarithm. Put

```text
ell := Log J = -log phi + 2 pi i/5,
a   := -ell = log phi - 2 pi i/5.
```

Thus `Re(a)>0`. For complex `t`, define

```text
J^t := exp(t ell).
```

`Li_s(z)` denotes the principal polylogarithm, agreeing with

```text
Li_s(z) = sum_(n>=1) z^n/n^s
```

for `|z|<1`. Principal `Li_2` has its standard cut along `[1,infinity)`.

Every power such as `(-u ell)^(s-1)` below means

```text
exp((s-1) Log(-u ell))
```

with the stated fixed branch. No identity is asserted across an unstated
branch change.

## 3. The low-order projective closure

[NON-CANONICAL candidate-T, classical repackaging]

For `z != 1`,

```text
Li_0(z) = z/(1-z),
1+Li_0(z) = 1/(1-z).
```

On any domain carrying the selected branch of `Li_1(z)=-Log(1-z)`,

```text
exp(Li_1(z)) = 1/(1-z).
```

Define the projective Mobius transformation

```text
f(z) := 1/(1-z).
```

On `P^1(C)`,

```text
f^2(z) = (z-1)/z,
f^3(z) = z.
```

The exceptional projective cycle is `1 -> infinity -> 0 -> 1`.

For the distinguished point `J`,

```text
f(J)   = exp(i pi/5) = -j^3,
f^2(J) = phi j,
f^3(J) = J.
```

Thus

```text
J  ->  exp(i pi/5)  ->  phi j  ->  J
```

has radii

```text
phi^-1  ->  1  ->  phi  ->  phi^-1.
```

Complex conjugation gives the second triangle. The complete six-point
anharmonic orbit is

```text
{J, conjugate(J), J^-1, conjugate(J)^-1,
 exp(i pi/5), exp(-i pi/5)}.
```

The package is exact, but its low-order polylogarithmic content is already
inside `PI-FROM-J` and `ELECTRON-G-RATIO`.

## 4. The J-Cayley coordinate

For every `z != 1`,

```text
Re(1/(1-z)) - 1/2
  = (1-|z|^2)/(2|1-z|^2).
```

Hence `f` maps the unit disk, the punctured unit circle `|z|=1, z!=1`,
and the exterior respectively to

```text
Re(s)>1/2,   Re(s)=1/2,   Re(s)<1/2.
```

For `alpha notin 2 pi Z`,

```text
f(exp(i alpha))
  = 1/2 + (i/2) cot(alpha/2).
```

Define the meromorphic `J`-Cayley trajectory

```text
C_J(t) := f(J^t) = 1/(1-exp(t ell))
```

on

```text
D_J := C minus (2 pi i/ell) Z.
```

It has period

```text
T_J = 2 pi i/ell
```

and satisfies, for `t in D_J`,

```text
C_J(-t) = 1-C_J(t).
```

For the completed Riemann function

```text
xi_R(s)
 = (1/2)s(s-1) pi^(-s/2) Gamma(s/2) zeta(s),
```

the classical functional equation therefore gives

```text
xi_R(C_J(-t)) = xi_R(C_J(t)).
```

This is a coordinate form of the existing functional equation, not a new
functional equation. At the excluded period lattice `C_J` has poles and the
composition generally has essential singularities.

Since

```text
|J^t| = exp(Re(t ell)),
```

one has, away from the pole lattice,

```text
Re C_J(t)=1/2
  iff Re(t ell)=0.
```

Writing

```text
t_alpha = i alpha/ell
```

gives

```text
J^(t_alpha) = exp(i alpha),
C_J(t_alpha) = 1/2 + (i/2)cot(alpha/2).
```

For `gamma>0`, the inverse representative in `(0,pi)` is

```text
alpha = 2 arctan(1/(2 gamma)).
```

For arbitrary real `gamma`, the angle is understood modulo `2 pi`, or is
selected with an `atan2`/`arccot` convention.

## 5. Radial and angular zero data are distinct

For a nontrivial zero `rho=beta+i gamma`, put

```text
w_rho := 1-1/rho.
```

Then

```text
rho = 1/(1-w_rho),

1-|w_rho|^2
  = (2 beta-1)/|rho|^2.
```

Consequently

```text
beta=1/2  iff  |w_rho|=1.
```

All preimages in the `J` coordinate are

```text
t_(rho,k)
  = (Log w_rho + 2 pi i k)/ell,   k in Z,
```

where one branch of `Log w_rho` is fixed before adding the complete
`2 pi i k` family. They obey

```text
Re(t_(rho,k) ell) = log|w_rho|.
```

Thus RH is exactly the radial condition `log|w_rho|=0`. Membership of the
angle in

```text
2 pi (1/4) Z[1/5]
```

is a separate, stronger torsion condition already owned by
`LAMBDA-COCYCLE-ANGLES [H]`. No torsion statement follows from the coordinate
change itself.

## 6. Mellin transform of the J-ray

[NON-CANONICAL candidate-T, exact termwise derivation]

For `u>0`,

```text
J^u = exp(-a u),   Re(a)>0.
```

If

```text
Re(q)>0,
Re(s+q)>1,
```

absolute convergence permits interchange of sum and integral:

```text
integral_0^infinity u^(q-1) Li_s(J^u) du
  = Gamma(q) a^(-q) zeta(s+q).
```

Here

```text
a^(-q) = exp(-q Log a)
```

uses the principal logarithm; this is unambiguous because `Re(a)>0`.

At `s=0`,

```text
Li_0(J^u)
  = J^u/(1-J^u)
  = C_J(u)-1.
```

Therefore, for `Re(q)>1`,

```text
zeta(q)
  = a^q/Gamma(q)
    integral_0^infinity u^(q-1)(C_J(u)-1) du.
```

The proof is only the gamma integral applied termwise. It is not a native
derivation of zeta, an Euler product, or a positivity theorem.

The Mellin identity does not select `J`: the same calculation works with any
complex `a` satisfying `Re(a)>0`. The special `J` data are instead

```text
1-J in mu_10,
C_J(1)=exp(i pi/5),
```

and the exact three-cycle in `Q(zeta_5)`.

## 7. Renormalized polylogarithmic edge

The raw limit

```text
Li_s(J^u) -> zeta(s),   u -> 0+,
```

holds directly only in the ordinary convergence half-plane `Re(s)>1`. It is
false on the critical strip.

For

```text
s notin {1,2,3,...}
```

Choose a sufficiently small simply connected complex sector `S` about the
positive `u` ray, with its vertex removed, so that throughout `S`

```text
Log(exp(u ell)) = u ell,
|u ell| < 2 pi,
```

Jonquiere's expansion gives

```text
Li_s(exp(u ell))
  = Gamma(1-s)(-u ell)^(s-1)
    + sum_(k>=0) zeta(s-k)(u ell)^k/k!.
```

On the central positive ray, an explicit safe range is `0<u<5/2`. There

```text
Log(exp(u ell))=u ell
```

and principal `Log(-u ell)=log u+Log(-ell)` remains fixed.

Define

```text
R_J(s,u)
  := Li_s(J^u)-Gamma(1-s)(-u ell)^(s-1).
```

On `S`, fix `Log u` continuously and hence
`Log(-u ell)=Log u+Log(-ell)`. The power series below gives a removable,
holomorphic continuation to `u=0` in the sector germ:

```text
R_J(s,u)
  = sum_(k>=0) zeta(s-k)(u ell)^k/k!,

R_J(s,0)=zeta(s).
```

It also satisfies

```text
partial_u R_J(s,u)
  = ell R_J(s-1,u),
```

and hence

```text
partial_u^k R_J(s,0)
  = ell^k zeta(s-k).
```

These are derivatives along the selected `J`-ray parameter `u`; they are not
geometric normal derivatives without an independently defined surface metric
and normal bundle.

The series is jointly holomorphic in `(s,u)` on a neighborhood of
`(rho,0)` for every nontrivial zero `rho`. If `rho` is simple, the complex
implicit-function theorem gives a local zero branch `rho_J(u)` of
`R_J(s,u)` with

```text
rho_J(0)=rho,

rho_J'(0)
  = -ell zeta(rho-1)/zeta'(rho).
```

No tangency to the critical line is asserted. In particular, the formula does
not support a claim that the natural `J` deformation preserves RH.

Positive integral orders require the standard limiting logarithmic formulas
and are outside the displayed Jonquiere scope.

## 8. Weight-two closure

Define the Bloch-Wigner function

```text
D(z)
  = Im Li_2(z)+log|z| Arg(1-z).
```

Its classical anharmonic identities include

```text
D(z)=D(1/(1-z)).
```

Because

```text
1/(1-J)=exp(i pi/5),
```

one gets

```text
D(J)
  = D(exp(i pi/5))
  = Cl_2(pi/5).
```

Using the public real-part identity

```text
Re Li_2(J)=pi^2/100
```

and

```text
log|J|=-log phi,
Arg(1-J)=-pi/5,
```

gives the full principal value

```text
Li_2(J)
  = pi^2/100
    + i(Cl_2(pi/5)-pi log(phi)/5).
```

This adds only the classical imaginary-part completion; it does not alter the
scope of `WALL-LI2-RUNG`.

For `0<=theta<=2 pi`,

```text
Re Li_2(exp(i theta))
  = pi^2/6-theta(2 pi-theta)/4.
```

Thus

```text
zeta(2)-Re Li_2(exp(i pi/5)) = 9 pi^2/100,
zeta(2)-Re Li_2(j)           = 16 pi^2/100.
```

If `sigma_2` denotes the algebraic embedding of the argument `j -> j^2`,
followed by evaluation of the principal analytic dilogarithm, the public
value

```text
Re Li_2(sigma_2(J))=9 pi^2/100
```

yields

```text
Re Li_2(sigma_2(J))
  + Re Li_2(exp(i pi/5))
  = zeta(2).
```

This is not Galois conjugation of a transcendental `Li_2` value and is not a
field-trace statement.

## 9. Li energy on the Cayley circle

[NON-CANONICAL candidate-T, classical corollary]

Let `lambda_n` be the standard Li coefficients. The zero formula is read with
multiplicities and symmetric truncation in `|Im rho|`; an unpaired zero sum is
not asserted to be absolutely convergent:

```text
lambda_n
 = lim_(T->infinity) sum_(|Im rho|<=T)
     (1-(1-1/rho)^n).
```

Under RH, write for each positive ordinate

```text
w_rho = exp(i alpha_gamma),
alpha_gamma = 2 arctan(1/(2 gamma)).
```

Pairing conjugate zeros gives, with multiplicities,

```text
lambda_n
  = 2 sum_(gamma>0)(1-cos(n alpha_gamma)).
```

For each fixed `n` this paired sum is absolutely convergent. For real `r>2`,
Tonelli's theorem and the absolutely convergent polylogarithm series give

```text
sum_(n>=1) lambda_n/n^r
  = 2 sum_(gamma>0)
      (zeta(r)-Re Li_r(exp(i alpha_gamma))).
```

Under RH the standard asymptotic

```text
lambda_n
  = (n/2)(log n - 1 + EulerGamma - log(2 pi)) + o(n)
```

shows that the finite convergence range is exactly `r>2`. For `r<=2` the
left side diverges, and for `1<r<=2` the right side may only be read as
`+infinity`, not as a finite exchange identity.

The following ordinary-convergence criterion is exact:

```text
RH
  iff there exists a real r for which
      sum_(n>=1) lambda_n/n^r converges ordinarily.
```

The forward direction follows from the standard RH growth of `lambda_n`.
For the reverse direction, ordinary convergence for `r=r_0` implies
`lambda_n=O(n^(r_0))`. Hence

```text
F(z)=sum_(n>=1) lambda_n z^n/n
```

has radius at least one. Its germ at zero is the Keiper logarithm

```text
F(z)
  = log(xi_R(1/(1-z))/xi_R(1)),
```

with the branch normalized by `F(0)=0`. By analytic continuation in the unit
disk,

```text
exp(F(z))
  = xi_R(1/(1-z))/xi_R(1).
```

The left side has no zeros, so `xi_R` has no zero in `Re(s)>1/2`. Its
functional equation then excludes `Re(s)<1/2`, proving RH.

This is a short classical consequence of the Keiper generating function and
Li/Bombieri-Lagarias criterion. It is not a new RH advance.

## 10. Mellin transform of the Li generating function

Assume RH. Let `L(s)` be the unique holomorphic logarithm of

```text
xi_R(s)/xi_R(1)
```

on `Re(s)>1/2`, normalized by `L(1)=0`. A pointwise principal logarithm is not
used. For `u>0`, define

```text
G_J(u) := L(C_J(u)).
```

Since `|J^u|<1`, the Keiper series gives

```text
G_J(u)
  = sum_(n>=1) lambda_n J^(u n)/n.
```

For real `q>1`, absolute convergence permits termwise Mellin integration:

```text
integral_0^infinity u^(q-1) G_J(u) du
  = Gamma(q) a^(-q)
    sum_(n>=1) lambda_n/n^(q+1).
```

The range `q>1` is sufficient for the identity. Combining with the circle
energy in section 9 gives

```text
integral_0^infinity u^(q-1)
  log_hol(xi_R(C_J(u))/xi_R(1)) du

  = 2 Gamma(q) a^(-q)
    sum_(gamma>0)
      (zeta(q+1)-Re Li_(q+1)(exp(i alpha_gamma))),

q>1.
```

The subscript `hol` emphasizes the normalized holomorphic logarithm. This
formula packages known Li/zero data in the `J` coordinate; it neither creates
the zero data nor yields a new positivity mechanism.

## 11. Exact scope and hard brakes

The candidate theorem package consists only of:

```text
P1  the order-three Mobius orbit and its exact J triangle;
P2  the J-Cayley coordinate, pole lattice, reflection, and critical-line
    preimage;
P3  the Mellin transform on the stated absolute-convergence domain;
P4  the branch-frozen renormalized edge and simple-zero velocity;
P5  the classical Bloch-Wigner/Clausen completion at weight two;
P6  the classical Li-energy and normalized-log Mellin repackaging.
```

The following are explicitly false or outside scope.

```text
F1  Li_s(J^u) tends to zeta(s) on the critical strip without subtraction.
F2  the Mellin identity selects p=5 or J uniquely.
F3  Li_s(J) has an Euler product or multiplicative coefficients.
F4  exp(i pi/5) is thereby identified with a zeta-zero Cayley phase.
F5  the J-ray zero deformation preserves the critical line.
F6  the package proves, supports, or falsifies RH; every use of RH in P6 is
    explicitly conditional.
F7  the package creates a physical bridge or an L1-L6 lift.
```

For `b(n)=J^n`, multiplicativity already fails at `b(1)=J!=1`. Even if that
normalization were ignored, the coprime pair `(2,3)` would require

```text
J^6=J^2 J^3=J^5,
```

which fails in general. Therefore no prime-place structure follows from the
single `J` polylogarithm.

## 12. Novelty boundary and sources

The two-variable polylogarithm/Lerch surface, its multivalued continuation,
the singular stratum at `z=1`, the Li generating function, and the zero
criterion are classical. The only proposed project contribution is the exact
packaging of the `J`-Cayley coordinate, its Mellin transform, and the
branch-frozen renormalized germ against the existing Public Canon claims. No
novelty in general polylogarithm or Li-coefficient analysis is claimed.

Primary and standard source pins:

1. NIST DLMF section 25.12:
   - series definition: <https://dlmf.nist.gov/25.12.E10>;
   - Jonquiere edge expansion: <https://dlmf.nist.gov/25.12.E12>;
   - unit-circle real and imaginary parts:
     <https://dlmf.nist.gov/25.12.E7>,
     <https://dlmf.nist.gov/25.12.E8>,
     <https://dlmf.nist.gov/25.12.E9>.
2. L. C. Maximon, *The Dilogarithm Function for Complex Argument*,
   Proc. R. Soc. A 459 (2003), 2807-2819,
   <https://doi.org/10.1098/rspa.2003.1156>.
3. D. Zagier, *The Bloch-Wigner-Ramakrishnan Polylogarithm Function*,
   Math. Ann. 286 (1990), 613-624,
   <https://archive.mpim-bonn.mpg.de/id/eprint/270/>.
4. J. C. Lagarias and W.-C. W. Li,
   *The Lerch Zeta Function III. Polylogarithms and Special Values*,
   Research in the Mathematical Sciences 3 (2016), article 2,
   <https://doi.org/10.1186/s40687-015-0049-2>,
   <https://arxiv.org/abs/1506.06161>.
5. J. B. Keiper, *Power Series Expansions of Riemann's Xi Function*,
   Math. Comp. 58 (1992), 765-773,
   <https://doi.org/10.1090/S0025-5718-1992-1122072-5>.
6. X.-J. Li, *The Positivity of a Sequence of Numbers and the Riemann
   Hypothesis*, J. Number Theory 65 (1997), 325-333,
   <https://doi.org/10.1006/jnth.1997.2137>.
7. E. Bombieri and J. C. Lagarias, *Complements to Li's Criterion for the
   Riemann Hypothesis*, J. Number Theory 77 (1999), 274-287,
   <https://doi.org/10.1006/jnth.1999.2392>.
8. J. C. Lagarias, *Li Coefficients for Automorphic L-Functions*,
   Ann. Inst. Fourier 57 (2007), 1689-1740, Theorem 1.1,
   <https://doi.org/10.5802/aif.2311>,
   <https://arxiv.org/abs/math/0404394>.

## 13. Promotion boundary

This remains one notes-only classical synthesis under issue #362. It
authorizes no formal gate. Any future claim must be separately locked, must
preserve every public owner in section 1, and must not combine this package
with the `Z_5` Fourier attack merely because both use Cayley coordinates.

No later summary may say that this package moves
`LAMBDA-COCYCLE-ANGLES`, RH, or any public scientific status.
