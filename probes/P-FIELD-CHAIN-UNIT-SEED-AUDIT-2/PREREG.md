# P-FIELD-CHAIN-UNIT-SEED-AUDIT-2

Status: preregistered independent review probe (`NON-CANONICAL`, result-exposed).
Action layer: L1 only.
Owner: A. M. Thorn / `Antigravity-20261016-v103-unit-seed-audit` session.
Public lock: #1565 (successor of #1561). Parent program: #1548 lane RB (`DISPATCH_RELEASED` comment `6223262884`; #1548 body read back at 13858 UTF-8 bytes, SHA-256 `c209686fede612501394f969d5052518d35c95be0523c9e22619cbd19984fd87`).
Reviewed author lane: B (#1549 abandoned predecessor `P-FIELD-CHAIN-UNIT-SEED-1` at pin `066ef45911f6215f7574daba80fd53616ee1c66d`, `PREREG.md` SHA-256 `7b83fad72421105a3a965679b4283bbe5a6f7206672e1af3f039913049a8d0cb`; #1553 successor `P-FIELD-CHAIN-UNIT-SEED-2` at pin `bc1648745323a8843d2c3cb831b0f585b4e00427`, `PREREG.md` SHA-256 `690e2731800de3cd387ccd798be888a6008ce88e77f746c5cc0bd06eb141ca06`).
Branch: `probe/P-FIELD-CHAIN-UNIT-SEED-AUDIT-2`.
Path: `probes/P-FIELD-CHAIN-UNIT-SEED-AUDIT-2/`.

## Predecessor

`P-FIELD-CHAIN-UNIT-SEED-AUDIT-1` (public lock #1561) is `ABANDONED`. Its pin `46e0ba7e4dafd9bb391253c9e888cfc54db574c2` was read back before execution; its single formal run exited 1 on a hand-transcribed off-diagonal cofactor error in the hardcoded constant matrix `ADJ_B_F` before any unit-shell solver, box enumeration, residue classification, or coset-minimum computation ran. It produced no scientific stdout, no `EXPECTED.txt`, and no `RUN.md`; its abandonment record is draft PR #1564 (`8e8c3f04`) and the identifier is consumed. This successor changes no scientific equation, domain, Schur-complement/adjugate diagonal bound, threshold, or falsifier from #1561; it updates only the off-diagonal entries of $5 B_f^{-1} = \operatorname{adj}(B_f)$ (whose diagonal $(4,6,10,20)$ is unchanged) and the `-2` identifier.

## Authority and exposure barrier

Source: public `main` at `a632c6a162dc87e60104d7a478e7650a6d5c4a1b` (`Public Canon v102` `ACTIVE`, peeled tag `canon-v102` at the same commit, content commit `b04e22dd3ed8e4240cff347364f24670d4183a4d`, `canon/CANON.md` 1024033 bytes, SHA-256 `c0657380438c965f9556b5b298a34a5e799c48a68ce66e9fe51786ce2413d7d1`). The required two-architecture `main` check (`38939750393`), tag publication (`38940217812` attempt 3), and release-event published-assets readback (`38956254023` attempt 2) are all completed with `success`.

Before freezing and publicly reading back this preregistration, `PROOF.md`, `SOURCES.tsv`, and `verify.py`, and before recording the first formal run of `verify.py`, the reviewer has read **only** the admitted specifications and canonical/lineage sources listed in `SOURCES.tsv`. The author's `verify.py`, `EXPECTED.txt`, `RUN.md`, `RESULT.md`, and pull-request diffs (#1552, #1555) have **not** been opened or imported. Exposed target counts and vectors in #1548 and the author's `PREREG.md` are treated as explicit hypotheses to prove or refute, not as enumeration bounds.

## 1. Equation (frozen review targets and independent proof route)

Fix the Canon v102 matrices and quadratic form (`FIELD-CONSERVATIVE-CHAIN-LAW`, shared proof section 2) on $y = (a,b,c,d)^T \in \mathbb{Z}^4$:

$$
A_f = \begin{pmatrix} 1 & 0 & 1 & 0 \\ 0 & 1 & 0 & 1 \\ -2 & 1 & -1 & 1 \\ 1 & -3 & 1 & -2 \end{pmatrix}, \quad
B_f = \begin{pmatrix} 4 & -2 & 2 & -1 \\ -2 & 6 & -1 & 3 \\ 2 & -1 & 2 & 0 \\ -1 & 3 & 0 & 2 \end{pmatrix}, \quad
L = \begin{pmatrix} 1 & -3 & -1 & -2 \\ -3 & 4 & -2 & 1 \\ 0 & 5 & 1 & 2 \\ 5 & -5 & 2 & -1 \end{pmatrix},
$$

$$
V_{\mathrm{inv}} = 5 L^{-1} = \begin{pmatrix} 1 & 2 & 1 & 2 \\ 2 & -1 & 2 & -1 \\ 0 & -5 & 1 & -3 \\ -5 & 5 & -3 & 4 \end{pmatrix}, \quad
H(y) = \frac{1}{2} y^T B_f y = 2a^2 - 2ab + 3b^2 + c^2 + d^2 + 2ac - ad - bc + 3bd.
$$

Whereas the author's `PREREG.md` bounds coordinates via the 6-coordinate $P(y)$ embedding into $4 H_{\mathrm{raw}}$ (yielding $[-2,2]^3 \times [-4,4]$ at $k=1$) and #1323 bounded the $C_{\mathrm{cyc}}$ $A_4$-Cartan coordinates via $5 K^{-1}$, this audit uses an independent native-coordinate route:

1. **R1 — Native block Schur complement and adjugate completeness bound ($H(y) \le k$ and $H(u) = 1$):**
   Because the $(c,d)$ block of $B_f$ is $2 I_2$, completing the squares in $(c,d)$ first yields the exact polynomial identity over $\mathbb{Z}[a,b,c,d]$:
   $$
   4 H(a,b,c,d) = (3a^2 + 2ab + 2b^2) + (2c + 2a - b)^2 + (2d - a + 3b)^2,
   $$
   together with the two binary Schur-complement identities
   $$
   2(3a^2 + 2ab + 2b^2) = 5a^2 + (a + 2b)^2, \qquad
   3(3a^2 + 2ab + 2b^2) = 5b^2 + (3a + b)^2,
   $$
   and $\det(B_f) = 5$ with adjugate
   $$
   \operatorname{adj}(B_f) = 5 B_f^{-1} = \begin{pmatrix} 4 & -2 & -5 & 5 \\ -2 & 6 & 5 & -10 \\ -5 & 5 & 10 & -10 \\ 5 & -10 & -10 & 20 \end{pmatrix}
   $$
   having diagonal $(4, 6, 10, 20)$. By Cauchy–Schwarz $y_i^2 \le 2(B_f^{-1})_{ii} H(y)$, every $y \in \mathbb{Z}^4$ with $H(y) \le k$ satisfies the sharp native coordinate bounds
   $$
   5a^2 \le 8k, \quad 5b^2 \le 12k, \quad c^2 \le 4k, \quad d^2 \le 8k.
   $$
   In particular, for $k=1$ ($H(u)=1$), every integer solution lies in the 225-point box $[-1,1] \times [-1,1] \times [-2,2] \times [-2,2] \subset [-2,2]^4$, and is also obtained without box scanning by solving the two-square fiber $(2c+2a-b)^2 + (2d-a+3b)^2 = 4 - (3a^2+2ab+2b^2)$ over the 7 pairs $(a,b) \in [-1,1]^2$ with $3a^2+2ab+2b^2 \le 4$.

2. **R2 — Conceptual injectivity and missing-residue theorem on the 25 gate residues:**
   Define the 25-element gate-residue subgroup
   $$
   \mathcal{G}_{25} = \{r \in \mathbb{F}_5^4 : r_0 + 2r_1 \equiv r_2 + 2r_3 \equiv 0 \pmod 5\} = \{(3r_1, r_1, 3r_3, r_3) \bmod 5 : (r_1, r_3) \in \mathbb{F}_5^2\}.
   $$
   Because $L^2 = 5 A_f^3$, $V_{\mathrm{inv}} = A_f^2 L$, and $V_{\mathrm{inv}} L = 5 I_4$, the homomorphism $\pi_L : \mathbb{Z}^4 \to \mathcal{G}_{25}$, $x \mapsto Lx \bmod 5$, is surjective with kernel **literally $\ker(\pi_L) = L\mathbb{Z}^4$**. Since $H(Lw) = 5 H(w)$, every nonzero vector in $\ker(\pi_L) = L\mathbb{Z}^4$ has $H \in 5\mathbb{Z}_{\ge 1}$.
   - *Injectivity on the unit shell:* If $H(u_1) = H(u_2) = 1$ and $Lu_1 \equiv Lu_2 \pmod 5$, then $u_1 - u_2 \in L\mathbb{Z}^4$, so $H(u_1 - u_2)$ is a multiple of $5$; by Cauchy–Schwarz $0 \le H(u_1 - u_2) \le (\sqrt{1}+\sqrt{1})^2 = 4 < 5$, forcing $H(u_1 - u_2) = 0$ and $u_1 = u_2$.
   - *Exact missing-residue subgroup:* On $\mathcal{G}_{25}$, $A_f \bmod 5$ acts on $(r_1, r_3)$ by the unipotent shear $(r_1, r_3) \mapsto (r_1 + r_3, r_3) \pmod 5$, with 5-element fixed subgroup $\mathcal{G}_{25}^{A_f} = \{(3r_1, r_1, 0, 0) \bmod 5 : r_1 \in \mathbb{F}_5\}$. If $H(u)=1$ had $Lu \bmod 5 \in \mathcal{G}_{25}^{A_f}$, then $L(A_f u - u) \equiv 0 \pmod 5 \implies A_f u - u \in L\mathbb{Z}^4 \implies H(A_f u - u) \in 5\mathbb{Z}_{\ge 0} \cap [0,4] = \{0\} \implies A_f u = u \implies 5u = \sum_{j=0}^4 A_f^j u = 0 \implies u = 0$, contradiction. Hence the 20 unit seeds map bijectively onto the 20 residues with $r_3 \not\equiv 0 \pmod 5$, and the 5 residues with no unit preimage are exactly $\mathcal{G}_{25}^{A_f}$.

3. **R3 — Exact coset minimum, attainment, and uniqueness for $\bar{y}_3 = (0,0,3,1)$:**
   Since $\bar{y}_3 = (0,0,3,1) \in \mathcal{G}_{25} \setminus \mathcal{G}_{25}^{A_f}$ has $r_1 = 0, r_3 = 1 \neq 0$, it has a unique unit preimage $u^* = (0,-1,-1,2)$ ($H(u^*)=1$) with $y^* = Lu^* = (0,0,-2,1) \equiv \bar{y}_3 \pmod 5$ and $H(y^*) = 5 H(u^*) = 5$. For any $y = Lx \in L\mathbb{Z}^4$ with $y \equiv \bar{y}_3 \pmod 5$, $x \neq 0 \implies H(x) \ge 1 \implies H(y) = 5 H(x) \ge 5$, with equality iff $H(x)=1$ and $Lx \equiv Lu^* \pmod 5$, which by R2 forces $x = u^*$ and $y = y^* = (0,0,-2,1)$ across all of $L\mathbb{Z}^4$.

4. **R4 — Lineage vs. novelty boundary (#1323) and post-run author audit:**
   Verify precisely which claims are inherited from `canon/CANON.md` and #1323 (`C-FIELD-J-ENERGY-READOUT-N` at `3f53cff429c67fbdfa95941b3024279d9fd59638`, which already proved the $A_4$-Cartan $H \le 5$ box and shell counts $(1,20,30,60,60,120)$) versus genuinely new in Lane B (native $B_f$ completeness bound, complete $Lu \bmod 5$ classification over $\mathcal{G}_{25}$ with the 5 missing residues $\mathcal{G}_{25}^{A_f}$, and exact coset minimum/uniqueness on $y \equiv \bar{y}_3 \pmod 5$). After recording our first formal run, audit both #1552 (abandoned `-1` record) and #1555 (successor `-2` package).

## 2. Code

`verify.py` in `probes/P-FIELD-CHAIN-UNIT-SEED-AUDIT-2/`, using only the Python standard library and exact integer/rational arithmetic. It verifies all algebraic and polynomial identities in R1–R3, solves the two-square fiber and scans the proved adjugate boxes for $k=1..5$, classifies all 25 gate residues and shell minimums, and prints a deterministic report.

Run from the repository root:

```text
PYTHONHASHSEED=0 PYTHONUTF8=1 PYTHONDONTWRITEBYTECODE=1 \
python3 probes/P-FIELD-CHAIN-UNIT-SEED-AUDIT-2/verify.py
```

## 3. Carrier and data

Carrier: $\mathbb{Z}^4$ and $\mathbb{F}_5^4$ with the canonical matrices $A_f, B_f, L, V_{\mathrm{inv}}$. No external data, floating-point arithmetic, randomness, or imported author code. Admitted inputs are fixed in `SOURCES.tsv`.

## 4. Systematics

This is an implementation-blind, result-exposed independent review: target counts and vectors were disclosed in #1548 and the author's `PREREG.md`, while the reviewer's proof route (native block Schur complement, adjugate diagonal bounds, and $\ker(L \bmod 5) = L\mathbb{Z}^4$ Cauchy–Schwarz injectivity) and verifier are derived and frozen before opening any author proof, verifier, or output.

## 5. Failure threshold (falsifiers)

- `F-PREMISE`: any canonical matrix, Schur-complement, adjugate, or kernel identity fails in `verify.py` (nonzero exit).
- `F-TARGET`: the independently computed unit count, distinct gate-residue count, missing gate-residue set, unique unit preimage $u^*$ for $\bar{y}_3$, or coset minimum differs from the exposed targets $(20, 20, 5, (0,-1,-1,2), 5)$.
- `F-INHERIT`: the author package claims novelty for content already proved in #1323 without reporting lineage inheritance.
- `F-AUTHOR-DEFECT`: post-run inspection of the author's #1552 / #1555 packages reveals a mathematical gap, unclosed completeness bound, exposure violation, or policy/record defect.

## 6. Action layer

L1 only (`NON-CANONICAL` review probe). This audit proves and checks finite integer lattice and residue properties of the canonical field cell; it establishes no native-$U$ source preparation, physical selection principle, energy-funded contact, or Canon/registry/frontier/gate modification.
