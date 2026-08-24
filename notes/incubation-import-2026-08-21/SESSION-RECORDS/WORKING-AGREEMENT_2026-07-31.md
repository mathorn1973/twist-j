# WORKING AGREEMENT. FOUR SEATS, TWO MODEL FAMILIES

NON-CANONICAL. An operating agreement, not science.

```text
DATE     2026-07-31
BASIS    Public Canon v28, main 3161cbc764f547c95a80c3bd5028acf71c2ef524
TESTED   everything in section 1 marked MEASURED was executed against the live
         machines from this session today. Everything marked STATED is your
         description of a seat I cannot reach and have not tested.
```

## 1. The fleet

```text
SEAT              model    machine                    arch     git             status
S1 Claude cloud   Claude   sandbox + JAS_2 relay      x86_64   push only       MEASURED
                                                      +aarch64  no issues/PRs
S2 Claude Work    Claude   local PC, WSL              x86_64   full            STATED
S3 ChatGPT Work   GPT      macOS arm64 leg                 arm64    full            STATED
S4 ChatGPT cloud  GPT      sandbox                    ?        bidirectional   STATED
```

### S1, measured in detail, because it is the seat with a hole

```text
JAS_2  gx10-e9fd, aarch64, Ubuntu 24.04.4 LTS, Python 3.12.3, 20 cores, 121 GB
       git identity already A. M. Thorn <thorn@twistj.com>
       ssh -T git@github.com -> "Hi mathorn1973! You've successfully
       authenticated"; push dry-run to a new branch SUCCEEDS
       reproduce/kernel/verify.py under the POLICY environment: exit 0, stderr
       0 bytes, stdout sha256 e49b20d0ac834b571c3b6061044bc8b73c9f337461404438f97c8bb1f276aaab,
       byte-identical to EXPECTED.txt, RESULT 15/15 ALL PASS
       33 of 38 probe run records read python: 3.12.3, so this is the platform
       the existing aarch64 legs already use
jam_write_file  byte-exact: 456 bytes both sides, sha256 e70dae93...a0b435e8a6,
       tested with non-ASCII, tabs, literal backslashes, raw strings,
       triple-quoted blocks and trailing whitespace
CAN    clone, fetch, read; run aarch64 formal legs; push branches; read issues
       (via JAS_2, unauthenticated API, 17 open right now)
CANNOT create issues, open PRs, merge. JAS_2 has no GitHub token, only an ssh
       key, and my own sandbox HTTP to github.com and api.github.com is gated
       at the proxy: even unauthenticated reads return "GitHub access to this
       repository is not enabled for this session."
```

**S1 can write code and history but cannot open the conversation around it.**
That is the one real hole and section 5 says how to fill it.

## 2. The fact that changes the plan: two model families

The three-session plan's sharpest falsifier was point 3: two sessions with the
same priors reading the same canon are not two people, so a long run of perfect
agreement between builder and breaker measures the shared prior rather than the
claim. With four seats across two model families, that stops being a hope.

**Rule: builder and breaker are never the same model family.**

This is already how the one real instance worked, and it is worth naming
because it was accidental. `PREREG-C-ENTROPY-MACKEY-OBSTRUCTION-4-N.md` records
its owner as a GPT-5.6 Thinking session; the M2 breaker was written by a Claude
session that had not seen the verifier. Builder GPT, breaker Claude. That is
the only session-separated breaker in the repository and it was already
cross-model.

### And it is necessary, not sufficient

The same instance is the evidence for the limit. Your adjudication of that
breaker found gate `B13` — the one reporting the common-cocycle premise
verified — "cannot fail if `B08` and `B10` pass": all four of its edge checks
were forced by earlier gates plus its own definitions. You confirmed it by
constructing a synthetic target with four deliberately different cocycles,
which passed anyway. Cross-model independence did not prevent a tautological
gate.

So one rule the fleet does not give us for free, and which this agreement adds:

```text
GATE DESIGN RULE
For every gate in a verifier or breaker, state in the preregistration what
input would make it FAIL. If you cannot name one, it is not a gate, it is a
restatement. Where practical, build that input and show the gate firing.
Gate count is not evidence.
```

That rule is written from a failure this seat committed, three hours after
writing "a verifier that can contain a tautology is a reminder that gate count
is not evidence" about someone else's work.

## 3. Git is the only shared bus

All four seats can read git. **Nothing else is common to all four.** The
claude.ai Project is invisible to S3 and S4; the JAM MCP fleet is reachable
only from S1; chat is per-seat.

```text
CONSEQUENCE
Every lock, claim, handoff and durable decision goes in git.
The Project is Claude-side working memory and nothing more. If a fact needs to
reach a GPT seat, it is not durable until it is committed.
```

The contract already says exactly this and it now has teeth: "The only handoff
is a committed `PROMO.md` package in public Git. An attachment, private
workspace, or chat summary is not a handoff and carries no currency."

I have been writing analysis to the Project all session. Under this agreement,
anything a GPT seat needs gets committed to `notes/` instead, or in addition.

## 4. Seat assignment

Cross-model pairing in both directions, so whoever builds, the other family
breaks.

```text
S1  Claude cloud + JAS_2      PUBLIC and AARCH64 RUNNER
    probes/, formal legs, pushes branches. Also breaker for GPT-built
    candidates. Strongest at long adversarial review: it ran four independent
    refutations of its own plan today and every one found real defects.
    Blocked from: issues, PRs, merges.

S2  Claude Work, local PC     PUBLIC BACKUP and ISSUE/PR HAND
    Full GitHub. Opens the lock issues and pull requests S1 cannot. x86_64
    local runs for development cross-checks (not a formal leg: the formal
    x86_64 leg is GitHub CI). Second Claude breaker seat.

S3  ChatGPT Work, macOS arm64 leg  BUILDER, heavy
    Full machine, full GitHub. Builds candidates and definitions. Its work is
    broken by S1 or S2.

S4  ChatGPT cloud             BUILDER, light and THEORY
    Sandbox with bidirectional git. Second GPT builder, and the natural home
    for pure theory that needs no machine.
```

Pairing rule, stated once:

```text
GPT builds  ->  Claude breaks     (S3 or S4 built, S1 or S2 breaks)
Claude builds -> GPT breaks       (S1 or S2 built, S3 or S4 breaks)
Never the same family on both sides of one candidate.
```

Collision rules are unchanged and are in the plan: 24 of 378 live pairs are
unsafe, they touch 14 rows, check the pair before two seats take two rows.

## 5. The hole in S1, and three ways to fill it

S1 cannot create the lock issue the contract requires before committing, nor
open the PR at the end.

```text
(a)  S2 does it. Simplest, needs no new convention, and S2 is a Claude seat so
     it can read the Project where S1 stages the issue text. Cost: S1 and S2
     must both be awake for S1 to start a probe.
(b)  You do it. Cost: one owner touch per probe, which is what the JAS_2 relay
     just removed.
(c)  A git-native lock. S1 pushes an annotated tag lock-<OBJECT_KEY>. Pushing
     an existing tag is rejected without --force, so first push wins and it is
     a true mutex visible to all four seats. Verified inert with respect to CI:
     the workflow's tag trigger is tags: [canon-v*], which lock-* does not
     match, and non-main branch pushes do not trigger it either.
     Cost: a new ref namespace in a strictly governed repo. That is a
     convention change and it is your call, not mine.
```

Recommend (a) as the default and (c) only if you want S1 to run unattended. Do
not pick (c) silently; it puts refs in the repo that POLICY never contemplated.

## 6. The loop

```text
1  BUILD      the builder seat authors PREREG + verifier, commits, pushes a
              branch. The preregistration must be complete enough that a
              breaker can derive what would falsify the claim WITHOUT reading
              the verifier. That is the contract's own test.
2  LOCK       claimed in a public issue before any commit, per AGENTS.md. For
              S1, see section 5.
3  BREAK      a seat of the other model family, which has not read the
              verifier, writes and freezes its breaker, then compares. It
              declares its forbidden-read list in the result, and applies the
              gate design rule of section 2 to its own gates.
4  RUN        formal aarch64 leg on JAS_2 under
              LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
              Development runs anywhere; only JAS_2 legs are formal.
5  PUSH       from the seat that owns the branch. Never main. Never a sealed
              probe. No machine nicknames anywhere in a public file: the fleet
              is private infrastructure and POLICY forbids it.
6  PR         opened by S2, S3 or by you. CI supplies the x86_64 leg. Two
              architectures, gate closed.
7  FOLD       one at a time, ever. Every fold rewrites canon/SHA256SUMS, so two
              in flight collide there whatever else they touch.
```

## 7. What I still need from you

```text
1  Which seat opens issues and PRs for S1: (a), (b) or (c) of section 5.
2  Confirmation that S2, S3 and S4 can genuinely push and open PRs. I have
   your description; I have tested none of them. If any cannot, the pairing in
   section 4 changes.
3  Whether the GPT seats can see notes/ in the repo well enough to consume a
   PROMO handoff, or whether they need the material in a specific shape.
4  The four rulings the M3 triage is waiting on: fold P-ENTROPY-LAW-REDUCTION-1;
   rule the QDD V28 HOLD; withdraw or re-audit the OBSERVER-WRITE-PORT
   retirement, dead at v28 by its own rejection test; repoint the NS-TILT
   falsifier, whose named instrument CMB-S4 was terminated in 2025.
```

## 8. Falsifier

```text
1  If a JAS_2 aarch64 leg does not reproduce byte-identically against the
   GitHub x86_64 leg on the first real probe, the platform match is weaker than
   Ubuntu 24.04 / Python 3.12.3 suggests and every formal leg is suspect.
   Check this on the first probe, before trusting the arrangement.
2  If jam_write_file ever produces a sha256 mismatch, hash-check every
   transfer, not just the first.
3  If a cross-model breaker still agrees with its builder on everything over
   several candidates, the independence is not coming from the model boundary
   and the pairing rule buys nothing. Watch for it; one clean disagreement is
   worth more than ten agreements.
4  If a gate written under the section 2 rule still turns out to be
   unfalsifiable, the rule is not strong enough and gates need a constructed
   failing input every time, not just where practical.
```

Point 3 is the live question. The one cross-model pair we have produced a
tautological gate on the most load-bearing premise, and the model boundary did
not catch it. You caught it. That is worth remembering when deciding how much
the pairing rule is actually buying.
