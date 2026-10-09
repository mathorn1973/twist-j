# Raw four-piston residue port

This supplementary standard-library exact audit accompanies the four L1
theorems in the Public Canon v101 fold claimed in issue
[#1435](https://github.com/mathorn1973/twist-j/issues/1435). Its inherited
public basis is Public Canon v100 at
`c164b79ce134152ac7cd600421791df74113f29f`.
The exploratory formulas and bounded results had already been exposed under
`C-U-RAW-RESIDUE-PORT-N`, NON-CANONICAL, L1, candidate-T/candidate-C.
They are not retrospectively preregistered. This directory is a minimal
proof audit, not a new formal public probe. The theorem status rests on the
written proofs, independently of the bounded audit.

Run from the repository root, after the audit code is publicly pinned and
read back:

```text
python3 reproduce/u_raw_residue_port/verify.py
```

Run without `-O`. Exit code must be zero, stderr empty and stdout
byte-identical to `EXPECTED.txt`. The program uses only integer arithmetic
and Python's standard library. It imports no repository verifier, reads no
external data, writes no files and makes no network request. The public
code-blob pin, byte readback and subsequent execution evidence are recorded
below; no retrospective formal run record is created.

The audit implements the original six-coordinate law directly and separately
implements the selected quotient table on `(z,q,r)`. It checks all 625 raw
piston inputs at common receiver ready `(0,1)` through tick 256, including
158750 restorations of the actual tick-three receiver and independent
quotient agreement. It checks all 25 common readies on all 625 sources
through tick three, their exact history and tail fibre sizes, the displayed
tick-three sum formulas and every projected-support overlap graph. A separate
finite support check starts at each of the 25 possible tick-three receivers
and runs through tick 1024. It also checks the 125-member source-sum fibres,
the compact context and reader boundary values, the exact cyclotomic
certificate, the integral inverse of J, and the universal `psi4=psi6`
collision on all 15625 origin-zero seeds.

## Executable readout and its inputs

`read_residue(n,q,r)` takes only the actual native counter and current
receiver. It returns `("BLANK", None)` before tick three or when the
restored receiver is outside the five-point codebook. It returns
`("PRESENT", kappa)` for the prescribed raw-input family at every tick
from three, including `("PRESENT", 0)` for a present zero sum. Negative
counters are rejected. All checkpoint arithmetic is modulo five; `n` is
a nonnegative integer, not a reduced counter.

`context(n)` computes `(sigma_n,z_n,N_n mod 5)` for `n>=3`.
`read_with_context(tau,q,r)` evaluates the same ready-region reading from
one of at most twenty context values. This upper bound is sufficient for
evaluation, not a minimum-size theorem or a mechanism for producing the
context. In fact, the explicit witness

```text
tau_4 = tau_6 = (-1,4,0),
tau_5 = (1,1,0),   tau_7 = (1,4,1)
```

rules out an autonomous update depending only on this particular `tau`.
It does not rule out an update using further state or supplied driving
information. The compact context does not separately certify the initial
ready region; replacing the counter requires an independently supplied
readiness distinction.

## Scope boundaries

The infinite-time reader identity follows from the exact synchronized
native chart. The receiver-only obstruction uses the inherited proof of
actual-clock recurrence at every point of the projected late support;
controlled reachability or this finite enumeration alone would not suffice.
It applies to every common ready, every fixed nonlinear receiver-only
reader and any eventual waiting threshold on the full raw-input family.
It proves a need for further distinguishing information, not a need for
the whole native counter.

At ready `(0,1)`, equal original sums give equal complete receiver histories
and each class has 125 sources. Reserving just one source for absence leaves
124 present sources with exactly the same observation. At the same port and
common counter a whole sum class must be reserved, leaving at most four
present residue values. A preparation that supports all five residues and
absence must provide an additional distinction actually visible to its
reader. Reserving a class alone supplies no physical absence mechanism,
persistent record or reset.

The identities `(J^2-1)(-2+j+2j^2+6j^3)=11` and
`J*(-j-j^2)=1` hold over the integral cyclotomic ring. Together with the
native collision they support the written no-go for a checkpoint-only
step reading into `Z[j]/5^m Z[j]` for every `m>=1`, with the recurrence
required at every step from n=0. A delayed-only recurrence is outside this
claim. This universal claim
does not extrapolate from testing finitely many moduli. The derived equality
`2^n payload(read_residue(n,C_n))=rho(J^n x_P)` is confined to the prescribed
family at `n>=3`, where the payload is defined; it does not select J as a
physical receiver law.

These are L1 mathematical statements. No empirical measurement, physical
preparation, internal evaluation of the reader, native context register,
source clearing for arbitrary raw inputs, reusable write, reset, event law
or cross-layer realization is supplied. The earlier five-symbol memory
with a larger receiver and a different source family retains its separate
scope.

## Audited source custody

Before the first execution of this audit, its complete source was stored
as public Git blob `5e757ae82934fc2e8e610ddac69f81f0ae47904b` and fetched
back through GitHub. The full UTF-8 source matched the reviewed local bytes.
Verifier: 10977 bytes, SHA-256
`f555b53e5647e17da978568ebc2d495a4c286ba2445bd35487aa067218523c6e`.

The subsequent supplementary run on 2026-10-09 used Linux x86_64,
Python 3.12.15, `LC_ALL=C`, `LANG=C`, `TZ=UTC`, `PYTHONHASHSEED=0`
and `PYTHONDONTWRITEBYTECODE=1`. It exited zero with empty stderr.
The captured stdout, copied unchanged into EXPECTED.txt, has 714 bytes and
SHA-256 `9e2865bc0ef5392c2cb80ee3519b7e2702cf43f14c6c87e6426c5c52b32678b2`.
This run is a supplementary finite audit on one architecture; the required
release workflow separately replays the exact expected bytes on both
architectures. It is not evidence of a blinded test or a formal probe pin.
