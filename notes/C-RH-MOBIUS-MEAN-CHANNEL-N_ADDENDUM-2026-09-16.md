# C-RH-MOBIUS-MEAN-CHANNEL-N — addendum 2026-09-16

```text
STATUS      NON-CANONICAL addendum to PR #979
DATE        2026-09-16
BASIS       C-RH-MOBIUS-MEAN-CHANNEL-N.md at head 0ecc82a234176eba10e4c8d7a7069aa8524eff2c
REVIEW      PR #1020, notes/RH-ATTACK-2026-09-15/, plus REVIEW-2026-09-16/
AUTHORITY   none; no Canon, Registry, Frontier, gate or claim-status motion
```

This addendum narrows the interpretation of target (41), records an independent review of identities (12)–(14), and closes one finite support class for certificate target (29). The source note remains unchanged for auditability; where this addendum narrows a handoff sentence, the narrower statement is the intended continuation rule.

## 1. Independent check of (12)–(14)

With

\[
s_Q(u)=\sum_{k\le u}t_Q(k),
\qquad
T_Q(u)=\sum_{k\le u}\frac{t_Q(k)}k,
\]

finite summation by parts gives

\[
\sum_{u=1}^{K-1}\frac{s_Q(u)}{u(u+1)}
=
\sum_{k<K}t_Q(k)\sum_{u=k}^{K-1}\frac1{u(u+1)}
=
\sum_{k<K}\frac{t_Q(k)}k-rac1K\sum_{k<K}t_Q(k)
=
\gamma_{Q,K}.
\]

This proves (12).

For one cut, writing the floor-difference source as a sum over quotient levels and collecting the balancing term gives

\[
e_K(n)=
\sum_{\ell=1}^{\lfloor n/K\rfloor}
 s_Q\!\left(\left\lfloor\frac n\ell\right\rfloor\right)
+K\left\lfloor\frac nK\right\rfloor\gamma_{Q,K},
\]

which is (13). Finally, with

\[
P(u)=\sum_{a=1}^{u}T_Q(a),
\qquad
s_Q(m)=mT_Q(m)-P(m-1),
\qquad
P(K-1)=K\gamma_{Q,K},
\]

the balancing term cancels exactly under finite summation by parts and yields

\[
\boxed{
 e_K(n)=\sum_{u=K}^{n}T_Q(u)\bigl(r_{u+1}(n)-r_u(n)\bigr),
}
\]

which is (14). These are algebraic identities; no RH input is used.

## 2. Correct Hardy-space object for target (41)

For fixed `0 < eps <= 1/4`, let

\[
F_\varepsilon(x)=c_\varepsilon x-H_\varepsilon(\lfloor x\rfloor),
\qquad
c_\varepsilon=\zeta(1+\varepsilon)^{-1}.
\]

The Mellin transform attached to (41) is

\[
\boxed{
M_\varepsilon(s)
=
\frac{c_\varepsilon}{s-1}
-
\frac{\zeta(s)}{s\zeta(s+\varepsilon)}.
}
\]

Thus

\[
(41)_\varepsilon
\Longleftrightarrow
\|F_\varepsilon\|_\varepsilon<\infty
\Longrightarrow
M_\varepsilon\in H^2\!\left(\Re s>\frac12-\frac\varepsilon2\right).
\]

The bare quotient `zeta(s)/(s zeta(s+eps))` is not itself in that Hardy space because of its simple pole at `s=1`. The pole-subtracted expression above is the correct holomorphic object.

## 3. Strength guard: one epsilon gives shadows, an accumulating family gives a zero-free half-plane

From Hardy holomorphy away from `s=1`, every nontrivial zero with

\[
\Re\rho\ge\frac12+\frac\varepsilon2
\]

must satisfy

\[
\operatorname{ord}_{\rho-\varepsilon}\zeta
\ge
\operatorname{ord}_{\rho}\zeta.
\]

For a single fixed `eps`, this is a shadow condition. It is not, without an additional exclusion of exact `eps`-spaced zero chains, a proof that the half-plane to the right of `1/2+eps/2` is zero-free.

If instead (41) holds for infinitely many distinct values `eps_j -> eps_*`, then any zero with

\[
\Re\rho>\frac12+\frac{\varepsilon_*}{2}
\]

would force distinct zeros `rho-eps_j` with a finite accumulation point, impossible for zeta. Therefore

\[
\boxed{
(41)_{\varepsilon_j}\text{ for an accumulating family }\varepsilon_j\to\varepsilon_*
\Longrightarrow
\zeta(s)\ne0\text{ for }\Re s>\frac12+\frac{\varepsilon_*}{2}.
}
\]

In particular, an accumulating family at `eps_*=1/4` implies the zero-free half-plane `Re s>5/8`; accumulation at `0`, with the functional-equation symmetry, gives RH. No uniform bound in `j` is needed for this isolation step; finiteness at each member is enough.

Accordingly, item 6 of the source note's no-go ledger should be read together with this strength guard: changing constants in the present pointwise-envelope proof cannot make (41) uniform in `N`, and proving (41) itself is already a zero-location constraint through the shadow mechanism.

## 4. Exact finite obstruction for target (29)

Target (29) asks for a finite rational `q in E` with

\[
\delta_q^2=\|1-q\|_H^2\le\frac9{2^{23}}.
\]

The 2026-09-16 exact verifier in PR #1020 solves the complete weighted least-squares problem on `n=1,...,144` over

\[
E_{72}=\operatorname{span}\{r_2,\ldots,r_{72}\}
\]

and proves

\[
\frac{7601923}{10^9}
<
\min_{q\in E_{72}}
\sum_{n=1}^{144}\frac{|1-q(n)|^2}{n(n+1)}
<
\frac{7601924}{10^9}.
\]

The lower bound is more than `7000 * 9/2^23`. Since the remaining H-norm tail is nonnegative,

\[
\boxed{
q\in E_{72}
\Longrightarrow
\delta_q^2>\frac9{2^{23}}.
}
\]

This closes the entire support class `2,...,72` for target (29), not merely one set of coefficients. It does not exclude a certificate using larger indices and does not weaken the validity of transfer (28).

## 5. Revised handoff

Two continuation targets remain legitimate, but they are logically different.

1. **Analytic target:** prove (41) for a chosen fixed `eps`, preserving the joined Jacobi/Hankel form. Record the result first as a shadow condition. A family of such proofs with an accumulation point upgrades to a genuine zero-free half-plane by the isolation argument above.
2. **Finite target:** search for a certificate satisfying (29) only after changing support beyond `72` or improving the transfer. For any proposed finite `q`, the upper certificate must include the infinite H-norm tail; a finite partial sum alone is insufficient.

The addendum does not select between these routes and makes no RH-status motion.
