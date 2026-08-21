# AUDIT: pre-push review of the P-PAULI-CARRIER-CAR-1 pin package. 2026-08-06

```
SESSION   pauli-recon-2026-08-06 (same session as the incubation recon)
STATUS    NON-CANONICAL AUDIT. Review before push. No authority. This session
          has read the incubation and the pin; it is NOT the independent
          breaker the probe will eventually need.
INPUT     PPAULICARRIERCAR1pin.zip: MANUAL_PIN.md, ISSUE_BODY.md, BRANCH.txt,
          COMMIT_MESSAGE.txt, LOCAL_DRAFT_SHA256SUMS, DRY_RUN_NOT_EVIDENCE.txt,
          probes/P-PAULI-CARRIER-CAR-1/{PREREG.md, verify.py}
          LOCAL_DRAFT_SHA256SUMS 3/3 OK against the delivered files.
```

## 1. Repo state at audit time

Fresh fetch of mathorn1973/twist-j: head unchanged since the morning gate,
main = 11a059c, STATE ACTIVE, Public Canon v38, same tag, content commit,
Canon hash and byte count as declared in ISSUE_BODY.md. No probe/P-PAULI-*
branch, no probes/P-PAULI-* directory, no PAULI row in REGISTRY.tsv, no
PAULI candidate under notes/. Open GitHub issues are not checkable from this
session (no API auth); the MANUAL_PIN procedure has the owner recheck
issues at claim time, which covers that hole.

## 2. Reproduction of the dry run (labeled, not evidence)

```
command   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
          python3 verify.py     (from the probe directory; the pin will run
          from repository root, the script is path-independent)
result    exit 0, stdout 686 bytes, stderr 0 bytes, wall 6.2 s
stdout    sha256 8dfcef98ab26c5f58b51982ca0e79fc5b262faf7c73e48e615686213bece09a7
          BYTE-IDENTICAL to the authoring session's declared dry hash
```

Two different machines now produce identical bytes. Informal but strong
determinism signal. Runtime is far under every limit.

## 3. Independent mathematical check (third code path)

The new content beyond the incubation is Theorem B, the complete
parity-string classification: for c_j(A) = (prod_k Z_k^A_jk) q_j on
(C^2)^(tensor N), zero diagonal, CAR holds iff A_ij + A_ji = 1 for every
pair, i.e. A is an orientation of the complete graph, 2^(N choose 2) of
them, every one of total string weight N choose 2, A = 0 dead for N >= 2.

Checked by hand (sign transport: the mixed relation carries the same
(-1)^(A_ij + A_ji) as both same-type relations; the on-site relations hold
because the diagonal is zero) and by a THIRD implementation, dense
Kronecker matrices over Z, independent of both the package's bit-state
action and the incubation recon:

```
N=3 complete class (64 matrices): predicate equivalence exact, 0 mismatches,
    8 admitted = 2^3
N=3 CYCLIC tournament (0->1->2->0): CAR HOLDS. The class is orientations,
    not orderings; non-Jordan-Wigner members are real. This is the sharpest
    new fact and it survives.
N=4: JW passes, one symmetric pair fails, a 4-tournament passes.
```

Theorems A, D, E and the shell identities were already independently
confirmed in the incubation recon (Reynolds over all 120 group elements,
characters, opposite-convention Jordan-Wigner, phi-power shell audit).
Theorem C (parity grading) is standard and its audit in G6 is sound.

## 4. Discipline check against POLICY and the A3-FCC precedent

```
six prereg fields        PRESENT (equation: frozen carrier + theorems A-E;
                         code: accepted verify.py; carrier: H_N, A-class,
                         K, marked 2I; systematics: declared audit ranges;
                         failure threshold: VIABLE/NONVIABLE + F1-F10;
                         action layer: L4 spectral algebra only)
falsifiers               F1-F10 concrete and exact; STOP list explicit
result exposure          disclosed twice (ISSUE_BODY and PREREG section 8),
                         probe self-labeled RESULT-EXPOSED confirmatory
scope fences             QUANT-SUBSTRATE, QUADRATIC-DECODER-DATA, D_matter,
                         L5/L6, parastatistics, kernel-point 2I action all
                         explicitly out; conclusion text stays inside scope
delta vs PROMO plan      legitimate (pre-pin): gates G4-G6 are new (the
                         classification and grading), the incubation's
                         walk-causality leg (old A7) is NOT carried, and
                         the conclusion correctly does not mention it
verifier                 stdlib only, integers + Fraction, no float, no
                         writes, no stderr, deterministic output, 6 s
self-containment         S_n, C_n definitions carried by the registered
                         BOOST-READING-SPLIT scope; marked generators
                         displayed; no unfrozen formula found
commit hygiene           pin = exactly PREREG.md + verify.py; author
                         identity correct; EXPECTED/RUN/RESULT post-run
```

## 5. Findings (both fixable before push, neither touches the mathematics)

```
FINDING 1, STOP TRAP, fix before push.
  PREREG section 6 declares "exact class counts and parity weights through
  N=12". The verifier enumerates every orientation and its weight only for
  N <= 6 (2^15 masks); for N in 7..12 it audits the count FORMULA and the
  Jordan-Wigner witness only. The probe's own STOP list contains
  "incomplete enumeration in the declared finite audit". As pinned, a
  hostile reader can fire that STOP against the bullet. One-sentence
  reword closes it, e.g.:
    "- exhaustive weight audit of every orientation through N=6;
     - Jordan-Wigner witness, weight, and CAR through N=8;
     - count formulas and the Jordan-Wigner weight through N=12;"
  This is exactly the A3-FCC failure mode (prereg text promising more than
  the frozen artifacts deliver), caught this time before the pin.

FINDING 2, disclosure completeness, fix at claim time.
  The verifier was fully executed twice before any public pin (dry runs,
  disclosed in DRY_RUN_NOT_EVIDENCE.txt with the stdout hash). POLICY
  allows compilation and static checks before the pin, not formal gates;
  a full execution is more than a static check. The honest resolution is
  the one the package already chose, declared confirmatory mode, BUT the
  DRY_RUN file is excluded from the pin commit by design, so the pre-pin
  executions would leave NO public trace. Paste the DRY_RUN_NOT_EVIDENCE
  content (including the dry stdout hash) into the public issue at claim
  time, next to the result-exposure disclosure. Then the record is
  complete: everything that happened is public, and the pin's remaining
  function, immutability plus the two-architecture byte gate, is intact.

MINOR
  ISSUE_BODY "Exact boundaries" cites the closed-negative kernel-point 2I
  route without naming the row; naming COLOR-DYNAMICAL-COLOR [F] in the
  issue would make the fence audit-proof. Optional.
```

## 6. Verdict

```
mathematics      SOUND. Third-path confirmation including the cyclic
                 tournament case; the classification is genuinely about
                 orientations, not Jordan-Wigner orderings.
discipline       SOUND after Finding 1 (one sentence in PREREG section 6)
                 and with Finding 2 executed at claim time.
recommendation   FIX, THEN PUSH. After the pin: remote readback, first
                 formal run, EXPECTED/RUN/RESULT, PR with the two
                 architecture jobs. The independent breaker for the fold
                 should be a session that has read NEITHER the incubation
                 NOR this audit.
```

## 7. What this adds to the decoder hunt (map note)

The probe, if folded, deletes one more freedom from any future D_matter:
an electron write into the qubit carrier cannot be strictly local; inside
the complete monomial parity class it must carry an orientation datum, one
bit per mode pair, total weight N choose 2, with Jordan-Wigner merely one
witness among 2^(N choose 2). The decoder search is not a search for a
mechanism; it is the deletion of the space where the mechanism could hide.
This is one deletion, at theorem grade, and QUADRATIC-DECODER-DATA [O]
stays exactly as open as it was.
