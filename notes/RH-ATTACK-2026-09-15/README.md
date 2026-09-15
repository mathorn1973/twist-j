# RH attack session, 2026-09-15

```text
STATUS         NON-CANONICAL. Incubation record of one attack session on the
               RH line. No registry row moves, no probe is opened, no lock is
               claimed, no F is recorded. RH remains an open program-level
               obligation with the falsifier declared on 2026-09-08.
DATE           2026-09-15
BASIS          Public Canon v86, tag canon-v86,
               content commit 56068ba4423a2ca38ce5760f1e34e82e2597f99f,
               canon/CANON.md sha256
               cfec639d2f952bc8d38f565b5ffc01851e53b39e764e10e95cfb6a1581b11b61,
               626540 bytes; public main d008270c9c979f457f73087e17672b1db85ee6ad
GATE           STATUS.md ACTIVE; tag and content commit ancestors of main;
               sha256sum -c canon/SHA256SUMS 5 of 5 OK; check_canon, check_ledger,
               check_policy PASS on that head
LAYER          NOT_APPLICABLE (analytic number theory; no L1-L6 lift)
PREVIOUS PAGE  twistj-handoff ZETA-RH-STATUS-2026-09-08.md (Public Canon v81)
COUNTING       notes/RH-ONE-WALL-CROSSREF_2026-08-17.md applies to every file here
```

## 1. What this directory is

The owner asked on 2026-09-15 where the RH program stands and for another
attack. This directory is the attack record. It was produced by four
independent lanes, each with an exact standard-library verifier, each then
refereed by two adversarial reviewers (a mathematics lens and an
evidence-and-code lens), repaired by the lane owner with every accepted
correction and every rejected objection listed in a review record, and
finally audited by a completeness critic. The referee reports and referee
scripts are carried here so that the review is auditable, not only asserted.

The lanes were pointed at the two newest public targets of the line, both
on unmerged branches, and at the F-watch the 2026-09-08 page asks for:

- PR #979, `notes/c-rh-mobius-mean-channel-n` at
  `0ecc82a234176eba10e4c8d7a7069aa8524eff2c` (object lock #978), the Mobius
  mean-channel note, whose next proof target is its (41).
- PR #933, `claude/dreamy-pascal-liep2q` at
  `820098a87a7245fa911945a57897f1dac5162113`, the review of the owner's
  binary-routing note (Nyman-Beurling sequence route).
- PR #856, `codex/rh-correlation-moment-note-20260906` at
  `3dd6d937e5d7700e1e34199b2d6923830f183038`, the signed-moment note, whose
  reduced target is its (M37), identical to (A71) of its analytic appendix.

Every equation number cited in the lane files binds to those three heads;
the branches are non-normative and may still be amended.

## 2. Files

| file | role |
|---|---|
| `ATTACK-NB-PROJECTION.md` | lane A: exact projection census for the binary-routing route and the mean-channel debt of #979 |
| `verify_nb_projection.py`, `.stdout.txt` | lane A verifier, 20 of 20 PASS, 143 s, exact `int`/`Fraction` |
| `REFEREE-NB-PROJECTION.md`, `referee_nb_projection.py`, `.stdout.txt`, `referee_nb_projection_spotcheck.py`, `.stdout.txt` | lane A referee records (mathematics lens; evidence lens spot-check) |
| `ATTACK-EPSILON-GUARD.md` | lane B: strength guard for the fixed-epsilon target (41) of #979 |
| `verify_epsilon_guard.py`, `.stdout.txt` | lane B verifier, 31 of 31 PASS, about 4 s |
| `REFEREE-MATH-EPSILON-GUARD.md`, `REFEREE-CODE-EPSILON-GUARD.md`, `referee_math_tests.py`, `referee_code_mutations.py` | lane B referee records |
| `ATTACK-M37-STRENGTH.md` | lane C: strength reading of the reduced target (M37) of #856 |
| `verify_m37_strength.py`, `.stdout.txt` | lane C verifier, 17 of 17 PASS, about 0.1 s |
| `REFEREE-C-M37-STRENGTH.md`, `referee_m37_strength.py`, `.stdout.txt` | lane C referee record and script |
| `F-WATCH-2026-09-15.md` | lane D: the external-claim scan and the F-watch procedure |
| `verify_f_watch.py`, `verify_f_watch.stdout` | lane D verifier, 7 of 7 PASS; records the watch state, asserts nothing about zeta |
| `REFEREE-D-F-WATCH-2026-09-15.md`, `REFEREE-LANE-D-EVIDENCE-CODE-2026-09-15.md`, `rerun.stdout.txt` | lane D referee records; `rerun.stdout.txt` is the evidence referee's rerun of the pre-repair lane D verifier, kept because the lane's review record names it |
| `SHA256SUMS` | hashes of every file above |

All four verifiers were re-run by the session coordinator from a clean shell
(`env -i PATH=/usr/bin:/bin LC_ALL=C PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1
python3 <verifier>`) inside this directory after assembly: exit 0 and stdout
byte-identical to the carried files for all four (lane A writes three timing
lines to stderr; the others write nothing). One architecture only
(x86_64, Python 3.11); nothing here has a two-architecture replay, so no
computation here can be filed as `C`.

## 3. Verdicts, one line each

Status labels are the lanes' own NON-CANONICAL labels after repair:
candidate-T (complete written proof, finite pieces exactly verified),
candidate-C (exact computation at a stated finite scope), F-route (a
precisely scoped proof route is ruled out; never a falsification of RH),
R (report), O (open), HEURISTIC (so marked at the step).

**Lane A, the Nyman-Beurling census.** The exact binary inner product of
periodic sequences (the record's theorem, re-implemented) gives the Gram
matrix of `r_2 .. r_72` and the exact squared distances `d_K(x)^2` for the
targets `1`, `a_1 = A_2`, `a_2 = A_4`, `a_3 = A_8` and `2 <= K <= 72`
(candidate-C). Calibration reproduces every number of the record it
touches (`c_2 = 160/251`, `c_3 = 105/251`, `d_3^2 = 52/251`,
`d_4^2 = 95/766`). The Mobius note's identity (1) and its identities
(12)-(14) receive written proofs (candidate-T); its bound (3) is checked to
`K = 4096` (candidate-C, finite). Lemma D (candidate-T): the note's Cesaro
averages lie in `span{r_2 .. r_{K_{J-1}}}`, so their error is at least the
optimal distance, and `||Y_{Q,J}||^2 >= 2 J^2 d_{K_{J-1}}(A_Q)^2 -
||D_{Q,J}||^2/4`. Reading: the note's closure-strength `CJ` mean-channel
bound implies an `O(1/log K)` rate for `d_K(a_j)^2` and is at least as
strong as that rate; a rate is not membership. Diagnostic: `d_K(1)^2 log K`
stays in `[0.0969, 0.1004]` for `32 <= K <= 72`; the note's sharp cuts do
not converge at `K_h <= 64` (errors `0.0678, 0.0686, 0.0865, 0.0806`),
the averages do (`0.0678, 0.0471, 0.0344, 0.0271`), with efficiency
against the optimum falling towards `1.2`. The mean-channel debt for one
`Q = 2^j` is `a_j in V` with a rate: the twisted Nyman-Beurling problem of
the #933 review, not a numerical seam.

**Lane B, the epsilon guard.** Target (41) of #979 is identified exactly:
`sup_N L_N(eps) < infinity` iff `||F_eps||_eps < infinity`, with
`sum_n (2n+3)|a_n|^2 = ||F_eps||_eps^2` exactly (candidate-T; the note's
(36) holds with its constant only when `g_eps` is read on `(0, infinity)`
with the trivial tail). Guard (candidate-T): that membership puts the
Mellin transform `c_eps/(s-1) - zeta(s)/(s zeta(s+eps))` into the Hardy
space `H^2(Re s > 1/2 - eps/2)`, so the quotient has no pole on
`Re s >= 1/2 - eps/2` except `s = 1`; hence every zero `rho` of `zeta` with
`Re rho >= 1/2 + eps/2` has an epsilon-shadow zero at `rho - eps` of at
least the same multiplicity, and an epsilon-chain of zeros ending in the
strip `|Re s - 1/2| <= eps/2`. Converse with margin (candidate-T, imports
declared): a zero-free half-plane `Re w >= 1/2 + eps/2 - eta` implies (41).
Reading: (41) at fixed `eps` sits, up to the shadow caveat and an `eta` of
margin, at the quasi-Riemann hypothesis with abscissa `1/2 + eps/2`
(`5/8` at `eps = 1/4`, `17/32` at `eps = 1/16`); (41) along any `eps_j -> 0`
is RH; RH implies (41) for every `eps`. No zero-free half-plane strictly
inside the critical strip is known, so a direct unconditional proof of (41)
at any fixed `eps < 1` would be the first. The note's "RH approximation
program" is therefore a zero-free half-plane ladder. Diagnostic: `L_N(eps)`
extended to `N = 64` (`0.611344` at `eps = 1/4`, `0.876432` at
`eps = 1/16`); finite partial sums decide nothing.

**Lane C, the (M37) strength reading.** The expected conclusion of the
session brief (that (M37) with `kappa` near `1` is at quasi-GRH strength
for `zeta_F`) did not survive its own verification; the lane records the
correction. Series structure (candidate-T): the full support series
`F^{(k)}(s) = G_k(s)/(zeta(s) L(s, chi_5))` with `G_k` an absolutely
convergent zero-free Euler product on `Re s > 1/2`, the O5 divisor
dictionary with one more local factor. Ceiling (candidate-T, conditional,
hypothesis displayed): the Lindelof hypothesis for the single function
`L(s, chi_5)` implies (M37) uniformly in `k <= T`, because the unweighted
version of (M37) is already the record's unconditional (A60) and the whole
gap `2 nu_sigma` of (M32) is the pointwise weight loss of the exponent-pair
bound (A41) against Lindelof at the two abscissae `1 - sigma` and
`2 sigma`. Floor (F-route, conditional on a residue bound): the single
Perron pole term of a hypothetical zero of `zeta_F` stays inside the (M37)
budget below `1 - nu_sigma/(2 - kappa)`, about `0.79`; the threshold
`beta*(kappa) = (3 - 2 kappa)/(4 - 2 kappa)` of the brief is an artefact
of confusing a supremum with an `L^2` mean. Multi-pole reading
(HEURISTIC): at best zero-density strength, and its domination lemma is the
least eigenvalue of a Cauchy/Pick Gram matrix of Lorentzians, the same wall
as the T2 Weyl detection threshold. Placement: no zero-location content of
(M37) is known; its inputs are classical `L(s, chi_5)` information outside
the fence of `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]`, which stays STOP.

**Lane D, the F-watch.** Of twelve reachable items, none is a record of an
off-critical zero. One disproof claim (Liu, arXiv 2404.06306, April 2024,
no zero exhibited per a review page that was itself unreachable) is filed
STOP, not F. Two Lean repositories reachable: one conditional (RH from a
finite Weil-pairing positivity hypothesis, open steps as `True := trivial`
stubs and one analytic axiom), one that says its proof is not complete. One
September 2026 T-direction item (a proportion-of-zeros result). The last
rigorous verified height found is unchanged (Platt-Trudgian,
`3 * 10^12`). arXiv egress is blocked on three hosts from this
environment, so the listing itself is unscanned; the page carries the
one-page watch procedure (closed finding vocabulary, what an exact
enclosure must contain, STOP on a claim, F only on a record) and a verifier
that certifies the consistency of the hand-typed table, not the scan.

## 4. Counting

Per the counting rule, this session adds readings, not theorems. Lanes A
and B are the second and third readings at the Nyman-Beurling / Mellin-
quotient level, first booked by the #933 review on 2026-09-10; both are
one obligation, "`1/zeta` controlled to the right of the line", in the
sequence-space and the Mellin-quotient dress, and must never be presented
as two theorems. Lane C is a further reading at the capacity/Gram level.
Lane D is not a wall result. Zero genuinely new structure: no new level,
carrier, or positive construction. The bridge row, the lambda row and RH
are exactly where the 2026-09-08 page left them.

Two residual wordings flagged by the critic were fixed before assembly:
the lane A verdict row V10r no longer says "equivalent up to constants"
(the rate-to-`CJ` direction is open, lane A section 9.4 item 2), and the
lane C single-pole exclusion is stated with its residue hypothesis in every
clause. Lanes B and C reach opposite-looking verdicts on two `L^2`
statements left of `Re s = 1/2`; they do not contradict: lane B's object is
the full Mellin transform of a global function (a supremum over all `N`),
lane C's is a truncated Dirichlet polynomial with a `T^{-1}`-normalised
mean over `[T, 2T]` (a finite prefix). That pair is section 4-5 of the
2026-09-08 page in two dresses: a finite prefix carries no zero content, a
global object encodes a half-plane.

## 5. What this session did not do

- Nothing on the Weil / T1' Euler side (the 2026-08-20 records
  RH-T1-WEIGHT-THEOREM, RH-T1-GLOBAL-TRANSFORM-ATTACK), nothing on the
  Hankel HE-2 armed route, nothing on the Widder depth audit: unchanged.
- The definitional lane for the bridge row (freeze the admissible transfer
  class, domain, norm, error) was not attempted; it remains the standing
  prerequisite for typing either closure.
- The O5 cluster decision and the owner-declaration fold were not touched;
  at v86 there is still no `RH-PROGRAM-DEPENDENCE` row and the branch
  `notes/rh-program-dependence-2026-09-08` (`ffff3452`) still has no pull
  request, so the F-watch's STOP/F actions name a row that does not exist.
- The Mobius note's secondary finite target, its certificate (29) at
  `Q = 8`, `U = 64`, was not attempted; it is the one finite, non-RH-strength
  target in that note and the natural next candidate-C.
- No two-architecture replay, no external reference re-verified (Bagchi,
  Burnol, Baez-Duarte, Lee-Leong are used only as the record cites them).

## 6. Smallest next steps

Ordered; each tied to a registry decision condition or an open PR.

1. Fold the owner declaration: open the pull request from
   `notes/rh-program-dependence-2026-09-08` with the three owner decisions
   taken, add the `RH-PROGRAM-DEPENDENCE [H]` row, and adopt section 3 of
   `F-WATCH-2026-09-15.md` as the row's watch procedure.
2. #856: merge as NON-CANONICAL with the lane C annotation on (M37)
   (implied by `LH(chi_5)`; unweighted version is the record's (A60); no
   known zero-location consequence; inputs outside the bridge fence). The
   bridge row stays STOP by its own decision condition.
3. #979: before merge, add lane B's reading to the note's no-go ledger
   ((41) at fixed `eps` is a zero-free half-plane modulo shadows and
   margin), lane A's convention note and the proofs of (12)-(14); the owner
   decides whether "continue from (41)" remains the handoff.
4. #933 plus lane A: merge as NON-CANONICAL; if the `K <= 72` census is to
   become a `C` row, run the aarch64 replay under a new probe identifier;
   attempt certificate (29) of the Mobius note as the next finite target.
5. Open the definitional lane for the bridge row and decide the O5 cluster;
   rebase #907 and the RH status page to v86.

## 7. Integrity record

Gate run on 2026-09-15 against a fresh clone of `origin/main` at
`d008270c`: `STATUS.md` fields as in the header; `git merge-base
--is-ancestor` true for the content commit `56068ba4` and for the peeled
tag `d008270c`; `sha256sum -c canon/SHA256SUMS` OK for all five files;
`canon/CANON.md` 626540 bytes; `check_canon.py` (`CANON PASS v86
claims=414`), `check_ledger.py`, `check_policy.py` PASS. The lane verifiers
use only the Python standard library with exact `int` and `Fraction`
arithmetic in every gated assertion; floating point appears only in blocks
labelled DIAGNOSTIC that assert nothing. Every number in section 3 is
traceable to a lane file by basename. No Canon file was edited.
