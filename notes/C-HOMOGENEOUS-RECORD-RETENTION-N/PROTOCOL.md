# Prospective Protocol: `C-HOMOGENEOUS-RECORD-RETENTION-N`

**PUBLIC, NON-CANONICAL. Preregistration frozen before the first formal
execution of the exact verifier.**

License: Apache-2.0.

---

## 1. Purpose and type

Successor to `HOMOGENEOUS-CAPTURE-CURRENT-RECORD [T]` (Public Canon v105),
whose remaining interpretation boundary lists "a quantitative finite-interval
or future-uniform retention bound" as not supplied. This package asks how long
the receiver of that law holds a coherently written record, and with what
error, for an explicitly declared ideal selected success component.

It is a non-canonical analytical package with a minimal standard-library
reproduction (`notes/C-HOMOGENEOUS-RECORD-RETENTION-N/` and
`reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/`, executed through
`tools/check_reproduce.py`), not a new `probes/P-...` registration, and it
changes no file under `canon/`. It creates no Canon claim, status or release.

## 2. Authority and inputs

- Authority: `mathorn1973/twist-j` main
  `892a0b11089d34e241e1eb76d2c03247022d18e6` = tag `canon-v105`; `STATUS.md`
  declares Public Canon v105, content commit
  `b8cdfd6ea58ae798545bc6000c817147fa0f0dcc`, `canon/CANON.md` SHA-256
  `73894f331dac3226fe30c86f1ccd893bc2761b0220557e0bfb374d049aa2fa31`,
  1295029 bytes (verified locally before this pin).
- Scientific inputs: only the public law, preparation and certified constants
  of `HOMOGENEOUS-CAPTURE-CURRENT-RECORD` in `canon/CANON.md` and in
  `notes/C-HOMOGENEOUS-CAPTURE-CURRENT-RECORD-N/`. Exact file identities are in
  `SOURCES.tsv`.
- Newer authority recorded: the assignment for this work was prepared against
  Public Canon v104 and a non-public source of the same homogeneous
  construction. Public Canon v105 has since integrated that construction. This
  package uses the public v105 statements only; no non-public material was read
  or copied. Any composition with a non-public source requires its own explicit
  map.
- Imported certified constants (v105 `verify.py` Group 1, unchanged):
  $M_0 = 440/53$ (resolvent bound on $|w-e^{-ig}| = 1/8$ at $P = 0$) and
  $N_{\min} = 8424/11449$ ($|\langle b_0,\chi_b(P)\rangle|^2$ for $|P|\le1/12$),
  and the formulas $W(P) = e^{iPQ}W(0)$, $|u_{+,1}|^2 = (1-v)/2$.

## 3. Preregistration fields

1. **Equation.** The record-location identity
   $\|(I-R_1)U_{\rm rec}^n\mathcal T(\chi\otimes e_1\otimes\Phi)\|^2 =
   (1-\|\phi_1\|^2)\|\mathbf 1_{c<z}U^n\chi\|^2$ and the target quantity
   $$\sup_{n\ge T}\ \sup_{\Phi}\ \|(I-R_1)\,U_{\rm rec}^n\,\Omega_{{\rm rec},+}\,
   \mathcal T_+(\varphi\otimes\Phi)\|,\qquad\varphi\in\mathcal F,$$
   bounded by $\varepsilon(T) = \bar\delta(T)+\bar\eta(T)$ as defined in
   `PROOF.md` §6.
2. **Code.** `reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/verify.py`, SHA-256
   `a349d3fc0711a59e6174a2534b47c62df766b1f6ab82e0e215ebcd8a596f26c7`,
   33053 bytes. Python standard library only, exact integers and fractions, no
   floating point, no file reads, no network, no randomness.
3. **Carrier and model.** The unchanged v105 one-pair, one-carrier,
   one-receiver law $U = U_0C$, $U_{\rm rec} = \mathcal T(U\otimes I)
   \mathcal T^*$, receiver $z = 100$, coded memory $\mathcal D$ (26 labels),
   arbitrary reference $\mathcal H_{\rm ref}$, phase-zero macrosteps. No lock,
   archive, reset, second carrier or additional receiver is added.
   - Memory projection: $R_1 = I\otimes|d_1\rangle\langle d_1|\otimes I$.
   - Success-state family $\mathcal F$: product outgoing states
     $\varphi = \chi\otimes\pi\otimes p_1$ with
     $\hat\chi(P) = A_g\theta_gb(P/p_1)\Pi_b(P)\chi_0$,
     $\hat\pi(k) = A_h\theta_hb((k-k_0)/w)P_+(k)e_2$,
     $b(t) = (1-t^2)^N\mathbf 1_{|t|\le1}$, unimodular $\theta$'s, and joint
     translates with object shift $R_c\le0$ and pulse shift $x_c\ge0$.
   - Normalization: $\|\chi\| = \|\pi\| = 1$, hence $\|\varphi\| = 1$; the
     success state is $\Psi_+ = \mathcal T_+(\varphi\otimes\Phi)\in
     \operatorname{Ran}Q_{\rm full}$, normalized inside the declared family.
     This is distinguished from the full unpostselected v105 input, whose exact
     wrong-memory probability is stated separately (`PROOF.md` Corollary 1.2)
     and is not bounded by this certificate. The family is not asserted to
     contain the normalized v105 selected component.
4. **Systematics.** Rational upper and lower bounds for $\sqrt5$, $\pi$
   ($333/106<\pi<355/113$), $e^\rho$ (Taylor with remainder), square roots
   (integer square roots at scale $10^{40}$); Cauchy estimates on complex disks;
   $L^1$ norms of polynomial derivatives bounded through coefficient sums;
   Cook's sum without cancellation. All are one-sided and conservative; no
   rounding is in the unsafe direction. The finite exact simulation of the local
   law runs in $\mathbb Z[i][\zeta_5]$ with integer scaling $125$ per macrostep.
5. **Failure thresholds (falsifiers).**
   - F1. Any exact identity of Groups 1–4 fails: the verifier aborts and the
     corresponding theorem (or its audit) is refuted at the stated instance.
   - F2. Any sector or analytic-constant condition of Group 5 fails
     (Neumann product $\ge1$, energy spread $>h$, $v_b\ge v_{\min}$, window not
     in $(-\pi,0)$, disk reaching the arccos branch points): the family is not
     certified as a success family and the quantitative target is void.
   - F3. The certified $\varepsilon(10^6)$ exceeds $1/100$: the verifier
     prints `NOT ACHIEVED` and the quantitative target is reported as not
     achieved at the frozen tolerance. Thresholds and parameters never move
     after this pin.
6. **Action layer.** L1 only (state and law on the declared Hilbert space). No
   lift to L2–L6, no occurrence, detector, sampling or Born statement.

## 4. Frozen parameters

| Symbol | Value | Role |
|---|---|---|
| $z$ | $100$ | receiver site (v105) |
| $h$ | $1/1000$ | half width of $I_E$ (v105) |
| $p_1$ | $1/1000$ | object momentum half width |
| $w$ | $1/1000$ | pulse momentum half width around $k_0$ |
| $N$ | $5$ | bump order and number of integrations by parts |
| $\rho_P$ | $1/10$ | complex radius for the bound branch |
| $\rho_k$ | $3/10$ | complex radius for the pulse band |
| $T$ | $10^6$ macrosteps ($2\cdot10^6$ microticks) | start of the future-uniform window |
| $L$ | $\infty$ (all $n\ge T$) | duration |
| $\varepsilon_{\rm retain}$ | $1/100$ | tolerance on $\|(I-R_1)\psi_n\|$ (probability $10^{-4}$) |
| modulus table | $T\in\{2\cdot10^5,5\cdot10^5,10^6,10^7\}$ | informational output |
| exact simulation | $4$ macrosteps, labels $\{0,1,2\}$, two-dimensional reference | Group 2 |
| dark record | $5$ macrosteps physical, $9$ object steps | Group 4 |

## 5. Gates

| Group | Content | Pass criterion |
|---|---|---|
| 1 `LABEL_ALGEBRA` | exchange $\mathsf J$ on all $26^2$ label pairs; wrong-memory, full-record and old-information identities on an entangled example | all exact equalities |
| 2 `PHYSICAL_CONJUGACY` | complete local law with receiver edge versus $\mathcal T(U^n\otimes I)\mathcal T^*$; wrong-memory identity; unitarity; balance (2) with the v105 bond current; two negative controls | all exact equalities, nonzero bond flux, both controls fail |
| 3 `RECROSSING_AND_NO_PARKING` | $\det V = 1$, $\operatorname{tr}V$, identity (3), branch point $w_0\in(0,1)$ simple, $V_{12}$ zeros; light-cone witness $0,0,0,1024/15625$ | all exact |
| 4 `SYMMETRY_AND_DARK_RECORD` | coin and displacement reflection, $\widetilde{\mathcal R}\chi_0 = -\chi_0$, $[\mathcal R_n,W] = 0$ on a $5\times5\times4$ box, dark state parity and zero contact overlap, eternal parked record | all exact |
| 5 `SUCCESS_SECTOR` | membership conditions of `PROOF.md` §6.1 and analytic-constant preconditions | all strict inequalities hold |
| 6 `RETENTION_CERTIFICATE` | $\bar\delta(T)$, $\bar\eta(T)$, $\varepsilon(T)$; verdict at $T = 10^6$ | verdict line printed; `ACHIEVED` iff $\varepsilon(10^6)\le1/100$ |

## 6. Resource ceiling

- Physical: one object pair, one carrier, one receiver; active native charge
  $4+4+2 = 10$ (unchanged); spectral support of the success family inside the
  v105 window $I_E$; memory code space $\mathcal D$; no added lock, archive,
  reset, energy source or helper activity; time budget $T = 10^6$
  macrosteps, future-uniform thereafter.
- Computational: one run of `verify.py` from the repository root under the
  `tools/check_reproduce.py` environment, at most 120 seconds, exit code 0,
  empty standard error, deterministic standard output.

## 7. Pre-pin disclosure

- The frozen parameters ($N$, $p_1$, $w$, $\rho_P$, $\rho_k$, $T$,
  $\varepsilon_{\rm retain}$) were chosen after a non-formal floating-point
  evaluation of the same analytic bound formula, outside the repository, which
  estimated $\varepsilon(10^6)\approx7\times10^{-4}$ for these parameters. The
  exact certificate is therefore not a blind test; it is an exact audit of an
  analytic theorem whose constants were explored numerically during design.
- Helper functions of `verify.py` were exercised before this pin only on
  non-frozen toy parameters (other receiver site, fewer steps, other bump
  order, windows and radii, a five-label alphabet), including the two negative
  controls. No gate was executed with the frozen parameters before this pin.

## 8. Execution and custody

1. Commit and push this protocol, `PROOF.md`, `INTERFACE.md`, `README.md`,
   `SOURCES.tsv`, the verifier, its `README.md` and a placeholder
   `EXPECTED.txt`; read the pin back from the remote.
2. From a clean checkout of the pin run
   `python3 reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/verify.py` under the
   `tools/check_reproduce.py` environment; save exact stdout as `EXPECTED.txt`
   and record neutral fields in `RUN.md`.
3. Add `RESULT.md`. A changed verifier, parameter or threshold after the pin
   invalidates the run and requires a new pin; a recorded first run is never
   overwritten. The pull-request check reruns the verifier on x86_64 and
   aarch64 and compares the bytes.

## 9. Scope fences

Not claimed: the actual normalized v105 selected component; exact permanent
retention of a captured record; finite preparation; any detector effect,
false-positive rate or measured post-state; many-carrier or asynchronous
dynamics; spectral-energy flow; occurrence or Born-rule statements; any Canon
promotion.
