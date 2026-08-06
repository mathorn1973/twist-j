# RESULT. P-TM-SYM2-SPECTRAL-COHERENCE-1

Route: POSITIVE. Local formal leg complete, exit zero, 19 certificates green,
empty stderr. The cross-architecture gate is pending and is recorded in the
section at the end of this file.

Scope: the frozen v16 S_TM carrier at its public pins, the complete 48-member
selector class, layer L5. This file records the probe outcome only. It moves
no registry row, no frontier row, and no Canon text.

## 1. Preregistered clauses and their verdicts

```text
C1  PASS  all 1128 unordered selector pairs admit a similarity witness
          L_t = D P^-1 L_s P D with P in {id, NPERM} and D a diagonal sign
          matrix                                              (CERT 19)
C2  PASS  one exact characteristic polynomial across all 48 selectors
                                                              (CERT 14)
C3  PASS  no frozen-battery functional separates the two epsilon_read
          classes                              (CERT 15, 16, 17, 18)
C4  PASS  exponent-one realizability 60, intersection with W 12, linear
          count 60                                     (CERT 08, 09, 10)
C5  PASS  two-graph split 10 and 10, Galois flips every pairwise dot sign
                                                          (CERT 11, 12)
```

No clause fired. No FIRED-OR-STOP line occurs in the transcript.

## 2. The exact spectrum

The transcript prints the characteristic polynomial coefficients in the
Q(sqrt5) basis a + b sqrt5:

```text
c_6 = 1
c_5 = 0
c_4 = -6 - 2 sqrt5
c_3 = 0
c_2 = 21/2 + 9/2 sqrt5
c_1 = 0
c_0 = 0
```

With phi = (1 + sqrt5)/2 these are exactly c_4 = -4 phi^2 and c_2 = 3 phi^4,
so for every selector s in the class

```text
det(xI - L_s) = x^2 (x^2 - phi^2) (x^2 - 3 phi^2),
spectrum      = {0, 0, +phi, -phi, +sqrt3 phi, -sqrt3 phi}.
```

The witness search records a first-found split of 552 pairs settled by the
identity window permutation and 576 pairs requiring the complement
permutation N, in the deterministic enumeration order of the verifier. The
split is reported as observed data, not as a claim.

## 3. What this establishes

Every invariant of the signed transfer operator under signed window
permutation similarity is constant on the whole 48-member class. In
particular the spectrum carries no witness of the residual reading
orientation epsilon_read = chi_Q chi_F, and neither does any member of the
frozen battery. The residual bit is not signed-transfer-spectral data.

Representative nonuniqueness and invariant nonuniqueness are therefore
distinct here: the class admits no canonical selector, yet the operator
spectrum is single-valued across it.

## 4. Scope firewall

This result proves no L5-to-L6 bridge, no physical measure, no Born reading,
and no uniqueness beyond the stated scope. It is mathematics on a frozen
carrier and is not empirical validation.

TM-SYM2-PHYSICAL-MEASURE remains an open obligation with its falsifier
unchanged. This probe registers an independent L5 statement that a future
bridge may cite; it supplies a lower bound on what such a bridge may demand,
namely that its coherence requirement is not weaker than signed transfer
similarity, and a stronger requirement must state what distinguishing
information it adds.

Coherence under pairings other than the registered sigma_line was observed
outside this probe and is out of scope here. Any classification over other
pairings is a separate lane.

No Canon, registry, frontier, gate, status, or other probe is edited by this
outcome. Such treatment is a later separately reviewed fold.

## 5. Cross-architecture gate

```text
architecture_gate: PASS
```

The required check reran the identical pinned verifier on both runners at
pull-request time. Both legs exited zero with empty stderr and stdout
byte-identical to the committed EXPECTED.txt.

```text
pull request:   279
workflow:       policy, event pull_request
workflow run:   31077427253
head:           b76e7e6be4add20388257f717dbf69a94fff508d
base:           bff109aa0272cb61e33df60682f2e30358dc9765
python:         3.12 as pinned by the workflow

job 92538416302   architecture-aarch64   runner label ubuntu-24.04-arm
                  2026-08-06T06:29:02Z to 2026-08-06T06:29:20Z   success
job 92538416559   architecture-x86_64    runner label ubuntu-latest
                  2026-08-06T06:29:02Z to 2026-08-06T06:29:18Z   success
job 92538472052   check                  TWO-ARCHITECTURE CHECK PASS
                  2026-08-06T06:29:22Z to 2026-08-06T06:29:28Z   success
```

Reproduction ran as `tools/check_verifier.py --base bff109aa` on each
architecture. That tool executes the pinned verifier from the repository root
and compares its transcript with EXPECTED.txt; a byte mismatch, a nonzero
exit, or nonempty stderr fails the step. Both architecture jobs passed it. In
the check job the failure branch was skipped, which is exactly the condition
that every architecture job succeeded.

The publication job was skipped. It is gated on a tag push or a release event
and is not part of the pull-request gate. Its skip is not a gate result.

Three executions now agree byte for byte on the transcript with sha256
410679552c329e420f7e7196e039c04e57708d5c9ff0975b260a2352c070b255: the local
aarch64 formal leg recorded in RUN.md and the two runner legs above. RUN.md
records the local leg as it stood at execution time and is not amended; this
section is the gate verdict of record.

The evidence above establishes reproduction, not status. Any registry,
frontier, or Canon movement is a later separately reviewed fold.
