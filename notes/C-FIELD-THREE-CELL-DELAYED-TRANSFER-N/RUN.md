# Exact execution and source custody

PUBLIC / NON-CANONICAL / L1. This record creates no Canon authority.

## Pins and conditions before execution

- Public base: b8ba1a07ad776cdd8d878fe0a407e07312c0e263.
- Preregistration: 9e04d722d95f2ad4725ce859164ab8aa8ca5ccdc.
- Joint proof/code/reproduction pin: 2075904decf5d3da42214495e82a299410464b3c.
- Both pins were pushed before scientific execution. All seven public source
  files at the joint pin were fetched through the public contents API and
  matched local bytes exactly. Public main remained the stated base.
- No scientific execution, import, dry run or scratch numerical calculation
  preceded the joint pin. Symbolic derivation, independent static reviews,
  AST parsing, administrative hashes and environment checks did precede it.
- The first runner launch required a clean checkout and verified all seven
  working files against the committed blobs byte for byte.

## Frozen inputs

The first four names are in this notes directory. The last three are in the
matching minimal reproduction directory.

| file | bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 20933 | 9b9f0c6ceab706474ac74ed0229df30fafced164ad128400770315a18796aa7d |
| verify.py | 22065 | 42ec10cd001028ec126045647eea89347ec12bbf3612c40e1aa204ab77913a59 |
| break.py | 25489 | fc435a7efffea8edd4bd8e11aa12e16c2d1489a39c74997ae0b204837b7445b1 |
| PROOF.md | 26660 | d439f642b3447aec34efa3951ac70575182686b3168f44d89a53039ad90948b7 |
| reproduce verify.py | 1004 | c1bcd8ade32c78d829a42b75f97e22842cebe5595a44bb52991d558ee1beefea |
| reproduce EXPECTED.txt | 291 | 9d22bd31bbafd95b057e2ea230707db3947e6675d6bbaba25e854a141c20bf23 |
| reproduce README.md | 2054 | dcc90f854022d812a248eacdc6d57c83710ab46e7c2e530e81e265bbdeb152e2 |

## First local execution

Started 2026-10-01T08:27:25Z. Fresh environment readback: Ubuntu 22.04.5 LTS,
x86_64, Python 3.10.12 standard library, WSL. From the clean pinned root:

```text
python3 tools/check_reproduce.py --base b8ba1a07ad776cdd8d878fe0a407e07312c0e263
```

The unchanged runner set LC_ALL=C, LANG=C, TZ=UTC, PYTHONHASHSEED=0 and
PYTHONDONTWRITEBYTECODE=1, enforced its 120-second whole-bridge limit, and
executed BOTH pinned implementations. Each completed its exact assertions;
the combined scientific output was exactly 291 bytes, identical to the
prospectively frozen EXPECTED.txt, with exit 0 and empty stderr. This is
the first observed agreement; the prospective target was not labelled
measured before execution.

The enclosing command completed in 11.342 seconds, exit 0,
empty stderr. Its exact stdout is RUNNER.txt: 181 bytes,
SHA-256 `798d47670ea8936725f4af71f62599cb21831144dbefa77457e57e7235571cdc`.
Empty stderr SHA-256:
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.

The five scientific output lines are preserved in reproduce EXPECTED.txt;
RUNNER.txt is the unchanged checker's exact receipt, including bridge and
expected-output hashes. No scientific source, proof, expected output or scope
changed after the joint pin. This is the ordinary ACTIVE reproduction lane,
not a fabricated formal probe or GENESIS staging record.

## Public computation gate

Pending actual public x86_64 and aarch64 job readbacks. Local success alone
is not represented as a two-architecture gate. The draft PR will carry the
same seven scientific files and only added reporting/custody records.
