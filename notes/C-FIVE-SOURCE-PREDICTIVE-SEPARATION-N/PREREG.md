# Preregistration: five-source predictive separation (`C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N`)

**PUBLIC NON-CANONICAL / L1 analytical incubation preregistration / 2026-10-14.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1500](https://github.com/mathorn1973/twist-j/issues/1500), dispatched under [#1497](https://github.com/mathorn1973/twist-j/issues/1497).

```text
candidate_id:       C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N
branch:             incubation/C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N
allowed_path:       notes/C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N/
authority_base:     8b91a935c426036e00ecb300019fd94734addeec (Public Canon v101 ACTIVE)
action_layer:       L1 (algebraic identifiability and conditional prospective measurement contract)
evidence_mode:      ANALYTICAL_PROOF_ONLY (no new scientific verifier execution)
scientific_code:    NONE / NOT_RUN
owner_session:      Antigravity-A3-1500-20261014-a6e51baf-bce0-4ee1-8b58-a954f4f3b12a
```

---

## 1. Distinction between previously exposed inputs and new obligations

### 1.1 Previously known and result-exposed inputs (inherited, not re-claimed as new)

1. **Canonical native substrate (`canon/CANON.md` at `8b91a935c426036e00ecb300019fd94734addeec`):** Autonomous state $\Omega = \mathbb{N}_0 \times \mathbb{F}_5^6$, update $U$, five involutions $g_0,\dots,g_4$ with $z_6$ action $(z, -z, 2-z, 2-z, 3-z)$, and theorems `U-NATIVE-RAW-RESIDUE-READOUT` `[T]` and `U-NATIVE-RECEIVER-ONLY-RESIDUE-NOGO` `[T]`.
2. **Classical signed-port contract and proofs (`1b69563af4018b08d7dc75781b12e9553a8c19c3`, contract pin `4302c31f07823b2a843e3702ca14620c1917b853`):**
   - Five-site source map $S(z)$, source Gram $G_{\mathrm{source}} = I_4 - \frac{1}{5}\mathbf{1}\mathbf{1}^T$, finite causal buffer $D = Y + B_{\mathrm{zero}} + B_{\mathrm{zero}}$, principal Dirichlet operator $L_D$, four loaded ports $R = (y_0,y_1,y_2,y_3)$ with $g_j = 2$.
   - First-cut response $b_0 = R_0 z = -\frac{1}{4}Mz$, explicit rank-one inverse $z = -4M^{-1}b_0 = -\frac{216}{59}(I + \frac{1}{365}v\mathbf{1}^T)b_0$, and loaded second-cut response $b_1 = R_1 z$ with $R_1 = \frac{1}{2}Q - \frac{1}{4}K + \frac{1}{8}JM$.
   - Occupied two-tape bijection $F$, inverse $F^{-1}$, and conserved full amplitude energy $E_{\mathrm{full}}$.
   - Prospective 9-preparation $Z_I$ / 24-preparation $Z_V$ calibration-and-validation split with engineering allowance $\varepsilon_y = \varepsilon_E = 1/10000$.
3. **Conditional native-classical two-cut contact (`ea924e214ec3c29009fd4590f294954d3e5ad43f`, contract pin `7b3fa47c0223bd99fce977de6ea58d484e257033`) and merged finite census (`P-NATIVE-CLASSICAL-CONTACT-CENSUS-1`, pin `498f658f2de0ecfcd71694cd2bc026f280f2fa3b`):**
   - Three-tick native branch schedule on $p \in \mathbb{F}_5^4$ from $C_0 = (0,1)$, receiver table $C_1(h)$, balanced lift $\eta(q,r)$, mixed contact $C_*$, induced five-point set $Z_5 = \{z^{(0)},\dots,z^{(4)}\}$, work values $(0, \frac{1}{10}, \frac{3}{20}, \frac{2}{5}, \frac{2}{5})$, integer tables $12960\,b_0$ and $1399680\,b_1$ on $Z_5$, and prepared-image inverse on all $625$ inputs.
4. **Historical read-only context (`b7636a334b09fcc68422bcd6cc6e15334d416c59`, `#1495`/`#1496`):** Bounded-store involution $H_B$ and resource bounds; owned by `#1495` and Agent 1 (`#1498`), not duplicated or re-proved here.

All numerical tables ($M, R_1, 12960\,b_0, 1399680\,b_1, E_0$) in the sources above are already public and result-exposed. None of them may be presented as a blind holdout discovery.

---

## 2. Frozen new obligations to be resolved after this pin

### Obligation A: Preparation mismatch and subspace accessibility certificate

1. Prove that $\operatorname{span}_{\mathbb{Q}}(Z_5) = \operatorname{aff}_{\mathbb{Q}}(Z_5) = \mathbb{Q}e_0 \oplus \mathbb{Q}e_1 = \{(z_0, z_1, 0, 0) : z_0, z_1 \in \mathbb{Q}\}$ of rational dimension $2$.
2. Determine the exact set intersections $Z_5 \cap Z_I$, $Z_5 \cap Z_V$, $\operatorname{span}_{\mathbb{Q}}(Z_5) \cap Z_I$, and $\operatorname{span}_{\mathbb{Q}}(Z_5) \cap Z_V$.
3. Prove that two additional source vectors $u_2, u_3 \in \mathbb{Q}^4$ complete $Z_5$ to a spanning set of $\mathbb{Q}^4$ if and only if their equivalence classes $[u_2], [u_3]$ in $\mathbb{Q}^4 / (\mathbb{Q}e_0 \oplus \mathbb{Q}e_1)$ are linearly independent, so two quotient-independent directions are both necessary and sufficient.
4. Decompose the linear/quadratic model parameter space under restriction to $\Pi_2 = \mathbb{Q}e_0 \oplus \mathbb{Q}e_1$ into an identifiable subspace and an annihilated kernel subspace for $A_0, A_1 \in \mathbb{Q}^{4 \times 4}$ and $G_0 \in \mathbb{Q}^{4 \times 4}_{\mathrm{sym}}$.

### Obligation B: Target-independent model family and ideal-classical-clone bound

1. Freeze the parameter dimensions and literal equality conditions of $\mathcal{A}_{\mathrm{lin}}$, $\mathcal{A}_{\mathrm{aff}}$, and $\mathcal{A}_{\mathrm{nl}}$.
2. Prove the exact clone indistinguishability theorem: if an ordinary rational classical wave/port comparator $D_{\mathrm{cl}}$ implements the same effective source map $p \mapsto z$, ready state $X_{\mathrm{blank}}$, transition $F$, and observable projection $\Pi_{\mathrm{port}}$ on a declared source domain $\mathcal{Z} \subseteq \mathbb{Q}^4$, then for every preparation protocol drawing inputs from $\mathcal{Z}$ (including any extension of $Z_5$ by two quotient-independent directions to span $\mathbb{Q}^4$), the induced classical port and energy records of $D_{\mathrm{NC}}$ and $D_{\mathrm{cl}}$ are identically equal.
3. Classify the exact types of interventions or extended observables that can separate $D_{\mathrm{NC}}$ from $D_{\mathrm{cl}}$ without circularity.

### Obligation C: Calibration-to-prediction decision ($I(m_1)=I(m_2) \Rightarrow V(m_1;s)=V(m_2;s)$)

Decide $\mathrm{Det}(\mathcal{A}, I_{\mathrm{set}}, V_{\mathrm{set}})$ across the following frozen regimes, giving exact reconstruction formulas where positive and explicit complete model pairs $(m_1, m_2)$ where negative:

1. **Regime C1 (Within-plane $Z_5$ calibration to withheld $Z_5$ / $\Pi_2$ predictions in $\mathcal{A}_{\mathrm{lin}}$ and $\mathcal{A}_{\mathrm{aff}}$):**
   - For $\mathcal{A}_{\mathrm{lin}}$: determine the minimal calibration subset $I_{\mathrm{min}} \subset Z_5$ for the linear response $(b_0, b_1)$ versus for the quadratic initial energy $E_0$, and prove the exact redundancy relations on the withheld $Z_5$ points and on $\Pi_2 \cap (Z_I \cup Z_V)$.
   - For $\mathcal{A}_{\mathrm{aff}}$: determine how many and which points of $Z_5$ are required so that $I(m_1)=I(m_2)$ fixes all predictions on $Z_5$ and $\Pi_2$.
2. **Regime C2 ($Z_5$ calibration to out-of-plane $Z_I/Z_V$ predictions in $\mathcal{A}_{\mathrm{lin}}$):**
   - Prove that $\mathrm{Det}(\mathcal{A}_{\mathrm{lin}}, Z_5, Z_V)$ fails on all $20$ out-of-plane preparations in $Z_V \setminus \Pi_2$, and exhibit explicit complete models $m_1, m_2 \in \mathcal{A}_{\mathrm{lin}}$ (including positive-definite energy matrices $G_0$) that agree identically on all five points of $Z_5$ (and all of $\Pi_2$) while diverging on $Z_I \setminus \Pi_2$ and $Z_V \setminus \Pi_2$.
3. **Regime C3 (Nonlinear source-dependent class $\mathcal{A}_{\mathrm{nl}}$ on $Z_5$ and on $Z_I \to Z_V$):**
   - Exhibit explicit polynomial/nonlinear models $m_1, m_2 \in \mathcal{A}_{\mathrm{nl}}$ that agree on any proper subset of $Z_5$ (or on all $9$ points of $Z_I$) while diverging on the remaining point(s) of $Z_5$ (or on $Z_V$).
4. **Regime C4 (Conditional full-span augmentation):**
   - Prove the exact conditions on added source preparations $U_{\mathrm{ext}} \subset \mathbb{Q}^4$ under which $I_{\mathrm{set}} = Z_5 \cup U_{\mathrm{ext}}$ determines all linear responses $(b_0, b_1)$ on $\mathbb{Q}^4$ versus all quadratic energies $E_0(z) = \frac{1}{2}z^T G_0 z$ on $\mathbb{Q}^4$ (distinguishing the 2 extra directions required for linear response from the cross-term requirements of symmetric quadratic forms), while proving that even full $\mathbb{Q}^4$ parameter identifiability leaves $D_{\mathrm{NC}}$ and $D_{\mathrm{cl}}$ indistinguishable on $\Pi_{\mathrm{port}}$.

### Obligation D: Prospective finite test specification and exported sibling interface

1. Specify the concrete two-stage prospective test on $Z_5$ (calibration subset $I_5 \subset Z_5$, held-out redundancy subset $V_5 = Z_5 \setminus I_5$, continuing-wave acquisition of $b_1$, full energy residual $r_E$, and interval decision rule with $\varepsilon_y = \varepsilon_E = 1/10000$) and the conditional extended test when external source directions or native-retention checks are supplied.
2. Populate the 13-field shared exported interface, explicitly marking unsupplied items `UNSUPPLIED` and stating exact non-circular test observables for any future capability delivered by Agent 1 or Agent 2.

---

## 3. Stop and falsifier conditions

- If any inherited identity from `#1484`/`#1485`, `#1486`/`#1489`, or `#1491`/`#1492` is contradicted on its declared domain, stop and record the exact contradiction.
- Once this preregistration commit is pushed and publicly read back (`PINNED_A3`), `README.md` (initial pin state), `CONTRACT.md`, `PREREG.md`, and `SOURCES.json` are frozen; all proofs, witnesses, results, and promotion mappings are added in descendant commits without history rewrite.
