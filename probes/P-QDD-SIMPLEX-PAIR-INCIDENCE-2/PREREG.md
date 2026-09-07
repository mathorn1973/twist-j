# P-QDD-SIMPLEX-PAIR-INCIDENCE-2 preregistration

**FORMAL PREREGISTRATION / PROOF-FIRST / RESULT-EXPOSED / SUCCESSOR.**
Author: A. M. Thorn. Date: 2026-09-07.
Public lock: [#879](https://github.com/mathorn1973/twist-j/issues/879).
Branch: `probe/P-QDD-SIMPLEX-PAIR-INCIDENCE-2`.

## Authority, predecessor and custody

Basis: ACTIVE Public Canon v79. Public `main` at claim time is
`acd0e9d97a6495d3b242e8d31c43243a0f59f751`; current x86_64, aarch64 and
aggregate `check` are green. `STATUS.md` still declares content commit
`48ede94165472e2d77896a7c20ddb3c567f3bcc1`, Canon SHA-256
`025b07fe39ec4ab857a50adf467acc640334a1ea0cb87e8f9500b90948896764`, and
516701 Canon bytes.

This is the mandatory fresh successor to `P-QDD-SIMPLEX-PAIR-INCIDENCE-1`,
issue #877. Its immutable pin
`cf8b5cbe1ceb571fd8769bc71f82bb5da994011e` is publicly recorded as
`Status: ABANDONED` on main. One post-pin invocation reached diagnostic stdout
but the local orchestration failed to retain the child exit code, so no public
gate was accepted. The predecessor identifier is consumed. This successor does
not resume, repair, rename or rerun it.

The mathematical theorem and falsifiers below are unchanged in substance. The
new verifier deliberately removes redundant exhaustive audit loops. Universal
claims rest on PROOF.md, so changing the finite audit density does not change
the theorem threshold.

Exact successor branch and issue collision scans were empty before claim.
Existing QDD incidence and stabilizer probes remain distinct predecessors.

The accepted verifier must not execute before PREREG.md, PROOF.md and verify.py
are committed, pushed and read back from GitHub. Static parsing is allowed.
After the pin, do not amend, rebase, squash, rename, reuse or force-push.

## Field 1: frozen theorem

For every integer `N>=2`, let

```text
V_N = {x in Q^N : sum_r x_r = 0}
u_k = e_k - (1/N) 1
P_k = (N/(N-1)) u_k u_k^T
Q_k = I - P_k
q(x) = sum_r x_r^2.
```

Choose a setting `k` and any bijection from the `N-1` source coordinates to
all simplex vertices except k. For integer source z define

```text
s  = sum_i z_i
S2 = sum_i z_i^2
x  = sum_i z_i u_(beta(i))
U  = N(N-1)
X  = U x
A  = s^2
B  = N * sum_(i<j)(z_i-z_j)^2
D  = A+B.
```

The target is:

1. `U=N(N-1)` is the least positive universal integer M making both `M x` and
   `M P_k x` integral for every integer source/context. Consequently X,
   `P_k X` and `Q_k X` are in `A_(N-1)`.
2. The prepared integral relation is injective in the source:
   `(X_(beta(i))-X_k)/U=z_i`. The ordered pair `(P_k X,Q_k X)` reconstructs X.
3. `a_k=N e_k-1` is, up to sign, the unique primitive integer generator of
   the LOW ray and `q(a_k)=U`.
4. The exact quadratic identities are

   ```text
   q(P_k x)=A/U,  q(Q_k x)=B/U,  q(x)=D/U,
   q(P_k X)=U A,  q(Q_k X)=U B,  q(X)=U D.
   ```

5. The second-order relation census has exactly A LOW pairs and B HIGH pairs:
   LOW is the ordered Cartesian square of `|s|` units; HIGH is N labeled copies
   of the ordered Cartesian squares of every `|z_i-z_j|` difference fibre.
   Hence the pair census and quadratic branch read are one scalar reading in
   two representations, with U fixed independently by integral minimality.
6. For nonzero z the normalized branch values are A/D and B/D. Zero has no
   normalized ratio; s=0 kills LOW; all source coordinates equal iff HIGH is
   zero.
7. At N=5, U=20 and

   ```text
   A=s^2
   B=5(4S2-s^2)
   D=4(5S2-s^2)
   q(P_k x)=A/20
   q(Q_k x)=B/20
   q(x)=D/20.
   ```

   For `k=2,beta=(0,1,3,4)` these are exactly the prior public QDD incidence
   and P/Q quadratic quantities. That p=5 equality is prior public input; the
   new theorem is the uniform simplex result, minimal lift, primitive scale and
   source recovery.

Scientific conclusion: the owner-adopted quadratic registration has an exact
integer relational interpretation as a chosen second-order Cartesian-pair
probe. No uniqueness claim is made.

Falsifier: any exact counterexample to any clause above.

## Field 2: accepted verifier and finite audit domain

Command:

```text
python3 probes/P-QDD-SIMPLEX-PAIR-INCIDENCE-2/verify.py
```

The verifier is standard-library only and exact. Its finite audit is frozen as:

- primitive LOW generator and scale for every `N=2,...,32`, with explicit
  denominator-failure controls below U;
- every `N=2,...,8`, every setting, canonical beta, and a fixed deterministic
  source witness family containing zero, one-hot, zero-sum, all-equal,
  alternating and arithmetic sources where typed;
- N=5, all five settings and all 24 beta permutations per setting, on ten fixed
  sources spanning zero, one-hot, signs, equal, zero-sum and mixed cases;
- N=5 canonical public `k=2,beta=(0,1,3,4)` on all 625 sources in
  `{-2,-1,0,1,2}^4`;
- N=5 every setting with canonical beta on all 81 sources in `{-4,0,4}^4`, a
  finite control outside the old source-slot bound;
- direct Cartesian-pair enumeration for the complete 625-source public box.

No random seed, external data, float, tolerance, fitted value or measurement is
used. The finite audit is not the proof of the universal statement.

## Field 3: carrier and prior inputs

Scope is L4 regular-simplex support. N is a mathematical family parameter; the
TWIST-J specialization is N=p=5.

Prior public inputs used only for p=5 comparison:

- `QDD-CONDITIONAL-INCIDENCE-AND-SYMBOLIC-RECORD [T]`;
- `QDD-STABILIZER-UNCOMPUTE-POSTSTATES [T]`.

The proof is self-contained and imports no predecessor verifier or output. The
old 544-slot calendar, source-capture protocol, 40-mode apparatus and terminal
account are outside this theorem.

## Field 4: controls

Use `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `PYTHONHASHSEED=0`,
`PYTHONDONTWRITEBYTECODE=1`, exit 0, empty stderr and a 600-second scientific
ceiling. Exact mismatch threshold is zero.

Mandatory controls: primitive-vector gcd, `q(a_k)=N(N-1)`, a source with s=1
showing no smaller sampled denominator clears `P_k x`, integer source recovery,
P/Q orthogonality, the complete pair-difference identity, direct pair-set
counts, all p=5 formulas, and sources beyond the old finite slot domain.

## Field 5: disposition

A theorem counterexample is scientific failure. Timeout, nonzero exit, missing
process record, source/pin mismatch or byte mismatch is integrity STOP. A
completed formal gate produces one exact `EXPECTED.txt` and `RUN.md`; a gate
that does not complete consumes this fresh identifier under the abandoned-pin
rule.

The GitHub x86_64 and aarch64 jobs must reproduce the same committed output
byte for byte. A theorem-grade proof may establish T; the verifier audits it.

## Field 6: explicit nonclaims

This probe does not claim global decoder uniqueness, physical realization of
the pair sets, physical effects, an apparatus, ready state, coupling, pointer,
reduction, exclusive event, occurrence law, sampling law, post-state selection,
reset, L5 stream or L6 measure. It does not close or partially close the three
open QDD physical-apparatus owners.

The result is intended to justify why the quadratic reading is a natural exact
second-order relational probe while leaving other mathematical readings
possible.
