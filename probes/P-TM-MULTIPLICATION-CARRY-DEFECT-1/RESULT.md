# P-TM-MULTIPLICATION-CARRY-DEFECT-1 result

Date: 2026-08-10

## Decision

```text
CARRY-PASS
```

**Probe evidence gate: COMPLETE. Canon status: unchanged.** The frozen written
proof is theorem-grade at the declared L1 scope, the exact local audit returned
15/15 PASS with empty stderr, and the repository-required GitHub x86_64 and
aarch64 jobs reproduced the same committed `EXPECTED.txt` byte for byte. The
aggregate two-architecture `check` also passed. The result is therefore
eligible for a later reviewed `T` fold, but this probe PR itself creates no
Registry or Canon claim.

## Frozen scope decided

Within the preregistered L1 scope:

```text
S1  CANONICAL BINARY MULTIPLICATION CARRY MASS
    kappa_2(a,b)=s2(a)s2(b)-s2(ab)>=0 is the exact total unit-carry value of
    binary schoolbook multiplication.

S2  BOOLEAN PARITY LAW AND MULTIPLICATIVITY DEFECT
    With P=s2(a) mod 2, Q=s2(b) mod 2, K=kappa_2(a,b) mod 2,
      s2(ab) mod 2 = (P AND Q) XOR K,
      tau(ab)tau(a)tau(b)=(-1)^((P OR Q) XOR K).

S3  COMPLETE DISTINCT-ODD-SEMIPRIME SHADOW CLASSIFICATION
    For c=mu*tau and distinct odd primes p,q,
      c(pq) in {-4,-2,0,2},
      c(pq)=0 iff K=0 and (P OR Q)=1.
    A zero shadow does not mean zero carries; kappa_2(3,11)=4 while c(33)=0.

S4  PRIME-SQUARE SHADOW
      c(p^2)=tau(p^2)-tau(p),
      c(p^2)=0 iff kappa_2(p,p) is even.

S5  HIGHER SQUAREFREE CARRY FIELD
    On the complete prime-divisor Boolean cube of an odd squarefree n, the
    top Moebius mixed difference is the signed sum of the exact carry-parity
    field frozen in PREREG.md.
```

The verifier audits finite instances, the complete abstract three-bit truth
table, and exact fixed controls. The all-integer, all-prime and all-squarefree
quantifiers come from the written proof.

## What this result means

Binary multiplication has a canonical integer carry defect. Before carries,
the parity of the raw coefficient mass is the Boolean AND of the two input
popcount parities. Carry parity supplies the exact XOR correction. The same
identity determines the failure of Thue-Morse multiplicativity through the
Boolean OR of the input parities.

When this local multiplication law is inserted into the Moebius mixed
difference on prime supports, semiprime zero shadows admit the exact eight-state
classification above, and higher squarefree values are a deterministic signed
sum over the full carry-parity field of the divisor Boolean cube.

## What this result does not mean

No layer lift occurred. This result does not assert RH, locate zeta zeros,
prove Nyman-Beurling or Baez-Duarte completeness, analytically continue a
series, couple anything to `J`, select `p=5`, or construct a decoder, Born
rule, observer, force, spacetime, SI bridge, vacuum, matter, entanglement, or
physical curvature. `kappa_2` is not the finite-vector-space carry form of
`CARRY-PENTAD` or issue 316 and is not the chronological carry cocycle of
`RAMIFIED-TM-LIFT`. `c=0` does not mean no carries or trivial multiplication.

## Reproducibility state

```text
pin:             fdabf9a15bf5f20875b5db77e6a8b5dbc5a05298
PREREG sha256:   df69655203b307c06136357a83afdaec460c331cc9a65553e8cecf76934a98bf
verifier sha256: 2d5ead2b4a506faddb8f86d9740cf4920ac375ec87af515532e19b1ac7ab055d
stdout sha256:   d10538998b533f2dc0f6a2796024b90368fb225b7edf21b993fd26b14851e2dc
local x86_64:    PASS, Debian GNU/Linux 13, Python 3.13.5, empty stderr
GitHub x86_64:   PASS, Ubuntu 24.04.4, Python 3.12.13
GitHub aarch64:  PASS, Ubuntu 24.04.4, Python 3.12.13
aggregate check: PASS, workflow run 31383719610
Canon fold:      not started
```

Both GitHub architecture logs report the same verifier SHA-256 and stdout
SHA-256 displayed above. Policy, 99 unit tests, Canon check, ledger check, and
the changed-probe verifier also passed on both architectures.

The next boundary is review and merge of this one-probe PR without squash or
rebase. Any Registry or Canon promotion is a later separate reviewed action.
