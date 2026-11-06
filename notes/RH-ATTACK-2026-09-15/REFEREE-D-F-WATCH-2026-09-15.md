# Referee report, lane D (F-watch), mathematics lens

```text
STATUS      NON-CANONICAL. Adversarial referee report on lane D. Status R.
DATE        2026-09-15
BASIS       Public Canon v86, tag canon-v86,
            content commit 56068ba4423a2ca38ce5760f1e34e82e2597f99f,
            CANON.md sha256 cfec639d2f952bc8d38f565b5ffc01851e53b39e764e10e95cfb6a1581b11b61
RH          unchanged: open program-level obligation, no status motion
REVIEWS     F-WATCH-2026-09-15.md, verify_f_watch.py, verify_f_watch.stdout
BUILDS ON   ZETA-RH-STATUS-2026-09-08.md sections 1 and 5;
            RH-PROGRAM-DEPENDENCE-PATCH-2026-09-08.md sections 3 and 7
```

## Falsifiers first

| referee claim | what kills it |
|---|---|
| RD1: the lane's gate, verifier and network statements reproduce | a rerun of `verify_f_watch.py` under `LC_ALL=C PYTHONHASHSEED=0` with different stdout or nonzero exit; or STATUS.md fields differing from the lane header; or an arXiv fetch succeeding from this session on 2026-09-15 |
| RD2: four of the five `CLAIM-ONLY` entries contradict step 4 of the lane's own procedure | a reading of section 3 step 4 under which an unconfirmed proof claim is STOP rather than NONE |
| RD3: checklist item 2 admits a non-falsifier (trivial zero) | a reading of item 2 as written that excludes a box around `s = -2` |
| RD4: the Gourdon `10^13` statement conflates zero count with height | a published Gourdon computation reaching height `10^13` |

## Verdict table

| claim | verdict | one line |
|---|---|---|
| D1-watch-state (R) | WEAKENED | negative finding reproduces (my own three searches, two README fetches, three egress tests: no record, arXiv/LMFDB still CONNECT 403); but "5 CLAIM-ONLY filed STOP" is wrong by the lane's own step 4 (only Liu is a disproof claim; the other four are proof claims, which step 4 files as NONE), Gourdon `10^13` is a zero count at height about `2.4*10^12`, below Platt-Trudgian, not a non-rigorous higher record, and the nine search results are not in the lane directory, so the verifier certifies the internal consistency of a hand-typed table, not the scan |
| D2-procedure (R, markdown only) | REFUTED as stated | step 2 item 2 lacks the strip condition `0 < Re(s) < 1`; the box `[-21/10, -19/10] x [-1/10, 1/10]` has rational endpoints, `1/2` outside, and contains exactly one zero of `zeta` (the trivial zero `s = -2`), so an item passing 1, 2, 4 is not a falsifier. Fix: require the box inside the strip, or require the zero to be of `xi` (not "or") |

## What I verified

1. Gate: STATUS.md reads ACTIVE, tag canon-v86, content commit and CANON.md
   sha256 as in the lane header; `sha256sum -c canon/SHA256SUMS` 5 of 5 OK;
   the content commit is an ancestor of the tag (the lane said it did not
   rerun the sums; I did).
2. Verifier: clean-environment rerun, stdout byte-identical to
   `verify_f_watch.stdout`, exit 0, `import sys` only, no floating point.
   Table tally: 10 fetch BLOCKED, 1 curl BLOCKED, 9 search reachable,
   3 fetch reachable; 23/12/11 correct.
3. Network: `export.arxiv.org`, `arxiv.org`, `www.lmfdb.org` all answered
   CONNECT 403 through the proxy at 20:38 UTC; proxy log shows the lane's
   19:54 rejection of `export.arxiv.org`.
4. READMEs: GPPVerify states a conditional flagship theorem
   `rh_of_weil_pairedForm_nonneg` with `True := trivial` stubs and one
   remaining axiom `exp_growth_not_tempered` (the lane's "no added axioms"
   condition 3 fails twice, not once); RiemannGaussian says "The proof is
   not complete" and exhibits no off-line zero.
5. Searches: no off-line zero record; Platt-Trudgian `3*10^12` (Bull. LMS
   2021) is still the last rigorous record indexed; 2609.02882 is by
   Lamzouri (Universite de Lorraine), submitted 2026-09-02, and credits the
   bound to a Claude run verified by Alpoge and Furman; the verifier's query
   string "Alpoge Furman 2609.02882" misattributes the identifier. One
   additional proof claim surfaced that the lane did not list (2603.05122,
   March 2026): NONE under step 4, no effect on the watch, but it shows the
   reachable search space was not exhausted.

## Verifier defects (bookkeeping, not zeta)

- Check 5 requires `n_claim >= 1`. A clean scan in which no claim surfaces
  would make the verifier exit 1. The check inverts its own meaning and
  should be `n_claim == number of rows filed STOP in the markdown`, or
  dropped (it is identical to check 4 by construction, as the comment says).
- Nothing in the verifier ties a row to the markdown's step-2 classification;
  the STOP filing is asserted in prose only.

## Counting rule

Not applicable: the lane proves nothing and says so. Its remark that the
GPPVerify conditional has the shape of the wall of ZETA-RH-STATUS-2026-09-08
section 4 is a reading, correctly not counted.

## What this does not do

- It does not verify any zero of `zeta(s)` and does not read arXiv.
- It does not change the lane's `R` status or any registry row; both lane
  claims stay `R` after correction.
- It does not claim the reachable search space was exhausted by my three
  extra queries either.
