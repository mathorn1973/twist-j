# PROMO-C-FUNDED-TWO-USE-EXECUTABLE-2-N — Promotion Packet (`DO NOT PROMOTE`)

- **Status:** `NON-CANONICAL`
- **Promotion Verdict:** `DO NOT PROMOTE`
- **Candidate ID:** `C-FUNDED-TWO-USE-EXECUTABLE-2-N`
- **Layer:** `L1`
- **Parent Program:** `#1506` (`P-FUNDED-TWO-USE-APPARATUS`)
- **Corrective Lane Issue:** `#1515` (`[LANE I2] C-FUNDED-TWO-USE-EXECUTABLE-2-N`)
- **Supersedes:** `C-FUNDED-TWO-USE-EXECUTABLE-N` (`#1507`, Draft PR `#1512`)
- **Reconciles Geometry:** `P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1` (`probes/P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1/DOMAIN.tsv`, `#1513` / `#1514`, commit `82ad219401d87c3900011d1e8801ffef4221e05b`)
- **Pin Commit SHA:** `06d63ae94f609cc54989e410e3c778ce147d22c5`
- **Scoped Corrective Successor for `T11`–`T18`:** `P-TWO-USE-TYPED-READOUT-CLOSURE-1` (`#1522`, Draft PR `#1523`, commit `d334fd1e7ac3dad65fe290297a78ba97beb74a0a`)

---

## Correction Notice (`2026-10-15`, per `#1515` review disposition)

1. **Withdrawal of unsupported unpinned summary prose:** The initial unpinned derived summary in Section 2 of commit `dac92207c11abb061c10fa4ab729e3789d9cbf85` contained template prose mentioning `PORT_A=120`, `PORT_B=120`, `JUNCTION=15`, `TAPE=450`, `BOUNDARY=0`, `G1`–`G12`, `60x60`/`50x50`/`100x100` matrices, symplectic $\Omega_{100}$ preservation, and $C_A, C_B, C_T, C_{AB}, C_{AT}, C_{BT}$ capacities, and misquoted the G1 identifier/path. Those partitions, matrix sizes, and capacity labels are **not** defined or tested by the pinned engine (`apparatus.py`, `verify.py` at `06d63ae94f609cc54989e410e3c778ce147d22c5`), are **not** accepted evidence, and are withdrawn and replaced below by the exact `T01`–`T10` checks actually implemented and executed by `verify.py`.
2. **Actual G1 geometry reference:** The reconciled 705-site geometry is `P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1` (`probes/P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1/DOMAIN.tsv`, `#1513` / `#1514`, pin `a96646c22267d59179a5a96a161c5f6f95ba6255`, result `82ad219401d87c3900011d1e8801ffef4221e05b`, `5029` bytes, SHA-256 `2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`).
3. **Preservation of pinned science:** All 9 pinned files at `06d63ae94f609cc54989e410e3c778ce147d22c5` (`DOMAIN.tsv`, `README.md`, `CONTRACT.md`, `PREREG.md`, `SOURCES.json`, `PROOF.md`, `MIGRATION.md`, `apparatus.py`, `verify.py`) and the first-run stdout file `EXPECTED.txt` (`1073` bytes, SHA-256 `e3e7063bfdb292d6a8ed6a86c82286c51caf150950eb344d99d6a8565c2eff6a`) remain untouched (`0` diff lines).

---

## 1. Governance & Non-Promotion Rule

Per `POLICY.md`, `AGENTS.md`, `#1506`, and `#1515`:

1. `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/` is an `L1` incubation note (`NON-CANONICAL`). It does not edit `canon/CANON.md`, `canon/CORE.md`, `canon/FRONTIER.md`, `canon/REGISTRY.tsv`, `canon/CHANGELOG.md`, `canon/SHA256SUMS`, or `STATUS.md`.
2. In default verification mode (`python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py`), gates `T01` through `T10` (`10/18`) pass on the reconciled 705-site geometry $D$, and gate `T11` stops at `T11.reject_forbidden[tuple]` (`AssertionError: T11.reject_forbidden[tuple]: expected=True, actual=False`, exit code `1`).
3. Per the two-commit immutability rule in `#1515`, no post-pin tuning or modification of `verify.py` or `apparatus.py` was performed (`0` diff lines across all 9 pinned files relative to `06d63ae94f609cc54989e410e3c778ce147d22c5`).
4. Consequently, the candidate is recorded with status **`DO NOT PROMOTE`**.

---

## 2. Reconciled Geometry & Verified Scope (`T01`–`T10`)

On unmodified pin commit `06d63ae94f609cc54989e410e3c778ce147d22c5`, the default execution of `verify.py` verifies `T01`–`T10` as follows:

- **`T01_geometry_stencil_and_operators` (`PASS`):** Verified $|Y| = 5$, $|B_{\mathrm{st}}| = 60$, $|B_{\mathrm{zero}}| = 61$, $|Y + B_{\mathrm{zero}}| = 142$, $|B_{\mathrm{zero}} + B_{\mathrm{zero}}| = 489$, $|D| = 705$, wave+tape basis dimension $2|D| + 16 = 1426$, exact byte count (`5029`), SHA-256 (`2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`), and ordered point-by-point equality against `DOMAIN.tsv` (matching `probes/P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1/DOMAIN.tsv`), full diagonal $\frac{8}{9}$, $P^T P = I_4$, $P^T J_0 = 0$, $K P = \frac{1}{2}P$, $P^T S = G_{\mathrm{source}}$, $\|S e_j\|_D^2 = \frac{4}{5}$, $J_p = \frac{1}{54}(59 I_4 + \mathbf{1}\mathbf{1}^T)$, $M = \frac{1}{1620}(1770 I_4 - v\mathbf{1}^T)$, and $R_0 = -\frac{1}{4}M$.
- **`T02_generators_and_v_non_invertibility` (`PASS`):** Verified all $5$ canonical involutions $g_0, \dots, g_4$ and sum actions on all $5^6 = 15{,}625$ states in $\mathbb{F}_5^6$, and verified the explicit $V$ collision at $n = 0$.
- **`T03_single_head_625_census_and_recovery` (`PASS`):** Verified all $625$ single-head preparations ($125$ per residue class $h \in \{0..4\}$), canonical selector words, $C_1(h), C_2(h), C_3(h)$, $\eta(C_1(h)) = z^{(h)}$, and exact 3-step generator inversion $g_{j_0} g_{j_1} g_{j_2} x_5 = x_0$.
- **`T04_paired_factorization_390625` (`PASS`):** Verified that all $625^2 = 390{,}625$ paired preparations factor into $25$ constant-apparatus fibres of $15{,}625$ pairs each and verified full input recovery `recover_prepared_inputs(Z(7)) == (p_A, p_B)` on distinct fibre representatives.
- **`T05_certificate_f_bijectivity_and_energy` (`PASS`):** Verified $H^T = H$ on all $705$ sites, $K^2 - K + \frac{1}{4}PP^T = 0$ on $H e_i$, and across all $1426$ standard basis vectors $E_m$ of $\mathbb{Q}^D \oplus \mathbb{Q}^D \oplus (\mathbb{Q}^4)^4$: `F_inverse(F_step(E_m)) == E_m`, `F_step(F_inverse(E_m)) == E_m`, `full_classical_energy(F_step(E_m)) == full_classical_energy(E_m)`, and $(\mathrm{col}_u(E_m), \mathrm{col}_v(E_m), \mathrm{col}_a(E_m)) = (0, 0, 0)$, certifying all $1426 \times 1426 = 2{,}033{,}476$ entries of the polarized symmetric bilinear energy form $\mathcal{B}_Q(X_1, X_2)$ of $E_{\mathrm{full}}(F(X)) - E_{\mathrm{full}}(X)$, plus the R1-A occupied witness $A_0 = e_0$.
- **`T06_certificate_hb_involutions_and_lbuf` (`PASS`):** Verified the polynomial identity $\Delta_\sigma(u, v, r) + \Delta_{-\sigma}(u, v + \sigma a(r), r) = 0$ on all $705$ wave coordinates across all $25$ receiver labels $r \in \mathbb{F}_5^2$ and $\sigma \in \{\pm 1\}$, $H_{B,A}^2 = \mathrm{id}$, $H_{B,B}^2 = \mathrm{id}$, $L_{\mathrm{buf}}^{-1}$, and two-sided invertibility of the supplied-label apparatus substate transitions $T_{c,B}^{(r_A, r_B)}$ and $S_B^{(r_A, r_B)}$ across all $8$ phases $c = 0..7$.
- **`T07_certificate_bilinear_work_and_mu` (`PASS`):** Extracted the $4 \times 4$ bilinear cross-work matrix directly from basis wave evolutions on the 705-site domain $D$ and verified exact equality with $-\frac{1}{10497600}\mathbf{1}\mu^T$, $\mu = (145483, 173653, 173653, 142153)^T$.
- **`T08_25_pair_work_table_and_capacities` (`PASS`):** Verified all $25$ source pairs across all $6$ stock capacities $\{0, \frac{1}{10}, \frac{1}{5}, \frac{2}{5}, \frac{8224427}{10497600}, \frac{4}{5}\}$, the 25-row rational work table $41990400 W_{\mathrm{final}}(h_A, h_B)$, sharp maximum $B_* = \frac{8224427}{10497600}$ at $(4, 4)$, and exact four-branch counts (`25/0/0/0`, `25/0/0/0`, `13/12/0/0`, `6/9/6/4`, `3/7/6/9`, `1/4/4/16`).
- **`T09_order_witness_14_vs_41` (`PASS`):** Direct 7-step wave/tape evolution at $B = b_{\mathrm{init}} = \frac{4}{5}$ yielded $W_{\mathrm{final}}(1, 4) = \frac{10352117}{20995200}$, $W_{\mathrm{final}}(4, 1) = \frac{10323947}{20995200}$, and $W_{\mathrm{final}}(1, 4) - W_{\mathrm{final}}(4, 1) = \frac{313}{233280}$.
- **`T10_certificate_four_cut_operators_and_archives` (`PASS`):** Verified $12960 R_0 z^{(h)}$ and $1399680 R_1 z^{(h)}$, coefficient-complete basis check on $(z_A, z_B, c_0, c_1) \in (\mathbb{Q}^4)^4$ across all $4$ acceptance/refusal branches, and explicit `WARM` old-archive trajectories at $c_1 = e_0$ for $(0, 0)$ ($b_3 = (-\frac{5}{9}, -\frac{1}{108}, -\frac{1}{108}, -\frac{1}{108})^T$) and $(0, 1)$ ($b_3 = (-\frac{292699}{699840}, -\frac{20263}{466560}, -\frac{20263}{466560}, -\frac{6871}{155520})^T$, $E_{\mathrm{full}} = \frac{21}{10}$, $W = \frac{1}{10}$).

---

## 3. Fired Gate (`T11`), Working CLI Modes (`--witnesses`, `--compare`), and Scoped Successor (`#1522`)

- **Fired gate (`T11`):** `run_t11_direct_chronological_and_source_readers` tests five inputs against `direct_source_reader` (`CompositeState`, `ApparatusSubstate`, `WaveTapeState`, 6-tuple native checkpoint `st7.x_A`, and 4-tuple `(1, 0, 0, 0)`). The first four are rejected with `TypeError`, whereas `(1, 0, 0, 0)` is accepted as $b_0 = e_0 \in \mathbb{Q}^4$ because `require_q_tuple` calls `require_fraction` (which coerces `int` to `Fraction(val, 1)`). Because `T11` stopped, `T11` parts 2–3 and `T12`–`T18` (`X01`–`X10`) were not reached in default mode on this pin (`#1522` / PR `#1523` subsequently executes `T11`–`T18` under a fresh pin with typed `DirectPortReadout`).
- **`--witnesses` mode (`exit_code: 0`):** `python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --witnesses` outputs all 6 full boundary trajectories (`20740` bytes, SHA-256 `b7996fa6cfc525890892efb6cef02c9acb9098c167ecc8888deffe132e72b896`) and:
  ```text
  WITNESS_SUMMARY order_W14=10352117/20995200 order_W41=10323947/20995200 order_diff=313/233280 dirty_c1_e0_B0=(-292699/699840,-20263/466560,-20263/466560,-6871/155520) ready_low_ref_sig=(-1,+1) warm_low_ref_sig=(-1,+1) warm_high_ref_sig=(-1,+1)
  ```
- **`--compare` mode (`exit_code: 0`):** `python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --compare` outputs (`182` bytes, SHA-256 `77348e12d9948ebafc15c15ea9904b53ece6a30990ea59a59633a1bef8c21c8d`):
  ```text
  TWOUSE-COMPARE-v2 domain_sha256=2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0 records=1200 sha256=670f270e88386e2f1f507e24ec0ae71daf1ff6638ea44783b793479291af3dbc
  ```
