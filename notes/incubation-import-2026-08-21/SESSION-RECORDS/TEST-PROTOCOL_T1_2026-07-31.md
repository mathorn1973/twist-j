# TEST T1. FOUR SEATS, ONE SMALL CLAIM, BLIND BREAKERS

NON-CANONICAL. A pipeline test. It creates no canon claim and authorizes no
fold. It produces one real incubation candidate under `notes/` and nothing else.

```text
DATE       2026-07-31
BASIS      Public Canon v28, mathorn1973/twist-j main
           HEAD 3161cbc764f547c95a80c3bd5028acf71c2ef524 = tag canon-v28
CANDIDATE  C-KERNEL-PAIR-ORDERS-1
BRANCH     notes/C-KERNEL-PAIR-ORDERS-1
PATH       notes/C-KERNEL-PAIR-ORDERS-1/
```

## 0. What this test is for

Two things at once.

```text
1  Does the four-seat loop work end to end without the owner doing manual work:
   build -> lock -> two blind breaks -> aarch64 leg -> push -> PR.
2  Does the cross-model pairing rule buy anything. One breaker is a different
   model family from the builder, one is the same family. Both attack the same
   frozen preregistration blind. If the cross-model breaker finds something the
   same-model breaker misses, the rule earns its keep. If neither finds
   anything, or both find the same thing, that is also a result and it is
   recorded, not hidden.
```

## 1. The claim under test

The public Canon section 3 declares five involutive kernel generators on
`F_5^6` with coordinates `(p1, p4, p1p, p4p, q, r)`, all arithmetic mod 5:

```text
a  swap             (p1,p4,p1p,p4p,q,r) -> (p4,p1,p4p,p1p,q,r)
b  time inversion   x -> (-p1p, -p4p, -p1, -p4, -q, -r)
c  transport        piston -> b4(piston) + s_c + r u_c ;  q -> 1-q ;  r -> -r
d  mirror           x -> c_d - x
e  shifted mirror   x -> (c_d + v_e) - x

s_c = (2,1,2,1),  u_c = (0,1,0,-1),  c_d = (2,1,3,4,1,1),  v_e = (0,0,0,0,1,0)
b4 is the piston part of b.
Relations stated in canon: a^2 = b^2 = c^2 = d^2 = e^2 = id, and (bc)^5 = id.
```

The canon states the order of exactly one generator product, `bc`. **The claim
under test is the complete table: the exact order of `g_i g_j` for all ten
unordered pairs, and whether `ord(g_i g_j) = ord(g_j g_i)` in every case.**

Nothing else. No group order, no structure theorem, no physical reading, no
registry row. Layer L1.

Why this target: it is exact, finite, integer, computable in seconds, absent
from `canon/REGISTRY.tsv`, and it has two genuinely different computational
routes (permutation composition on 15625 points, or the affine linear-part
route `x -> M x + v` over `F_5`). That second fact is what makes a blind
breaker meaningful rather than a rerun.

## 2. The adjudicator's answer is already sealed

Seat S1 computed the full table before writing this protocol and has therefore
disqualified itself as a breaker. It is the adjudicator instead, and to stop it
from moving its own goalposts the answer is sealed by hash now:

```text
SHA-256 of the sealed answer file:
73a59c4a8a867d5448e63dd49c4e954767f7b4175c2a759b3c375fb611b6fc02

format of the sealed file, so it can be checked against later:
  ten lines, one per unordered pair in lexicographic order ab, ac, ad, ae,
  bc, bd, be, cd, ce, de
  each line exactly:  ord(XY)=<int> ord(YX)=<int>
  LF line endings, trailing newline, no other bytes
```

S1 reveals the file only after both breakers have pushed their frozen breaker
code. Anyone can then verify the hash matches what was published here.

## 3. Seats and roles

```text
S3  ChatGPT Work, macOS arm64 leg     BUILDER
S2  Claude Work, local PC        BREAKER 1, cross-model vs the builder
                                 also PUBLISHER: opens the issue and the PR
S4  ChatGPT cloud                BREAKER 2, same model family as the builder
S1  Claude cloud + JAS_2         ADJUDICATOR, aarch64 formal runner, coordinator
```

The two breakers must not talk to each other, must not read each other's code,
and must not read the builder's verifier before freezing their own.

## 4. Hard rules, all seats

```text
NEVER  push to main. Branch only.
NEVER  touch canon/, probes/, tools/, .github/, POLICY.md, AGENTS.md, STATUS.md.
NEVER  put a machine name, hostname, token, key or path from your local machine
       into any committed file. Public run records say only
       platform: <OS name and version>   architecture: <x86_64|aarch64>
       python: <version>.  Nothing else about the machine.
NEVER  use floating point in any assertion. int and fractions.Fraction only.
ALWAYS commit as:  A. M. Thorn <thorn@twistj.com>
ALWAYS Python standard library only. No network, no subprocess, no imports from
       the repository.
ALWAYS run verifiers and breakers with:
       LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
ALWAYS deterministic output: sort every collection before printing, print only
       explicit strings and integers, no repr, no paths, no timestamps.
STOP   if anything is unclear. Report the blocker; do not guess.
```

## 5. The gate design rule, and it is the point of the test

This rule exists because the one previous blind breaker in this repository, an
S1 product, shipped a gate that could not fail. The owner's adjudication proved
it by constructing a synthetic input the gate should have rejected and did not.

```text
For EVERY gate you write, state in your preregistration or result what input
would make that gate FAIL. If you cannot name one, it is not a gate, it is a
restatement of an earlier gate, and you must delete it or redesign it.
Where the failing input is cheap to construct, construct it and show the gate
firing on it.
Gate count is not evidence.
```

Both breakers are explicitly scored on this. A breaker that reports agreement
with an untested gate has not broken anything.

---

# 6. INSTRUCTION BLOCKS

Hand each block to its seat verbatim. Each is self-contained.

---

## 6.1 INSTRUCTION FOR S3, ChatGPT Work on macOS arm64 leg, BUILDER

```text
ROLE: BUILDER for incubation candidate C-KERNEL-PAIR-ORDERS-1.
You are one of four agents. Two other agents will independently try to break
your work without seeing your code. Write for that.

STEP 1. Clone and gate.
  git clone git@github.com:mathorn1973/twist-j.git   (or fetch if you have it)
  cd twist-j && git checkout main && git pull
  Confirm: git rev-parse HEAD == 3161cbc764f547c95a80c3bd5028acf71c2ef524
  Confirm: sha256sum -c canon/SHA256SUMS  -> 5 of 5 OK
  If either differs, STOP and report. Do not proceed on a moved head.

STEP 2. Read the source of truth.
  canon/CANON.md section 3 "The kernel and the census", the generator table.
  That table is the ONLY definition of a, b, c, d, e you may use. Do not import
  any generator implementation from anywhere else in the repository.

STEP 3. Create the branch and directory.
  git checkout -b notes/C-KERNEL-PAIR-ORDERS-1
  mkdir -p notes/C-KERNEL-PAIR-ORDERS-1

STEP 4. Freeze the preregistration FIRST, before writing any code.
  File: notes/C-KERNEL-PAIR-ORDERS-1/PREREG-C-KERNEL-PAIR-ORDERS-1.md
  It must contain the six fields and the action layer:
    1 exact claim
    2 exact domain and equality
    3 accepted inputs and dependencies
    4 method and systematics
    5 failure threshold and falsifiers
    6 action layer (L1)
  CRITICAL: field 5 must be written so that a breaker who has NOT seen your
  code can determine exactly what would falsify the claim, and can build its
  own attack from your text alone. Name every output field you will print and
  its exact format. If a breaker cannot derive the falsification condition from
  your preregistration, the preregistration is defective and the test fails on
  you, not on them.
  Do NOT put the numeric answers in the preregistration. Freeze the QUESTION
  and the FORMAT, not the result.
  Record: prereg_sha256 = sha256 of this file after you finish writing it.

STEP 5. Commit and push the preregistration ALONE.
  git add notes/C-KERNEL-PAIR-ORDERS-1/PREREG-C-KERNEL-PAIR-ORDERS-1.md
  git commit -m "notes: preregister C-KERNEL-PAIR-ORDERS-1"
  git push -u origin notes/C-KERNEL-PAIR-ORDERS-1
  This commit is the freeze point. The breakers branch from it.
  Report the commit sha and the prereg sha256.

STEP 6. Only now write the verifier.
  File: notes/C-KERNEL-PAIR-ORDERS-1/verify_kernel_pair_orders_1.py
  Stdlib only, exact integers, no float, deterministic sorted output.
  Compute the order of g_i g_j for all ten unordered pairs, and separately the
  order of g_j g_i, so the commutativity question is answered rather than
  assumed.
  Include gates that verify your own premises: that each generator is an
  involution on all 15625 states, and that the canon relation (bc)^5 = id
  reproduces. For EVERY gate, state in a comment what input would make it fail.
  Delete any gate you cannot make fail.
  Run it:
    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
      python3 notes/C-KERNEL-PAIR-ORDERS-1/verify_kernel_pair_orders_1.py \
      > notes/C-KERNEL-PAIR-ORDERS-1/verify_kernel_pair_orders_1.stdout.txt
  Record exit code, stderr byte count, and the sha256 of the code and stdout.

STEP 7. Commit and push the verifier and its stdout.
  Report: verifier sha256, stdout sha256, exit code, stderr bytes, and your
  platform/architecture/python in the neutral form of section 4.

STEP 8. STOP. Do not write a RESULT, do not write SHA256SUMS.txt, do not open
  a pull request. Wait. The breakers work next and the adjudicator closes it.
```

---

## 6.2 INSTRUCTION FOR S2, Claude Work on the local PC, BREAKER 1 and PUBLISHER

```text
You have TWO jobs. Do job A first, and do not start job B until told the
builder has pushed.

=== JOB A, PUBLISHER, do this immediately ===
Open a GitHub issue on mathorn1973/twist-j with this exact title:
  [INCUBATION LOCK] C-KERNEL-PAIR-ORDERS-1 - kernel generator pair orders
Body:
  OBJECT_KEY: notes/C-KERNEL-PAIR-ORDERS-1
  CLAIM_KEY: C-KERNEL-PAIR-ORDERS-1
  OWNER_SESSION: builder seat, macOS arm64 leg
  BREAKERS: two, independent, blind
  SCOPE: exact order of g_i g_j for all ten unordered pairs of the five public
    kernel involutions, and whether ord(g_i g_j) = ord(g_j g_i). Layer L1.
  EXCLUDED: group order, structure theorem, registry row, any physical reading.
  NON-CANONICAL. This lock creates no claim.
Report the issue number.
Then check: no other open issue or branch claims this object. If one does,
STOP and report a collision.

=== JOB B, BREAKER 1, cross-model ===
You are breaking work built by a DIFFERENT model family. Independence is the
entire point.

FORBIDDEN, absolutely, until your own breaker file is committed and pushed:
  notes/C-KERNEL-PAIR-ORDERS-1/verify_kernel_pair_orders_1.py
  notes/C-KERNEL-PAIR-ORDERS-1/verify_kernel_pair_orders_1.stdout.txt
  any other breaker's code or output
  any private explanation from the builder
You MAY read: the frozen PREREG file, and canon/CANON.md section 3.
Enforce it mechanically: check out the PREREG freeze commit, not the branch
tip, so the verifier is not in your working tree at all.
  git fetch origin
  git checkout -b break/C-KERNEL-PAIR-ORDERS-1-r1 <PREREG_FREEZE_COMMIT>

STEP 1. From the preregistration text alone, write down what would falsify the
  claim. If you cannot, do not guess: report
  BLIND-BREAKER-UNDERSPECIFIED and list exactly which types, domains, equality
  rules or output fields are missing. Disclose NO attack strategy in that
  report. That outcome is a legitimate result and it indicts the builder.

STEP 2. Write your breaker with an INDEPENDENT method. The builder is likely to
  compose permutations on 15625 states. You must not do the same thing in
  different words. Use a structurally different route, for example the affine
  representation: each generator is x -> M x + v over F_5, so work with the
  6x6 matrices and translation vectors and derive the order of a product from
  the linear part's order and the induced translation, rather than by iterating
  a permutation. If you choose another route, say why it is independent.
  File: notes/C-KERNEL-PAIR-ORDERS-1/break_kernel_pair_orders_1_r1.py
  Stdlib only, exact integers, no float, deterministic sorted output.

STEP 3. Apply the gate design rule to yourself. For every gate you write, state
  what input would make it fail, and where cheap, construct that input and show
  the gate firing. A gate that cannot fail must be deleted. This is scored.

STEP 4. Run it under
    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
  Save stdout to break_kernel_pair_orders_1_r1.stdout.txt

STEP 5. FREEZE: commit and push both files BEFORE you look at anything the
  builder wrote. The push is the freeze.
  Report: your breaker sha256, stdout sha256, exit code, stderr bytes,
  platform/architecture/python in the neutral form, and the commit sha.

STEP 6. Only now read the builder's verifier and stdout, and write
  notes/C-KERNEL-PAIR-ORDERS-1/BREAK-r1.md containing:
    your forbidden-read list, declared as a signed process assertion
    your independent route, and why it is independent
    your gate table: gate id, what it tests, what input makes it FAIL, whether
      you constructed that input
    value-by-value comparison with the builder's output
    every disagreement, preserved. Never adjust either side to reconcile.
  Push it. Do NOT open the pull request yet.
```

---

## 6.3 INSTRUCTION FOR S4, ChatGPT cloud, BREAKER 2

```text
ROLE: BREAKER 2 for incubation candidate C-KERNEL-PAIR-ORDERS-1.
You are the SAME model family as the builder. That is deliberate: this test
measures whether same-family breaking is weaker than cross-family breaking.
Do your best work; the comparison is the experiment, not a judgment of you.

FORBIDDEN, absolutely, until your own breaker file is committed and pushed:
  notes/C-KERNEL-PAIR-ORDERS-1/verify_kernel_pair_orders_1.py
  notes/C-KERNEL-PAIR-ORDERS-1/verify_kernel_pair_orders_1.stdout.txt
  the other breaker's code or output, at any path ending _r1
  any private explanation from the builder
You MAY read: the frozen PREREG file, and canon/CANON.md section 3.
Enforce it mechanically: check out the PREREG freeze commit, not the branch tip.
  git fetch origin
  git checkout -b break/C-KERNEL-PAIR-ORDERS-1-r2 <PREREG_FREEZE_COMMIT>

Then follow exactly the same steps as the other breaker, with r2 in place of r1:
  1  derive the falsification condition from the preregistration alone; if you
     cannot, report BLIND-BREAKER-UNDERSPECIFIED with the missing types only
  2  write an INDEPENDENT method, not a restatement of the obvious one, and say
     why it is independent
  3  apply the gate design rule: for every gate, name the input that makes it
     FAIL, and construct it where cheap. Delete gates that cannot fail.
  4  run under LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
  5  FREEZE by pushing break_kernel_pair_orders_1_r2.py and its stdout BEFORE
     reading anything the builder wrote
  6  then write BREAK-r2.md with the same six sections
Report the same fields: sha256 of code and stdout, exit code, stderr bytes,
platform/architecture/python, commit sha.
Do NOT open a pull request.
```

---

## 6.4 WHAT S1 DOES, for the record

```text
1  Holds the sealed answer, hash published in section 2, reveals it only after
   both breakers have pushed.
2  Runs the formal aarch64 leg of the builder's verifier and both breakers on
   JAS_2 under the POLICY environment, and records whether every stdout is
   byte-identical to what each seat pushed. A mismatch here is a portability
   defect and is a first-class finding.
3  Adjudicates: compares builder, breaker 1, breaker 2 and the sealed answer.
4  Writes notes/C-KERNEL-PAIR-ORDERS-1/RESULT.md and SHA256SUMS.txt and pushes.
5  Reports the verdict to the owner. S2 then opens the pull request.
```

## 7. Pass and fail

```text
PIPELINE PASSES if all of:
  the builder froze a preregistration a breaker could work from
  both breakers froze before reading the verifier, provably: their freeze
    commits have the verifier nowhere in their ancestry
  all three stdouts reproduce byte-identically on JAS_2 aarch64
  the numeric table agrees across builder, both breakers, and the sealed answer
  no machine name, token or local path reached any committed file
  no seat touched main, canon/, probes/, tools/ or a workflow

PIPELINE FAILS, and this is useful, if any of:
  a breaker had to read the verifier to know what to attack
    -> the preregistration was underspecified, fix the template
  the stdouts differ across architectures
    -> a portability defect in someone's output discipline
  the numeric results disagree
    -> a real scientific disagreement, preserve both sides, do not reconcile
  a breaker's gates cannot fail
    -> the gate design rule is not being applied and the breaker is decorative

THE PAIRING EXPERIMENT reports, separately from pass or fail:
  did breaker 1 (cross-model) and breaker 2 (same-model) find different things
  did either find a defect in the builder's gates
  did either ship a gate that cannot fail
```

## 8. Cleanup

If the pipeline fails, the branch stays as the record and is not merged. Nothing
here touches `main` until the owner merges the pull request, and merging is
optional: the value of T1 is the process record, not the table.

## 9. Falsifier for this test

```text
This test is badly designed if the claim turns out to be so easy that both
breakers reproduce it trivially and no gate discipline is exercised. If that
happens, T1 has tested the plumbing and not the science, which is a partial
result: the loop is proven, the pairing rule is not, and T2 needs a harder
target with a genuine chance of disagreement.
```
