# Result and exported interface: `C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N`

**NON-CANONICAL / L1 analytical result (R1/R2 revision after A4 review) / 2026-10-14.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1500](https://github.com/mathorn1973/twist-j/issues/1500), dispatched under [#1497](https://github.com/mathorn1973/twist-j/issues/1497).

```text
candidate_id:               C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N
slot:                       A3
branch:                     incubation/C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N
allowed_path:               notes/C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N/
authority_base:             8b91a935c426036e00ecb300019fd94734addeec (Public Canon v101 ACTIVE)
preregistration_commit:     274a88757863f55a838068e92241af1ee23f2de4
initial_result_commit:      58d7d6d962d847a19473dc8b233e2f844b2d378d
r1_result_commit:           963ac3d0cc2386eddf7b636ebb817fc098697155
revision_round:             R2 narrow completion after A4 R1 review (https://github.com/mathorn1973/twist-j/pull/1503#pullrequestreview-5525320737)
revision_assignment:        https://github.com/mathorn1973/twist-j/issues/1500#issuecomment-6179502346 (completing https://github.com/mathorn1973/twist-j/issues/1500#issuecomment-6178752881)
exposure_status:            Outcome-exposed R1/R2 revision after administrative intake (#1497#issuecomment-6178339036)
                            and A4 reviews (#1497#issuecomment-6178492183, #1497#issuecomment-6179511092)
proof_status:               AUTHORED_PROOF; SELF_REVIEWED; A4_REVIEWED_R1_R2_AMENDED (awaiting A4 re-review of R2 head)
scientific_code_status:     NONE / NOT_RUN (analytical proof-only round)
physical_status:            NOT_READY (no laboratory instance or Stage S certificates supplied)
overall_verdict:            DELIVERED_CANDIDATE (conditional candidate-T and candidate-D at L1 scope;
                            exact within-plane determination on Z5, exact out-of-plane underdetermination
                            with positive-definite witnesses, exact same-law classical-clone indistinguishability,
                            and conditional witnesses against restricted comparators)
```

---

## 1. Summary of proved, conditional, excluded, and still-missing statements

### 1.1 What is proved (conditional candidate-T at L1 scope, [PROOF.md](PROOF.md))

1. **Rank-two source span and preparation mismatch (`Theorem A1`, `Proposition A2`, `Theorem A3`, `Theorem A4`):**
   - Under $\ell(0,1,2,3,4) = (0,1,2,-2,-1)$ and $\eta(q,r) = (\ell(q)/2, (\ell(r)+1)/2, 0, 0)$, the five native-accessible encodings $Z_5 = \{z^{(0)}, z^{(1)}, z^{(2)}, z^{(3)}, z^{(4)}\}$ span the $2$-dimensional plane $\Pi_2 = \mathbb{Q}e_0 \oplus \mathbb{Q}e_1$ both linearly and affinely ($\operatorname{span}_{\mathbb{Q}}(Z_5) = \operatorname{aff}_{\mathbb{Q}}(Z_5) = \Pi_2$, $\dim_{\mathbb{Q}} = 2$), and even the full $25$-point receiver image $\eta(\mathbb{F}_5^2)$ is contained in $\Pi_2$.
   - Literally, $Z_5 \cap Z_I = \{0, e_1\}$ ($2$ of $9$) and $Z_5 \cap Z_V = \emptyset$ ($0$ of $24$); at the subspace level, $\Pi_2 \cap Z_I = \{0, \pm e_0, \pm e_1\}$ ($5$ of $9$) and $\Pi_2 \cap Z_V = \{\pm e_0 \pm e_1\}$ ($4$ of $24$), leaving $4$ identification sources and $20$ validation sources outside $\Pi_2$.
   - Adjoining an external source set $U_{\mathrm{ext}} \subset \mathbb{Q}^4$ spans $\mathbb{Q}^4$ together with $Z_5$ if and only if $\pi_{23}(U_{\mathrm{ext}})$ spans $\mathbb{Q}^2$, so $\min |U_{\mathrm{ext}}| = 2$ quotient-independent directions ($u^{(2)}_2 u^{(3)}_3 - u^{(2)}_3 u^{(3)}_2 \ne 0$) are necessary and sufficient.
   - Restricting the $42$-parameter linear/quadratic model class $\mathcal{A}_{\mathrm{lin}} = \{(A_0, A_1, G_0)\}$ to $\Pi_2$ identifies the $19$-dimensional subspace $(A_0^{(01)}, A_1^{(01)}, G_{00})$ via (A9)–(A10) and annihilates the $23$-dimensional kernel $\mathcal{K}_{\mathrm{lin}}(\Pi_2)$ ($8$ entries in $A_0^{(23)}$, $8$ in $A_1^{(23)}$, $7$ in $(G_{01}, G_{11})$).
2. **Ideal classical clone indistinguishability and conditional witnesses against restricted comparators (`Theorem B1`, `Theorem B2`):**
   - On the inherited ordered port tuple $R = (y_0, y_1, y_2, y_3) = ((0,0,0), (1,1,0), (1,0,1), (0,1,1)) \in D_3^4$ (with fifth site $y_4 = (2,0,0) \in D_3$), any ordinary rational classical wave/port comparator $D_{\mathrm{cl}}$ implementing the same $(S, F, \eta, X_{\mathrm{blank}}, \Pi_{\mathrm{port}})$ produces byte-identical signed port outputs $(b_0, b_1)$, wave/tape energies $(E_0, E_1, E_2)$, and work ledger $w$ to $D_{\mathrm{NC}}$ on all $625$ native inputs $p \in \mathbb{F}_5^4$ and on any extended source set $\mathcal{Z} \subseteq \mathbb{Q}^4$ (including full $\mathbb{Q}^4$ span). Matched timing, memory, and funding are required before claiming mechanism discrimination.
   - Against explicitly restricted comparator classes (without claiming a necessary-and-sufficient classification of all mechanisms or excluding classical devices with matched timing, memory, or store guards), three conditional witnesses are established:
     - **Witness M1 (vs. $h$-only comparator):** Reading the retained native checkpoint $x_3(p)$ across the $125$-element fibres $\mathcal{F}_h$ breaks $h$-factorization and separates $D_{\mathrm{NC}}$ from an $h$-only comparator (witness $p^{(0,a)}=(0,0,0,0)$ vs $p^{(0,b)}=(1,4,0,0)$ in (B3)); a classical comparator retaining full $p \in \mathbb{F}_5^4$ is not excluded.
     - **Witness M2 (vs. static lookup comparator):** Shifting single-contact timing from $n=1$ to $n=2$ (reading current $C_2(p)$) merges $h=0,1 \mapsto e_1$ ($12960\,b_0 = (698,-2832,708,696) \ne 0$ at $h=0$) and prepares $z_{n=2}^{(2)} = (-\frac{1}{2},\frac{1}{2},0,0)$, $z_{n=2}^{(3)} = (-1,\frac{1}{2},0,0)$ with energies $\frac{1}{4}, \frac{3}{5}$, separating $D_{\mathrm{NC}}$ from a static $n=1$ lookup comparator. At fixed $n=2$, M2 still factors through $h(p)$, does not exclude a classical comparator implementing the same time-dependent table, does not prepare $-e_0$ or $-e_1$, and is distinct from Agent 2's (`#1499`) second contact at $n=3$ reading retained $d = C_{1,B}$ captured at $n=1$.
     - **Witness M3 (vs. differently funded comparator under historical $H_B$):** Under the full `#1495`/`#1496` law $H_B$ with fixed capacity $B$, variable stock $b \in [0,B]$, signed work $w$, direction $\sigma \in \{\pm 1\}$, $\Delta_\sigma = E_D(u,v+\sigma a)-E_D(u,v)$, and two-sided guard $0 \le b - \Delta_\sigma \le B$, a cold one-shot trial at $X_{\mathrm{blank}}, w=0, b=B=\frac{1}{5}, \sigma=+1$ accepts $h \in \{0,1,2\}$ and refuses $h \in \{3,4\}$. Because accepted $h=0$ and refused $h \in \{3,4\}$ both produce $\Pi_{\mathrm{port}} = ((0,0),(0,0,0),0)$, the observable must include the post-contact state $(b, \sigma)$ ($(\frac{1}{5}, -1)$ for accepted $h=0$ vs $(\frac{1}{5}, +1)$ for refused $h \in \{3,4\}$). At fixed $(b, B, \sigma)$, M3 still factors through $h(p)$ and does not exclude a classical comparator with the same store and guard; multi-trial wave-reset renewal is `UNSUPPLIED`.
3. **Exact calibration-to-prediction criterion (`Theorem C1`–`Theorem C5`):**
   - **Within $Z_5$ in $\mathcal{A}_{\mathrm{lin}}$ (`Theorem C1`):** Any $2$ nonzero points of $Z_5$ determine $(b_0, b_1)$ on all of $\Pi_2$, but axis-only calibration $\{z^{(0)}, z^{(1)}, z^{(4)}\}$ (or $\Pi_2 \cap Z_I$) leaves the off-diagonal energy entry $g_{01}$ undetermined (positive-definite witness $(m_*, m_{\mathrm{off}})$ with $G_0^{(\mathrm{off})} = G_{\mathrm{source}} + \frac{2}{5}(e_0 e_1^T + e_1 e_0^T)$ in (C2)–(C3), giving $E_0(z^{(2)}) = \frac{3}{20}$ vs $\frac{1}{4}$ and $E_0(z^{(3)}) = \frac{2}{5}$ vs $\frac{3}{5}$). Calibrating any $3$ nonzero points of $Z_5$ (such as $I_3 = \{z^{(1)}, z^{(2)}, z^{(4)}\}$) uniquely determines all observables $\mathcal{O}_m$ on the held-out point $z^{(3)}$ and on all of $\Pi_2$, enforcing $b_t(z^{(3)}) = b_t(z^{(1)}) + b_t(z^{(2)})$ and $E_0(z^{(3)}) = 2E_0(z^{(1)}) + 2E_0(z^{(2)}) - \frac{1}{4}E_0(z^{(4)})$.
   - **In $\mathcal{A}_{\mathrm{aff}}$ (`Theorem C2`):** Three affinely independent points $\{z^{(0)}, z^{(1)}, z^{(4)}\}$ determine affine responses on $\Pi_2$, whereas an unconstrained $6$-parameter affine-quadratic energy function on $\Pi_2$ retains the $1$-dimensional nullspace spanned by $\Phi_{Z_5}(z_0, z_1) = z_0(z_0 - \frac{1}{2}) - 2z_1(z_0 + z_1 - 1)$ even after calibrating all $5$ points of $Z_5$.
   - **Out-of-plane $Z_I \setminus \Pi_2$ and $Z_V \setminus \Pi_2$ (`Theorem C3`):** Calibrating all of $Z_5$ (or $\Pi_2$) in $\mathcal{A}_{\mathrm{lin}}$ leaves every $s \in \mathbb{Q}^4 \setminus \Pi_2$ undetermined; since $\det R_0 = \det(-M/4) = +\frac{1}{4^4}\det M > 0$, the positive-definite isometric conjugate $m_\sharp = (R_0 J_{01}, R_1 J_{01}, J_{01}^T G_{\mathrm{source}} J_{01})$ agrees identically with $m_*$ on all of $\Pi_2$ while diverging simultaneously on all $4$ points of $Z_I \setminus \Pi_2$ and all $20$ points of $Z_V \setminus \Pi_2$.
   - **Nonlinear class $\mathcal{A}_{\mathrm{nl}}$ (`Theorem C4`):** For **every** proper subset $I \subsetneq Z_5$ (all $31$ proper subsets) and every held-out $s \in Z_5 \setminus I$, the rational polynomial Lagrange-distance indicator $L_{I,s}(z) = \prod_{a \in I} \|z-a\|^2 / \|s-a\|^2$ has strictly positive denominator $\prod_{a \in I}\|s-a\|^2 > 0$, vanishes on $I$, equals $1$ at $s$, and embeds into the complete admitted model pair $(m_*, m_{\mathrm{nl}}^{(I,s)}) \in \mathcal{A}_{\mathrm{nl}}$ in (C18a)–(C18b) (supplemented by the cubic witness $\Psi_{z^{(3)}}(z) = 2z_0(2z_0-1)z_1$ for $I_4 \to z^{(3)}$ in (C18c) and the complete model pair $(m_*, m_{\mathrm{cross}})$ with $E_{0,m_{\mathrm{cross}}} = E_{0,m_*}$ for $Z_I \to Z_V$ in (C18d)).
   - **Conditional full-span augmentation (`Theorem C5`):** Beyond $Z_5$, $\min |U_{\mathrm{ext}}| = 2$ quotient-independent directions suffice to determine $(b_0, b_1)$ on all of $\mathbb{Q}^4$, whereas an unconstrained symmetric energy matrix $G_0 \in \mathbb{Q}^{4 \times 4}_{\mathrm{sym}}$ remains undetermined under $Z_5 \cup Z_I$ (witness $(m_*, m_{\mathrm{energy\text{-}flip}})$ in (C21)) and requires $\min |U_{\mathrm{ext}}| = 7$ additional preparations (such as $U_{\mathrm{quad},7}$ in (C22)–(C24)).

### 1.2 What remains conditional, excluded, or still missing

- **Conditional premises retained:** The mixed-carrier contact $C_*$ (or its bounded-store variant $H_B$), the five-site classical source $S$, the finite Dirichlet wave/tape update $F$, and the four-stage external schedule remain explicit premises. None is compiled from native $U$ or derived from $J$.
- **Physical status `NOT_READY`:** No physical apparatus, calibration reference, sensor certificate, timing bridge, or measurement trace is supplied. All twelve Stage S qualification fields and `I_FREEZE` remain unissued debts.
- **Untouched public owners:** `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]` and `QDD-INSTRUMENT-APPARATUS` `[O]` are untouched. No public claim is registered or promoted by this note.

### 1.3 Package file index and R1/R2 scientific erratum (`A3-R1` through `A3-R6`)

To preserve `PREREG.md` line 77 (which freezes `README.md`, `CONTRACT.md`, `PREREG.md`, and `SOURCES.json` at `274a88757863f55a838068e92241af1ee23f2de4`), `README.md` has been restored byte-for-byte from `274a88757863f55a838068e92241af1ee23f2de4` in the R1 amendment, and the complete package index is housed here in `RESULT.md`:

- **Frozen preregistration files (byte-identical to `274a88757863f55a838068e92241af1ee23f2de4`):**
  - [README.md](README.md): Frozen research question, four ordered obligations, and scope/non-duplication boundary (`4943` bytes, blob `bff2283a6feda94a966c29fc08134ddf5971c184`). *Erratum note on frozen `README.md` line 17:* Line 17 of the pinned `README.md` contains the notation typo $\mathcal{A}_{\mathrm{aff}} \subset \mathcal{A}_{\mathrm{full}} \subset \mathcal{A}_{\mathrm{nl}}$. As frozen in [CONTRACT.md](CONTRACT.md) Section 2.1 and [PREREG.md](PREREG.md) Section 2 (Obligation B.1), the operative model hierarchy throughout the package is $\mathcal{A}_{\mathrm{lin}} \subset \mathcal{A}_{\mathrm{aff}} \subset \mathcal{A}_{\mathrm{nl}}$; `README.md` is restored without editing the pin.
  - [CONTRACT.md](CONTRACT.md): Self-contained mathematical definitions, carrier domains, literal equality, source families $Z_5, Z_I, Z_V$, and model hierarchy $\mathcal{A}_{\mathrm{lin}} \subset \mathcal{A}_{\mathrm{aff}} \subset \mathcal{A}_{\mathrm{nl}}$ (`13617` bytes, blob `e47f25e9edc9be150479f570ea1cc9206f8a5ce2`).
  - [PREREG.md](PREREG.md): Six frozen preregistration fields, action layer L1, and decision rules (`9339` bytes, blob `968acef67d3cb25a07ba2959ef958f4421cf8fac`).
  - [SOURCES.json](SOURCES.json): Pinned provenance manifest of all 26 read-only input files, commits, blobs, SHA-256 hashes, byte counts, and extracted mathematical constants (`16845` bytes, blob `791a34c4b95a5fc4125fa191b876824e0ee1e353`).
- **Unfrozen post-pin analytical deliverables (amended in R1 and R2):**
  - [PROOF.md](PROOF.md): Complete algebraic proofs and exact witnesses for Obligations A, B, C, and D.
  - [RESULT.md](RESULT.md): Summary of proved/conditional/missing statements, R1/R2 erratum, and 14-item exported interface.
  - [INTERFACE.json](INTERFACE.json): Machine-readable JSON serialization of the 14-item exported interface.
  - [PROMO-C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N.md](PROMO-C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N.md): Candidate statement mapping to proof sections, quantified domains, witnesses, and prospective owners, with an explicit recommendation of **NO promotion** in this round.

**Concise summary of R1/R2 scientific corrections ([R1 assignment](https://github.com/mathorn1973/twist-j/issues/1500#issuecomment-6178752881), [R2 narrow completion](https://github.com/mathorn1973/twist-j/issues/1500#issuecomment-6179502346)):**
- **`A3-R1` (Port and fifth-source coordinates, completed in R2):** Restored the inherited ordered port tuple $R = ((0,0,0), (1,1,0), (1,0,1), (0,1,1)) \in D_3^4$ and the exact fifth zero-mean reference site $y_4 = (2,0,0) \in D_3$ from `notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/CONTRACT.md` (`4302c31f07823b2a843e3702ca14620c1917b853`, line 28) in `INTERFACE.json` fields 6 and 10, `RESULT.md`, `PROOF.md` (B0), and `PROMO-C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N.md`. *R2 coordinate and source-reference erratum:* Commit `963ac3d0cc2386eddf7b636ebb817fc098697155` (R1) restored the four output ports $R$ but erroneously wrote $y_4 = (1,-1,0)$ instead of the pinned $y_4 = (2,0,0)$. With $s = \sum_{i=0}^3 z_i$, replacing $p=(2,0,0)$ by $q=(1,-1,0)$ alters the first signed cut by $b_0^{\mathrm{wrong}}(z) - b_0^{\mathrm{pin}}(z) = \frac{s}{1296}(1,-1,0,0)$ (giving $(-1416,349,354,348)/12960$ at $z = e_0/2$ instead of the inherited $(-1421,354,354,348)/12960$). Restoring $y_4 = (2,0,0)$ aligns all text exports with the preserved original $S, F, D$, response matrices, and numerical tables. In addition, R2 corrects the historical citation for the rank-one inverse and determinant of $M$ in `PROOF.md` line 375 from the nonexistent `notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/PROOF.md` to `notes/C-CLASSICAL-SIGNED-PORT-CONTRACT-N/OBSERVABILITY_CALIBRATION.md` (`1b69563af4018b08d7dc75781b12e9553a8c19c3`, line 101 / equation (O4)).
- **`A3-R2` (Narrowed Theorem B2):** Replaced the "necessary and sufficient" heading/claim in `PROOF.md` Section 2.2, `RESULT.md`, `INTERFACE.json`, and `PROMO` by three conditional witnesses against explicitly restricted comparators (M1 vs. $h$-only; M2 vs. static lookup; M3 vs. differently funded comparator), recording that M2 and M3 still factor through $h(p)$ at a fixed intervention context and do not exclude classical comparators with matched timing, memory, or store guards.
- **`A3-R3` (Complete historical $H_B$ law in M3):** Restored the full `#1495`/`#1496` state $(v, w, b, \sigma)$ with fixed capacity $B$, variable stock $b \in [0,B]$, signed work $w$, direction $\sigma \in \{\pm 1\}$, and two-sided guard $0 \le b - \Delta_\sigma \le B$ in `PROOF.md` (B7)–(B10), `RESULT.md`, `INTERFACE.json`, and `PROMO`; withdrew the unproved second-trial wave-reset claim (marking multi-trial reset `UNSUPPLIED`); and proved that distinguishing accepted $h=0$ from refused $h \in \{3,4\}$ at cold $b=B=\frac{1}{5}, \sigma=+1$ requires reading the post-contact state $(b, \sigma)$ rather than zero port/energy output alone.
- **`A3-R4` (Distinction between M2 and A2's second contact):** Corrected `RESULT.md` field 13, `INTERFACE.json`, and `PROOF.md` so M2 at $n=2$ (reading current $C_2$, giving $e_1$ at $h=0$) is kept strictly separate from Agent 2's (`#1499`) second contact at $n=3$ (reading retained delayed $d = C_{1,B}$ captured at $n=1$, giving $0$ at $h_B=0$).
- **`A3-R5` (Formula and preparation transfers):** Fixed $\det(-M/4) = +\det(M)/4^4 > 0$ in `PROOF.md` Theorem C3; fixed the `PROMO` Theorem C1 $G_0^{(\mathrm{off})}$ coefficient from $\frac{1}{5}$ to $\frac{2}{5}$ matching `PROOF.md` (C2); replaced the undefined $\psi_5$ shorthand in `PROMO` Theorem A1 with $\eta(q,r) = (\ell(q)/2, (\ell(r)+1)/2, 0, 0)$; and removed the claim in `PROOF.md` Section 4.2 that the $n=2$ table prepares $-e_0$ or $-e_1$.
- **`A3-R6` (General nonlinear construction, complete $m_{\mathrm{cross}}$, and `README.md` restoration):** Added the general rational polynomial Lagrange-distance construction $L_{I,s}(z) = \prod_{a \in I}\|z-a\|^2/\|s-a\|^2$ embedded in complete admitted model pairs $(m_*, m_{\mathrm{nl}}^{(I,s)}) \in \mathcal{A}_{\mathrm{nl}}$ for every proper subset $I \subsetneq Z_5$ and $s \in Z_5 \setminus I$ in `PROOF.md` Theorem C4 (C18a)–(C18b); completed $m_{\mathrm{cross}}$ with explicit $E_{0,m_{\mathrm{cross}}} = E_{0,m_*}$ and conservation equations in (C18d); and restored `README.md` byte-for-byte from `274a88757863f55a838068e92241af1ee23f2de4`.

---

## 2. Shared exported interface for later composition

In accordance with the assignment contract, each of the shared interface fields is stated below (and serialized in [INTERFACE.json](INTERFACE.json)), with absent items explicitly marked `UNSUPPLIED`:

```text
1. carrier:
   Composite L1 product Omega x X x Q x C_ctrl for D_NC, where
   Omega = N_0 x F_5^6, X = (Q^D x Q^D) x (Q^4)^2 x (Q^4)^2 x (Z/2Z)
   with |D| = 869, signed work ledger w in Q, and fixed 5-stage schedule
   (extended in bounded-store H_B context by fixed capacity B in Q_(>=0),
   variable stock b in [0,B] cap Q, and direction sigma in {-1,+1});
   model parameter carrier A_lin = Q^(4x4) x Q^(4x4) x Q^(4x4)_sym (dim_Q = 42)
   with Pi_2-identifiable quotient I_lin(Pi_2) (dim_Q = 19) and kernel K_lin(Pi_2) (dim_Q = 23).

2. literal equality:
   Exact coordinate equality in F_5^4 (625 preparations), N_0 x F_5^6 (native states),
   Q^4 (sources and signed port outputs b_0, b_1), Q (energies E_0, E_1, E_2, w, b, B),
   {-1,+1} (direction sigma), and pointwise equality of observable maps O_m(z) with tolerance 0;
   no sign quotient, normalization, or projectivization.

3. native projection:
   Residue sum h(p) = sum_(i=0)^3 p_i mod 5 on p in F_5^4 (5 fibres F_h of size 125 each);
   first-tick receiver C_1(h) in {(0,4),(1,4),(1,0),(2,0),(0,1)} at n=1;
   second-tick receiver C_2(h) in {(0,1),(0,1),(4,0),(3,0),(1,4)} at n=2 (merging h=0,1; still factors through h).

4. source family:
   Under ell(0,1,2,3,4) = (0,1,2,-2,-1) and eta(q,r) = (ell(q)/2, (ell(r)+1)/2, 0, 0),
   native-induced 5-point set at n=1 is Z_5 = {(0,0,0,0), (1/2,0,0,0), (1/2,1/2,0,0), (1,1/2,0,0), (0,1,0,0)}
   with span_Q(Z_5) = aff_Q(Z_5) = Pi_2 = Q e_0 + Q e_1 (dim_Q = 2);
   Z_5 cap Z_I = {0, e_1} (2/9), Z_5 cap Z_V = empty (0/24),
   Pi_2 cap Z_I = {0, +-e_0, +-e_1} (5/9), Pi_2 cap Z_V = {+-e_0 +- e_1} (4/24);
   at n=2, distinct sources are {e_1, (-1/2,1/2,0,0), (-1,1/2,0,0), (1/2,0,0,0)} (neither n=1 nor n=2 prepares -e_0 or -e_1);
   out-of-plane directions in Q^4 \ Pi_2 are UNSUPPLIED by eta(F_5^2).

5. common readiness:
   Native receiver C_0 = (0,1) at n=0; classical cold state X_blank = ((0,0),(0,0),(0,0),0);
   work ledger w = 0; controller stage = 0 (and in cold H_B context, b = B = 1/5, sigma = +1).
   Renewal/reset after stage 4 is UNSUPPLIED.

6. admitted primitives and origin of each permission:
   - Unchanged native U and involutions g_0..g_4: inherited from Public Canon v101.
   - Classical stencil B, Dirichlet L_D, 5-site source S, 4-port g_j=2 coupler on ordered ports
     R = ((0,0,0),(1,1,0),(1,0,1),(0,1,1)) in D_3^4 (with y_4 = (2,0,0)), and two-tape F:
     inherited conditional premise from #1484/#1485 (4302c31f07823b2a843e3702ca14620c1917b853).
   - Balanced lift eta(q,r) = (ell(q)/2, (ell(r)+1)/2, 0, 0) and one-shot mixed contact C_* at n=1:
     inherited conditional premise from #1486/#1489 (7b3fa47c0223bd99fce977de6ea58d484e257033).
   - Bounded-store contact involution H_B with (w, b, B, sigma) and guard 0 <= b - Delta_sigma <= B:
     inherited read-only premise from #1495/#1496 (b7636a334b09fcc68422bcd6cc6e15334d416c59).
   - Native compilation of C_* or H_B, physical transducer realization, negative-axis preparation (-e_0,-e_1),
     and out-of-plane source writing: UNSUPPLIED.

7. forward map:
   On Z_5 (and Pi_2), O_m(z) = (A_0 z, A_1 z, (E_0(z), E_1(z), E_2(z)));
   at reference m_*, b_0 = R_0 z = -(1/4)Mz, b_1 = R_1 z = (1/2)Qz - (1/4)Kz + (1/8)JMz,
   E_0(z) = (1/2)z^T (I_4 - 11^T/5) z;
   within Z_5, calibrating I_3 = {z^(1), z^(2), z^(4)} determines z^(3) via
   b_t(z^(3)) = b_t(z^(1)) + b_t(z^(2)) and E_0(z^(3)) = 2E_0(z^(1)) + 2E_0(z^(2)) - (1/4)E_0(z^(4)).

8. inverse and its exact domain:
   - Classical first-cut inverse z = -4 M^-1 b_0 on all Q^4, with det(R_0) = det(-M/4) = +det(M)/4^4 > 0
     (inherited from #1484/#1485).
   - Prepared-image whole-run inverse on the 625-element image at n=3, stage=4 with piston-sum guard
     (inherited from #1486/#1489 and audited in #1491/#1492).
   - Calibration-to-parameter inverse (A9)-(A10) on I_3 = {z^(1), z^(2), z^(4)} -> I_lin(Pi_2) (dim 19),
     and conditional full-space inverse on Z_5 union U_quad,7 -> A_lin (dim 42) in (C23)-(C24).
   - Inverse on K_lin(Pi_2) (dim 23) from Z_5 data alone: IMPOSSIBLE (proved non-identifiable).

9. clock access, program, stage and any driver/history state:
   Fixed 5-stage external schedule program = (U, C_*, U x F, U x F, STOP) with stage in {0..4},
   native counter n in {0,1,2,3} using theta_0,theta_1,theta_2 = 0,1,1, and classical tape pointer k in Z/2Z.
   Autonomous stop/renewal and physical SI clock bridge: UNSUPPLIED.

10. signed output ports and record order:
    Four marked ports R = (y_0, y_1, y_2, y_3) = ((0,0,0), (1,1,0), (1,0,1), (0,1,1)) in D_3^4
    (with fifth zero-mean reference site y_4 = (2,0,0) in D_3) and g_j = 2;
    chronological record Y_2 = (b_0, b_1) in (Q^4)^2 extracted from final outgoing tape B_tape = (b_1, b_0)
    as ((B_tape)_1, (B_tape)_0), with b_1 acquired from continuing wave transition F (never synthesized from b_0).

11. energy store, boundary, resources and finite-use guarantee:
    Bookkeeping invariant E_full - w conserved across C_* and F^2 on the declared classical boundary,
    with retained tape energy 2||b_0||^2 + 2||b_1||^2 counted once inside E_full.
    Under historical H_B (#1495/#1496), fixed capacity B in Q_(>=0), variable stock b in [0,B] cap Q,
    signed work w in Q, direction sigma in {-1,+1}, Delta_sigma = E_D(u,v+sigma*a)-E_D(u,v),
    accept iff 0 <= b - Delta_sigma <= B, transition (v,w,b,sigma) -> (v+sigma*a, w+Delta_sigma, b-Delta_sigma, -sigma)
    on accept and identity on refusal; at cold b=B=1/5, sigma=+1, accepted h=0 and refused h in {3,4}
    both yield zero port/energy/work output and require (b,sigma) readout to distinguish.
    Native compilation of H_B, physical energy store, controller/sensor/reset energy accounts,
    and multi-trial wave-reset renewal: UNSUPPLIED.

12. physical interpretation and unpassed layer bridges:
    L1 mathematical state and prospective qualification specification only.
    All 12 Stage S qualification fields and I_FREEZE are UNSUPPLIED (physical status NOT_READY).
    L1-to-L4/L5/L6 bridges, occurrence/Born sampling, and SI calibration remain UNPASSED / OPEN.

13. assumptions required from another component (and non-circular test observables):
    - Historical H_B bounded-store context (#1495/#1496) and Agent 1 (#1498):
      Agent 1 keeps native compilation of H_B UNSUPPLIED/STOP on the frozen primitive grammar.
      In the conditional H_B specification (#1495/#1496), a cold one-shot test at X_blank, w=0,
      b=B=1/5, sigma=+1 (Witness M3, Theorem B2(3)) accepts h in {0,1,2} and refuses h in {3,4}
      against a differently funded comparator, provided the observable includes post-contact (b,sigma)
      to distinguish accepted h=0 ((1/5,-1)) from refused h in {3,4} ((1/5,+1)); does not exclude
      a classical comparator with the same (b,B,sigma) guard.
    - Agent 2 (#1499, two-use control and archive continuation) vs. Witness M2:
      Witness M2 (single contact shifted to n=2 reading current C_2, giving z_(n=2)^(0) = e_1 at h=0)
      is a separate prospective intervention against a static lookup comparator and is NOT equivalent
      to Agent 2's second contact, which occurs at n=3 and reads the retained delayed label d = C_(1,B)
      captured at n=1 (giving eta(d) = 0 at h_B = 0). Any future joint test with Agent 2 must use
      A2's actual delayed source z_B = eta(C_(1,B)) at n=3 and continuing wave/tape state
      (b_2 = D_2(z_A) + R_0 z_B, b_3 = D_3(z_A) + R_1 z_B - (J_p/2)c_1), and requires a separately
      specified direction/funding adapter before combining with H_B.
    - Future out-of-plane source adapter:
      requires 2 quotient-independent directions u^(2), u^(3) with u^(2)_2 u^(3)_3 != u^(2)_3 u^(3)_2
      (for linear response) and 7 preparations U_quad,7 (for unconstrained symmetric quadratic energy).

14. conservative verdict and finite rejection witnesses:
    Verdict: DELIVERED_CANDIDATE (candidate-T and candidate-D at L1 scope; physical status NOT_READY;
    mechanism attribution on Pi_port alone against a matched classical clone D_cl is INDISTINGUISHABLE_ON_PORT;
    M1-M3 are conditional witnesses against restricted comparator classes only).
    Exact finite rejection witnesses:
    - Axis-only Z_5 energy witness (m_*, m_off) in (C2)-(C3) with G_0^(off) = G_source + (2/5)(e_0 e_1^T + e_1 e_0^T):
      agrees on {z^(0), z^(1), z^(4)} and Pi_2 cap Z_I, diverges on E_0(z^(2)) (3/20 vs 1/4) and E_0(z^(3)) (2/5 vs 3/5).
    - Affine-quadratic energy null witness Phi_Z5 in (C12)-(C13): vanishes on all 5 points of Z_5,
      diverges on +e_0 (+1/2), -e_0 (+3/2), -e_1 (-4), and e_0 +- e_1 (-3/2).
    - Out-of-plane witness (m_*, m_sharp) in (C15)-(C17): agrees on all of Pi_2 (incl. Z_5),
      diverges on all 4 points of Z_I \ Pi_2 and all 20 points of Z_V \ Pi_2 (e.g. at e_0 + e_2,
      12960 b_0 = (-2144,1416,-2124,1392) vs (-3540,0,3540,0) and E_0 = 3/5 vs 1).
    - General nonlinear witness (m_*, m_nl^(I,s)) in (C18a)-(C18b) via L_(I,s)(z) = prod_(a in I) ||z-a||^2/||s-a||^2
      for every proper subset I subsetneq Z_5 and s in Z_5 \ I, cubic witness Psi_(z^(3)) in (C18c),
      and complete model pair (m_*, m_cross) in (C18d) for Z_I -> Z_V.
    - Full-Z_I energy witness (m_*, m_energy-flip) in (C21): agrees on all of Z_5 union Z_I for
      (b_0,b_1,E_0), diverges on E_0(sigma e_i + rho e_k) by +-2/5 on all 16 mixed points of Z_V.
```

---

## 3. Executed administrative checks versus non-executed scientific code

- **Scientific code / verifiers executed:** `NONE` (`NOT_RUN`). No `verify.py`, `EXPECTED.txt`, or `RUN.md` is included or claimed.
- **Repository administrative checks executed locally on clean clone:**
  - `python3 tools/check_policy.py` (`POLICY PASS`)
  - `python3 -m unittest discover -s tools -p 'test_*.py'` (`Ran 188 tests ... OK`)
  - `python3 tools/check_canon.py` (`CANON PASS v101 claims=514`)
  - `python3 tools/check_ledger.py` (`LEDGER PASS`)
  - `python3 tools/check_gate_contract.py` (`GATE CONTRACT PASS`)
  - `python3 tools/check_verifier.py --base 8b91a935c426036e00ecb300019fd94734addeec` (`VERIFY NOT APPLICABLE`)
  - `python3 tools/check_reproduce.py --base 8b91a935c426036e00ecb300019fd94734addeec` (`REPRODUCE NOT APPLICABLE`)
  - `git diff --check 8b91a935c426036e00ecb300019fd94734addeec...HEAD` (clean)
  - `git diff --name-only 8b91a935c426036e00ecb300019fd94734addeec...HEAD` (strictly inside `notes/C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N/`)
