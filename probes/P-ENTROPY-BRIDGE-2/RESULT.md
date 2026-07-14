# P-ENTROPY-BRIDGE-2 result

Status: FORMAL AARCH64 RECORD; PUBLIC X86_64 GATE PENDING

## Scientific decision (aarch64 leg)

```text
RESULT 10/10 ALL PASS, exit 0, stderr empty.
```

All ten preregistered gates passed on the first execution of the pinned
verifier (pin commit eb54dff5ac4176017f5de8bca695953292a469f5, public lock
issue 27, base dfb8bc43f9f1c9df25aaa334fa9780f460e75f51).

Recorded outcomes at the preregistered scope:

```text
G05 + G06          THE CYLINDER NO-GO. The pure-word constraint system has
                   zero solutions for every driver window L = 4..16, and
                   the zero residue class is J-invariant with positive
                   Haar measure at every depth, so NO exact
                   finite-cylindrical cut with driver window <= 16 exists
                   at ANY lambda-depth. The obstruction is the driver-word
                   holonomy alone; the residue tower cannot repair it.
G07 + G08          corroborating full tables: zero solutions at
                   lambda-depth 4 (L <= 6, every current position, orbit
                   lengths {1, 4, 20}) and lambda-depth 8 (L = 4, orbit
                   lengths {1, 4, 20, 100}).
G09                THE ONE-BIT-PER-SCALE LAW (C at finite range): the
                   renormalized block maps are exactly 2:1 on the
                   recurrent core at every dyadic scale k = 0..10, both
                   letters: |image| = 3125 = 6250/2 exactly. One bit
                   hidden per scale, never more, never less.
G10                the odometer-cylinder reading with one block label
                   fails with the exact pattern: first collision at
                   4096 + 2^(k+1), k = 1..10.
G01-G04            framework pins: orbit spectra mod 5 and mod 25, no
                   constant cut, core 6250 on 313.
```

The recorded F: the finite-cylindrical ansatz for the bridge cut is
falsified at the tested depths, with the killing-lemma extension over all
lambda-depths for windows <= 16. The recorded consequence, carried at its
stated grade: a solution of the bridge equation, if it exists, is
measurable and not locally constant in the driver coordinate; it must read
unboundedly many letters (the carry structure), with the lambda-digit
tower of O_{K,lambda} as the natural per-scale carrier. No scientific gate
fired against the preregistration; the no-go is the preregistered
expected outcome, recorded first-class.

## Scope

Layer L5. Window lengths above 16 and lambda-depths above 8 untested;
measurable non-cylinder cuts are successor scope. No L2 lift, no L6
measure claim, no canon, registry, or frontier edit.

## Two-architecture computation gate

```text
aarch64 leg:  PASS (RUN.md in this directory; stdout sha256
              62ed9aef7226f363684f316511e9baa62972afd394aeb24def45ad9c376ca2ba,
              1296 bytes)
x86_64 leg:   PENDING (the public pull request check)
```

This file will be extended with the public run and job reference and the
final gate status after the x86_64 comparison, in a further commit that
does not alter the pinned files.
