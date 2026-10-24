# Result: `C-HOMOGENEOUS-RECORD-RETENTION-N`

**PUBLIC, NON-CANONICAL. L1 result on the unchanged Public Canon v105 law.**

License: Apache-2.0.
Prospective pin: `24cc067983142017d3fd9a111acf80d6ab29db54`.
Run record: `reproduce/C-HOMOGENEOUS-RECORD-RETENTION-N/RUN.md`.

## 1. Outcome

The pinned verifier ran once with exit code 0, empty standard error and 187
passed checks in all six frozen groups. No falsifier fired. The frozen
quantitative target is **achieved** for the declared family:

```text
RETENTION TARGET T=1000000 eps=1/100: delta<=5.418e-10 eta<=7.475e-4 eps_cert<=7.475e-4 ACHIEVED
```

For every state of the declared ideal success family $\mathcal F$, every coded
memory/reference input and **every** $n\ge10^6$ macrosteps,
$\|(I-R_1)U_{\rm rec}^n\Omega_{{\rm rec},+}\mathcal T_+(\varphi\otimes\Phi)\|
\le7.475\times10^{-4}$, so the wrong-memory probability is below
$5.59\times10^{-7}$ and the full record (memory $d_1$ with the old memory in
the outgoing carrier label) is within $1.058\times10^{-3}$ in norm. The bound is
future-uniform: there is no end to the retention window.

Certified modulus (upper bounds, same theorem):

| $T$ (macrosteps) | $\sup_{n\ge T}\|(I-R_1)\psi_n\|\le$ |
|---|---|
| $2\cdot10^5$ | $2.090\times10^{-1}$ |
| $5\cdot10^5$ | $8.457\times10^{-3}$ |
| $10^6$ | $7.475\times10^{-4}$ |
| $10^7$ | $2.364\times10^{-7}$ |

Constants: $v_{\min}\ge0.833210$, $v_{\max}\le0.833435$, bound-pair velocity
$v_b\le0.02916$, energy spread $\le8.481\times10^{-4}\le h$, Neumann product
$\le0.8732$, separation rate $\kappa_c\ge0.4020$, Cook constant
$\le1.454\times10^{17}$, 19 terms in $\mathcal L^5$. The free-tail part
($5.4\times10^{-10}$) is negligible; the conservative interaction (Cook) part
dominates.

## 2. Exact results (all groups passed)

1. **Record location** (Theorem 1). The memory is exactly $d_1$ on the
   carrier-right component and holds its old value on the rest, so the
   wrong-memory probability equals $(1-\|\phi_1\|^2)\|\mathbf 1_{c<z}U^n\chi\|^2$
   for every one-carrier state and every time, uniformly over coded memory and
   reference inputs; each step changes it by $-\frac14$ of the carrier current
   through the receiver cut. Audited on the complete local law for four steps
   with writing and un-writing contacts, tokens and pulses on both sides and an
   entangled reference, with unitarity and two failing negative controls.
2. **Eraser and writers** (Theorem 2). Only the receiver edge touches the
   memory; leftward carrier crossings un-write exactly; contacts beyond the
   receiver leave the record unchanged.
3. **No uniform modulus** (Theorem 3). Over the whole success sector the
   supremum of the wrong-memory amplitude is 1 at every time.
4. **No exact permanence of the free surrogate** (Theorem 4). A nonzero
   right-moving pulse is never entirely beyond the receiver; the v105 free tail
   is strictly positive at every time. Exact witness: a record held exactly at
   $n = 0,1,2$ is lost with probability $(1-\|\phi_1\|^2)\cdot1024/15625$ at
   $n = 3$.
5. **Eternal parked records** (Proposition 5). A dark token right of the
   receiver holds $d_1$ exactly for all times, with no write event and outside
   the success sector.

## 3. Negative and unachieved results (preserved)

- Exact permanent retention of a captured record: **not claimed**. Excluded for
  the free surrogate at every time; the interacting captured case is open.
- Uniform retention over the success sector: **impossible**.
- Retention of the actual normalized v105 selected component
  $Q_{\rm ch,full}\mathcal S\Psi_{\rm loc}/\sqrt{p(Q_{\rm full})}$: **not
  achieved**. Its time delay and position moments are not certified and its
  sharp spectral edges block the integration by parts; the minimal missing
  premise is in `PROOF.md` §7.
- Before $T$ no bound is asserted: the certified modulus exceeds the tolerance
  for $T\le2\cdot10^5$ and the record may still be in transit. This is a
  property of the conservative bound, not a measured excursion.
- For the full unpostselected v105 input the exact wrong-memory probability is
  $(1-\|\phi_1\|^2)(1-p_R(n))$; $p_R$ is not computed, and only
  $p(Q_{\rm full})>2/10^{28}$ is certified.

## 4. Status and scope

Status: NON-CANONICAL analytical result with an exact single-architecture run;
the two-architecture byte gate is supplied by the pull-request workflow. No
Canon, registry, frontier or status file changes. L1 only; no preparation,
detector, occurrence, many-carrier or spectral-energy-flow claim; no lock,
archive or reset added to the law. A candidate later fold could at most record
Theorems 1–4 and Proposition 5 as proved statements about the v105 law and
Theorem 6 as a bound for the declared family, after independent review.

## 5. What a reviewer should check

1. Time uniformity: monotonicity of $\bar\delta,\bar\eta$ and the sum bound in
   §6.9; the role of $T$ and of the reference slice.
2. Success conditioning: that $\mathcal F\subset\operatorname{Ran}Q_{\rm
   ch,full}$ (§6.1), that the normalization is inside the family only, and the
   separate unpostselected statement (Corollary 1.2).
3. Recrossing: Theorem 1 and the balance identity; the Hardy argument of
   Theorem 4; the open interacting permanence question.
4. Resources: unchanged law and charge, no lock; one-sided rational bounds,
   imported $M_0$, $N_{\min}$ and $W(P) = e^{iPQ}W(0)$.
5. Old-information accounting: Theorem 1 items 3–4 and Corollary 6.1.
