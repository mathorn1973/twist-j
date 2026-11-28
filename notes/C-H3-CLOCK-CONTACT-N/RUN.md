# C-H3-CLOCK-CONTACT-N run and custody

NON-CANONICAL / NO AUTHORITY. L1. Informal notes, not a formal public probe.
Date: 2026-11-28. Owner: GPT-6 Astra Pro session 2026-11-28.
Candidate-C computations; no status promotion or independent external review.

## Authority and preregistration

Public main and annotated canon-v117 target:
6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.
Declared content commit: d65e32c4b8e9a14496d3b7aba46fc384f51f81dc.
The content ancestry, tag object, all five normative SHA-256 values and
required main architecture/aggregate checks were read back before work.
The public issue and explicit remote-head scan found no colliding candidate.
The claim is [#2137](https://github.com/mathorn1973/twist-j/issues/2137).

Original preregistration was committed and publicly read back before its
computations at 53bc0c11b51d671f85977117a2b8df74f2b0698c.
PREREG.md: 9222 bytes,
SHA-256 e6b3225db9ff47f9ba8159675430de04f29dd6bfdfd0ddd736b0ae168e4cbdac.

The separate E extension followed the completed original findings and was
publicly frozen before its computations in
[issue comment 7239703583](https://github.com/mathorn1973/twist-j/issues/2137#issuecomment-7239703583)
and commit 1ec66152a8d50e56a9ed0b382690e6606d4016c3.
PREREG-E.md: 4235 bytes,
SHA-256 948ab61c34d22f23099a19a1546db52c17194e1c594bb78435da66a3a2945878.
Both repository preregistration texts were read back byte-identical to
the claimed texts. No original threshold or source file was retuned.

## Code custody and same-session blind separation

Each source was committed before its first execution. The public issue
preregistration preceded computation; these local code freezes were not
formal public gate pins. Helper commits were then integrated by ordinary
cherry-pick without changing their file bytes. Original local commit IDs
are session custody records, not claims that those original objects are
reachable from the public branch. Public integration commits below bind
the same source bytes.

| Source | Original local pre-execution commit | Public integration commit |
|---|---|---|
| response.py | 4c859a0a86b51064081e808d2c62aa91da84ce11 | 8b1d5f6 |
| verify.py | 612699595ec2198446bb4ac8359a35883a21649f | 6126995 |
| break.py | a2a33d4ec547672f02f76d837e5348222dfc4c1f | 3937360 |
| retention.py | 4bcfb1afa966bf79f8cf7d162c8060efd4d5342a | 4bcfb1a |
| break_retention.py | 764894f4cd83cb4f846846916395e4456bd4120d | 6d787ac |

The B/C checker author received the frozen preregistration and old source
specifications but did not read the new primary source or output before
freezing and executing break.py. The same separation was repeated for E:
break_retention.py was frozen and run without reading retention.py or its
output. Both primary sources were already frozen before the corresponding
alternate findings were reported to the coordinator. The alternate engine
uses its own cyclic-five ring arithmetic and its own C/B/field update.

These are separate code authors within one session. They are not
independent external reviewers. Section A has no blind alternate solver;
it has an exact printed residual certificate and the architecture replay.
The proof received a separate same-session review, which clarified its
generic boundary-locality and realized-predicate hypotheses. No scientific
code or frozen experimental criterion changed in that clarification.

## Immutable scientific replay

The complete public scientific package was replayed at
5c45447eccb91c1807e704b0cfe34cbc450ba1be.
Later additions are explanatory documents and this run record only.

| Role | System | Architecture | Python | Disposition |
|---|---|---|---|---|
| Original primary and alternate executions | Linux | x86_64 | 3.12.14 | All five exit 0, empty stderr |
| Complete committed-byte replay | Linux | aarch64 | 3.11.2 | All five exit 0, empty stderr, exact expected bytes |

The aarch64 checkout had the exact replay commit and was clean before and
after all five commands. Its initial launch encountered an unmaterialized
sparse-checkout path before any scientific verifier ran. Materializing the
same immutable Git files corrected that checkout setup; no source, target,
threshold or expected output changed. The complete successful replay is the
one recorded here. No failed scientific assertion was discarded.

The scripts use only Python's standard library. The replay environment
set PYTHONHASHSEED=0, PYTHONDONTWRITEBYTECODE=1, LC_ALL=C, TZ=UTC.
Commands were the five Python invocations in README.md, from the repository
root, each compared byte for byte with its paired committed output.
Cross-architecture byte agreement is reproduction. It does not constitute
independent authorship or promotion to public computation-grade T.

### Source bytes

| File | Bytes | SHA-256 |
|---|---:|---|
| response.py | 12563 | 12c966ca69084d6bc7fa592519e15dca60059cb736a17560e92403b6344e6427 |
| verify.py | 17618 | c754e65a80a8b10523177296825d4d260c2d79012a59ec3139e6caa2598c9d2d |
| break.py | 21447 | a8a7ae5d1f08156ad6dbd766602e658cb2d5e5f6840097c07a2aa75c48d61b60 |
| retention.py | 9663 | b111786b33e937410e9fd95b6fbc53e3203343bb3a071478e2c892ae854e493e |
| break_retention.py | 10013 | 292373011ef18a55f9f7b8e6b0ba1e186c78829114bf4f0367f8a00bb48bc32f |

The pinned native source is reproduce/h3-referenced-record/verify.py,
SHA-256 4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
The primary scripts check it directly or through the hashed primary module.
The alternate scripts import no native verifier or new primary module.

### Expected scientific stdout

| File | Bytes | SHA-256 |
|---|---:|---|
| RESPONSE.txt | 3130 | d5de448664deb0da0124731c2eaa7736221e27f4fd8e12e0dc46e1c6a29f4893 |
| EXPECTED.txt | 4802 | 02f41961c73df16d1689f8495705baa05a6f7d508cb82fc5f3ac810baf619acf |
| BREAK.txt | 2875 | 5b59eb44e73437cc3d88ac3d6942578758483979296129f86163844cfb54e1b9 |
| E.txt | 11613 | b0eff11960532777fd00b945725ec93bd2ca700e2d327ae742de2f740f547120 |
| BREAK-E.txt | 11999 | fcd68b37fb0fcbfaaf5e3ab8ceab571c1514c96ac15db2105efe49903473ee95 |

Each row is byte-identical across the two architectures. Primary and
alternate have intentionally different transcript formats and are not
claimed byte-identical to each other; their scientific outcomes agree.

## Coverage and boundaries

The A response covers both frozen earlier events, each single and their
pair, all eight source/worker radiation slots, complete baseline accounts
and inverse, plus the exact rank/residual certificates.

B/C checks the complete first interval, all 25 second-input pairs with
proved 10-state equality where deduplicated, all bank rows and unwanted
times, both selected targets, full accounts and inverses, material class
counts, immediate reversal, continuation and literal restoration counts.

E checks every m=1..8, the same complete first/prefix fields, the specified
four-slot impulses, all four incident next-C contacts, exact local B2
reversal when applicable, and the 32 subsequent ticks at both stages.
The alternate transcript supplies explicit input witnesses for class
failures as well as the matching finite verdicts.

No third-input test, native input loader, native S0-reading circuit,
permanent hold, full second restoration, physical effect or occurrence,
native-U equivalence, layer lift, or Canon promotion was tested or earned.
