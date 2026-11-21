# C-CONTACT-FOUR-CHART-RENEWAL-N

**NON-CANONICAL / L1. Author: A. M. Thorn.**

This note supplies candidate-T proofs and a fixed candidate-C finite replay.
Reservation: [#1866](https://github.com/mathorn1973/twist-j/issues/1866).
Base: 0c33e2b281e39127c269ef5dd7f5b529a62e9e65, Public Canon v107.

It follows the direct numerator construction in
[#1865](https://github.com/mathorn1973/twist-j/pull/1865), at
b67b5f0783a81bd38475eefc4d10dfaa4ff78bda, and the arithmetic block
analysis in [#1864](https://github.com/mathorn1973/twist-j/pull/1864), at
fa3605cd8b36a5cc0fd7a9f1b26cf0871df72c75.
Those frozen files are unchanged. The proofs here are self-contained.

## The exact advance

Write rho=j^2, U_d=1-rho^d and J_d=1+rho^d, with d in {1,2,3,4}.
The four integral units satisfy the telescoping identity

    U_d J_d=U_(2d),     J_d J_(2d) J_(4d) J_(3d)=1.

The declared source is

    F_(q,d)(n)=(U_d n,(4q-J_d)n,2J_d).

This is a newly supplied input interface. It is not a conversion of an
already occupied output of the earlier E source into F.

Two native powered contacts C01^d C02^d create U_(2d)(qn+1).
The subsequent predetermined powers C^(2^s d mod5), on fresh zero
targets, give for v=v2(qn+1)<=12:

    active=U_(d') m,   m=(qn+1)/2^v,   d'=2^(v+1)d mod5.

The active output is already the first port of F_(q,d')(m). Its four
possible coefficient shapes determine m and d' directly; the current
nonzero archive prefix determines v. No growing inverse-unit
normalization is needed by this mathematical reader. Every code has
Q(U_d)=5, so the active account is exactly 5m^2 at any admitted depth.

The four words are Galois-related at their powered-contact boundaries.
They use 34, 38, 37 and 41 literal native contacts on 16 core slots,
respectively. Their selection by the supplied initial chart remains
part of the interface. A native autonomous selector is not constructed.

## What the account now says

For q=3 every ready source has account 260n^2+12 and the same labelled
residues (0,0,4). This removes the old source's input-dependent first
residue obstruction. The other two occupied source ports still contain
the old n and are not automatically renewed.

The new literal depth records have exact total account

    R=5((3n+1)^2-m^2).

At 3->5, a strict reload of F_(3,d')(5), retaining those records, needs
additional account at least 4535. This is a necessary bound, not a
proved attainable minimum. For comparison, retaining the original
construction's records raises its account bound from 4352 to 4602;
its same-slot residue obstruction remains absolute.

Two further analytic limits delimit an iteration proposal:

- Every positive odd step writes at least 75 units of new literal
  record account in the four-chart construction. Finite funding gives
  a finite retention horizon even at the arithmetic fixed point.
- No fixed finite affine initial loading of the form a_l*n+b_l can
  fund a strict ready source after every step for every positive odd
  input. Explicit Mersenne prefixes have unbounded size amplification,
  while such an initial account is only a fixed quadratic in n.

These statements do not decide reachability of an individually funded
finite reload or a different history representation.

## Files and fixed replay

| File | Role |
| --- | --- |
| [PROOF-CHART.md](PROOF-CHART.md) | Four code vectors, native words, complete outputs and current-state reader |
| [PROOF-RESOURCES.md](PROOF-RESOURCES.md) | Literal record costs, sum bounds, retention horizons and loading obstructions |
| [REPLAY-SPEC.md](REPLAY-SPEC.md) | Fixed finite inventory and first-execution contract |
| [verify.py](verify.py) | Exact integer implementation of native contacts and independent closed formulas |
| [EXPECTED.txt](EXPECTED.txt) | Actual first stdout, 1167 bytes |
| [RUN.md](RUN.md) | Public pin and neutral first-execution record |
| [SHA256SUMS](SHA256SUMS) | Hashes of the seven companion files |

The identities were derived before this verifier was written. This is a
result-exposed publication replay. The complete source was publicly pinned at
[4b7e4e7d176bdae9bf77546d91fcb5a9d93fa234](https://github.com/mathorn1973/twist-j/commit/4b7e4e7d176bdae9bf77546d91fcb5a9d93fa234)
and all five files were read back before the first execution. That execution
passed all 12,648 cases and full inverses on Linux x86_64 with Python 3.13.5,
exited zero and wrote empty stderr. Actual stdout and the neutral record are
appended without rewriting the pin. Both proofs, the specification and the
verifier remain unchanged.

From the repository root, with Python 3.12 or later and assertions enabled:

    python3 -I notes/C-CONTACT-FOUR-CHART-RENEWAL-N/verify.py

The verifier executes actual primitive contacts and their inverses. It
checks complete outputs, every corresponding Galois macro boundary,
literal occupied archives and exact account formulas. It never executes
a claimed source reload.

The gain, correlated source preparation and bounded depth remain supplied
premises. No autonomous renewal, native-U bridge, physical calibration,
occurrence law, global Collatz result or Canon promotion is supplied.
The repository CI selectors do not run this notes verifier; their
architecture successes are repository-integrity checks.
