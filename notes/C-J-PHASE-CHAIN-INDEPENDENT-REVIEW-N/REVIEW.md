# Independent Mathematical, Computational, and Scope Review: `P-J-PHASE-THREE-REFERENCE-1` (`#1581`) with Predecessor Chain `#1577` and `#1579`

```text
Candidate: C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N
Branch: notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N
Path: notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N/
Assignment issue: https://github.com/mathorn1973/twist-j/issues/1598
Parent coordination issue: https://github.com/mathorn1973/twist-j/issues/1548
Reviewer session: Antigravity-phase-chain-review-20261018 (A. M. Thorn <thorn@twistj.com>, Apache-2.0)
Public authority base: Public Canon v103, main commit dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d
Phase-1 pin commit: 80d6814a6b7c871b2b46d8e52f764c78c26810b4
Visibility / status / layer: PUBLIC / NON-CANONICAL / L1
```

## 1. Executive verdict and PR recommendations

- **Main target — [PR #1581](https://github.com/mathorn1973/twist-j/pull/1581) (`probes/P-J-PHASE-THREE-REFERENCE-1/`, head `694e5839f50dc9ef19f28792c8c6b9d64307389d`, original pin `6731b13455e221e097b33b6cf54d2356d00bef95`):** **PASS (recommend merge as non-canonical L1 probe; no Canon fold or status promotion in this PR).** Every mathematical identity, combinatorics census, 182-operation shared-reference prefix restoration law, $B=5$ two-input energy bound ($\le 23/5$, observed maximum $11978371/5248800$), record-only decoding with $d=\text{None}$ across all $25$ ordered root pairs, $W$-deleted collapse control, and outside-family zero-piston alias ($P=(0,0,0,0) \mapsto M=2 \leftrightarrow k=4$) is independently proved and computationally reproduced by our standalone method-blind verifier `break.py` without importing any target or canonical probe module.
- **Predecessor 1 — [PR #1577](https://github.com/mathorn1973/twist-j/pull/1577) (`probes/P-J-PHASE-PORT-SEPARATION-1/`, head `9c6a2471b72252d13eb45d4e58c77620ed8dfb92`, original pin `9af150e18d2c3749dbe44ff7a5c990b345cc1802`):** **PASS (recommend merge as non-canonical L1 negative-port probe; no Canon fold).** The quotient $Q(a,b,c,d,q,r) = (a+b+c+d+q+r,q,r) \bmod 5$ makes all five fifth-root pistons $P_0,\dots,P_4$ with common $(q,r)=(0,1)$ share $Q(x)=(2,0,1)$ and produces identical complete receiver histories $Y_t$ at every boundary of the unchanged `P-TWO-USE-TYPED-READOUT-CLOSURE-1` interface, while the control $p_B=(2,0,0,0)$ separates at boundary $2$ (capture $d$) and boundary $5$ (wave/tape $X$). Scope is strictly restricted to the unchanged port interface.
- **Predecessor 2 — [PR #1579](https://github.com/mathorn1973/twist-j/pull/1579) (`probes/P-J-PHASE-DECLARED-CONTACT-1/`, head `03390dca1c0a69ab8989f0daada0810c9956791a`, original pin `f48e0ce8ca86d707a5b2db458affb065419445df`):** **PASS (recommend merge as non-canonical L1 conditional-contact probe; no Canon fold).** The literal 14-leaf `CONTACT-RECORD` word $A_y$ on single reference $I_2=(1,0,0,1)$ separates $P_+=(0,1,0,0)$ ($\delta=1$) from $P_-=(4,4,4,4)$ ($\delta=0$) at leaf $4$ (`W`), satisfies the global occupied-reference update and $(r_y')^2 \bmod 5$ continuation invariance across all $2{,}500$ cases and $75{,}000$ continuation boundaries, and transmits all $4$ ordered pairs in $\{P_+,P_-\}^2$ through the unchanged funded apparatus at $B=2$ (maximum work $8252597/10497600 \le 8/5$) into distinct record pairs $(b_0,b_2)$ while collapsing to $(+,+)$ when all four `W` leaves are omitted.

---

## 2. Information-barrier and two-phase review audit

1. **Method-blind Phase 1 (before execution and before opening target proofs, verifiers, or results):**
   - Only the public Canon (`canon/CANON.md`, `canon/CORE.md`, `canon/FRONTIER.md`, `canon/REGISTRY.tsv`, `canon/SHA256SUMS`), the primary apparatus contracts (`probes/P-CONTACT-RECORD-1/PREREG.md`, `probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/{PREREG.md,CONTRACT.md,SOURCE_PROOF.md,PROOF.md,DOMAIN.tsv}`), the public issues (`#1548`, `#1576`, `#1578`, `#1580`, `#1598`), and the three target `PREREG.md` specifications (`#1581`, `#1577`, `#1579`) were read.
   - From those specifications and primary equations alone, we authored `SOURCES.tsv`, `PREREG.md`, `PROOF.md`, and standalone standard-library `break.py` (`1412` lines, zero imports from `probes/`), committed and pushed the Phase-1 pin `80d6814a6b7c871b2b46d8e52f764c78c26810b4` to `origin/notes/C-J-PHASE-CHAIN-INDEPENDENT-REVIEW-N`, and verified remote readback before running `break.py`.
2. **First frozen execution of `break.py`:**
   - Executed from the clean repository root at `80d6814a6b7c871b2b46d8e52f764c78c26810b4` under `LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1` with Python `3.13.13` (`Darwin 27.0.0`, `aarch64`).
   - Completed in `8.103` seconds with `exit_code: 0`, `stderr_bytes: 0`, and `stdout_bytes: 909` (`EXPECTED.txt` SHA-256 `244903d606fc5767966791bfd9004bed0282d9a04a34a39374a25e18140f34fb`).
   - All method-blind assertions passed on the first run of the unmodified pinned `break.py`, independently producing `max_work_1579 = 8252597/10497600` and `max_work_1581 = 11978371/5248800`.
3. **Phase-2 source inspection and isolated replay of target verifiers:**
   - After capturing `EXPECTED.txt` and `RUN.md`, we inspected `PROOF.md`, `verify.py`, `RESULT.md`, `EXPECTED.txt`, `RUN.md`, `README.md`, and `SOURCES.tsv` across `#1581`, `#1577`, and `#1579`, verified pin-to-head immutability, checked GitHub Actions check runs on all three PR heads, and replayed all three target `verify.py` scripts in an isolated temporary directory against their committed `EXPECTED.txt` files (`exit=0`, `stderr_len=0`, byte-for-byte match on all three).

---

## 3. Target PR custody, pin immutability, and CI status

### 3.1 Pin-to-head immutability and GitHub check-run table

In all three target PRs, `git diff --name-status <pin_commit> <head_commit>` shows that only post-run artifacts (`EXPECTED.txt`, `RESULT.md`, `RUN.md`, and `README.md` update in `#1577`) were added after the pin; `PREREG.md`, `PROOF.md`, `SOURCES.tsv`, and `verify.py` are byte-for-byte identical between `<pin_commit>` and `<head_commit>`.

| PR | Probe directory | Pin commit | Head commit | `architecture-x86_64` | `architecture-aarch64` | `check` | Isolated local replay |
|---|---|---|---|---|---|---|---|
| `#1577` | `probes/P-J-PHASE-PORT-SEPARATION-1` | `9af150e18d2c3749dbe44ff7a5c990b345cc1802` | `9c6a2471b72252d13eb45d4e58c77620ed8dfb92` | `success` | `success` | `success` | `1982 B` exact match |
| `#1579` | `probes/P-J-PHASE-DECLARED-CONTACT-1` | `f48e0ce8ca86d707a5b2db458affb065419445df` | `03390dca1c0a69ab8989f0daada0810c9956791a` | `success` | `success` | `success` | `4371 B` exact match |
| `#1581` | `probes/P-J-PHASE-THREE-REFERENCE-1` | `6731b13455e221e097b33b6cf54d2356d00bef95` | `694e5839f50dc9ef19f28792c8c6b9d64307389d` | `success` | `success` | `success` | `5927 B` exact match |

### 3.2 Complete file custody across `#1577`, `#1579`, and `#1581`

| PR | File path | Git blob | Bytes | SHA-256 |
|---|---|---|---:|---|
| `#1577` | `probes/P-J-PHASE-PORT-SEPARATION-1/PREREG.md` | `3195fc76088f31ad6227f9f0feab0011a9df6a93` | `6906` | `a2e772ae0bd638fdbb979eef9090b3519d2d80419a3adf53311b92bdc287a585` |
| `#1577` | `probes/P-J-PHASE-PORT-SEPARATION-1/PROOF.md` | `28a699c52a0285fd40bde441c21c2483c20e8ead` | `6632` | `a44ca2ac30895898f4a00ad2071a6130e0b44189b302720f3fd943e4b4cc3b67` |
| `#1577` | `probes/P-J-PHASE-PORT-SEPARATION-1/SOURCES.tsv` | `51139a44029c1729290bbb9419082723a1d5f7aa` | `920` | `b43a5d7e4192deb7c6119a477637a0ba35ff3197053728b4791d59867eadf834` |
| `#1577` | `probes/P-J-PHASE-PORT-SEPARATION-1/verify.py` | `e885eb8699549792d6da014511d11dc68f158348` | `10843` | `964d7a59d76cc7ff13ec531d79e087dd77d067542fbb9b6548cf4416b3d4cffe` |
| `#1577` | `probes/P-J-PHASE-PORT-SEPARATION-1/EXPECTED.txt` | `c6a12f0785404a1df6e804d1496f251d4315f148` | `1982` | `418ddd95da7a17c571d19b730f2f18ead763ef4d9b120fb45590d39ed26102d6` |
| `#1577` | `probes/P-J-PHASE-PORT-SEPARATION-1/RESULT.md` | `93cc20ec469f44e42c284ceb7da8da32f477f69f` | `6414` | `92e07893260172de34bfe1118f20c56cd7f98f054e1f8938649e408fd4c0e984` |
| `#1577` | `probes/P-J-PHASE-PORT-SEPARATION-1/RUN.md` | `df693aad1408ef8f29dcbc8b2e3f890005674704` | `1754` | `a60a029927896b9637ef1588d4fb04481a84aedab84de2d71077f7177a13b47c` |
| `#1577` | `probes/P-J-PHASE-PORT-SEPARATION-1/README.md` | `c246b9cee6fa68d4e643d0ed24e9ec09446c656a` | `1487` | `ee7af9711af12878813d49699a18bccfefccc11e486dad4f4e31a7d09bb98e48` |
| `#1579` | `probes/P-J-PHASE-DECLARED-CONTACT-1/PREREG.md` | `e4d5aa408a653436670644bc6f6edadb1af42ae2` | `11558` | `72a20e673f91b850868b77f9863ee35ef0911b912c1ecae5e12e0b14c593d404` |
| `#1579` | `probes/P-J-PHASE-DECLARED-CONTACT-1/PROOF.md` | `dc827576bbe3a62e1fe8dc25e3264482da0c0fd4` | `20618` | `c094d2239e4eecc59c864185fd2dd159d27dbf2c35b5177412d122e524bbabe2` |
| `#1579` | `probes/P-J-PHASE-DECLARED-CONTACT-1/SOURCES.tsv` | `85be5b01dba8b57c8fa8239ccc6e5c904e9c2f52` | `1510` | `061c4626b3cf0c32496cbb5369ae379af4a3c7737e6c10b1c99ce5bbb1c10f7d` |
| `#1579` | `probes/P-J-PHASE-DECLARED-CONTACT-1/verify.py` | `f8a82bd739e7591e243300d46238cbcea2e020fe` | `14653` | `ec04b1cbc9fcf842571209798613d832bcf94ebcb86be421a1e7741f5b30018f` |
| `#1579` | `probes/P-J-PHASE-DECLARED-CONTACT-1/EXPECTED.txt` | `0d1e3b15ab160fb3ac2c9accb2d68e92ea68e4d6` | `4371` | `4a74d8ce680d8b7cebc389105b699b85054afcb23630835adea5a3c5f0457cbc` |
| `#1579` | `probes/P-J-PHASE-DECLARED-CONTACT-1/RESULT.md` | `2c6000f79549bc4a5da1ac41d34e9dd469e0b68b` | `10116` | `02c29a0f7a06312548bf5a8891e781d9f9e8701a76219536ff9bce94d36cf178` |
| `#1579` | `probes/P-J-PHASE-DECLARED-CONTACT-1/RUN.md` | `2bd762eb1b7deb2c352f49f0251c35c796efe586` | `2294` | `223ec5fad3d8018424e6259f1a34f8204e7ba1beb45f4bba251358ab6cbec96d` |
| `#1579` | `probes/P-J-PHASE-DECLARED-CONTACT-1/README.md` | `d84245ffaa3fb49b6fea345ffddd547fd0a387b0` | `1606` | `23b511639f908ce40591371105a73d0b525228118844dd2a48a5abff7e233378` |
| `#1581` | `probes/P-J-PHASE-THREE-REFERENCE-1/PREREG.md` | `a42f896cefe46e48902d883420883be0beb54e5e` | `13116` | `0715999fc0d35c9547aee603a23747387a7ce80425236f920c3f657985a960a3` |
| `#1581` | `probes/P-J-PHASE-THREE-REFERENCE-1/PROOF.md` | `9b41b1b1808279dfd156051fbbdb0da87d6b36e4` | `21125` | `388670e91371acd707d887aeff3919dfeddaaadb762767a19fba5945786e7e43` |
| `#1581` | `probes/P-J-PHASE-THREE-REFERENCE-1/SOURCES.tsv` | `85be5b01dba8b57c8fa8239ccc6e5c904e9c2f52` | `1510` | `061c4626b3cf0c32496cbb5369ae379af4a3c7737e6c10b1c99ce5bbb1c10f7d` |
| `#1581` | `probes/P-J-PHASE-THREE-REFERENCE-1/verify.py` | `65b555d9963e205c08b5cc173b6b1e226526244c` | `24263` | `cbd542c2504913fee15257c0d67477cf7469ad070f99c0ef3b42b699fc889757` |
| `#1581` | `probes/P-J-PHASE-THREE-REFERENCE-1/EXPECTED.txt` | `03a8df20f05522edeb5378f1232d8797fa5fefd4` | `5927` | `c94ccd06a464a9725856d10ab7d24dc7ecc17ea0a9cccde4b68ce3eb16d2d36e` |
| `#1581` | `probes/P-J-PHASE-THREE-REFERENCE-1/RESULT.md` | `a1491d93c23a0bb7540bc88c0c860d376712b469` | `9849` | `f131c49bd87ca416b7d4fe901b70eac3cffbc01264ab58eab4af5b9457076fd6` |
| `#1581` | `probes/P-J-PHASE-THREE-REFERENCE-1/RUN.md` | `a107915e6f2555ec608ccd424237c8847794c69f` | `3613` | `f729e2f37a899119343af40ed72af10a51db810b5e19748bef4912dd2bcd66ea` |
| `#1581` | `probes/P-J-PHASE-THREE-REFERENCE-1/README.md` | `29df58d29319bade81c809bce5f994e9f8639432` | `3410` | `497f2ecd2013f16a7fe974a3ac89fd8cf18d8d8ee7d67242aa9f92545dade5c4` |

---

## 4. Detailed evaluation of the six required review questions

### Question 1 — Unchanged-port boundary (`#1577`)

- **Mathematical & computational verification:**
  In the marked basis $B_0=(1,\zeta_5,\zeta_5^2,\zeta_5^3)$ of $\mathcal O=\mathbb Z[\zeta_5]$ reduced modulo $5$, the five fifth roots of unity $1,j,j^2,j^3,j^4$ have piston vectors $P_0=(1,0,0,0)$, $P_1=(0,1,0,0)$, $P_2=(0,0,1,0)$, $P_3=(0,0,0,1)$, and $P_4=(4,4,4,4)$ with balanced lifts $\ell(P_k)=\zeta_5^k$, Archimedean norm squares $A(\zeta_5^k)=B(\zeta_5^k)=1$, and distinct mixed terms $C(\zeta_5^k)=\zeta_5^k\tau_3(\zeta_5^k)=\zeta_5^{-k}$. Because $\Phi_5(1)=5\equiv 0\pmod 5$, all five satisfy $\sum_{i=0}^3 (P_k)_i \equiv 1\pmod 5$, so at the fixed ready receiver $(q,r)=(0,1)$ all five share $Q(x)=(z,q,r)=(2,0,1)$.
  Every native generator $g_0,\dots,g_4$ and the selector $(z+2\theta_n)\bmod 5$ factor through $Q(x)$ (`31,250` checkpoint-driver pairs verified), and the coupled two-use transition accesses the two native heads only through $(q_A,r_A)$ at $c=1$ and $(q_B,r_B)$ into $d$ at $c=1$. By induction (`PROOF.md` Theorem 1.2 and `#1577/PROOF.md` Sections 3–4), all ordered pairs in $\{P_0,\dots,P_4\}^2$ (and specifically the four pairs in $\{P_1,P_4\}^2$) produce identical complete receiver histories $Y_t$ at every boundary $t\ge 0$, identical final work $W=8252597/41990400$, and identical decoded vectors $z_A=z_B=(1/2,0,0,0)$, while the control $p_B=(2,0,0,0)$ ($Q=(3,0,1)$) separates $d$ at boundary $2$ and $X$ at boundary $5$, decoding $z_B=(1/2,1/2,0,0)$.
- **Scope audit:**
  `#1577` strictly scopes this negative result to the unchanged `P-TWO-USE-TYPED-READOUT-CLOSURE-1` port and quotient-compatible operations. It explicitly notes that the native heads $x_A,x_B$ themselves remain distinct in $\mathbb F_5^6$ and that $\mathcal O/(5^k)$ retains $j-j^4 = 1+2j+j^2+j^3 \not\equiv 0$, so it does not claim impossibility for every native word or rule out piston-sensitive contacts.

### Question 2 — Single-reference contact and `W` witness (`#1579`)

- **Mathematical & computational verification:**
  For the literal 14-leaf word $A_y = (\mathcal U_y,e_y,d_y,W,b_x,b_y,W,d_y,e_y,W,b_y,b_x,W,\mathcal U_y)$ on $(x,y,\eta) \in \mathbb F_5^6 \times \mathbb F_5^6 \times \{0,1\}$, $E_b = W_b(b_x b_y)W_b$ applies $b_x b_y$ when $h(P_x,P_y)=0$ ($\delta=1$) and flips only $\eta$ when $h(P_x,P_y)\ne 0$ ($\delta=0$). Conjugating by $\tau_y = e_y d_y$ and $\mathcal U_y$ gives the exact occupied-reference map
  \[
  (p_x,q_x,r_x;\;p_y,q_y,r_y;\;\eta) \longmapsto \bigl(p_x,q_x,r_x;\;p_y,q_y+3\delta,P_{q_y+3\delta}(P_{q_y}(r_y));\;\eta\bigr),
  \]
  preserving $x$ and $\eta$ completely and writing $r_y'=\delta$ whenever $r_y=0$. With $I_2=(1,0,0,1)$, $h(P_x,I_2)=3(a+d)\bmod 5$ yields mask $(\delta(P_k,I_2))_{k=0}^4 = (0,1,1,0,0)$, separating $P_+=(0,1,0,0)$ ($\delta=1$, endpoint $(1,0,0,1,3,1)$) from $P_-=(4,4,4,4)$ ($\delta=0$, endpoint $(1,0,0,1,0,0)$).
  In `break.py` (matching `#1579/verify.py`), we verified:
  - The first leaf where $(Q(x),Q(y),\eta)$ differs between $P_+$ and $P_-$ is leaf $4$ (`W`).
  - All $2{,}500$ complete cases ($2$ sources $\times 5^4$ fibres $\times 2$ bits) and $500$ ready ($r_y=0$) cases match the exact formula and its reversed-word inverse.
  - Across all $75{,}000$ continuation boundaries ($2{,}500 \times 2 \times 15$ through $A_x$ and $A_x^{-1}$), only $b_y$ acts on $r_y$ (by negation), so $(r_y')^2 \bmod 5$ is invariant at every leaf boundary and full $y$ is restored at the endpoint.
  - Under the two-copy relay into the unchanged apparatus at $B=2$, all $4$ pairs in $\{P_+,P_-\}^2$ accept both contacts ($W \le 8252597/10497600 < 8/5 < 2$) and decode via $d=\text{None}$ to the exact pairs in $\{(1,0,0,0),(1/2,1/2,0,0)\}^2$.
  - Deleting the four `W` leaves forces $\delta=1$ on both sources, collapsing all $4$ ordered pairs to the $(+,+)$ endpoint $((1,0,0,1,3,1),(1,0,0,1,3,1))$.

### Question 3 — Hyperplane bijection and 625-reference census (`#1581`)

- **Mathematical & computational verification:**
  For $Y=(u,v,w,z)\in \mathbb F_5^4$, evaluating $h_Y(P_k)$ on the five roots gives
  \[
  \Phi(u,v,w,z) = (h_Y(P_0),\dots,h_Y(P_4)) = 3\bigl(z,\,-w,\,-v,\,u,\,v+w-u-z\bigr) \bmod 5,
  \]
  which is an $\mathbb F_5$-linear bijection onto the 4-dimensional sum-zero hyperplane $\mathcal H = \{h\in \mathbb F_5^5 : \sum_{k=0}^4 h_k = 0\}$ with explicit inverse $(u,v,w,z) = (2h_3,-2h_2,-2h_1,2h_0)\bmod 5$.
  Because non-empty zero-sum tuples of length $m=5-s$ over $\mathbb F_5^\times$ have count $N(m) = \frac{4^m + 4(-1)^m}{5}$, each binary mask $\delta \in \{0,1\}^5$ of weight $s=\sum_k \delta_k$ is realized by:
  - $s=0$: $204$ references ($1$ mask),
  - $s=1$: $52$ references per mask ($5$ masks, $260$ references),
  - $s=2$: $12$ references per mask ($10$ masks, $120$ references),
  - $s=3$: $4$ references per mask ($10$ masks, $40$ references),
  - $s=4$: $0$ references per mask ($5$ masks, $0$ references — a single nonzero entry cannot sum to $0$),
  - $s=5$: $1$ reference ($Y=(0,0,0,0)$, $1$ mask).
  Total: $204 + 260 + 120 + 40 + 0 + 1 = 625$ references across $32-5 = 27$ nonempty mask classes (`3,125` polar evaluations verified).
  - **Separating $j$ from $j^4$ ($\delta_1 \ne \delta_4$):** $2 \times (1 \times 4 \times 5^2) = 200$ references.
  - **Separating both conjugate pairs ($\delta_1 \ne \delta_4$ and $\delta_2 \ne \delta_3$):** $4 \times 4^2 = 64$ references, splitting into $16$ references for each of the $4$ marked complex-embedding sign patterns $(\delta_1,\delta_2,\delta_3,\delta_4) \in \{(1,1,0,0),(1,0,1,0),(0,1,0,1),(0,0,1,1)\}$.
  - **Constant masks:** $204$ ($00000$) $+ 1$ ($11111$) $= 205$ references.

### Question 4 — Three-reference lower bound and code (`#1581`)

- **Mathematical & computational verification:**
  In the frozen binary-output reference class where each reference interaction contributes only $\delta(P_x,Y_r)\in \{0,1\}$ and the collector update factors through $(\delta_1,\dots,\delta_m)\in \{0,1\}^m$, at most $2^m$ distinct values can be produced; since $2^2=4 < 5 \le 2^3=8$, $m=3$ binary reference outputs are necessary and sufficient.
  The three fixed references $Y_A=(0,2,2,0)$, $Y_B=(4,2,2,0)$, and $Y_C=(1,1,0,1)$ all satisfy $\det(Y_r) \equiv 1\pmod 5$ and produce masks $\delta_{Y_A}=(1,0,0,1,0)$, $\delta_{Y_B}=(1,0,0,0,1)$, and $\delta_{Y_C}=(0,1,0,0,0)$. With weights $(1,2,4)$,
  \[
  M(P_k) = (\delta_{Y_A}(P_k) + 2\delta_{Y_B}(P_k) + 4\delta_{Y_C}(P_k)) \bmod 5
  \]
  gives $(M(P_0),\dots,M(P_4)) = (3,4,0,1,2)$ with exact affine inverse $k = (M+2)\bmod 5$.
- **Scope audit:**
  `#1581` (`PREREG.md`, `PROOF.md` Section 3, `RESULT.md` Section 2, `README.md`) explicitly scopes the $m=3$ lower bound to binary-output results in the declared bit-factor class and explicitly states that it is neither a lower bound on the number of physical reference cells (if re-preparation were admitted) nor an impossibility theorem for non-binary five-valued contacts outside that class.

### Question 5 — Resource and admission audit (`#1579` and `#1581`)

Relative to the unchanged two-use port baseline (`P-TWO-USE-TYPED-READOUT-CLOSURE-1` / `#1577`), `#1579` and `#1581` require the following explicit extra resources:

| Resource / Parameter | Baseline (`#1577`) | Single-reference contact (`#1579`) | Three-reference chain (`#1581`) | Admission status |
|---|---|---|---|---|
| Native cells on carrier | $2$ source heads ($x_A,x_B \in \mathbb F_5^6$) | $4$ cells ($2$ sources $+ 2$ copies of reference $I_2$, or shared reference + two heads) | $7$ cells ($2$ sources $S_A,S_B$, $3$ shared references $R_A,R_B,R_C$, $2$ collectors $H_A,H_B$) | Declared L1 extension; **not** derived from autonomous $U$ |
| Piston-sensitive gate `W` ($W_b$) | None ($0$ leaves) | $4$ `W` leaves per $A_y$ ($8$ across two copies) | $48$ `W` leaves across $6$ compute/uncompute blocks (`168` contact leaves total) | Outside quotient envelope $\mathcal E_Q$; native/physical admission **OPEN** |
| Reading involution $\mathcal U_i$ | None ($0$ leaves) | $2$ $\mathcal U_y$ leaves per $A_y$ ($4$ across two copies) | $24$ $\mathcal U_y$ leaves across $6$ blocks | In $\mathcal E_Q$, but native/physical compilation **OPEN** |
| External sign-history bit $\eta \in \{0,1\}$ | None | $1$ bit per contact ($2$ bits across two independent copies, or $1$ restored bit) | $1$ shared bit $\eta \in \{0,1\}$ across all $182$ prefix leaves, restored at all $300$ block boundaries | Declared auxiliary bit; physical carrier **OPEN** |
| Reference pistons | None | $I_2=(1,0,0,1)$ at $(q_y,r_y)=(0,0)$ | $Y_A=(0,2,2,0)$, $Y_B=(4,2,2,0)$, $Y_C=(1,1,0,1)$ at $(0,0)$, restored after every block | Selection principle & preparation cost **OPEN** |
| Collector heads & whole-cell `CSUM` | None | None (written reference cells become apparatus heads directly) | $2$ collectors initialized to $Z_0=(4,0,4,2,0,0)$ + $14$ weighted `CSUM` leaves ($1+2+4=7$ per source) | Prefix energy & autonomous scheduling **UNSUPPLIED / OPEN** |
| Classical work capacity $B$ | $B = 4/5$ (max work $8252597/41990400 \approx 0.1965$) | $B = 2$ (a priori bound $8/5$, max work $8252597/10497600 \approx 0.7861$) | $B = 5$ (a priori bound $23/5$, max work $11978371/5248800 \approx 2.2821$) | Covers only the two classical wave/tape kicks; prefix energy **UNSUPPLIED** |

- **Frontier and Canon boundary verification:**
  Neither `#1579` nor `#1581` modifies `canon/*`, `STATUS.md`, `POLICY.md`, or any workflow. Both explicitly state that `O-J-PHASE-ACQUISITION`, `O-QDD-INSTRUMENT-APPARATUS` (`#1398`/`#1399`), and `O-QUADRATIC-MEMORY-NATIVE-CONTACT` (`#1498`/`#1502`) remain **OPEN**, and neither claims autonomous native acquisition, physical photon/frequency identification, late second-message arrival, or apparatus reset/renewal.

### Question 6 — Outside-family alias (`#1581`)

- **Mathematical & computational verification:**
  For the outside-family zero piston $P_{\text{zero}}=(0,0,0,0)$ (which has $\sum P_{\text{zero}} \equiv 0 \not\equiv 1\pmod 5$ and $\det P_{\text{zero}} = 0$, outside the five-root unit family), $h(P_{\text{zero}},Y)=0$ for every reference $Y\in \mathbb F_5^4$, so $(\delta_{Y_A},\delta_{Y_B},\delta_{Y_C}) = (1,1,1)$ and
  \[
  M(P_{\text{zero}}) = (1 + 2 + 4)\bmod 5 = 2 = M(P_4),
  \]
  which produces the exact same collector head $(1,0,0,1,1,2)$ as $j^4$ ($k=4$) and is distinct from the present identity root $1=P_0=(1,0,0,0)$ ($M(P_0)=3$, collector head $(1,0,0,1,4,3)$, $k=0$).
  Both `#1581` (`PROOF.md` Section 9, `RESULT.md` Section 4, `EXPECTED.txt` `AUDIT.zero_piston_alias_phase = 4`, `AUDIT.physical_absence_detected = false`) and our standalone `break.py` explicitly verify and document this alias boundary: a present identity phase $k=0$ is not source absence, and the three-reference code on the promised five-root family does not detect outside-family absence.

---

## 5. Claim-by-claim disposition table

| Source PR | Claim / Component | Method-blind `break.py` check | Disposition | Scope & boundary note |
|---|---|---|---|---|
| `#1577` | Five fifth-root balanced lifts in $B_0$, norms $A=B=1$, distinct $C(j^k)=j^{-k}$, common $Q=(2,0,1)$ | `check_cyclotomic_and_quotient_envelope()` (`5` roots + `4` basis rows) | **VERIFIED (`candidate-T / C`)** | Exact in $\mathbb Z[\zeta_5]$ and $\mathbb F_5^6$ |
| `#1577` | $31{,}250$ native step quotient checks & all-time receiver blindness on $\{P_+,P_-\}^2$ at $B=4/5$ + rollover + $p_B=(2,0,0,0)$ control | `check_cyclotomic_and_quotient_envelope()` (`31,250` steps) & `check_all_relays()` (`4` pairs $\times 9$ boundaries + control) | **VERIFIED (`candidate-T / C`)** | Strictly scoped to unchanged `P-TWO-USE-TYPED-READOUT-CLOSURE-1` port |
| `#1579` | Quotient-compatible envelope $\mathcal E_Q$ (`35` affine basis rows, `125` $\mathcal U_i$ triples, `13`/`26` `CSUM` basis rows) & leaf `4:W` first split | `check_cyclotomic_and_quotient_envelope()` & `check_contact_inventories()` (`first_unequal_leaf = "4:W"`) | **VERIFIED (`candidate-T / C`)** | Proves piston-sensitive gate outside $\mathcal E_Q$ is required |
| `#1579` | $2{,}500$ complete $A_y$ cases, $500$ ready cases, inverse restoration, $75{,}000$ continuation $(r_y')^2\bmod 5$ boundaries | `check_contact_inventories()` (`cases_1579 = 2500`, `ready_1579 = 500`, `cont_boundaries_1579 = 75000`) | **VERIFIED (`candidate-T / C`)** | Holds on arbitrary occupied $(q_x,r_x,q_y,r_y,\eta)$ |
| `#1579` | $4$ two-copy relays at $B=2$, max work $8252597/10497600 \le 8/5$, $d=\text{None}$ decoding, $W$-deleted $(+,+)$ collapse | `check_all_relays()` (`max_work_1579 = "8252597/10497600"`, `4` distinct records, $W$-deleted control) | **VERIFIED (`candidate-T / C`)** | Conditional on declared $A_y$, $I_2$, $\eta$, and $B=2$ |
| `#1581` | Bijection $\Phi: \mathbb F_5^4 \to \mathcal H \subset \mathbb F_5^5$, mask counts $(204,52,12,4,0,1)$, $27$ classes, $200$ sep $j/j^4$, $64=4\times 16$ sep both, $205$ constant | `check_reference_census_and_code()` (`3,125` evaluations, all counts exact) | **VERIFIED (`candidate-T / C`)** | Exact finite-field combinatorics |
| `#1581` | Binary-output lower bound $m=3$ ($2^2 < 5 \le 2^3$), $\det(Y_A)=\det(Y_B)=\det(Y_C)=1$, $M=(3,4,0,1,2)$, $k=(M+2)\bmod 5$ | `check_reference_census_and_code()` (`codes_m = [3,4,0,1,2]`) | **VERIFIED (`candidate-T / C`)** | Minimum is for binary outputs in bit-factor class, not physical cells |
| `#1581` | $18{,}750$ occupied contact/CSUM/uncompute cases ($3{,}750$ ready) & $50$ two-source 182-leaf prefixes ($300$ block boundaries) | `check_contact_inventories()` (`18,750` / `3,750`) & `check_all_50_prefixes()` (`50` prefixes, `300` boundaries) | **VERIFIED (`candidate-T / C`)** | Full restoration of sources, $3$ shared refs, and $1$ shared bit $\eta$ |
| `#1581` | Invertibility $\det R_0 = \frac{14992667}{13060694016} > 0$, cold energies $(3/20,2/5,17/20,2/5,23/20)$, $25$ relays at $B=5$ ($200$ boundaries), max work $11978371/5248800 \le 23/5$, $d=\text{None}$ recovery | `IndependentWaveApparatus` & `check_all_relays()` (`200` boundaries, `25` distinct records, `5` first records, `max_work_1581 = "11978371/5248800"`) | **VERIFIED (`candidate-T / C`)** | Independently implemented from primary 705-site stencil equations |
| `#1581` | $25$ $W$-deleted controls collapsing to $M=2$ ($(j^4,j^4)$) & outside-family zero-piston alias $P=(0,0,0,0) \mapsto M=2$ | `check_all_50_prefixes()` & `check_all_relays()` (`w_deleted_controls = 25`, zero-piston alias verified) | **VERIFIED (`candidate-T / C`)** | Explicitly documents that $k=0$ is present identity and $(0,0,0,0)$ aliases $k=4$ |
| `#1577`, `#1579`, `#1581` | Native/physical admission of $W_b$, $\mathcal U_i$, `CSUM`, reference/bit preparation, prefix energy, autonomous control, late arrival, renewal | Audited across all three `PREREG.md`, `PROOF.md`, `RESULT.md`, `README.md` | **OPEN (`O`)** | Properly left open under `O-J-PHASE-ACQUISITION`, `#1398/#1399`, `#1498/#1502` |
