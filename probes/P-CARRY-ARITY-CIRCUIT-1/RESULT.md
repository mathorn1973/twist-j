# P-CARRY-ARITY-CIRCUIT-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: RESULT 6/6 ALL PASS
exit:    0
stderr:  empty
```

No preregistered scientific falsifier fired. The exact finite audit agrees
with the frozen all-n proof at the scope stated in `PREREG.md`. This records a
reproduced scientific result, not a registered Canon theorem. Registration or
promotion requires a separate sealed fold.

## Frozen all-n result

For

```text
q_n(x) = binom(popcount(x),2) mod 2
P_n    = {x in F_2^n, x != 0 : q_n(x)=0},
```

the complete nonzero singular locus `P_n` is a spanning circuit if and only
if `n=4`. Equivalently `|P_n|=n+1` iff `n=4`.

At the selected arity,

```text
P_4 = {1,2,4,8,15},     |P_4| = 5,
1 XOR 2 XOR 4 XOR 8 XOR 15 = 0.
```

Thus the arity four is selected inside the frozen second-carry family without
fixing a prime or an order-five target first; the cardinality five appears
only after the arity selection. The criterion itself, "the complete nonzero
singular locus is one spanning circuit", is a frozen arithmetic predicate and
is not claimed to be the unique possible carry selector or physically forced.

## Immutable pin and local leg

```text
public lock:          issue 314
base commit:          4d8558356f2f945b34e9f7fece323771d266585a
preregistration pin: 4234d5ef9e9720aa29b355a9aef15b0e529f59f9
PREREG.md SHA-256:    d36f804b1a397d7bb5291ad48cbc9ba046f6bdaf27824e08bd8288d06c6e4ebf
verify.py SHA-256:    8c77db1e149c56c06452b7267ac0ab1e59e3c15a4d8ee29d8f597c8c31874073

platform:             Linux
architecture:         x86_64
Python:               CPython 3.13.5
exit/stderr:          0 / 0 bytes
stdout SHA-256:       1f751aa0ce1773a218862eb47d6973884f9079fba9891d92778844207ceae329
stdout bytes/lines:   378 / 7
result:               6/6 ALL PASS
```

`EXPECTED.txt` is the exact stdout. `PREREG.md` and `verify.py` remain
byte-identical to the immutable public pin.

## Public two-architecture reproduction

The first PR workflow attempt failed before scientific execution because the
initial `RUN.md` prose did not use the repository's machine-readable field
schema. `check_policy.py` passed; the verifier was not run by that failed
attempt. Only `RUN.md` was corrected. The immutable `PREREG.md` and `verify.py`
were not changed.

The corrected head then passed the full public workflow:

```text
pull request:          315
workflow run:          31330712747
x86_64 job:            93288394923     success
aarch64 job:           93288394895     success
aggregate check job:   93288419843     success
Python:                CPython 3.12.13 in the architecture jobs
changed-probe replay:  success on both architectures
policy/canon/ledger:   success on both architectures
two-architecture gate: PASS
```

Both architecture jobs ran the changed public probe against the committed
`EXPECTED.txt`; the aggregate `check` reported `TWO-ARCHITECTURE CHECK PASS`.

## Earned scope and fences

The result removes the **fixed-order-five premise** from the narrow arity
selection step: within the family `q_n`, the unique spanning-circuit arity is
four and its complete singular circuit has five points. It does not by itself
select a five-cycle, orientation, exponent, cyclotomic field, `J`, or any
physical object.

The existing `CARRY-PENTAD [T]` remains separate and supplies only its already
registered fixed-frame consequences after the selected arity is four. No
zeta carrier, adelic completion, Hilbert-symbol or Redei realization, Weil
form, positivity, RH, decoder, measure, spacetime, or L2-L6 lift is claimed.
No Canon, Registry, Frontier, dependency, or status row changes in this probe.
