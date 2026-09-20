# Full measurable Route A obstruction

Status: **candidate-T / L2-to-L5 / NON-CANONICAL / PROSPECTIVE PROOF**.
No formal verifier was run while preparing this proof. A proof, a completed
scientific audit, public acceptance, and a later Canon fold are distinct
steps. This file alone changes no public claim status.

Public basis: Public Canon v90, `main` commit
`c7223ba461e264bde96eaedee4430704580235d3`. The decision owner is
`ENTROPY-LAYER-BRIDGE [O]`, with its full frozen measurable class `A_A`.

Candidate conclusion: the frozen full measurable class `A_A` is empty. In
fact no measurable checkpoint map satisfies the frozen equivariance equation
almost everywhere, even before its uniform-pushforward requirement is imposed.

The main obstruction uses the elementary return-word estimate in Section 5
and the finite quotient source spectrum in Section 6. It does not require a
complete classification of substitution spectra. Unique ergodicity of the
constructed substitution is proved from uniform word frequencies below; the Thue–Morse source carries its already frozen
unique substitution probability. Dekking's exact spectral theorem is a
separately identified cross-check only. This is not the earlier depth-five,
fibrewise-bijective Mackey obstruction.

## 1. Frozen source and native target

Let `K_TM` be the two-sided Thue–Morse subshift for
`mu(0)=01, mu(1)=10`, with shift `S` and its unique invariant probability `m`.
Let `Y=O_(K,lambda)` have normalized additive Haar probability `h`, and let
`V(y)=Jy`. Multiplication by `J` is an invertible measure-preserving map,
acting as a permutation on every finite quotient `O/lambda^k`.

Suppose, for contradiction, a measurable total map

```
P : K_TM x Y -> F_5^6
P(S kappa, Jy) = F_(kappa_0)(P(kappa,y))
```

satisfies the displayed equation almost everywhere. The existing exact
[trace-synchronization theorem](https://github.com/mathorn1973/twist-j/blob/c7223ba461e264bde96eaedee4430704580235d3/probes/P-ENTROPY-LAW-REDUCTION-1/PREREG.md)
from `P-ENTROPY-LAW-REDUCTION-1`, Section 7, Lemmas 1–3, gives

```
z(P(kappa,y)) = 4 + 2 kappa_-1 (mod 5)
```

almost everywhere. The inference uses only equivariance, not `Law_W`, not
uniform state pushforward, and not a finite-depth factorization.

For `a=kappa_-1` and `b=kappa_0`, the native generator chosen on these two
sheets is respectively `e,b,b,d` for pairs `00,01,10,11`. Its sixth coordinate
therefore obeys the exact recursion

```
r(S kappa,Jy) = [a=b] - r(kappa,y)  (mod 5),
```

where `r` denotes the sixth coordinate of `P`.

Replace all relevant conull sets by their intersection under countably many
positive and negative source iterates. The equation and trace formula then
hold at every integer time on one invariant conull set. No pointwise claim is
made on its null complement.

## 2. Induce on the even Thue–Morse tower

The two-sided Thue–Morse system decomposes into two disjoint level-one tower
sets

```
E = mu(K_TM),          S E,
```

with `m(E)=1/2`. Here `mu` denotes the aligned bi-infinite substitution.
The tower is uniquely recognized: occurrences of `00` or `11` can occur only
across boundaries of the pairs `01,10`, so their parity determines the pair
alignment; such occurrences exist with bounded gaps by the elementary
primitive substitution language. Thus no alternating bi-infinite sequence
creates a competing alignment. The map

```
b -> mu(b)
```

conjugates `S` on `K_TM` to the first-return map `S^2` on `E`. Its pushforward
of `m` is the normalized restriction `2m|E`: the latter is `S^2` invariant,
and pulling it back gives an `S` invariant probability, which equals `m` by
unique ergodicity. The independent Haar coordinate remains independent under
this conditioning, and the induced source is exactly

```
(K_TM x Y, m x h, S x V^2).
```

For `kappa=mu(b)`, the coordinates relevant to two native steps are

```
kappa_-1=1-b_-1,       kappa_0=b_0,       kappa_1=1-b_0.
```

Put `d(b)=b_-1 XOR b_0`. The first native step has equality indicator `d(b)`,
the second has indicator zero. Hence

```
r(S^2 mu(b),J^2y) = r(mu(b),y) - d(b).
```

Define `q(b,y)=-r(mu(b),y)`. Then

```
q(Sb,J^2y) = q(b,y) + (b_-1 XOR b_0) (mod 5).
```

Shift the base origin once: set `a=S^-1 b` and
`Q(a,y)=q(Sa,y)`. The equation becomes

```
Q(Sa,J^2y) = Q(a,y) + d(a) (mod 5),
d(a)=a_0 XOR a_1.
```

All equations here hold on a conull set for the indicated induced product
probability. Countable invariant intersection again permits simultaneous
iteration if needed.

## 3. Remove the constant drift using an auxiliary five-cycle

Adjoin an independent uniform coordinate `u in Z/5` with update `u->u+1`.
This is a proof enlargement only: existence of `Q` on the frozen source would
also give `Q` on the enlarged source by ignoring `u`. It asserts no extra
physical or registered source input.

Let

```
Z = Y x Z/5,
T_Z(y,u)=(J^2y,u+1),
eta=h x Uniform(Z/5).
```

Define `B(a,y,u)` as the unique element of `Z/10` with

```
B mod 2 = a_0,
B mod 5 = 3 Q(a,y) - 2u.
```

The Chinese remainder theorem makes this a total measurable definition.
Its update is

```
B(Sa,T_Z(y,u)) = B(a,y,u) + 3d(a)-2 (mod 10).
```

Indeed the difference modulo five is `3d-2`, and its difference modulo two is
`a_1-a_0=d mod 2`, also equal to `3d-2 mod 2`.

## 4. The exact generalized Morse extension

On the alphabet `Z/10`, define the constant-length four substitution

```
sigma(j) = (j,j+1,j-1,j).
```

Let `X_sigma` be its two-sided substitution subshift. This substitution is
primitive: after five substitutions, the possible sums of five increments
from `{-1,0,1}` include every residue modulo ten, so every letter occurs in
`sigma^5(j)` for every `j`. It is aperiodic since its parity factor is the
aperiodic Thue–Morse subshift.

For completeness, unique ergodicity here has an elementary finite-word proof.
Fix a word `w` of length `m`, and let `C_k(j)` count its occurrences fully
inside `sigma^k(j)`. With `M[j,l]` the number of copies of `l` in `sigma(j)`,

```
C_(k+1)=M C_k+E_k,       0<=E_k(j)<=3(m-1).
```

Only occurrences crossing one of three concatenation boundaries contribute
to `E_k`. Normalize `u_k=C_k/4^k` and put `P=M/4`. This primitive stochastic
matrix has `P^5` strictly positive. A strictly positive stochastic power
contracts the oscillation `max_j v_j-min_j v_j` by a factor strictly below
one: subtract the common positive minimum in each column and bound the
remaining row sums. Consequently it has a unique stationary left
probability vector `pi`, and its powers contract on the complement of
constant vectors. The recurrence

```
u_(k+1)=P u_k+e_k,       ||e_k||_infinity<=3(m-1)/4^(k+1)
```

has summable perturbations. The scalar increments
`pi u_(k+1)-pi u_k=pi e_k` are summable. The oscillations tend to zero by
stochastic contraction and the same summable error bound. Therefore
`C_k(j)/4^k` converges to one common limit, uniformly in `j`.

Any long legal word can be placed inside a sufficiently high substituted
word. Decompose that occurrence into complete level-`k` blocks plus at most
two partial boundary blocks. Counts crossing complete block boundaries
contribute at most `m-1` per boundary. For fixed large `k`, the discrepancy
per letter from the common limit is consequently bounded by the
level-`k` discrepancy, `(m-1)/4^k`, and an end error tending to zero as the
word length grows. Taking first the word length and then `k` large proves
uniform frequencies of every finite word on the whole subshift. Compactness
gives an invariant probability by an empirical-measure subsequence; uniform
word frequencies force all invariant probabilities to agree on every
cylinder. The invariant probability `nu_sigma` is therefore unique and
hence ergodic.

Every adjacent pair `(j,k)` occurring in `X_sigma` satisfies

```
k-j = 3((j mod 2) XOR (k mod 2))-2 (mod 10).       (A)
```

Proof: internal differences in `sigma(j)` are `1,-2,1`, with parity changes
`1,0,1`. At a substituted boundary, both the difference and parity change are
those of the original adjacent pair. Induction from the internal pairs in a
first substituted word proves the identity for every substitution word and
hence the subshift.

Parity projects `sigma` onto `mu^2`, so the parity factor

```
pi:X_sigma -> K_TM,       pi(x)_n=x_n mod 2,
```

is onto. Primitivity ensures every translated letter language agrees, and
translation by any even residue commutes with substitution, so global even
translation `x -> x+2j`, `j in Z/5`, preserves `X_sigma` and its base sequence.
Equation (A) determines an entire bi-infinite `x` uniquely from `pi(x)` and
`x_0`. The five even translations furnish all five possible lifts of every
base sequence. Thus the map

```
x -> (pi(x),x_0)
```

is a topological conjugacy of `X_sigma` with the exact five-point extension

```
X_B={(a,b): a in K_TM, b in Z/10, b mod 2=a_0},
T_B(a,b)=(Sa,b+3d(a)-2).
```

No finite-depth assumption, fibrewise bijectivity of the original `P`, or
measurable selection theorem enters this identification.

The unique invariant probability `nu_sigma` just proved is
invariant under each even translation because these translations commute
with shift. Consequently under the displayed conjugacy its base marginal is
`m`, and its conditional probability on the five points of each fibre is
uniform. In particular, for any `f in L^2(m)` and `k=1,2,3,4`,

```
H(a,b)=f(a) exp(2 pi i k b/5)
```

has conditional mean zero given the base. Its norm equals `||f||_2`.

## 5. Elementary return-word obstruction to the relevant eigenvalues

### 5.1. A uniform positive-measure exact return

Put `L=4^k` and `t_k=3L`. Since `sigma(0)=(0,1,9,0)`, the word
`sigma^(k+1)(0)` contains the identical words `sigma^k(0)` in its first and
fourth blocks, at offsets zero and `3L`.

Let `nu=nu_sigma`. Global translation of all letters by any residue in
`Z/10` preserves `X_sigma` and commutes with shift. Indeed substitution
commutes with translation, and primitivity includes words from every initial
letter in the same subshift language. Uniqueness of `nu` makes it invariant
under all these translations, so

```
nu{x:x_0=0}=1/10.
```

For every `n>=1` the probability

```
nu_n = (1/4^n) sum_(i=0)^(4^n-1) (S^i o sigma^n)_* nu
```

is shift invariant: shifting cycles its terms, and the last term returns to
the first because `S^(4^n) sigma^n = sigma^n S` and `S_*nu=nu`. Its support
lies in `X_sigma`. Unique ergodicity therefore gives `nu_n=nu`.

Fix a nonnegative integer window radius `m`. Define the cylinder agreement
set

```
A_(k,m) = {x: x_j=x_(j+t_k) for every -m<=j<=m}.
```

For each `x` with `x_0=0`, the substituted sequence `sigma^(k+1)(x)` has the
repeated blocks just displayed. Every shift offset

```
m <= i <= L-1-m
```

places the whole radius-`m` window inside its first block and the translated
window at distance `t_k` inside the identical fourth block. There are
`L-2m` such offsets when `L>2m`. Applying the measure average at level `k+1`
gives the exact lower bound

```
nu(A_(k,m)) >= (L-2m)/(4L) * (1/10)
             = (4^k-2m)/(40*4^k).                 (B)
```

In particular its limiting lower bound for fixed `m` is `1/40`. This is an
all-`k` statement from exact substituted words, not an extrapolated finite
census.

### 5.2. The necessary return condition for a measurable eigenfunction

Let `F in L^2(nu)` be a nonzero eigenfunction with eigenvalue `omega`:

```
F(Sx)=omega F(x),       |omega|=1.
```

Ergodicity implies that `|F|` is a positive constant almost everywhere;
normalize it to one. Intersect countably many conull sets so the eigenvalue
equation can be iterated at every integer time.

For arbitrary `epsilon>0`, density of cylinder functions gives a function
`G` depending only on coordinates `[-m,m]`, for some fixed `m`, with
`||F-G||_2<epsilon`. On `A_(k,m)` its two reads agree:
`G(S^t_k x)=G(x)`. Thus shift invariance and the triangle-square inequality
give

```
|omega^t_k-1|^2 nu(A_(k,m))
 = integral_(A_(k,m)) |F(S^t_k x)-F(x)|^2 dnu
 <= 2 integral_(A_(k,m)) |F(S^t_k x)-G(S^t_k x)|^2 dnu
    + 2 integral_(A_(k,m)) |G(x)-F(x)|^2 dnu
 <= 4 epsilon^2.
```

By (B), for fixed `epsilon` and its cylinder radius,

```
limsup_(k->infinity) |omega^(3*4^k)-1|^2 <= 160 epsilon^2.
```

Since `epsilon` was arbitrary,

```
omega^(3*4^k) -> 1.                               (C)
```

This necessary condition holds for every measurable eigenfunction, without
assuming it continuous and without invoking a full spectral classification.

### 5.3. Apply the condition only to the source eigenvalue orders

Section 6 proves that every source eigenvalue needed in the coefficient
argument has finite order dividing `2*5^a` for some integer `a>=0`. If such
an `omega` satisfies (C), its powers lie in a finite set and eventually equal
one. Its order therefore divides both `2*5^a` and `3*4^k` for some `k>=1`.
Their gcd divides two, so

```
omega is either 1 or -1.                          (D)
```

Both possible eigenspaces already come from the Thue–Morse base. Constants
supply eigenvalue one. The uniquely recognized two-level tower in Section 2
supplies a phase function taking opposite signs on its two levels; shifting
exchanges those levels, so this function has eigenvalue minus one. Pull both
functions back along `pi:X_sigma->K_TM`.

Ergodicity makes each eigenspace one-dimensional. To see this directly,
nonzero eigenfunctions have constant positive modulus, and the quotient of
two with the same eigenvalue is invariant and hence constant almost
everywhere. Consequently every eigenfunction with an order allowed by the
source is base measurable. A function in any nontrivial five-fibre Fourier
sector has conditional mean zero over that fibre and is therefore orthogonal
to this entire eigenspace. Such an eigenfunction must be zero.

This restricted eigenfunction conclusion is all the main proof needs.

### 5.4. Independent spectral cross-check, not a main-proof dependency

The substitution is prolongable at zero. Its fixed one-sided word satisfies

```
x_n = sum of base-four digit weights of n (mod 10),
weights(0,1,2,3)=(0,1,-1,0).
```

Thus `x_0=x_3=0`. The integer

```
N=(4^10-1)/3=349525
```

has ten base-four digits equal to one, so `x_N=0`, and `N=1 mod 3`.
The return-position gcd and substitution height are therefore exactly one.

F. M. Dekking, *The Spectrum of Dynamical Systems Arising from Substitutions
of Constant Length*, primary preprint in *Publications mathématiques et
informatique de Rennes* (1976), no. 2, exposé no. 6, submitted March 1977,
[primary full text](https://www.numdam.org/item/PSMIR_1976___2_A6_0.pdf),
Section 2, Theorem 13 (printed pages 12–13) identifies the constant-length
odometer times height factor; Section 3, Theorem 7 and its proof (printed
pages 22–23, PDF pages 24–25) places all measurable eigenfunctions in that
factor. The later published article is *Zeitschrift für
Wahrscheinlichkeitstheorie und verwandte Gebiete* **41** (1978), 221–239,
[DOI 10.1007/BF00534241](https://doi.org/10.1007/BF00534241).
The stated page references bind to the accessed preprint edition.

Applied here, that theorem gives exactly the dyadic measurable eigenvalues.
They all already occur in the Thue–Morse factor: iterating the recognizable
substitution partition gives compatible residues `t_n(a) in Z/2^n` with
`t_n(Sa)=t_n(a)+1`, whose exponential characters give all dyadic roots.
Ergodicity again makes each eigenspace one-dimensional. This independently
confirms, and extends, the restricted conclusion (D). The main contradiction
uses only Sections 5.1–5.3 and requires neither this height calculation nor
this imported spectral classification.

## 6. Pure point source and the contradiction

The Koopman operator of `V^2` on `L^2(Y,h)` has pure point spectrum. For each
`k`, functions constant on residue classes modulo `lambda^k` form a finite
invariant subspace on which the operator is a finite permutation. These
nested spaces have dense union because residue cylinders generate the Borel
sigma-algebra of `Y`. Diagonalizing their nested invariant orthogonal
complements supplies a complete orthonormal eigenbasis. The same holds for
`T_Z` after tensoring with the five-cycle eigenbasis.

Their eigenvalue orders are controlled explicitly. For every integer `k>=1`, the local residue field
is `F_5`, and the group of units of `O/lambda^k` has order

```
|(O/lambda^k)^x| = (5-1)5^(k-1)=4*5^(k-1).
```

The element `J` is a unit. Lagrange's theorem implies that its multiplicative
order in this finite unit group divides `4*5^(k-1)`. Squaring gives

```
ord_(lambda^k)(J^2) divides 2*5^(k-1).
```

The corresponding multiplication permutation on the whole additive quotient
has an order dividing that same number. All its Koopman eigenvalues
therefore have orders dividing `2*5^(k-1)`. Tensoring with the five-cycle
replaces that bound by `2*5^max(k-1,1)`. The nested finite-quotient
construction of the orthonormal eigenbasis retains this property for every
basis vector: each eigenvalue has order dividing `2*5^a` for some finite
`a>=0`. No assertion about a continuum of spectral orders is needed.

Choose such a countable orthonormal basis `{e_l}` of `L^2(Z,eta)`, with

```
e_l(T_Z z)=omega_l e_l(z),       |omega_l|=1.
```

Let `zeta=exp(2 pi i/5)` and form the supposed unit-modulus function

```
F(a,z)=zeta^(B(a,z)).
```

It satisfies

```
F(Sa,T_Zz)=zeta^(3d(a)-2) F(a,z).
```

Expand in the pure point coordinate, in `L^2(m x eta)`:

```
F(a,z)=sum_l f_l(a)e_l(z),       f_l in L^2(m).
```

Fubini, Parseval and invariance of the product probability justify taking
coefficients; the equivariance equation yields

```
omega_l f_l(Sa)=zeta^(3d(a)-2) f_l(a)
```

almost everywhere for every `l`.

On the generalized Morse extension define

```
H_l(a,b)=f_l(a) zeta^(-b).
```

Then

```
H_l(T_B(a,b)) = omega_l^(-1) H_l(a,b).
```

It is therefore an eigenfunction, but its conditional mean over the five
fibre points is zero. Sections 5.1–5.3 force `H_l=0`, hence `f_l=0`, for every `l`.
Completeness of the source eigenbasis then gives `F=0` in `L^2`, contradicting
`|F|=1` almost everywhere.

There is no such measurable `Q`, hence no native `r` satisfying the full
frozen equivariance, hence no measurable checkpoint map `P` at all. In
particular the subset satisfying `Law_W` is empty:

```
A_A = empty.
```

## 7. Scope and scientific consequences

- This covers every measurable total map modulo the declared source null
  sets, including arbitrary lambda depth, variable depth, nonbijective fibres,
  maps that do not factor through any finite quotient, and all allowed TM
  context depths.
- It does not rely on the finite 629 component count or a guessed full Mackey
  range. No finite-window calculation is extrapolated.
- It uses no occurrence probability, no new physical source law, no quantum
  measurement postulate and no numerical approximation. The probabilities
  here are precisely the already frozen mathematical source probabilities.
- It supplies a prospective complete negative decision of the specified
  entropy bridge, subject to the frozen proof review and public acceptance
  gates.
  It does not rule out a different source architecture, a correlated source
  law, a changed native target, an altered equivariance equation, or a
  different physical bridge.
- A public pin, exact finite audit of the elementary algebra, independent
  breaker, two-architecture replay, and owner-reviewed fold remain distinct
  from this intermediate argument.
