# Run record. C-RH-RAY-FINITE-WINDOW-CERTIFICATE-3-N

```text
STATUS:       NON-CANONICAL incubation record
AUTHORITY:    none
PUBLIC ROW:   none
CANON CHANGE: none
DATE:         2026-08-20 UTC
PLATFORM:     Linux x86_64, kernel 6.18.35
PYTHON:       CPython 3.13.5
```

## Order and custody

```text
issue lock
  #469

preregistration
  commit b568893de960063691de7d8d1c066017cef109a0
  blob   b23f6be3c4aef2864eb80297acade2fb03bcc27f

breaker pin
  commit 260adaf94266ee806661eac65d152ad8e4f4ffd1
  blob   5d31fecb5a417b8463deea8797a4d6a4334f5b38
  bytes  12117
  SHA256 3fa0ebbd647440ec0843fbc68f9a10dc4a024794496ea5431fd0d26688f68b2c

carried proof and exact matrix engine
  commit       83768fad3552a87b118a9c21d0a862a4b0b2ff6e
  proof blob   92dc38ca54d59ead6d4ff849bed9eae32edad950
  engine blob  e656d8fa2db5f968c19108621d17a70d4ba00716
  engine bytes 16016
  engine SHA256 e386abd2b362f3cfc0bc3181f3cc7fdcecfe64e21988c7520f29f540ea39d29e

fresh proof binding
  commit 63efdde5821ab5172ac9c402902bba81a058e9cf

accepted wrapper pin
  commit 4e49a3161b8f0399c1215bb842765c76c03e70b4
  blob   34191dff432a262d341ae34ac06f78ee1b1a7598
  bytes  1121
  SHA256 64abafbea39cf90ff345b011f4b96049d0e1126841384b9c78377c4a7965a575
```

The local execution bytes recomputed the remote Git blob identities for
`break.py`, `engine.py`, and `verify.py` before execution. Every identity
matched. The engine is intentionally byte-identical to the successful v56
matrix engine. The fresh wrapper differs from the failed #468 wrapper only by
its declared module name, explanatory text, and the load-bearing line

```python
sys.modules[spec.name] = module
```

before `exec_module`.

## Deterministic command

Both programs used

```text
env LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 <file>
```

No actual zero, external data, network, random search, floating-point
assertion, or filesystem write was used.

## Breaker run

```text
file:          break.py
exit:          0
stderr:        empty, 0 bytes
stdout:        492 bytes
stdout SHA256: d6f0dd421fd3b8bc5808605ab44454721b6c57b0665a1e380c5064606ff5cfa7
terminal:      BREAKER FINDINGS 0/10
```

The exact stdout is `BREAKER.txt`.

## Accepted verifier run

```text
file:          verify.py
engine:        engine.py, hash checked before import
exit:          0
stderr:        empty, 0 bytes
stdout:        691 bytes
stdout SHA256: 151c0da55a29d1bb370ec00f2543ff83a68de802431dc4793f9a16fdb9483a36
terminal:      RESULT 10/10 ALL PASS
```

The exact stdout is `EXPECTED.txt`.

## Evidence ceiling

This is one x86_64 lane and a result-exposed replay. It is not a public
computation gate, not another architecture, and not independent confirmation.
The written conditional proof may carry candidate-T inside incubation. The
bounded exact synthetic replay carries at most candidate-C. No public status or
RH evidence is earned.