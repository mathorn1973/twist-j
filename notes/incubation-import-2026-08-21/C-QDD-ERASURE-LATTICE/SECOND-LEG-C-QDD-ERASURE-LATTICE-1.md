# SECOND-LEG. C-QDD-ERASURE-LATTICE-1

NON-CANONICAL. Candidate lane, no authority. This file records a second
independent execution architecture for the three programs of
C-QDD-ERASURE-LATTICE-1. It creates no claim and changes no status.

## What was compared

The three frozen programs were transported to a second machine and executed
under the frozen command with no edit of any kind. Unlike the audit programs
of the 2026-08-20 bundle, these three read no repository path and take no
argument, so the transported bytes are identical to the executed bytes and
no path line had to be adjusted.

```text
frozen command (both legs)
  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC python3 <file>

leg 1   Linux x86_64, CPython 3.11.15
leg 2   Darwin arm64, CPython 3.13.13
```

Two different operating systems, two different processor architectures, two
different CPython minor versions.

## Program bytes, identical on both legs

```text
verify_qdd_erasure_lattice_1.py
  e482ed41ffa7471a7307ee0cf02d1d2d7bd3f6cab2be39318b2c7978a471c9b8   18550 B
breaker_qdd_erasure_lattice_1.py
  c1223b967bfdf864ef9f8a38bf11515bfbc2f5d28171a68234079cfb5eb6f89b   11792 B
diag_qdd_erasure_lattice_1.py
  3fa07d6eb1b9b279756bb4b6908c426407c050a962169057578fce0ecf81fb28    6454 B
```

No CR bytes, final LF present, verified on the second leg after transport.

## Results, byte-identical on both legs

```text
verify   stdout  eaa53d32a8f2eace3d4d2e993993588fea9afd309d38d1def07a1ba4fd36a140
         exit 0, empty stderr, 45 of 45 gates PASS, DECISION: ERASURE-LADDER
breaker  stdout  9c3ef3ae4e0996bd1aa0ac2a9c4ec597ba9c19bfb9ba72e38e4998b9edec263a
         exit 2, empty stderr, 9 of 10 HOLDS, FINDINGS 1 of 10 (B4b)
diag     stdout  e85f5203614797555743e4bba2f6a5718fd8de0fa1716ed74d9886787523517b
         exit 0, empty stderr, DIAGNOSIS confirms the E3 member list
```

The stdout files committed in the handoff repository are the leg 2 outputs,
written by execution on the second machine rather than transported. Their
SHA-256 values equal the leg 1 values recorded in
`RESULT-C-QDD-ERASURE-LATTICE-1_2026-08-21.md`, so the two legs agree byte
for byte including the fired breaker line and its exact counts.

## What this does and does not establish

```text
DOES     the arithmetic is exact and platform independent across the two
         legs; no float, hash-order, locale, or word-size dependence is
         present; the fired breaker line B4b reproduces exactly, so it is
         a property of the frozen construction, not of one machine.
DOES NOT establish anything public. This is a candidate-lane reproduction,
         not the two-architecture gate of the public probe protocol, which
         requires a pinned public branch and the GitHub check at pull
         request time. QDD-INSTRUMENT-APPARATUS remains O with O1 and O2
         open. SAMPLING NOT PROVIDED.
```

## Handoff location

```text
repo    mathorn1973/twistj-handoff (private)
branch  handoff/qdd-erasure-lattice-20260821
commit  6ad511d0f7917d9d8c7755e393c2746e89d16cd9
parent  0928939019f2ce451f4e63a132c0993ca6fb06b7 (origin/main at push)
files   11 new artifacts plus one INDEX.md manifest section
```
