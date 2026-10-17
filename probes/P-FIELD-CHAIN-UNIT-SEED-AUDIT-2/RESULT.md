# Result: Independent Audit of Native Unit-Seed Complete Classification (`P-FIELD-CHAIN-UNIT-SEED-AUDIT-2`)

- **Probe ID:** `P-FIELD-CHAIN-UNIT-SEED-AUDIT-2`
- **Program Issue:** `#1548` (Lane `RB` — Independent Review of Lane `B`)
- **Claim Issue:** `#1565` (successor to abandoned `P-FIELD-CHAIN-UNIT-SEED-AUDIT-1` in `#1561` / PR `#1564`)
- **Canonical Authority Pin:** `Public Canon v102` (`main` commit `a632c6a162dc87e60104d7a478e7650a6d5c4a1b`, content commit `b04e22dd3ed8e4240cff347364f24670d4183a4d`, `canon/CANON.md` SHA-256 `c0657380438c965f9556b5b298a34a5e799c48a68ce66e9fe51786ce2413d7d1`)
- **Specification Pin Commit:** `5838eb457cf2ec966682d97f4652259a5d3d6291`
- **First Formal Run Commit:** `ca4077448fa347ac4d6ff42eb41922de558c9f02`
- **Status:** `COMPLETED` (`candidate-T` for analytical completeness, injectivity, $A_f$-fixed missing-residue subgroup, and coset-minimum theorems; `candidate-C` for deterministic two-architecture reproduction)
- **Review Verdict on Author Lane `B`:**
  - `P-FIELD-CHAIN-UNIT-SEED-1` (Issue `#1549`, PR `#1552`, pin `066ef45911f6215f7574daba80fd53616ee1c66d`, head `1844322bbb1f0b9f08ceaa9b9081b078024226d3`): **VALID `ABANDONED` RECORD** (`POLICY.md` §3).
  - `P-FIELD-CHAIN-UNIT-SEED-2` (Issue `#1553`, PR `#1555`, pin `bc1648745323a8843d2c3cb831b0f585b4e00427`, head `a12efb98551f972cdfebaa070baf051216ffe7ff`): **ACCEPT (`candidate-T` / `candidate-C`, Layer L1 mathematical scope only)**.

---

## 1. Exposure & Blindness Chronology

To guarantee complete methodological independence between the author lane (`P-FIELD-CHAIN-UNIT-SEED-1` / `-2`) and this review lane (`P-FIELD-CHAIN-UNIT-SEED-AUDIT-1` / `-2`), the independent proof (`PROOF.md`) and verifier (`verify.py`) were authored, pinned, read back on GitHub, and executed before any inspection of the author's branches, commits, or pull requests:

1. **Pre-Pin Source Boundary (`SOURCES.tsv`):**
   - Only `Public Canon v102` (`a632c6a162dc87e60104d7a478e7650a6d5c4a1b`), merged `P-2-5-LOW-NORM-SHELL` (`3f53cff429c67fbdfa95941b3024279d9fd59638`, PR `#1323`), the program issue `#1548` (body SHA-256 `c209686fede612501394f969d5052518d35c95be0523c9e22619cbd19984fd87`), and the metadata-only receipts on `#1548` (`6223262884`, `6224519265`, `6224570728`, `6224630229`) were read before pinning and executing our verifier.
2. **Abandoned First Attempt (`P-FIELD-CHAIN-UNIT-SEED-AUDIT-1`, Issue `#1561`, PR `#1564`):**
   - Pin commit `46e0ba7e4dafd9bb391253c9e888cfc54db574c2` was pushed and read back (`#1561` comment `6225223960`).
   - Its single formal execution exited with code `1` at line 156 (`assert mat_mul(B_F, ADJ_B_F) == mat_scale(5, I4)`) due to a hand-transcribed off-diagonal sign typo in the hardcoded matrix `ADJ_B_F`, before any lattice or residue enumeration ran.
   - Per `POLICY.md` §3, `P-FIELD-CHAIN-UNIT-SEED-AUDIT-1` was closed on its own branch with `RESULT.md` (`Status: ABANDONED`, commit `8e8c3f04`, no `EXPECTED.txt` or `RUN.md`) and opened as PR `#1564`.
3. **Successor Pin & First Formal Execution (`P-FIELD-CHAIN-UNIT-SEED-AUDIT-2`, Issue `#1565`):**
   - Specification pin `5838eb457cf2ec966682d97f4652259a5d3d6291` was pushed to `origin/probe/P-FIELD-CHAIN-UNIT-SEED-AUDIT-2`, read back via the GitHub API, and receipted on `#1565` (comment `6225295372`) before execution:
     - `PREREG.md`: 10583 bytes, SHA-256 `7122fdd6cb956db4c7c4a4c4ec3901ba7ea88d9592d0b2c43bdea23f76b47262`
     - `PROOF.md`: 13294 bytes, SHA-256 `0b4f3e06ccc4fc2f8331e81b5ba0730871a8e5c1b5b015329f4135382115d2cb`
     - `SOURCES.tsv`: 2898 bytes, SHA-256 `7835efc2c63aa8b9014eee9e9f3a64b05ded9c81133cb0400dcfb6c167a5d427`
     - `verify.py`: 12209 bytes, SHA-256 `397622dbfad43e52481abf63455b8b9a06da4355405fd3e78d6d129a853d947e`
   - The single formal local run (`python3 probes/P-FIELD-CHAIN-UNIT-SEED-AUDIT-2/verify.py`) succeeded with `exit_code: 0` and `stderr_bytes: 0`, producing `EXPECTED.txt` (2113 bytes, 36 lines, SHA-256 `71e8a101d2ec8d2d9b01090d981b13b2318c9288baba441c88cfd95bdf3b3538`) and `RUN.md` at commit `ca4077448fa347ac4d6ff42eb41922de558c9f02` (`#1565` comment `6225308394`).
4. **Post-Run Inspection of Author Package (`#1552` and `#1555`):**
   - Only after `ca4077448fa347ac4d6ff42eb41922de558c9f02` was pushed and receipted did we fetch and inspect `probe/P-FIELD-CHAIN-UNIT-SEED-1` (PR `#1552`, head `1844322bbb1f0b9f08ceaa9b9081b078024226d3`) and `probe/P-FIELD-CHAIN-UNIT-SEED-2` (PR `#1555`, head `a12efb98551f972cdfebaa070baf051216ffe7ff`).

---

## 2. Independent Findings (`P-FIELD-CHAIN-UNIT-SEED-AUDIT-2`)

### 2.1 Requirement R1: Complete $\mathbb{Z}^4$ Unit-Seed Bound via Schur Complement and Exact Adjugate

In the native basis $(1, \zeta_5, \zeta_5^2, \zeta_5^3)$ with $B_f(x,y) = \tfrac{1}{5}\operatorname{Tr}_{\mathbb{Q}(\zeta_5)/\mathbb{Q}}(\bar{x}y)$ and $H(x) = \tfrac{1}{2}x^T B_f x$:

1. **Exact Schur-Complement Sum of Squares (`PROOF.md` Theorem 1):**
   $$4H(a,b,c,d) = (3a^2 + 2ab + 2b^2) + (2c + 2a - b)^2 + (2d - a + 3b)^2,$$
   with positive-definite binary fiber form $q_2(a,b) = 3a^2 + 2ab + 2b^2$ satisfying
   $$2q_2(a,b) = 5a^2 + (a+2b)^2, \qquad 3q_2(a,b) = 5b^2 + (3a+b)^2.$$
2. **Exact Inverse/Adjugate Diagonal Bound (`PROOF.md` Corollary 1):**
   $$5B_f^{-1} = \operatorname{adj}(B_f) = \begin{pmatrix} 4 & -2 & -5 & 5 \\ -2 & 6 & 5 & -10 \\ -5 & 5 & 10 & -10 \\ 5 & -10 & -10 & 20 \end{pmatrix},$$
   which gives the sharp coordinate inequalities valid for every $x = (a,b,c,d) \in \mathbb{R}^4$ with $H(x) \le k$:
   $$5a^2 \le 8k, \qquad 5b^2 \le 12k, \qquad c^2 \le 4k, \qquad d^2 \le 8k.$$
3. **Complete $H(x)=1$ Unit Shell:**
   - For $k=1$, any integer solution to $H(x)=1$ satisfies $|a| \le 1$, $|b| \le 1$, $|c| \le 2$, $|d| \le 2$, restricting the entire $\mathbb{Z}^4$ search to the 225-point box $[-1,1]^2 \times [-2,2]^2$ (and via $q_2(a,b) \le 4$ to just 7 admissible $(a,b)$ fibers).
   - Both the 7-fiber Schur solver and the 225-point adjugate box (as well as the 625-point box $[-2,2]^4$) find the exact same **20 unit seeds** $U_1 = \{u \in \mathbb{Z}^4 : H(u)=1\}$, with maximum absolute coordinates $(1,1,2,2) \subset [-2,2]^4$.
4. **Complete $H(x) \le 5$ Shell Census:**
   - For $k=5$, the adjugate bounds restrict $\mathbb{Z}^4$ to $[-2,2] \times [-3,3] \times [-4,4] \times [-6,6]$ (4095 points), yielding the complete shell counts:
     $$(\#S_0, \#S_1, \#S_2, \#S_3, \#S_4, \#S_5) = (1, 20, 30, 60, 60, 120), \qquad \sum_{k=0}^{5} \#S_k = 291.$$

### 2.2 Requirement R2: Gate-Space Residue Classification and the $A_f$-Fixed Subgroup

For $L = I_4 - A_f$ ($\det L = 5$), the mod-5 image of $\mathbb{Z}^4$ is the 25-element gate subspace
$$\mathcal{G}_{25} = \{(3r_1, r_1, 3r_3, r_3) \bmod 5 : r_1, r_3 \in \mathbb{F}_5\} = \{r \in \mathbb{F}_5^4 : r_0 \equiv 3r_1,\; r_2 \equiv 3r_3 \pmod 5\}.$$

1. **Injectivity on $U_1$ (`PROOF.md` Proposition 2 & Theorem 2):**
   - The kernel of $x \mapsto Lx \bmod 5$ on $\mathbb{Z}^4$ is exactly $L\mathbb{Z}^4$, and $H(Lw) = 5H(w)$ for all $w \in \mathbb{Z}^4$.
   - For any $u_1, u_2 \in U_1$, Cauchy–Schwarz gives $H(u_1 - u_2) \le (\sqrt{H(u_1)} + \sqrt{H(u_2)})^2 = 4 < 5$. Hence $u_1 - u_2 \notin L\mathbb{Z}^4 \setminus \{0\}$, so $u \mapsto Lu \bmod 5$ is strictly injective on $U_1$: the 20 unit seeds map bijectively onto **20 distinct gate residues**, each with multiplicity `1`.
2. **Conceptual Characterization of the 5 Missing Gate Residues (`PROOF.md` Proposition 3 & Theorem 3):**
   - Since $A_f L = L A_f$, multiplication by $A_f \bmod 5$ preserves $\mathcal{G}_{25}$ and acts on the coordinates $(r_1, r_3)$ by the upper-unitriangular shear $(r_1, r_3) \mapsto (r_1 + r_3, r_3) \pmod 5$.
   - Its fixed-point subgroup is the 5-element subgroup defined by $r_3 \equiv 0 \pmod 5$ (equivalently $r_2 = r_3 = 0$):
     $$\mathcal{G}_{25}^{A_f} = \{(0,0,0,0),\; (1,2,0,0),\; (2,4,0,0),\; (3,1,0,0),\; (4,3,0,0)\}.$$
   - For any $u \in \mathbb{Z}^4$, $Lu \bmod 5 \in \mathcal{G}_{25}^{A_f}$ if and only if $L(A_f u - u) \equiv 0 \pmod 5$, i.e., $A_f u - u = -Lu \in L\mathbb{Z}^4$. If $H(u)=1$, then $H(A_f u)=1$ and $H(A_f u - u) \le 4 < 5$, which would force $A_f u = u$ and $u=0$, a contradiction. Thus **no unit seed can map into $\mathcal{G}_{25}^{A_f}$**, proving conceptually why those exact 5 gate residues have multiplicity `0` on the $H(x)=1$ shell while the four free $\langle A_f \rangle$-orbits of size 5 in $\mathcal{G}_{25} \setminus \mathcal{G}_{25}^{A_f}$ have multiplicity `1` everywhere.
   - *Precision note on higher-shell attainment:* In `EXPECTED.txt`, `NONZERO_MISSING_K2_MULTS=(1,2,0,0):5,(2,4,0,0):0,(3,1,0,0):0,(4,3,0,0):5` shows that on the $H(x)=2$ shell (`#S_2 = 30`), the two generator residues $(1,2,0,0)$ and $(4,3,0,0)$ of $\mathcal{G}_{25}^{A_f} \setminus \{0\}$ are attained with multiplicity 5 each, whereas their mod-5 doubles $(2,4,0,0)$ and $(3,1,0,0)$ have multiplicity 0 on $S_2$ and are first attained on $S_3$ ($H(x)=3$) via $x \mapsto (I_4+A_f)x$ with $H((I_4+A_f)u) = 3H(u) = 3$. (This refines the non-essential prose remark in `PROOF.md` §3.3 that all four nonzero missing residues are attained on $S_2$.)

### 2.3 Requirement R3: Unique Coset Minimum for $\bar{y}_3 = (0,0,3,1)$

- The target residue $\bar{y}_3 = (0,0,3,1) \pmod 5$ has $(r_1, r_3) = (0,1)$ with $r_3 = 1 \not\equiv 0 \pmod 5$, so $\bar{y}_3 \in \mathcal{G}_{25} \setminus \mathcal{G}_{25}^{A_f}$.
- Its unique unit preimage in $U_1$ is
  $$u^* = (0, -1, -1, 2), \qquad H(u^*) = 1,$$
  with image
  $$y^* = Lu^* = (0, 0, -2, 1) \equiv (0, 0, 3, 1) \pmod 5, \qquad H(y^*) = 5H(u^*) = 5.$$
- Every $y \in L\mathbb{Z}^4$ with $y \equiv (0,0,3,1) \pmod 5$ has the form $y = Lx$ with $Lx \equiv (0,0,3,1) \pmod 5$ and $H(y) = 5H(x) \in 5\mathbb{Z}_{\ge 1}$. Since $u^*$ is the unique solution with $H(x)=1$, $y^* = (0,0,-2,1)$ is the **unique global minimizer** of $H$ on the coset $\{y \in L\mathbb{Z}^4 : y \equiv (0,0,3,1) \pmod 5\}$, achieving $\min H = 5$.
- Across the shells $H(x) = k$ for $k = 1, 2, 3, 4, 5$, the number of preimages of $\bar{y}_3$ is `k1:1, k2:1, k3:2, k4:3, k5:5` (12 preimages with $H(x) \le 5$).

---

## 3. Audit of Author Lane `B` (`#1552` and `#1555`)

### 3.1 Abandoned Predecessor `P-FIELD-CHAIN-UNIT-SEED-1` (Issue `#1549`, PR `#1552`)

- **Commits inspected:**
  - Pin commit `066ef45911f6215f7574daba80fd53616ee1c66d`: `PREREG.md` and `verify.py`.
  - Closure commit `1844322bbb1f0b9f08ceaa9b9081b078024226d3`: adds `probes/P-FIELD-CHAIN-UNIT-SEED-1/RESULT.md` (`Status: ABANDONED`) without modifying `PREREG.md` or `verify.py` and without adding `EXPECTED.txt` or `RUN.md`.
- **Verification:**
  - Confirmed that the pinned `verify.py` in `066ef45911f6215f7574daba80fd53616ee1c66d` contained a formula defect in its coordinate box helper (`t = int(math.isqrt(2 * k))` with `b_bound = (t + s) // 2 = 1` instead of `2` at $k=1$, omitting the 4 unit vectors with $|b|=2$ in the raw $(1-\zeta_5)\zeta_5^j$ basis) and exited non-zero on its first formal run.
  - Confirmed that `PREREG.md` and `verify.py` are byte-identical between `066ef45911f6215f7574daba80fd53616ee1c66d` and `1844322bbb1f0b9f08ceaa9b9081b078024226d3`, and that GitHub Actions required checks (`check` `117192496399`, `architecture-x86_64` `117192159320`, `architecture-aarch64` `117192159445`) all succeeded.
  - **Conclusion:** `P-FIELD-CHAIN-UNIT-SEED-1` (PR `#1552`) is a compliant `ABANDONED` record under `POLICY.md` §3.

### 3.2 Successor `P-FIELD-CHAIN-UNIT-SEED-2` (Issue `#1553`, PR `#1555`)

- **Commits & Artifact Integrity:**
  - Commit 1 (`bc1648745323a8843d2c3cb831b0f585b4e00427`, specification pin):
    - `PREREG.md`: 8777 bytes, SHA-256 `690e2731800de3cd387ccd798be888a6008ce88e77f746c5cc0bd06eb141ca06`
    - `verify.py`: 6550 bytes, SHA-256 `548d0d57d28058651715360385dcfdd1a93a455d30f1314e73a7e4a5d1c81b9c`
  - Commit 2 (`87d6bd1e3c2eb05db97823ac927760ab5d858084`, formal run & results):
    - `EXPECTED.txt`: 2923 bytes, SHA-256 `bfaab07056c665a6d5d85d933fc4596fc06cc9d52e5f7cb3535cbda72f92645d`
    - `RUN.md`: 811 bytes, SHA-256 `6b7bd9594b76b03bfac9b1486b599dd43dfbe67fb3ce57302d3462511330ddbc` (`Ubuntu 22.04`, `x86_64`, `Python 3.10.12`, `exit_code: 0`, `stderr_bytes: 0`)
    - `PROOF.md`: 3201 bytes, SHA-256 `d8eb7c3334ccd2f0c439e0e77843dd574ac1e7022505f4bc6edc66042451324da`
    - `RESULT.md`: 2403 bytes, SHA-256 `5e46f2d38dcecd01998a175ac1e2e93c0385cc8404bc63367bb6390db88aa7a2`
  - Commit 3 (`a12efb98551f972cdfebaa070baf051216ffe7ff`, source manifest):
    - `SOURCES.sha256`: 774 bytes, SHA-256 `8ec2eec2fd52ec3d07806a824608391e5e0b7234fecb97113368178c672b0a43`
  - Both `PREREG.md` and `verify.py` are byte-for-byte unchanged from pin commit `bc1648745323a8843d2c3cb831b0f585b4e00427` to PR head `a12efb98551f972cdfebaa070baf051216ffe7ff`.
  - GitHub Actions required checks on `a12efb98551f972cdfebaa070baf051216ffe7ff` passed on both `x86_64` (`117208749534`) and `aarch64` (`117208749137`), as well as the aggregate `check` gate (`117208998140`).

### 3.3 Quantitative & Analytical Comparison (`P-FIELD-CHAIN-UNIT-SEED-2` vs. `P-FIELD-CHAIN-UNIT-SEED-AUDIT-2`)

| Audit Dimension | Author (`P-FIELD-CHAIN-UNIT-SEED-2`, `#1555`) | Reviewer (`P-FIELD-CHAIN-UNIT-SEED-AUDIT-2`, `#1565`) | Agreement |
| :--- | :--- | :--- | :--- |
| Quadratic form & basis | $H_{\mathrm{native}}(u) = \tfrac{1}{2}u^T B_f u$ in $(1,\zeta_5,\zeta_5^2,\zeta_5^3)$; also transforms from raw $(1-\zeta_5)\zeta_5^j$ basis via $M_{\mathrm{raw}\to\mathrm{native}} = L A_f^{\mathrm{raw}}$ | Native $H(x) = \tfrac{1}{2}x^T B_f x$ in $(1,\zeta_5,\zeta_5^2,\zeta_5^3)$ with $B_f = L^T L / 5$ | Exact match |
| Analytical $\mathbb{Z}^4$ completeness bound | Raw SOS identity $4H_{\mathrm{raw}}(a,b,c,d) = (a-c)^2 + (a+c+d)^2 + (2b-a-c+d)^2 + d^2 = 4k$, $s=\lfloor\sqrt{4k}\rfloor, t=\lfloor\sqrt{3k}\rfloor$: box $[-2,2]^3 \times [-4,4]$ (1125 pts) at $k=1$; $[-4,4]^3 \times [-8,8]$ (19635 pts) at $k \le 5$ | Native Schur-complement SOS $4H = q_2(a,b) + (2c+2a-b)^2 + (2d-a+3b)^2$ and $\operatorname{adj}(B_f)$ diagonal $(4,6,10,20)$: box $[-1,1]^2 \times [-2,2]^2$ (225 pts; 7 fibers) at $k=1$; $[-2,2]\times[-3,3]\times[-4,4]\times[-6,6]$ (4095 pts) at $k \le 5$ | Independent rigorous bounds; identical solution sets |
| Unit shell $H(u)=1$ | 20 vectors, all inside $[-1,1]^2 \times [-2,2]^2 \subset [-2,2]^4$ | 20 vectors, all inside $[-1,1]^2 \times [-2,2]^2 \subset [-2,2]^4$ | Byte-for-byte identical 20 vectors |
| Shell counts $H(u)=0..5$ | `(1, 20, 30, 60, 60, 120)` (sum 291) | `(1, 20, 30, 60, 60, 120)` (sum 291) | Exact match |
| Gate subspace $\mathcal{G}_{25}$ | $\{(3r_1, r_1, 3r_3, r_3) \bmod 5\}$ (25 residues) | $\{(3r_1, r_1, 3r_3, r_3) \bmod 5\}$ (25 residues) | Exact match |
| $Lu \bmod 5$ on $U_1$ | 20 distinct gate residues with multiplicity `1` each | 20 distinct gate residues with multiplicity `1` each (proved conceptually via $\ker(L\bmod 5)=L\mathbb{Z}^4$ and Cauchy–Schwarz) | Exact match |
| 5 missing gate residues | `(0,0,0,0), (1,2,0,0), (2,4,0,0), (3,1,0,0), (4,3,0,0)` ($r_2=r_3=0$, multiplicity `0` on $U_1$) | $\mathcal{G}_{25}^{A_f} = \{(0,0,0,0), (1,2,0,0), (2,4,0,0), (3,1,0,0), (4,3,0,0)\}$ (proved conceptually as the $A_f$-fixed subgroup of $\mathcal{G}_{25}$) | Exact match |
| Coset minimum for $\bar{y}_3 = (0,0,3,1)$ | Unique unit seed $u^* = (0,-1,-1,2)$, $y^* = Lu^* = (0,0,-2,1)$, $\min H(y) = 5$ | Unique unit seed $u^* = (0,-1,-1,2)$, $y^* = Lu^* = (0,0,-2,1)$, $\min H(y) = 5$ | Exact match |

### 3.4 Falsifier Audit (`PREREG.md` §5)

- **`F-BOX` (Did not fire):** Both the author's SOS completeness proof on $4H_{\mathrm{raw}}$ and our independent Schur-complement / $\operatorname{adj}(B_f)$ completeness proof establish explicit finite $\mathbb{Z}^4$ coordinate boxes analytically before any enumeration. Every unit vector satisfies $|u_i| \le 2$ (more tightly, $u \in [-1,1]^2 \times [-2,2]^2$).
- **`F-GAP` (Did not fire):** Among the 25 gate residues in $\mathcal{G}_{25}$, exactly 20 are hit with multiplicity 1 and 5 are missed with multiplicity 0.
- **`F-MIN` (Did not fire):** $u^* = (0,-1,-1,2)$ is the unique unit preimage of $\bar{y}_3 = (0,0,3,1)$, and $y^* = Lu^* = (0,0,-2,1)$ with $H(y^*)=5$ is the unique global minimizer of $H$ on $\{y \in L\mathbb{Z}^4 : y \equiv (0,0,3,1) \pmod 5\}$.
- **`F-INHERIT` (Properly enforced by the author):** The author explicitly credits `#1323` (`P-2-5-LOW-NORM-SHELL`, commit `3f53cff429c67fbdfa95941b3024279d9fd59638`) for the bounded $H \le 5$ shell counts `(1,20,30,60,60,120)` and raw 20-unit enumeration, claiming novelty only for the native-basis $\mathbb{Z}^4$ completeness proof, the complete 20-of-25 gate-residue table with 5 missing residues, and the unique coset minimum $u^* = (0,-1,-1,2) \mapsto y^* = (0,0,-2,1)$ at $H=5$.
- **`F-SELECTION` (Did not fire):** Both `PROOF.md` and `RESULT.md` in `#1555` explicitly restrict their scope to Layer L1 mathematical existence, minimum, and uniqueness, making no physical selection claim or native-$U$ source-preparation claim.

---

## 4. Conclusion

The independent mathematical derivation (`PROOF.md`) and two-architecture deterministic verifier (`verify.py`, `EXPECTED.txt`, `RUN.md`) in `P-FIELD-CHAIN-UNIT-SEED-AUDIT-2` confirm every mathematical and computational claim of `P-FIELD-CHAIN-UNIT-SEED-2` (PR `#1555`) and further strengthen its theoretical foundation by providing:
1. A tighter native-basis Schur-complement and $\operatorname{adj}(B_f)$ completeness box ($[-1,1]^2 \times [-2,2]^2$, 225 points vs. 1125 points at $k=1$; 4095 points vs. 19635 points at $k \le 5$), and
2. A conceptual, enumeration-free proof of both the injectivity of $u \mapsto Lu \bmod 5$ on $U_1$ (via $\ker(L \bmod 5) = L\mathbb{Z}^4$ and Cauchy–Schwarz) and the exact identity of the 5 missing gate residues as the $A_f$-fixed subgroup $\mathcal{G}_{25}^{A_f}$ of $\mathcal{G}_{25}$.

We recommend **merging PR `#1552`** as a valid `ABANDONED` record for `P-FIELD-CHAIN-UNIT-SEED-1` and **accepting PR `#1555` (`P-FIELD-CHAIN-UNIT-SEED-2`)** at `candidate-T` / `candidate-C` (Layer L1 mathematical scope).
