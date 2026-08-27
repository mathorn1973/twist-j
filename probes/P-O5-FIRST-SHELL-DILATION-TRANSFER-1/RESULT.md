# P-O5-FIRST-SHELL-DILATION-TRANSFER-1 result

Status: **CANDIDATE-T / PROOF-FIRST / LOCAL FORMAL LEG PASS / PUBLIC TWO-ARCHITECTURE REPLAY PENDING / CANON UNCHANGED**

## Verdict

The frozen written proof survives the accepted exact audit.

Let `B_11(N)` be the summatory function of `(-2)^omega(n)` on squarefree
integers supported only on split rational primes strictly greater than `11`,
and put

```text
D f(N)=f(floor(N/11)),
W_11=(I-D)B_11.
```

Then, exactly for every `N>=0`,

```text
S_5^sum = (I-2D)B_11,
W_11    = (I-D)B_11.
```

The function `W_11` is the `r(n)=11` terminal shell of merged probe
`P-O5-FIRST-MISSING-SHELL-1`:

```text
W_11(N)
 = sum_(N/11<n<=N, n squarefree,
        every p|n split and p>11) (-2)^omega(n).
```

The pointwise inversions are finite and exact:

```text
B_11(N)=sum_(j>=0)W_11(floor(N/11^j)),

S_5^sum(N)
 = W_11(N)-sum_(j>=1)W_11(floor(N/11^j)),

W_11(N)
 = S_5^sum(N)
   +sum_(j>=1)2^(j-1)S_5^sum(floor(N/11^j)).
```

On `Re(s)>1`,

```text
W_11(s)
 = ((1-11^-s)/(1-2*11^-s)) S_5(s).
```

For the weighted sup norm

```text
||f||_theta=sup_(N>=1)|f(N)|/N^theta,
```

the explicit absolute Neumann transfers give, whenever
`2*11^-theta<1`,

```text
||S_5^sum||_theta
 <= 1/(1-11^-theta) ||W_11||_theta,

||W_11||_theta
 <= (1-11^-theta)/(1-2*11^-theta)
    ||S_5^sum||_theta.
```

Hence

```text
S_5^sum(N)=O(N^theta)
iff
W_11(N)=O(N^theta)
```

for every fixed `theta>log_11(2)`. Since `2^3=8<11`, the equivalence applies
throughout `theta>1/3`, including every `theta=1/2+epsilon`.

This is a transfer theorem, not a cancellation estimate.

## Accepted exact audit

```text
pin_commit:       32aa778b7c08fe50946b14e89b16f0a6219c2b49
verifier_sha256:  b004c4f6adbbd14224bb4101ba975ac91d7cebc8325b148667ad05b35e8f95d9
stdout_sha256:    e102f9de3ea7d1d2f7f1f1927983af70107f46ee871874c0447eb32d55526c99
stdout_bytes:     368
stdout_lines:     9
exit_code:        0
stderr_bytes:     0
readout:          VERIFY RESULT 8/8 ALL PASS
```

Frozen breakers fired at the preregistered witnesses:

```text
B1 wrong optional-11 coefficient: N=11
B2 wrong dilation scale 19:       N=11
B3 missing j=0 inversion term:    N=1
B4 flat inverse weights:          N=121
B5 false theta=1/4 threshold:     2^4=16>11
```

## Scientific boundary

The exact first-shell identities, finite inversions, local quotient and
weighted power-bound equivalence are `candidate-T`.

No RH or GRH result, new summatory estimate, analytic continuation,
zero-location theorem, Hecke or automorphic object, selected split
orientation, physical dictionary, probability statement, SI statement or
L1-L6 lift is claimed. The theorem does not say that `W_11` is small. It says
that proving a power bound for this single annular shell is neither weaker nor
stronger than proving the same exponent for the complete squarefree split
carrier in the entire region above the exact dilation threshold.

Public Canon v67, Registry, Frontier, dependencies, gates, evidence, Notes and
all existing public rows remain unchanged.
