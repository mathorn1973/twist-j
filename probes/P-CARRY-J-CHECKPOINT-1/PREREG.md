# PREREG. P-CARRY-J-CHECKPOINT-1

Public lock: issue #81. Base: Public Canon v11, activation commit
`3d8c6307f20d01ad50fc90ae1c5777926b884881`, Canon content commit
`3dc0d4255ae47f0512e5dd656d92ceb308ab026a`.

```text
LAYER:  L1 state and readout arithmetic. No lift to L2-L6 is claimed.
TARGET: decide CARRY-J-CHECKPOINT [O] on the frozen full forward carrier.
```

No scientific status is earned by this preregistration. The proposed result
is an exact checkpoint-factorization no-go. Its eventual Canon and registry
disposition is separate reviewed work.

## Frozen architecture and carrier

Let the checkpoint be

```text
psi = (p1, p4, p1p, p4p, q, r) in F_5^6,
z_6(psi) = p1 + p4 + p1p + p4p + q + r mod 5.
```

The five declared checkpoint generators are indexed by
`(g_0,g_1,g_2,g_3,g_4)=(a,b,c,d,e)`. The only properties used in the
symbolic proof are

```text
z_6(a psi) = z_6(psi),
z_6(b psi) = -z_6(psi),
z_6(c psi) = 2-z_6(psi),
z_6(d psi) = 2-z_6(psi),
z_6(e psi) = 3-z_6(psi),
b^2 = id.
```

Let `theta_n = s_2(n) mod 2`, where `s_2` is the finite binary digit
sum. Freeze the public update and checkpoint projection as

```text
i_n = z_6(psi_n) + 2 theta_n mod 5,
U(n,psi_n) = (n+1,g_(i_n)(psi_n)),
psi_n = pr_checkpoint(U^n(0,psi_0)).
```

The carrier under attack is the union of every forward orbit with clock
coordinate zero and arbitrary initial checkpoint:

```text
C = {U^n(0,psi_0) : n >= 0, psi_0 in F_5^6}.
```

The ramified phase is the inherited `RAMIFIED-TM-LIFT [T]` value

```text
Theta_n = 2^s_2(n) mod 5 in F_5^*.
```

## Frozen statement

For every `psi_0 in F_5^6`, the claim is

```text
pr_checkpoint(U^4(0,psi_0)) = pr_checkpoint(U^6(0,psi_0)),  (A)
Theta_4 = 2,  Theta_6 = 4.                                  (B)
```

Consequently there is no single-valued map

```text
h : F_5^6 -> F_5^*
```

such that

```text
h(pr_checkpoint(U^n(0,psi_0))) = Theta_n                    (C)
```

for every state in `C`. This decides the frozen full-carrier factorization
route negatively. It does not decide a separately defined restricted
carrier.

## Frozen symbolic proof

The first six Thue-Morse bits are

```text
(theta_0,theta_1,theta_2,theta_3,theta_4,theta_5)
= (0,1,1,0,1,0).
```

Write `z_n=z_6(psi_n)`. At the first step, the selector is `i_0=z_0`.
The five trace laws give

```text
z_1 in {0,4}.
```

At `n=1`, the selector is `z_1+2`, so

```text
z_1=0 -> i_1=2 -> z_2=2,
z_1=4 -> i_1=1 -> z_2=1.
```

At `n=2`, the selector is `z_2+2`, so

```text
z_2=2 -> i_2=4 -> z_3=1,
z_2=1 -> i_2=3 -> z_3=1.
```

Thus `z_3=1` for every seed. The next three selectors are forced:

```text
i_3 = 1+2 theta_3 = 1,
i_4 = z_4+2 theta_4 = -1+2 = 1,
i_5 = z_5+2 theta_5 = 1.
```

All three steps therefore use `b`, and `b^2=id` gives

```text
psi_4 = b psi_3,
psi_5 = b^2 psi_3 = psi_3,
psi_6 = b psi_3 = psi_4.
```

This proves (A) uniformly over all `5^6` seeds. Since `s_2(4)=1` and
`s_2(6)=2`, (B) follows. Equations (A) and (B) assign two different values
to the same argument of any proposed `h`, which proves the no-go (C).

The proof, not the verifier, carries the conclusion on the full forward
carrier. The finite exhaustive verifier audits every checkpoint seed and
every generator input because the collision occurs by time six.

## The six frozen fields

```text
EQUATION     Statements (A)-(C) exactly as written above, including the
             universal quantifier over all psi_0 in F_5^6 and the negative
             conclusion only for the frozen full forward carrier C.

CODE         verify.py, SHA-256
             406004360a511512f3c3c44351f25df64df115aa6f35dbd1c0ac16f4587b20c2
             (5045 bytes). Python standard library only; exact integers;
             deterministic; no file, network, or subprocess access; no
             floats. Run from the repository root with LC_ALL=C LANG=C
             PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

CARRIER      theorem: C as defined above, with every psi_0 in F_5^6 and
             n >= 0. The proof needs only n=0,...,6. Audit: every one of the
             15625 checkpoints as a generator input, every initial seed
             through six updates, all five initial z_6 classes, and the two
             inherited phase values at n=4 and n=6. No external dataset.

SYSTEMATICS  no numerical approximation or sampling. The theorem is
             conditional on the declared Public Canon v11 architecture,
             selector offset +2, generator definitions, and inherited
             RAMIFIED-TM-LIFT phase formula. Implementation correctness and
             inherited-premise correctness are the only audit limitations.
             A later architecture change is outside this frozen scope.

THRESHOLD    KILL the theorem candidate on any psi_0 with psi_4 != psi_6;
             Theta_4 = Theta_6; any defect in the five trace laws, b^2=id,
             or proof steps; any unreconciled FAIL in gates 01-05; nonzero
             stderr or exit; or a transcript mismatch. A defect discovered
             in PREREG.md or verify.py after the pin invalidates this named
             probe. Do not amend either frozen file or move the threshold.

LAYER        L1 only. No state-to-manifold, boundary, support, stream, or
             measure lift is asserted.
```

## Dependencies and scope firewall

Frozen premises:

```text
Public architecture definitions   F_5^6, a,b,c,d,e, z_6, selector, U
DEF-ODOMETER-ORBIT                 the forward n in N_0 carrier
RAMIFIED-TM-LIFT [T]               Theta_n = 2^s_2(n) mod 5
```

The finite census results are not premises. This probe does not identify
`Theta_n` with the full autonomous state, derive the selector offset, add a
physical carry or phase reading, extend parity to all of `Z_2`, establish
decoder completeness, or lift a result to L2-L6. It leaves
`RAMIFIED-TM-LIFT [T]`, `READING-SPLIT [D]`, and every separately specified
restricted-carrier question unchanged.

Before the first formal execution, this file and `verify.py` must be committed
and pushed together. After that pin they are immutable for this probe.
