# P-O5-GOLDEN-AXIS-BAND-1 result

Status: **CANDIDATE-T / PROOF-FIRST / LOCAL FORMAL LEG PASS / PUBLIC TWO-ARCHITECTURE REPLAY PENDING / CANON UNCHANGED**

## Verdict

The frozen written proof survives the accepted exact audit.

Put

```text
alpha=phi^2,
X_k=L_(2k)-1=floor(alpha^k).
```

With the unit shell `I_-1={1}` and, for `k>=0`,

```text
I_k={L_(2k),...,L_(2k+2)-1},
```

the positive integers are partitioned by the multiplicative unit intervals

```text
alpha^k<n<=alpha^(k+1).
```

For the restricted Mobius sequence `nu` of merged probe
`P-O5-FIRST-SHELL-BILINEAR-SQUARE-1`, define

```text
P_s(Y)=sum_(i+j=s)sum_(a in I_i,b in I_j,ab<=Y)nu(a)nu(b).
```

The ordinary bilinear hyperbola carrier decomposes as

```text
H(Y)=sum_(s>=-2)P_s(Y).
```

The exact inequalities

```text
alpha^2<11<alpha^3
```

force the ratio-11 annulus to have uniformly finite range on the golden shell
axis. If `N in I_m`, `m>=3`, and `M=floor(N/11)`, then

```text
P_s(N)=P_s(M)   for s<=m-5,
P_s(N)=P_s(M)=0 for s>=m+1,
```

hence

```text
Q_11(N)
 = sum_(s=max(-2,m-4))^m [P_s(N)-P_s(M)].
```

For `m>=4` this is exactly five adjacent anti-diagonals.

At the exact Lucas cutoff

```text
N=X_K=L_(2K)-1, K>=4,
M=floor(N/11),
```

one has `M in I_(K-3)` and the sharper four-diagonal normal form

```text
Q_11(X_K)
 = [D_(K-4)-P_(K-4)(M)]
   +[D_(K-3)-P_(K-3)(M)]
   + D_(K-2)
   + P_(K-1)(X_K),
```

where `D_s=sum_(i+j=s)u_i u_j` and `u_i=sum_(n in I_i)nu(n)`.

This is an exact localization theorem. It is not a cancellation estimate.

## Accepted exact audit

```text
pin_commit:       0038e753efa7fe828eb3c1a7d3f332a96ea75524
verifier_sha256:  94c0ae4185fc9ca764d1cef64209ca922119a79f8140256c92783471db2d839c
stdout_sha256:    697dc1a869c0fd34e35caedb41390668b256ff6476e5c2977ac91d792754aff9
stdout_bytes:     408
stdout_lines:     9
exit_code:        0
stderr_bytes:     0
readout:          VERIFY RESULT 8/8 ALL PASS
```

Frozen breakers fired at their preregistered witnesses:

```text
B1 wrong unshifted Lucas cutoff:       k=1
B2 false 11<alpha^2 inequality:        exact square comparison
B3 deleted lower outer diagonal:       N=322, contribution -4
B4 deleted upper outer diagonal:       N=361, contribution +1
B5 false one-shell product rule:       19^2 in I_6, 41^2 in I_7
```

## Scientific boundary

The Lucas-floor theorem, complete unit-plus-Lucas shell partition, product
shell localization, five-diagonal full-axis band and four-diagonal Lucas-top
refinement are `candidate-T`.

No RH or GRH result, new summatory estimate, zero-free region, analytic
continuation, selected orientation, physical dictionary, probability
statement, SI statement or L1-L6 lift is claimed.

The theorem does not claim that arithmetic addition is replaced by Lucas
addition or that Nature uses a different number line. It establishes the
narrow mathematical fact suggested by the alternate-axis intuition: the
current multiplicative bilinear carrier becomes a finite-range operator when
indexed by the exact `phi^2`/Lucas cutoff scale.

Public Canon v67, Registry, Frontier, dependencies, gates, evidence, Notes and
all existing public rows remain unchanged.
