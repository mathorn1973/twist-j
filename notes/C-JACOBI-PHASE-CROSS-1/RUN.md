# RUN C-JACOBI-PHASE-CROSS-1

**NON-CANONICAL.** Incubation lane. Single-platform, non-formal runs. No
two-architecture gate, no GitHub rerun, no earned status.

```text
preregistration pin  2841517ab1df229bbdd98b7e879af18d766b78e5
                     (PREREG + both verifiers + selftest stdout committed
                     before the census execution)
platform             macOS (Darwin 25.5), single platform
architecture         arm64
python               3.9.6
environment          LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
                     PYTHONHASHSEED=0 TZ=UTC
working directory    repository root
```

## Run 1, micro-selftest (executed before the pin; no decision surface)

```text
command    python3 notes/C-JACOBI-PHASE-CROSS-1/verify_jacobi_selftest.py
exit code  0
stderr     empty (0 bytes)
verifier   verify_jacobi_selftest.py
           sha256 b72300a5cbcf005e4953d5fd874067b3c1fc09fd3f65ae27380df51c88b1dd06
           12022 bytes
stdout     stdout_jacobi_selftest.txt
           sha256 c272e4e93ed1c06b62676c24da4d209f73234465382e40c05b984f3c8607b064
           1205 bytes
result     all gates S0a-S0d, S1-S7 PASS
```

One pre-pin correction is disclosed: the first draft carried `29971` in the
frozen list of large anchors. `29971 = 17 * 41 * 43` is composite, gates
S1, S2, S3, S6 and S7 fired, and the anchor list was replaced by
`1021, 3001, 10061, 29921`, each now checked against the verifier's own
sieve before use. The fired gates were a correct rejection of a bad input,
not a moved threshold.

## Run 2, census (executed after the pin, once)

```text
command    python3 notes/C-JACOBI-PHASE-CROSS-1/verify_jacobi_phase_cross.py
exit code  0
stderr     empty (0 bytes)
runtime    1.65 s
verifier   verify_jacobi_phase_cross.py
           sha256 5240d99a73d33cc652e03a338ab0dc4f4d2605e079c77da3c68fafc69de3f18e
           11999 bytes
stdout     stdout_jacobi_phase_cross.txt
           sha256 5781ff3e9a5d6b34b183981e43e07e866c89ad774128186800e1b9601b4029ce
           2447 bytes
result     exact gates G1-G12 PASS on all 808 carrier primes;
           T1 NOT-REJECTED, T2 NOT-REJECTED, T3 NOT-REJECTED
```

No re-run, no re-binning, no carrier change after the pin.

## Interpreter witness (non-gate)

`verify_jacobi_phase_cross.py` re-run under Python 3.13.13 on the same
machine produced stdout with SHA-256
`5781ff3e9a5d6b34b183981e43e07e866c89ad774128186800e1b9601b4029ce`, byte
identical to the 3.9.6 run. Same architecture, so this is an interpreter
independence witness only and satisfies no architecture gate.

## Repository checks

```text
python3 tools/check_canon.py     CANON PASS v26 claims=210
python3 tools/check_ledger.py    LEDGER PASS claims=210 items=226
python3 tools/check_policy.py    POLICY PASS
```

`check_policy.py` iterates the filesystem root, so it also fails on any
untracked local directory. Two such directories predate this work in this
checkout (`.claude`, `scratch`); the PASS above is with them set aside.
Nothing in this directory adds a root entry.

`check_verifier.py` and `check_reproduce.py` fail on pre-existing probes
(`P-C8-BILINEAR-SHADOW-1`, `color-ladder`) because the local interpreter is
Python 3.9.6 and those verifiers call `int.bit_count()`, added in 3.10.
Unrelated to this directory, which is not scanned by either tool and which
runs on 3.9 and 3.13 alike.

## Independent witness check (float, non-gate)

The rapidity bins `QUART` and `H` were re-derived by an independent
floating-point path (`eta_p = log(|sigma_1(w_p)| / sqrt p) mod log phi`,
binned with ordinary comparisons). It reproduced the exact bin counts
`[155, 211, 202, 240]` and `[366, 442]` element for element. This is a
witness that the `Z[phi]` comparison ladder is not mis-binning; it is not a
gate and no claim rests on it.
