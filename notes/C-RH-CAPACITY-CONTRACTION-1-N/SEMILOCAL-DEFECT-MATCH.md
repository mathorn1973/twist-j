# SEMILOCAL DEFECT COEFFICIENT MATCH

```text
STATUS: NON-CANONICAL incubation result
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. Target tested

The previous notes identified the complete local Euler factor of the frozen
delayed-amplitude construction with the same local Blaschke/scattering factor
used in the Connes--Consani Hardy model. The next proposed step was a direct
sectorwise identification of their one-prime off-diagonal decomposition

```text
(1-P) kappa kappa_p P = E_inf + E_p + E_0
```

with the three visible source sectors in the localized Weil functional:

```text
archimedean gamma ladder,
complete-prime delayed tower,
universal pole pair M_+, M_-.
```

This note performs the coefficient test against Theorem 4.4 of
Connes--Consani, `Quasi-inner functions and local factors` (2020).

## 2. E_inf matches the dressed archimedean pole sector exactly

For the pure archimedean ratio, Connes--Consani Theorem 2.3 writes

```text
(1-P) kappa P = sum_(n>=1) A_n |xi_n><eta_n|,

A_n = (-1)^(n+1)
      2*pi^(2n+1/2)
      /[(4n+1) Gamma(n+1) Gamma(n+1/2)].
```

For the finite local ratio

```text
rho_p(s)=(1-p^(s-1))/(1-p^(-s)),
```

one has at every nonzero archimedean pole `s=-2n`

```text
rho_p(-2n)
 = -(1-p^(-(2n+1)))/(p^(2n)-1).
```

Therefore

```text
A_n rho_p(-2n)
 = (-1)^n
   2*pi^(2n+1/2) (1-p^(-(2n+1)))
   /[(4n+1)(p^(2n)-1)Gamma(n+1)Gamma(n+1/2)],
```

which is exactly the coefficient displayed for `E_inf` in Theorem 4.4.

Thus `E_inf` is not merely analogous to the archimedean pole ladder. It is
exactly the pure archimedean off-diagonal pole expansion dressed, pole by pole,
by the value of the prime scattering ratio at the same pole.

**Status:** candidate-T, exact coefficient identity.

## 3. E_p matches the dressed nonzero prime-pole lattice exactly

For the pure finite-place ratio, Connes--Consani Lemma 3.5 gives

```text
(1-P) kappa_p P
 = ((1-p)/p) U_- V I V^* U_+^*.
```

Equivalently it is the sum over the full pole lattice

```text
s_n=2*pi*i*n/log p,  n in Z,
```

of the corresponding rank-one modes. In the product with `rho_inf`, Theorem
4.4 removes `n=0` from this simple-pole sum and inserts the diagonal multiplier

```text
D delta_n = rho_inf(s_n) delta_n,  n!=0,
D delta_0=0.
```

Hence

```text
E_p = ((1-p)/p) U_- V D I V^* U_+^*
```

is exactly the nonzero prime-pole lattice from the pure finite-place operator,
with each pole mode dressed by the value `rho_inf(s_n)` of the archimedean
scattering factor.

This is the Hardy-disk unfolding of the same complete Euler tower whose
cylinder-level factor is `b_(p^-1/2)` in this incubation.

**Status:** candidate-T, exact mode-by-mode identity.

## 4. E_0 does NOT match a pure third sector

At `s=0`, both local ratios have a simple pole:

```text
rho_inf(s) ~ 2/s,

rho_p(s)
 ~ (1-p^-1)/(s log p).
```

Their product therefore has a genuine double pole. Connes--Consani compute its
off-diagonal contribution `E_0` explicitly and show that it has rank two. In
the disk coordinate the common pole is at

```text
x = psi^-1(0) = -1/3,
```

and the negative Fourier coefficients have the form

```text
alpha x^(k-1) + (k-1) beta x^(k-1),
```

with nonzero `beta` and with both `alpha` and `beta` depending explicitly on
`p` and `log p`.

The two universal pole squares in Suzuki's additive Weil functional,

```text
|M_+(v)|^2 + |M_-(v)|^2,
```

are independent of the prime being added. They come from the global polar part
of the completed zeta functional. There is therefore no coefficientwise
identification

```text
E_0 = universal M_+/M_- sector
```

compatible with the frozen additive sector labels.

More conceptually, `E_0` is a **mixed collision jet** produced by multiplying
two local scattering factors which share a pole at `s=0`. It belongs neither
to the pure archimedean factor nor to the pure finite factor.

**Status:** exact F for `DIRECT-THREE-SECTOR-MATCH`.

This falsification does not exclude a larger intertwiner that contains a mixed
finite-dimensional defect channel.

## 5. General finite-place sets produce a growing collision-jet tower

Let `F` contain the archimedean place and `m` finite primes. Each local ratio
has a simple pole at `s=0` with nonzero leading coefficient. Consequently

```text
u_F(s)=rho_inf(s) product_(p in F_fin) rho_p(s)
```

has a pole of exact order `m+1` at `s=0`.

Under the conformal disk coordinate `v=psi^-1(s)`, a principal part of exact
order `r` at one point gives negative Fourier coefficients of the form

```text
P_(r-1)(k) x^(k-1),
```

where `P_(r-1)` has exact degree `r-1`. The associated Hankel/off-diagonal
piece has rank exactly `r`: the sequences

```text
x^k, k x^k, ..., k^(r-1) x^k
```

are linearly independent and span its columns.

Therefore the common-pole collision contributes an exact finite-dimensional
jet sector of rank

```text
m+1.
```

Adding one new finite prime raises this collision-jet rank by one.

**Status:** candidate-T, elementary meromorphic/Hankel lemma.

This is a nested defect architecture, but it is not present as a fixed
prime-independent two-dimensional sector in the additive `R_+,R_-` feature
bookkeeping.

## 6. Why the additive Weil object does not see the growing pole order

The preceding mismatch identifies a category error in the attempted direct
intertwiner. The multiplicative scattering object is

```text
u_F = product_(v in F) rho_v.
```

On the critical boundary it is scalar unitary. Its logarithmic phase derivative
is

```text
Q_F(xi)
 := -i conjugate(u_F) d/dxi u_F
 = d/dxi arg u_F.
```

By the ordinary product rule and `|rho_v|=1`, exactly

```text
Q_F(xi)
 = sum_(v in F)
   [-i conjugate(rho_v) d/dxi rho_v].
```

Thus all multiplicative cross terms, including the growing common-pole order,
disappear at the level of the logarithmic derivative. The local summands are
exactly the finite-place Poisson/Weil symbols and the archimedean digamma/Weil
symbol already proved in `SCATTERING-PHASE.md`.

In scattering terminology this scalar logarithmic derivative is the
one-channel Wigner--Smith phase-delay generator. The terminology is secondary;
the displayed additivity is an elementary exact identity.

**Status:** candidate-T for the exact logarithmic-derivative decomposition;
`Wigner--Smith` is a dictionary label, not a new theorem.

## 7. Ruling on the attempted intertwiner

The proposed map

```text
frozen additive feature sectors
  <-> off-diagonal pole sectors of u_F itself
```

is **F** in its direct sectorwise form. It fails at the first prime because of
`E_0`, and the mismatch grows into an `(m+1)`-jet collision sector for `m`
finite primes.

The surviving construction must operate one infinitesimal level below the
multiplicative scattering matrix:

```text
lossless semilocal scattering u_F
          |
          | logarithmic / phase derivative
          v
additive local delay generator Q_F
          |
          | finite cutoff / prolate compression
          v
localized Weil quadratic form.
```

This is exactly the hierarchy suggested by the signed Pythagorean attack:
unitary scattering one level up, additive quadratic delay one level down.

## 8. New gate: COMPRESSED-DELAY-GENERATOR

A non-circular successor to the failed direct intertwiner must define the
finite-cutoff object from the unconditional lossless scattering system before
using Weil positivity. A viable target has the following shape.

Let `C_a` denote the independently defined support/time-frequency cutoff and
let a conservative dilation/colligation of the compressed scattering channel be
fixed. Construct its self-adjoint infinitesimal phase-delay generator
`Q_(F,a)` and prove an exact quadratic-form identity

```text
<j_a(v), Q_(F,a) j_a(v)>
 = Q_W^a(v) + ||defect_a(v)||^2
```

or the same identity with a completely typed signed defect decomposition.

Required falsifiers:

1. the construction of `Q_(F,a)` uses `Q_W^a` or its positivity as input;
2. the first-prime expansion fails to reproduce the exact local Weil symbol;
3. the archimedean term fails to reproduce the digamma multiplier and known
   prolate correction;
4. the cutoff derivative creates an untyped boundary distribution or a defect
   with the wrong sign;
5. complete-prime updates fail the frozen cutoff coherence law;
6. a claimed positivity follows only after assuming an inner/subspace property
   equivalent to the target inequality.

No RH conclusion is claimed. The value of this gate is that its uncompressed
local generator is already exactly the Weil local sum, while its multiplicative
unitary ancestor is unconditional and lossless.
