# `C-FUNDED-TWO-USE-EXECUTABLE-N`

**NON-CANONICAL / L1 executable incubation apparatus and audit / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1507](https://github.com/mathorn1973/twist-j/issues/1507), under parent program [#1506](https://github.com/mathorn1973/twist-j/issues/1506) (`DISPATCH_RELEASED`: [#1506#issuecomment-6188571217](https://github.com/mathorn1973/twist-j/issues/1506#issuecomment-6188571217)).

---

## 1. Purpose and scope

This package delivers the self-contained, exact standard-library Python executable funded two-use continuing apparatus (`apparatus.py`) and its complete deterministic audit and CLI runner (`verify.py`), together with the frozen contract (`CONTRACT.md`), preregistration and test inventory (`PREREG.md`), source manifest (`SOURCES.json`), and analytical/coefficient-complete proof (`PROOF.md`).

All primary definitions are embedded directly from the frozen upstream sources (`#1485`, `#1489`, `#1492`, `#1496`, A1 `#1498`, A2 `#1499`, A3 `#1500`, and R1 `#1504` at `c67b9af4f25f9ebb5904e3d654fd9fb3856c8c6f`) without importing any mutable sibling branch at runtime and without using precomputed output lookup tables to drive transitions.

### Explicit dispatch clarifications (`#1506`)

1. **Clarification (i) (`q_3` shift magnitude):** For the cubic separator $q_3(z_0, z_1) = z_0 z_1(2z_0 - 1)$, $q_3(z^{(0)}) = q_3(z^{(1)}) = q_3(z^{(2)}) = q_3(z^{(4)}) = 0$ and $q_3(z^{(3)}) = 1 \cdot \frac{1}{2} \cdot 1 = \frac{1}{2}$. Therefore, adding $q_3(z_A) u$ to $b_2(z_A, z_B)$ changes $b_2$ at $h_A = 3$ by $\frac{1}{2}u$ (`u/2`), not $u$, while adding $\lambda q_3(z_B)$ to $\Delta_B(z_A, z_B)$ changes $\Delta_B$ at $h_B = 3$ by $\frac{\lambda}{2}$.
2. **Clarification (ii) ($\sigma_B$ ready-family readout vs. reversible transition role):** On the common-ready family $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$, second-contact acceptance $\alpha_B \in \{0, 1\}$ is already readable from $(d, b_0, b_2)$ **without** $\sigma_B$: $d = C_1(h_B)$ determines $z_B = \eta(d)$; if $z_B = 0$ ($d = (0,4)$), then $\Delta_B = 0 \in [0, B]$ is always accepted ($\alpha_B = 1$) on $\mathcal{R}_{(c_0, c_1, b_{\mathrm{init}}, B)}$; if $z_B \ne 0$, then $R_0 z_B \ne 0$ and $b_2 - D_2(R_0^{-1} b_0) = \alpha_B R_0 z_B$ uniquely determines $\alpha_B \in \{0, 1\}$. By contrast:
   - First-contact acceptance $\alpha_A$ is **not** readable from $(d, b_0, b_2)$ (or $\Pi_{\mathrm{class}+d} = (X, W, b, d)$) when $b_0 = 0$: at $B = b_{\mathrm{init}} = \frac{1}{5}$, $(h_A, h_B) = (0, 0) \in (\mathrm{ACC}, \mathrm{ACC})$ and $(3, 0) \in (\mathrm{REF}, \mathrm{ACC})$ both have $b_0 = b_2 = 0$ and $d = (0, 4)$, so $\sigma_A$ is strictly required to distinguish accepted zero from refusal at Contact A.
   - For Contact B, $\sigma_B$ is separately required for the **complete reversible transition** $H_{B,B}^2 = \mathrm{id}$ on $\mathcal{Z}_B$ and $\mathcal{A}_B$ (and to prevent the un-reset single-shared-$\sigma$ sign flip on $(0, 1)$), as well as for acceptance readout on the buffer-omitted classical projection $\Pi_{\mathrm{class}} = (X, W, b)$ (where $(0, 0)$ and $(0, 3)$ collide at $B = \frac{1}{5}$).

---

## 2. Frozen pin inventory (before first scientific execution)

The following seven files constitute the immutable preregistration pin before any scientific execution:

- `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/README.md`: this overview and CLI specification.
- `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/CONTRACT.md`: complete mathematical and software contract, API access rules, and `TWOUSE-COMPARE-v1` serialization specification.
- `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/PREREG.md`: six preregistration fields, test inventory (`T01`–`T18` and invalid-endpoint suite `X01`–`X10`), and zero-tolerance failure rules.
- `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/SOURCES.json`: 37-entry frozen source manifest and provenance.
- `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/PROOF.md`: paired-factorization proof ($625^2 = 390{,}625$ inputs) and universal rational-carrier identity proofs.
- `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/apparatus.py`: self-contained exact standard-library Python machine.
- `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py`: complete executable audit and CLI entry point.

---

## 3. CLI entry points

1. **Default scientific audit and witness boundary report (commits stdout to `EXPECTED.txt` after pin):**
   ```text
   python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py
   ```
2. **Separate cross-implementation comparison mode (`TWOUSE-COMPARE-v1`, withheld from Lane V until V's pin and first-run receipt):**
   ```text
   python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py --compare
   ```
3. **Standalone witness boundary dump (human-readable JSON/text inspection):**
   ```text
   python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py --witnesses
   ```

---

## 4. Non-canonical and CI boundary

- This package is **NON-CANONICAL** (`L1`). It modifies only `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/`.
- Ordinary `tools/check_verifier.py` and `tools/check_reproduce.py` inspect `probes/` and `reproduce/` and therefore report `NOT APPLICABLE` on a `notes/`-only pull request; they do not execute `notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py`.
- Public Canon v101 (`canon-v101`), `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]`, and `QDD-INSTRUMENT-APPARATUS` `[O]` remain unchanged.
