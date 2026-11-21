<!-- SPDX-License-Identifier: Apache-2.0 -->

# Prospective Preregistration: C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N

- **Candidate:** `C-COLOCATED-RESONANT-RECORD-TWO-PLACE-ACCOUNT-N`
- **Status:** `NON-CANONICAL / L1` (incubation notes package; conditional analytical proof `candidate-T`, bounded local finite audit `candidate-C`).
- **Public baseline:** `mathorn1973/twist-j` `main` `d4d363722f052141a4ce65e9da39f11a74b43b95` (`Public Canon v109`, content commit `2b0f94ec1e0874bff9141259e0b7da80e6681ea6`).
- **Scientific execution count BEFORE this prospective source pin:** `ZERO`. Neither `verify.py` nor `break.py` has been executed or imported; only static `ast.parse` syntax checking and SHA-256 hashing have occurred prior to the prospective Git commit.

---

## 1. Frozen Mathematical Specification and Sources

The complete mathematical specification is fixed in `PROOF.md` (Sections 1–7, Theorems 1–5 and Propositions 1–2) and `SOURCES.md`:

- `README.md`: `4231` bytes, SHA-256 `6ef418c8e8d372e99888a32112543d77f851d9d17c2e01fce68062206e309216`
- `SOURCES.md`: `3127` bytes, SHA-256 `416714dcd949f2d93633459e76d44e44abd974c98a40842d315ce546176acc25`
- `PROOF.md`: `25877` bytes, SHA-256 `428b9ca0072bf9e997898b9d3e6de5b9f9a4a23c4b855169c4782ec693a75c04`
- Primary verifier `verify.py` (4-component power basis `(1, j, j^2, j^3)`, quadratic forms `S_0, S_1, S_2`, reduced co-located step `d = (v - x)/2`):
  - `30892` bytes, SHA-256 `e2daf2f53e1e2e1410bb1fdd5a09a108c081e8b7a1ecb9090809c9ea05edc692`
- Independent checker `break.py` (5-component cyclic group ring `Z[C_5]` modulo `(1, 1, 1, 1, 1)`, 5-cyclic convolution, autocorrelation extraction `A = p_0 - p_1, B = p_1 - p_2`, `4x4` rational multiplication matrix trace/determinant checks, unreduced loaded contact step `d = (2v - x - e_v + F)/4`):
  - `31928` bytes, SHA-256 `a1dd4213b92731f7f5050eccbfc36a2cf30a2f92c4c0b2755574afcf8f96f9ec`

All arithmetic uses Python standard-library `int` and `fractions.Fraction`. No floating-point numbers, numerical tolerances, random sampling, or external packages are permitted.

---

## 2. Frozen Finite Fixture Inventory (`A1`–`A6`)

1. **`A1` (Two-place Galois/Hermitian account and conjugate trace decomposition):**
   - Check $J J^{-1} = 1$ for $J = 1 + j^2$ and $J^{-1} = -j - j^2$.
   - Check $h(1 - j^2) = 2 + \phi$, $h(1 - j^4) = 3 - \phi = \sigma_2(2 + \phi)$, $h(J) = 2 - \phi$, $h(3 + j^2) = 10 - 3\phi = 4h(J) + h(1 - j^2)$, and their traces and norms.
   - Across all $625$ elements $c \in \{-2, -1, 0, 1, 2\}^4 \subset O$:
     - Verify $c\bar{c} = A_c + B_c\phi$, $Q(c) = 2A_c + B_c = \frac{1}{2}\operatorname{Tr}_{K/\mathbb{Q}}(c\bar{c})$, $N_{\mathbb{Q}(\phi)/\mathbb{Q}}(h(c)) = A_c^2 + A_c B_c - B_c^2 = N_{K/\mathbb{Q}}(c)$, strict positivity for $c \neq 0$,
     - Verify $h((1 - j^2)c) = (2A_c + B_c) + (A_c + 3B_c)\phi$ and $h((1 - j^4)c) = (3A_c - B_c) + (2B_c - A_c)\phi$,
     - Verify $Q((1 - j^2)c) = 5(A_c + B_c)$, $Q((1 - j^4)c) = 5A_c$, $Q((1 - j^2)c) + Q((1 - j^4)c) = 5Q(c)$, equality $Q((1 - j^2)c) = Q((1 - j^4)c) \iff B_c = 0$ (where $2Q((1 - j^2)c) = 5Q(c)$), and $5h(c) = (3 - \phi)h((\rho - 1)c)$.
     - Verify the counterexample pair $c_1 = 1 - j^2$, $c_2 = 1 - j^4$ with $Q(c_1) = Q(c_2) = 5$ and $Q((1 - j^2)c_1) = 15 \neq 10 = Q((1 - j^2)c_2)$.
2. **`A2` (Iff resonance theorem for the 2-contact returning selector):**
   - Check the slot-sum counterexample $(a, c) = (1, 1)$.
   - Across all $81 \times 80 = 6480$ pairs $(a, c) \in \{-1, 0, 1\}^4 \times (\{-1, 0, 1\}^4 \setminus \{0\})$ on $W_{\mathrm{sel}} = C(x, z) \circ C(x, h)$ from $(x, h, z, u) = (a, a+2c, 0, -2a-2c)$ with $F = -a$:
     - Check all 6 primitive-cut invariants ($G_A = F+x=0$, $G_B = F-\sum_B v=0$, total slot sum, individual mod-$5$ residues, complete scalar account $E_{\mathrm{full}}$, complete Hermitian account $H_{\mathrm{full}}$) at every forward cut (`2`) and every literal inverse cut (`8`), totaling $64,800$ cuts.
     - Check that $2a + 2c = 3a + (1 - \rho)c \iff a = Jc$, and that Step 2 is admitted and restores $(x_2, F_2) = (a, -a)$ **if and only if** $a = Jc$.
   - Across all $624$ non-zero seeds $c \in \{-2, -1, 0, 1, 2\}^4 \setminus \{0\}$ at resonance $a = Jc$, verify $(Jc, (3+\rho)c, 0) \to (2c, 2Jc, 0) \to (Jc, 2Jc, (1-\rho)c)$, $h(h_0) = h(h_1) + h(z_2)$, $Q(h_0) = 17A_c + B_c$, $Q(h_1) = 12A_c - 4B_c$, $Q(z_2) = 5(A_c + B_c)$, and total step area $2h(c)$.
3. **`A3` ($\mathbb{F}_{16}$ inertness and 5-phase one-hot selectivity iff $c \notin 2O$):**
   - Verify that all $15 \times 15 = 225$ products of non-zero cosets in $O/2O$ are non-zero mod $2O$.
   - Across $81$ odd seeds ($\{-1, 0, 1\}^4 \setminus \{0\}$ plus $c_{\#1957} = (-1, -2, -2, 0)$) and $81$ even seeds $2c$ (`162` seeds $\times 5$ phases $m \in \{0..4\} = 810$ runs of the 10-contact bank $W_{\mathrm{bank}}$ plus 40-contact inverses = $40,500$ cuts):
     - Check all 6 primitive-cut invariants at all $40,500$ cuts and exact 40-contact state restoration.
     - Verify that all 5 phase inputs achieve one-hot selectivity (leaving all $k \neq m$ untouched, writing $z_m' = (1-\rho)c\rho^m$ with $Q(z_m') = 5(A_c + B_c)$ and path area $2h(c)$, and restoring $(x, F)$) **if and only if** $c \notin 2O$ (`81` odd seeds pass; `81` even seeds fail at $m=1, k=0$).
4. **`A4` (Exact instantiation of PR `#1957` `35`-quantum):**
   - Verify $c_{\#1957} = (1-\rho)J^{-1} = (-1, -2, -2, 0) \in O \setminus 2O$, $h(c_{\#1957}) = 3 + 4\phi$, $Q(c_{\#1957}) = 10$, and across all $5$ phases $k \in \{0..4\}$: $Q(a_k) = 5$ ($2+\phi$), $Q(h_{0,k}) = 55$ ($18+19\phi$), $Q(h_{1,k}) = 20$ ($8+4\phi$), $w_0 = Q(z_{2,k}) = 35$ ($10+15\phi$), active area $6+8\phi$ (half-trace $20$), and two-selector port responses `P27 -> (0, 35)`, `P35 -> (35, 0)`.
5. **`A5` (Conditional closure of the work-to-count identity `(9a)`):**
   - Across all $81$ odd seeds and $12$ multi-channel click-count profiles (`4860` channel evaluations), verify in exact `Fraction` arithmetic that $\bar{w}_k = w_0(c) = 5(A_c + B_c)$ is channel-invariant and that both $W_{\mathrm{rec}, k}/\sum_i W_{\mathrm{rec}, i} = N_k/\sum_i N_i$ and the two-place Hermitian record shares equal $N_k/\sum_i N_i$.
6. **`A6` (Operational boundaries — dead-time lock, unarchived backreaction, and `2b^n` free-mode denominators):**
   - Across all $81 \times 5 = 405$ odd-seed phase channels, verify that a repeat pulse $x = Jc\rho^m$ on discharged $h_m^{(1)} = 2Jc\rho^m$ refuses both contacts when $z_m = 0$ is a fresh blank (dead-time lock), whereas leaving $z_m^{(1)} = (1-\rho)c\rho^m$ in the port causes Contact 2 to fire ($d_2 = -\rho^{m+1}c \in O$) and disturb $(x, z_m)$ to $((1+\rho^2)c\rho^m, (1-\rho^2)c\rho^m)$.
   - For both modes $(a_0, b) \in \{(5, 4), (7, 6)\}$ and all $n = 1, \dots, 25$, verify that $\cos(n\omega) = P_n / (2b^n)$ has odd $P_n$ coprime to $2b^n$, irreducible denominator $D_n = 2b^n$, and $e_0 \cos(n\omega) \notin O$ for primitive $e_0$ while $2b^{25} e_0 \cos(n\omega) \in O$.

---

## 3. Pass/Fail Threshold and Resource Ceiling

- **Failure threshold:** Zero tolerance. Any assertion failure, invariant discrepancy, or non-zero exit code is a hard failure that must be retained unchanged.
- **Cross-check requirement:** Both `verify.py` and `break.py` must exit `0` with empty `stderr` and produce byte-for-byte identical `stdout`.
- **Resource ceiling:** `120` seconds wall-clock time and `1 GiB` RAM per script.
