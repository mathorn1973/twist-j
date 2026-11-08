# Review — P-RELATIONAL-MASS-STABLE-BINDING-1

Disposition: completed local PASS; required CI pending at this review.
Scope remains NON-CANONICAL, NEW_DECLARED L1.
Ownership: https://github.com/mathorn1973/twist-j/issues/1688
Base: `8a2e6a3b1f35bfc2e2616c340086a7182ffbc050`.
Prospective pin: `79d2247fd8e6937347e367b922de1c6e24a54cb4`.

## Contract, sources and analytical scope

The six required preregistration fields were present before execution:

| Field | Concrete content reviewed |
|---|---|
| Equation | Common action, four Hamilton equations, energy exchanges, conserved J and delta, binding and minimum inequalities |
| Code | Separate Fraction/Taylor/binomial/adjugate primary and integer-pair/Picard/root-recurrence/matrix-recurrence breaker |
| Carrier/data | Real SPD G, symmetric Pi, relative canonical r,rho; two unit groups at P=0; exact ordered fixtures and degree-four audit |
| Systematics | Frobenius multiplicity, factors of two, inverse/root domain, evolving momentum, delta sectors, proper distance, fixed-charge quotient scope |
| Failure threshold | One exact discrepancy; F01–F12; completed FAIL distinguished from incomplete abandoned execution |
| Action layer | Explicit NEW_DECLARED L1, without native, physical-particle, calibration or cross-layer promotion |

SOURCE.md binds the unchanged public Canon v103, administrative baseline,
predecessor #1687 and historical attachment hashes. Its collision audit
distinguishes the occupied scalar/integer oscillator, local-parent,
fixed-support bound-charge and Hilbert gauge-Hamiltonian lanes. Historical
mass-volume/proton statements do not select this interaction or kappa.

The reduction preserves p1 dx1+p2 dx2=P dX+rho dr. On P=0, p1=rho/2
and p2=-rho/2; E=sqrt(rho^T G rho) is the sum of the two individual energies.
Both factors of two and the symmetric off-diagonal pairing are accounted
for before variation. The potential supplies both metric and matter forces.
Their reaction terms give the three exchanges whose sum vanishes; separate
source-energy conservation is neither assumed nor obtained.

The conserved GL(2) matrix charge gives delta=det J-(tr J)^2/4.
Whitening yields 4delta<=(y wedge q)^2<=|y|^2|q|^2, hence E^2 V>=4kappa delta.
The gap identity (9a) supplies an exact audit without numerical matrix roots.
For delta>0, conserved nonnegative H bounds proper separation above and
away from zero and supplies a positive stream-energy floor. Metric kinetic
bounds control G on finite intervals; the energy floor keeps rho away
from zero there. These combined bounds support complete smooth flow after
the interaction has made momenta evolve. At Pi=0, rank-one J gives
delta<=0: this protected sector needs nonzero initial metric momentum.

The sufficient delta>0 criterion is not asserted necessary. The collinear
comparison reaches the nonsmooth momentum boundary without continuing the
original flow through it; delta<=0 does not imply proper escape. The
kappa=0 comparison recovers the predecessor's unbound proper separation.

For traceless elliptic charge, the sharp one-variable bound has a unique
stationary root by opposite strict monotonicity. The kappa=3, delta=8
witness attains H=10 at a=3. Its initial Hamilton field and covariance give
the exact group orbit; its full labeled period differs from the metric's
half-period. The stronger theorem fixes kappa=3 and the exact J=J* level.
It identifies the whole minimum set as a centralizer orbit, bounds the
metric condition number on energy sublevels, and removes the free scale to
obtain compact representatives. Conserved energy then supplies nonlinear
Lyapunov stability modulo Z(J*). This is not arbitrary-J or nonzero-P
orbital stability, coordinate-scale stability, attraction or a physical
stable-particle claim. The harmonic interaction and kappa remain choices.

## Code, security and independence

The coordinator fully reviewed the primary. This reviewer read the breaker
in full without reading the primary or running/importing either program.
The breaker review traced reduced integer-pair arithmetic, four Picard
passes, root and inverse recurrences, Hamilton gradients, all invariant
checks, covariance, periodic/minimum calculations, eight live negative
controls and exact payload ordering. No concrete code/contract bug was found.

| Reviewed implementation | Bytes | SHA-256 |
|---|---:|---|
| verify.py | 25072 | dca77be0c45671fcd2c78f6873bc8970984a93839475170a230d0873df0b7fae |
| breaker.py | 31145 | bfea3156ebb10d965a03b23be33d9425e955df34903c3edaf46abe4ac7bd153a |

The breaker's only imports are hashlib.sha256, math.gcd/isqrt and pathlib.Path.
Its only runtime reads are the five fixed authority files, verified before
scientific computation. It has no writes, subprocesses, network, environment
or secret reads, companion/predecessor reads, floats, dynamic execution or
outcome-file reads. The coordinator's primary review confirmed the isolated
sibling invocation with the same interpreter, -I, shell=False, closed stdin,
fixed minimal environment, captured streams and the 540-second timeout.
Both payloads are computed in memory; no expected digest is supplied.

The implementation authors were isolated from companion and predecessor
scientific source, while sharing the common contract and proof. Coordinator
and analytical reviewers knew the predecessor and prospective predictions.
This is same-session review, not external blind review or independent model
discovery. The finite audit supports the analytical proof; its truncation
cannot establish all-time binding or stability by extrapolation.

## Pin custody and observed result

The coordinator fetched all six complete public files at the immutable pin
and compared their bytes and Git blobs before the public receipt:
https://github.com/mathorn1973/twist-j/issues/1688#issuecomment-6297016370
The receipt was created at 2026-10-20T17:29:48Z and read back before the
first run. This reviewer independently fetched the unchanged receipt after
the run and matched all six local byte counts, hashes and committed blobs.
The frozen files have no diff against the pin; its manifest hash is
`ec457f7f91714acb8ef46e705d98961dac3b7094aad6066580b8e2088990b523`.

Direct review of the original stdout, stderr and metadata confirms one
completed first formal invocation on Ubuntu 24.04.3 LTS, x86_64,
Python 3.12.14. Start: 2026-10-20T17:29:56.537967Z; finish:
2026-10-20T17:30:48.826110Z; elapsed 52.288 seconds; exit zero; stderr empty.
Stdout is 455 bytes, 20 LF-terminated lines, SHA-256
`cefaf22c7a6112835ccf1e4b4114e3b8ac0393445c7df7d6fa6c9582efef33ec`.

The actual certificate reports 210 trajectories: 51 elliptic, 21 parabolic,
138 hyperbolic; 1050 coefficient rows, six covariance cases, one periodic
case and eight detected negative controls. Its 1329-record payload digest is
`5f981356b844fe332740ab1ba3d90de15479e71ccb32d96913dcfecfcca56d15`.
It ends with CERTIFICATE_RESULT=PASS, BREAKER_RAW_BYTES=IDENTICAL and
RESULT=PASS. The negative controls passed by detecting the specified false
alternatives; no failed control or excluded sector was relabeled as binding.

No scientific rerun was performed for this review, and none of the six
prospective files was edited. Required x86_64/aarch64 byte-identical replay,
policy/Canon/ledger/gate checks and preserved pin ancestry remain merge gates.
They were pending when this review was written; a local PASS is not their
completion and does not promote any Canon claim.
