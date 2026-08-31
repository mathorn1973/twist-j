# P-O5-DEDEKIND-GRH-DIVISOR-READ-1 result

Status: **SCIENTIFIC RESULT / CANDIDATE-T / PUBLIC TWO-ARCHITECTURE REPLAY PENDING / CANON UNCHANGED**

The written universal proof and the accepted local exact audit support the
frozen divisor-coordinate theorem:

```text
widehat_O_5 = O_5 on Re(s)>1,
H_5 is holomorphic and nowhere zero on Re(s)>1/2,
H_5 widehat_O_5 = 1/zeta_F,
ord_rho(widehat_O_5) = -ord_rho(zeta_F) on Re(rho)>1/2,
GRH(zeta_F) iff widehat_O_5 is pole-free on Re(s)>1/2.
```

This is a read equivalence only. It proves no pole-freeness, zero location,
RH or GRH.

## Local formal decision

```text
VERIFY RESULT 8/8 ALL PASS
exit_code: 0
stderr_bytes: 0
stdout_sha256: 1136f7a6abe6688a3ea2b6980a4fc6966cbd4fe5241f2d29cb4c9ca953ebf6c7
breakers: B1,B2,B3,B4,B5 all FIRE
```

No scientific falsifier fired.

## Evidence boundary

The verifier audits exact local rational functions, formal global factor
bookkeeping, divisor multiplicities, functional-equation symmetry logic,
unordered split support and source firewalls. The analytic continuation and
Euler-product nonvanishing inputs are the four classical imports frozen in
PREREG.md and are not numerically evaluated.

The merged squarefree-core probe `P-O5-SQUAREFREE-CORE-1` is adjacent and
independent; it is not used as evidence here.

## Public status boundary

This PR itself creates no Registry row and changes no Canon file. Maximum
later fold candidate:

```text
O5-DEDEKIND-GRH-DIVISOR-READ [T]
```

The required GitHub workflow must replay the unchanged pinned verifier on
x86_64 and native aarch64 against the same EXPECTED.txt. Until both jobs and
aggregate `check` pass, the architecture gate remains pending.
