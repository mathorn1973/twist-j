# R-LAMBDA-COCYCLE-CONDUCTOR-CAPACITY-1-N-REVIEW

STATUS: NON-CANONICAL independent review, no authority
REVIEWED OBJECT: `C-LAMBDA-COCYCLE-CONDUCTOR-CAPACITY-1-N`, `RESULT.md` sha256 `21bf7204…99f1a`
BASIS: PUBLIC, Public Canon v46
LAYER: L6 spectral measure only
DATE: 2026-08-14
REPOSITORY EFFECT: none. No Canon, Registry, release, status or RH change.

## 0. Reproduction leg

Second independent architecture leg for the reviewed package.

| item | result |
|---|---|
| `SHA256SUMS.txt` | 6 of 6 OK |
| `verify.py` | exit 0, stdout sha256 `aa2847e5…6ed0c`, byte-identical to shipped `verify.stdout` |
| `break.py` | exit 0, stdout sha256 `3407c3a6…f6f5`, byte-identical to shipped `break.stdout` |
| platform | x86_64, Ubuntu 24.04.4 LTS, CPython 3.12.3, sympy 1.14.0, mpmath 1.3.0 |

Theorems 1 to 5 were additionally re-derived by hand rather than only re-run.
Confirmed: the `cot` inversion including the strict and non-strict endpoints;
`19/27 - 1/2 = 11/54`; the optimisation `C = 9/\sqrt{11}` with
`f^\* = 11\sqrt{11}/1458`; the capacity threshold `\kappa = 22/27`; the degree
coefficient `11/270`; and `\min \varphi(\mathrm{ord}\,\xi) = q_B/5` over the three
admissible exact orders. The `\S 6` breaker correction is correct and necessary.

Nothing in sections 1 to 5 of the reviewed note is withdrawn by this review.

## 1. R1, correction of a claim about scope

Theorem 4 carries no information about the cocycle vector.

The set `\mathbb T \setminus G_A` is invariant under conjugation. Combined with
the symmetrisation identity `(\mu_v + \check\mu_v)/2 = \sigma/2` this gives
`\check\mu_v(\mathbb T\setminus G_A) = \mu_v(\mathbb T\setminus G_A)`, hence

$$
\mu_v(\mathbb T\setminus G_A) = \tfrac12\,\sigma(\mathbb T\setminus G_A) = \tfrac{R_A}{2}
\qquad\text{for every } v .
$$

The quantity bounded in Theorem 4 is therefore a functional of `\sigma` alone.
Theorem 4 is Theorem 3 composed with the Markov inequality, not an independent
constraint on the carrier.

Consequence for `\S 7`. The sentence

> It narrows the only surviving carrier class to genuinely rough `L^2` vectors.

should be withdrawn. The class was never wider: every realising vector has the
same mass outside every `G_A`, so nothing has been narrowed.

This strengthens rather than weakens closure route 1. Since no vector whatsoever
can lie in `\mathrm{Dom}(\mathcal C_5^{1/4})`, any proof that a Canon-natural
construction necessarily produces a vector in `\mathrm{Dom}(\mathcal C_5^{1/4})`
fires `LAMBDA-COCYCLE-ANGLES [H]` immediately. Route 1 is the only lever in the
package and should be listed first in `\S 7`, not as one of three peers.

## 2. R2, improvement of the Theorem 3 constant by a factor `\sqrt 7`

Theorem 3 uses a single dyadic window. Taking all windows `T_j = 2^j T_0`,
`j \ge 0`, window `j` contributes

$$
\frac{11}{216\pi C}\,2^{-j} \;-\; \frac{1}{8\pi C^3}\,8^{-j}
$$

to `\sqrt{q_A}\,R_A/(\log q_A)^{3/2}`. Both series converge:

$$
\sum_{j\ge 0}\left(\frac{11}{216\pi C}2^{-j}-\frac1{8\pi C^3}8^{-j}\right)
=\frac1\pi\left(\frac{11}{108\,C}-\frac1{7\,C^3}\right).
$$

The maximum is at `C^\* = 18/\sqrt{77}`, and every window from `j = 0` upward is
already positive there, since `27/(11 C^{\*2}) = 7/12 < 1`.

### Theorem 3', candidate-T, conditional on RH

$$
\liminf_{A\to\infty}\frac{\sqrt{q_A}\,R_A}{(\log q_A)^{3/2}}
\;\ge\;\frac{11\sqrt{77}}{2916\pi}
\;=\;\sqrt 7\cdot\frac{11\sqrt{11}}{2916\pi}.
$$

The exponent is unchanged and so is the threshold `s = 1/4`. That is the point
worth recording: the threshold survives a factor `\sqrt 7` in the constant, which
shows it is structural and not an artefact of the Bui and Heath-Brown proportion
`19/27`. Any future improvement of that proportion likewise moves the constant
only.

## 3. R3, Theorem 5 is already optimal for this method

Running the Theorem 5 argument in window `j` allows `\kappa` up to
`(22/27)\cdot 4^j`, but the zero produced then satisfies
`\gamma \le 2^{j+1}T`, so `T^2 \ge \gamma^2/4^{j+1}` and the factor `4^j` cancels
exactly:

$$
\frac{22}{27}\cdot\frac{4^{j}}{5\cdot 4^{j+1}}=\frac{11}{270}
\qquad\text{for every } j .
$$

The degree coefficient is window-invariant. This is worth recording so the
window-widening idea is not attempted a second time.

## 4. R4, closure route 3 cannot be reached by a height argument

For any root of unity `\xi \ne 1`,

$$
\rho=\frac1{1-\xi},\qquad \operatorname{Re}\rho=\tfrac12,\qquad
h(\rho)=h(1-\xi)\le\log 2 ,
$$

the last step because `h(1)=h(\xi)=0` and `h(a-b)\le h(a)+h(b)+\log 2`, with
`h(1/x)=h(x)`. The height is bounded uniformly while Theorem 5 makes the degree
unbounded, so Northcott finiteness never fires. Closure route 3 in `\S 7` needs a
transcendence input for a specific zero, not a height or a finiteness argument.
`\S 7` should say so, otherwise the route reads cheaper than it is.

## 5. Out-of-lane material

The frozen PREREG states that no numerical zero table is admissible. A grid
probe was nevertheless run as a decision aid and is filed under `out-of-lane/`
with that label. It is not evidence, it is not gated, and it supports no claim in
this review.

Result, for the record only: first 30 zeros at 250 digits, levels `A \le 300`, no
grid hit; the closest approach over all 9030 pairs is `6.8\cdot10^{-5}`, which is
what equidistribution predicts for that sample size. No anomaly, no concentration.

## 6. Decision

**[NON-CANONICAL review, no status change]**

The reviewed package stands. Four edits are proposed to it, none of which touches
Theorems 1 to 3 or 5 as proved:

1. withdraw the carrier-narrowing sentence in `\S 7` and restate Theorem 4 as a
   corollary of Theorem 3 under Markov;
2. promote closure route 1 to the head of `\S 7` with the reason given in R1;
3. fold Theorem 3' as the sharpened constant, or record `\sqrt 7` as a remark;
4. add the window-invariance remark of R3 and the height remark of R4 as
   negative results, so neither route is re-attempted.

## Reproduction

```
sha256sum -c SHA256SUMS.txt
python3 verify.py          # exit 0, ALL PASS
```

`verify.py` uses no zeta-zero table. It re-derives the reviewed constants from
scratch in section 0 before checking R1 to R4.
