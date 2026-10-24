# Prospective independent review contract: five-phase transfer and resource boundary

**PUBLIC / NON-CANONICAL / L1. Prospective independent review pin; unexecuted.**
- **Candidate:** `C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N`
- **Branch:** `notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N`
- **Sole output path:** `notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N/`
- **Reviewer session:** `Antigravity-phase-chain-review-20261018` (`A. M. Thorn <thorn@twistj.com>`, Apache-2.0)
- **Public assignment & claim:** [#1598](https://github.com/mathorn1973/twist-j/issues/1598) (`4736` UTF-8 bytes, SHA-256 `031ee71ad309cbcbff69ea9fcaed75be8ee5a106264222c43dfff6bdd979e59d`), claim receipt [#1598 comment](https://github.com/mathorn1973/twist-j/issues/1598#issuecomment-6241849223), parent coordination [#1548](https://github.com/mathorn1973/twist-j/issues/1548).
- **Authority basis:** Public Canon v103 ACTIVE, `main` / tag `canon-v103` at `dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d`, content commit `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`, `canon/CANON.md` `1052518` bytes, SHA-256 `d87657aeccc568dd668718fb9cbea6136643e5db32dd4e289a4de328e64f824b`.

## 1. Frozen targets and exposure boundary

This review audits the three-part phase-transfer chain:

1. **Main target:** [PR #1581](https://github.com/mathorn1973/twist-j/pull/1581) (`probes/P-J-PHASE-THREE-REFERENCE-1/`), result head `694e5839f50dc9ef19f28792c8c6b9d64307389d`, original preregistration pin `6731b13455e221e097b33b6cf54d2356d00bef95` (`PREREG.md` `13116` bytes, SHA-256 `0715999fc0d35c9547aee603a23747387a7ce80425236f920c3f657985a960a3`).
2. **Context target 1 (unchanged-port negative):** [PR #1577](https://github.com/mathorn1973/twist-j/pull/1577) (`probes/P-J-PHASE-PORT-SEPARATION-1/`), result head `9c6a2471b72252d13eb45d4e58c77620ed8dfb92`, original preregistration pin `9af150e18d2c3749dbe44ff7a5c990b345cc1802` (`PREREG.md` `6906` bytes, SHA-256 `a2e772ae0bd638fdbb979eef9090b3519d2d80419a3adf53311b92bdc287a585`).
3. **Context target 2 (single-reference conjugate-pair contact):** [PR #1579](https://github.com/mathorn1973/twist-j/pull/1579) (`probes/P-J-PHASE-DECLARED-CONTACT-1/`), result head `03390dca1c0a69ab8989f0daada0810c9956791a`, original preregistration pin `f48e0ce8ca86d707a5b2db458affb065419445df` (`PREREG.md` `11558` bytes, SHA-256 `72a20e673f91b850868b77f9863ee35ef0911b912c1ecae5e12e0b14c593d404`).

**Exposure statement:**
- High-level advertised conclusions are disclosed in assignment `#1598`, daily index `#1602`, and the three preregistrations; result blindness is not claimed.
- This reviewer session (`Antigravity-phase-chain-review-20261018`) did not author `#1577`, `#1579`, or `#1581`.
- For Phase 1 (before committing, pushing, and reading back this pin and before the first execution of `break.py`), **method-blind discipline** is maintained: only `#1598`, `#1602`, the Public Canon v103 bundle (`STATUS.md`, `POLICY.md`, `AGENTS.md`, `canon/*`), the canonical dependencies on `main` (`probes/P-CONTACT-RECORD-1/PREREG.md`, `probes/P-CONTACT-RECORD-1/verify.py`, `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/PREREG.md`, `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py`, `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/DOMAIN.tsv`), and the three target `PREREG.md` files at their exact original pins (`9af150e18d2c3749dbe44ff7a5c990b345cc1802`, `f48e0ce8ca86d707a5b2db458affb065419445df`, `6731b13455e221e097b33b6cf54d2356d00bef95`) were read.
- None of the target `verify.py`, `PROOF.md`, `RESULT.md`, `EXPECTED.txt`, or `RUN.md` files on `#1577`, `#1579`, or `#1581` has been opened before this pin. They will be inspected and compared only in Phase 2, after this pin is pushed, read back from GitHub, and `break.py` has completed its first frozen execution.

## 2. Equations and independent mathematical program

All mathematical derivations are written in [PROOF.md](PROOF.md) and audited by the standalone standard-library program [break.py](break.py), which imports no code from `#1577`, `#1579`, `#1581`, `P-CONTACT-RECORD-1`, or `P-TWO-USE-TYPED-READOUT-CLOSURE-1` (it reads only `SOURCES.tsv` and `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/DOMAIN.tsv` to verify custody hashes and cross-check the constructed 705-site lattice domain).

### Attack 1: Reconciling the unchanged-port negative (`#1577`) with supplied-contact positive (`#1579`, `#1581`)
- In the marked basis $(1, \zeta_5, \zeta_5^2, \zeta_5^3)$ of `DEF-QDD-AMPLITUDE-B0` (written $(1, j, j^2, j^3)$ in the target specifications) with balanced lift $\ell = (0, 1, 2, -2, -1)$, the five fifth roots of unity $\zeta_5^k$ ($k=0,1,2,3,4$) have unique piston coordinates
  $$P_0 = (1,0,0,0),\quad P_1 = (0,1,0,0),\quad P_2 = (0,0,1,0),\quad P_3 = (0,0,0,1),\quad P_4 = (4,4,4,4).$$
- Verify in $\mathbb Z[\zeta_5]$ that all five roots satisfy $\mathrm{aug}(\zeta_5^k) = 1$, Archimedean norms $A(\zeta_5^k) = \zeta_5^k \tau_4(\zeta_5^k) = 1$ and $B(\zeta_5^k) = \tau_2(\zeta_5^k)\tau_3(\zeta_5^k) = 1$, and distinct cross-place mixed terms $C(\zeta_5^k) = \zeta_5^k \tau_3(\zeta_5^k) = \zeta_5^{4k} = \zeta_5^{-k}$.
- With common ready control $(q,r) = (0,1)$, all five source cells $x^{(k)} = (P_k, 0, 1) \in \mathbb F_5^6$ have identical native quotient $Q(x^{(k)}) = (\sum x^{(k)} \bmod 5, q, r) = (2, 0, 1)$.
- Verify across all $15625 \times 2 = 31250$ native checkpoints $(x, \theta) \in \mathbb F_5^6 \times \{0,1\}$ and all $5$ native generators $g_0, \dots, g_4$ that each generator is an involution on $\mathbb F_5^6$ and descends to $Q(x) = (z,q,r)$ as
  $$(z,q,r),\quad (-z,-q,-r),\quad (2-z,1-q,-r),\quad (2-z,1-q,1-r),\quad (3-z,2-q,1-r) \pmod 5.$$
- Verify that the reading swap $\mathcal U_i : (p, q, r) \mapsto (p, q, P_q(r))$ descends to $Q(x) \mapsto ((z - r + P_q(r)) \bmod 5, q, P_q(r))$ (all $125$ triples), and whole-cell `CSUM` $(x, y) \mapsto (x, y \pm x)$ descends to $Q(y') = Q(y) \pm Q(x) \pmod 5$ (tested on zero plus $12$ basis vectors of $\mathbb F_5^{12}$). Thus the entire quotient-compatible envelope $\mathcal E_Q$ generated by slotwise $g_0,\dots,g_4$, forward $U$ at common $(n,\theta_n)$, $\mathcal U_i$, whole-cell `CSUM`/inverses, and whole-cell swap preserves equal $Q$-histories across all five root sources.
- Execute the unchanged coupled apparatus (`#1577`, $B=4/5$) on all $4$ ordered pairs in $\{P_1, P_4\}^2$: verify that the complete receiver projection $Y = (n, c, X, W, b, B, \sigma_A, \sigma_B, d)$ is byte-for-byte identical at all $8$ boundaries $(n,c) = (0,0), (1,1), (1,2), (2,3), (3,4), (3,5), (4,6), (5,7)$ and at the 8th phase rollover $(5,0)$, even though both contacts accept ($W > 0$) and the native heads $(x_A, x_B)$ remain distinct. Verify the control pair $(P_1, (2,0,0,0))$, which agrees with $(P_1, P_1)$ through boundary 1, differs in $d$ at boundary 2, agrees in wave/tape $X$ through boundary 4, differs in $X, W, b$ at boundary 5, preserves the first cuts, and decodes to $((0,-1/2,0,0), (1/2,0,0,0))$.
- In the 14-leaf contact word $A_y = (\mathrm{Uy}, \mathrm{ey}, \mathrm{dy}, \mathrm{W}, \mathrm{bx}, \mathrm{by}, \mathrm{W}, \mathrm{dy}, \mathrm{ey}, \mathrm{W}, \mathrm{by}, \mathrm{bx}, \mathrm{W}, \mathrm{Uy})$, verify that leaves 1–3 ($\mathrm{Uy}, \mathrm{ey}, \mathrm{dy}$) lie in $\mathcal E_Q$ and keep $(Q(x), Q(y), \eta)$ identical across all five root sources, whereas **leaf 4 ($\mathrm{W} = W_b$)** is the exact first leaf where piston-sensitive information $h_Y(P_k)$ crosses the quotient $Q$.

### Attack 2: Complete 625-reference census, hyperplane bijection, and three-reference bit code
- For row-major $P = (a,b,c,d)$ and $Y = (u,v,w,z)$ in $\mathbb F_5^4$, verify the determinant polarization
  $$h_Y(P) = \frac{\det(P+Y)-\det(P)-\det(Y)}{2} = 3(az + du) + 2(bw + cv) \pmod 5,\qquad \delta_Y(P) = 1 - h_Y(P)^4 \in \{0,1\}.$$
- Evaluate $(h_Y(P_0), \dots, h_Y(P_4))$ across all $625$ references $Y \in \mathbb F_5^4$ ($3125$ evaluations): verify that it equals $3(z, -w, -v, u, v+w-u-z) \pmod 5$ and bijects $\mathbb F_5^4$ onto the sum-zero hyperplane $\{\mathbf v \in \mathbb F_5^5 : \sum_{k=0}^4 v_k \equiv 0 \pmod 5\}$.
- Verify the mask census over all $32$ binary masks $m \in \{0,1\}^5$:
  - Exact counts per mask of Hamming weight $s \in \{0,1,2,3,4,5\}$ are $N(5-s) = (4^{5-s} + 4(-1)^{5-s})/5 = (204, 52, 12, 4, 0, 1)$, giving $27$ nonempty mask classes and $5$ empty weight-4 masks.
  - Exactly $200$ references separate $P_1$ ($j$) from $P_4$ ($j^4$).
  - Exactly $64 = 4 \times 16$ references separate both conjugate pairs $(P_1, P_4)$ and $(P_2, P_3)$, matching the $4$ positive-imaginary-half sign patterns of the $4$ complex embeddings of $\mathbb Q(\zeta_5)$.
  - Exactly $205 = 204 + 1$ references have constant masks; $\delta_{-Y} = \delta_Y$ for all $Y$.
  - On the single receiver piston $I_2 = (1,0,0,1)$ of `#1579`, the mask on $k=0..4$ is $(0, 1, 1, 0, 0)$, separating $j$ ($k=1, \delta=1$) from $j^4$ ($k=4, \delta=0$) but merging $j$ with $j^2$ and $1, j^3, j^4$.
- For the three determinant-one references $Y_A = (0,2,2,0)$, $Y_B = (4,2,2,0)$, $Y_C = (1,1,0,1)$ of `#1581`:
  - Verify $\det(Y_A) = \det(Y_B) = \det(Y_C) = 1 \pmod 5$.
  - Verify their masks on $k=0..4$: $\delta_A = (1,0,0,1,0)$, $\delta_B = (1,0,0,0,1)$, $\delta_C = (0,1,0,0,0)$.
  - Verify that $M(P_k) = (\delta_A + 2\delta_B + 4\delta_C) \bmod 5 = (3, 4, 0, 1, 2)$ bijects $k=0..4$ onto $\mathbb F_5$ with inverse $k = (M + 2) \bmod 5$.
  - Verify that $2^2 = 4 < 5 \le 2^3 = 8$ forces at least $3$ binary outputs in any code factoring solely through binary flags $\delta \in \{0,1\}^m$, while noting that this does not bound physical cell count or non-binary readers.
  - Verify that present identity phase $P_0 = (1,0,0,0)$ has $M(P_0) = 3$, whereas the outside-family zero piston $P_{\mathrm{zero}} = (0,0,0,0)$ has $h_Y(0) = 0 \implies \delta_A = \delta_B = \delta_C = 1 \implies M(0) = 2 = M(P_4)$ (aliasing $j^4$).

### Attack 3: Literal joined-state contact, CSUM, and prefix execution
- For `#1579`: across all $2500$ cases ($2$ sources $P_1, P_4 \times 1$ receiver $I_2 \times 5^4$ controls $(q_x, q_y, r_x, r_y) \times 2$ bits $\eta \in \{0,1\}$), execute all $14$ literal leaves of $A_y$ and its reversed inverse, verifying $q_y' = (q_y + 3\delta) \bmod 5$, $r_y' = P_{q_y'}(P_{q_y}(r_y))$, full restoration of source and bit, $r_y' = \delta$ on all $500$ ready cases ($r_y=0$), and $r_y^2 \bmod 5$ invariance across all $15$ boundaries of subsequent $A_x$ and $A_x^{-1}$ ($75000$ continuation boundaries).
- For `#1581`: across all $18750$ occupied contact cases ($5$ sources $P_0..P_4 \times 3$ references $Y_A, Y_B, Y_C \times 5^4$ controls $(q_x, q_y, r_x, r_y) \times 2$ bits $\eta \in \{0,1\}$), execute all $14$ literal leaves of $A_y$, its reversed inverse, and the weighted whole-cell `CSUM` transfer into an arbitrary collector cell $Z$ followed by `CSUM` inverse, verifying exact endpoints and $r_y' = \delta$ on all $3750$ ready ($r_y=0$) cases.
- Execute all $50$ complete 182-operation prefixes of `#1581` ($25$ ordered pairs $(P_{k_A}, P_{k_B}) \times 2$ initial shared bits $\eta_0 \in \{0,1\}$) on the full joined carrier $(\mathbb F_5^6)^5 \times \{0,1\} \times Z_B$:
  - Verify at all $6$ block boundaries ($300$ block boundaries total) that both sources $(P_{k_A},0,1), (P_{k_B},0,1)$, all three shared references $(Y_A,0,0), (Y_B,0,0), (Y_C,0,0)$, and the shared work bit $\eta_0$ are literally restored.
  - Verify at all $182$ leaves that every classical apparatus coordinate $(n, c, X, W, b, B, \sigma_A, \sigma_B, d)$ is unchanged, and at all $91$ leaves of the second source's three blocks that the first collector head $Z_A = (1,0,0,1,3M_A \bmod 5, M_A)$ is untouched.
  - Verify that the literal 182-operation prefix brings the two collector heads from $Z = (4,0,4,2,0,0)$ to $(1,0,0,1,3M_A \bmod 5, M_A)$ and $(1,0,0,1,3M_B \bmod 5, M_B)$, and that the reversed 182-operation word restores the complete initial state.

### Attack 4: Downstream wave/tape propagation, retained tape cuts, and `d=None` port readout
- Independently construct the 705-site lattice domain $D = Y + B_0 + B_0$, check byte-for-byte agreement with `DOMAIN.tsv`, construct the 60-neighbor stencil $H$, operators $P, J_0, K, S$, quadratic energy $E(X)$, wave/tape step $F$ and $F^{-1}$, and response matrices $R_0, R_0^{-1}, R_1, D_2, D_3$, verifying the closed-form identity $R_0 = I_4 - \frac{1}{2} P^T H S$ and $D_2 = R_1 K_{P^T H P}$.
- Execute the 28-leaf prefix + 7 coupled steps for all $4$ pairs of `#1579` ($B=2$) and the 182-leaf prefix + 7 coupled steps for all $25$ pairs of `#1581` ($B=5$), auditing all $8$ boundaries ($200$ relay boundaries in `#1581`, $32$ in `#1579`):
  - Verify that the first native step ($c=0 \to 1$) maps $(1,0,0,1,3M \bmod 5, M)$ for $M=0..4$ to receivers $(1,0), (2,4), (1,2), (3,3), (4,2)$ and rational source vectors $\eta_{\mathrm{lift}} = (1/2,1/2,0,0), (1,0,0,0), (1/2,3/2,0,0), (-1,-1/2,0,0), (-1/2,3/2,0,0)$.
  - Verify that for each fixed first source $k_A$, the wave/tape history $X$ through boundary 4 ($c=4$) and the first retained cuts $(b_0, b_1) = (A_0, A_1)$ at boundary 7 ($c=7$) are identical across all $5$ choices of the second source $k_B$, and that Cut 0 (written at $c=3$) and Cut 1 (written at $c=4$) persist unchanged through the second contact ($c=4 \to 5$) to completion ($c=7$).
  - Verify that the restricted port reader receiving only $(b_0, b_2, \sigma_A, \sigma_B)$ with $d$ omitted (`d=None`) recovers the exact source vectors $(z_A, z_B)$ and ordered phase indices $(k_A, k_B)$ for all $25$ pairs in `#1581` ($25$ distinct $(b_0, b_2)$ pairs, $5$ distinct $b_0$ values) and all $4$ pairs in `#1579`.
  - Verify the $W$-deleted syntactic controls in `#1579` (all $4$ pairs collapse to $M=1$ on both heads, matching $(j,j)$) and `#1581` (all $25$ pairs collapse to $M=2$ on both heads, matching $(j^4, j^4)$, as does the outside-family zero-piston pair $((0,0,0,0), (0,0,0,0))$).

### Attack 5: Resource accounting, prefix energy boundary, and non-renewal
- Verify from $S^T S = I_4 - \frac{1}{5}\mathbf 1 \mathbf 1^T$ that the five cold kick energies $\frac{1}{2}\|S \eta_{\mathrm{lift}}\|^2$ for $M=0..4$ are $(3/20, 2/5, 17/20, 2/5, 23/20)$.
- Verify at every boundary of `#1579` ($B=2$) and `#1581` ($B=5$) that both contacts are accepted ($\sigma_A = \sigma_B = -1$ at completion), $E(X) = W$, and $b + W = B$, and compute the exact maximum realized work $W_{\max}$ across the $4$ pairs of `#1579` and $25$ pairs of `#1581`.
- Verify explicitly that:
  1. $B=2$ (`#1579`) and $B=5$ (`#1581`) account only for the two classical wave/tape kicks at $c=1$ and $c=4$; the 28-leaf / 182-leaf prefixes, source/reference preparation, shared bit, and external schedule carry no energy cost in the model.
  2. Reference and source restoration at the end of the prefix does not reset the apparatus: at $(n,c)=(5,7)$ and after rollover $(5,0)$, $W > 0$, $b = B - W < B$, $\sigma_A = \sigma_B = -1$, $d \ne (0,0)$, and the collector heads are at $n=5$.
  3. Both sources are preloaded before the prefix and $d$ captures the second collector receiver at $c=1$; this is not an independently arriving late second input.

## 3. Failure threshold and execution protocol

Zero tolerance for any algebraic, state, trajectory, cut-persistence, readout, or energy-account mismatch. Any failed assertion in `break.py` raises an `AssertionError` with the failing check name and witness and exits nonzero.

Commit and push `SOURCES.tsv`, `PREREG.md`, `PROOF.md`, and `break.py` to `origin/notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N` and verify their public commit SHA and blob SHA-256 values before executing:

```text
LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
  python3 notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N/break.py
```

Only after the first frozen run completes, record `EXPECTED.txt` and `RUN.md`, open and inspect the author `PROOF.md`, `verify.py`, `RESULT.md`, `EXPECTED.txt`, and `RUN.md` at the three target PR heads (`9c6a2471b72252d13eb45d4e58c77620ed8dfb92`, `03390dca1c0a69ab8989f0daada0810c9956791a`, `694e5839f50dc9ef19f28792c8c6b9d64307389d`), and write `REVIEW.md` and `README.md`.

## 4. Action layer and scope ceiling

Action layer **L1** only (`NON-CANONICAL` review note). Native admission of $W_b$, $\mathcal U_i$, whole-cell `CSUM`, reference selection, autonomous prefix compilation, prefix energy accounting, independent late arrival, apparatus renewal, photon identity, frequency sign, and physical phase measurement remain explicit open premises. `QUADRATIC-MEMORY-NATIVE-CONTACT` and `QDD-INSTRUMENT-APPARATUS` remain open. No Canon, registry, gate, workflow, or source branch is modified.
