# Result and exported interface: `C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N`

**NON-CANONICAL / L1 analytical result / 2026-10-14.**
Original work Apache-2.0, A. M. Thorn.
Reservation: [#1500](https://github.com/mathorn1973/twist-j/issues/1500), dispatched under [#1497](https://github.com/mathorn1973/twist-j/issues/1497).

```text
candidate_id:               C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N
slot:                       A3
branch:                     incubation/C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N
allowed_path:               notes/C-FIVE-SOURCE-PREDICTIVE-SEPARATION-N/
authority_base:             8b91a935c426036e00ecb300019fd94734addeec (Public Canon v101 ACTIVE)
preregistration_commit:     274a88757863f55a838068e92241af1ee23f2de4
proof_status:               AUTHORED_PROOF; SELF_REVIEWED; NOT_INDEPENDENTLY_REVIEWED
scientific_code_status:     NONE / NOT_RUN (analytical proof-only round)
physical_status:            NOT_READY (no laboratory instance or Stage S certificates supplied)
overall_verdict:            DELIVERED_CANDIDATE (conditional candidate-T and candidate-D at L1 scope;
                            exact within-plane determination on Z5, exact out-of-plane underdetermination
                            with positive-definite witnesses, and exact classical-clone indistinguishability bound)
```

---

## 1. Summary of proved, conditional, excluded, and still-missing statements

### 1.1 What is proved (conditional candidate-T at L1 scope, [PROOF.md](PROOF.md))

1. **Rank-two source span and preparation mismatch (`Theorem A1`, `Proposition A2`, `Theorem A3`, `Theorem A4`):**
   - The five native-accessible encodings $Z_5 = \{z^{(0)}, z^{(1)}, z^{(2)}, z^{(3)}, z^{(4)}\}$ span the $2$-dimensional plane $\Pi_2 = \mathbb{Q}e_0 \oplus \mathbb{Q}e_1$ both linearly and affinely ($\operatorname{span}_{\mathbb{Q}}(Z_5) = \operatorname{aff}_{\mathbb{Q}}(Z_5) = \Pi_2$, $\dim_{\mathbb{Q}} = 2$), and even the full $25$-point receiver image $\eta(\mathbb{F}_5^2)$ is contained in $\Pi_2$.
   - Literally, $Z_5 \cap Z_I = \{0, e_1\}$ ($2$ of $9$) and $Z_5 \cap Z_V = \emptyset$ ($0$ of $24$); at the subspace level, $\Pi_2 \cap Z_I = \{0, \pm e_0, \pm e_1\}$ ($5$ of $9$) and $\Pi_2 \cap Z_V = \{\pm e_0 \pm e_1\}$ ($4$ of $24$), leaving $4$ identification sources and $20$ validation sources outside $\Pi_2$.
   - Adjoining an external source set $U_{\mathrm{ext}} \subset \mathbb{Q}^4$ spans $\mathbb{Q}^4$ together with $Z_5$ if and only if $\pi_{23}(U_{\mathrm{ext}})$ spans $\mathbb{Q}^2$, so $\min |U_{\mathrm{ext}}| = 2$ quotient-independent directions ($u^{(2)}_2 u^{(3)}_3 - u^{(2)}_3 u^{(3)}_2 \ne 0$) are necessary and sufficient.
   - Restricting the $42$-parameter linear/quadratic model class $\mathcal{A}_{\mathrm{lin}} = \{(A_0, A_1, G_0)\}$ to $\Pi_2$ identifies the $19$-dimensional subspace $(A_0^{(01)}, A_1^{(01)}, G_{00})$ and annihilates the $23$-dimensional kernel $\mathcal{K}_{\mathrm{lin}}(\Pi_2)$ ($8$ columns in $A_0^{(23)}$, $8$ in $A_1^{(23)}$, $7$ entries in $(G_{01}, G_{11})$).
2. **Ideal classical clone indistinguishability and separating interventions (`Theorem B1`, `Theorem B2`):**
   - Any ordinary rational classical wave/port comparator $D_{\mathrm{cl}}$ implementing the same $(S, F, \eta, X_{\mathrm{blank}}, \Pi_{\mathrm{port}})$ produces byte-identical signed port outputs $(b_0, b_1)$, wave/tape energies $(E_0, E_1, E_2)$, and work ledger $w$ to $D_{\mathrm{NC}}$ on all $625$ native inputs $p \in \mathbb{F}_5^4$ and on any extended source set $\mathcal{Z} \subseteq \mathbb{Q}^4$ (including full $\mathbb{Q}^4$ span).
   - Genuine mechanism separation between $D_{\mathrm{NC}}$ and an $h$-only classical clone $D_{\mathrm{cl}}$ requires an intervention outside fixed-$n=1$ port readout: (M1) reading the retained native checkpoint $x_3(p)$ across the $125$-element same-$h$ fibres $\mathcal{F}_h$ (witness $p^{(0,a)}=(0,0,0,0)$ vs $p^{(0,b)}=(1,4,0,0)$ in (B3)); (M2) shifting the contact boundary from $n=1$ to $n=2$, where $D_{\mathrm{NC}}$ merges $h=0,1 \mapsto e_1$ (giving $12960\,b_0 = (698,-2832,708,696) \ne 0$ at $h=0$) and flips $h=2,3$ to negative $e_0$ amplitudes $(-\frac{1}{2},\frac{1}{2},0,0), (-1,\frac{1}{2},0,0)$; or (M3) bounded-store exhaustion under a finite energy store $B$.
3. **Exact calibration-to-prediction criterion (`Theorem C1`–`Theorem C5`):**
   - **Within $Z_5$ in $\mathcal{A}_{\mathrm{lin}}$ (`Theorem C1`):** Any $2$ nonzero points of $Z_5$ determine $(b_0, b_1)$ on all of $\Pi_2$, but axis-only calibration $\{z^{(0)}, z^{(1)}, z^{(4)}\}$ (or $\Pi_2 \cap Z_I$) leaves the off-diagonal energy entry $g_{01}$ undetermined (witness $(m_*, m_{\mathrm{off}})$ in (C2)–(C3) with $E_0(z^{(2)}) = \frac{3}{20}$ vs $\frac{1}{4}$ and $E_0(z^{(3)}) = \frac{2}{5}$ vs $\frac{3}{5}$). Calibrating any $3$ nonzero points of $Z_5$ (such as $I_3 = \{z^{(1)}, z^{(2)}, z^{(4)}\}$) uniquely determines all observables $\mathcal{O}_m$ on the held-out point $z^{(3)}$ and on all of $\Pi_2$, enforcing the exact parameter-free identities $b_t(z^{(3)}) = b_t(z^{(1)}) + b_t(z^{(2)})$ and $E_0(z^{(3)}) = 2E_0(z^{(1)}) + 2E_0(z^{(2)}) - \frac{1}{4}E_0(z^{(4)})$.
   - **In $\mathcal{A}_{\mathrm{aff}}$ (`Theorem C2`):** Three affinely independent points $\{z^{(0)}, z^{(1)}, z^{(4)}\}$ determine affine responses on $\Pi_2$, whereas an unconstrained $6$-parameter affine-quadratic energy function on $\Pi_2$ retains the $1$-dimensional nullspace spanned by $\Phi_{Z_5}(z_0, z_1) = z_0(z_0 - \frac{1}{2}) - 2z_1(z_0 + z_1 - 1)$ even after calibrating all $5$ points of $Z_5$.
   - **Out-of-plane $Z_I \setminus \Pi_2$ and $Z_V \setminus \Pi_2$ (`Theorem C3`):** Calibrating all of $Z_5$ (or $\Pi_2$) in $\mathcal{A}_{\mathrm{lin}}$ leaves every $s \in \mathbb{Q}^4 \setminus \Pi_2$ undetermined; the single positive-definite isometric conjugate $m_\sharp = (R_0 J_{01}, R_1 J_{01}, J_{01}^T G_{\mathrm{source}} J_{01})$ agrees identically with $m_*$ on all of $\Pi_2$ while diverging simultaneously on all $4$ points of $Z_I \setminus \Pi_2$ and all $20$ points of $Z_V \setminus \Pi_2$.
   - **Nonlinear class $\mathcal{A}_{\mathrm{nl}}$ (`Theorem C4`):** The cubic polynomial $\Psi_{z^{(3)}}(z) = 2z_0(2z_0 - 1)z_1$ vanishes on $\{z^{(0)}, z^{(1)}, z^{(2)}, z^{(4)}\}$ and on all $9$ points of $Z_I$ while equaling $1$ at $z^{(3)}$.
   - **Conditional full-span augmentation (`Theorem C5`):** Beyond $Z_5$, $\min |U_{\mathrm{ext}}| = 2$ quotient-independent directions suffice to determine $(b_0, b_1)$ on all of $\mathbb{Q}^4$, whereas an unconstrained symmetric energy matrix $G_0 \in \mathbb{Q}^{4 \times 4}_{\mathrm{sym}}$ remains undetermined under $Z_5 \cup Z_I$ (witness $(m_*, m_{\mathrm{energy\text{-}flip}})$ in (C21)) and requires $\min |U_{\mathrm{ext}}| = 7$ additional preparations (such as $U_{\mathrm{quad},7}$ in (C22)).

### 1.2 What remains conditional, excluded, or still missing

- **Conditional premises retained:** The mixed-carrier contact $C_*$ (or its bounded-store variant $H_B$), the five-site classical source $S$, the finite Dirichlet wave/tape update $F$, and the four-stage external schedule remain explicit premises. None is compiled from native $U$ or derived from $J$.
- **Physical status `NOT_READY`:** No physical apparatus, calibration reference, sensor certificate, timing bridge, or measurement trace is supplied. All twelve Stage S qualification fields and `I_FREEZE` remain unissued debts.
- **Untouched public owners:** `QUADRATIC-MEMORY-NATIVE-CONTACT` `[O]` and `QDD-INSTRUMENT-APPARATUS` `[O]` are untouched. No public claim is registered or promoted by this note.

---

## 2. Shared exported interface for later composition

In accordance with the assignment contract, each of the 13 shared interface fields is stated below (and serialized in [INTERFACE.json](INTERFACE.json)), with absent items explicitly marked `UNSUPPLIED`:

```text
1. carrier:
   Composite L1 product Omega x X x Q x C_ctrl for D_NC, where
   Omega = N_0 x F_5^6, X = (Q^D x Q^D) x (Q^4)^2 x (Q^4)^2 x (Z/2Z)
   with |D| = 869, work ledger w in Q, and fixed 5-stage schedule;
   model parameter carrier A_lin = Q^(4x4) x Q^(4x4) x Q^(4x4)_sym (dim_Q = 42)
   with Pi_2-identifiable quotient I_lin(Pi_2) (dim_Q = 19) and kernel K_lin(Pi_2) (dim_Q = 23).

2. literal equality:
   Exact coordinate equality in F_5^4 (625 preparations), N_0 x F_5^6 (native states),
   Q^4 (sources and signed port outputs b_0, b_1), Q (energies E_0, E_1, E_2, w),
   and pointwise equality of observable maps O_m(z) with tolerance 0;
   no sign quotient, normalization, or projectivization.

3. native projection:
   Residue sum h(p) = sum_(i=0)^3 p_i mod 5 on p in F_5^4 (5 fibres F_h of size 125 each);
   first-tick receiver C_1(h) in {(0,4),(1,4),(1,0),(2,0),(0,1)} at n=1;
   second-tick receiver C_2(h) in {(0,1),(0,1),(4,0),(3,0),(1,4)} at n=2 (merging h=0,1).

4. source family:
   Native-induced 5-point set Z_5 = {(0,0,0,0), (1/2,0,0,0), (1/2,1/2,0,0), (1,1/2,0,0), (0,1,0,0)}
   with span_Q(Z_5) = aff_Q(Z_5) = Pi_2 = Q e_0 + Q e_1 (dim_Q = 2);
   Z_5 cap Z_I = {0, e_1} (2/9), Z_5 cap Z_V = empty (0/24),
   Pi_2 cap Z_I = {0, +-e_0, +-e_1} (5/9), Pi_2 cap Z_V = {+-e_0 +- e_1} (4/24);
   out-of-plane directions in Q^4 \ Pi_2 are UNSUPPLIED by eta(F_5^2).

5. common readiness:
   Native receiver C_0 = (0,1) at n=0; classical cold state X_blank = ((0,0),(0,0),(0,0),0);
   work ledger w = 0; controller stage = 0. Renewal/reset after stage 4 is UNSUPPLIED.

6. admitted primitives and origin of each permission:
   - Unchanged native U and involutions g_0..g_4: inherited from Public Canon v101.
   - Classical stencil B, Dirichlet L_D, 5-site source S, 4-port g_j=2 coupler, and two-tape F:
     inherited premise from #1484/#1485 (4302c31f07823b2a843e3702ca14620c1917b853).
   - Balanced lift eta(q,r) and one-shot mixed contact C_* at n=1:
     inherited conditional premise from #1486/#1489 (7b3fa47c0223bd99fce977de6ea58d484e257033).
   - Native compilation of C_*, physical transducer realization, and out-of-plane source writing:
     UNSUPPLIED.

7. forward map:
   On Z_5 (and Pi_2), O_m(z) = (A_0 z, A_1 z, (E_0(z), E_1(z), E_2(z)));
   at reference m_*, b_0 = R_0 z = -(1/4)Mz, b_1 = R_1 z = (1/2)Qz - (1/4)Kz + (1/8)JMz,
   E_0(z) = (1/2)z^T (I_4 - 11^T/5) z;
   within Z_5, calibrating I_3 = {z^(1), z^(2), z^(4)} determines z^(3) via
   b_t(z^(3)) = b_t(z^(1)) + b_t(z^(2)) and E_0(z^(3)) = 2E_0(z^(1)) + 2E_0(z^(2)) - (1/4)E_0(z^(4)).

8. inverse and its exact domain:
   - Classical first-cut inverse z = -4 M^-1 b_0 on all Q^4 (inherited from #1484/#1485).
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
    Four marked ports R = (y_0,y_1,y_2,y_3) with g_j = 2; chronological record Y_2 = (b_0, b_1) in (Q^4)^2
    extracted from final outgoing tape B_tape = (b_1, b_0) as ((B_tape)_1, (B_tape)_0),
    with b_1 acquired from continuing wave transition F (never synthesized from b_0).

11. energy store, boundary, resources and finite-use guarantee:
    Bookkeeping invariant E_full - w conserved across C_* and F^2 on the declared classical boundary,
    with retained tape energy 2||b_0||^2 + 2||b_1||^2 counted once inside E_full.
    Positive bounded physical energy store, native/controller/sensor/reset energy accounts,
    and multi-trial renewal: UNSUPPLIED (exported to #1495/#1496, Agent 1, and Agent 2).

12. physical interpretation and unpassed layer bridges:
    L1 mathematical state and prospective qualification specification only.
    All 12 Stage S qualification fields and I_FREEZE are UNSUPPLIED (physical status NOT_READY).
    L1-to-L4/L5/L6 bridges, occurrence/Born sampling, and SI calibration remain UNPASSED / OPEN.

13. assumptions required from another component (and non-circular test observables):
    - From Agent 1 (#1498, H_B native admission boundary / finite store B):
      requires an explicit native/admissible gate specification or bounded store B in Q_(>=0)
      with forward/no-op threshold rule; tested non-circularly by Intervention M3 (Theorem B2(3))
      at B = 1/5 (admitting h in {0,1,2} and blocking h in {3,4}) without refitting R_0, R_1.
    - From Agent 2 (#1499, two-use control and archive continuation):
      requires an explicit multi-use schedule, pointer/tape archive continuation, and second-contact
      timing n_2; tested non-circularly by Intervention M2 (Theorem B2(2), contact at n=2 merging
      h=0,1 -> e_1 and shifting h=2,3 to negative e_0 amplitudes) and warm-tape continuation F^4.
    - From a future out-of-plane source adapter:
      requires 2 quotient-independent directions u^(2), u^(3) with u^(2)_2 u^(3)_3 != u^(2)_3 u^(3)_2
      (for linear response) and 7 preparations U_quad,7 (for unconstrained symmetric quadratic energy).

14. conservative verdict and finite rejection witnesses:
    Verdict: DELIVERED_CANDIDATE (candidate-T and candidate-D at L1 scope; physical status NOT_READY;
    mechanism attribution on Pi_port alone is INDISTINGUISHABLE_ON_PORT).
    Exact finite rejection witnesses:
    - Axis-only Z_5 energy witness (m_*, m_off) in (C2)-(C3): agrees on {z^(0), z^(1), z^(4)} and
      Pi_2 cap Z_I, diverges on E_0(z^(2)) (3/20 vs 1/4) and E_0(z^(3)) (2/5 vs 3/5).
    - Affine-quadratic energy null witness Phi_Z5 in (C12)-(C13): vanishes on all 5 points of Z_5,
      diverges on +e_0 (+1/2), -e_0 (+3/2), -e_1 (-4), and e_0 +- e_1 (-3/2).
    - Out-of-plane witness (m_*, m_sharp) in (C15)-(C17): agrees on all of Pi_2 (incl. Z_5),
      diverges on all 4 points of Z_I \ Pi_2 and all 20 points of Z_V \ Pi_2 (e.g. at e_0 + e_2,
      12960 b_0 = (-2144,1416,-2124,1392) vs (-3540,0,3540,0) and E_0 = 3/5 vs 1).
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
