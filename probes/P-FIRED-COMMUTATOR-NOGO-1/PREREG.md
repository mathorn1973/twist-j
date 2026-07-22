# PREREG: P-FIRED-COMMUTATOR-NOGO-1

**FORMAL PREREGISTRATION PIN.** No formal execution of this probe verifier
occurred before this preregistration commit.

```text
ISSUE:         none; no GitHub CLI credential is available to this session.
               The probe is authorized by the owner's direct instruction of
               2026-07-21. Collision check at BASE_COMMIT: no
               probe/P-FIRED-COMMUTATOR-NOGO-1 branch, no probes/ directory,
               no registry row, and no notes lane names this claim. The
               owner may attach a public issue number at pull-request time.
BASE_COMMIT:   3f6500afe1ea71fb60f7c7d81da9a2d4d05d2ba3
LAYER:         L1 state only; no lift to L2-L6 is claimed
TARGET:        new claim candidate FIRED-COMMUTATOR-NOGO at T (proposed):
               the derived subgroup of the fired algebra <b, d, e> is
               exactly the 25 fiber translations, with zero piston
               component; the fired dynamics is spatially abelian.
STATUS_ACTION: none in this probe; any registry, frontier, or Canon change
               is a later sealed fold decision.
```

## Frozen fields

```text
EQUATION     On X = (Z/5Z)^6 with the five public census involutions
             a, b, c, d, e (byte-matching probes/P-CENSUS-REPLAY-1),
             piston = the first four coordinates, fiber = (q, t):

             (i)    on the sheet z5 in {1, 4} the selector
                    i = (z5 + 2 t) mod 5 takes only values {1, 3, 4},
                    so only b, d, e ever fire (a, c silent);
             (ii)   [d,e] = T_(0,0,0,0,3,0), [b,d] = T_(0,0,0,0,3,3),
                    [b,e] = T_(0,0,0,0,1,3), all with zero piston part;
             (iii)  the linear parts of b, d, e are B, -I, -I and
                    {I, -I, B, -B} is an abelian Klein group of
                    exponent 2, so every group commutator in <b, d, e>
                    is a pure translation;
             (iv)   the three pair-commutator vectors generate the full
                    25-element fiber plane, and conjugation by b, d, e
                    preserves the fiber plane, so the derived subgroup
                    D(<b, d, e>) is exactly the fiber translation plane:
                    the fired dynamics is spatially abelian, and
                    piston-block noncommutativity cannot arise from the
                    fired steps;
             (v)    negative control: [a, c] is not a translation.

             Proof audited by the gates: (iii) forces linear part I for
             every commutator; the word sweep confirms zero piston on all
             ordered pairs of words up to length 3; the normal closure of
             the generator pair commutators under Klein conjugation stays
             in the fiber plane and already fills it.

CODE         verify.py, frozen at this pin.
             SHA-256 d4303d6eca517c4c2afa922e691d31d0aab63987b5a137c0c51ca6f8d5340e28
             9237 bytes. Python standard library only; exact integer
             arithmetic; deterministic; no files written; no floats.

CARRIER      X = (Z/5Z)^6, 15625 states, coordinates (p1, p4, p1p, p4p,
             q, t); the five public involutions of
             probes/P-CENSUS-REPLAY-1 with S_VEC = (2,1,2,1),
             U_VEC = (0,1,0,-1), C_D = (2,1,3,4,1,1),
             V_E = (0,0,0,0,1,0); z5(x) = sum of coordinates mod 5;
             selector i = (z5 + 2 t) mod 5.

SYSTEMATICS  All gates are exhaustive on the declared finite carrier or on
             the declared finite word set (length up to 3); the general
             statement rests on the elementary group-theoretic proof in
             EQUATION, which the gates audit ingredient by ingredient.
             Group-theoretic claim only: no curvature operator value,
             spectrum, or canonical selection is computed
             (CURVATURE-OPERATOR-CANONICAL stays O and is not addressed);
             no physical reading is claimed. Disclosure: the identities in
             EQUATION were found in exploratory incubation work outside
             this repository (single-platform x86_64, no canon weight,
             archived in the project incubation lane as
             REZ_CASU_SYNTEZA_AUDIT_2026-07-21.md and
             verify_tm_cut_synthesis.py). The present verifier is a fresh
             file, statically compiled only, first executed after this pin.

THRESHOLD    PASS only if the post-pin Linux aarch64 command exits 0,
             writes empty stderr, and prints RESULT 10/10 ALL PASS; the
             GitHub x86_64 required check at pull-request time must
             reproduce the same verifier hash and byte-identical stdout.
             FAIL-STOP on any hash, byte, gate, exit-code, or stderr
             mismatch. Preserve a failed formal result; do not move
             thresholds or silently rerun under a changed pin.
```

## Falsifiers

```text
F1  a commutator in the word sweep with nonzero piston component or a
    non-identity linear part
F2  any of the three pinned pair-commutator vectors wrong at any state
F3  the additive closure of the three commutator vectors is not the full
    25-element fiber plane
F4  the selector fires a or c on the sheet z5 in {1, 4}
F5  [a, c] is a translation (the silent control collapses; the
    fired-set restriction clause would be unsupported as scoped)
F6  the two-architecture transcripts differ at the same verifier hash
```

## Formal command and environment

From a clean checkout of the full immutable pin, repository root:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 probes/P-FIRED-COMMUTATOR-NOGO-1/verify.py
```

The owner record uses neutral public fields (platform, architecture, Python
version, hashes, byte counts, exit code, elapsed time). No machine nickname
or private path.

## Scope firewall

- No Canon, registry, frontier, evidence, or hash file is changed in this
  probe.
- No claim is promoted here. The proposed row FIRED-COMMUTATOR-NOGO enters
  only through a later sealed fold, at the status the evidence then earns.
- CURVATURE-HISTORICAL-TRACE, CURVATURE-HISTORICAL-GAUSS-SPLIT,
  CURVATURE-OPERATOR-CANONICAL, and KERNEL-MACRO-READING are untouched and
  complementary; nothing here selects a curvature operator or computes its
  value.
- No physical reading, no continuum statement, no L2 to L6 lift.

## Pin checklist

1. Confirm no collision (branch, probes/ directory, registry, notes lanes).
2. Commit and push only this PREREG.md and verify.py as the immutable pin
   on branch probe/P-FIRED-COMMUTATOR-NOGO-1.
3. Do not amend, rebase, squash, or force-push the pin.
4. Only then execute the owner aarch64 gate and add EXPECTED.txt, RUN.md,
   and RESULT.md in later commits on the same branch.
