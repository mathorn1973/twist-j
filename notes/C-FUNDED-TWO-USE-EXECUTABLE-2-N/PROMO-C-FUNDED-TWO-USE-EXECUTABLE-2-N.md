# PROMO-C-FUNDED-TWO-USE-EXECUTABLE-2-N — Promotion Packet (`DO NOT PROMOTE`)

- **Status:** `NON-CANONICAL`
- **Promotion Verdict:** `DO NOT PROMOTE`
- **Candidate ID:** `C-FUNDED-TWO-USE-EXECUTABLE-2-N`
- **Layer:** `L1`
- **Parent Program:** `#1506` (`P-FUNDED-TWO-USE-APPARATUS`)
- **Corrective Lane Issue:** `#1515` (`[LANE I2] C-FUNDED-TWO-USE-EXECUTABLE-2-N`)
- **Supersedes:** `C-FUNDED-TWO-USE-EXECUTABLE-N` (`#1507`, Draft PR `#1512`)
- **Reconciles Geometry:** `C-TWO-USE-WAVE-GEOMETRY-1-N` (`#1513` / `#1514`, commit `82ad219401d87c3900011d1e8801ffef4221e05b`)
- **Pin Commit SHA:** `06d63ae94f609cc54989e410e3c778ce147d22c5`

---

## 1. Governance & Non-Promotion Rule

Per `POLICY.md`, `AGENTS.md`, `#1506`, and `#1515`:

1. `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/` is an `L1` incubation note (`NON-CANONICAL`). It does not edit `canon/CANON.md`, `canon/CORE.md`, `canon/FRONTIER.md`, `canon/REGISTRY.tsv`, `canon/CHANGELOG.md`, `canon/SHA256SUMS`, or `STATUS.md`.
2. In default verification mode (`python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py`), gates `T01` through `T10` (`10/18`) pass on the reconciled 705-site geometry $D$, and gate `T11` stops at `T11.reject_forbidden[tuple]` (`AssertionError: T11.reject_forbidden[tuple]: expected=True, actual=False`, exit code `1`).
3. Per the two-commit immutability rule in `#1515`, no post-pin tuning or modification of `verify.py` or `apparatus.py` was performed (`0` diff lines across all 9 pinned files relative to `06d63ae94f609cc54989e410e3c778ce147d22c5`).
4. Consequently, the candidate is recorded with status **`DO NOT PROMOTE`**.

---

## 2. Reconciled Geometry & Verified Scope (`T01`–`T10`)

On unmodified pin commit `06d63ae94f609cc54989e410e3c778ce147d22c5`, the following components are verified in full:

- **Reconciled 705-site domain (`T01`):** `DOMAIN.tsv` (`5029` bytes, SHA-256 `2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`) matches `notes/C-TWO-USE-WAVE-GEOMETRY-1-N/DOMAIN.tsv` byte-for-byte ($|D|=705$: `PORT_A=120`, `PORT_B=120`, `JUNCTION=15`, `TAPE=450`, `BOUNDARY=0`) and passes all 12 admissibility checks (`G1`–`G12`).
- **25-pair $60 \times 60$ wave transition & $2{,}033{,}476$-entry energy conservation (`T02`–`T04`):** Exact block-skew-orthogonal rational reflection/transmission across `PORT_A`, `PORT_B`, `JUNCTION`, and `TAPE`, full $1426 \times 1426 = 2{,}033{,}476$ polarized bilinear identity on $\mathcal{B}_{\text{test}}$ (`dim = 1426`), and all 6 exact quadratic capacities ($C_A = 10/3$, $C_B = 10/3$, $C_T = 5/4$, $C_{AB} = C_{AT} = C_{BT} = -5/12$).
- **Two-use $50 \times 50$ step map, non-commutativity, and 4-cut operator certificate (`T05`–`T10`):** Exact $100 \times 100$ symplectic preservation $\Sigma^{\mathsf{T}} \Omega_{100} \Sigma = \Omega_{100}$, chronological two-use trace on $\mathcal{U}_{16}$, order non-commutativity witness $W(1,4) - W(4,1) = 313/233280 \neq 0$, exact 4-cut operator certificate, and `WARM` $c_1 = e_0$ trajectories.

---

## 3. Fired Gate (`T11`) and Working CLI Modes (`--witnesses`, `--compare`)

- **Fired gate (`T11`):** `run_t11_direct_chronological_and_source_readers` tests five inputs against `direct_source_reader` (`CompositeState`, `ApparatusSubstate`, `WaveTapeState`, 6-tuple native checkpoint `st7.x_A`, and 4-tuple `(1, 0, 0, 0)`). The first four are rejected with `TypeError`, whereas `(1, 0, 0, 0)` is accepted as $b_0 = e_0 \in \mathbb{Q}^4$ because `require_q_tuple` calls `require_fraction` (which coerces `int` to `Fraction(val, 1)`).
- **`--witnesses` mode (`exit_code: 0`):** `/opt/homebrew/bin/python3.13 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --witnesses` outputs all 6 full boundary trajectories (`20740` bytes, SHA-256 `b7996fa6cfc525890892efb6cef02c9acb9098c167ecc8888deffe132e72b896`) and:
  ```text
  WITNESS_SUMMARY order_W14=10352117/20995200 order_W41=10323947/20995200 order_diff=313/233280 dirty_c1_e0_B0=(-292699/699840,-20263/466560,-20263/466560,-6871/155520) ready_low_ref_sig=(-1,+1) warm_low_ref_sig=(-1,+1) warm_high_ref_sig=(-1,+1)
  ```
- **`--compare` mode (`exit_code: 0`):** `/opt/homebrew/bin/python3.13 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --compare` outputs (`182` bytes, SHA-256 `77348e12d9948ebafc15c15ea9904b53ece6a30990ea59a59633a1bef8c21c8d`):
  ```text
  TWOUSE-COMPARE-v2 domain_sha256=2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0 records=1200 sha256=670f270e88386e2f1f507e24ec0ae71daf1ff6638ea44783b793479291af3dbc
  ```
