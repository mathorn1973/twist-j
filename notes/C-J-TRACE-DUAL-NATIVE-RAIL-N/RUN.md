# Informal exact audit

NON-CANONICAL. Issue #2104 pinned the carrier, preparations, predictions
and failure conditions before computation. No formal repository probe
or formal scientific runner was invoked.

Public source commit 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed,
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
Source SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
The source is Apache-2.0 licensed; it is used directly, not copied into
this package. The new scripts are original proof-led, source-exposed
audit code.

First audit: Linux aarch64, Python 3.11.2. Both scripts exited zero.
The native source was fetched at the immutable base and its Git blob
identity checked before import. Executed verify.py and break.py are
archived byte for byte. The 36 READ lines from the first output matched
the alternate output byte for byte with cmp. The alternate calculation
uses the real quadratic ring and direct phase counts, and does not
exercise native full-field histories. Neither is blind review.

SHA-256:
```text
eb7d376b51ea50adb16c3660abc45c1442b5b7aac3b90f06cf37bc52adc3268f  verify.py
339421b93c206a5f676a356c8e74c3203c63991cce3172fe97a9e47d45620324  break.py
ac9e45d120b0d3465e2edc38472aef801ae299776c9582d50d74df31d35ff5d2  EXPECTED.txt
0c9e1e8e0312f8ccf54e376439df3bbbb6e59babe619bd25790107de7674b327  BREAK.txt
```

No formal public computation gate, status promotion or physical
inference is claimed. No external preprint code was incorporated.
