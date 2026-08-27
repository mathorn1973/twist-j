# P-O5-SQUAREFREE-CORE-1 result

Status: **WRITTEN UNIVERSAL PROOF SURVIVES / FORMAL AUDIT 9 OF 9 PASS / PUBLIC TWO-ARCHITECTURE REPLAY PENDING / CANON UNCHANGED**

## Disposition

The frozen squarefree-core theorem package survives its one accepted local formal audit. The all-prime and all-integer theorem is carried by the written proof in `PREREG.md`; the finite verifier is an exact audit of the frozen mechanisms and controls.

A later sealed Canon fold may decide whether to register:

```text
O5-SQUAREFREE-CORE [T]
```

at the exact analytic-number-theory scope below. This probe itself changes no public row and proves no RH or GRH statement.

## Exact result

For the public split-prime scalar factor

\[
O_5(s)
=
\prod_{\chi_5(p)=1}
\frac{(1-p^{-s})^2}{1+p^{-2s}},
\qquad \Re(s)>1,
\]

define

\[
S_5(s)
=
\prod_{\chi_5(p)=1}(1-2p^{-s})
\]

and

\[
A_5(s)
=
\prod_{\chi_5(p)=1}
\frac{(1-p^{-s})^2}
{(1+p^{-2s})(1-2p^{-s})}.
\]

Then

\[
\boxed{O_5(s)=A_5(s)S_5(s)}
\qquad (\Re(s)>1).
\]

At one split prime, with `T=p^-s`,

\[
A_p(T)-1
=
\frac{2T^3}{(1+T^2)(1-2T)},
\]

and

\[
A_p(T)^{-1}-1
=
-\frac{2T^3}{(1-T)^2}.
\]

Both deviations start exactly at degree three.

The smallest split rational prime is 11. For every compact subset of `Re(s)>1/3`, the exact `9/20` guard gives uniform nonvanishing of the local factors, and the written bounds

\[
|A_p-1|<26p^{-3\sigma_0},
\qquad
|A_p^{-1}-1|<7p^{-3\sigma_0}
\]

are summable. Therefore

\[
\boxed{
A_5\text{ and }A_5^{-1}
\text{ are holomorphic nowhere-zero Euler-product units on }
\Re(s)>\frac13.
}
\]

Moreover their Dirichlet coefficients `a(n)` and `b(n)` satisfy, for every fixed real `theta>1/3`,

\[
\sum_{n\ge1}|a(n)|n^{-\theta}<\infty,
\qquad
\sum_{n\ge1}|b(n)|n^{-\theta}<\infty.
\]

## Exact squarefree carrier

Let

\[
S_5(s)=\sum_{n\ge1}s_5(n)n^{-s}.
\]

Then

\[
\boxed{
s_5(n)
=
\begin{cases}
(-2)^{\omega(n)},&
n\text{ squarefree and every prime divisor is split},\\
0,&\text{otherwise}.
\end{cases}
}
\]

Using the registered ideal-count theorem `a_F=1*chi_5` for `F=Q(sqrt5)`, the same sequence is

\[
\boxed{
s_5(n)=\mu(n)a_F(n)\mathbf 1_{(n,5)=1}
}
\]

for every positive integer.

Thus on squarefree split input with `a=omega(n)`, the magnitude `2^a` is exactly the number of independent choices of one prime ideal from each unordered conjugate pair, while the sign is the ordinary Mobius parity `(-1)^a`. No global orientation is selected.

## Summatory equivalence

Write

\[
T_5(x)=\sum_{n\le x}o(n),
\qquad
S_5^{\rm sum}(x)=\sum_{n\le x}s_5(n),
\]

where `o(n)` are the coefficients of the public `O_5` factor.

The exact Dirichlet coefficient identities are

\[
o=a*s_5,
\qquad
s_5=b*o.
\]

The absolute coefficient convergence of both `a` and `b` therefore gives, for every fixed real `theta>1/3`,

\[
\boxed{
T_5(x)=O(x^\theta)
\iff
S_5^{\rm sum}(x)=O(x^\theta).
}
\]

This is the scientific point of the result: every higher split prime-power tail in `O_5` is removable by a unit already to the left of the critical line. Any power cancellation question with exponent greater than `1/3` can be studied on the squarefree split carrier without loss.

This theorem does not itself supply such cancellation.

## Gate readout

```text
G01 PASS  exact local O_p=A_p(1-2T)
G02 PASS  exact cubic onset of dressing and inverse
G03 PASS  first split prime 11 and exact 9/20 guard
G04 PASS  coefficient formula through n=50000
G05 PASS  local formal series through degree 16
G06 PASS  exact majorant constants 26 and 7
G07 PASS  both Dirichlet convolutions through n=20000
G08 PASS  stdlib-only exact-integer source firewall
G09 PASS  all five production-path breakers
```

The finite bounds audit the universal written proof. They are not the theorem scope.

## Fired negative controls

All frozen controls fired through the same local or coefficient mechanisms used by the positive path:

```text
B1  wrong core 1-T:
    first dressing defect degree 1, global first split witness n=11.

B2  wrong core (1-T)^2:
    first dressing defect degree 2, global witness n=121.

B3  omit ramified cutoff:
    first coefficient disagreement n=5.

B4  treat inert 2 as split:
    first support disagreement n=2.

B5  delete the (1+T^2) local denominator:
    exact rational-function identity fails.
```

No falsifier against the frozen theorem fired.

## Scope boundary

This result does not construct or consume meromorphic continuation of `O_5`, does not consume issue #590, locates no zero or pole, and makes no RH or GRH claim.

It supplies no `O(x^(1/2+epsilon))` estimate, no Hecke or automorphic character, no global orientation selector, no probability or Haar interpretation, no physical dictionary, and no L1-L6 lift.

`TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` remains unchanged.

The distinct in-flight `P-O5-DEDEKIND-GRH-DIVISOR-READ-1` lane remains separate and owns the divisor-coordinate question.

## Evidence boundary

The accepted local formal leg is:

```text
platform:       Linux
architecture:   x86_64
python:         CPython 3.13.5
pin:            f80ff006c5be1793772addc636d328cfb073e407
verifier SHA256:0df92255bc7b770b5e521e205b2ad10e0c56ac8577dffc61194f65c62f117c4c
stdout SHA256:  830c1a1550c51c404d6c4a944c4108027b9fb795cf483306998c48f38ad69525
stdout bytes:   476
stderr bytes:   0
result:         VERIFY RESULT 9/9 ALL PASS
```

The repository pull-request workflow must replay the unchanged pinned verifier with Python 3.12 on GitHub-hosted x86_64 and aarch64 and require byte identity with `EXPECTED.txt`. Until that workflow passes, the public two-architecture replay is pending.

The written proof, not architecture count, is the proposed theorem-grade source. The verifier audits it.

No Canon, Registry, Frontier, dependency, gate, evidence, workflow, Note, reproduction, or existing probe is changed by this result.
