# Execution and immutable source custody

PUBLIC / NON-CANONICAL, L1. No Canon status or authority is created.

## Pins before execution

- Public base: `b8ba1a07ad776cdd8d878fe0a407e07312c0e263`.
- Preregistration: `f3993f87f537cfaa991bef3875ba5d74bfc82855`.
- Joint code/proof/reproduction pin: `9645330e26e4dcae91d5db019c8a7145e9c0004b`.
- Both pins were pushed and their remote heads read back before scientific
  execution. Public main was still the declared base at the code-pin readback.
- The checkout was clean. All seven scientific/input files were compared
  byte for byte against their committed blobs before launch.
- No implementation was executed or imported, and no scientific dry run or
  scratch calculation occurred before the joint pin. AST parsing and static
  review were the only pre-pin program checks.

## Frozen files

Paths in the first four rows are relative to this notes directory; paths in
the remaining rows are relative to the matching standard reproduction.

| file | bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 18107 | 0cc0e1cffe396d6dbef867549c6bf7634ea1e9c453f8ccec9eb6aab72a2ed753 |
| verify.py | 15018 | b0b3312f7c7f9b7cc3a3ad89ac6d7800a32099cb8b1e5098205c90fff17c7d84 |
| break.py | 21434 | d581ab780dc74b053ac51220df87c6adb6ed67af2429b4480dae892b76e5e89f |
| PROOF.md | 14740 | 58cc146e07a32dd36119cb9caf52e9c58c1137d7216fb0f48ba264e8da272861 |
| reproduce verify.py | 999 | 6c8a5f31db6820ab9aa2c63dcbef40c21b711f2668b9a78484a44b504a946e91 |
| reproduce EXPECTED.txt | 285 | 45e85949c1282724ea4f99893abcc65a29284994e97c1f7f97eea6d44cd8e709 |
| reproduce README.md | 1796 | 536008174e241ad97349aeaa3655c2183c859a7eb504e87cfdc5bf0862ae6ee5 |

## First local execution

Started 2026-09-30 23:53:36 UTC (2026-10-01 local date). Environment:
Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12 standard library, WSL.
The unchanged repository command, from the clean code-pin root, was:

```text
python3 tools/check_reproduce.py --base b8ba1a07ad776cdd8d878fe0a407e07312c0e263
```

The current runner supplied LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0
and PYTHONDONTWRITEBYTECODE=1 and enforced its 120-second bridge limit.
It observed exit 0, empty stderr and all 285 scientific stdout bytes equal
to the prospective EXPECTED.txt. This is the first measured agreement with
that target; the target's earlier existence is not itself execution evidence.

The enclosing command also exited 0 with empty stderr, in 7.627 seconds.
Its exact stdout is RUNNER.txt: 179 bytes, SHA-256
`73e8f48b8a9c2a59da7909f54cc630143980685338a29afeeba566ce1beba771`.
The empty stderr SHA-256 is
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The five observed scientific lines are preserved in the reproduction's
EXPECTED.txt. RUNNER.txt records the unchanged checker's exact PASS and
wrapper/expected hashes. Neither source changed after this execution.

## Public computation gate

PENDING: both public PR architecture jobs must execute this reproduction.
Local x86_64 agreement does not satisfy that gate. The result is not yet
reported as public two-architecture acceptance. Append actual job URLs,
head, Python version and the matching REPRODUCE PASS readbacks here.

This package uses the ACTIVE repository's ordinary PR reproduction workflow;
it does not create GENESIS staging records or a formal probes/P-* lane.
