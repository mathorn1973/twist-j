# PREREG C-RH-CAPACITY-CONTRACTION-1-N

```text
STATUS:        NON-CANONICAL INCUBATION PREREGISTRATION
AUTHORITY:     none
ISSUE:         #357
TARGET LINE:   PUBLIC
LAYER:         analytic / number-theoretic only
PUBLIC BASIS:  Public Canon v46
RH CLAIM:      none
```

## 0. Purpose

Decide whether the signed delayed-prime factorization of the localized Weil
quadratic form admits an unconditional positive Hilbert `capacity` form, and,
only if it does, whether the negative/symmetric prime channel is the image of
one coherent contractive family. The target is a construction, not a
reformulation of Weil positivity.

## 1. Primary source and fixed conventions

Primary source: Masatoshi Suzuki, *Weil's quadratic form via the screw
function*, arXiv:2606.09096v1, PDF page 1 for the Weil functional and the
localized `Q_W^a` framework. The imported classical statement that complete
Weil positivity is equivalent to RH is not admissible as an input to any
positive gate below.

For `a>0` freeze

```text
D_a       = C_c^infty(-a,a)
E_a v     = zero extension of v to R
L_n       = log n
w_n       = Lambda(n)/sqrt(n)
(U_L f)(x)=f(x+L)
```

with the standard complex `L2(R)` inner product. For `v in D_a`, correlations
with `U_L` vanish for `L>=2a` (strict support gives equality at the boundary as
well), so the prime sum is finite.

The prime part is

```text
q_P,a(v) = -2 sum_(Lambda(n)>0, L_n<2a)
                  w_n Re <U_(L_n) E_a v, E_a v>.
```

Define

```text
(V_a^- v)_n = sqrt(w_n/2) (E_a v - U_(L_n)E_a v)
(V_a^+ v)_n = sqrt(w_n/2) (E_a v + U_(L_n)E_a v)
```

on the finite direct sum over the same `n`.

Define `q_inf,a` by expanding the non-prime terms of Suzuki's displayed Weil
functional after substituting `f=v*tilde(v)`. It may not be inferred from a
zero-side formula. The capacity candidate is

```text
q_A,a(v) = q_inf,a(v) + ||V_a^- v||^2.
```

Algebraically, once G1 is proved,

```text
q_A,a(v) = Q_W^a(v) + ||V_a^+ v||^2,
```

but this identity may not be combined with assumed Weil positivity to prove
G3.

## 2. Gates

### G1 DELAYED-KREIN-FACTOR

Prove exactly

```text
q_P,a(v)=||V_a^-v||^2-||V_a^+v||^2.
```

Also prove the local inertia obstruction: each isolated delayed bilinear block
has both signs, so no invertible basis change makes an individual prime leg
positive.

### G2 PURE-ARCHIMEDEAN-SCHUR-NOGO

Prove the abstract sign statement: for a positive lower block `B>0`, a Hilbert
Schur complement changes the upper block by `-C B^-1 C*`, a negative
semidefinite form. Therefore an indefinite prime term cannot be generated
entirely through such an off-diagonal coupling from a purely archimedean upper
block. A positive Hilbert completion must absorb the positive prime channel in
the capacity block, or use an explicitly indefinite auxiliary geometry.

### G3 CAPACITY-POSITIVITY

First try to break

```text
q_A,a(v) >= 0 for every a>0 and v in D_a.
```

One rigorous negative witness fires the Hilbert-capacity route. Numerical
positivity is diagnostic only. A positive theorem must be derived directly
from the explicit finite/archimedean formula and may not use RH, zero data,
Weil positivity, or any equivalent positivity theorem.

Subgate G3a: derive the complete explicit formula for `q_inf,a` from the
source functional.

Subgate G3b: isolate every positive, negative, rank-one, and translation
component of `q_A,a` and determine whether a standard inequality or explicit
factorization proves positivity.

Subgate G3c: if no proof is found, run a falsification search on frozen finite
families of compact test functions. Any numerical candidate must be converted
to a rigorous inequality before it can fire G3.

### G4 CAPACITY-CLOSURE

Only after G3 positive closure: prove closability, determine nullspace, and
define the Hilbert completion `H_A,a` with canonical dense map
`R_a:D_a->H_A,a`. Type the target finite prime-channel Hilbert space `K_a`.
No silent quotient or regularization.

### G5 CUTOFF-COHERENCE

For `0<a<b`, prove the exact restriction law on `D_a`. In particular decide
whether newly admitted shifts with `2a <= L_n < 2b` have disjoint translated
supports and add equal positive diagonal mass to `||V_b^-v||^2` and
`||V_b^+v||^2`. Record the exact scalar increment and its consequence for any
candidate inductive system.

### G6 NESTED-CONTRACTION

Only after G3-G5, seek a family

```text
T_a:H_A,a -> K_a
V_a^+ = T_a R_a
||T_a|| <= 1
```

compatible with the cutoff maps. A `T_a` obtained by assuming
`Q_W^a>=0`, by invoking Douglas factorization after the target inequality is
known, or by fitting each cutoff separately is circular and fails.

## 3. Breaker order

1. Attack G3 before searching for `T_a`.
2. Independently attack the pure-archimedean Schur claim in G2.
3. Test cutoff coherence before any global limit language.
4. Only a surviving positive G3-G5 permits G6 work.

## 4. Frozen negative conditions

```text
F-CAP-1  exists rigorous a,v with q_A,a(v)<0
F-CAP-2  claimed pure-archimedean positive Schur block produces an
         indefinite prime contribution despite the Schur sign law
F-CAP-3  any proof uses RH/zeros/Weil positivity or a positivity-equivalent input
F-CAP-4  cutoff family has no coherent typed maps preserving the frozen forms
F-CAP-5  only unrelated per-cutoff contractions exist
```

## 5. Allowed statuses

Only `candidate-T`, `candidate-D`, `candidate-C`, `F`, or `STOP` may be
recorded. No public status changes occur in this incubation.

## 6. Scope firewall

No RH or GRH proof/evidence, no J-native carrier, no Born/decoder statement,
no privileged `zeta_8`, no physics, no SI bridge, and no L1-L6 lift. Any later
promotion requires a fresh public claim lock and current public protocol.
