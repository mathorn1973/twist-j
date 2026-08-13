# Local exact run record

Status: **NON-CANONICAL**

Date: 2026-08-13

Preregistration commit:
`494ce485e92911c107b2a171935f76d7e3f81ff5`

Issue lock: [#364](https://github.com/mathorn1973/twist-j/issues/364)

## Environment

```text
platform: Linux 6.18.35
architecture: x86_64
Python: CPython 3.12.13
dependencies: Python standard library only
```

No machine nickname, private address, or floating-point scientific result is
recorded. This notes run is not a formal two-architecture public probe and
claims no architecture gate.

## Commands

With the source from `SOURCE.md` saved as `AME46_ORIGINAL.m`:

```sh
python3 verify_g0_g1.py AME46_ORIGINAL.m > g0_g1.stdout
python3 verify_g2.py > g2.stdout
python3 breaker_g3_g4.py AME46_ORIGINAL.m > g3_g4.stdout

cmp g0_g1.stdout EXPECTED_G0_G1.txt
cmp g2.stdout EXPECTED_G2.txt
cmp g3_g4.stdout EXPECTED_G3_G4.txt
```

Every command exited zero. All three stderr streams were empty. A second
complete run was byte-identical.

## Frozen artifacts

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| `verify_g0_g1.py` | 13795 | `5150dfeb2c7c1dc283263b2be503c2c64ce8bfc6ea04d019f26ba4dfe4e1fece` |
| `EXPECTED_G0_G1.txt` | 1151 | `3ed4587d8526cc3625cfbceefa4a8ab66983795c0bd90111e7486dd296d964cb` |
| `verify_g2.py` | 14006 | `43ee8b327811b0ec0b8c2f93a7ba52aaebc88da3e1640b59989d42e0841cc377` |
| `EXPECTED_G2.txt` | 1217 | `2069775de8a777617fc48ef73f14b19db0f9f103e315a430b5cb089a73bac7d2` |
| `breaker_g3_g4.py` | 12441 | `b8674539e40ab32c373366bae03af9f8ba3a28ea65c28232345575f8bff18578` |
| `EXPECTED_G3_G4.txt` | 1670 | `9d975d5e9a775e1752295877e27df14d977f0895cccaf93bac8268c8f2963577` |

The upstream input was 8515 bytes with SHA-256
`55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae`.
