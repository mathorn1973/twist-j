# P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3 — Source Pin and Provenance

Status: PROSPECTIVE  
Scope: NON-CANONICAL, NEW_DECLARED L1  
Owner: A. M. Thorn (`antigravity-windows-de9b3dcc-e611-4360-a2c9-df8dfe124fd3`)  
Ownership: https://github.com/mathorn1973/twist-j/issues/1655

## 1. Normative canonical baseline (`canon-v103`)

This probe is branched from public `main` / peeled tag `canon-v103`:

- Merge commit (`main` / `canon-v103`): `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`
- Content commit: `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`

Both `verify.py` and `breaker.py` verify the byte lengths and SHA-256 digests of
all five normative canonical authority files before running any scientific check:

| Path | Bytes | SHA-256 |
|---|---:|---|
| `canon/CANON.md` | `1052518` | `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b` |
| `canon/CORE.md` | `30714` | `9d5617a163bc7a4e1964d41861ff7f2f44009117c61debe08a4e1547c88be728` |
| `canon/FRONTIER.md` | `27382` | `8574c3d4b0cc70278dec7d64e2a51022718cc54497c64025d9e6021775fcbaf0` |
| `canon/REGISTRY.tsv` | `532811` | `5cd008147435bf1facfe93b2e05d9d73f647ad09659aac002195890d` |
| `canon/CHANGELOG.md` | `207770` | `79f6bd8f30b1f845ae918b7374049f4bf8e0a2270e89b4c5223469a93855f078` |

## 2. Companion non-canonical probe lineage

This probe is self-contained and does not import code from any earlier probe
directory. It builds mathematically on the following non-canonical L1 probes:

1. `P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (issue #1649, draft PR #1650,
   prospective pin `edfedd7e75c515d6d318032f526f381f66317da3`, result head
   `a17fe5f2198f1693277b45bcf7c55458e8c2c381`):
   - Established the autonomous quadratic-affine action `A_auto[h, chi]` on the
     five-site circulant carrier with `m = 324`, `g = 1/324`,
     `ell = (1,-1,0,0,0)`, `a in {-1,0,1}`, `A = a/4`, and `L = L_int / 324`,
     together with the conserved total bond energy `H_b` and equilibrium offset
     `E_star = (4342005/8683757) A^2`.
2. `P-INTEGER-NONLINEAR-CONSTRAINT-PROPAGATION-1` (issue #1651, draft PR #1652,
   prospective pin `a0841a10e922bf3b3db567f30e66c51c39175fc0`, post-review
   head `98ec11df0cf1b0b4238867879fa07a675a4f7822`):
   - Introduced the oriented edge incidence `B`, positive diagonal edge weights
     `W`, local bond energy density `e_loc,b`, edge current `j_n`, local
     continuity identity `C_n = e_loc,n+1 - e_loc,n + B^T j_n`, and auxiliary
     constraint propagation identity with `tau_b in e^perp` and `p_n in ker B^T`.
3. `P-INTEGER-CUBIC-NOETHER-CLOSURE-1` (issue #1653, draft PR #1654,
   prospective pin `d978a878dd6044d7ba297d8402195a522e6fc8f8`, result head
   `350eb009516f29b6f98c4afb48e3820e6336bc33`):
   - Formulated the global finite-horizon action `S_0 + epsilon S_int` across
     `133` independent coordinates at `T = 5`, proved the exact first-order
     Noether identities `delta_0 S_0 = 0` and `delta_0 S_int + delta_1 S_0 = 0`,
     and isolated the three exact second-order obstructions that motivate the
     present probe:
     - the nonzero second-order variation remainder
       `U = delta_1^(psi) S_int = 115/324`,
     - the pure-gauge field-redefinition remainder
       `S_1(x; Gamma(psi)) - A_auto(x - G_psi x) = -115/648`,
     - the bare order-`epsilon^2` field commutator
       `([delta_1^(psi), delta_1^(eta)] h)_2 = (-1/4, 1/4, 0, 0, 0)`.
4. `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-1` (issue #1655, draft PR #1656,
   prospective pin `4572a78b05994485248db6b480c329b12b335365`, abandonment
   commit `c5e8e956`):
   - Closed as `Status: ABANDONED` per `POLICY.md` Section 3 after its first
     execution exited nonzero (`0` stdout bytes) on `KeyError: 'T'` in
     `sint_grad_x` when applied to a tangent dictionary created by `zeros(t)`
     without metadata key `'T'`.
5. `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-2` (issue #1655, draft PR #1657,
   prospective pin `f0520db827dac1b2ec9242a9c82083fd9151aeb4`, result head
   `049e3969`):
   - Closed as `Status: FAIL` (`FALSIFIER=BREAKER_BYTES`) per `POLICY.md`
     Section 3 after `verify.py` and `breaker.py` passed all scientific checks
     and produced identical SHA-256 digests, but `breaker.py` inserted the
     positive pure-gauge witness label `"pure_gauge_s2_completion"` into the
     10-element negative-control set `controls` at line 866, triggering
     `require(len(controls) == 10, "CERTIFICATE")` at line 936. Retargeted here
     as `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3`.

## 3. Provenance of mathematical objects in this probe

| Mathematical object | Provenance | Role in `P-INTEGER-SECOND-ORDER-NOETHER-CLOSURE-3` |
|---|---|---|
| Five-site carrier `Z/5`, `m = 324`, `L_int` | Canon K1 (`canon/CANON.md`) | Spatial operator `L = L_int / 324` |
| Oriented 10-edge incidence `B`, weights `W` | Inherited from #1652, #1654 (`NEW_DECLARED L1`) | Factorizes `L = B^T W B` and defines edge currents and shifts |
| Autonomous action `A_auto`, `e_loc,b`, `j_n`, `E_star` | Inherited from #1650, #1652, #1654 (`NEW_DECLARED L1`) | Zeroth- and first-order action building blocks |
| Global finite-horizon sectors `S_0`, `S_int`, `Gamma(psi)`, `G_psi` | Inherited from #1654 (`NEW_DECLARED L1`) | First-order Noether system on `31 T - 22` coordinates |
| Prefix-sum multiplier dressing `Psi[M]` and `M_tilde[M] = M - Gamma(Psi[M])` | `NEW_DECLARED L1` in #1655 | Satisfies `delta_0^(psi) Psi_n[M] = psi_n` and `delta_0^(psi) M_tilde[M] = 0` |
| Second-order action `S_2[x, M]` (forms (3.7a) and (3.7b)) | `NEW_DECLARED L1` in #1655 | Quadratic-in-`M`, quadratic-affine-in-`x` extension of the action |
| Second-order field generator `delta_2^(psi) x = G_(Psi[M]) G_psi x` | `NEW_DECLARED L1` in #1655 | Multiplier-dependent two-step field variation |
| Exact second-order Noether identity `delta_0 S_2 + delta_1 S_int + delta_2 S_0 = 0` | `NEW_DECLARED L1` in #1655 | Cancels the `O(epsilon^2)` variation off-shell and leaves `epsilon^3 W_3 + epsilon^4 W_4` |
| Pure-gauge completion `S_<=2(epsilon)|_(M = Gamma(psi)) = A_auto(x - epsilon G_psi x)` | `NEW_DECLARED L1` in #1655 | Exact Taylor completion of the quadratic field-redefinition remainder |
| Order-`epsilon^2` extended commutator cancellation `[hat_delta_psi, hat_delta_eta]_<=2 = 0` | `NEW_DECLARED L1` in #1655 | Cross-commutator `(delta_0 delta_2 - delta_0 delta_2) x` cancels `[delta_1, delta_1] x` |
| Order-`epsilon^3` and `epsilon^4` commutator residuals `C_3`, `C_4` | `NEW_DECLARED L1` in #1655 | Exact higher-order nonclosure of the second-order truncated generators |
| Integer second-order Noether scale `16 m D^3 Q_psi` and tangent denominator `D'' = 80 D^2 Q_psi` | `NEW_DECLARED L1` in #1655 | Exact common-denominator integer lift of the second-order identities |

## 4. External literature context (non-imported)

All definitions, lemmas, and proofs in `PROOF.md` are self-contained algebraic
identities over `Q` and `Z`. The following external works provide conceptual
context for perturbative Noether consistency and discrete gauge structure
without supplying any imported theorem:

- G. Barnich and M. Henneaux, "Consistent couplings between fields with a
  gauge freedom and deformations of the master equation", *Phys. Lett. B* 311
  (1993) 123-129, https://arxiv.org/abs/hep-th/9304057 (Section 4, order-by-order
  consistency of deformed actions and deformed symmetry generators).
- B. Dittrich, "How to construct diffeomorphism symmetry on the lattice",
  *PoS QGQGS2011* (2012) 012, https://arxiv.org/abs/1201.3840.
- B. Dittrich and P. A. Hoehn, "Constraint analysis for variational discrete
  systems", *J. Math. Phys.* 54 (2013) 093505, https://arxiv.org/abs/1303.4294.
