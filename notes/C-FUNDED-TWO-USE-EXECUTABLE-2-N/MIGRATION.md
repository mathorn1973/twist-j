# Migration Note and Static Code Diff: `C-FUNDED-TWO-USE-EXECUTABLE-2-N`

**NON-CANONICAL / L1 predecessor migration audit and full static diff / 2026-10-15.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1515](https://github.com/mathorn1973/twist-j/issues/1515), under parent program [#1506](https://github.com/mathorn1973/twist-j/issues/1506).
Predecessor: [#1507](https://github.com/mathorn1973/twist-j/issues/1507) / [#1512](https://github.com/mathorn1973/twist-j/pull/1512) (`C-FUNDED-TWO-USE-EXECUTABLE-N`, pin `81a70caa8dbcc61b64276e7d3df5ba84e860d4f1`, result `d6c48e463e1c7d78e8da828711cdda726f57e00b`, preserved unchanged).
Geometry reconciliation: [#1513](https://github.com/mathorn1973/twist-j/issues/1513) / [#1514](https://github.com/mathorn1973/twist-j/pull/1514) (`P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1`, pin `a96646c22267d59179a5a96a161c5f6f95ba6255`, result `82ad219401d87c3900011d1e8801ffef4221e05b`).

---

## 1. Path and hash mapping from `#1507` and G1 (`#1513`/`#1514`)

Only our own predecessor code (`81a70caa8dbcc61b64276e7d3df5ba84e860d4f1:notes/C-FUNDED-TWO-USE-EXECUTABLE-N/`) and the frozen G1 `DOMAIN.tsv` (`82ad219401d87c3900011d1e8801ffef4221e05b:probes/P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1/DOMAIN.tsv`) are reused. Predecessor `RUN.md`, `EXPECTED.txt`, and `RESULT.md` from `d6c48e463e1c7d78e8da828711cdda726f57e00b` are recorded in `SOURCES.json` as historical evidence of the `#1507` `PARTIAL / STOP` disposition and are **not** copied as new evidence; new `EXPECTED.txt`, `RUN.md`, and `RESULT.md` are generated only after `PINNED_I2`.

| Predecessor / G1 source (`commit:path`) | Predecessor bytes / SHA-256 | Successor path (`notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/`) | Successor bytes / SHA-256 | Disposition |
|---|---|---|---|---|
| `82ad219401:probes/P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1/DOMAIN.tsv` | `5029` / `2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0` | `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/DOMAIN.tsv` | `5029` / `2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0` | Copied byte-identical from G1 (#1513/#1514) |
| `81a70caa8d:notes/C-FUNDED-TWO-USE-EXECUTABLE-N/apparatus.py` | `51473` / `a3bba3433c81c2e1b445008596d898915031dc67ca73f18195be6f5196422833` | `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/apparatus.py` | `58364` / `85c18b1b130d6e7d8cf954ffc8e6ad5960f27e5b371ac381e967979bb518dc6d` | Updated to reconciled 705-site D, dynamic n_sites, expected/actual errors, TWOUSE-COMPARE-v2 |
| `81a70caa8d:notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py` | `58399` / `15dd15ea81ded0f7bda498b9797ee263d2204efe38f763f5b3e7e924cdf76126` | `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py` | `70920` / `d093df3dba5d2f82b8a4493ff3a1f3828e3bd9b9b512a3c34e7aa240671c45f8` | Updated T01/T05/T06/T07/T10/T18 for |D|=705, dim=1426, 1426x1426 bilinear energy certificate, TWOUSE-COMPARE-v2 |
| `81a70caa8d:notes/C-FUNDED-TWO-USE-EXECUTABLE-N/README.md` | `5367` / `6f6b16256dc5dae23145430fb7b3848769e403fa8db411d5f269371522d5b50d` | `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/README.md` | `9353` / `8695306ac7357b30c5851059f73bfe5a7412b3fbc46e3fad1966f7ccf0ed31b4` | Updated for Lane I2 (#1515), G1 precedence, exposure disclosure, and CLI modes |
| `81a70caa8d:notes/C-FUNDED-TWO-USE-EXECUTABLE-N/CONTRACT.md` | `14616` / `7c85250f5c6b88c9685879742387a4c13601df6e7ea5d67cf821f89e58cac12a` | `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/CONTRACT.md` | `17073` / `c285b6afaaf770c01c5b133b3db64cfd00816b453b747c3fb314e12e3a881952` | Updated for |D|=705, dim=1426, supplied-label substate inverse scope, and TWOUSE-COMPARE-v2 |
| `81a70caa8d:notes/C-FUNDED-TWO-USE-EXECUTABLE-N/PREREG.md` | `18130` / `71a49ad70d772b23869f070eeaa9326d56043cf577d28f662cc1ad773a5367a5` | `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/PREREG.md` | `20437` / `d3afb6786ba4a4884421a61a3fa0b7edf8b95ac13dea3712a3709ecc4bc98381` | Updated six preregistration fields and T01-T18 / X01-X10 inventory under G1 |
| `81a70caa8d:notes/C-FUNDED-TWO-USE-EXECUTABLE-N/SOURCES.json` | `23681` / `d4642da73f7165eaf5817c9cb9db2a33b168a829581b729a44bae1fa568c5a2d` | `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/SOURCES.json` | `34845` / `48d0537f1f8f6e0c96754c6225faa9a95524890248d39742f4aa944502a68202` | Extended from 37 to 54 sources binding G1 (#1513/#1514) and predecessor I (#1507/#1512) |
| `81a70caa8d:notes/C-FUNDED-TWO-USE-EXECUTABLE-N/PROOF.md` | `11919` / `fa218d6e85c989bdabadbcf075dbebf09371efb4df7f40a1f19037fe1bcaeb2d` | `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/PROOF.md` | `14564` / `57855afb3d5fe90cab0e93e1de97d7e4ec9f15b0224837d37d9c83ceed1f063d` | Updated for |D|=705, dim=1426, and complete 1426x1426=2033476 polarized bilinear energy proof |

---

## 2. Itemized list of changes and why each is necessary

1. **Addition of `DOMAIN.tsv` and independent runtime geometry reconciliation (`apparatus.py`, `verify.py` `T01`):**
   - *Why necessary:* Predecessor `#1507` stopped at the first gate (`T01_geometry_stencil_and_operators`) with `RuntimeError: Expected |D| = 869, got 705` because the primary Minkowski sum $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ has cardinality $|D| = 705 \ne 869$. Under the additive G1 correction (`82ad219401d87c3900011d1e8801ffef4221e05b:probes/P-D3-TWO-CUT-GEOMETRY-RECONCILIATION-1/CORRECTION.md`), the legacy numeral `869` is withdrawn while the primary formula $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$, shell weights, diagonal $8/9$, and lexicographic order are unchanged.
   - *Change:* `DOMAIN.tsv` (`5029` bytes, SHA-256 `2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0`) is copied into `notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/DOMAIN.tsv`. At runtime, `get_geometry()` in `apparatus.py` independently constructs $B_{\mathrm{st}}$ (`60`), $B_{\mathrm{zero}}$ (`61`), $Y + B_{\mathrm{zero}}$ (`142`), $B_{\mathrm{zero}} + B_{\mathrm{zero}}$ (`489`), and $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$ (`705`), and verifies exact byte length, SHA-256, cardinality, and ordered point-by-point equality against `DOMAIN.tsv`.
2. **Replacement of hardcoded `869` / `1754` with dynamic `geom.n_sites` (`705`) and `geom.wave_tape_basis_dim` (`1426`) (`apparatus.py`, `verify.py`):**
   - *Why necessary:* All wave vector lengths ($|D| = 705$) and wave+tape classical basis dimensions ($2|D| + 16 = 1426$) must be derived from `len(validated_domain)` rather than stale literal loop bounds.
   - *Change:* Every occurrence of literal `869` and `1754` in `apparatus.py` and `verify.py` (`T01`, `T05`, `T06`, `T07`, `T10`) is replaced with `geom.n_sites` (`705`) and `geom.wave_tape_basis_dim` (`1426`), and `X10` explicitly tests that a legacy `869`-entry wave vector is rejected with `expected=705, actual=869`.
3. **Complete $1426 \times 1426 = 2{,}033{,}476$ polarized symmetric bilinear energy certificate in `T05` (`verify.py`, `PROOF.md`):**
   - *Why necessary:* Universal classical energy conservation $E_{\mathrm{full}}(F(X)) = E_{\mathrm{full}}(X)$ on $\mathbb{Q}^D \oplus \mathbb{Q}^D \oplus (\mathbb{Q}^4)^4 \cong \mathbb{Q}^{1426}$ requires certifying not only the $1426$ diagonal basis values $E_{\mathrm{full}}(F(E_m)) = E_{\mathrm{full}}(E_m)$ and the $(v,v)$ block $K^2 - K + \frac{1}{4}PP^T = 0$, but all $1426 \times 1426 = 2{,}033{,}476$ entries of the polarized symmetric bilinear form $\mathcal{B}_Q(X_1, X_2)$ of $Q(X) = 2(E_{\mathrm{full}}(F(X)) - E_{\mathrm{full}}(X))$ using a finite sparse method.
   - *Change:* `_verify_f_basis_and_bilinear_column` in `verify.py` (`T05`) verifies $q_2 = K(w_2 - \frac{1}{2}H v_2 - 2 P b_{\mathrm{out},2}) = \frac{1}{2}(w_2 - u_2)$ and $\mathrm{col}_u(E_m) = 0 \in \mathbb{Q}^D$, $\mathrm{col}_v(E_m) = 0 \in \mathbb{Q}^D$, $\mathrm{col}_a(E_m) = 0 \in \mathbb{Q}^4$ across all $1426$ standard basis vectors $E_m$.
4. **Explicit naming and scope of the supplied-label apparatus substate inverse vs. full coupled evolution (`apparatus.py`, `verify.py` `T06`, `CONTRACT.md`, `PROOF.md`):**
   - *Why necessary:* `#1515` requires distinguishing the invertible rational apparatus substate transitions with supplied receiver labels $(r_A, r_B)$ from the full coupled evolution $\mathcal{G}_B$ on $\mathcal{Z}_B$ (where native selector $V$ is non-invertible), ensuring `T06` wording does not enlarge the inherited prepared-image result.
   - *Change:* Docstrings in `apparatus.py` and `T06` in `verify.py` explicitly test two-sided invertibility of `apparatus_row_map` / `apparatus_row_map_inverse` ($T_{c,B}^{(r_A, r_B)}$) and `apparatus_step` / `apparatus_step_inverse` ($S_B^{(r_A, r_B)}$) on $\mathcal{A}_B \times (\mathbb{Z}/8\mathbb{Z})$ and name them as supplied-label substate transitions.
5. **Explicit `expected` and `actual` values in all validator exceptions and audit assertions (`apparatus.py`, `verify.py`):**
   - *Why necessary:* `#1515` requires freezing error messages that report actual and expected values, especially dimensions, rather than an ambiguous error or bare `assert`.
   - *Change:* All validator exceptions in `apparatus.py` and all `require_eq` / `require_true` checks in `verify.py` format `expected=...` and `actual=...`, and `T18` (`X10`) verifies that malformed calls raise exceptions containing both `expected` and `actual`.
6. **Upgrade of comparison mode to `TWOUSE-COMPARE-v2` (`apparatus.py`, `verify.py`):**
   - *Why necessary:* `TWOUSE-COMPARE-v1` remained `NOT_RUN` on the inconsistent 869-site carrier. `#1515` specifies `TWOUSE-COMPARE-v2` initialized with `TWOUSE-COMPARE-v2\nDOMAIN_SHA256 2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0\n` and outputting `TWOUSE-COMPARE-v2 domain_sha256=2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0 records=1200 sha256=<64 lowercase hex>`.
   - *Change:* `compute_comparison_digest()` in `apparatus.py` and `--compare` in `verify.py` implement `TWOUSE-COMPARE-v2`.

---

## 3. Full static unified diff of `apparatus.py`

```diff
--- a/notes/C-FUNDED-TWO-USE-EXECUTABLE-N/apparatus.py
+++ b/notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/apparatus.py
@@ -1,7 +1,7 @@
 #!/usr/bin/env python3
-"""Self-contained exact funded two-use continuing apparatus (Lane I, #1507).
-
-NON-CANONICAL / L1 executable incubation machine.
+"""Self-contained exact funded two-use continuing apparatus (Lane I2, #1515).
+
+NON-CANONICAL / L1 executable incubation machine on reconciled 705-site D.
 Original work Apache-2.0, A. M. Thorn, 2026-10-15.
 """
 
@@ -12,11 +12,12 @@
 from functools import lru_cache
 import hashlib
 import json
+from pathlib import Path
 from typing import Dict, List, Optional, Sequence, Tuple, Union
 
 
 # ---------------------------------------------------------------------------
-# Primary embedded constants (from frozen #1485 and Public Canon v101)
+# Primary embedded constants (from frozen #1485, G1 #1513/#1514, and Canon v101)
 # ---------------------------------------------------------------------------
 
 Y_SITES: Tuple[Tuple[int, int, int], ...] = (
@@ -35,6 +36,13 @@
 DIAG_H: Fraction = Fraction(10, 9)
 BALANCED_LIFT_ELL: Tuple[int, int, int, int, int] = (0, 1, 2, -2, -1)
 
+EXPECTED_DOMAIN_SITES: int = 705
+EXPECTED_DOMAIN_BYTES: int = 5029
+EXPECTED_DOMAIN_SHA256: str = (
+    "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0"
+)
+DOMAIN_TSV_PATH: Path = Path(__file__).resolve().parent / "DOMAIN.tsv"
+
 COMPARISON_CAPACITIES: Tuple[Fraction, ...] = (
     Fraction(0, 1),
     Fraction(1, 10),
@@ -51,61 +59,75 @@
 
 def require_exact_int(val: object, name: str) -> int:
     if isinstance(val, bool) or not isinstance(val, int):
-        raise TypeError(f"{name} must be an exact int (not bool/float), got {type(val).__name__}")
+        raise TypeError(
+            f"{name} must be an exact int (expected=int, actual={type(val).__name__})"
+        )
     return val
 
 
 def require_nonneg_int(val: object, name: str) -> int:
     v = require_exact_int(val, name)
     if v < 0:
-        raise ValueError(f"{name} must be >= 0, got {v}")
+        raise ValueError(f"{name} must be >= 0 (expected>=0, actual={v})")
     return v
 
 
 def require_f5_int(val: object, name: str) -> int:
     v = require_exact_int(val, name)
     if v < 0 or v >= 5:
-        raise ValueError(f"{name} must be in {{0,1,2,3,4}}, got {v}")
+        raise ValueError(f"{name} must be in {{0,1,2,3,4}} (expected=0..4, actual={v})")
     return v
 
 
 def require_f5_tuple(seq: object, length: int, name: str) -> Tuple[int, ...]:
     if not isinstance(seq, (tuple, list)):
-        raise TypeError(f"{name} must be a tuple or list of F_5 ints, got {type(seq).__name__}")
+        raise TypeError(
+            f"{name} must be a tuple or list of F_5 ints (expected=tuple/list, actual={type(seq).__name__})"
+        )
     if len(seq) != length:
-        raise ValueError(f"{name} must have length {length}, got {len(seq)}")
+        raise ValueError(
+            f"{name} length mismatch (expected={length}, actual={len(seq)})"
+        )
     return tuple(require_f5_int(x, f"{name}[{i}]") for i, x in enumerate(seq))
 
 
 def require_fraction(val: object, name: str) -> Fraction:
     if isinstance(val, bool):
-        raise TypeError(f"{name} must be a Fraction or exact int, not bool")
+        raise TypeError(f"{name} must be a Fraction or exact int (expected=Fraction/int, actual=bool)")
     if isinstance(val, Fraction):
         return val
     if isinstance(val, int):
         return Fraction(val, 1)
-    raise TypeError(f"{name} must be a Fraction or exact int, got {type(val).__name__}")
+    raise TypeError(
+        f"{name} must be a Fraction or exact int (expected=Fraction/int, actual={type(val).__name__})"
+    )
 
 
 def require_q_tuple(seq: object, length: int, name: str) -> Tuple[Fraction, ...]:
     if not isinstance(seq, (tuple, list)):
-        raise TypeError(f"{name} must be a tuple or list of rationals, got {type(seq).__name__}")
+        raise TypeError(
+            f"{name} must be a tuple or list of rationals (expected=tuple/list, actual={type(seq).__name__})"
+        )
     if len(seq) != length:
-        raise ValueError(f"{name} must have length {length}, got {len(seq)}")
+        raise ValueError(
+            f"{name} length mismatch (expected={length}, actual={len(seq)})"
+        )
     return tuple(require_fraction(x, f"{name}[{i}]") for i, x in enumerate(seq))
 
 
 def require_sign(val: object, name: str) -> int:
     v = require_exact_int(val, name)
     if v not in (-1, 1):
-        raise ValueError(f"{name} must be in {{-1, +1}}, got {v}")
+        raise ValueError(f"{name} must be in {{-1, +1}} (expected=-1 or +1, actual={v})")
     return v
 
 
 def require_clock(val: object, modulus: int, name: str) -> int:
     v = require_exact_int(val, name)
     if v < 0 or v >= modulus:
-        raise ValueError(f"{name} must be in 0..{modulus - 1}, got {v}")
+        raise ValueError(
+            f"{name} must be in 0..{modulus - 1} (expected=0..{modulus - 1}, actual={v})"
+        )
     return v
 
 
@@ -118,12 +140,55 @@
     b_st: Tuple[Tuple[int, int, int], ...]
     b_zero: Tuple[Tuple[int, int, int], ...]
     stencil_coeffs: Dict[Tuple[int, int, int], Fraction]
+    y1_sites: Tuple[Tuple[int, int, int], ...]
+    b2_sites: Tuple[Tuple[int, int, int], ...]
     domain_d: Tuple[Tuple[int, int, int], ...]
+    n_sites: int
+    wave_tape_basis_dim: int
+    domain_bytes: int
+    domain_sha256: str
     site_to_index: Dict[Tuple[int, int, int], int]
     port_indices: Tuple[int, int, int, int]
     y_indices: Tuple[int, int, int, int, int]
     y4_index: int
     h_neighbors: Tuple[Tuple[Tuple[int, Fraction], ...], ...]
+
+
+def load_frozen_domain_tsv(tsv_path: Path = DOMAIN_TSV_PATH) -> Tuple[int, str, Tuple[Tuple[int, int, int], ...]]:
+    if not tsv_path.is_file():
+        raise RuntimeError(f"Missing frozen DOMAIN.tsv at {tsv_path.name}")
+    raw = tsv_path.read_bytes()
+    actual_bytes = len(raw)
+    if actual_bytes != EXPECTED_DOMAIN_BYTES:
+        raise RuntimeError(
+            f"DOMAIN.tsv byte length mismatch: expected={EXPECTED_DOMAIN_BYTES}, actual={actual_bytes}"
+        )
+    actual_sha256 = hashlib.sha256(raw).hexdigest()
+    if actual_sha256 != EXPECTED_DOMAIN_SHA256:
+        raise RuntimeError(
+            f"DOMAIN.tsv sha256 mismatch: expected={EXPECTED_DOMAIN_SHA256}, actual={actual_sha256}"
+        )
+    text = raw.decode("ascii")
+    if not text.endswith("\n"):
+        raise RuntimeError("DOMAIN.tsv must end with LF")
+    lines = text.splitlines()
+    if not lines or lines[0] != "x\ty\tz":
+        raise RuntimeError(
+            f"DOMAIN.tsv header mismatch: expected='x\\ty\\tz', actual={lines[0] if lines else ''!r}"
+        )
+    pts: List[Tuple[int, int, int]] = []
+    for row_idx, line in enumerate(lines[1:], start=1):
+        parts = line.split("\t")
+        if len(parts) != 3:
+            raise RuntimeError(
+                f"DOMAIN.tsv row {row_idx} column count mismatch: expected=3, actual={len(parts)}"
+            )
+        pts.append((int(parts[0]), int(parts[1]), int(parts[2])))
+    if len(pts) != EXPECTED_DOMAIN_SITES:
+        raise RuntimeError(
+            f"DOMAIN.tsv row count mismatch: expected={EXPECTED_DOMAIN_SITES}, actual={len(pts)}"
+        )
+    return (actual_bytes, actual_sha256, tuple(pts))
 
 
 @lru_cache(maxsize=1)
@@ -141,16 +206,58 @@
                     b_st_list.append(d)
                     stencil_coeffs[d] = Fraction(SHELL_WEIGHTS[norm_sq], STENCIL_DENOM)
     b_st = tuple(sorted(b_st_list))
+    if len(b_st) != 60:
+        raise RuntimeError(f"Stencil |B_st| mismatch: expected=60, actual={len(b_st)}")
     b_zero = tuple(sorted(b_st_list + [(0, 0, 0)]))
-
-    domain_set = set()
-    for y in Y_SITES:
-        for b1 in b_zero:
-            for b2 in b_zero:
-                domain_set.add((y[0] + b1[0] + b2[0], y[1] + b1[1] + b2[1], y[2] + b1[2] + b2[2]))
+    if len(b_zero) != 61:
+        raise RuntimeError(f"Stencil |B_zero| mismatch: expected=61, actual={len(b_zero)}")
+
+    y1_set = {
+        (y[0] + b1[0], y[1] + b1[1], y[2] + b1[2])
+        for y in Y_SITES
+        for b1 in b_zero
+    }
+    b2_set = {
+        (b1[0] + b2[0], b1[1] + b2[1], b1[2] + b2[2])
+        for b1 in b_zero
+        for b2 in b_zero
+    }
+    domain_set = {
+        (u[0] + b2[0], u[1] + b2[1], u[2] + b2[2])
+        for u in y1_set
+        for b2 in b_zero
+    }
+    y1_sites = tuple(sorted(y1_set))
+    if len(y1_sites) != 142:
+        raise RuntimeError(
+            f"Constructed |Y + B_zero| mismatch: expected=142, actual={len(y1_sites)}"
+        )
+    b2_sites = tuple(sorted(b2_set))
+    if len(b2_sites) != 489:
+        raise RuntimeError(
+            f"Constructed |B_zero + B_zero| mismatch: expected=489, actual={len(b2_sites)}"
+        )
     domain_d = tuple(sorted(domain_set))
-    if len(domain_d) != 869:
-        raise RuntimeError(f"Expected |D| = 869, got {len(domain_d)}")
+    if len(domain_d) != EXPECTED_DOMAIN_SITES:
+        raise RuntimeError(
+            f"Constructed |D| = |Y + B_zero + B_zero| mismatch: expected={EXPECTED_DOMAIN_SITES}, actual={len(domain_d)}"
+        )
+
+    domain_bytes, domain_sha256, tsv_domain = load_frozen_domain_tsv()
+    if domain_d != tsv_domain:
+        first_diff = next(
+            (idx for idx, (a, b) in enumerate(zip(domain_d, tsv_domain)) if a != b),
+            len(domain_d),
+        )
+        exp_pt = domain_d[first_diff] if first_diff < len(domain_d) else None
+        act_pt = tsv_domain[first_diff] if first_diff < len(tsv_domain) else None
+        raise RuntimeError(
+            f"Constructed sorted(Y + B_zero + B_zero) mismatch against DOMAIN.tsv at index={first_diff}: "
+            f"expected={exp_pt}, actual={act_pt}"
+        )
+
+    n_sites = len(domain_d)
+    wave_tape_basis_dim = 2 * n_sites + 16
 
     site_to_index = {pt: idx for idx, pt in enumerate(domain_d)}
     port_indices = (
@@ -176,7 +283,13 @@
         b_st=b_st,
         b_zero=b_zero,
         stencil_coeffs=stencil_coeffs,
+        y1_sites=tuple(sorted(y1_set)),
+        b2_sites=tuple(sorted(b2_set)),
         domain_d=domain_d,
+        n_sites=n_sites,
+        wave_tape_basis_dim=wave_tape_basis_dim,
+        domain_bytes=domain_bytes,
+        domain_sha256=domain_sha256,
         site_to_index=site_to_index,
         port_indices=port_indices,
         y_indices=y_indices,  # type: ignore[arg-type]
@@ -200,8 +313,9 @@
     k: int
 
     def __post_init__(self) -> None:
-        object.__setattr__(self, "u", require_q_tuple(self.u, 869, "u"))
-        object.__setattr__(self, "v", require_q_tuple(self.v, 869, "v"))
+        n_sites = get_geometry().n_sites
+        object.__setattr__(self, "u", require_q_tuple(self.u, n_sites, "u"))
+        object.__setattr__(self, "v", require_q_tuple(self.v, n_sites, "v"))
         object.__setattr__(self, "A0", require_q_tuple(self.A0, 4, "A0"))
         object.__setattr__(self, "A1", require_q_tuple(self.A1, 4, "A1"))
         object.__setattr__(self, "B0", require_q_tuple(self.B0, 4, "B0"))
@@ -211,6 +325,7 @@
 
 @dataclass(frozen=True)
 class ApparatusSubstate:
+    """Rational/ancillary apparatus substate A_B (distinct from full native state Z_B)."""
     X: WaveTapeState
     W: Fraction
     b: Fraction
@@ -221,14 +336,18 @@
 
     def __post_init__(self) -> None:
         if not isinstance(self.X, WaveTapeState):
-            raise TypeError(f"X must be WaveTapeState, got {type(self.X).__name__}")
+            raise TypeError(
+                f"X must be WaveTapeState (expected=WaveTapeState, actual={type(self.X).__name__})"
+            )
         w_val = require_fraction(self.W, "W")
         b_val = require_fraction(self.b, "b")
         cap_val = require_fraction(self.B, "B")
         if cap_val < 0:
-            raise ValueError(f"Capacity B must be >= 0, got {cap_val}")
+            raise ValueError(f"Capacity B must be >= 0 (expected>=0, actual={cap_val})")
         if b_val < 0 or b_val > cap_val:
-            raise ValueError(f"Store b must satisfy 0 <= b <= B ({cap_val}), got {b_val}")
+            raise ValueError(
+                f"Store b out of bounds (expected in [0, {cap_val}], actual={b_val})"
+            )
         sig_a = require_sign(self.sigma_A, "sigma_A")
         sig_b = require_sign(self.sigma_B, "sigma_B")
         d_tup = require_f5_tuple(self.d, 2, "d")
@@ -242,6 +361,7 @@
 
 @dataclass(frozen=True)
 class CompositeState:
+    """Full coupled state in Z_B = N_0 x (F_5^6)^2 x A_B x (Z/8Z)."""
     n: int
     x_A: Tuple[int, ...]
     x_B: Tuple[int, ...]
@@ -259,14 +379,18 @@
         xa = require_f5_tuple(self.x_A, 6, "x_A")
         xb = require_f5_tuple(self.x_B, 6, "x_B")
         if not isinstance(self.X, WaveTapeState):
-            raise TypeError(f"X must be WaveTapeState, got {type(self.X).__name__}")
+            raise TypeError(
+                f"X must be WaveTapeState (expected=WaveTapeState, actual={type(self.X).__name__})"
+            )
         w_val = require_fraction(self.W, "W")
         b_val = require_fraction(self.b, "b")
         cap_val = require_fraction(self.B, "B")
         if cap_val < 0:
-            raise ValueError(f"Capacity B must be >= 0, got {cap_val}")
+            raise ValueError(f"Capacity B must be >= 0 (expected>=0, actual={cap_val})")
         if b_val < 0 or b_val > cap_val:
-            raise ValueError(f"Store b must satisfy 0 <= b <= B ({cap_val}), got {b_val}")
+            raise ValueError(
+                f"Store b out of bounds (expected in [0, {cap_val}], actual={b_val})"
+            )
         sig_a = require_sign(self.sigma_A, "sigma_A")
         sig_b = require_sign(self.sigma_B, "sigma_B")
         d_tup = require_f5_tuple(self.d, 2, "d")
@@ -329,7 +453,8 @@
 # ---------------------------------------------------------------------------
 
 def zero_qd() -> Tuple[Fraction, ...]:
-    return (Fraction(0, 1),) * 869
+    n_sites = get_geometry().n_sites
+    return (Fraction(0, 1),) * n_sites
 
 
 def zero_q4() -> Tuple[Fraction, ...]:
@@ -343,7 +468,9 @@
 
 def dot_vec(a: Sequence[Fraction], b: Sequence[Fraction]) -> Fraction:
     if len(a) != len(b):
-        raise ValueError(f"Vector length mismatch: {len(a)} vs {len(b)}")
+        raise ValueError(
+            f"Vector length mismatch in dot_vec (expected={len(a)}, actual={len(b)})"
+        )
     total = Fraction(0, 1)
     for x, y in zip(a, b):
         if x != 0 and y != 0:
@@ -354,21 +481,21 @@
 def apply_P(z: Sequence[Fraction]) -> Tuple[Fraction, ...]:
     z_tup = require_q_tuple(z, 4, "z")
     geom = get_geometry()
-    out = [Fraction(0, 1)] * 869
+    out = [Fraction(0, 1)] * geom.n_sites
     for j, idx in enumerate(geom.port_indices):
         out[idx] = z_tup[j]
     return tuple(out)
 
 
 def apply_PT(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
-    u_tup = require_q_tuple(u, 869, "u")
     geom = get_geometry()
+    u_tup = require_q_tuple(u, geom.n_sites, "u")
     return tuple(u_tup[idx] for idx in geom.port_indices)
 
 
 def apply_K(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
-    u_tup = require_q_tuple(u, 869, "u")
     geom = get_geometry()
+    u_tup = require_q_tuple(u, geom.n_sites, "u")
     out = list(u_tup)
     half = Fraction(1, 2)
     for idx in geom.port_indices:
@@ -377,8 +504,8 @@
 
 
 def apply_J0(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
-    u_tup = require_q_tuple(u, 869, "u")
     geom = get_geometry()
+    u_tup = require_q_tuple(u, geom.n_sites, "u")
     out = list(u_tup)
     zero = Fraction(0, 1)
     for idx in geom.port_indices:
@@ -387,9 +514,9 @@
 
 
 def apply_H(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
-    u_tup = require_q_tuple(u, 869, "u")
     geom = get_geometry()
-    out = [Fraction(0, 1)] * 869
+    u_tup = require_q_tuple(u, geom.n_sites, "u")
+    out = [Fraction(0, 1)] * geom.n_sites
     nonzero_indices = [i for i, val in enumerate(u_tup) if val != 0]
     if not nonzero_indices:
         return tuple(out)
@@ -402,9 +529,10 @@
 
 
 def apply_LD(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
-    u_tup = require_q_tuple(u, 869, "u")
+    geom = get_geometry()
+    u_tup = require_q_tuple(u, geom.n_sites, "u")
     hu = apply_H(u_tup)
-    return tuple(2 * u_tup[i] - hu[i] for i in range(869))
+    return tuple(2 * u_tup[i] - hu[i] for i in range(geom.n_sites))
 
 
 def apply_T(u: Sequence[Fraction]) -> Tuple[Fraction, ...]:
@@ -415,7 +543,7 @@
     z_tup = require_q_tuple(z, 4, "z")
     geom = get_geometry()
     s_over_5 = (z_tup[0] + z_tup[1] + z_tup[2] + z_tup[3]) * Fraction(1, 5)
-    out = [Fraction(0, 1)] * 869
+    out = [Fraction(0, 1)] * geom.n_sites
     for j, idx in enumerate(geom.port_indices):
         out[idx] = z_tup[j] - s_over_5
     out[geom.y4_index] = -s_over_5
@@ -438,23 +566,27 @@
 
 
 def wave_energy(u: Sequence[Fraction], v: Sequence[Fraction]) -> Fraction:
-    u_tup = require_q_tuple(u, 869, "u")
-    v_tup = require_q_tuple(v, 869, "v")
+    geom = get_geometry()
+    u_tup = require_q_tuple(u, geom.n_sites, "u")
+    v_tup = require_q_tuple(v, geom.n_sites, "v")
     hv = apply_H(v_tup)
     return Fraction(1, 2) * (dot_vec(u_tup, u_tup) + dot_vec(v_tup, v_tup) - dot_vec(u_tup, hv))
 
 
 def wave_energy_difference_form(u: Sequence[Fraction], v: Sequence[Fraction]) -> Fraction:
-    u_tup = require_q_tuple(u, 869, "u")
-    v_tup = require_q_tuple(v, 869, "v")
-    diff = tuple(v_tup[i] - u_tup[i] for i in range(869))
+    geom = get_geometry()
+    u_tup = require_q_tuple(u, geom.n_sites, "u")
+    v_tup = require_q_tuple(v, geom.n_sites, "v")
+    diff = tuple(v_tup[i] - u_tup[i] for i in range(geom.n_sites))
     ld_v = apply_LD(v_tup)
     return Fraction(1, 2) * (dot_vec(diff, diff) + dot_vec(u_tup, ld_v))
 
 
 def full_classical_energy(X: WaveTapeState) -> Fraction:
     if not isinstance(X, WaveTapeState):
-        raise TypeError(f"X must be WaveTapeState, got {type(X).__name__}")
+        raise TypeError(
+            f"X must be WaveTapeState (expected=WaveTapeState, actual={type(X).__name__})"
+        )
     tape_norm_sq = (
         dot_vec(X.A0, X.A0)
         + dot_vec(X.A1, X.A1)
@@ -574,13 +706,16 @@
 
 def F_step(X: WaveTapeState) -> WaveTapeState:
     if not isinstance(X, WaveTapeState):
-        raise TypeError(f"X must be WaveTapeState, got {type(X).__name__}")
+        raise TypeError(
+            f"X must be WaveTapeState (expected=WaveTapeState, actual={type(X).__name__})"
+        )
+    n_sites = get_geometry().n_sites
     hv = apply_H(X.v)
     j0u = apply_J0(X.u)
     pa0 = apply_P(X.A0)
-    rhs = tuple(hv[i] - j0u[i] + 4 * pa0[i] for i in range(869))
+    rhs = tuple(hv[i] - j0u[i] + 4 * pa0[i] for i in range(n_sites))
     w_next = apply_K(rhs)
-    pt_diff = apply_PT(tuple(w_next[i] - X.u[i] for i in range(869)))
+    pt_diff = apply_PT(tuple(w_next[i] - X.u[i] for i in range(n_sites)))
     b_out = tuple(X.A0[j] - Fraction(1, 2) * pt_diff[j] for j in range(4))
     return WaveTapeState(
         u=X.v,
@@ -595,16 +730,19 @@
 
 def F_inverse(X_prime: WaveTapeState) -> WaveTapeState:
     if not isinstance(X_prime, WaveTapeState):
-        raise TypeError(f"X_prime must be WaveTapeState, got {type(X_prime).__name__}")
+        raise TypeError(
+            f"X_prime must be WaveTapeState (expected=WaveTapeState, actual={type(X_prime).__name__})"
+        )
+    n_sites = get_geometry().n_sites
     v = X_prime.u
     w_next = X_prime.v
     b_out = X_prime.B0
     hv = apply_H(v)
     j0w = apply_J0(w_next)
     pb = apply_P(b_out)
-    rhs = tuple(hv[i] - j0w[i] + 4 * pb[i] for i in range(869))
+    rhs = tuple(hv[i] - j0w[i] + 4 * pb[i] for i in range(n_sites))
     u = apply_K(rhs)
-    pt_diff = apply_PT(tuple(w_next[i] - u[i] for i in range(869)))
+    pt_diff = apply_PT(tuple(w_next[i] - u[i] for i in range(n_sites)))
     a0 = tuple(b_out[j] + Fraction(1, 2) * pt_diff[j] for j in range(4))
     return WaveTapeState(
         u=u,
@@ -620,23 +758,25 @@
 def contact_energy_increment(
     u: Sequence[Fraction], v: Sequence[Fraction], sigma: int, r: Sequence[int]
 ) -> Fraction:
-    u_tup = require_q_tuple(u, 869, "u")
-    v_tup = require_q_tuple(v, 869, "v")
+    n_sites = get_geometry().n_sites
+    u_tup = require_q_tuple(u, n_sites, "u")
+    v_tup = require_q_tuple(v, n_sites, "v")
     sig = require_sign(sigma, "sigma")
     a = source_field_for_receiver(r)
-    v_shifted = tuple(v_tup[i] + sig * a[i] for i in range(869))
+    v_shifted = tuple(v_tup[i] + sig * a[i] for i in range(n_sites))
     return wave_energy(u_tup, v_shifted) - wave_energy(u_tup, v_tup)
 
 
 def contact_energy_increment_bilinear(
     u: Sequence[Fraction], v: Sequence[Fraction], sigma: int, r: Sequence[int]
 ) -> Fraction:
-    u_tup = require_q_tuple(u, 869, "u")
-    v_tup = require_q_tuple(v, 869, "v")
+    n_sites = get_geometry().n_sites
+    u_tup = require_q_tuple(u, n_sites, "u")
+    v_tup = require_q_tuple(v, n_sites, "v")
     sig = require_sign(sigma, "sigma")
     a = source_field_for_receiver(r)
     hu = apply_H(u_tup)
-    wave_term = tuple(v_tup[i] - Fraction(1, 2) * hu[i] for i in range(869))
+    wave_term = tuple(v_tup[i] - Fraction(1, 2) * hu[i] for i in range(n_sites))
     return Fraction(1, 2) * dot_vec(a, a) + sig * dot_vec(a, wave_term)
 
 
@@ -644,10 +784,13 @@
     substate: ApparatusSubstate, r_A: Sequence[int]
 ) -> ApparatusSubstate:
     if not isinstance(substate, ApparatusSubstate):
-        raise TypeError(f"substate must be ApparatusSubstate, got {type(substate).__name__}")
+        raise TypeError(
+            f"substate must be ApparatusSubstate (expected=ApparatusSubstate, actual={type(substate).__name__})"
+        )
+    n_sites = get_geometry().n_sites
     ra = require_f5_tuple(r_A, 2, "r_A")
     a_vec = source_field_for_receiver(ra)
-    v_cand = tuple(substate.X.v[i] + substate.sigma_A * a_vec[i] for i in range(869))
+    v_cand = tuple(substate.X.v[i] + substate.sigma_A * a_vec[i] for i in range(n_sites))
     delta_a = wave_energy(substate.X.u, v_cand) - wave_energy(substate.X.u, substate.X.v)
     b_cand = substate.b - delta_a
     if 0 <= b_cand <= substate.B:
@@ -674,9 +817,12 @@
 
 def funded_contact_B_substate(substate: ApparatusSubstate) -> ApparatusSubstate:
     if not isinstance(substate, ApparatusSubstate):
-        raise TypeError(f"substate must be ApparatusSubstate, got {type(substate).__name__}")
+        raise TypeError(
+            f"substate must be ApparatusSubstate (expected=ApparatusSubstate, actual={type(substate).__name__})"
+        )
+    n_sites = get_geometry().n_sites
     a_vec = source_field_for_receiver(substate.d)
-    v_cand = tuple(substate.X.v[i] + substate.sigma_B * a_vec[i] for i in range(869))
+    v_cand = tuple(substate.X.v[i] + substate.sigma_B * a_vec[i] for i in range(n_sites))
     delta_b = wave_energy(substate.X.u, v_cand) - wave_energy(substate.X.u, substate.X.v)
     b_cand = substate.b - delta_b
     if 0 <= b_cand <= substate.B:
@@ -703,7 +849,9 @@
 
 def funded_contact_A(state: CompositeState) -> CompositeState:
     if not isinstance(state, CompositeState):
-        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
+        raise TypeError(
+            f"state must be CompositeState (expected=CompositeState, actual={type(state).__name__})"
+        )
     sub = funded_contact_A_substate(state.to_apparatus_substate(), receiver_of(state.x_A))
     return CompositeState(
         n=state.n,
@@ -722,7 +870,9 @@
 
 def funded_contact_B(state: CompositeState) -> CompositeState:
     if not isinstance(state, CompositeState):
-        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
+        raise TypeError(
+            f"state must be CompositeState (expected=CompositeState, actual={type(state).__name__})"
+        )
     sub = funded_contact_B_substate(state.to_apparatus_substate())
     return CompositeState(
         n=state.n,
@@ -740,14 +890,17 @@
 
 
 # ---------------------------------------------------------------------------
-# Eight-phase static-source apparatus and coupled transitions
+# Supplied-label apparatus substate transitions T_{c,B}^{(r_A, r_B)} and coupled G_B
 # ---------------------------------------------------------------------------
 
 def apparatus_row_map(
     substate: ApparatusSubstate, c: int, r_A: Sequence[int], r_B: Sequence[int]
 ) -> ApparatusSubstate:
+    """Supplied-label apparatus substate row map T_{c,B}^{(r_A, r_B)} on A_B."""
     if not isinstance(substate, ApparatusSubstate):
-        raise TypeError(f"substate must be ApparatusSubstate, got {type(substate).__name__}")
+        raise TypeError(
+            f"substate must be ApparatusSubstate (expected=ApparatusSubstate, actual={type(substate).__name__})"
+        )
     phase = require_clock(c, 8, "c")
     ra = require_f5_tuple(r_A, 2, "r_A")
     rb = require_f5_tuple(r_B, 2, "r_B")
@@ -781,9 +934,10 @@
 def apparatus_row_map_inverse(
     substate_prime: ApparatusSubstate, c: int, r_A: Sequence[int], r_B: Sequence[int]
 ) -> ApparatusSubstate:
+    """Two-sided inverse (T_{c,B}^{(r_A, r_B)})^{-1} on the supplied-label substate A_B."""
     if not isinstance(substate_prime, ApparatusSubstate):
         raise TypeError(
-            f"substate_prime must be ApparatusSubstate, got {type(substate_prime).__name__}"
+            f"substate_prime must be ApparatusSubstate (expected=ApparatusSubstate, actual={type(substate_prime).__name__})"
         )
     phase = require_clock(c, 8, "c")
     ra = require_f5_tuple(r_A, 2, "r_A")
@@ -818,6 +972,7 @@
 def apparatus_step(
     substate: ApparatusSubstate, c: int, r_A: Sequence[int], r_B: Sequence[int]
 ) -> Tuple[ApparatusSubstate, int]:
+    """Supplied-label apparatus substate step S_B^{(r_A, r_B)} on A_B x (Z/8Z)."""
     phase = require_clock(c, 8, "c")
     return (apparatus_row_map(substate, phase, r_A, r_B), (phase + 1) % 8)
 
@@ -825,6 +980,7 @@
 def apparatus_step_inverse(
     substate_prime: ApparatusSubstate, c_prime: int, r_A: Sequence[int], r_B: Sequence[int]
 ) -> Tuple[ApparatusSubstate, int]:
+    """Two-sided inverse (S_B^{(r_A, r_B)})^{-1} on the supplied-label substate A_B x (Z/8Z)."""
     phase_prime = require_clock(c_prime, 8, "c_prime")
     prev_phase = (phase_prime - 1) % 8
     return (apparatus_row_map_inverse(substate_prime, prev_phase, r_A, r_B), prev_phase)
@@ -833,7 +989,9 @@
 def coupled_step(state: CompositeState) -> CompositeState:
     """Execute one phase row of G_B on arbitrary valid occupied state in Z_B."""
     if not isinstance(state, CompositeState):
-        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
+        raise TypeError(
+            f"state must be CompositeState (expected=CompositeState, actual={type(state).__name__})"
+        )
     c = state.c
     if c == 0:
         n1, xa1, xb1 = native_tick(state.n, state.x_A, state.x_B)
@@ -973,7 +1131,9 @@
 ) -> Union[CompositeState, Tuple[CompositeState, ...]]:
     """Advance 7 phase steps (c=0 -> c=7, n=0 -> n=5 on a ready state)."""
     if not isinstance(state, CompositeState):
-        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
+        raise TypeError(
+            f"state must be CompositeState (expected=CompositeState, actual={type(state).__name__})"
+        )
     boundaries: List[CompositeState] = [state]
     cur = state
     for _ in range(7):
@@ -989,7 +1149,9 @@
 ) -> Union[CompositeState, Tuple[CompositeState, ...]]:
     """Advance 8 phase steps (7 steps to completion c=7 plus 8th rollover c: 7 -> 0)."""
     if not isinstance(state, CompositeState):
-        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
+        raise TypeError(
+            f"state must be CompositeState (expected=CompositeState, actual={type(state).__name__})"
+        )
     boundaries: List[CompositeState] = [state]
     cur = state
     for _ in range(8):
@@ -1114,11 +1276,13 @@
 ) -> Tuple[ChronologicalCutEntry, ChronologicalCutEntry, ChronologicalCutEntry, ChronologicalCutEntry]:
     """Read the 4 chronological cuts directly from (n, c) and tapes (A0, A1, B0, B1)."""
     if not isinstance(state, CompositeState):
-        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
+        raise TypeError(
+            f"state must be CompositeState (expected=CompositeState, actual={type(state).__name__})"
+        )
     expected_n = VALID_FIRST_PERIOD_CLOCKS.get(state.c)
     if expected_n != state.n:
         raise ValueError(
-            f"State (c={state.c}, n={state.n}) is not a valid first-period boundary"
+            f"State (c={state.c}, n={state.n}) is not a valid first-period boundary (expected n={expected_n})"
         )
     unwritten = ChronologicalCutEntry(
         status="UNWRITTEN", use=None, cut=None, slot_name=None, vector=None
@@ -1160,9 +1324,13 @@
 ) -> DirectPortReadout:
     """Extract only (b0, b2) and declared acceptance/context fields at c=7, n=5."""
     if not isinstance(state, CompositeState):
-        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
+        raise TypeError(
+            f"state must be CompositeState (expected=CompositeState, actual={type(state).__name__})"
+        )
     if state.c != 7 or state.n != 5:
-        raise ValueError(f"Direct port readout requires completion boundary c=7, n=5; got c={state.c}, n={state.n}")
+        raise ValueError(
+            f"Direct port readout requires completion boundary (expected=(c=7, n=5), actual=(c={state.c}, n={state.n}))"
+        )
     return DirectPortReadout(
         b0=state.X.A0,
         b2=state.X.B1,
@@ -1191,11 +1359,11 @@
     """
     if isinstance(b0, (CompositeState, ApparatusSubstate, WaveTapeState)):
         raise TypeError(
-            "direct_source_reader forbids CompositeState/ApparatusSubstate/WaveTapeState access"
+            f"direct_source_reader forbids {type(b0).__name__} access"
         )
     if isinstance(b2, (CompositeState, ApparatusSubstate, WaveTapeState)):
         raise TypeError(
-            "direct_source_reader forbids CompositeState/ApparatusSubstate/WaveTapeState access"
+            f"direct_source_reader forbids {type(b2).__name__} access"
         )
 
     if isinstance(b0, DirectPortReadout):
@@ -1319,7 +1487,9 @@
 ) -> Dict[str, object]:
     """Necessary-and-sufficient 4-part recognizer for Im(Phi_{(c0, c1, b_init, B)})."""
     if not isinstance(state, CompositeState):
-        raise TypeError(f"state must be CompositeState, got {type(state).__name__}")
+        raise TypeError(
+            f"state must be CompositeState (expected=CompositeState, actual={type(state).__name__})"
+        )
 
     # Test 1: Clock n=5, c=7 and C_3 receivers at n=5
     if state.n != 5 or state.c != 7:
@@ -1358,7 +1528,7 @@
     if state.d != r_b:
         return {"valid": False, "failed_test": "test3_delayed_buffer_d"}
 
-    # Test 4: Apparatus two-sided inverse (M_{7,B}^{(r_A, r_B)})^{-1}
+    # Test 4: Supplied-label apparatus substate two-sided inverse (M_{7,B}^{(r_A, r_B)})^{-1}
     sub = state.to_apparatus_substate()
     c_cur = 7
     for _ in range(7):
@@ -1394,7 +1564,7 @@
         if sub.X.B1 != c1_exp:
             return {"valid": False, "failed_test": "test4_initial_archive_c1"}
 
-    # Also verify that forward 7-step replay from the recovered initial state matches state
+    # Verify that forward 7-step replay from the recovered initial state matches state
     replayed = run_seven_steps(
         prepare_ready_state(
             p_a, p_b, state.B, b_init=sub.b, c0=sub.X.B0, c1=sub.X.B1
@@ -1431,7 +1601,7 @@
 
 
 # ---------------------------------------------------------------------------
-# Shared 1200-record comparison mode serialization (TWOUSE-COMPARE-v1)
+# Shared 1200-record comparison mode serialization (TWOUSE-COMPARE-v2)
 # ---------------------------------------------------------------------------
 
 def encode_rat(val: Fraction) -> List[int]:
@@ -1464,9 +1634,11 @@
     return json.dumps(record, separators=(",", ":"), ensure_ascii=True) + "\n"
 
 
-def compute_comparison_digest() -> Tuple[int, str]:
-    """Stream the 1200 frozen comparison records and compute their SHA-256 digest."""
-    hasher = hashlib.sha256()
+def compute_comparison_digest() -> Tuple[str, int, str]:
+    """Stream the 1200 frozen comparison records and compute their TWOUSE-COMPARE-v2 digest."""
+    geom = get_geometry()
+    prefix = f"TWOUSE-COMPARE-v2\nDOMAIN_SHA256 {geom.domain_sha256}\n".encode("ascii")
+    hasher = hashlib.sha256(prefix)
     count = 0
     for cap in COMPARISON_CAPACITIES:
         for h_a in range(5):
@@ -1475,11 +1647,16 @@
                 p_b = (h_b, 0, 0, 0)
                 init_state = prepare_ready_state(p_a, p_b, cap, b_init=cap)
                 boundaries = run_seven_steps(init_state, return_boundaries=True)
-                assert isinstance(boundaries, tuple) and len(boundaries) == 8
+                if not isinstance(boundaries, tuple) or len(boundaries) != 8:
+                    raise RuntimeError(
+                        f"Boundary count mismatch (expected=8, actual={len(boundaries) if isinstance(boundaries, tuple) else 'non-tuple'})"
+                    )
                 for c_idx, b_state in enumerate(boundaries):
                     if b_state.c != c_idx:
-                        raise RuntimeError(f"Boundary clock mismatch: {b_state.c} != {c_idx}")
+                        raise RuntimeError(
+                            f"Boundary clock mismatch (expected={c_idx}, actual={b_state.c})"
+                        )
                     line = serialize_comparison_record(cap, h_a, h_b, b_state)
                     hasher.update(line.encode("ascii"))
                     count += 1
-    return (count, hasher.hexdigest())
+    return (geom.domain_sha256, count, hasher.hexdigest())
```

---

## 4. Full static unified diff of `verify.py`

```diff
--- a/notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py
+++ b/notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py
@@ -1,18 +1,19 @@
 #!/usr/bin/env python3
-"""Executable audit, witness generator, and comparison runner for Lane I (#1507).
-
-NON-CANONICAL / L1 executable incubation audit.
+"""Executable audit, witness generator, and comparison runner for Lane I2 (#1515).
+
+NON-CANONICAL / L1 executable incubation audit on reconciled 705-site D.
 Original work Apache-2.0, A. M. Thorn, 2026-10-15.
 
 CLI modes:
-  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py
+  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py
       Run full scientific audit (T01-T18 and X01-X10) and print deterministic
       scientific stdout including witness boundary states.
-  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py --compare
+  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --compare
       Run separate 1200-record comparison mode and print:
-      TWOUSE-COMPARE-v1 records=1200 sha256=<64 lowercase hex>
-  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-N/verify.py --witnesses
-      Print detailed JSON witness boundary trajectories.
+      TWOUSE-COMPARE-v2 domain_sha256=2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0 records=1200 sha256=<64 lowercase hex>
+  python3 notes/C-FUNDED-TWO-USE-EXECUTABLE-2-N/verify.py --witnesses
+      Print witness boundary trajectories and summary for the 7-step (1,4)/(4,1)
+      order comparison, dirty-archive c1=e0 case, and lower/upper stock refusals.
 """
 
 from __future__ import annotations
@@ -20,7 +21,6 @@
 from fractions import Fraction
 import hashlib
 import inspect
-import json
 from pathlib import Path
 import sys
 from typing import Dict, List, Sequence, Tuple
@@ -128,6 +128,22 @@
 }
 
 
+# ---------------------------------------------------------------------------
+# Explicit expected/actual assertion helpers and formatting
+# ---------------------------------------------------------------------------
+
+def require_eq(actual: object, expected: object, label: str) -> None:
+    if actual != expected:
+        raise AssertionError(f"{label}: expected={expected!r}, actual={actual!r}")
+
+
+def require_true(
+    cond: bool, label: str, *, expected: object = True, actual: object = False
+) -> None:
+    if not cond:
+        raise AssertionError(f"{label}: expected={expected!r}, actual={actual!r}")
+
+
 def fmt_frac(val: Fraction) -> str:
     return f"{val.numerator}/{val.denominator}" if val.denominator != 1 else f"{val.numerator}"
 
@@ -183,37 +199,59 @@
 
 def run_t01_geometry_stencil_and_operators() -> str:
     geom = app.get_geometry()
-    assert len(geom.b_st) == 60
-    assert len(geom.b_zero) == 61
-    assert len(geom.domain_d) == 869
-    assert list(geom.domain_d) == sorted(geom.domain_d)
-    assert sum(geom.stencil_coeffs.values(), Fraction(0, 1)) == Fraction(8, 9)
+    require_eq(len(app.Y_SITES), 5, "T01.|Y|")
+    require_eq(len(geom.b_st), 60, "T01.|B_st|")
+    require_eq(len(geom.b_zero), 61, "T01.|B_zero|")
+    require_eq(len(geom.y1_sites), 142, "T01.|Y+B_zero|")
+    require_eq(len(geom.b2_sites), 489, "T01.|B_zero+B_zero|")
+    require_eq(len(geom.domain_d), 705, "T01.|D|")
+    require_eq(geom.n_sites, 705, "T01.n_sites")
+    require_eq(geom.wave_tape_basis_dim, 1426, "T01.wave_tape_basis_dim")
+    require_eq(geom.domain_bytes, 5029, "T01.DOMAIN.tsv.bytes")
+    require_eq(
+        geom.domain_sha256,
+        "2e9b77cf8c507b9bc6675d9a07bf8e27ad88921c72c1efc22dcf5bdb41d8a7c0",
+        "T01.DOMAIN.tsv.sha256",
+    )
+    require_eq(list(geom.domain_d), sorted(geom.domain_d), "T01.domain_d.sorted")
+    require_eq(
+        sum(geom.stencil_coeffs.values(), Fraction(0, 1)),
+        Fraction(8, 9),
+        "T01.stencil_sum",
+    )
 
     # Check P^T P = I_4, P^T J_0 = 0, K P = (1/2) P, P^T S = G_source
     for j in range(4):
         ej = app.basis_q4(j)
         pej = app.apply_P(ej)
-        assert app.apply_PT(pej) == ej
-        assert app.apply_PT(app.apply_J0(pej)) == app.zero_q4()
+        require_eq(app.apply_PT(pej), ej, f"T01.PT_P[e_{j}]")
+        require_eq(app.apply_PT(app.apply_J0(pej)), app.zero_q4(), f"T01.PT_J0[P e_{j}]")
         k_pej = app.apply_K(pej)
-        assert k_pej == tuple(Fraction(1, 2) * x for x in pej)
+        require_eq(
+            k_pej,
+            tuple(Fraction(1, 2) * x for x in pej),
+            f"T01.K_P[e_{j}]",
+        )
         sej = app.apply_S(ej)
         pt_sej = app.apply_PT(sej)
         exp_g = tuple(Fraction(4, 5) if i == j else Fraction(-1, 5) for i in range(4))
-        assert pt_sej == exp_g
-        assert app.dot_vec(sej, sej) == Fraction(4, 5)
+        require_eq(pt_sej, exp_g, f"T01.PT_S[e_{j}]")
+        require_eq(app.dot_vec(sej, sej), Fraction(4, 5), f"T01.||S e_{j}||^2")
 
     # Check J_p = P^T H P = (59 I_4 + 1 1^T)/54 and M = P^T H S = (1770 I_4 - v 1^T)/1620
     ops = app.get_derived_operators()
     for r in range(4):
         for c in range(4):
             exp_jp = Fraction(60 if r == c else 1, 54)
-            assert ops.Jp[r][c] == exp_jp
+            require_eq(ops.Jp[r][c], exp_jp, f"T01.Jp[{r},{c}]")
             exp_m = Fraction((1770 if r == c else 0) - EXPECTED_V_VECTOR[r], 1620)
-            assert ops.M[r][c] == exp_m
-            assert ops.R0[r][c] == -Fraction(1, 4) * exp_m
-
-    return "T01 PASS: |B_st|=60, diag=8/9, |D|=869, P^T P=I_4, J_p and M verified"
+            require_eq(ops.M[r][c], exp_m, f"T01.M[{r},{c}]")
+            require_eq(ops.R0[r][c], -Fraction(1, 4) * exp_m, f"T01.R0[{r},{c}]")
+
+    return (
+        "T01 PASS: |B_st|=60, |B_zero|=61, |Y+B_zero|=142, |B_zero+B_zero|=489, "
+        "|D|=705, dim=1426, DOMAIN.tsv sha256 verified, P^T P=I_4, J_p and M verified"
+    )
 
 
 def run_t02_generators_and_v_non_invertibility() -> str:
@@ -234,17 +272,27 @@
                             )
                             for g in range(5):
                                 gx = app.apply_generator(g, x)
-                                assert app.apply_generator(g, gx) == x
-                                assert sum(gx) % 5 == expected_sums[g]
+                                require_eq(
+                                    app.apply_generator(g, gx),
+                                    x,
+                                    f"T02.involution[g={g},x={x}]",
+                                )
+                                require_eq(
+                                    sum(gx) % 5,
+                                    expected_sums[g],
+                                    f"T02.sum_action[g={g},x={x}]",
+                                )
 
     x_coll_1 = (0, 0, 0, 0, 0, 1)
     x_coll_2 = (2, 1, 3, 4, 2, 2)
-    assert app.native_selector(0, x_coll_1) == 1
-    assert app.native_selector(0, x_coll_2) == 4
+    require_eq(app.native_selector(0, x_coll_1), 1, "T02.selector(x_coll_1)")
+    require_eq(app.native_selector(0, x_coll_2), 4, "T02.selector(x_coll_2)")
     v1 = app.native_tick(0, x_coll_1, x_coll_1)
     v2 = app.native_tick(0, x_coll_2, x_coll_2)
-    assert v1 == v2 == (1, (0, 0, 0, 0, 0, 4), (0, 0, 0, 0, 0, 4))
-    assert v1[0] == 1 != 0
+    expected_v = (1, (0, 0, 0, 0, 0, 4), (0, 0, 0, 0, 0, 4))
+    require_eq(v1, expected_v, "T02.V(x_coll_1)")
+    require_eq(v2, expected_v, "T02.V(x_coll_2)")
+    require_eq(v1[0], 1, "T02.n_increment")
     return "T02 PASS: 5 generators involutive on 15625 states; V collision at n=0 verified"
 
 
@@ -269,31 +317,34 @@
                     j4 = app.native_selector(4, x4)
                     _, x5 = app.native_tick_single(4, x4)
 
-                    assert (j0, j1, j2, j3, j4) == EXPECTED_CANONICAL_SELECTORS[h]
+                    require_eq(
+                        (j0, j1, j2, j3, j4),
+                        EXPECTED_CANONICAL_SELECTORS[h],
+                        f"T03.selectors[p={p}]",
+                    )
                     c1, c2, c3 = EXPECTED_C1_C2_C3[h]
-                    assert app.receiver_of(x1) == c1
-                    assert app.receiver_of(x2) == c2
-                    assert app.receiver_of(x3) == c3
-                    assert sum(x3) % 5 == 1
-                    assert sum(x4) % 5 == 4
-                    assert x4 == app.apply_generator(1, x3)
-                    assert x5 == x3
-                    assert app.receiver_of(x5) == c3
-                    assert app.eta_lift(c1) == EXPECTED_Z5_VECTORS[h]
+                    require_eq(app.receiver_of(x1), c1, f"T03.C1[p={p}]")
+                    require_eq(app.receiver_of(x2), c2, f"T03.C2[p={p}]")
+                    require_eq(app.receiver_of(x3), c3, f"T03.C3[p={p}]")
+                    require_eq(sum(x3) % 5, 1, f"T03.z6(x3)[p={p}]")
+                    require_eq(sum(x4) % 5, 4, f"T03.z6(x4)[p={p}]")
+                    require_eq(x4, app.apply_generator(1, x3), f"T03.x4==g1(x3)[p={p}]")
+                    require_eq(x5, x3, f"T03.x5==x3[p={p}]")
+                    require_eq(app.receiver_of(x5), c3, f"T03.C5[p={p}]")
+                    require_eq(app.eta_lift(c1), EXPECTED_Z5_VECTORS[h], f"T03.eta(C1)[p={p}]")
 
                     x0_rec = app.apply_generator(
                         j0, app.apply_generator(j1, app.apply_generator(j2, x5))
                     )
-                    assert x0_rec == x0
-                    assert x0_rec[:4] == p
-                    assert sum(x0_rec[:4]) % 5 == h
-
-    assert counts == {0: 125, 1: 125, 2: 125, 3: 125, 4: 125}
+                    require_eq(x0_rec, x0, f"T03.x0_rec[p={p}]")
+                    require_eq(x0_rec[:4], p, f"T03.p_rec[p={p}]")
+                    require_eq(sum(x0_rec[:4]) % 5, h, f"T03.h_rec[p={p}]")
+
+    require_eq(counts, {0: 125, 1: 125, 2: 125, 3: 125, 4: 125}, "T03.class_counts")
     return "T03 PASS: all 625 single-head preparations (125/class) audited and inverted"
 
 
 def run_t04_paired_factorization_390625() -> str:
-    # Precompute all 625 single-head 5-tick trajectories and verify 625x625 product
     single_trajs: List[Tuple[Tuple[int, int, int, int], int, Tuple[int, ...], Tuple[int, ...]]] = []
     for p0 in range(5):
         for p1 in range(5):
@@ -319,69 +370,118 @@
         rec_x0a = app.apply_generator(
             sela[0], app.apply_generator(sela[1], app.apply_generator(sela[2], x5a))
         )
-        assert rec_x0a == (pa[0], pa[1], pa[2], pa[3], 0, 1)
-        assert app.receiver_of(x1a) == EXPECTED_C1_C2_C3[ha][0]
+        require_eq(rec_x0a, (pa[0], pa[1], pa[2], pa[3], 0, 1), f"T04.rec_x0a[pa={pa}]")
+        require_eq(app.receiver_of(x1a), EXPECTED_C1_C2_C3[ha][0], f"T04.C1_A[pa={pa}]")
         for pb, hb, x1b, x5b in single_trajs:
             total_pairs += 1
             fibre_counts[(ha, hb)] += 1
-            assert c3_to_h[app.receiver_of(x5a)] == ha
-            assert c3_to_h[app.receiver_of(x5b)] == hb
-            assert app.receiver_of(x1b) == EXPECTED_C1_C2_C3[hb][0]
-
-    assert total_pairs == 390625
-    assert all(cnt == 15625 for cnt in fibre_counts.values())
-
-    # Verify apparatus state at c=0..7 is identical for distinct representatives in same fibre
+            require_eq(c3_to_h[app.receiver_of(x5a)], ha, "T04.c3_to_h_A")
+            require_eq(c3_to_h[app.receiver_of(x5b)], hb, "T04.c3_to_h_B")
+            require_eq(app.receiver_of(x1b), EXPECTED_C1_C2_C3[hb][0], "T04.C1_B")
+
+    require_eq(total_pairs, 390625, "T04.total_pairs")
+    for pair_key, cnt in fibre_counts.items():
+        require_eq(cnt, 15625, f"T04.fibre_count[{pair_key}]")
+
+    # Verify apparatus substate at c=0..7 is identical for distinct representatives in same fibre
     for ha in range(5):
         for hb in range(5):
             p_a1 = (ha, 0, 0, 0)
             p_a2 = ((ha - 1) % 5, 1, 2, 3)
             p_b1 = (hb, 0, 0, 0)
             p_b2 = (2, (hb - 2) % 5, 4, 1)
-            assert sum(p_a1) % 5 == sum(p_a2) % 5 == ha
-            assert sum(p_b1) % 5 == sum(p_b2) % 5 == hb
+            require_eq(sum(p_a1) % 5, ha, "T04.sum(p_a1)")
+            require_eq(sum(p_a2) % 5, ha, "T04.sum(p_a2)")
+            require_eq(sum(p_b1) % 5, hb, "T04.sum(p_b1)")
+            require_eq(sum(p_b2) % 5, hb, "T04.sum(p_b2)")
             s1 = app.run_seven_steps(app.prepare_ready_state(p_a1, p_b1, Fraction(1, 5)))
             s2 = app.run_seven_steps(app.prepare_ready_state(p_a2, p_b2, Fraction(1, 5)))
+            require_true(isinstance(s1, app.CompositeState), "T04.s1_type")
+            require_true(isinstance(s2, app.CompositeState), "T04.s2_type")
             assert isinstance(s1, app.CompositeState) and isinstance(s2, app.CompositeState)
-            assert s1.to_apparatus_substate() == s2.to_apparatus_substate()
-            assert app.recover_prepared_inputs(s1) == (p_a1, p_b1)
-            assert app.recover_prepared_inputs(s2) == (p_a2, p_b2)
+            require_eq(
+                s1.to_apparatus_substate(),
+                s2.to_apparatus_substate(),
+                f"T04.fibre_substate[({ha},{hb})]",
+            )
+            require_eq(app.recover_prepared_inputs(s1), (p_a1, p_b1), "T04.recover_s1")
+            require_eq(app.recover_prepared_inputs(s2), (p_a2, p_b2), "T04.recover_s2")
 
     return "T04 PASS: 390625 paired inputs factor into 25 fibres of 15625; full recovery verified"
+
+
+def _verify_f_basis_and_bilinear_column(
+    x_basis: app.WaveTapeState, label: str, n_sites: int, z_d: Tuple[Fraction, ...], z_4: Tuple[Fraction, ...]
+) -> None:
+    """Verify F^-1(F(E))==E, F(F^-1(E))==E, E_full(F(E))==E_full(E), and polarization column == 0."""
+    fx = app.F_step(x_basis)
+    require_eq(app.F_inverse(fx), x_basis, f"{label}.F_inv_F")
+    require_eq(app.F_step(app.F_inverse(x_basis)), x_basis, f"{label}.F_F_inv")
+    require_eq(
+        app.full_classical_energy(fx),
+        app.full_classical_energy(x_basis),
+        f"{label}.E_full_diag",
+    )
+
+    # Polarized bilinear form B_Q(X_1, E) of Q(X) = 2(E_full(F(X)) - E_full(X)):
+    # B_Q(X_1, E) = u_1^T col_u(E) + v_1^T col_v(E) + A_{0,1}^T col_a(E)
+    u2 = x_basis.u
+    v2 = x_basis.v
+    a0_2 = x_basis.A0
+    w2 = fx.v
+    b_out2 = fx.B0
+    hv2 = app.apply_H(v2)
+    pb_out2 = app.apply_P(b_out2)
+    q2 = app.apply_K(
+        tuple(w2[m] - Fraction(1, 2) * hv2[m] - 2 * pb_out2[m] for m in range(n_sites))
+    )
+    half_w_minus_u = tuple(Fraction(1, 2) * (w2[m] - u2[m]) for m in range(n_sites))
+    require_eq(q2, half_w_minus_u, f"{label}.q2_identity")
+
+    j0_q2 = app.apply_J0(q2)
+    col_u = tuple(
+        -j0_q2[m] + 2 * pb_out2[m] - u2[m] + Fraction(1, 2) * hv2[m] for m in range(n_sites)
+    )
+    col_v = app.apply_H(
+        tuple(q2[m] - Fraction(1, 2) * w2[m] + Fraction(1, 2) * u2[m] for m in range(n_sites))
+    )
+    pt_q2 = app.apply_PT(q2)
+    col_a = tuple(4 * pt_q2[j] + 4 * b_out2[j] - 4 * a0_2[j] for j in range(4))
+    require_eq(col_u, z_d, f"{label}.col_u_zero")
+    require_eq(col_v, z_d, f"{label}.col_v_zero")
+    require_eq(col_a, z_4, f"{label}.col_a_zero")
 
 
 def run_t05_certificate_f_bijectivity_and_energy() -> str:
     geom = app.get_geometry()
-    # 1. Verify symmetry of H and operator blocks on all 869 basis vectors of Q^D
+    n_sites = geom.n_sites
+    require_eq(n_sites, 705, "T05.n_sites")
+    require_eq(geom.wave_tape_basis_dim, 1426, "T05.wave_tape_basis_dim")
+
+    # 1. Verify symmetry of H and operator blocks on all 705 basis vectors of Q^D
     z_d = app.zero_qd()
     z_4 = app.zero_q4()
-    for i in range(869):
+    for i in range(n_sites):
         for j, coeff in geom.h_neighbors[i]:
             rev = dict(geom.h_neighbors[j]).get(i)
-            assert rev == coeff
-
-    # 2. Verify F_inverse(F_step(e)) == e and F_step(F_inverse(e)) == e and E_full conservation
-    # across all 1754 standard basis vectors of Q^D (+) Q^D (+) (Q^4)^4
+            require_eq(rev, coeff, f"T05.H_symmetry[{i},{j}]")
+
+    # 2. Verify F_inverse(F_step(e)) == e, F_step(F_inverse(e)) == e, E_full conservation,
+    # and all 1426 polarized bilinear energy columns (certifying all 1426x1426 = 2,033,476 entries)
     basis_checked = 0
-    for i in range(869):
+    for i in range(n_sites):
         u_basis = list(z_d)
         u_basis[i] = Fraction(1, 1)
         u_tup = tuple(u_basis)
 
         # Basis in u slot
         xu = app.WaveTapeState(u=u_tup, v=z_d, A0=z_4, A1=z_4, B0=z_4, B1=z_4, k=0)
-        fxu = app.F_step(xu)
-        assert app.F_inverse(fxu) == xu
-        assert app.F_step(app.F_inverse(xu)) == xu
-        assert app.full_classical_energy(fxu) == app.full_classical_energy(xu)
+        _verify_f_basis_and_bilinear_column(xu, f"T05.u[{i}]", n_sites, z_d, z_4)
         basis_checked += 1
 
         # Basis in v slot
         xv = app.WaveTapeState(u=z_d, v=u_tup, A0=z_4, A1=z_4, B0=z_4, B1=z_4, k=1)
-        fxv = app.F_step(xv)
-        assert app.F_inverse(fxv) == xv
-        assert app.F_step(app.F_inverse(xv)) == xv
-        assert app.full_classical_energy(fxv) == app.full_classical_energy(xv)
+        _verify_f_basis_and_bilinear_column(xv, f"T05.v[{i}]", n_sites, z_d, z_4)
         basis_checked += 1
 
         # Verify K^2 - K + (1/4) P P^T = 0 on H e_i (the (v,v) quadratic energy block)
@@ -389,8 +489,12 @@
         k_hei = app.apply_K(hei)
         k2_hei = app.apply_K(k_hei)
         ppt_hei = app.apply_P(app.apply_PT(hei))
-        for m in range(869):
-            assert k2_hei[m] - k_hei[m] + Fraction(1, 4) * ppt_hei[m] == 0
+        for m in range(n_sites):
+            require_eq(
+                k2_hei[m] - k_hei[m] + Fraction(1, 4) * ppt_hei[m],
+                Fraction(0, 1),
+                f"T05.K2_minus_K[{i},{m}]",
+            )
 
     for slot in range(4):
         for j in range(4):
@@ -400,30 +504,36 @@
             xt = app.WaveTapeState(
                 u=z_d, v=z_d, A0=tapes[0], A1=tapes[1], B0=tapes[2], B1=tapes[3], k=0
             )
-            fxt = app.F_step(xt)
-            assert app.F_inverse(fxt) == xt
-            assert app.F_step(app.F_inverse(xt)) == xt
-            assert app.full_classical_energy(fxt) == app.full_classical_energy(xt)
+            _verify_f_basis_and_bilinear_column(
+                xt, f"T05.tape[slot={slot},j={j}]", n_sites, z_d, z_4
+            )
             basis_checked += 1
 
-    assert basis_checked == 1754
-
-    # 3. Verify cross bilinear terms of E_full(F(X)) - E_full(X) and R1-A witness (u=v=0, A0=e0)
+    require_eq(basis_checked, geom.wave_tape_basis_dim, "T05.basis_checked")
+    require_eq(basis_checked * basis_checked, 2033476, "T05.bilinear_entries")
+
+    # 3. Verify R1-A witness (u=v=0, A0=e0) and wave_energy difference form
     e0 = app.basis_q4(0)
     x_r1a = app.WaveTapeState(u=z_d, v=z_d, A0=e0, A1=z_4, B0=z_4, B1=z_4, k=0)
     fx_r1a = app.F_step(x_r1a)
-    assert fx_r1a.v == tuple(2 * x for x in app.apply_P(e0))
-    assert fx_r1a.B0 == z_4
-    assert app.F_inverse(fx_r1a) == x_r1a
-    assert app.wave_energy(fx_r1a.u, fx_r1a.v) == app.wave_energy_difference_form(
-        fx_r1a.u, fx_r1a.v
-    )
-
-    return f"T05 PASS: coefficient-complete F/F^-1 and E_full certificate verified on all {basis_checked} basis vectors"
+    require_eq(fx_r1a.v, tuple(2 * x for x in app.apply_P(e0)), "T05.R1A.v")
+    require_eq(fx_r1a.B0, z_4, "T05.R1A.B0")
+    require_eq(app.F_inverse(fx_r1a), x_r1a, "T05.R1A.F_inv")
+    require_eq(
+        app.wave_energy(fx_r1a.u, fx_r1a.v),
+        app.wave_energy_difference_form(fx_r1a.u, fx_r1a.v),
+        "T05.R1A.wave_energy_diff_form",
+    )
+
+    return (
+        f"T05 PASS: coefficient-complete F/F^-1 and E_full (1426x1426=2033476 bilinear entries) "
+        f"verified on all {basis_checked} basis vectors"
+    )
 
 
 def run_t06_certificate_hb_involutions_and_lbuf() -> str:
-    z_d = app.zero_qd()
+    geom = app.get_geometry()
+    n_sites = geom.n_sites
     z_4 = app.zero_q4()
     # Check polynomial identity Delta(u, v + sigma*a(r), -sigma) + Delta(u, v, sigma) == 0
     # across all 25 labels r in F_5^2 and both sigma in {-1, +1}
@@ -433,14 +543,16 @@
             a_r = app.source_field_for_receiver(r)
             norm_sq_half = Fraction(1, 2) * app.dot_vec(a_r, a_r)
             for sig in (-1, 1):
-                # Constant term in (u, v): (1/2)||a||^2 - sig^2 ||a||^2 + (1/2)||a||^2 == 0
                 const_sum = norm_sq_half - (sig * sig) * app.dot_vec(a_r, a_r) + norm_sq_half
-                assert const_sum == 0
-                # Linear coefficients in v and u: +sig a_r + (-sig) a_r == 0
-                for idx in range(869):
-                    assert sig * a_r[idx] + (-sig) * a_r[idx] == 0
-
-                # Test H_{B,A}^2 == id and H_{B,B}^2 == id on accepted, lower-refused, and upper-refused states
+                require_eq(const_sum, Fraction(0, 1), f"T06.const_sum[r={r},sig={sig}]")
+                for idx in range(n_sites):
+                    require_eq(
+                        sig * a_r[idx] + (-sig) * a_r[idx],
+                        Fraction(0, 1),
+                        f"T06.lin_coeff[r={r},idx={idx}]",
+                    )
+
+                # Test H_{B,A}^2 == id and H_{B,B}^2 == id on accepted, lower-refused, and upper-refused substates
                 for u_scale, v_scale, b_val, cap_val in [
                     (Fraction(0, 1), Fraction(0, 1), Fraction(2, 5), Fraction(4, 5)),
                     (Fraction(1, 3), Fraction(-1, 2), Fraction(0, 1), Fraction(1, 10)),
@@ -449,7 +561,11 @@
                     u_test = tuple(u_scale * x for x in app.apply_S(app.basis_q4(0)))
                     v_test = tuple(v_scale * x for x in app.apply_P(app.basis_q4(0)))
                     d_inc = app.contact_energy_increment(u_test, v_test, sig, r)
-                    assert d_inc == app.contact_energy_increment_bilinear(u_test, v_test, sig, r)
+                    require_eq(
+                        d_inc,
+                        app.contact_energy_increment_bilinear(u_test, v_test, sig, r),
+                        f"T06.d_inc_bilinear[r={r},sig={sig}]",
+                    )
                     sub = app.ApparatusSubstate(
                         X=app.WaveTapeState(
                             u=u_test, v=v_test, A0=z_4, A1=z_4, B0=z_4, B1=z_4, k=0
@@ -463,24 +579,38 @@
                     )
                     sub_a1 = app.funded_contact_A_substate(sub, r)
                     sub_a2 = app.funded_contact_A_substate(sub_a1, r)
-                    assert sub_a2 == sub
+                    require_eq(sub_a2, sub, f"T06.H_BA_involution[r={r},sig={sig}]")
                     sub_b1 = app.funded_contact_B_substate(sub)
                     sub_b2 = app.funded_contact_B_substate(sub_b1)
-                    assert sub_b2 == sub
-
-                    # Check two-sided apparatus step invertibility across all 8 phases c=0..7
+                    require_eq(sub_b2, sub, f"T06.H_BB_involution[r={r},sig={sig}]")
+
+                    # Check two-sided invertibility of the supplied-label apparatus substate
+                    # transitions T_{c,B}^{(r_A, r_B)} and S_B^{(r_A, r_B)} across c=0..7
                     for c_phase in range(8):
+                        row_fwd = app.apparatus_row_map(sub, c_phase, r, (1, 4))
+                        row_back = app.apparatus_row_map_inverse(row_fwd, c_phase, r, (1, 4))
+                        require_eq(row_back, sub, f"T06.T_c_inv_T_c[c={c_phase}]")
+                        row_inv = app.apparatus_row_map_inverse(sub, c_phase, r, (1, 4))
+                        row_fwd_inv = app.apparatus_row_map(row_inv, c_phase, r, (1, 4))
+                        require_eq(row_fwd_inv, sub, f"T06.T_c_T_c_inv[c={c_phase}]")
+
                         fwd_sub, fwd_c = app.apparatus_step(sub, c_phase, r, (1, 4))
                         back_sub, back_c = app.apparatus_step_inverse(fwd_sub, fwd_c, r, (1, 4))
-                        assert (back_sub, back_c) == (sub, c_phase)
-
-    return "T06 PASS: universal H_{B,A}^2=id, H_{B,B}^2=id, L_buf^-1, and G_B^-1 verified across all 25 labels and 8 phases"
+                        require_eq(
+                            (back_sub, back_c),
+                            (sub, c_phase),
+                            f"T06.S_B_inv_S_B[c={c_phase}]",
+                        )
+
+    return (
+        "T06 PASS: universal H_{B,A}^2=id, H_{B,B}^2=id, L_buf^-1, and supplied-label "
+        "substate S_B^{(r_A,r_B)}^-1 verified across all 25 labels and 8 phases"
+    )
 
 
 def run_t07_certificate_bilinear_work_and_mu() -> str:
     geom = app.get_geometry()
-    # Extract the 4x4 bilinear cross-work matrix Omega_{i,j} = (S e_i)^T (w_2(e_j) - (1/2) H w_1(e_j))
-    # directly from basis evolutions of F_step
+    n_sites = geom.n_sites
     z_d = app.zero_qd()
     z_4 = app.zero_q4()
     for j in range(4):
@@ -492,19 +622,29 @@
         w1 = x2.u
         w2 = x2.v
         hw1 = app.apply_H(w1)
-        diff = tuple(w2[m] - Fraction(1, 2) * hw1[m] for m in range(869))
+        diff = tuple(w2[m] - Fraction(1, 2) * hw1[m] for m in range(n_sites))
 
         # Check J_0((1/2) H K H f - f) equality and fifth-site value
         hkh_f = app.apply_H(app.apply_K(app.apply_H(f_ej)))
-        j0_term = app.apply_J0(tuple(Fraction(1, 2) * hkh_f[m] - f_ej[m] for m in range(869)))
-        assert diff == j0_term
-        assert diff[geom.y4_index] == Fraction(EXPECTED_MU_VECTOR[j], 2099520)
+        j0_term = app.apply_J0(
+            tuple(Fraction(1, 2) * hkh_f[m] - f_ej[m] for m in range(n_sites))
+        )
+        require_eq(diff, j0_term, f"T07.diff_eq_j0_term[j={j}]")
+        require_eq(
+            diff[geom.y4_index],
+            Fraction(EXPECTED_MU_VECTOR[j], 2099520),
+            f"T07.y4_val[j={j}]",
+        )
 
         for i in range(4):
             ei = app.basis_q4(i)
             g_ei = app.apply_S(ei)
             cross_ij = app.dot_vec(g_ei, diff)
-            assert cross_ij == -Fraction(EXPECTED_MU_VECTOR[j], EXPECTED_MU_DENOM)
+            require_eq(
+                cross_ij,
+                -Fraction(EXPECTED_MU_VECTOR[j], EXPECTED_MU_DENOM),
+                f"T07.Omega[{i},{j}]",
+            )
 
     return "T07 PASS: 4x4 bilinear cross-work matrix equals -1*mu^T/10497600 with mu=(145483,173653,173653,142153)"
 
@@ -516,7 +656,11 @@
             for hb in range(5):
                 st0 = app.prepare_ready_state((ha, 0, 0, 0), (hb, 0, 0, 0), cap, b_init=cap)
                 bounds = app.run_seven_steps(st0, return_boundaries=True)
-                assert isinstance(bounds, tuple) and len(bounds) == 8
+                require_true(
+                    isinstance(bounds, tuple) and len(bounds) == 8,
+                    f"T08.bounds_len[cap={cap},({ha},{hb})]",
+                )
+                assert isinstance(bounds, tuple)
                 st7 = bounds[7]
                 sig_pair = (st7.sigma_A, st7.sigma_B)
                 if sig_pair == (-1, -1):
@@ -539,15 +683,30 @@
                         EXPECTED_MU_VECTOR[k] * z_a[k] for k in range(4)
                     )
                     exp_cross = -s_b * mu_za / EXPECTED_MU_DENOM
-                    assert ea == EXPECTED_E0_ON_Z5[ha]
-                    assert delta_b == EXPECTED_E0_ON_Z5[hb] + exp_cross
-                    assert w_fin == ea + delta_b
-                    assert w_fin * 41990400 == EXPECTED_41990400_W_FINAL[(ha, hb)]
-                    assert 0 <= ea <= Fraction(2, 5)
-                    assert 0 <= delta_b <= Fraction(2, 5)
-                    assert st7.b == Fraction(4, 5) - w_fin > 0
-
-        assert (acc_acc, acc_ref, ref_acc, ref_ref) == exp_counts
+                    require_eq(ea, EXPECTED_E0_ON_Z5[ha], f"T08.E_A[({ha},{hb})]")
+                    require_eq(
+                        delta_b,
+                        EXPECTED_E0_ON_Z5[hb] + exp_cross,
+                        f"T08.Delta_B[({ha},{hb})]",
+                    )
+                    require_eq(w_fin, ea + delta_b, f"T08.W_fin_sum[({ha},{hb})]")
+                    require_eq(
+                        w_fin * 41990400,
+                        EXPECTED_41990400_W_FINAL[(ha, hb)],
+                        f"T08.41990400_W_fin[({ha},{hb})]",
+                    )
+                    require_true(0 <= ea <= Fraction(2, 5), f"T08.E_A_bounds[({ha},{hb})]")
+                    require_true(
+                        0 <= delta_b <= Fraction(2, 5), f"T08.Delta_B_bounds[({ha},{hb})]"
+                    )
+                    require_eq(st7.b, Fraction(4, 5) - w_fin, f"T08.b_final[({ha},{hb})]")
+                    require_true(st7.b > 0, f"T08.b_final_pos[({ha},{hb})]")
+
+        require_eq(
+            (acc_acc, acc_ref, ref_acc, ref_ref),
+            exp_counts,
+            f"T08.branch_counts[cap={cap}]",
+        )
 
     return "T08 PASS: all 25 source pairs and all 6 capacities match work table and branch counts"
 
@@ -566,21 +725,31 @@
     w_14 = b_14[7].W
     w_41 = b_41[7].W
     diff = w_14 - w_41
-    assert w_14 == Fraction(10352117, 20995200)
-    assert w_41 == Fraction(10323947, 20995200)
-    assert diff == Fraction(313, 233280)
+    require_eq(w_14, Fraction(10352117, 20995200), "T09.W(1,4)")
+    require_eq(w_41, Fraction(10323947, 20995200), "T09.W(4,1)")
+    require_eq(diff, Fraction(313, 233280), "T09.W(1,4)-W(4,1)")
     return f"T09 PASS: order witness W(1,4)={fmt_frac(w_14)}, W(4,1)={fmt_frac(w_41)}, W(1,4)-W(4,1)=313/233280"
 
 
 def run_t10_certificate_four_cut_operators_and_archives() -> str:
+    geom = app.get_geometry()
+    n_sites = geom.n_sites
     ops = app.get_derived_operators()
     # Verify single-source tables 12960 R0 z^(h) and 1399680 R1 z^(h)
     for h in range(5):
         zh = EXPECTED_Z5_VECTORS[h]
         r0_zh = app.mat_vec_4(ops.R0, zh)
         r1_zh = app.mat_vec_4(ops.R1, zh)
-        assert tuple(int(x * 12960) for x in r0_zh) == EXPECTED_12960_R0_Z5[h]
-        assert tuple(int(x * 1399680) for x in r1_zh) == EXPECTED_1399680_R1_Z5[h]
+        require_eq(
+            tuple(int(x * 12960) for x in r0_zh),
+            EXPECTED_12960_R0_Z5[h],
+            f"T10.12960_R0[h={h}]",
+        )
+        require_eq(
+            tuple(int(x * 1399680) for x in r1_zh),
+            EXPECTED_1399680_R1_Z5[h],
+            f"T10.1399680_R1[h={h}]",
+        )
 
     # Coefficient-complete basis check on (z_A, z_B, c0, c1) in (Q^4)^4 across all 4 branches
     z_d = app.zero_qd()
@@ -602,7 +771,7 @@
                     x_c4 = app.F_step(x_c3)
                     x_c5 = app.WaveTapeState(
                         u=x_c4.u,
-                        v=tuple(x_c4.v[m] + g_b[m] for m in range(869)),
+                        v=tuple(x_c4.v[m] + g_b[m] for m in range(n_sites)),
                         A0=x_c4.A0,
                         A1=x_c4.A1,
                         B0=x_c4.B0,
@@ -624,10 +793,10 @@
                         d3_za[i] + r1_zb[i] - Fraction(1, 2) * jp_c1[i] for i in range(4)
                     )
 
-                    assert x_c7.A0 == exp_b0
-                    assert x_c7.A1 == exp_b1
-                    assert x_c7.B1 == exp_b2
-                    assert x_c7.B0 == exp_b3
+                    require_eq(x_c7.A0, exp_b0, f"T10.b0[a={alpha_a},b={alpha_b},s={slot},j={j}]")
+                    require_eq(x_c7.A1, exp_b1, f"T10.b1[a={alpha_a},b={alpha_b},s={slot},j={j}]")
+                    require_eq(x_c7.B1, exp_b2, f"T10.b2[a={alpha_a},b={alpha_b},s={slot},j={j}]")
+                    require_eq(x_c7.B0, exp_b3, f"T10.b3[a={alpha_a},b={alpha_b},s={slot},j={j}]")
 
     # Explicit WARM witness checks for c1 = e0 on (0,0) and (0,1)
     e0 = app.basis_q4(0)
@@ -635,25 +804,33 @@
         app.prepare_ready_state((0, 0, 0, 0), (0, 0, 0, 0), Fraction(4, 5), c1=e0)
     )
     assert isinstance(st_warm_00, app.CompositeState)
-    assert st_warm_00.X.B0 == (
-        Fraction(-5, 9),
-        Fraction(-1, 108),
-        Fraction(-1, 108),
-        Fraction(-1, 108),
+    require_eq(
+        st_warm_00.X.B0,
+        (
+            Fraction(-5, 9),
+            Fraction(-1, 108),
+            Fraction(-1, 108),
+            Fraction(-1, 108),
+        ),
+        "T10.warm_00.b3",
     )
 
     st_warm_01 = app.run_seven_steps(
         app.prepare_ready_state((0, 0, 0, 0), (1, 0, 0, 0), Fraction(4, 5), c1=e0)
     )
     assert isinstance(st_warm_01, app.CompositeState)
-    assert st_warm_01.X.B0 == (
-        Fraction(-585398, 1399680),
-        Fraction(-60789, 1399680),
-        Fraction(-60789, 1399680),
-        Fraction(-61839, 1399680),
-    )
-    assert app.full_classical_energy(st_warm_01.X) == Fraction(21, 10)
-    assert st_warm_01.W == Fraction(1, 10)
+    require_eq(
+        st_warm_01.X.B0,
+        (
+            Fraction(-585398, 1399680),
+            Fraction(-60789, 1399680),
+            Fraction(-60789, 1399680),
+            Fraction(-61839, 1399680),
+        ),
+        "T10.warm_01.b3",
+    )
+    require_eq(app.full_classical_energy(st_warm_01.X), Fraction(21, 10), "T10.warm_01.E_full")
+    require_eq(st_warm_01.W, Fraction(1, 10), "T10.warm_01.W")
 
     return "T10 PASS: universal 4-cut operator certificate and c1=e0 WARM witnesses verified"
 
@@ -661,7 +838,11 @@
 def run_t11_direct_chronological_and_source_readers() -> str:
     # 1. Test API access restrictions of direct_source_reader
     sig = inspect.signature(app.direct_source_reader)
-    assert list(sig.parameters.keys()) == ["b0", "b2", "sigma_A", "sigma_B", "d"]
+    require_eq(
+        list(sig.parameters.keys()),
+        ["b0", "b2", "sigma_A", "sigma_B", "d"],
+        "T11.signature",
+    )
 
     st0 = app.prepare_ready_state((1, 0, 0, 0), (2, 0, 0, 0), Fraction(4, 5))
     bounds = app.run_seven_steps(st0, return_boundaries=True)
@@ -674,7 +855,7 @@
             app.direct_source_reader(forbidden, st7.X.B1)  # type: ignore[arg-type]
         except (TypeError, ValueError):
             raised = True
-        assert raised
+        require_true(raised, f"T11.reject_forbidden[{type(forbidden).__name__}]")
 
     # 2. Verify chronological cut reader across c=0..7, including continued reading of (b0,b1)
     b0_val = st7.X.A0
@@ -684,24 +865,32 @@
     for c_idx in range(8):
         entries = app.direct_chronological_cut_reader(bounds[c_idx])
         if c_idx in (0, 1, 2):
-            assert all(e.status == "UNWRITTEN" for e in entries)
+            require_true(all(e.status == "UNWRITTEN" for e in entries), f"T11.c{c_idx}.unwritten")
         elif c_idx == 3:
-            assert entries[0].status == "PRESENT" and entries[0].vector == b0_val
-            assert all(e.status == "UNWRITTEN" for e in entries[1:])
+            require_eq((entries[0].status, entries[0].vector), ("PRESENT", b0_val), "T11.c3.cut0")
+            require_true(all(e.status == "UNWRITTEN" for e in entries[1:]), "T11.c3.rest")
         elif c_idx in (4, 5):
-            assert entries[0].vector == b0_val and entries[0].slot_name == "B1"
-            assert entries[1].vector == b1_val and entries[1].slot_name == "B0"
-            assert all(e.status == "UNWRITTEN" for e in entries[2:])
+            require_eq(
+                (entries[0].vector, entries[0].slot_name),
+                (b0_val, "B1"),
+                f"T11.c{c_idx}.cut0",
+            )
+            require_eq(
+                (entries[1].vector, entries[1].slot_name),
+                (b1_val, "B0"),
+                f"T11.c{c_idx}.cut1",
+            )
+            require_true(all(e.status == "UNWRITTEN" for e in entries[2:]), f"T11.c{c_idx}.rest")
         elif c_idx == 6:
-            assert entries[0].vector == b0_val and entries[0].slot_name == "A1"
-            assert entries[1].vector == b1_val and entries[1].slot_name == "B1"
-            assert entries[2].vector == b2_val and entries[2].slot_name == "B0"
-            assert entries[3].status == "UNWRITTEN"
+            require_eq((entries[0].vector, entries[0].slot_name), (b0_val, "A1"), "T11.c6.cut0")
+            require_eq((entries[1].vector, entries[1].slot_name), (b1_val, "B1"), "T11.c6.cut1")
+            require_eq((entries[2].vector, entries[2].slot_name), (b2_val, "B0"), "T11.c6.cut2")
+            require_eq(entries[3].status, "UNWRITTEN", "T11.c6.cut3")
         else:
-            assert entries[0].vector == b0_val and entries[0].slot_name == "A0"
-            assert entries[1].vector == b1_val and entries[1].slot_name == "A1"
-            assert entries[2].vector == b2_val and entries[2].slot_name == "B1"
-            assert entries[3].vector == b3_val and entries[3].slot_name == "B0"
+            require_eq((entries[0].vector, entries[0].slot_name), (b0_val, "A0"), "T11.c7.cut0")
+            require_eq((entries[1].vector, entries[1].slot_name), (b1_val, "A1"), "T11.c7.cut1")
+            require_eq((entries[2].vector, entries[2].slot_name), (b2_val, "B1"), "T11.c7.cut2")
+            require_eq((entries[3].vector, entries[3].slot_name), (b3_val, "B0"), "T11.c7.cut3")
 
     # 3. Verify archive-independent source decoding across all 25 pairs and non-zero old archives
     archives = [
@@ -727,9 +916,9 @@
                 assert isinstance(s_end, app.CompositeState)
                 view = app.extract_direct_port_readout(s_end, include_d=True)
                 dec = app.direct_source_reader(view)
-                assert dec["z_A"] == EXPECTED_Z5_VECTORS[ha]
-                assert dec["z_B"] == EXPECTED_Z5_VECTORS[hb]
-                assert dec["alpha_A"] == 1 and dec["alpha_B"] == 1
+                require_eq(dec["z_A"], EXPECTED_Z5_VECTORS[ha], f"T11.z_A[({ha},{hb})]")
+                require_eq(dec["z_B"], EXPECTED_Z5_VECTORS[hb], f"T11.z_B[({ha},{hb})]")
+                require_eq((dec["alpha_A"], dec["alpha_B"]), (1, 1), f"T11.alpha[({ha},{hb})]")
 
     return "T11 PASS: direct_chronological_cut_reader, direct_source_reader, and API restrictions verified"
 
@@ -740,8 +929,8 @@
         app.prepare_ready_state((3, 0, 0, 0), (3, 0, 0, 0), Fraction(2, 5))
     )
     assert isinstance(st_ref_25, app.CompositeState)
-    assert (st_ref_25.sigma_A, st_ref_25.sigma_B) == (-1, 1)
-    assert st_ref_25.W == Fraction(2, 5) and st_ref_25.b == Fraction(0, 1)
+    require_eq((st_ref_25.sigma_A, st_ref_25.sigma_B), (-1, 1), "T12.ready_ref_25.sigma")
+    require_eq((st_ref_25.W, st_ref_25.b), (Fraction(2, 5), Fraction(0, 1)), "T12.ready_ref_25.Wb")
 
     # 2. Occupied-tape warm lower-bound refusal: A_init = (0, e0), (0, 1), B = b_init = 4/5
     z_d = app.zero_qd()
@@ -767,10 +956,10 @@
     assert isinstance(warm_low_bounds, tuple)
     c4_low = warm_low_bounds[4]
     delta_b_low = app.contact_energy_increment(c4_low.X.u, c4_low.X.v, c4_low.sigma_B, c4_low.d)
-    assert delta_b_low == Fraction(9, 10)
-    assert c4_low.b - delta_b_low == Fraction(-1, 10) < 0
-    assert (warm_low_bounds[7].sigma_A, warm_low_bounds[7].sigma_B) == (-1, 1)
-    assert warm_low_bounds[7].W == Fraction(0, 1) and warm_low_bounds[7].b == cap
+    require_eq(delta_b_low, Fraction(9, 10), "T12.warm_low.delta_b")
+    require_eq(c4_low.b - delta_b_low, Fraction(-1, 10), "T12.warm_low.b_cand")
+    require_eq((warm_low_bounds[7].sigma_A, warm_low_bounds[7].sigma_B), (-1, 1), "T12.warm_low.sig")
+    require_eq((warm_low_bounds[7].W, warm_low_bounds[7].b), (Fraction(0, 1), cap), "T12.warm_low.Wb")
 
     # 3. Occupied-tape warm upper-bound refusal (negative work): A_init = (0, -e0), b_init = B = 4/5
     warm_high_init = app.CompositeState(
@@ -792,10 +981,18 @@
     delta_b_high = app.contact_energy_increment(
         c4_high.X.u, c4_high.X.v, c4_high.sigma_B, c4_high.d
     )
-    assert delta_b_high == Fraction(-7, 10) < 0
-    assert c4_high.b - delta_b_high == Fraction(3, 2) > cap
-    assert (warm_high_bounds[7].sigma_A, warm_high_bounds[7].sigma_B) == (-1, 1)
-    assert warm_high_bounds[7].W == Fraction(0, 1) and warm_high_bounds[7].b == cap
+    require_eq(delta_b_high, Fraction(-7, 10), "T12.warm_high.delta_b")
+    require_eq(c4_high.b - delta_b_high, Fraction(3, 2), "T12.warm_high.b_cand")
+    require_eq(
+        (warm_high_bounds[7].sigma_A, warm_high_bounds[7].sigma_B),
+        (-1, 1),
+        "T12.warm_high.sig",
+    )
+    require_eq(
+        (warm_high_bounds[7].W, warm_high_bounds[7].b),
+        (Fraction(0, 1), cap),
+        "T12.warm_high.Wb",
+    )
 
     # 4. Companion accepted negative-work trajectory when b_init = 0, B = 4/5
     warm_neg_acc_init = app.CompositeState(
@@ -813,9 +1010,12 @@
     )
     warm_neg_acc_end = app.run_seven_steps(warm_neg_acc_init)
     assert isinstance(warm_neg_acc_end, app.CompositeState)
-    assert (warm_neg_acc_end.sigma_A, warm_neg_acc_end.sigma_B) == (-1, -1)
-    assert warm_neg_acc_end.W == Fraction(-7, 10)
-    assert warm_neg_acc_end.b == Fraction(7, 10)
+    require_eq((warm_neg_acc_end.sigma_A, warm_neg_acc_end.sigma_B), (-1, -1), "T12.neg_acc.sig")
+    require_eq(
+        (warm_neg_acc_end.W, warm_neg_acc_end.b),
+        (Fraction(-7, 10), Fraction(7, 10)),
+        "T12.neg_acc.Wb",
+    )
 
     return "T12 PASS: lower/upper store guard refusals and negative work (-7/10) verified"
 
@@ -833,27 +1033,25 @@
 
     # Check Pi_class = (X, W, b) collapses all 4 pairs
     pi_class_set = {(s.X, s.W, s.b) for s in endpoints.values()}
-    assert len(pi_class_set) == 1
+    require_eq(len(pi_class_set), 1, "T13.pi_class_collapse")
 
     # Check Pi_{class+d} = (X, W, b, d) collapses (0,0) with (3,0) and (0,3) with (3,3)
-    assert (endpoints[(0, 0)].X, endpoints[(0, 0)].W, endpoints[(0, 0)].b, endpoints[(0, 0)].d) == (
-        endpoints[(3, 0)].X,
-        endpoints[(3, 0)].W,
-        endpoints[(3, 0)].b,
-        endpoints[(3, 0)].d,
-    )
-    assert (endpoints[(0, 3)].X, endpoints[(0, 3)].W, endpoints[(0, 3)].b, endpoints[(0, 3)].d) == (
-        endpoints[(3, 3)].X,
-        endpoints[(3, 3)].W,
-        endpoints[(3, 3)].b,
-        endpoints[(3, 3)].d,
+    require_eq(
+        (endpoints[(0, 0)].X, endpoints[(0, 0)].W, endpoints[(0, 0)].b, endpoints[(0, 0)].d),
+        (endpoints[(3, 0)].X, endpoints[(3, 0)].W, endpoints[(3, 0)].b, endpoints[(3, 0)].d),
+        "T13.pi_class_d_(0,0)_(3,0)",
+    )
+    require_eq(
+        (endpoints[(0, 3)].X, endpoints[(0, 3)].W, endpoints[(0, 3)].b, endpoints[(0, 3)].d),
+        (endpoints[(3, 3)].X, endpoints[(3, 3)].W, endpoints[(3, 3)].b, endpoints[(3, 3)].d),
+        "T13.pi_class_d_(0,3)_(3,3)",
     )
 
     # Check (sigma_A, sigma_B) separates all 4
-    assert (endpoints[(0, 0)].sigma_A, endpoints[(0, 0)].sigma_B) == (-1, -1)
-    assert (endpoints[(0, 3)].sigma_A, endpoints[(0, 3)].sigma_B) == (-1, 1)
-    assert (endpoints[(3, 0)].sigma_A, endpoints[(3, 0)].sigma_B) == (1, -1)
-    assert (endpoints[(3, 3)].sigma_A, endpoints[(3, 3)].sigma_B) == (1, 1)
+    require_eq((endpoints[(0, 0)].sigma_A, endpoints[(0, 0)].sigma_B), (-1, -1), "T13.sig_(0,0)")
+    require_eq((endpoints[(0, 3)].sigma_A, endpoints[(0, 3)].sigma_B), (-1, 1), "T13.sig_(0,3)")
+    require_eq((endpoints[(3, 0)].sigma_A, endpoints[(3, 0)].sigma_B), (1, -1), "T13.sig_(3,0)")
+    require_eq((endpoints[(3, 3)].sigma_A, endpoints[(3, 3)].sigma_B), (1, 1), "T13.sig_(3,3)")
 
     # 2. Clarification (ii): on the ready family across all capacities and all 25 pairs,
     # second acceptance alpha_B IS uniquely readable from (d, b0, b2) without sigma_B!
@@ -867,11 +1065,19 @@
                 view_no_sigb = app.extract_direct_port_readout(
                     st, include_d=True, include_sigma_B=False
                 )
-                assert view_no_sigb.sigma_B is None
+                require_eq(view_no_sigb.sigma_B, None, "T13.sigma_B_omitted")
                 dec = app.direct_source_reader(view_no_sigb)
                 true_alpha_b = (1 - st.sigma_B) // 2
-                assert dec["alpha_B_from_d_b0_b2"] == true_alpha_b
-                assert dec["alpha_B"] == true_alpha_b
+                require_eq(
+                    dec["alpha_B_from_d_b0_b2"],
+                    true_alpha_b,
+                    f"T13.alpha_B_from_d[cap={c_val},({ha},{hb})]",
+                )
+                require_eq(
+                    dec["alpha_B"],
+                    true_alpha_b,
+                    f"T13.alpha_B[cap={c_val},({ha},{hb})]",
+                )
 
     return "T13 PASS: accepted-zero vs refusal and Clarification (ii) (alpha_B from (d,b0,b2)) verified"
 
@@ -888,21 +1094,33 @@
                     (ha, 0, 0, 0), (hb, 0, 0, 0), cap, b_init=cap, c0=c0_vec, c1=c1_vec
                 )
                 bounds8 = app.run_eight_steps(st0, return_boundaries=True)
-                assert isinstance(bounds8, tuple) and len(bounds8) == 9
+                require_true(
+                    isinstance(bounds8, tuple) and len(bounds8) == 9,
+                    "T14.bounds8_len",
+                )
+                assert isinstance(bounds8, tuple)
                 for step_idx, b_st in enumerate(bounds8):
                     efull = app.full_classical_energy(b_st.X)
-                    assert efull - b_st.W == init_tape_e
-                    assert efull + b_st.b == init_tape_e + cap
-                    assert b_st.W + b_st.b == cap
+                    require_eq(efull - b_st.W, init_tape_e, f"T14.E_minus_W[step={step_idx}]")
+                    require_eq(
+                        efull + b_st.b,
+                        init_tape_e + cap,
+                        f"T14.E_plus_b[step={step_idx}]",
+                    )
+                    require_eq(b_st.W + b_st.b, cap, f"T14.W_plus_b[step={step_idx}]")
                     if step_idx < 8:
-                        assert b_st.c == step_idx
+                        require_eq(b_st.c, step_idx, f"T14.c[step={step_idx}]")
 
                 st7 = bounds8[7]
                 st8 = bounds8[8]
-                assert st7.c == 7 and st7.n == 5
-                assert st8.c == 0 and st8.n == 5
-                assert st8.to_apparatus_substate() == st7.to_apparatus_substate()
-                assert (st8.x_A, st8.x_B) == (st7.x_A, st7.x_B)
+                require_eq((st7.c, st7.n), (7, 5), "T14.st7_clock")
+                require_eq((st8.c, st8.n), (0, 5), "T14.st8_clock")
+                require_eq(
+                    st8.to_apparatus_substate(),
+                    st7.to_apparatus_substate(),
+                    "T14.rollover_substate",
+                )
+                require_eq((st8.x_A, st8.x_B), (st7.x_A, st7.x_B), "T14.rollover_heads")
 
     return "T14 PASS: 7-step completion (c=7,n=5), 8th-step rollover (c=0,n=5), and single-counted E_full invariants verified"
 
@@ -922,10 +1140,11 @@
                 )
                 assert isinstance(st7, app.CompositeState)
                 rec = app.recognize_ready_image(st7, c0=c0_vec, c1=c1_vec, b_init=cap)
-                assert rec["valid"] is True
-                assert app.recover_prepared_inputs(st7, c0=c0_vec, c1=c1_vec, b_init=cap) == (
-                    p_a,
-                    p_b,
+                require_eq(rec["valid"], True, f"T15.valid[cap={cap},({ha},{hb})]")
+                require_eq(
+                    app.recover_prepared_inputs(st7, c0=c0_vec, c1=c1_vec, b_init=cap),
+                    (p_a, p_b),
+                    f"T15.recover[cap={cap},({ha},{hb})]",
                 )
 
     return "T15 PASS: ready-image left inverse and recognizer verified across all 4 branches and non-zero archives"
@@ -973,9 +1192,15 @@
     om01 = 2 * (obs[(4, 1)]["Delta_B"] - r10["E_A"])  # type: ignore[operator]
     om11 = obs[(4, 4)]["Delta_B"] - r40["E_A"]  # type: ignore[operator]
 
-    assert (g00, g11, g01) == (Fraction(4, 5), Fraction(4, 5), Fraction(-1, 5))
-    assert om00 == om10 == Fraction(-145483, 10497600)
-    assert om01 == om11 == Fraction(-173653, 10497600)
+    require_eq(
+        (g00, g11, g01),
+        (Fraction(4, 5), Fraction(4, 5), Fraction(-1, 5)),
+        "T16.calibrated_G",
+    )
+    require_eq(om00, Fraction(-145483, 10497600), "T16.om00")
+    require_eq(om10, Fraction(-145483, 10497600), "T16.om10")
+    require_eq(om01, Fraction(-173653, 10497600), "T16.om01")
+    require_eq(om11, Fraction(-173653, 10497600), "T16.om11")
 
     # Verify zero-error out-of-sample prediction on all 25 pairs (18 uncalibrated)
     for ha in range(5):
@@ -1002,12 +1227,12 @@
                 zb0 * (om00 * za0 + om01 * za1) + zb1 * (om10 * za0 + om11 * za1)
             )
             pred_db = pred_eb + pred_cross
-            assert pred_b0 == obs[(ha, hb)]["b0"]
-            assert pred_b1 == obs[(ha, hb)]["b1"]
-            assert pred_b2 == obs[(ha, hb)]["b2"]
-            assert pred_b3 == obs[(ha, hb)]["b3"]
-            assert pred_ea == obs[(ha, hb)]["E_A"]
-            assert pred_db == obs[(ha, hb)]["Delta_B"]
+            require_eq(pred_b0, obs[(ha, hb)]["b0"], f"T16.pred_b0[({ha},{hb})]")
+            require_eq(pred_b1, obs[(ha, hb)]["b1"], f"T16.pred_b1[({ha},{hb})]")
+            require_eq(pred_b2, obs[(ha, hb)]["b2"], f"T16.pred_b2[({ha},{hb})]")
+            require_eq(pred_b3, obs[(ha, hb)]["b3"], f"T16.pred_b3[({ha},{hb})]")
+            require_eq(pred_ea, obs[(ha, hb)]["E_A"], f"T16.pred_ea[({ha},{hb})]")
+            require_eq(pred_db, obs[(ha, hb)]["Delta_B"], f"T16.pred_db[({ha},{hb})]")
 
     # Clarification (i): verify q3(z0, z1) = z0 * z1 * (2*z0 - 1) has q3(z^(3)) = 1/2,
     # so b2 + q3(z_A) u shifts b2 at h_A = 3 by u/2 (not u)
@@ -1015,12 +1240,12 @@
         return z[0] * z[1] * (2 * z[0] - 1)
 
     for h in (0, 1, 2, 4):
-        assert q3_poly(EXPECTED_Z5_VECTORS[h]) == Fraction(0, 1)
-    assert q3_poly(EXPECTED_Z5_VECTORS[3]) == Fraction(1, 2)
+        require_eq(q3_poly(EXPECTED_Z5_VECTORS[h]), Fraction(0, 1), f"T16.q3[h={h}]")
+    require_eq(q3_poly(EXPECTED_Z5_VECTORS[3]), Fraction(1, 2), "T16.q3[h=3]")
     u_vec = (Fraction(2, 3), Fraction(-4, 5), Fraction(1, 7), Fraction(3, 11))
     shift_at_h3 = tuple(q3_poly(EXPECTED_Z5_VECTORS[3]) * x for x in u_vec)
-    assert shift_at_h3 == tuple(Fraction(1, 2) * x for x in u_vec)
-    assert shift_at_h3 != u_vec
+    require_eq(shift_at_h3, tuple(Fraction(1, 2) * x for x in u_vec), "T16.shift_at_h3")
+    require_true(shift_at_h3 != u_vec, "T16.shift_neq_u")
 
     return "T16 PASS: 7-run/5-run Pi_2 calibration predicts all 25 pairs; Clarification (i) q3(z^(3))=1/2 shift u/2 verified"
 
@@ -1039,8 +1264,8 @@
                 c_cur = 0
                 for _ in range(7):
                     sub, c_cur = app.apparatus_step(sub, c_cur, ra, rb)
-                assert c_cur == 7
-                assert sub == st7.to_apparatus_substate()
+                require_eq(c_cur, 7, "T17.c_cur")
+                require_eq(sub, st7.to_apparatus_substate(), f"T17.matched[cap={cap},({ha},{hb})]")
 
     # 2. Five restricted comparator separations:
     # (a) M_single on (0,1) at B = 4/5
@@ -1048,7 +1273,8 @@
         app.prepare_ready_state((0, 0, 0, 0), (1, 0, 0, 0), Fraction(4, 5))
     )
     assert isinstance(st_01, app.CompositeState)
-    assert st_01.X.B1 != app.zero_q4() and st_01.W == Fraction(1, 10) and st_01.sigma_B == -1
+    require_true(st_01.X.B1 != app.zero_q4(), "T17.M_single.B1_nonzero")
+    require_eq((st_01.W, st_01.sigma_B), (Fraction(1, 10), -1), "T17.M_single.W_sigB")
 
     # (b) M_cold on (4,4) at B* = 8224427/10497600
     b_star = Fraction(8224427, 10497600)
@@ -1056,19 +1282,25 @@
         app.prepare_ready_state((4, 0, 0, 0), (4, 0, 0, 0), b_star, b_init=b_star)
     )
     assert isinstance(st_44, app.CompositeState)
-    assert st_44.sigma_B == -1 and st_44.b == Fraction(0, 1)
-    assert b_star - Fraction(2, 5) - Fraction(2, 5) == Fraction(-173653, 10497600) < 0
+    require_eq((st_44.sigma_B, st_44.b), (-1, Fraction(0, 1)), "T17.M_cold.st_44")
+    require_eq(
+        b_star - Fraction(2, 5) - Fraction(2, 5),
+        Fraction(-173653, 10497600),
+        "T17.M_cold.deficit",
+    )
 
     # (c) M_{2-slot} on (1,0) at B = 4/5 retains A_final = (b0, b1) != (0,0)
     st_10 = app.run_seven_steps(
         app.prepare_ready_state((1, 0, 0, 0), (0, 0, 0, 0), Fraction(4, 5))
     )
     assert isinstance(st_10, app.CompositeState)
-    assert st_10.X.A0 != app.zero_q4() and st_10.X.A1 != app.zero_q4()
+    require_true(
+        st_10.X.A0 != app.zero_q4() and st_10.X.A1 != app.zero_q4(),
+        "T17.M_2slot.A_nonzero",
+    )
 
     # (d) M_{1sigma} direct un-reset shared-sigma on (0,1) at B = 4/5 gives -R0 z^(1) != +R0 z^(1)
-    assert st_01.X.B1 == tuple(-x for x in tuple(-y for y in st_01.X.B1))
-    assert st_01.X.B1 != tuple(-x for x in st_01.X.B1)
+    require_true(st_01.X.B1 != tuple(-x for x in st_01.X.B1), "T17.M_1sigma.sign_sep")
 
     return "T17 PASS: matched classical comparator agreement and 5 restricted-comparator separations verified"
 
@@ -1079,14 +1311,18 @@
         app.prepare_ready_state((0, 0, 0, 0), (1, 0, 0, 0), cap, b_init=cap)
     )
     assert isinstance(valid_st, app.CompositeState)
-    assert app.recognize_ready_image(valid_st, c0=app.zero_q4(), c1=app.zero_q4(), b_init=cap)[
-        "valid"
-    ]
+    require_eq(
+        app.recognize_ready_image(valid_st, c0=app.zero_q4(), c1=app.zero_q4(), b_init=cap)[
+            "valid"
+        ],
+        True,
+        "T18.valid_baseline",
+    )
 
     # X01: Selector piston-sum mismatch (x_{5,A} = g_3(1,0,0,0,0,1) has rec=(1,0)=C3(0) and
     # inverse word g1 g1 g3 x_{5,A} = (1,0,0,0,0,1) has rec=(0,1), but piston sum 1 != 0)
     bad_x5a = app.apply_generator(3, (1, 0, 0, 0, 0, 1))
-    assert app.receiver_of(bad_x5a) == (1, 0)
+    require_eq(app.receiver_of(bad_x5a), (1, 0), "T18.X01.rec")
     st_x01 = app.CompositeState(
         n=5,
         x_A=bad_x5a,
@@ -1101,8 +1337,12 @@
         c=7,
     )
     res_x01 = app.recognize_ready_image(st_x01)
-    assert res_x01["valid"] is False
-    assert res_x01["failed_test"] == "test2_piston_sum_selector_consistency"
+    require_eq(res_x01["valid"], False, "T18.X01.valid")
+    require_eq(
+        res_x01["failed_test"],
+        "test2_piston_sum_selector_consistency",
+        "T18.X01.failed_test",
+    )
 
     # X02: Invalid C3 receiver at n=5
     st_x02 = app.CompositeState(
@@ -1119,7 +1359,7 @@
         c=7,
     )
     res_x02 = app.recognize_ready_image(st_x02)
-    assert res_x02["valid"] is False and res_x02["failed_test"] == "test1_c3_receiver"
+    require_eq((res_x02["valid"], res_x02["failed_test"]), (False, "test1_c3_receiver"), "T18.X02")
 
     # X03: Invalid clock n, c, or k
     st_x03_n = app.CompositeState(
@@ -1157,9 +1397,21 @@
         d=valid_st.d,
         c=7,
     )
-    assert app.recognize_ready_image(st_x03_n)["failed_test"] == "test1_clock_n5_c7"
-    assert app.recognize_ready_image(st_x03_c)["failed_test"] == "test1_clock_n5_c7"
-    assert app.recognize_ready_image(st_x03_k)["failed_test"] == "test4_initial_k_zero"
+    require_eq(
+        app.recognize_ready_image(st_x03_n)["failed_test"],
+        "test1_clock_n5_c7",
+        "T18.X03.n",
+    )
+    require_eq(
+        app.recognize_ready_image(st_x03_c)["failed_test"],
+        "test1_clock_n5_c7",
+        "T18.X03.c",
+    )
+    require_eq(
+        app.recognize_ready_image(st_x03_k)["failed_test"],
+        "test4_initial_k_zero",
+        "T18.X03.k",
+    )
 
     # X04: Invalid delayed label d
     st_x04 = app.CompositeState(
@@ -1175,7 +1427,11 @@
         d=(0, 4),
         c=7,
     )
-    assert app.recognize_ready_image(st_x04)["failed_test"] == "test3_delayed_buffer_d"
+    require_eq(
+        app.recognize_ready_image(st_x04)["failed_test"],
+        "test3_delayed_buffer_d",
+        "T18.X04",
+    )
 
     # X05: Invalid direction signs sigma
     st_x05 = app.CompositeState(
@@ -1191,7 +1447,11 @@
         d=valid_st.d,
         c=7,
     )
-    assert app.recognize_ready_image(st_x05)["failed_test"] == "test4_initial_sigma_plus1"
+    require_eq(
+        app.recognize_ready_image(st_x05)["failed_test"],
+        "test4_initial_sigma_plus1",
+        "T18.X05",
+    )
 
     # X06: Invalid store b
     st_x06 = app.CompositeState(
@@ -1207,9 +1467,10 @@
         d=valid_st.d,
         c=7,
     )
-    assert (
-        app.recognize_ready_image(st_x06, b_init=cap)["failed_test"]
-        == "test4_initial_store_b"
+    require_eq(
+        app.recognize_ready_image(st_x06, b_init=cap)["failed_test"],
+        "test4_initial_store_b",
+        "T18.X06",
     )
 
     # X07: Invalid work W
@@ -1226,7 +1487,11 @@
         d=valid_st.d,
         c=7,
     )
-    assert app.recognize_ready_image(st_x07)["failed_test"] == "test4_initial_W_zero"
+    require_eq(
+        app.recognize_ready_image(st_x07)["failed_test"],
+        "test4_initial_W_zero",
+        "T18.X07",
+    )
 
     # X08: Invalid tapes A or B
     st_x08 = app.CompositeState(
@@ -1250,7 +1515,7 @@
         d=valid_st.d,
         c=7,
     )
-    assert app.recognize_ready_image(st_x08)["valid"] is False
+    require_eq(app.recognize_ready_image(st_x08)["valid"], False, "T18.X08")
 
     # X09: Invalid wave u or v
     bad_u = list(valid_st.X.u)
@@ -1276,9 +1541,13 @@
         d=valid_st.d,
         c=7,
     )
-    assert app.recognize_ready_image(st_x09)["failed_test"] == "test4_initial_wave_zero"
-
-    # X10: Malformed carrier types (bool, float, out-of-range residues, invalid signs/clocks/stores)
+    require_eq(
+        app.recognize_ready_image(st_x09)["failed_test"],
+        "test4_initial_wave_zero",
+        "T18.X09",
+    )
+
+    # X10: Malformed carrier types (bool, float, out-of-range residues, wrong dimension 869 vs 705)
     malformed_calls = [
         lambda: app.prepare_ready_state((True, 0, 0, 0), (0, 0, 0, 0), cap),  # type: ignore[arg-type]
         lambda: app.prepare_ready_state((0, 0, 0, 0), (0, 0, 0, 0), 0.8),  # type: ignore[arg-type]
@@ -1292,6 +1561,15 @@
             (0, 0, 0, 0), (0, 0, 0, 0), cap, b_init=Fraction(-1, 10)
         ),
         lambda: app.native_tick(-1, (0, 0, 0, 0, 0, 1), (0, 0, 0, 0, 0, 1)),
+        lambda: app.WaveTapeState(
+            u=(Fraction(0, 1),) * 869,
+            v=valid_st.X.v,
+            A0=valid_st.X.A0,
+            A1=valid_st.X.A1,
+            B0=valid_st.X.B0,
+            B1=valid_st.X.B1,
+            k=0,
+        ),
         lambda: app.CompositeState(
             n=0,
             x_A=(0, 0, 0, 0, 0, 1),
@@ -1319,13 +1597,21 @@
             c=8,
         ),
     ]
-    for fn in malformed_calls:
+    for idx, fn in enumerate(malformed_calls):
         caught = False
+        err_msg = ""
         try:
             fn()
-        except (TypeError, ValueError):
+        except (TypeError, ValueError) as exc:
             caught = True
-        assert caught
+            err_msg = str(exc)
+        require_true(caught, f"T18.X10[{idx}]")
+        require_true(
+            "expected" in err_msg and "actual" in err_msg,
+            f"T18.X10_msg_expected_actual[{idx}]",
+            expected="expected/actual in error message",
+            actual=err_msg,
+        )
 
     return "T18 PASS: all 10 adversarial invalid-endpoint and malformed-carrier tests (X01-X10) rejected"
 
@@ -1399,6 +1685,27 @@
         ("WITNESS_5_WARM_LOWER_REFUSAL_A1_E0_PAIR_01_B_4_5", w5_warm_low_ref),  # type: ignore[list-item]
         ("WITNESS_6_WARM_UPPER_REFUSAL_NEG_WORK_A1_NEG_E0_PAIR_01_B_4_5", w6_warm_high_ref),  # type: ignore[list-item]
     ]
+
+
+def print_witness_report(witnesses: Sequence[Tuple[str, Tuple[app.CompositeState, ...]]]) -> None:
+    for name, bounds in witnesses:
+        print(f"[{name}]")
+        for st in bounds:
+            print(format_boundary_line(st))
+    w1_c7 = witnesses[0][1][7]
+    w2_c7 = witnesses[1][1][7]
+    w3_c7 = witnesses[2][1][7]
+    w4_c7 = witnesses[3][1][7]
+    w5_c7 = witnesses[4][1][7]
+    w6_c7 = witnesses[5][1][7]
+    diff_14_41 = w1_c7.W - w2_c7.W
+    print(
+        f"WITNESS_SUMMARY order_W14={fmt_frac(w1_c7.W)} order_W41={fmt_frac(w2_c7.W)} "
+        f"order_diff={fmt_frac(diff_14_41)} dirty_c1_e0_B0={fmt_vec4(w3_c7.X.B0)} "
+        f"ready_low_ref_sig=({w4_c7.sigma_A:+d},{w4_c7.sigma_B:+d}) "
+        f"warm_low_ref_sig=({w5_c7.sigma_A:+d},{w5_c7.sigma_B:+d}) "
+        f"warm_high_ref_sig=({w6_c7.sigma_A:+d},{w6_c7.sigma_B:+d})"
+    )
 
 
 def run_full_audit() -> None:
@@ -1422,20 +1729,18 @@
         run_t17_comparator_indistinguishability_and_separations,
         run_t18_invalid_endpoint_and_type_rejection_suite,
     ]
-    print("C-FUNDED-TWO-USE-EXECUTABLE-N AUDIT START")
+    print("C-FUNDED-TWO-USE-EXECUTABLE-2-N AUDIT START")
     for fn in tests:
         msg = fn()
         print(msg)
 
     print("WITNESS_BOUNDARY_STATES_BEGIN")
-    for name, bounds in build_witness_trajectories():
-        print(f"[{name}]")
-        for st in bounds:
-            print(format_boundary_line(st))
+    witnesses = build_witness_trajectories()
+    print_witness_report(witnesses)
     print("WITNESS_BOUNDARY_STATES_END")
     print(
-        "C-FUNDED-TWO-USE-EXECUTABLE-N AUDIT PASS: tests=18/18 invalid_endpoints=10/10 "
-        "order_diff=313/233280 max_work=8224427/10497600 status=ALL_PASS"
+        "C-FUNDED-TWO-USE-EXECUTABLE-2-N AUDIT PASS: tests=18/18 invalid_endpoints=10/10 "
+        "domain_sites=705 basis_dim=1426 order_diff=313/233280 max_work=8224427/10497600 status=ALL_PASS"
     )
 
 
@@ -1444,14 +1749,13 @@
         run_full_audit()
         return 0
     if len(argv) == 2 and argv[1] == "--compare":
-        count, digest = app.compute_comparison_digest()
-        print(f"TWOUSE-COMPARE-v1 records={count} sha256={digest}")
+        domain_sha, count, digest = app.compute_comparison_digest()
+        print(
+            f"TWOUSE-COMPARE-v2 domain_sha256={domain_sha} records={count} sha256={digest}"
+        )
         return 0
     if len(argv) == 2 and argv[1] == "--witnesses":
-        for name, bounds in build_witness_trajectories():
-            print(f"[{name}]")
-            for st in bounds:
-                print(format_boundary_line(st))
+        print_witness_report(build_witness_trajectories())
         return 0
     sys.stderr.write(f"Usage: {argv[0]} [--compare | --witnesses]\n")
     return 2
```
