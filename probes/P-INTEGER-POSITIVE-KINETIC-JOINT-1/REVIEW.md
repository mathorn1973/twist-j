# Self-Review: P-INTEGER-POSITIVE-KINETIC-JOINT-1

## 1. Custody and Prospective Integrity

- **Prospective pin commit:** `bd7e1dada3a4869ecfae76c0aea03c0a88c9983f`
- **Public pin receipt (posted before any execution):**
  https://github.com/mathorn1973/twist-j/issues/1647#issuecomment-6269491226
- All 6 prospective files (`PREREG.md`, `PROOF.md`, `SOURCE.md`,
  `verify.py`, `breaker.py`, `FROZEN.sha256`) were committed, pushed, and
  read back remotely from GitHub before running `verify.py` or
  `breaker.py`.
- Zero post-pin modifications were made to any of the 6 frozen files.

## 2. Independent Implementation Audit

- `verify.py` (27218 bytes, SHA-256
  `7fdea52ae7f106f45104bb7d7a7e9f7d13f36c8a1f9e14cc028ed5f634fbfd3b`)
  evolves the 21-integer core via the integer recurrence
  $P' = m^{k-1}C P - r_k W + Y\ell$ and
  $Y' = m^k Y - r_k V + a D_{k+1} + \langle \ell, P\rangle$, inverts via
  modulo-$r_{k-1}$ congruence, and implements $\mathbb{Z}[\zeta_5]$
  Hermitian matrices by polynomial multiplication modulo
  $1 + j + j^2 + j^3 + j^4$.
- `breaker.py` (39476 bytes, SHA-256
  `071bd62a5ef52a03f413ff6069fc0e3f468615dfde73ca09d4cdd9add2009ec9`)
  evolves rational fields and sources via `Fraction`, checks backward
  integrality at scale $D_{k-2}$, evaluates spatial quadratic forms by
  cyclic edge differences (`edge_quadratic`) without calling `laplacian`,
  and computes 8-integer Hermitian transports by closed-form coordinate
  maps.
- Both scripts produce the exact same 680-byte, 23-line certificate
  (SHA-256
  `3accd1e0633cb07e10410bb6df112d4712b789c6bd50dc62226ae7674667d334`).

## 3. Post-Review Scope Narrowing and Frozen-Text Wording Errata

In response to the public review on PR #1648
(`https://github.com/mathorn1973/twist-j/pull/1648#issuecomment-6270208985`),
the post-run files (`RESULT.md`, `REVIEW.md`, `README.md`) and PR
description have been updated as follows while preserving all 6 frozen
files and `EXPECTED.txt` intact:

1. **Homogeneous ($a=0$) vs affine ($a\ne 0$) symplectic Wronskian scope:**
   `PREREG.md` §4.3 and `PROOF.md` §4.3 correctly restrict the uncentered
   two-solution Wronskian $\Omega_n^+$ (`SYMPLECTIC_CHECKS=540`) to the
   homogeneous context $a = 0$. On uncentered affine solutions with
   $a \ne 0$, $\Omega_{n+1}^+ - \Omega_n^+ = a(\chi_n^{(1)} - \chi_n^{(2)})$
   (e.g. at `(0010, 0011)` and $a=+1$, $\Omega_1^+ = \Omega_2^+ = 1/4$ but
   $\Omega_3^+ = 163/648$). For general fixed $a$, symplectic conservation
   holds for tangent variations or differences from a common particular
   solution.
2. **Uncoupled quadratic bond form $\mathcal{H}_{\mathrm{phys},n}$ and
   interaction energy account:**
   $\mathcal{H}_{\mathrm{phys},n} = \mathcal{H}_{h,n} + \mathcal{H}_{\chi,n} > 0$
   is the quadratic bond energy of the two uncoupled operators around the
   uncoupled equilibrium $(\frac{1}{5}\mathbf{1}, a)$, satisfying the exact
   work balance $\mathcal{H}_{\mathrm{phys},n+1} - \mathcal{H}_{\mathrm{phys},n} = W_n$
   (`HAMILTONIAN_CHECKS=720`, `ZERO_SOURCE_WORK1=1/839808`). In the witness
   `0011`, $a=0$, $\mathcal{H}_{h,1} = \mathcal{H}_{h,2} = 53/432$ and
   $\mathcal{H}_{\chi,2} = 1/839808$: the gain comes from the interaction
   term $W_n = g_n(B_{n+1} - B_n)$ with $g_n = 324^{-n}$ and
   $B_n = \frac{1}{2}(\chi_n\langle\ell,h_{n-1}\rangle + \chi_{n-1}\langle\ell,h_n\rangle)$,
   so $J_n = \mathcal{H}_{\mathrm{phys},n} - g_{n-1}B_n$ satisfies
   $J_{n+1} - J_n = (g_{n-1} - g_n)B_n$.
3. **Terminology and count errata:**
   - $\Omega_n^+$ is the canonical alternating symplectic form associated
     with the positive-definite kinetic metric $I_6 \succ 0$.
   - `OFFSHELL_VARIATIONS=36` evaluates 36 gradient components on 6
     off-shell triples with at least one nonzero component per triple (18
     zero and 18 nonzero components).
   - The funded map $F$ is a reversible bijection ($F^{-1} = \mathrm{Rev}\,F\,\mathrm{Rev}$),
     where $\mathrm{Rev}$ is the involution.
   - Exact centered finite differences equal analytical partial derivatives
     because $A_{\mathrm{pos}}$ is quadratic.

## 4. Remaining Limitations

1. **Step-dependent coupling scale vs autonomous total Hamiltonian:**
   Because $g_n = m^{-n}$ varies with $n$, $J_{n+1} - J_n = (g_{n-1} - g_n)B_n$
   is not identically zero. Autonomous constant-coupling evolution with an
   interaction-inclusive conserved total energy and discrete Legendre map
   is established in the successor probe
   `P-INTEGER-AUTONOMOUS-JOINT-ENERGY-1` (Draft PR #1650, issue #1649).
2. **Linear 3+1 TT and 1D ring idealization:**
   The probe treats the linearized TT sector on the 5-site ring with a
   scalar source; nonlinear gravitational terms and constraint propagation
   remain open.
