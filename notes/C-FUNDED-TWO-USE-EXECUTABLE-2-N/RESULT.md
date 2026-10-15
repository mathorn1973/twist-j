# Result Report: `C-FUNDED-TWO-USE-EXECUTABLE-2-N`

**NON-CANONICAL / L1 post-pin execution result / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1515](https://github.com/mathorn1973/twist-j/issues/1515), under parent program [#1506](https://github.com/mathorn1973/twist-j/issues/1506).

```text
candidate_id:               C-FUNDED-TWO-USE-EXECUTABLE-2-N
pin_commit_sha:             06d63ae94f609cc54989e410e3c778ce147d22c5
overall_status:             PARTIAL / STOP (10/18 default audit gates PASS; STOP at T11 line 858; --witnesses and --compare PASS)
passed_gates:               T01, T02, T03, T04, T05, T06, T07, T08, T09, T10 (10/18)
fired_gate:                 T11_direct_chronological_and_source_readers (line 858: T11.reject_forbidden[tuple])
unexecuted_in_default_run:  T11 (parts 2-3), T12, T13, T14, T15, T16, T17, T18 (X01-X10)
witnesses_cli_status:       PASS (exit 0, 20740 bytes, sha256 b7996fa6cfc525890892efb6cef02c9acb9098c167ecc8888deffe132e72b896)
compare_cli_status:         PASS (exit 0, TWOUSE-COMPARE-v2 records=1200 sha256=670f270e88386e2f1f507e24ec0ae71daf1ff6638ea44783b793479291af3dbc)
promotion_recommendation:   DO NOT PROMOTE
```

---

## 1. Executive summary and post-pin disposition

Following the G1 geometry reconciliation (`#1513` / `#1514`, `82ad219401d87c3900011d1e8801ffef4221e05b`), Lane I2 (`C-FUNDED-TWO-USE-EXECUTABLE-2-N`) was frozen at commit `06d63ae94f609cc54989e410e3c778ce147d22c5` ([`PINNED_I2`](https://github.com/mathorn1973/twist-j/issues/1515#issuecomment-6191145416)) prior to any scientific execution or import.

On the first post-pin execution under Python `3.13.13` (`LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1`):

1. **Gates `T01` through `T10` (`10/18`) PASSED in full on the reconciled 705-site domain $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$:**
   - `T01_geometry_stencil_and_operators`: **PASS** — Verified $|Y| = 5$, $|B_{\mathrm{st}}| = 60$, $|B_{\mathrm{zero}}| = 61$, $|Y + B_{\mathrm{zero}}| = 142$, $|B_{\mathrm{zero}} + B_{\mathrm{zero}}| = 489$, $|D| = 705$, wave+tape basis dimension $2|D| + 16 = 1426$, exact byte count (`5029`), SHA-256 (`2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`), and ordered point-by-point equality against `DOMAIN.tsv`, full diagonal $\frac{8}{9}$, $P^T P = I_4$, $P^T J_0 = 0$, $K P = \frac{1}{2}P$, $P^T S = G_{\mathrm{source}}$, $\|S e_j\|_D^2 = \frac{4}{5}$, $J_p = \frac{1}{54}(59 I_4 + \mathbf{1}\mathbf{1}^T)$, $M = \frac{1}{1620}(1770 I_4 - v\mathbf{1}^T)$, and $R_0 = -\frac{1}{4}M$.
   - `T02_generators_and_v_non_invertibility`: **PASS** — Verified all $5$ canonical involutions $g_0, \dots, g_4$ and sum actions on all $5^6 = 15{,}625$ states in $\mathbb{F}_5^6$, and verified the explicit $V$ collision at $n = 0$.
   - `T03_single_head_625_census_and_recovery`: **PASS** — Verified all $625$ single-head preparations ($125$ per residue class $h \in \{0..4\}$), canonical selector words, $C_1(h), C_2(h), C_3(h)$, $\eta(C_1(h)) = z^{(h)}$, and exact 3-step generator inversion $g_{j_0} g_{j_1} g_{j_2} x_5 = x_0$.
   - `T04_paired_factorization_390625`: **PASS** — Verified that all $625^2 = 390{,}625$ paired preparations factor into $25$ constant-apparatus fibres of $15{,}625$ pairs each and verified full input recovery `recover_prepared_inputs(Z(7)) == (p_A, p_B)` on distinct fibre representatives.
   - `T05_certificate_f_bijectivity_and_energy`: **PASS** — Verified $H^T = H$ on all $705$ sites, $K^2 - K + \frac{1}{4}PP^T = 0$ on $H e_i$, and across all $1426$ standard basis vectors $E_m$ of $\mathbb{Q}^D \oplus \mathbb{Q}^D \oplus (\mathbb{Q}^4)^4$: `F_inverse(F_step(E_m)) == E_m`, `F_step(F_inverse(E_m)) == E_m`, `full_classical_energy(F_step(E_m)) == full_classical_energy(E_m)`, and $(\mathrm{col}_u(E_m), \mathrm{col}_v(E_m), \mathrm{col}_a(E_m)) = (0, 0, 0)$, certifying all $1426 \times 1426 = 2{,}033{,}476$ entries of the polarized symmetric bilinear energy form $\mathcal{B}_Q(X_1, X_2)$ of $E_{\mathrm{full}}(F(X)) - E_{\mathrm{full}}(X)$, plus the R1-A occupied witness $A_0 = e_0$.
   - `T06_certificate_hb_involutions_and_lbuf`: **PASS** — Verified the polynomial identity $\Delta_\sigma(u, v, r) + \Delta_{-\sigma}(u, v + \sigma a(r), r) = 0$ on all $705$ wave coordinates across all $25$ receiver labels $r \in \mathbb{F}_5^2$ and $\sigma \in \{\pm 1\}$, $H_{B,A}^2 = \mathrm{id}$, $H_{B,B}^2 = \mathrm{id}$, $L_{\mathrm{buf}}^{-1}$, and two-sided invertibility of the supplied-label apparatus substate transitions $T_{c,B}^{(r_A, r_B)}$ and $S_B^{(r_A, r_B)}$ across all $8$ phases $c = 0..7$.
   - `T07_certificate_bilinear_work_and_mu`: **PASS** — Extracted the $4 \times 4$ bilinear cross-work matrix directly from basis wave evolutions on the 705-site domain $D$ and verified exact equality with $-\frac{1}{10497600}\mathbf{1}\mu^T$, $\mu = (145483, 173653, 173653, 142153)^T$.
   - `T08_25_pair_work_table_and_capacities`: **PASS** — Verified all $25$ source pairs across all $6$ capacities $\{0, \frac{1}{10}, \frac{1}{5}, \frac{2}{5}, \frac{8224427}{10497600}, \frac{4}{5}\}$, the 25-row rational work table $41990400 W_{\mathrm{final}}(h_A, h_B)$, sharp maximum $B_* = \frac{8224427}{10497600}$ at $(4, 4)$, and exact four-branch counts (`25/0/0/0`, `25/0/0/0`, `13/12/0/0`, `6/9/6/4`, `3/7/6/9`, `1/4/4/16`).
   - `T09_order_witness_14_vs_41`: **PASS** — Direct 7-step wave/tape evolution at $B = b_{\mathrm{init}} = \frac{4}{5}$ yielded $W_{\mathrm{final}}(1, 4) = \frac{10352117}{20995200}$, $W_{\mathrm{final}}(4, 1) = \frac{10323947}{20995200}$, and $W_{\mathrm{final}}(1, 4) - W_{\mathrm{final}}(4, 1) = \frac{313}{233280}$.
   - `T10_certificate_four_cut_operators_and_archives`: **PASS** — Verified $12960 R_0 z^{(h)}$ and $1399680 R_1 z^{(h)}$, coefficient-complete basis check on $(z_A, z_B, c_0, c_1) \in (\mathbb{Q}^4)^4$ across all $4$ acceptance/refusal branches, and explicit `WARM` old-archive trajectories at $c_1 = e_0$ for $(0, 0)$ ($b_3 = (-\frac{5}{9}, -\frac{1}{108}, -\frac{1}{108}, -\frac{1}{108})^T$) and $(0, 1)$ ($b_3 = (-\frac{292699}{699840}, -\frac{20263}{466560}, -\frac{20263}{466560}, -\frac{6871}{155520})^T$, $E_{\mathrm{full}} = \frac{21}{10}$, $W = \frac{1}{10}$).
2. **Gate `T11` (`run_t11_direct_chronological_and_source_readers`) fired at line 858 (`T11.reject_forbidden[tuple]`):**
   - In part 1 of `T11`, the loop
     ```python
     for forbidden in (st7, st7.to_apparatus_substate(), st7.X, st7.x_A, (1, 0, 0, 0)):
         app.direct_source_reader(forbidden, st7.X.B1)
     ```
     verifies that `direct_source_reader` rejects forbidden state/native-head arguments. The first four arguments (`CompositeState`, `ApparatusSubstate`, `WaveTapeState`, and the 6-tuple native checkpoint `st7.x_A`) raised `TypeError` or `ValueError` as expected.
   - However, the fifth argument `(1, 0, 0, 0)` (intended in `T11` as an unbranded 4-tuple piston input $p_A \in \mathbb{F}_5^4$) is a 4-tuple of Python `int`s. Because `require_q_tuple(b0, 4, "b0")` in `apparatus.py` calls `require_fraction(val)`, which accepts `isinstance(val, int)` and converts `int` to `Fraction(val, 1)`, `direct_source_reader((1, 0, 0, 0), st7.X.B1)` treated `(1, 0, 0, 0)` as the valid rational port 4-vector $b_0 = e_0 = (1, 0, 0, 0)^T \in \mathbb{Q}^4$ rather than raising `TypeError`.
   - Per `#1515` ("After pin, preserve each fired check and stop its declared dependent scope; no tuning or silent repair. Expose actual status, not intended PASS"), the pinned files `apparatus.py` and `verify.py` are preserved byte-identical to `06d63ae94f609cc54989e410e3c778ce147d22c5` (`0` diff lines).
3. **Unexecuted obligations in default `verify.py` mode (`T11` parts 2–3 and `T12`–`T18`):**
   - Because `run_full_audit()` halted at `T11` line 858, parts 2–3 of `T11` and tests `T12` through `T18` (`X01`–`X10`) were not reached in the default `verify.py` CLI invocation.
4. **Complete execution of `--witnesses` and `--compare` CLI modes on the unmodified pin `06d63ae94f609cc54989e410e3c778ce147d22c5`:**
   - Both `/opt/homebrew/bin/python3.13 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --witnesses` and `/opt/homebrew/bin/python3.13 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --compare` do not call `run_t11_direct_chronological_and_source_readers` and completed with exit code `0` and empty stderr on the unmodified pinned code ( note that `format_boundary_line` in `--witnesses` calls `direct_chronological_cut_reader` at every boundary $c = 0..7$ across all 6 witness trajectories).

---

## 2. Witness trajectories (`verify.py --witnesses`) and `TWOUSE-COMPARE-v2` digest (`verify.py --compare`)

### 2.1 Six witness boundary trajectories (`verify.py --witnesses`, `20740` bytes, SHA-256 `b7996fa6cfc525890892efb6cef02c9acb9098c167ecc8888deffe132e72b896`)

| Witness ID | Preparation | Completion boundary ($c = 7, n = 5$) key observables | Rollover ($c = 0, n = 5$) |
|---|---|---|---|
| `WITNESS_1_ORDER_14_BLANK_B_4_5` | $(p_A, p_B) = ((1,0,0,0), (4,0,0,0))$, $B = b_{\mathrm{init}} = \frac{4}{5}$, $c_0 = c_1 = 0$ | $\sigma = (-1,-1)$, $W = \frac{10352117}{20995200}$, $b = \frac{6444043}{20995200}$, $E_{\mathrm{full}} = \frac{10352117}{20995200}$, $\mathrm{nz}(u,v) = (705, 705)$, `uv_sha16=21f2fa1fabd93bbb` | Holds data; $c: 7 \mapsto 0$ |
| `WITNESS_2_ORDER_41_BLANK_B_4_5` | $(p_A, p_B) = ((4,0,0,0), (1,0,0,0))$, $B = b_{\mathrm{init}} = \frac{4}{5}$, $c_0 = c_1 = 0$ | $\sigma = (-1,-1)$, $W = \frac{10323947}{20995200}$, $b = \frac{6472213}{20995200}$, $E_{\mathrm{full}} = \frac{10323947}{20995200}$, $\mathrm{nz}(u,v) = (705, 705)$, `uv_sha16=877707b70ae87d54`; $W(1,4) - W(4,1) = \frac{313}{233280}$ | Holds data; $c: 7 \mapsto 0$ |
| `WITNESS_3_OLD_ARCHIVE_C1_E0_PAIR_01_B_4_5` | $(p_A, p_B) = ((0,0,0,0), (1,0,0,0))$, $B = b_{\mathrm{init}} = \frac{4}{5}$, $c_0 = 0, c_1 = e_0$ | $\sigma = (-1,-1)$, $W = \frac{1}{10}$, $b = \frac{7}{10}$, $E_{\mathrm{full}} = \frac{21}{10}$, $B_0 = b_3 = (-\frac{292699}{699840}, -\frac{20263}{466560}, -\frac{20263}{466560}, -\frac{6871}{155520})$, $B_1 = b_2 = (-\frac{1421}{12960}, \frac{59}{2160}, \frac{59}{2160}, \frac{29}{1080})$ | Holds data; $c: 7 \mapsto 0$ |
| `WITNESS_4_READY_LOWER_REFUSAL_PAIR_33_B_2_5` | $(p_A, p_B) = ((3,0,0,0), (3,0,0,0))$, $B = b_{\mathrm{init}} = \frac{2}{5}$, $c_0 = c_1 = 0$ | $\sigma = (-1,+1)$ (`ACC, REF`), $W = \frac{2}{5}$, $b = 0$, $E_{\mathrm{full}} = \frac{2}{5}$, $\mathrm{nz}(u,v) = (705, 705)$ | Holds data; $c: 7 \mapsto 0$ |
| `WITNESS_5_WARM_LOWER_REFUSAL_A1_E0_PAIR_01_B_4_5` | $(h_A, h_B) = (0, 1)$, $A_1 = e_0$, $B = b_{\mathrm{init}} = \frac{4}{5}$ | At $c=4$: $\Delta_B^{\mathrm{warm}} = \frac{9}{10}$, $b - \Delta_B^{\mathrm{warm}} = -\frac{1}{10} < 0$; at $c=7$: $\sigma = (-1,+1)$, $W = 0$, $b = \frac{4}{5}$, $E_{\mathrm{full}} = 2$, $\mathrm{nz}(u,v) = (61, 489)$ | Holds data; $c: 7 \mapsto 0$ |
| `WITNESS_6_WARM_UPPER_REFUSAL_NEG_WORK_A1_NEG_E0_PAIR_01_B_4_5` | $(h_A, h_B) = (0, 1)$, $A_1 = -e_0$, $B = b_{\mathrm{init}} = \frac{4}{5}$ | At $c=4$: $\Delta_B^{\mathrm{warm}} = -\frac{7}{10} < 0$, $b - \Delta_B^{\mathrm{warm}} = \frac{3}{2} > \frac{4}{5}$; at $c=7$: $\sigma = (-1,+1)$, $W = 0$, $b = \frac{4}{5}$, $E_{\mathrm{full}} = 2$, $\mathrm{nz}(u,v) = (61, 489)$ | Holds data; $c: 7 \mapsto 0$ |

### 2.2 Full-state comparison digest (`TWOUSE-COMPARE-v2`)

```text
TWOUSE-COMPARE-v2 domain_sha256=2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0 records=1200 sha256=670f270e88386e2f1f507e24ec0ae71daf1ff6638ea44783b793479291af3dbc
```
This digest was computed solely from our own pinned `verify.py --compare` prior to inspecting any V2 (`#1516`) outputs or digest.
