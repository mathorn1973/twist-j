# How to land C-LI2-PENTAGON-BALANCE-1 in the public repo

The session could not push. `gh` is absent, and the sandbox proxy refuses
`mathorn1973/twist-j` for both the GitHub API and git push, so the token in the
environment is not usable here. The branch is built, committed and verified
instead, and handed over as a bundle.

```
branch        notes/C-LI2-PENTAGON-BALANCE-1
base          b8d4d585820d04ebd008444661f3a71d6e24f423  (origin/main, unchanged)
commit        80bd13295142ff122c959bf15a902691f6190751
author        A. M. Thorn <thorn@twistj.com>
files         6 added under notes/C-LI2-PENTAGON-BALANCE-1/, 1636 insertions
normative     none touched. No canon/, no probes/, no reproduce/, no tools/.
```

## Option A, the bundle. One command from any clone.

```sh
git fetch /path/to/C-LI2-PENTAGON-BALANCE-1.bundle \
    'refs/heads/*:refs/heads/*'
git push origin notes/C-LI2-PENTAGON-BALANCE-1
```

Then open the pull request against `main`.

## Option B, the patch, if you would rather re-author the commit

```sh
git checkout -b notes/C-LI2-PENTAGON-BALANCE-1 origin/main
git am /path/to/C-LI2-PENTAGON-BALANCE-1.patch
git push origin notes/C-LI2-PENTAGON-BALANCE-1
```

## What was already checked, so the pull request should be green

Run locally against the staged tree at base `b8d4d58`:

```
tools/check_policy.py                       POLICY PASS
tools/check_canon.py                        CANON PASS v30 claims=216
tools/check_ledger.py                       LEDGER PASS claims=216 items=232
tools/check_status_labels.py                STATUS LABELS PASS
python -m unittest discover -s tools        99 tests, OK
tools/check_verifier.py  --base b8d4d58...  VERIFY NOT APPLICABLE
tools/check_reproduce.py --base b8d4d58...  REPRODUCE NOT APPLICABLE
```

The last two are correct and expected: `check_verifier.py` reproduces
`probes/` only, so a notes-only change is out of its scope by design. That is
also why this lane carries audit grade rather than probe grade, and the note
says so in its section 10 rather than leaving a reader to assume otherwise.

Bundle re-verified by fetching it into a fresh clone of `main`: it applies
cleanly, `SHA256SUMS` is 5 of 5 OK in place, and the gates pass there too.

Security audit of every staged file: no secrets, no keys, no `.env`, no private
hostnames, no machine nicknames, no private logs, no binaries. The two scripts
are pure ASCII and standard library only. The recorded environment fields are
neutral and public: Ubuntu 24.04, x86_64, Python 3.11.

## Suggested pull request body

> `notes: C-LI2-PENTAGON-BALANCE-1`
>
> NON-CANONICAL note, audit grade. Promotes nothing, edits no normative file,
> moves no frontier row.
>
> The golden modulus point `phi^-1 = |J|` is the unique positive point at which
> Abel's five-term relation degenerates to two terms. The collapse gives
> `2 L(phi^-1) = 3 L(phi^-2)` and the balance
> `sum_a Re Li_2(sigma_a(J)) = 2 L(|J|) = 3 L(J conj(J)) = (6/5) zeta(2)`
> against the registered wall sum.
>
> Merges the `C-LI2-MODULUS-POINTS-1` proposal from the 2026-07-31 recon into
> this lane. Landen's values are a corollary of the collapse rather than an
> import, so one lane replaces two.
>
> Records two fired falsifiers against the incoming submission instead of
> dropping them, and replaces both with a selector that is not shaped. States
> in section 4 that both legs of the balance lie a priori in `zeta(2)Q`, so the
> match is an equality of two rationals and numerical agreement is not evidence.
>
> Closes one open question negatively: the Rogers bridge supplies no modulus
> anchor, so `METRO-EDGE-SCALE` and `CURVATURE-OPERATOR-CANONICAL` are
> untouched.

## What is deliberately not in this branch

```
no registry row, no frontier edit, no Canon edit
no probes/ directory and no preregistration
C-LI2-RELATIVE-BLOCH-SEAM-2, the hypothesis half, stays in the project until
  its governing difficulty (section 6 of the note) is either met or fired
```

A public probe on this lane still needs its own six-field preregistration, a
pin on `probe/P-LI2-PENTAGON-BALANCE-1` before first execution, and two
architectures with byte-identical stdout.
