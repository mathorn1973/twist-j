# SONIN INTERTWINER AUDIT

```text
STATUS: NON-CANONICAL incubation note
ISSUE:  #357
PUBLIC STATUS CHANGES: none
RH STATUS CHANGE: none
```

## 1. Exact Sonin transfer lemma

Let `H=L2(boundary)` with Hardy projection `P`, `Q=1-P`, and let `u` be a
unimodular boundary multiplier, hence multiplication by `u` is unitary on `H`.
Write its block matrix with respect to `H=PH (+) QH` as

```text
u11 = P u P,      u12 = P u Q,
u21 = Q u P,      u22 = Q u Q.
```

For the Sonin space

```text
S(u) = ker(u22) subset QH,
```

one has for every `xi in S(u)`

```text
u xi = u12 xi in PH,
||u12 xi|| = ||xi||.
```

Thus `u12|S(u)` is an exact isometry. This follows directly from unitarity and
the kernel condition; it does not require RH. Connes--Consani Definition 5.2
uses exactly `S(u)=ker u22`, and their Proposition 5.4 identifies the analogous
partial-isometry structure of triangular unitaries.

**Status:** candidate-T, elementary operator lemma.

## 2. Direct-intertwiner no-go for the corrected signed pair

The frozen signed feature factorization in this incubation is

```text
Q_W^a(v) = ||R_+(v)||^2 - ||R_-(v)||^2.
```

A direct identification of the form

```text
J R_+(v) in S(u),
J_- R_-(v) = u12 J R_+(v),
```

with `J,J_-` isometric would force

```text
||R_-(v)|| = ||R_+(v)||
```

for every admitted `v`, hence `Q_W^a(v)=0` identically. Therefore the exact
Sonin isometry itself cannot be the desired G6 contraction.

Any Sonin mechanism in this candidate class must contain a genuine
compression, quotient, projection, or additional defect channel after the
Sonin isometry.

**Status:** exact F for the direct-isometry candidate class.

## 3. Source-level obstruction already at the archimedean place

Connes--Consani's specific archimedean construction does not identify its
Sonin trace with the archimedean Weil functional without a correction. They
express the difference between the Weil distribution and the Sonin trace in
terms of prolate spheroidal data and later write

```text
Tr(theta(f) S) = W_inf(f) + E(f)
```

with the correction controlled through the prolate pair of cutoff projections.
Their result therefore involves the Sonin trace and an explicit remainder,
not a correction-free equality of the two functionals.

Consequently the candidate that identifies the corrected #357 feature pair
directly with that specific source-normalized Sonin trace, with no prolate
correction, is false already in the one-place archimedean case. This does not
exclude a differently normalized carrier with an independently constructed
defect term.

**Status:** F for `DIRECT-SONIN-EQUALITY`.

## 4. Corrected G6 template

The source-compatible target is now:

```text
R_+ --J_a-->  S(u(F_a)) (+) D_a
                |
                | u12 (+) defect transfer
                v
              output carrier
                |
                | C_a   (orthogonal compression / contraction)
                v
              corrected R_-
```

where

```text
u(F_a) = rho_inf * product_(p in F_a) rho_p,
F_a    = {p : log p < 2a}
```

using the Euler-normalized balanced stabilization tested in this incubation.
The required content is not the diagram itself but exact formulas
for `J_a`, the defect carrier `D_a`, and `C_a`, with

```text
R_- = C_a [u12 (+) defect] J_a R_+,
||C_a|| <= 1
```

proved without RH or Weil positivity.

For an identification with the cited source-normalized Sonin trace, the defect
carrier is not optional: the archimedean trace-remainder theorem shows that a
correction-free equality is already wrong at `F={inf}`.

## 5. Filtration alignment

Connes--Consani prove that for finite place sets `F subset F'`, multiplication
by

```text
D(F,F') = product_(p in F'\F) (1-p^(-s))
```

injects `S(u(F))` into `S(u(F'))`.

The current incubation independently has the cutoff filtration obtained by
completing every admitted prime to its full Euler tower. For an old test vector
`v in D_a`, a newly admitted prime `p` with `log p >= 2a` contributes matched
positive and negative diagonal mass because every shift `k log p` is disjoint
from the old support. Thus the signed Weil difference is unchanged at the
instant the full prime is added.

These are structurally compatible filtrations: both add one complete local
Euler factor at a time. No intertwiner between the two filtrations is claimed
here. Constructing it is the remaining content.

**Status:** candidate-D structural alignment; exact ingredients on each side,
intertwiner open.

## 6. Falsifier for an independently locked comparison

A proposed semilocal comparison fails if any of the following occurs:

1. it identifies `R_-` directly with the exact Sonin isometric image of `R_+`;
2. it omits the known archimedean trace/prolate remainder while claiming exact
   equality with the Weil form;
3. it invokes the contractivity of a Hardy compression of a unimodular
   multiplier as if this alone implied Weil positivity;
4. its cutoff maps are incompatible with the complete-prime filtration;
5. the defect term is defined from the target Weil inequality rather than from
   the independent cutoff/scattering geometry.

## 7. Current boundary

If separately preregistered as an independent comparison/no-go study, the
narrowed non-circular problem would be:

```text
Construct the explicit prolate/semilocal defect channel which completes the
Sonin isometry into the corrected R_+ -> R_- graph map, and prove that the final
output is an orthogonal compression of an unconditional isometry.
```

Success would still require a proof that the constructed map has the corrected
`R_+ -> R_-` typing; only then could contractivity be inherited from Hilbert
geometry rather than RH. Failure at the archimedean place or the first added
prime would close this candidate class without affecting RH itself.

The frozen breaker order permits G6 only after G3-G5 survive. Since G3 is
currently undecided, this audit does not open or execute G6.
