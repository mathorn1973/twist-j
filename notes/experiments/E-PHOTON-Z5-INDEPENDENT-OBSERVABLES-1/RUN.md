# Execution record

> **NON-CANONICAL / ZERO-EVIDENCE.** This is an engineering-integrity record.
> It carries no phase, Canon, Registry, Gate, Frontier or production authority.

## Freeze-before-run chronology

1. Issue `#748` was publicly reserved before the candidate existed.
2. The final reader, independent oracle, fixtures, verifier, documents and
   source manifest were committed without a formal execution.
3. Candidate commit `0c376934740fe2bdafc5270fb21fa90c4ad6eb96`, with parent
   `59cee594b974be6ccddf9785d35cf9da750d36a6`, was pushed to
   `experiment/E-PHOTON-Z5-INDEPENDENT-OBSERVABLES-1`.
4. The public commit and all 16 pinned files were read back from GitHub. Every
   byte count and SHA-256 matched. The pre-run receipt is issue comment
   `5494415485`.
5. Only after that receipt existed was the exact formal command executed once.
   It will not be executed again under this pin.

## Pinned custody

```text
26c2b7adb2543ed4c04d3f0bf407dec76174eaa66306d2e594e2872516e75eda  SOURCE_SHA256SUMS
6faaf8f43e3f91c5d07913c1bcd685fb2e44b09ff622fce55e9a8835f4eedd18  verify.py
5c23228ab8a019affbceef6373ed1d727150f363f9a25af4150519b3d71b3180  independent_reader.cpp
c8844e142509bd61825d408e7023de450c423d8bf28c9cc42b3b39d0d743cce3  fixture_oracle.py
```

`SOURCE_SHA256SUMS` is 1,489 bytes. The public pin/readback receipt owns its
hash because the manifest cannot recursively contain its own row.

## Frozen environment

```text
operating system  Windows NT 10.0.26200 x64
Python            3.12.10
Python flags      -B; optimize=0
CXX               unset
compiler          g++.exe MinGW-W64 x86_64-ucrt-posix-seh
                  Brecht Sanders r7, version 15.2.0
compile flags      -std=c++20 -O2 -Wall -Wextra -pedantic
```

## One-shot formal gate

The exact command was issued once from the repository root:

```text
python -B notes/experiments/E-PHOTON-Z5-INDEPENDENT-OBSERVABLES-1/verify.py
```

The capture began at `2026-09-01 13:08:10 UTC` and completed approximately
2,295 ms later.

```text
exit status       0
stdout bytes      72
stdout SHA-256    31c4eebd2f427fc27d0ea1c94980e7462abe1d786695774a3cbd4173a2415708
stderr bytes      0
stderr SHA-256    e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
```

Exact stdout is preserved byte for byte in `EXPECTED.txt`:

```text
INDEPENDENT_READER_FIXTURE_PASS
EVIDENTIAL_STATUS ZERO_ENGINEERING_ONLY
```

The formal gate compiled the pinned C++ source, checked the complete pinned
inventory and custody manifest, loaded the Python oracle directly from its
manifest-owned source bytes, exercised all positive and malformed fixtures,
and required byte-identical canonical JSON from the two implementations.

No production state was generated, opened or inspected.
