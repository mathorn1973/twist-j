# AUDIT-PR441-CLOSE, P-DQRC-INTRINSIC-SELECTION-1, 2026-08-19

NON-CANONICAL. Independent close-out audit of pull request 441 at head
`561dcbf0b9c1fe6536ca73903b89939193331287`, by a session that does not own the
probe and did not write any file in it. Third and last of the audit series:

```text
claude/AUDIT-DQRC-BETA-INTERCEPT-SELECTION_2026-08-19.md          the science
claude/AUDIT-PIN-READBACK-P-DQRC-INTRINSIC-SELECTION-1_2026-08-19.md  the pin
claude/AUDIT-PR441-CLOSE_2026-08-19.md                            this file
```

---

## 1. Chain of custody: intact

```text
main                18f1180b6128c05705ebaa23733a10457aea3d3f   unmoved, Public Canon v54
pin                 2897cd968b3271d1c928891d6fea06a948119a03   ancestor of head   CONFIRMED
                    116cc85029d59c8491287fb7c36ec870131f3c8a   record the audit
head                561dcbf0b9c1fe6536ca73903b89939193331287   record the replay
author, all three   A. M. Thorn <thorn@twistj.com>
```

Linear history, three commits, the pin preserved as an ancestor. No amend, no
rebase, no squash, no force-push. The diff against `main` is exactly five files
in one probe directory, 921 insertions, zero deletions. `canon/`, `STATUS.md`,
`POLICY.md`, `AGENTS.md`, `tools/` and `.github/` are untouched.

The two pinned files are byte-identical at the head to their pinned blobs, and
`EXPECTED.txt` is byte-identical between `116cc85` and `561dcbf`:

```text
verify.py    226824dbc053acd8f41517f5f5103697509172519ea483055e2fd49711e7062f
PREREG.md    3e937835a35fecd5baf9089d256b667cd5acb2f6e02ddeb094738bab02c0beec
EXPECTED.txt 67eeba11fccc240d7da681357f72620adc741e854165b4b2657b51059bf5342e
```

---

## 2. The strongest single check in this whole lane

`EXPECTED.txt` in the repository has SHA-256

```text
67eeba11fccc240d7da681357f72620adc741e854165b4b2657b51059bf5342e
```

which is bit for bit the stdout this auditing session captured on a different
machine, from the pinned verifier, **before `EXPECTED.txt` existed**, and
recorded in
`claude/AUDIT-PIN-READBACK-P-DQRC-INTRINSIC-SELECTION-1_2026-08-19.md`
section 6. The prediction was published ahead of the artifact and the artifact
matched it.

Counting every reproduction of those 596 bytes:

```text
this session, pre-PR audit leg      x86_64    CPython 3.12.3    exit 0
owner local formal leg              x86_64    CPython 3.12.13   exit 0
required check, aarch64 job         aarch64   CPython 3.12.13   exit 0
required check, x86_64 job          x86_64    CPython 3.12.14   exit 0
this session, check_verifier replay x86_64    CPython 3.12.3    VERIFY PASS
```

Two architectures, three distinct CPython patch levels, five runs, one stdout
hash. The patch-level spread is itself useful evidence: it shows the frozen
`sys.version_info[:2] == (3, 12)` guard binds the minor version only, and that
patch drift does not disturb byte identity.

---

## 3. Machine checks re-run locally at the head

Every check the workflow runs, executed here at `561dcbf` under CPython 3.12:

```text
tools/check_policy.py                      exit 0   POLICY PASS
tools/check_preregistration.py             exit 0   PREREGISTRATION DRAFTS PASS drafts=6
tools/check_status_labels.py               exit 0   STATUS LABELS PASS
tools/check_canon.py                       exit 0   CANON PASS v54 claims=279
tools/check_ledger.py                      exit 0   LEDGER PASS claims=279 items=324
python -m unittest discover -s tools        exit 0   OK
tools/check_verifier.py --base 18f1180      exit 0
    RUN RECORD P-DQRC-INTRINSIC-SELECTION-1 TWO-ARCHITECTURE
    VERIFY PASS P-DQRC-INTRINSIC-SELECTION-1 226824db... 67eeba11...
```

`check_policy.py` previously failed on this branch for the missing artifacts.
That failure is now cleared. The `TWO-ARCHITECTURE` leg class is earned by the
recorded local `x86_64` leg against the recorded GitHub `aarch64` leg, exactly
as `classify_leg_pair` defines it.

The green state of workflow run `32297071981` itself is taken from the owner's
report; this session has no GitHub API access and verified the substance by
re-running every check locally instead.

---

## 4. The two findings from the pin audit are discharged

**F2, launcher normalization: resolved as recommended, by disclosure.**
`RUN.md` records `command: python3 probes/P-DQRC-INTRINSIC-SELECTION-1/verify.py`
for the checker and states the sealed invocation
`python3 -B ...` in a named `sealed_invocation` field plus a prose section, with
the correct reason: `-B` is an interpreter option, does not enter `sys.argv`,
leaves the frozen `len(sys.argv) == 1` gate untouched, and the checker sets
`PYTHONDONTWRITEBYTECODE=1` itself. The pin was not edited.

**F3, interpreter guard: recorded, not hidden.** `RUN.md` states the guard, the
current workflow pin, and that a future minor-version bump would produce an
integrity STOP that cannot be repaired in place and would need a fresh probe.
That is the honest handling of a fragility in a sealed artifact.

---

## 5. Two documentation nits. Neither is worth a commit.

**N1, a grep hazard.** `PREREG.md` section 7 says no result may say `PROMO`.
`RESULT.md` line 46 contains the token inside the negative clause
"No `PROMO-*` package is authorized." The meaning is the opposite of what the
rule forbids and no machine check objects. Recorded here so that a later reader
running a literal token scan does not read a silent rule break. Recommendation:
leave it. Amending a merged-ready record to satisfy a literal grep would be a
worse trade than the note.

**N2, an inherent self-reference limit.** `RUN.md` and `RESULT.md` cite workflow
run `32295818148` on head `116cc85`, because a commit cannot contain the
identifier of the run that tests it. The final green run `32297071981` tests
`561dcbf`. This is not stale evidence: `verify.py`, `PREREG.md` and
`EXPECTED.txt` are byte-identical across those two commits, verified above, so
the later run re-verified the same pinned script against the same expected
bytes. Only prose changed in `561dcbf`. Recommendation: leave it, and let the
issue 440 comment carry the final run identifier, which it does.

---

## 6. Scope: nothing overstated

`RESULT.md` uses only the allowed vocabulary and keeps every boundary:

```text
intercept finite audit       AUDIT-CONSISTENT
beta route                   REPARAMETERIZATION-ONLY
integrity                    no STOP
DQRC-H-COEFFICIENT-NONSELECTION [T]   controlling and unchanged
F-DQRC-ANTIFIT               neither narrowed nor lifted
QPAIR coefficient            read-only sentinel
silver frequency             not independent evidence
physical origin, pre or post step, clock, decoder, apparatus, event stream,
causal claim, CHSH derivation, layer lift                     none obtained
PROMO package                none authorized
Canon, Registry, Frontier, workflow, gate, other probes       unchanged
```

The universal statements stay with the written proofs in `PREREG.md`; the seven
bounded gates stay labelled as an audit of those proofs. The finite box result
is stated as the finite box result. Nothing in the record claims a status the
evidence does not carry.

---

## 7. Merge readiness

```text
main unmoved at 18f1180                                    CONFIRMED
merge is clean, no conflict                                CONFIRMED
diff touches exactly one probe directory                   CONFIRMED
no normative file changed, so no sealed integer-versioned  CONFIRMED
  fold is required by this pull request
POLICY merge mode: merge without squash or rebase          required
```

Nothing blocks the merge. This audit does not issue the merge instruction; the
owner does.

What the merge does: it lands a probe directory and its evidence. What it does
not do: it moves no registry row, changes no Canon, and earns no status. A
one-probe pull request with a two-architecture computational replay leaves the
candidate object `DQRC-SILVER-INTERCEPT-CLASSIFICATION` at `C` on the finite
audit. Its declared `T` ceiling depends on public review of the section 3 and
section 4 proofs, which is a separate action and a separate sealed content
change.

The open item in the lane is unchanged and is not this probe's job: derive the
saturation normalization, equivalently `S_inf = M_8` on the maximal locus, from
`J`, `Omega` or `U`. `F-DQRC-ANTIFIT` remains fired and archived.
