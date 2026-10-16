# Semantic Refusal Branches, Honest Failure-Phase Partition, and Adapter Non-Interference

**PUBLIC / NON-CANONICAL / conditional L1 proof / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Probe: `P-TWO-USE-READOUT-FAILURE-REGRESSION-1` (`#1526`), parent `#1506`.

---

## 1. Semantic Rejection Branches on `DirectPortReadout` (`S1`–`S5`) and Positive Controls (`P1`–`P5`)

Let $R_0 = -\frac{1}{4}M$ and $D_2 = R_0 H_{\mathrm{port}}^2 + R_1 H_{\mathrm{port}} + R_2$ be the exact $4 \times 4$ four-cut response operators of `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py`, with explicit inverse
$$R_0^{-1} = -\frac{216}{59}\left(I_4 + \frac{1}{365} v \mathbf{1}^T\right), \qquad v = (349, 354, 354, 348)^T.$$
On the common-ready family at completion boundary $(c = 7, n = 5)$, the two recorded port cuts $(b_0, b_2) = (X.A_0, X.B_1) \in (\mathbb{Q}^4)^2$ satisfy
$$b_0 = \alpha_A R_0 z_A, \qquad b_2 = \alpha_A D_2 z_A + \alpha_B R_0 z_B,$$
where $\alpha_A = (1 - \sigma_A)/2 \in \{0, 1\}$, $\alpha_B = (1 - \sigma_B)/2 \in \{0, 1\}$, and $z_B = \eta(d)$ whenever the delayed label $d \in \mathbb{F}_5^2$ is retained. Defining
$$\widehat{a} = R_0^{-1} b_0, \qquad r = b_2 - D_2 \widehat{a}, \qquad \widehat{b} = R_0^{-1} r,$$
the common-ready equations reduce to $\widehat{a} = \alpha_A z_A$ and $r = \alpha_B R_0 z_B$ ($\widehat{b} = \alpha_B z_B$).

The five-field record `DirectPortReadout(b0, b2, sigma_A=None, sigma_B=None, d=None)` validates carrier membership at construction ($b_0, b_2 \in \mathbb{Q}^4$ via exact `int`/`Fraction`, $\sigma_A, \sigma_B \in \{None, -1, +1\}$, $d \in \{None\} \cup \mathbb{F}_5^2$). Consequently, a record whose individual fields are well-typed passes construction even when its tuple $(b_0, b_2, \sigma_A, \sigma_B, d)$ violates the common-ready consistency equations above. Semantic reading via `direct_source_reader(readout)` delegates to `decode_port_vectors`, which enforces five distinct semantic consistency branches. With $z = (0,0,0,0)$ and $e = (1,0,0,0)$:

1. **`S1_REFUSED_A_NONZERO_B0` — `DirectPortReadout(e, z, sigma_A=1)`:**
   Here $\sigma_A = +1 \implies \alpha_A = 0$, which requires $b_0 = \alpha_A R_0 z_A = 0$. Since $b_0 = e \neq 0$, `decode_port_vectors` raises `ValueError("Inconsistent refused sigma_A=+1 with non-zero b0")`.
2. **`S2_ZERO_B_SOURCE_NONZERO_RESIDUAL` — `DirectPortReadout(z, e, d=(0, 4))`:**
   Here $b_0 = z \implies \widehat{a} = 0$ and $r = b_2 - D_2 \widehat{a} = e \neq 0$, while $d = (0, 4)$ has balanced lift $\eta(0, 4) = (0, 0, 0, 0) = z^{(0)}$. Any branch with $z_B = 0$ forces $r = \alpha_B R_0 z_B = 0$, contradicting $r = e \neq 0$. `decode_port_vectors` raises `ValueError("Inconsistent d=(0,4) with non-zero b2 - D2(alpha_A z_A)")`.
3. **`S3_RESIDUAL_INCOMPATIBLE_WITH_D` — `DirectPortReadout(z, e, d=(1, 4))`:**
   Here $b_0 = z \implies r = e = (1, 0, 0, 0)$, while $d = (1, 4)$ has $z_B = \eta(1, 4) = (\frac{1}{2}, 0, 0, 0) = z^{(1)} \neq 0$ and $R_0 z^{(1)} = (-\frac{1421}{12960}, \frac{59}{2160}, \frac{59}{2160}, \frac{29}{1080}) \neq e$. Because $r \notin \{0, R_0 z^{(1)}\}$, `decode_port_vectors` raises `ValueError("Residual b2 - D2(alpha_A z_A) does not match d on ready family")`.
4. **`S4_SIGMA_B_CONTRADICTS_ZERO_COST_D` — `DirectPortReadout(z, z, sigma_B=1, d=(0, 4))`:**
   On the ready family, $d = (0, 4) \implies z_B = 0 \implies \Delta_B = 0$, so the store bound $0 \le b - \Delta_B \le B$ holds on every admissible store state $b \in [0, B]$ and $\alpha_{B,\text{from } d} = 1$. Supplying $\sigma_B = +1$ asserts $\alpha_B = 0 \neq \alpha_{B,\text{from } d}$, so `decode_port_vectors` raises `ValueError("Mismatch between sigma_B and (d, b0, b2) acceptance readout")`.
5. **`S5_REFUSED_B_NONZERO_RESIDUAL` — `DirectPortReadout(z, e, sigma_B=1)`:**
   Here $b_0 = z, d = None, \sigma_B = +1 \implies \alpha_B = 0$, which requires $r = \alpha_B R_0 z_B = 0$, contradicting $r = e \neq 0$. `decode_port_vectors` raises `ValueError("Inconsistent refused Contact B with non-zero residual b2")`.

### Partial-contract boundary and provenance non-claim (`P1`–`P5`)

- **Accepted zero (`P1`), refused input (`P2`), and unknown zero (`P3`):**
  For $(b_0, b_2) = (z, z)$, $(\sigma_A, \sigma_B, d) = (-1, -1, (0, 4))$ yields $(\alpha_A, \alpha_B, z_A, z_B) = (1, 1, z, z)$; $(\sigma_A, \sigma_B, d) = (+1, +1, (1, 4))$ yields $(0, 0, None, None)$; and omitted context $(\sigma_A, \sigma_B, d) = (None, None, None)$ yields $(None, None, None, None)$.
- **Deliberately partial contract (`P4`):**
  When $(b_0, b_2) = (z, R_0 z^{(1)})$ is supplied with $(\sigma_A, \sigma_B, d) = (None, None, None)$, `direct_source_reader` computes $\alpha_B z_B = R_0^{-1} b_2 = z^{(1)} \neq 0$ in `alpha_B_z_B` while leaving `alpha_B = None` and `z_B = None`. Thus a returned `None` reflects the deliberately partial context rules of `CONTRACT.md` §3 and is **not** a theorem of mathematical indistinguishability.
- **Explicitly tagged integer $\mathbb{Q}^4$ record vs. physical provenance (`P5`):**
  Wrapping integer coordinates `e = (1, 0, 0, 0)` inside `DirectPortReadout(e, z)` succeeds and yields $\alpha_A = 1$, $z_A = R_0^{-1} e = (-\frac{154224}{21535}, -\frac{1296}{365}, -\frac{1296}{365}, -\frac{75168}{21535})$, matching `decode_port_vectors(e, z)`, while raw `direct_source_reader(e)` raises `TypeError`. Because any caller can construct `DirectPortReadout(e, z)` directly, the record type is a software interface boundary and **never** a proof of physical acquisition.

---

## 2. Honest Failure-Phase Partition and Non-Conflation (`H1`–`H6`)

In the frozen `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/verify.py`:
1. `run_full_audit()` assigns `CURRENT_STAGE = fn.__name__` inside the 19-test loop (`lines 1844–1847`), then calls `build_witness_trajectories()` and `print_witness_report(witnesses)` (`lines 1850–1851`) before setting `CURRENT_STAGE = "full_state_comparison"` (`line 1853`). Any failure during witness building therefore inherits `CURRENT_STAGE == "run_t19_typed_record_factorization"`.
2. `main()` (`lines 1869–1871`) catches every `AssertionError` and prints `TYPED_CLOSURE_FAIL remaining_dependent_checks=NOT_RUN comparison=NOT_RUN`, even when `CURRENT_STAGE == "full_state_comparison"` after `compute_comparison_digest()` has already run and failed `COMPARISON.count` (`line 1855`) or `COMPARISON.unchanged_I2_V2_state_stream` (`line 1856`).

Without editing `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/verify.py`, the isolated reporting adapter `run_reporting_adapter(audit_stages, witness_fn, compare_fn)` defines five mutually exclusive phase states:
$$\mathcal{S}_{\mathrm{phase}} = \{\texttt{AUDIT},\; \texttt{WITNESS\_BUILDING},\; \texttt{COMPARISON\_STARTED},\; \texttt{COMPARISON\_FAILED},\; \texttt{COMPLETED}\}$$
with component statuses $(\texttt{audit\_status}, \texttt{witness\_status}, \texttt{comparison\_status}, \texttt{remaining\_dependent\_checks})$ governed by the deterministic transitions:
- During `audit_stages`: `phase_state = AUDIT`, `current_stage = stage_name`. On `AssertionError`: `audit_status = FAIL`, `witness_status = NOT_RUN`, `comparison_status = NOT_RUN`, `remaining_dependent_checks = NOT_RUN`, and execution halts immediately before `witness_fn` and `compare_fn`.
- After all audit stages pass: `audit_status = PASS`, `phase_state = WITNESS_BUILDING`, `current_stage = "witness_boundary_trajectories"`. On `AssertionError` in `witness_fn`: `witness_status = FAIL`, `comparison_status = NOT_RUN`, `remaining_dependent_checks = NOT_RUN`, and execution halts before `compare_fn`.
- After `witness_fn` passes: `witness_status = PASS`, `remaining_dependent_checks = NONE`, `phase_state = COMPARISON_STARTED`, `current_stage = "full_state_comparison"`, `comparison_status = STARTED`. If `compare_fn()` or the count/digest equality checks (`count == 1200`, `domain_sha == EXPECTED_DOMAIN_SHA256`, `digest == EXPECTED_COMPARE_DIGEST`) raise `AssertionError`, the adapter transitions to `phase_state = COMPARISON_FAILED` with `comparison_status = FAIL` (never `NOT_RUN` or `PASS`).
- Only if all three phases succeed does `phase_state` transition to `COMPLETED` with `comparison_status = PASS` and emit `ADAPTER_HARNESS_COMPLETE status=ALL_STAGES_PASS`.

Hence:
1. A witness-building failure is reported under `phase_state = WITNESS_BUILDING` and `first_failed_stage = "witness_boundary_trajectories"`, never under `T19`.
2. A not-started comparison (`H1`, `H2`, `H3`) has `comparison_status = NOT_RUN`, whereas a count or digest mismatch after comparison starts (`H4`, `H5`) has `phase_state = COMPARISON_FAILED` and `comparison_status = FAIL`.
3. The completion marker `ADAPTER_HARNESS_COMPLETE status=ALL_STAGES_PASS` is emitted if and only if `phase_state == COMPLETED` (`H6`).

---

## 3. Non-Interference with Wave/Contact/Native Dynamics and Source Heads

The reporting adapter `run_reporting_adapter` receives only zero-argument callables `(stage_name, stage_fn)`, `witness_fn`, and `compare_fn`, plus expected scalar comparison constants. By construction and static AST verification (`R04`):
1. `run_reporting_adapter` contains zero `import` statements, zero attribute writes (`ast.Store` on `ast.Attribute`) to external objects, and zero references to `CompositeState`, `WaveTapeState`, `ApparatusSubstate`, `u`, `v`, `A0`, `A1`, `B0`, `B1`, `x_A`, `x_B`, `p_A`, `p_B`, `F_step`, `H_B_step`, `native_tick_single`, `prepare_ready_state`, `run_seven_steps`, or `run_eight_steps`.
2. Consequently, `run_reporting_adapter` cannot alter any wave, contact, store, or native state transition and cannot inspect any native head or source variable.
