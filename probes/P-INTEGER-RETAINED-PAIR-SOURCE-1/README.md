# P-INTEGER-RETAINED-PAIR-SOURCE-1

**Status:** `NON-CANONICAL`, `L1` (`RESULT=PASS`).
**Public Lock:** [Issue #1698](https://github.com/mathorn1973/twist-j/issues/1698).
**Predecessor:** `C-JM-RETAINED-PAIR-SOURCE-N` ([PR #1681](https://github.com/mathorn1973/twist-j/pull/1681), [Issue #1680](https://github.com/mathorn1973/twist-j/issues/1680)).

## Overview

This formal two-architecture probe extends `C-JM-RETAINED-PAIR-SOURCE-N` (`PR #1681`) with:
1. **Theorem 1 (`PROOF.md` §1):** An explicit integral basis and trace-form bridge from $(J, M) = (1+j^2, 1+m+m^2)$ to the coordinate carrier $(S, G, \ell)$, proving $G = \operatorname{diag}(5I_4 - \mathbf 1_4\mathbf 1_4^T, 4I_4)$ ($\det G = 32\,000$, $\det G_S = 288\,000$, $\det G_R = 484\,128\,000$), $T_M(\mathbb Z^4) = \Lambda_3 = \{b_1 - b_2 - b_3 \equiv 0 \pmod 3\}$, and $\ell = (1, 10, 18, 16, -1, -27, -32, -3)$ via the unique mod-41 root lifts $(j \equiv 10, m \equiv 27) \pmod{41}$.
2. **Theorem 2 (`PROOF.md` §2):** A universal division-free integer pair involution $\widehat U_z$ on $\mathcal C = \mathbb Z^{81} \times \mathbb Z_{>0}$ that preserves the integer scale content $m(X, D) = \gcd(X, D)$, satisfies $\widehat U_z^2 = \mathrm{id}_{\mathcal C}$ for all $z \in \mathbb Z^8$, and maps $(e, 1) \leftrightarrow (y_z \otimes y_z, A_z)$.
3. **Theorem 3 (`PROOF.md` §3):** A 2-phase funded reversible integer pair-source automaton with positive-definite energy $E(\mathcal S)$ and bank $b \in \mathbb Z_{\ge 0}$ whose constant-budget level sets are finite and whose sharp $K$-round bank threshold
   $$b_{\mathrm{sharp}}(z, K) = 2K\bigl(A_z^2 - 1\bigr) + K^2 = 2K\,q(z)\bigl(q(z) + 2\bigr) + K^2$$
   is strictly independent of the initial occupied output-port state $P_0 = (X_{P_0}, D_{P_0})$.

## Contents

- `PREREG.md` — frozen preregistration, scope, and falsifiers.
- `PROOF.md` — analytical proofs of Theorems 1, 2, and 3.
- `SOURCE.md` — public basis and predecessor manifest.
- `verify.py` — primary exact verifier (invokes `breaker.py` in `python3 -I`).
- `breaker.py` — independent cyclic-vector / dictionary-state implementation.
- `FROZEN.sha256` — pre-execution SHA-256 manifest of the 5 pinned files.
- `EXPECTED.txt` — exact 24-line deterministic stdout (`1562` bytes).
- `RUN.md` — formal execution record.
- `RESULT.md` — earned `L1` results and scope boundaries.

## Reproduction

```bash
python3 -I probes/P-INTEGER-RETAINED-PAIR-SOURCE-1/verify.py
```
