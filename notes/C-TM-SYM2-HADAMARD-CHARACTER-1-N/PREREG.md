# C-TM-SYM2-HADAMARD-CHARACTER-1-N preregistration

```text
STATUS:        NON-CANONICAL INCUBATION
AUTHORITY:     none
PUBLIC BASIS:  Public Canon v46, mathorn1973/twist-j main
ISSUE LOCK:    #372
TARGET LINE:   PUBLIC
LAYER:         L5 selector/orientation algebra only; no L6 measure lift
OWNER:         current ChatGPT owner session
```

This file is the computation pin. No result observed after this commit may move the objects, gates, or decision vocabulary below.

## 1. Frozen public inputs

Use only the following registered facts at their public scopes:

```text
W = Cent(sigma_line) = C2 wr S3, |W| = 48,
chi_Q : W -> {+1,-1},
chi_F : W -> {+1,-1},
G = ker(chi_Q) intersect ker(chi_F), |G| = 12,
epsilon_read = chi_Q chi_F.
```

`TM-SYM2-PROJECTIVE-FOURFOLD [T]` supplies four free `G`-orbits of selectors, each of size 12, and selector-independent mathematical outputs

```text
nu_s(v_i) = 1/6,
M_s = (1/3) P1 + (2/15) P5.
```

`TM-SYM2-SPECTRAL-COHERENCE` supplies frozen selector diagnostics that do not separate the two `epsilon_read` classes at its public scope.

`TM-SYM2-PHYSICAL-MEASURE [O]` remains open and requires a successor L5 source retaining `epsilon_read`, no selected representative among the 48 selectors, a frozen allowed action and coherence law, a physical Born carrier, a total L5-to-L6 map, normalization, and complete dependencies.

No theorem or output in this incubation may strengthen those rows.

## 2. G1 quotient

Freeze the character map

```text
chi = (chi_Q, chi_F): W -> C2 x C2.
```

Using the stated kernel and orders, prove that `im chi` has order 4 and hence

```text
W/G ~= C2 x C2.
```

The four quotient classes are labeled canonically relative to the frozen characters by

```text
(++), (+-), (-+), (--).
```

A sign/order mismatch or failure of full image fires G1.

## 3. G2 H4 character table

Freeze

```text
H4 = [[1, 1, 1, 1],
      [1, 1,-1,-1],
      [1,-1, 1,-1],
      [1,-1,-1, 1]].
```

Rows, in order, are

```text
1,
chi_Q,
chi_F,
epsilon_read = chi_Q chi_F.
```

Required identity:

```text
H4 H4^T = 4 I4.
```

No row permutation is allowed after execution.

## 4. G3 canonical projectors

For a `G`-invariant scalar selector function, identify it with a class vector

```text
f = (f_++, f_+-, f_-+, f_--)^T.
```

For each frozen character row `v_chi`, define

```text
hat_f_chi = (1/4) v_chi^T f,
P_chi     = (1/4) v_chi v_chi^T.
```

Prove exactly

```text
P_chi^2 = P_chi,
P_chi P_psi = 0 for chi != psi,
sum_chi P_chi = I4.
```

Decide whether `P_epsilon` is representative-free relative to the frozen quotient labels. It is not enough that a formula exists; it must be invariant under permutations inside each 12-selector `G`-orbit.

## 5. G4 current frozen outputs

For any selector-independent output `X`, the quotient class vector is

```text
(X,X,X,X).
```

Compute its H4 coefficients exactly. Apply this componentwise to the registered common mathematical pushforward and common Sym2 operator. No physical interpretation follows.

Also apply the same criterion to every frozen scalar diagnostic from `TM-SYM2-SPECTRAL-COHERENCE` that is stated to be identical across selectors or across the two epsilon classes.

## 6. G5 physical-measure bar

For each missing premise of `TM-SYM2-PHYSICAL-MEASURE [O]`, mark whether H4 alone supplies it:

```text
S  successor L5 source,
R  retained orientation type,
A  allowed action/coherence law,
B  physical Born carrier,
T  total L5-to-L6 map,
N  normalization,
D  complete dependency graph.
```

`R` is already present in the public row; reproducing its character projector is not closure of a missing premise. `ADVANCE` requires H4 to close at least one premise that was actually missing before this incubation, with no new input.

## 7. G6 spectral-coherence control

If a frozen selector diagnostic is constant on all four quotient classes, its three nontrivial H4 coefficients must vanish.

If it is only known to agree on the two `epsilon_read` fibers, its `epsilon_read` coefficient must vanish, but `chi_Q` and `chi_F` may remain. Keep these two statements distinct.

A claimed nonzero epsilon mode in an epsilon-blind diagnostic fires G6.

## 8. G7 independent breaker

Freeze `break.py` before reading `verify.py`. It must attack:

```text
B1  H4 orthogonality and inverse,
B2  projector idempotence, orthogonality, completeness,
B3  quotient-class ordering and epsilon row,
B4  representative independence under all within-class permutations,
B5  vanishing of nontrivial modes for constant outputs,
B6  epsilon-mode vanishing for epsilon-blind outputs,
B7  any illicit L5-to-L6 promotion.
```

The breaker is derived from this file, not from the accepted verifier.

## 9. Decision

```text
ADVANCE
    H4 produces a representative-free object that closes at least one explicit previously-missing premise of TM-SYM2-PHYSICAL-MEASURE [O].

DIAGNOSTIC
    H4 produces a canonical L5 character decomposition/projector and localizes missing orientation information, but closes no previously-missing physical-measure premise.

F
    H4 is only a renaming of already frozen character bookkeeping and supplies no usable new invariant even at L5.

STOP
    authority/collision drift, missing breaker, source ambiguity, or an untyped L5-to-L6 lift.
```

Record only candidate-T, candidate-D, candidate-C, bounded F, or STOP.

## 10. Hard boundary

The registered mathematical image `nu_s(v_i)=1/6` and common operator `M_s` may be transformed but may not be used to choose a physical measure. If their nontrivial H4 modes vanish, the conclusion is only that those frozen outputs do not carry orientation.

No Canon, Registry, frontier, Born, decoder, physical probability, RH, SI, or L6 status movement is authorized.
