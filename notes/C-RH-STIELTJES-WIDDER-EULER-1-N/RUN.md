# Run record

```text
STATUS:          NON-CANONICAL single-platform candidate audit
PUBLIC BASIS:    Public Canon v57
MAIN/TAG:        4ef54f0c34f80897af0121a2d93b710e70a8377c
CONTENT_COMMIT:  8e8b04abe4d3359942449533854ef1d142be70df
CANON_SHA256:    c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON_BYTES:     295013
PLATFORM:        Linux 6.18.35 x86_64
PYTHON:          CPython 3.13.5
DATE:            2026-08-20
```

## Order and custody

The frozen order was followed.

```text
1. PREREG.md committed:
   commit 4e3abc1e68e49915bf52cd28f806e3f74731769a
   blob   9cc01fd28e34a8c89d2a72163fca73cd65638caa
   remotely read before breaker authorship.

2. break.py committed:
   commit 783b24927cc80ea9ff9c0db55c5ccc240eb65f00
   blob   418320636e4bc3368a0f65456a1f4ab02430dff1
   SHA256 79cc932b483354398cceb396ee8cf6687fe2e8dc37f5a3321db969139f8b6057
   bytes  6450
   remotely read before execution.

3. The first clean-clone attempt failed at DNS before Python was invoked.
   It produced no scientific execution and no script output. The pinned UTF-8
   content was copied locally only after remote readback. `git hash-object`
   reproduced the remote blob exactly before the interpreter was entered.

4. break.py executed once under the frozen environment.

5. PROOF.md committed only after the breaker run:
   commit e6935c7b1d3b74de7317f3321916a2a446d45369

6. verify.py committed:
   commit 9026d349112220fecf5323957b89f521c72d6a25
   blob   b4d629ff4a3ac38d3efe78bc4d695a416ec08da1
   SHA256 23537184c77fd344b7b882d15f048382d8a3731599bbd0d80ea527e18932f73c
   bytes  7903
   remotely read before execution.

7. The pinned verifier was copied locally only after readback.
   `git hash-object` reproduced the remote blob exactly.

8. verify.py executed once under the frozen environment.
```

No pinned file was changed after its first execution. No retry, threshold
change, carrier change, range change, or expected-output change occurred.

## Frozen command environment

```text
LC_ALL=C
LANG=C
PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0
TZ=UTC
```

## Breaker result

```text
exit:            0
redirected stderr: 0 bytes
stdout bytes:    437
stdout SHA256:   abea20cbd8de8b3e7e53bdde516149b4b8d6f51ac57ce647638ccb19d41a8dba
terminal line:   BREAKER FINDINGS 0/10
```

The exact stdout is `BREAKER_STDOUT.txt`.

## Verifier result

```text
exit:            0
redirected stderr: 0 bytes
stdout bytes:    621
stdout SHA256:   5e4663f529ea8904f040a7c225db6af16e3f19de39ff03d9e354f7eae4acb2c1
terminal line:   RESULT 12/12 ALL PASS
```

The exact stdout is `EXPECTED.txt`.

## Evidence boundary

This is one x86_64 lane only. It is not a public two-architecture gate and
cannot earn public computation grade. The all-variable statements are carried
by `PROOF.md`; the scripts are exact finite audits using rational synthetic
controls. No actual zero, external dataset, floating-point assertion, or
network data entered either run.
