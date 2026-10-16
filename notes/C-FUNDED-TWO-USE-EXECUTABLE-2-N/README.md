# `C-FUNDED-TWO-USE-EXECUTABLE-2-N`

**NON-CANONICAL / L1 executable incubation apparatus and audit on reconciled 705-site domain / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1515](https://github.com/mathorn1973/twist-j/issues/1515), under parent program [#1506](https://github.com/mathorn1973/twist-j/issues/1506) (`SUCCESSORS_G1_RELEASED`: [#1506#issuecomment-6190487767](https://github.com/mathorn1973/twist-j/issues/1506#issuecomment-6190487767); `CORRECTIVE_SUCCESSOR_READY`: [#1507#issuecomment-6190488507](https://github.com/mathorn1973/twist-j/issues/1507#issuecomment-6190488507)).
Predecessor: [#1507](https://github.com/mathorn1973/twist-j/issues/1507) / [#1512](https://github.com/mathorn1973/twist-j/pull/1512) (`C-FUNDED-TWO-USE-EXECUTABLE-N`, pin `81a70caa8dbcc61b64276e7d3df5ba84e860d4f1`, result `d6c48e463e1c7d78e8da828711cdda726f57e00b`, preserved unchanged).

---

## 1. Purpose, G1 geometry reconciliation, and scope

This package delivers the corrective Lane I2 successor (`C-FUNDED-TWO-USE-EXECUTABLE-2-N`): the self-contained, exact standard-library Python executable funded two-use continuing apparatus (`apparatus.py`) and its complete deterministic audit and CLI runner (`verify.py`) on the reconciled 705-site finite lattice domain $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$, together with the frozen domain point list (`DOMAIN.tsv`), mathematical/software contract (`CONTRACT.md`), preregistration and test inventory (`PREREG.md`), 54-entry source manifest (`SOURCES.json`), analytical/coefficient-complete proof (`PROOF.md`), and full predecessor migration audit and static diff (`MIGRATION.md`).

### Additive G1 geometry reconciliation precedence (`#1513` / `#1514`)

Per `82ad219401d87c3900011d1e8801ffef4221e05b:probes/P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1/CORRECTION.md` (`3782` bytes, SHA-256 `84b76140333e5edeae5c6aa8895cd85bafdece05a6d80770b1635fdac6294aab`, scientific pin `a96646c22267d59179a5a96a161c5f6f95ba6255`), the primary `#1485` formula $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$, marked sites $Y$, shell weights $\{2:6, 4:1, 8:15, 10:1, 16:1\}/324$, full diagonal $\frac{8}{9}$, and lexicographic ordering are unchanged, and only the legacy prose numeral `869` is withdrawn as a description of that formula-defined set:

- $|Y| = 5$, $|B_{\mathrm{st}}| = 60$, $|B_{\mathrm{zero}}| = 61$, $|Y + B_{\mathrm{zero}}| = 142$, $|B_{\mathrm{zero}} + B_{\mathrm{zero}}| = 489$, and $|D| = |Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}| = 705$.
- The wave+tape classical basis dimension of $\mathbb{Q}^D \oplus \mathbb{Q}^D \oplus (\mathbb{Q}^4)^4$ is $2|D| + 16 = 1426$ (replacing `1754`).
- At runtime, `apparatus.py` independently constructs $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ from the primary definitions and verifies exact byte count (`5029`), SHA-256 (`2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`), cardinality (`705`), and lexicographically ordered point-by-point equality against `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/DOMAIN.tsv`. All wave/vector/basis dimensions are derived dynamically from `len(validated_domain)`.

### Explicit substate vs. full native invertibility distinction

- **Supplied-label apparatus substate transitions:** For fixed supplied receiver labels $(r_A, r_B) \in (\mathbb{F}_5^2)^2$, the row maps $T_{c,B}^{(r_A, r_B)}$ (`apparatus_row_map`) on $\mathcal{A}_B$ and clocked step $S_B^{(r_A, r_B)}$ (`apparatus_step`) on $\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$ have exact two-sided inverses (`apparatus_row_map_inverse`, `apparatus_step_inverse`) because $L_{\mathrm{buf}}^{(r_B)}$ is a group translation on $\mathbb{F}_5^2$, $H_{B,A}^{(r_A)}$ and $H_{B,B}$ are involutions on $\mathcal{A}_B$, and $F$ is a bijection on $\mathcal{X}_{\mathrm{wave+tape}}$ with explicit two-sided inverse $F^{-1}$.
- **Full coupled native+apparatus evolution $\mathcal{G}_B$:** Because the native step $V$ at $c \in \{0, 2, 3, 5, 6\}$ is not globally invertible on $\mathbb{N}_0 \times (\mathbb{F}_5^6)^2$, the full coupled evolution $\mathcal{G}_B$ on $\mathcal{Z}_B$ is **not** globally invertible on arbitrary native states; on the full state space, only the prepared-image left inverse $D(Z(7)) = (p_A, p_B)$ (`recover_prepared_inputs` / `recognize_ready_image`) on $\mathrm{Im}(\Phi_{(c_0, c_1, b_{\mathrm{init}}, B)})$ is claimed and proved.

### Retained R1 clarifications (`#1506` / `#1515`)

1. **Clarification (i) (`q_3` shift magnitude):** For $q_3(z_0, z_1) = z_0 z_1(2z_0 - 1)$, $q_3(z^{(0)}) = q_3(z^{(1)}) = q_3(z^{(2)}) = q_3(z^{(4)}) = 0$ and $q_3(z^{(3)}) = \frac{1}{2}$. Thus $b_2(z_A, z_B) + q_3(z_A) u$ shifts $b_2$ at $h_A = 3$ by $\frac{1}{2}u$ (`u/2`), not $u$, and $\Delta_B(z_A, z_B) + \lambda q_3(z_B)$ shifts $\Delta_B$ at $h_B = 3$ by $\frac{\lambda}{2}$.
2. **Clarification (ii) ($\sigma_B$ ready-family readout vs. reversible contact transition role):** On the common-ready family $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$, second-contact acceptance $\alpha_B \in \{0, 1\}$ is already readable from $(d, b_0, b_2)$ without $\sigma_B$, whereas $\sigma_A$ is strictly required to separate accepted zero ($h_A = 0$) from refusal ($h_A \in \{3, 4\}$) when $b_0 = 0$, and $\sigma_B$ belongs to the complete reversible contact transition $H_{B,B}^2 = \mathrm{id}$ on $\mathcal{A}_B$ and is required on the buffer-omitted projection $\Pi_{\mathrm{class}} = (X, W, b)$.

### Exposure and independence disclosure

- Owner session `Antigravity-20261015-lane-I2-executable` is the direct descendant of `Antigravity-20261015-lane-I-executable` (`#1507` / `#1512`), reusing only our own predecessor code (`81a70caa8dbcc61b64276e7d3df5ba84e860d4f1`) with a full path/hash mapping and static diff in `MIGRATION.md`.
- During the `#1507` post-pin STOP disposition, we read the public comments on `#1506` and `#1508` and the prose failure records `RUN.md` and `RESULT.md` of `#1511` (`846902867881e535666d88fadfffb6d47323dbb3`, containing V's 3-line negative geometry gate stdout and prose STOP summary).
- Neither V's implementation code (`probes/P-FUNDED-TWO-USE-INDEPENDENT-AUDIT-1/*.py`) nor any V2 (`#1516`) code, outputs, or comparison digest has been opened or read, and none will be opened before both I2 and V2 code pins and first-run records are public.

---

## 2. Frozen pin inventory (before first scientific execution)

The following nine files in `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/` constitute the immutable preregistration pin before any scientific execution or import:

1. `DOMAIN.tsv`: frozen 705-site domain $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ copied byte-for-byte from `82ad219401d87c3900011d1e8801ffef4221e05b:probes/P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1/DOMAIN.tsv` (`5029` bytes, SHA-256 `2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`).
2. `README.md`: this overview, G1 reconciliation summary, exposure disclosure, and CLI specification.
3. `CONTRACT.md`: complete mathematical and software contract on the 705-site carrier, API access rules, and `TWOUSE-COMPARE-v2` serialization specification.
4. `PREREG.md`: six preregistration fields, test inventory (`T01`–`T18` and invalid-endpoint/type suite `X01`–`X10`), and zero-tolerance failure rules.
5. `SOURCES.json`: 54-entry frozen source manifest binding Public Canon v101, upstream notes/probes, G1 (`#1513`/`#1514`), and predecessor Lane I (`#1507`/`#1512`).
6. `PROOF.md`: paired-factorization proof ($625^2 = 390{,}625$ inputs) and universal rational-carrier identity proofs (including the $1426 \times 1426 = 2{,}033{,}476$ polarized bilinear energy certificate).
7. `MIGRATION.md`: exact path/hash mapping from `#1507` (`81a70caa8dbcc61b64276e7d3df5ba84e860d4f1`), itemized list of changes and why each is necessary, and full static unified diff of `apparatus.py` and `verify.py`.
8. `apparatus.py`: self-contained exact standard-library Python machine on the validated 705-site domain.
9. `verify.py`: complete executable audit, witness reporter, and `TWOUSE-COMPARE-v2` CLI runner.

---

## 3. CLI entry points

1. **Default scientific audit and witness boundary report (commits exact stdout to `EXPECTED.txt` after pin):**
   ```text
   python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py
   ```
2. **Separate cross-implementation comparison mode (`TWOUSE-COMPARE-v2`, withheld from Lane V2 until both I2 and V2 pins and first-run records are public):**
   ```text
   python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --compare
   ```
3. **Working command for the 7-step `(1,4)`/`(4,1)` order comparison, dirty-archive `c1=e0` case, and lower/upper stock refusals:**
   ```text
   python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --witnesses
   ```

---

## 4. Non-canonical and CI boundary

- This package is **NON-CANONICAL** (`L1`). It modifies only `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/`.
- Administrative repository checks (`check_policy.py`, `check_canon.py`, `check_ledger.py`, `check_gate_contract.py`, `check_reproduce.py`, `check_verifier.py`) do not execute `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py`; green notes CI is administrative only and is reported separately from scientific execution in `RUN.md`.
- Public Canon v101 (`canon-v101`), `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]`, and `QDD-INSTRUMENT-APPARATUS` `[O]` remain unchanged.
