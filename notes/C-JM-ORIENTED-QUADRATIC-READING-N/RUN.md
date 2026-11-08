# Local run record

NON-CANONICAL, L1. One architecture.

platform: Linux
architecture: x86_64
python: 3.13.5
sympy: 1.14.0

Commands: `python verify.py` and `python breaker.py`.
Both exit codes: 0. Both stderr streams: empty.
The second implementation was result-exposed; no independent agent.

```json
[
  {
    "file": "PREREG.md",
    "bytes": 5326,
    "sha256": "d83fd63b3f3518b247dc4a97378f708a09fb169d90d2af871b08627ffd54b885"
  },
  {
    "file": "verify.py",
    "bytes": 7333,
    "sha256": "39fd1ce7295dee64c10eb99681d19df4a618b7176e7dca39c6267a3c4da96444"
  },
  {
    "file": "ACTUAL.txt",
    "bytes": 1011,
    "sha256": "f87b21e161ec65e26652a98b6e82b9864c64659219b3b6f5370da95a051e1d46"
  },
  {
    "file": "STDERR.txt",
    "bytes": 0,
    "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  },
  {
    "file": "BREAKER-PREREG.md",
    "bytes": 1133,
    "sha256": "a89dfe4fdb55ea8f3235853b22f3a20b29cb81618ccf9dd1444ecc38ff40717d"
  },
  {
    "file": "breaker.py",
    "bytes": 4154,
    "sha256": "948f34cabfde8cbbce5c8c60cf06ddc35381f48661cfff7008341bd8366061f6"
  },
  {
    "file": "BREAKER-ACTUAL.txt",
    "bytes": 387,
    "sha256": "0b60e2b2048b1785a96a34e107384cf7bc40620c69bdf3627613c619d6b1ba40"
  },
  {
    "file": "BREAKER-STDERR.txt",
    "bytes": 0,
    "sha256": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
  }
]
```
