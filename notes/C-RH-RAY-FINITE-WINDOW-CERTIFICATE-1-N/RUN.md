# Run record. C-RH-RAY-FINITE-WINDOW-CERTIFICATE-1-N

```text
STATUS:       NON-CANONICAL incubation record
AUTHORITY:    none
PUBLIC ROW:   none
CANON CHANGE: none
PLATFORM:     Linux x86_64, kernel 6.18.35
PYTHON:       CPython 3.13.5
DATE:         2026-08-20 UTC
```

## Ordering

The public issue lock #466 preceded every file and every run.

```text
1  PREREG.md committed and remotely read back
   commit 07b27c044c7c86fd49d1c52ef1f9a9aaf42bd051
   blob   fc4ffa8f49c633180ceebb2c39b6e14d34b0770e

2  break.py written without an accepted verifier, committed, and remotely
   read back
   commit 7b377ebb8c27be4b2e2ae940b081bbe367d674ec
   blob   a6493c43b9d89161883252bb80261cc52dfc8392
   bytes  12344
   SHA256 a0999c1efb5808b027ff3f36ebacbfb91f62e54bdbea4e638a002d2b4fc128ef

3  breaker formal run 1, approximately 2026-08-20T17:43:52Z

4  PROOF.md committed
   commit d361872dc8c5a82e3ac5ad051bdc525fe02ac966
   blob   8f323c7ebd4a4595b6842f592807a8f2e10b627b

5  verify.py written after the breaker result, with that exposure disclosed,
   committed, and remotely read back
   commit 7c070053cb1d32f5f510467ff0ed33a079faf065
   blob   e656d8fa2db5f968c19108621d17a70d4ba00716
   bytes  16016
   SHA256 e386abd2b362f3cfc0bc3181f3cc7fdcecfe64e21988c7520f29f540ea39d29e

6  verifier formal run 1, approximately 2026-08-20T17:51:15Z
```

The locally executed breaker and verifier were reconstructed from the remote
files and their Git blob identities were recomputed before execution. They
matched the remote blobs exactly. Neither pinned program was changed after its
first execution.

## Frozen command

Both programs used

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 <file>
```

No network, external data, randomness, floating point, filesystem write, or
actual zeta ordinate was used by either program.

## Breaker run

```text
exit:         0
stderr:       empty, 0 bytes
stdout bytes: 484
stdout SHA256:fce07f7eed8e9fab462ed37311a9e485abb7164bf8ed24fbb348213f7509849c
terminal:     BREAKER FINDINGS 0/10
```

The exact breaker stdout is `BREAKER.txt`.

## Verifier run

```text
exit:         0
stderr:       empty, 0 bytes
stdout bytes: 691
stdout SHA256:151c0da55a29d1bb370ec00f2543ff83a68de802431dc4793f9a16fdb9483a36
terminal:     RESULT 10/10 ALL PASS
```

The exact verifier stdout is `EXPECTED.txt`.

## Evidence ceiling

This is one x86_64 lane. It is not a public computation gate and does not
satisfy a two-architecture requirement. It earns at most candidate-T for the
written conditional theorem and candidate-C for the exact bounded synthetic
audit. The breaker run is an independent code path inside the same session,
not independent confirmation by another owner and not another architecture.
