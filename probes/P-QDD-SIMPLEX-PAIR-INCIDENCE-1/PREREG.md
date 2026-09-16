# P-QDD-SIMPLEX-PAIR-INCIDENCE-1 preregistration

**FORMAL PREREGISTRATION / PROOF-FIRST / RESULT-EXPOSED.**
Author: A. M. Thorn. Date: 2026-09-07.
Public lock: [#877](https://github.com/mathorn1973/twist-j/issues/877).
Branch: `probe/P-QDD-SIMPLEX-PAIR-INCIDENCE-1`.

## Authority and custody

Basis: ACTIVE Public Canon v79. Public `main` at claim time is
`7664702e5e30a5c2fa048319519dbb5f0e56534e`. `STATUS.md` declares content
commit `48ede94165472e2d77896a7c20ddb3c567f3bcc1`, Canon SHA-256
`025b07fe39ec4ab857a50adf467acc640334a1ea0cb87e8f9500b90948896764`, and
516701 Canon bytes. The annotated `canon-v79` tag resolves to activation commit
`2f6384b99818280839b8219ce1ee91c9c1b278b6`, which is an ancestor of current
main. Current main passes x86_64, aarch64 and aggregate `check`.

The immediately preceding public probe `P-A4-RATIONAL-FRAME-WEIGHT-NONUNIQUENESS-1`
merged as `7664702e5e30a5c2fa048319519dbb5f0e56534e`. It decides only that positive
complete-frame additivity does not force quadratic reading. It does not reject
the owner-adopted quadratic branch.

Before issue #877 the session searched open issues and pull requests, code,
probe names and remote branches for `SIMPLEX-PAIR-INCIDENCE`, `PAIR-INCIDENCE`
and equivalent live lanes. No collision was found. Existing
`P-U-PREPARATION-EVENT-RECORD-1` and `P-QDD-STABILIZER-APPARATUS-1` are
predecessors with distinct scopes. No sealed or abandoned identifier is reused.

The formulas below were derived in non-canonical analysis before this public
pin. The result is therefore exposed. The accepted verifier must not execute
before PREREG.md, PROOF.md and verify.py are committed, pushed and read back
from GitHub. Static parsing is allowed. After the pin, do not amend, rebase,
squash, rename, reuse or force-push the identifier.

## Field 1: frozen theorem

For every integer `N>=2`, let

```text
V_N = {x in Q^N : sum_r x_r = 0}
u_k = e_k - (1/N) 1
P_k = (N/(N-1)) u_k u_k^T
Q_k = I - P_k
q(x) = sum_r x_r^2.
```

Choose a setting `k` and any bijection

```text
beta : {0,...,N-2} -> {0,...,N-1} minus {k}.
```

For an integer source `z=(z_0,...,z_(N-2))`, define

```text
s  = sum_i z_i
S2 = sum_i z_i^2
x  = sum_i z_i u_(beta(i))
U  = N(N-1)
X  = U x.
```

Define the second-order Cartesian-pair counts

```text
A = s^2
B = N * sum_(i<j) (z_i-z_j)^2
D = A+B.
```

Equivalently, let `I_LOW` be the ordered Cartesian square of `|s|` amplitude
units. Let `I_HIGH` contain `N` separately labeled copies of the ordered
Cartesian square of `|z_i-z_j|` units for every unordered source-coordinate
pair. Signs are record payload and do not change cardinality. Then
`|I_LOW|=A`, `|I_HIGH|=B`, and the total pair census is `D`.

The frozen theorem target is:

1. **Minimal universal integral lift.** `U=N(N-1)` is the least positive integer
   `M` for which both `M x` and `M P_k x` are integral for every integer source,
   every setting and every beta. For `X=U x`, the three vectors `X`, `P_k X`
   and `Q_k X` lie in the integer root lattice `A_(N-1)`.
2. **No source loss in the prepared relation.** For every source coordinate,
   `(X_(beta(i))-X_k)/U=z_i`. Also `P_k X+Q_k X=X`, so the complete ordered
   branch pair reconstructs the prepared relation.
3. **Primitive LOW scale.** `a_k=N e_k-1` is, up to sign, the unique primitive
   integral generator of the ray `Q u_k`, and `q(a_k)=U`.
4. **Pair-count / quadratic equivalence.** Exactly

   ```text
   q(P_k x) = A/U
   q(Q_k x) = B/U
   q(x)     = D/U
   ```

   and equivalently

   ```text
   q(P_k X) = U A
   q(Q_k X) = U B
   q(X)     = U D.
   ```

   Thus the chosen second-order pair census and the quadratic branch reading
   are the same scalar reading in two representations. The denominator is not
   fitted to the target; it is the minimal integral simplex scale from clause 1.
5. **Normalized branch reading.** For every nonzero source,

   ```text
   q(P_k x)/q(x) = A/D
   q(Q_k x)/q(x) = B/D.
   ```

   Zero has `D=0` and no ratio. If `s=0`, LOW is zero. HIGH is zero exactly
   when all source coordinates are equal.
6. **Public p=5 specialization.** At `N=5`, `U=20` and

   ```text
   B = 5(4 S2-s^2)
   D = 4(5 S2-s^2)
   q(P_k x) = A/20
   q(Q_k x) = B/20
   q(x)     = D/20.
   ```

   With the public source ordering `beta=(0,1,3,4)` and missing setting `k=2`,
   these are exactly the already-public QDD incidence quantities `A`, `B`, `D`
   and algebraic LOW/HIGH/total quadratic readings. Their p=5 equality is prior
   public input. New content is the uniform theorem, minimal integral lift,
   primitive scale and source-recovery statement.

The scientific conclusion is deliberately narrow: the adopted quadratic
registration has an exact integer relational interpretation as a second-order
Cartesian-pair probe on the regular-simplex carrier. The theorem does not say
that this is the only possible reading.

A falsifier is any exact admitted counterexample to lift minimality,
integrality, source recovery, primitive-ray scale, pair cardinality, branch
norm identity, nonzero-source ratio or the N=5 specialization.

## Field 2: accepted verifier and finite audit domain

Command from repository root:

```text
python3 probes/P-QDD-SIMPLEX-PAIR-INCIDENCE-1/verify.py
```

The verifier uses only the Python standard library and exact integer/Fraction
arithmetic. It audits the universal written proof on these frozen finite
classes:

- every `N=2,...,8`, every setting, canonical complement beta, and every source
  in `{-1,0,1}^{N-1}`;
- `N=5`, all five settings, all 24 bijections beta for each setting, and all
  625 sources in `{-2,-1,0,1,2}^4`;
- `N=5`, every setting, canonical beta and all 6561 sources in
  `{-4,-3,...,4}^4`, explicitly beyond the old bounded 544-slot implementation;
- primitive LOW rays for `N=2,...,32`;
- direct Cartesian-pair enumeration on the public `N=5,k=2,beta=(0,1,3,4)`
  sources in `{-2,-1,0,1,2}^4`;
- zero, zero-sum, all-equal and nontrivial mixed controls.

The verifier reconstructs the rational simplex vector and projector with
`Fraction`, independently constructs the integer lift, and checks the two
representations against each other. Universal conclusions rest on PROOF.md,
not on extrapolation from these finite audits.

No external data, floating point, random seed, tolerance, fitted coefficient,
measured number or occurrence target is used.

## Field 3: carrier, data and prior public inputs

The theorem carrier is L4 regular-simplex support. `N` is a mathematical family
parameter. The TWIST-J physical specialization uses `N=p=5`, but no physical
claim is made for other N.

The public p=5 comparison is against the already merged mathematical inputs:

- `QDD-CONDITIONAL-INCIDENCE-AND-SYMBOLIC-RECORD [T]` from
  `probes/P-U-PREPARATION-EVENT-RECORD-1/RESULT.md`;
- `QDD-STABILIZER-UNCOMPUTE-POSTSTATES [T]` from
  `probes/P-QDD-STABILIZER-APPARATUS-1/RESULT.md`.

The new proof is self-contained and does not import their verifier code or old
stdout. The older fixed 544-slot incidence calendar, source capture convention,
40-mode apparatus and terminal account are not part of this theorem.

## Field 4: systematics and controls

Use deterministic iteration order, `LC_ALL=C`, `LANG=C`, `TZ=UTC`,
`PYTHONHASHSEED=0`, `PYTHONDONTWRITEBYTECODE=1`, exit 0, empty stderr and a
600-second local ceiling. Every scientific comparison is exact.

Mandatory controls include:

- the least-denominator witness `z=(1,0,...,0)`, which forces divisibility by
  `N(N-1)` through `P_k x=-a_k/[N(N-1)]`;
- explicit orthogonality `P_k X . Q_k X=0`;
- the identity `sum_(i<j)(z_i-z_j)^2=(N-1)S2-s^2`;
- direct source recovery from integer coordinates;
- direct Cartesian-pair cardinality on the public bounded source domain;
- `N=5,k=2,beta=(0,1,3,4)` as the public-order control;
- sources outside the old finite slot bounds, proving that this theorem does
  not depend on the 1024-slot calendar.

## Field 5: threshold and disposition

Mismatch threshold is zero. A completed gate passes only with exact committed
stdout, exit 0 and empty stderr. Any theorem counterexample fires the scientific
falsifier and is preserved. A pin mismatch, timeout, syntax/source defect or
platform-dependent byte mismatch is integrity STOP, not mathematical evidence.

After the first completed formal run, add `EXPECTED.txt`, `RUN.md` and
`RESULT.md`. GitHub x86_64 and aarch64 must independently match the same
`EXPECTED.txt` byte for byte. The theorem-grade written proof may earn T; the
verifier is then an audit.

## Field 6: layer and explicit nonclaims

Scope is **L4 only**. The integer source `z` in this theorem is a formal support
coordinate. This probe does not derive source capture from native `Omega,U` and
performs no L1-to-L4 or L1-to-L5 lift.

The following are explicitly not claimed:

- uniqueness of quadratic reading;
- a physical effect identifier or complete effect family;
- a physical apparatus, carrier, ready state, coupling, pointer or reduction;
- a realized exclusive LOW/HIGH event;
- an onset, occurrence, sampling or randomness law;
- a post-state selection principle beyond the prior conditional L4 maps;
- reset, fresh physical storage or detector energetics;
- an L5 stream or L6 probability measure;
- closure or partial closure of `QDD-INSTRUMENT-APPARATUS`,
  `QDD-INSTRUMENT-CLASS-COMPLETENESS` or `QDD-TERMINAL-EVENT-SEMANTICS`.

`I_LOW` and `I_HIGH` are mathematical relation-pair sets. Their cardinalities
are not called physical event counts. The intended result is a reason for the
chosen quadratic decoder branch, not a theorem that Nature must choose it.
