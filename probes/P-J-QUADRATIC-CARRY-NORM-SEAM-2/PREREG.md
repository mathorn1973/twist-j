# P-J-QUADRATIC-CARRY-NORM-SEAM-2 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION. RESULT-EXPOSED. NO SCIENTIFIC RESULT YET.**

Claim lock: issue #622.
Owner session: `chatgpt-gpt56sol-2026-08-28-quadratic-carry-norm-seam-2`.
Target line: PUBLIC. Layer: **L1 exact cyclotomic, integral, and finite-field algebra only**.

```text
STATE:          ACTIVE
CANON:          Public Canon v67
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v67
CONTENT_COMMIT: f58df589519d04820d0d819afcb732e2c2ec0429
CANON_SHA256:   b20b62ee730c2b5ac2e2845cb99f40a1cf72618eb71dae3c1279056943d43a98
CANON_BYTES:    351502
BASE_MAIN:      4b451c5bdf5d72fe9642916950b6e2a8edb449cd
```

## Mandatory predecessor STOP disclosure

Issue #620 / `P-J-QUADRATIC-CARRY-NORM-SEAM-1` is consumed with `STOP / VERIFIER-INTEGRITY DEFECT / NO SCIENTIFIC CONCLUSION`. Its immutable pin is `5efc0beed470118fd2648951d1002b2af195048b`; its sole formal execution is preserved by STOP-record PR #621. The predecessor verifier hard-coded the expected G4 defect coefficients and compared them with themselves. No predecessor file, run, or stdout is imported as evidence. This successor changes no scientific carrier, theorem target, threshold, falsifier, layer, or status ceiling. The sole pre-pin repair is that G4 is independently recomputed by exact polynomial arithmetic in formal `B` over `Q(sqrt5)` from the computed witness values.

The formulas below were derived before this public lock. That prior calculation is discovery context only. This probe is proof-first and RESULT-EXPOSED; the accepted verifier is an audit. It uses the Python standard library only, exact `Fraction` arithmetic, no float, no tolerance, no randomness, no network, no data file, and no environment-dependent scientific input.

## 1. Public inputs and collision boundary

The probe uses these already-public rows only at their registered scopes:

```text
AFFINE-QUADRATIC-FORM-UNIQUENESS [T]
J-BINARY-NORM-DESCENT            [T]
J-ODD-MOTOR-MEDIATED-BRIDGE      [T]
CARRY-QUADRATIC-SYMMETRY         [T]
BORN-FACE-WEIGHTS                 [T]
```

The first row owns the invariant quadratic line `q_+`. The second owns the reduction of that line modulo two and its explicit isometry to the registered Boolean carry form. The third owns the second quadratic line `q_-`, transforming by the quadratic multiplier character. The fourth owns the prime-free carry form `e_2`. The fifth owns only the exact algebraic face weights.

The following rows are boundaries, not theorem inputs:

```text
MEASURE-BORN-VERB          [D]
TM-SYM2-PHYSICAL-MEASURE   [D]
TWO-PLACE-PHYSICS          [D]
READING-SPLIT              [D]
QUADRATIC-DECODER-DATA     [O]
```

No physical Born measure, decoder action, apparatus, event, observer, physical place selector, or L2-L6 lift is allowed.

At claim time no issue, branch, probe directory, or public row named `P-J-QUADRATIC-CARRY-NORM-SEAM-2` or `J-QUADRATIC-CARRY-NORM-SEAM` existed.

## 2. Frozen algebra

Let

```text
j = zeta_5,
K = Q(j),
O = Z[j],
K+ = Q(sqrt5),
c(j) = j^-1,
u(j) = j^2,
sqrt5 = 1 + 2(j+j^-1).
```

For `x in O`, define

```text
H(x)  = x c(x) in O_(K+),
q0(x) = Tr_(K+/Q)(H(x)),
q1(x) = (H(x)-u(H(x)))/sqrt5.
```

Because `H(x)` belongs to `Z[phi]`, the difference of its two real conjugates is an integer multiple of `sqrt5`, so `q1(x)` is integer-valued.

Write

```text
x = a + b j + c j^2 + d j^3.
```

The frozen target polynomials are

```text
q0 = 2(a^2+b^2+c^2+d^2) - (ab+ac+ad+bc+bd+cd),
q1 = ab-ac-ad+bc-bd+cd.
```

Equivalently, with `G = I_4 - (1/5) 11^T`, the symmetric matrix of `q0` is `(5/2)G`, while the symmetric matrix of `2 q1` is

```text
q_- = [[ 0, 1,-1,-1],
       [ 1, 0, 1,-1],
       [-1, 1, 0, 1],
       [-1,-1, 1, 0]].
```

These are the displayed public forms, but their identification with the field formulas is part of G1 and must be proved, not assumed.

## 3. G1: trace and sign identification

Expand `H(x)=x c(x)` coefficient-by-coefficient in the power basis. Taking the real trace gives the displayed `q0`. Taking the signed real difference and dividing by `sqrt5` gives the displayed `q1`.

Let `D=M_J-I=m_(j^2)` and let `U` be the rational matrix of `u:j->j^2`. Since `j^2 c(j^2)=1`, multiplication by `D` preserves `H`; since `u` exchanges the two real embeddings of `K+`,

```text
q0(Dx)=q0(x),     q1(Dx)=q1(x),
q0(Ux)=q0(x),     q1(Ux)=-q1(x).
```

Thus `q0` is the public invariant line and `2q1` is the public `epsilon` line. Since `D` and `U` generate the frozen affine action, this gives the required character law.

## 4. G2: unique prime-two coalescence

Use monomial order

```text
a^2,b^2,c^2,d^2,ab,ac,ad,bc,bd,cd.
```

The coefficient vectors are

```text
q0:  (2,2,2,2,-1,-1,-1,-1,-1,-1),
q1:  (0,0,0,0, 1,-1,-1, 1,-1, 1).
```

Their difference is

```text
(2,2,2,2,-2,0,0,-2,0,-2),
```

whose nonzero coefficients have gcd `2`. Therefore, for a rational prime `ell`, coefficientwise equality of the two quadratic polynomials modulo `ell` holds if and only if `ell=2`.

At `ell=2`, both reduce to

```text
e_2(a,b,c,d) = ab+ac+ad+bc+bd+cd.
```

The parent theorem `J-BINARY-NORM-DESCENT [T]` already owns the typed identification of `q0 mod 2` with the `F_16/F_4/F_2` norm-trace form and its explicit isometry to the registered carry carrier. This probe adds only that the sign line has the same binary shadow and that rational prime two is the unique prime where the two character channels coalesce.

## 5. G3: exact norm reconstruction

By definition

```text
q0 = H + u(H),
sqrt5 q1 = H - u(H).
```

Hence coefficientwise for every `x in O`,

```text
H(x)    = (q0(x) + sqrt5 q1(x))/2,
u(H(x)) = (q0(x) - sqrt5 q1(x))/2.
```

The two rational quadratic channels are exactly the two coordinates of the canonical relative norm under the basis `{1,sqrt5}` of `K+`.

## 6. G4: affine nonselection and multiplicative rigidity

The two character lines yield the frozen two-parameter covariant family

```text
F_(A,B)(x) = A q0(x) + B sqrt5 q1(x),     A,B in Q.
```

Affine covariance alone leaves both rational coefficients free. This is an explicit nonselection statement.

Normalization gives

```text
q0(1)=2, q1(1)=0,
F(1)=1  =>  A=1/2.
```

Now take the single witness `x=1+j`. Exact expansion gives

```text
q0(x)=3,   q1(x)=1,
q0(x^2)=7, q1(x^2)=3.
```

With `A=1/2`,

```text
F(x^2)-F(x)^2 = (5/4)(1-4B^2).
```

Thus multiplicativity even on this one frozen witness forces

```text
B=+1/2 or B=-1/2.
```

By G3 these two members are exactly `H` and `u o H`; both are multiplicative because they are the two real embeddings of the relative norm. Therefore the normalized multiplicative members of the frozen covariant family are exactly one Galois pair. No Galois-invariant datum selects one oriented member.

## 7. G5: exact face-weight reconstruction

For

```text
x_k = 1+j^k,  k=0,1,2,3,4,
```

require

```text
(q0(x_k)) = (8,3,3,3,3),
(q1(x_k)) = (0,1,-1,-1,1).
```

G3 then gives

```text
(H(x_k)) =
(4,
 (3+sqrt5)/2,
 (3-sqrt5)/2,
 (3-sqrt5)/2,
 (3+sqrt5)/2).
```

This is exactly the already-registered algebraic vector `BORN-FACE-WEIGHTS [T]`. The comparison adds a proof dependency/seam only. It earns no duplicate evidence credit for the existing weight theorem and gives no L6 interpretation.

## 8. G6: single-invariant no-go

The exact witness

```text
q0(1+j)   = 3,
q0(1+j^2) = 3,
H(1+j)    = (3+sqrt5)/2,
H(1+j^2)  = (3-sqrt5)/2
```

proves that the unique invariant scalar line alone cannot recover the face weights. The `epsilon` line is load-bearing. This does not contradict uniqueness of the invariant line because the second line is covariant, not invariant.

## 9. Verifier obligations

The accepted verifier must audit all of the following exactly:

1. cyclotomic multiplication, conjugation, `u`, `sqrt5^2=5`, and `D^5=I`;
2. coefficientwise expansion of `H`, `q0`, and `q1`;
3. matrix identification of `q0` and `2q1` with the two public forms;
4. invariance/sign covariance under the generators `D` and `U`;
5. gcd `2` of the polynomial difference and the common mod-two `e_2` coefficients;
6. coefficientwise norm reconstruction;
7. the normalization and exact multiplicativity-witness factor `(5/4)(1-4B^2)`, computed by explicit polynomial multiplication in formal `B` over `Q(sqrt5)` from the exact witness values; hard-coding the left-hand coefficient tuple is STOP;
8. exact identification of the `B=+/-1/2` members with `H` and `uH`;
9. the five `q0`, `q1`, and face-weight values;
10. the single-invariant no-go witness.

The verifier may recheck parent formulas for integrity but must not re-claim their theorem scope.

## 10. Decision

```text
SEAM-CERTIFIED
  every frozen G1-G6 statement and every verifier integrity check passes exactly.

ROUTE-FALSIFIED
  carrier integrity passes but at least one frozen mathematical statement fails;
  preserve the smallest witness and do not repair this identifier.

STOP
  authority, collision, proof scope, pin/readback, exactness, deterministic
  execution, stderr, security, mutation, or architecture requirements fail.
```

No numerical threshold exists.

## 11. Maximum scope and firewall

Maximum later claim: one **L1 theorem** `J-QUADRATIC-CARRY-NORM-SEAM [T]`, subject to the public fold procedure after the probe is complete. The probe itself changes no Canon, Registry, Frontier, Evidence, Dependency, Gate, tag, release, or status row.

The theorem may say:

```text
the registered invariant and epsilon quadratic channels have a unique common
rational-prime reduction at 2; that common shadow is the registered carry form;
the two channels reconstruct the relative norm; normalized multiplicativity
selects its Galois pair; evaluating the pair on 1+j^k reconstructs the existing
exact face weights.
```

It may NOT say that Boolean carry derives `J`, that `Q(zeta_5)` is physically selected, that Nature or the complete decoder must read at prime two, that the algebraic face weights are probabilities, or that any physical Born rule, apparatus, observer, measurement, spacetime, force, SI bridge, or L2-L6 result follows.

## 12. Formal order

1. `PREREG.md` and a fresh standard-library `verify.py` are committed and pushed together as the immutable pin.
2. Both files are read back from the pushed pin; byte counts, SHA-256 and Git blob identities are checked.
3. The accepted verifier is not scientifically executed before that readback.
4. After the pin, execute exactly `python3 probes/P-J-QUADRATIC-CARRY-NORM-SEAM-2/verify.py` and require exit `0`, empty stderr, deterministic stdout.
5. Commit only `EXPECTED.txt`, `RUN.md`, and `RESULT.md` in the result commit.
6. Open one PR changing only this probe directory.
7. Require the public GitHub-hosted x86_64 and aarch64 jobs to match the same committed `EXPECTED.txt` byte-for-byte and aggregate `check` to pass.
8. Never amend, rebase, squash, force-push, retune, or reuse this identifier after the pin.
