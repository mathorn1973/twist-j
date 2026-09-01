# P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-1

Deterministic zero-evidence qualification of the exact arbitrary-width dyadic
orbit sampler and fail-closed two-child supervisor reserved on issue #756.

The orbit fixture reproduces the old `shift >= 63` guard on the exact
high-level two-plane envelopes `(0,-72,-36)` at `L=6` and `(0,-128,-64)` at
`L=8`, then verifies exact `cpp_int` sampling.  It separately reproduces the
old sum-overflow and 64-bit bounded-draw-width guards.  Whenever the inherited
`uint64_t` path is defined, including its `bit_length(total-1)<=63` condition,
selected indices and random-bit consumption remain byte-identical.  The
independent supervisor fixture preserves bounded stderr custody and both
return codes, cancels queued work, kills running siblings and reaps every
child.

The canonical verifier is

```sh
python3 probes/P-PHOTON-Z5-DUAL-WARD-ENGINE-QUALIFICATION-1/verify.py
```

It compiles and runs only synthetic fixtures, requires empty stderr and exact
LF stdout, verifies `SOURCE_SHA256SUMS`, and byte-compares the combined fixture
with `FIXTURE_EXPECTED.txt`.  It needs no network and opens no abandoned seed,
log, partial stream or Ward value.

The only successful terminal is

```text
WARD_ENGINE_QUALIFICATION_PASS
```

Every outcome has maximum status `ZERO_ENGINEERING_ONLY`.  A pass does not
satisfy issue #757/F3, does not authorize production issue #742, and does not
reserve CROSSCHECK-3.  Canon remains Public Canon v74 and no physical or
cosmological claim changes.
