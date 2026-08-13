# C-GOLDEN-AME-TWOPLACE-1-N — preregistration

Status: **NON-CANONICAL INCUBATION**  
Target line: **PUBLIC**  
Layer: **L1 exact algebra and finite-group structure only**  
Lock: [issue #364](https://github.com/mathorn1973/twist-j/issues/364)  
Created: 2026-08-13  
Canon writes: **forbidden**  
Precomputation under this lock: **none**

## 1. Purpose

Determine whether the published golden AME(4,6) tensor has a non-accidental, exact bridge to both of these already-frozen TWIST-J structures:

1. the two cyclotomic places `Q(zeta_5)` and `Q(zeta_8)`, through their compositum `Q(zeta_40)`; and
2. the six golden projective lines, their `Sym^2 = 1 + 5` split, and the six-point action induced from their ambient three-dimensional geometry.

The default null is that the common golden ratio, the number six, and a compatible coefficient field are coincidences. An arbitrary isomorphism between two six-dimensional vector spaces is not a bridge.

## 2. Frozen authority

| Item | Frozen value |
|---|---|
| Canon | Public Canon v46 |
| Authority | `mathorn1973/twist-j` `main` |
| Tag | `canon-v46` |
| Activation commit | `6545c1d0de61ff4696eb3de1a258139e8891f436` |
| Content commit | `62628ca4da2d938e4e3a122d35c0d93a6debc27f` |
| `canon/CANON.md` SHA-256 | `6c57e714c441bd679b9f6c673352cfae44ac993433d7c4624cd9c3c93df291ff` |
| `canon/CANON.md` bytes | `222760` |

Relevant frozen Canon keys:

- `PLENUM-POINT [T]`: `T_pl/2 = zeta_20^3 = zeta_4^(-1) zeta_5^2` and `s_J^2 = 3 - phi`.
- `DEGREES-BY-PRIME [T]` and `Z2-PLACES-SPLIT [T]`: the fifth and eighth cyclotomic places are separate, including `Q(zeta_5) intersect Q(zeta_8) = Q`.
- `TWO-PLACE-PHYSICS [D]`: only a dictionary-level write/read interpretation; it is not imported as an operator, AME, or uniqueness theorem.
- `GOLDEN-SIX-LINE-SYM2-FRAME [T, L1]`: six frozen lines with equal weights, tight-frame identity, centered regular simplex, and `1 + 5` split.
- `COLOR-CORE-2I [T]`, `COLOR-GOLDEN-TABLE [T]`, and `COLOR-INTEGRAL-LIFT [T]`: the labeled binary icosahedral group `2I = SL_2(F_5)` and its golden model.
- `COLOR-CM-2I-SEMILINEAR-PAIR [T, L4]`: a separate labeled semilinear carrier; it supplies no decoder Gram, amplitude bridge, or L5-L6 measure.

No frozen Canon object identifies the AME local space, the matrix below, quantum Latin squares, or a quantum code with the six-line projector span.

## 3. External source pin

### 3.1 Authoritative machine input

Repository: [`matrix-toolbox/AME_4_6`](https://github.com/matrix-toolbox/AME_4_6)  
Commit: [`1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8`](https://github.com/matrix-toolbox/AME_4_6/commit/1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8)  
License: MIT

| File | Role | Git blob OID | Additional pin |
|---|---|---|---|
| `AME46_ORIGINAL.m` | sole authoritative matrix input | `e0d0e171d58b3360c39595d677ffc401a466112d` | 8515 raw bytes; SHA-256 `55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae` |
| `AME46.py` | textual cross-check only; never executable authority | `01ff4a0036dd76214163db8901b7b6b8fca12ec2` | syntactically incomplete and depends on undefined `np` and `d` |
| `README.md` | provenance | `7d3e389b13d1db1e218e0fce3378083c9ca26fa8` | — |
| `LICENSE` | license | `9fe67ac570332da204ccab6aab9a4a05f42b3f32` | — |

`AME46_ORIGINAL.m` is parsed as tokens into exact algebraic numbers. Running MATLAB/Octave and accepting floating-point output does not satisfy an exact gate. No source permutation, transpose, reshuffling, partial transpose, local unitary, or rephasing is allowed before the source-integrity hash and support checks.

### 3.2 Papers

- S. A. Rather et al., [*Thirty-six entangled officers of Euler: Quantum solution to a classically impossible problem*](https://arxiv.org/abs/2104.05122v2), arXiv:2104.05122v2; Phys. Rev. Lett. 128, 080507 (2022). Construction and AME source.
- W. Bruzda et al., [*Multi-Unitary Complex Hadamard Matrices*](https://arxiv.org/abs/2204.06800v2), arXiv:2204.06800v2. Its Appendix B is a human-readable full-row cross-check under CC BY 4.0.
- S. Ball and R. Simoens, [*Thirty-six quantum officers are entangled*](https://arxiv.org/abs/2603.02334v1), arXiv:2603.02334v1; Phys. Rev. Lett. 137, 050202 (2026). Imported scope only: order-six mutually orthogonal quantum Latin squares cannot both be non-entangled.

The 2026 theorem supplies neither the exact matrix nor a TWIST-J bridge. The Appendix-B representative and the matrix called `U_36` in the original construction are related by a partial transpose; they may not be silently substituted for the pinned MATLAB representative.

## 4. Exact imported object and conventions

All tensor indices are zero-based: `i,j,k,l in {0,...,5}`. Parse the pinned source matrix `U` without modification and define

```text
A[i,j,k,l] = U[6 i + j, 6 k + l].
R(U)[6 i + k, 6 j + l] = A[i,j,k,l].
Gamma_2(U)[6 i + l, 6 k + j] = A[i,j,k,l].
```

The last two equations freeze this incubation's reshuffling and second-factor partial-transpose conventions. If the pinned source cannot be reproduced with these maps, stop and document the convention mismatch; do not repair it post hoc.

Parse the source constants exactly as

```text
phi = (1 + sqrt(5))/2,
w   = exp(2 pi i / 20) = zeta_20,
a   = sqrt(1 - 1/sqrt(5))/2,
b   = sqrt(1 + 1/sqrt(5))/2,
c   = 1/sqrt(2).
```

The upstream imported assertion is

```text
U U* = R(U) R(U)* = Gamma_2(U) Gamma_2(U)* = I_36.
```

Reproducing this 2-unitarity / AME(4,6) assertion is a source check, not a new TWIST-J result.

## 5. Preregistered algebraic predictions

Test, rather than assume from decimal evaluation,

```text
w       = (T_pl/2)^7,
a^2     = (3 - phi)/10 = s_J^2/10,
b^2     = (2 + phi)/10,
b/a     = phi,
c^2     = 1/2.
```

Let `F_U` be the smallest number field generated by all nonzero entries of the pinned matrix, with no prior enlargement. The field prediction is

```text
F_U = Q(zeta_20, sqrt(2))
    = Q(zeta_40)
    = Q(zeta_5, zeta_8).
```

The classical compositum identity may be used, but equality with `F_U` must be certified from actual entries; mere containment is not enough. This gate can establish only an L1 coefficient bridge.

## 6. Frozen six-line object

Work over `K = Q(phi)` with

```text
v1 = (0, 1,  phi)   v2 = (0, 1, -phi)
v3 = (1, phi, 0)    v4 = (1, -phi, 0)
v5 = (phi, 0, 1)    v6 = (phi, 0, -1)
r  = phi + 2
P_i = v_i v_i^T / r.
```

Let `W = span_K{P_1,...,P_6}` inside `Sym^2(K^3)`. Reproduce the frozen tight-frame and `1 + 5` data before using them.

Two symmetry groups must remain distinct:

```text
Gamma_Gram = permutations of {P_i} preserving only their Frobenius Gram matrix.

Gamma_line = { sigma in S_6 : there exists R in SO(3,K)
               with R P_i R^T = P_{sigma(i)} for every i }.
```

The regular-simplex permutation symmetry of the six vectors in `W` is not by itself evidence for a bridge. The preregistered ambient-geometry check is

```text
Gamma_line ~= A_5 ~= 2I/{+I,-I},
```

together with an exact labeled comparison to the quotient of `COLOR-CORE-2I`. This is a test, not permission to choose a convenient isomorphism after seeing the AME stabilizer.

The center of `2I` acts trivially on projective lines. Therefore this six-line carrier can test only `A_5 = 2I/{±I}`. Any claim of a faithful `2I` bridge requires a different spinor carrier and is outside this incubation.

## 7. Frozen AME symmetry class

First compute the strict diagonal permutation stabilizer

```text
G_strict = { sigma in S_6 :
             A[sigma(i),sigma(j),sigma(k),sigma(l)]
             = chi_sigma A[i,j,k,l] for one chi_sigma in mu_40 }.
```

Then, and only then, search the following finite monomial class. For every `g in Gamma_line` and leg `q=1,...,4`, allow

```text
M_q(g) = D_q(g) P_{rho_q(g)},
```

where the diagonal entries of `D_q(g)` lie in `mu_40`, and each permutation representation `rho_q` is conjugate in `S_6` to the frozen six-point action of `Gamma_line`. A leg permutation in `S_4` may also be tested and must be reported explicitly. Require exact homomorphism laws and

```text
(M_1(g) tensor M_2(g) tensor M_3(g) tensor M_4(g))
    (pi_g . A) = chi(g) A
```

for one global character `chi(g) in mu_40`. Enlarging phases beyond `mu_40`, allowing arbitrary local unitaries, or choosing arbitrary `GL_6` matrices changes the question and is prohibited.

## 8. Bridge and equivalence relation

For each leg let `H_q` be the pinned local computational space with basis `e_1,...,e_6`. A primary incidence intertwiner has the form

```text
X_q(e_i) = P_{tau_q(i)}
```

for a bijection `tau_q` that intertwines the candidate AME action with the ambient golden-line action. It transports the tensor to

```text
A_tilde = (X_1 tensor X_2 tensor X_3 tensor X_4) A in W_C^(tensor 4).
```

Also compute the full exact intertwiner spaces and their restrictions to the fixed line plus five-dimensional complement. A construction that needs a freely selected relative scalar or phase between the `1` and `5` components fails the canonicity gate.

Two bridge tuples are equivalent only under:

1. one overall nonzero scalar;
2. exact automorphisms of the frozen golden-line object; and
3. genuine exact stabilizers of the pinned AME tensor within the frozen monomial/gauge class.

No quotient by all of `GL_6`, all local unitaries, or an unregistered selector is allowed. Survival requires exactly one equivalence class of compatible bridge tuples.

## 9. Frozen gates

### G0 — source integrity

- Verify commit, blob, raw-byte count, SHA-256, source support, and exact values.
- Reproduce exact unitarity of `U`, `R(U)`, and `Gamma_2(U)`.
- Cross-check only after the pinned representative passes.

### G1 — two-place field

- Determine `F_U` minimally.
- Prove or refute every identity in section 5.
- Record field degree, defining embedding, and entry witnesses that generate the field.

### G2 — six-line audit

- Reproduce rank six, tight-frame identity, centered rank five, and the `1 + 5` split.
- Compute `Gamma_Gram` and `Gamma_line` separately.
- Test the exact labeled quotient relation with public `2I` without lifting projective lines to a spinor claim.

### G3 — intrinsic AME stabilizers

- Compute support automorphisms, strict permutations, projective monomial stabilizers, and allowed leg permutations.
- Give generators, orders, phase solutions, and machine-checkable exact certificates.
- Guessing `A_5` from the golden ratio is prohibited.

### G4 — common-action breaker

- Search strict simultaneous permutations first.
- Then search the frozen independently conjugated legwise monomial class.
- Require a faithful embedded copy of `Gamma_line` on every leg that fixes `A` projectively and preserves the local `6 = 1 + 5` decomposition.

### G5 — intertwiner and canonicity

- Enumerate incidence intertwiners and full exact intertwiner spaces.
- Quotient only by the relation in section 8.
- Require exactly one surviving equivalence class and no unselected `1/5` relative phase or scale.

### G6 — gauge robustness

- Repeat the classification for exact representatives reached by the allowed local monomial gauge.
- Distinguish an invariant bridge from an accident of the printed representative.

### G7 — output discipline

- Record only exact candidate-T/D/C statements or an exact scoped negative result.
- Ship source pins, scripts, certificates, and `RESULTS.md` on this notes branch.
- Create `PROMO.md` only if every nontrivial gate survives.
- No Canon edit, Registry row, formal probe, evidence, or release action is authorized.

## 10. Hard falsifiers and stop rules

1. **Import stop:** any unexplained mismatch with the pinned source, hash, support, or index convention.
2. **Two-place failure:** `F_U` is not exactly `Q(zeta_5,zeta_8)` under the frozen embeddings.
3. **Line/color failure:** no exact labeled `Gamma_line ~= 2I/{±I}` comparison.
4. **Symmetry killer:** no allowed, faithfully embedded diagonal `Gamma_line` survives in the exact AME monomial stabilizer.
5. **Canonicity killer:** zero bridges, or more than one inequivalent bridge, after the frozen quotient.
6. **Gauge killer:** the claimed bridge depends on a printed gauge for which no intrinsic selector exists.
7. **Selector killer:** the result needs one of the 48 open selectors, a post-hoc basis, an arbitrary `GL_6` transport, phases outside `mu_40`, or a widened search class chosen after seeing failure.
8. **Evidence killer:** floating-point tolerance, plots, visual sparsity, the word "golden", dimension counting, entanglement, or QEC usefulness used as proof.

If G4 fails, the correct result is a negative for this exact preregistered monomial bridge class. It does not prove that no conceivable relation exists.

## 11. Success criterion

`C-GOLDEN-AME-TWOPLACE-1-N` survives incubation only if:

- G0 reproduces the published tensor exactly;
- G1 proves the exact two-place entry field;
- G2 identifies the ambient six-line `A_5` quotient exactly;
- G4 finds the required tensor symmetry within the frozen class;
- G5 leaves exactly one bridge class; and
- G6 shows that class is intrinsic under the allowed gauge.

Passing G0-G2 alone is explicitly insufficient. At most it records a coefficient-level L1 coincidence.

## 12. Scope firewall

This incubation does not claim that TWIST-J explains AME(4,6), quantum Latin squares, the Ball-Simoens necessity theorem, quantum error correction, or fault-tolerant hardware. It authorizes no Born probability, color-physics promotion, decoder, SI bridge, L5-L6 measure, or physical interpretation. `TWO-PLACE-PHYSICS [D]` remains a dictionary, and the public Canon remains unchanged.