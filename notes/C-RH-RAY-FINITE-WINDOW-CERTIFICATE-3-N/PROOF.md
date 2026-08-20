# Proof binding. C-RH-RAY-FINITE-WINDOW-CERTIFICATE-3-N

```text
STATUS:       NON-CANONICAL candidate-T
ISSUE:        #469
BASIS:        Public Canon v57
PREREG BLOB:  b23f6be3c4aef2864eb80297acade2fb03bcc27f
BREAKER BLOB: 5d31fecb5a417b8463deea8797a4d6a4334f5b38
FULL PROOF:   proof_engine.md
PROOF BLOB:   92dc38ca54d59ead6d4ff849bed9eae32edad950
RH:           unchanged and open
```

`proof_engine.md` is carried byte-identically from the stopped v57 lane #468.
That lane stopped because its wrapper failed during Python module import before
any scientific gate. The proof was written and pinned before that failed run;
its mathematics did not depend on the wrapper.

This fresh binding adopts exactly that proof, without changing one formula,
constant, hypothesis, threshold, or scope. It proves only the conditional
statement:

```text
complete tau-invariant zero window W
+ one nontrivial tau orbit O in W
+ q_W<1
=> an explicit finite one-point Ray-Pick derivative matrix is indefinite.
```

The explicit sufficient threshold is

```text
r_*=min{r>=r_0:A_W(c)q_W^(2(r-r_0))<2m_O},
N_*=r_*+|W|-1.
```

The proof also gives

```text
sum_beta m_beta|t_beta|^2<=M(c)/(c-1/2)
```

and the complete-height sufficient condition

```text
T>sqrt(y^2+(c+|x|)^2).
```

No actual off-critical orbit, complete zero window, or Euler-side certificate
is supplied. The carried proof is self-contained inside this branch and its
status ceiling remains candidate-T.