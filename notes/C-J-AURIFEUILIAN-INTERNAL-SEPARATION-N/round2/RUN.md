# Round-two exact execution record

**NON-CANONICAL. NO AUTHORITY. Finite evidence: candidate-C.**

## Complete four-unit menu, R2-M125

Source pin: `7b50c67e16e712d5653d9f594d506eacff2d0ba7`.
The public GitHub connector returned all three source files byte-for-byte
before either program was executed. The remote branch head was also read
back at this exact pin. The checkout was clean at the start.

| Source | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 5933 | bee0fd397370dadcc1aecc0b96ab77bcc7e078816096142a35e99f12bb54d234 |
| verify.py | 3860 | 3df05739e598d11ea4cb8f7e9d0d407716a09c98adc219236b5ee4e1efe96996 |
| break.py | 3525 | 1c0dd934db616592b7fdd7fc25cae50c342558385218f8f531264713b8fb6234 |

Platform: Linux, Debian 12. Architecture: aarch64. Python: 3.11.2.
Both processes received PYTHONDONTWRITEBYTECODE=1, PYTHONHASHSEED=0,
LC_ALL=C and TZ=UTC. Each had the preregistered 600-second process limit.

Commands, from the repository root:

```text
python3 notes/C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/round2/verify.py
python3 notes/C-J-AURIFEUILIAN-INTERNAL-SEPARATION-N/round2/break.py
```

| Program | Exit | Stderr bytes | Stdout bytes | SHA-256 of stdout |
| --- | ---: | ---: | ---: | --- |
| verify.py | 0 | 0 | 1032 | e90991f9b8c2f98b03170e5270ed85894871f1cbf69242898e49d60550f88ea3 |
| break.py | 0 | 0 | 1032 | e90991f9b8c2f98b03170e5270ed85894871f1cbf69242898e49d60550f88ea3 |

The complete outputs were byte-identical. Both programs processed all
1562500 prescribed comparisons. No input, bound, source or threshold changed.
For each side the histogram is gcd 1 on 781246 labelled tests and gcd N
on four tests, with no proper gcd. The full outputs are EXPECTED.txt and
BREAK_EXPECTED.txt. The reported support partition has one atom per side;
the program makes no primality assertion about that atom.

The source authors used the same frozen mathematical specification and
output schema. The recurrence author did not read the matrix source before
both hashes were frozen; the matrix author did not read the recurrence
source before that freeze. Both then performed static source review before
execution. This is independently authored code comparison in one session,
not independent external scientific confirmation.

This is one aarch64 scientific execution lane. Repository policy checks on
two architectures do not execute these notes programs and cannot replace
an additional scientific run. No public computation-grade T is claimed.
