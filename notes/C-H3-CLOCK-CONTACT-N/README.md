# PROMO-C-H3-CLOCK-CONTACT-N

NON-CANONICAL / NO AUTHORITY. L1. Candidate package under claim
[#2137](https://github.com/mathorn1973/twist-j/issues/2137).
Public Canon v117 base: 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.

The selected prepared H3 clock bank is present before the first measurement,
writes the second predicate at absolute203, and retains a fixed material
column-sum record for 32 subsequent ticks on all 25 ordered inputs while
the old material record survives. The full worker-reset target remains
20/25. All finite results are candidate-C; the explicit conditional
two-scale synthesis proof has candidate-T scope only. No promotion occurs.

## Read and review

| File | Role |
|---|---|
| RESULT.md | Complete findings, negative results, selected stock and limits |
| THEOREM.md | Conditional exact contact-synthesis proof |
| PREREG.md | Original frozen A-D scope |
| PREREG-E.md | Separately frozen parity/retention extension |
| RUN.md | Custody, source/output hashes and actual replay coverage |
| A_RESULT.md | Exact earlier fixed-response obstruction |
| response.py / RESPONSE.txt | Earlier89/90 repair response |
| verify.py / EXPECTED.txt | Original preinstalled first-contact constructions |
| break.py / BREAK.txt | Blind same-session alternate for B/C |
| retention.py / E.txt | All eight parity/retention cases |
| break_retention.py / BREAK-E.txt | Blind same-session alternate for E |

## Reproduce

Use the repository root. Standard-library Python 3.11 or 3.12 is sufficient
for the recorded environments. These notes invoke no formal public gate.
The unchanged native source is hash-checked at runtime. The alternate
engine uses its own cyclic-five ring and actual update.

```sh
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 notes/C-H3-CLOCK-CONTACT-N/response.py > /tmp/h3-contact-response.txt
cmp /tmp/h3-contact-response.txt notes/C-H3-CLOCK-CONTACT-N/RESPONSE.txt
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 notes/C-H3-CLOCK-CONTACT-N/verify.py > /tmp/h3-contact-primary.txt
cmp /tmp/h3-contact-primary.txt notes/C-H3-CLOCK-CONTACT-N/EXPECTED.txt
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 notes/C-H3-CLOCK-CONTACT-N/break.py > /tmp/h3-contact-alternate.txt
cmp /tmp/h3-contact-alternate.txt notes/C-H3-CLOCK-CONTACT-N/BREAK.txt
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 notes/C-H3-CLOCK-CONTACT-N/retention.py > /tmp/h3-contact-retention.txt
cmp /tmp/h3-contact-retention.txt notes/C-H3-CLOCK-CONTACT-N/E.txt
PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 python3 notes/C-H3-CLOCK-CONTACT-N/break_retention.py > /tmp/h3-contact-retention-alternate.txt
cmp /tmp/h3-contact-retention-alternate.txt notes/C-H3-CLOCK-CONTACT-N/BREAK-E.txt
```

The proposed promotion unit is this scoped package, preserving its old
odd-impulse reversals and both old/new repair failures. Any promotion
requires the separate public fold and its required review and checks.
