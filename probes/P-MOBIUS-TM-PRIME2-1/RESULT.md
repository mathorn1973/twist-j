# P-MOBIUS-TM-PRIME2-1 result

Date: 2026-08-10

## Decision

```text
BRIDGE-PASS
```

**Local proof and audit: PASS. Public two-architecture gate: PENDING. Canon
status: unchanged.** The frozen written proof is theorem-grade at the declared
L1 scope and the exact local audit returned 18/18 PASS with empty stderr. The
probe is not eligible for a public `T` fold until the repository-required
GitHub x86_64 and aarch64 jobs reproduce the committed `EXPECTED.txt` byte for
byte and the aggregate `check` passes.

## Frozen scope decided locally

Within the preregistered L1 scope, the written proof establishes the following
conditional on final repository review finding no proof defect:

```text
S1  PRIME-DILATION / MOEBIUS-SUPPORT EQUIVALENCE
    For every prime p, arithmetic f, and g=mu*f,
      f(pn)=f(n) for every n
    iff
      g(m)=0 for every m divisible by p.

S2  PRIME-2 THUE-MORSE SPECIALIZATION
    For tau(n)=(-1)^s_2(n) and c=mu*tau,
      c(2n)=0 for every n>=1,
    and Moebius inversion gives the unique odd-supported primitive spectrum
      tau(n)=sum_(d|n,d odd)c(d).

S3  BOOLEAN MIXED DIFFERENCE
    On odd squarefree n=product_(p in P)p,
      c(n)=product_(p|n)(D_p-I)tau(1),
    equivalently the top alternating finite difference over the complete
    prime-divisor Boolean cube. No multiplicativity is claimed.

S4  ODD DIVISOR RECURSION
      sum_(d|2n+1)c(d) = -sum_(d|n)c(d).

S5  LAMBERT BRIDGE, |x|<1
      product_(j>=0)(1-x^(2^j))-1
        = sum_(d odd)c(d)x^d/(1-x^d).

S6  DIRICHLET BRIDGE, Re(s)>1
      T(s)=zeta(s)C(s),
      C(s)=T_odd(s)/zeta_odd(s),
    with the common prime-2 dilation factor cancelled on the odd layer.
```

The local verifier audits finite instances and coefficient identities only.
The all-n and all-function quantifiers are supplied by the written exact proofs
in `PREREG.md`, not by enumeration.

## What this result means

The narrow L1 statement is that Moebius inversion acts as an exact detector of
prime-dilation invariance. For Thue-Morse, invariance under multiplication by
2 becomes complete support exclusion of the even prime direction in
`c=mu*tau`. The surviving odd-supported primitive reconstructs the full
Thue-Morse sequence by divisor sums, and on odd squarefree support it is the
top Boolean mixed difference of binary digit parity across prime directions.

The Lambert and Dirichlet identities are exact analytic rewritings inside their
explicit absolute-convergence domains.

## What this result does not mean

No layer lift occurred. This result does not assert RH, locate zeta zeros,
prove Nyman-Beurling or Baez-Duarte completeness, analytically continue the new
series, couple anything to `J`, select `p=5`, or construct a decoder, measure,
observer, force, spacetime, SI bridge, or physical vacuum. It is not a
pointwise Moebius-orthogonality theorem, and `c` is not multiplicative.

## Reproducibility state

```text
pin:             bb7ee2d4cff05784cfcee75a9b8d191009c76fd2
PREREG sha256:   bc6e0d05c1504d098870dd24a4f24ff4883a36594b3b8460e8c0fc2761ee868c
verifier sha256: 3c5c41adec750fdb11835b7eb0fb08654bea33e4fc2a0010fff0d2d443fc7389
stdout sha256:   d8ef89267c4b284b77ce6298c268ce60d2c76ccb517cf0a9a33b972e3dc6f9bd
local x86_64:    PASS, Debian GNU/Linux 13, Python 3.13.5, empty stderr
GitHub x86_64:   PENDING
GitHub aarch64:  PENDING
aggregate check: PENDING
Canon fold:      not started
```

The next boundary is the public pull-request two-architecture audit. Any
Registry or Canon promotion is a later separate reviewed action.
