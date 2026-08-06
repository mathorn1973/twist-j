# FOLD-V39-LAMBDA-COCYCLE

**NON-CANONICAL.** Fold proposal. One document a fold can consume without
reading anything else. This file carries no authority, earns no status, and
changes nothing in `canon/`.

```text
CANDIDATES   P-LAMBDA-COCYCLE-ANGLES-1  issue 284, pull request 286,
                                        pin d7ad9d9973a7859e030b42e572b7f64a1f926b2d
             P-LAMBDA-COCYCLE-ANGLES-2  issue 287, pull request 288,
                                        pin ac496a684d715cbfca69b199abfb19dcc8000c20
TARGET       Public Canon v39: two new T rows, one amendment to the live
             LAMBDA-COCYCLE-ANGLES [H] row, one queue change.
BASE         Public Canon v38, content commit
             64639e922c774990884963a708d7efb86b9dc1a7,
             canon/CANON.md sha256
             f4bb9d7700f08c9609068e3e3eac4b60259c8f1ae3eab49eaa92832bc591c703,
             182096 bytes.
BLOCKER      Both probe pull requests must merge into main BEFORE this fold
             starts. See "Ordering constraint" below; it is not a preference.
```

## Ordering constraint

This fold cannot be prepared as a single branch alongside the probes, for two
independent mechanical reasons.

1. `tools/check_ledger.py` requires every `PUBLIC_PROBE` evidence row to point
   at a directory that exists in the tree, containing all five probe files, and
   to carry the exact `bundle-manifest-sha256-v1` digest of that directory. A
   fold branch that does not already contain both probe directories fails.
2. `tools/check_verifier.py` fails any pull request whose diff names more than
   one probe directory. A branch carrying both probes plus the Canon change is
   therefore rejected.

So the order is forced:

```text
1. merge pull request 286   (probes/P-LAMBDA-COCYCLE-ANGLES-1)
2. merge pull request 288   (probes/P-LAMBDA-COCYCLE-ANGLES-2)
3. branch canon/v39-lambda-cocycle from the resulting main
4. apply this fold, then the release-form commit
```

A pull request that changes any file under `canon/` widens both changed-path
checks to every public probe and every minimal reproduction in every
architecture job, so step 4 reruns the whole tree. Budget for that.

## What is being folded

Two probes, both with a passed two-architecture gate, both of which leave
`LAMBDA-COCYCLE-ANGLES [H]` unfired.

`P-LAMBDA-COCYCLE-ANGLES-1` proves that on the critical line the Cayley factor
is exactly the Cayley-angle unit,

```text
1 - 1/rho = e^(i alpha_gamma),   alpha_gamma = 2 arctan(1/(2 gamma)),
1/rho^2   = -(1 - 1/rho)/(1/4 + gamma^2),
```

and hence, inside the declared class,

```text
M - t_n = sum_(gamma>0) 4 sin^2(n alpha_gamma / 2)/(1/4 + gamma^2),
M       = 2 lambda_1 = sum_(gamma>0) 2/(1/4 + gamma^2).
```

Every summand is nonnegative and bounded, so `0 <= M - t_n <= 2 M` holds
automatically once the class is nonempty. No finite Li profile can fire the row
at any range or precision, and a tail separation localizes to one ordinate in an
explicit finite window.

`P-LAMBDA-COCYCLE-ANGLES-2` proves that the registered grid is not an assumption
about zeta but the point spectrum of the operator. `J` is a unit, so `U_J`
permutes the character basis with every orbit finite; an orbit of exact level
`k` has size `ord_(lambda^k)(J)`; and

```text
ord_(lambda^(4m))(J) = 4 . 5^m,
```

so the registered index sequence `n_A = 4 . 5^A` is exactly the orbit size at
level `4A`. A cycle of length `d` contributes the `d`-th roots of unity, so the
eigenvalue angle set is exactly `2 pi (1/4) Z[1/5]`. The converse construction
then gives the equivalence.

Net effect on the frontier: the row's three registered falsifier branches — one
angle exclusion, one second-difference limit, one all-vector class contradiction
— are proved to be **one branch**, and the row reduces to a single arithmetic
statement about the zeros of zeta.

## Rows to add

### `canon/REGISTRY.tsv`

Two rows, tab separated, in the file's existing sort position.

```text
LAMBDA-COCYCLE-BRANCH-COLLAPSE	T	on the critical line the Cayley factor is exactly the unit 1 - 1/rho = e^(i alpha_gamma) with alpha_gamma = 2 arctan(1/(2 gamma)) and 1/rho^2 = -(1 - 1/rho)/(1/4 + gamma^2); inside the declared cocycle-vector class M - t_n = sum_(gamma>0) 4 sin^2(n alpha_gamma / 2)/(1/4 + gamma^2) with M = 2 lambda_1 = sum_(gamma>0) 2/(1/4 + gamma^2), so 0 <= M - t_n <= 2 M holds automatically, no finite set of exact Li values or interval enclosures can contradict the class, and a tail separation localizes to one ordinate in an explicit finite window	18. The frontier	probes/P-LAMBDA-COCYCLE-ANGLES-1	fires if the Cayley unit identity, the reciprocal-square collapse, the residual identity, or the finite-window localization is exhibited to fail for an admissible ordinate
LAMBDA-COCYCLE-GRID-EQUIVALENCE	T	multiplication by J = 1 + zeta_5^2 permutes the character basis of L^2(O_lambda,Haar) with every orbit finite, an orbit of exact level k has size ord_(lambda^k)(J), and ord_(lambda^(4m))(J) = 4 . 5^m so the registered index sequence n_A = 4 . 5^A is exactly the orbit size at level 4A; U_J therefore has pure point spectrum with eigenvalue angle set exactly 2 pi (1/4) Z[1/5], and a cocycle vector exists if and only if RH holds and every Cayley angle 2 arctan(1/(2 gamma)) lies in that grid, equivalently every nontrivial zero is rho = 1/(1 - xi) with xi^(4 . 5^a) = 1	18. The frontier	probes/P-LAMBDA-COCYCLE-ANGLES-2	fires if an orbit size outside {4 . 5^a} is exhibited, if a grid angle is exhibited that is not an eigenvalue angle of U_J, or if the converse construction or its two-initial-value induction is exhibited to fail
```

Scope hashes of those two scope strings, for the `HISTORY.tsv` rows:

```text
LAMBDA-COCYCLE-BRANCH-COLLAPSE   60bd8424c6cc6608211ac0c5d690a6ee38b57639a5cbf5ceb26dbed648059a05
LAMBDA-COCYCLE-GRID-EQUIVALENCE  9d4025a4d520070e6b532f4eca26d76783d3ce875e854117e6277eb3742ddd74
```

### `canon/EVIDENCE.tsv`

```text
LAMBDA-COCYCLE-BRANCH-COLLAPSE	EV-LAMBDA-COCYCLE-BRANCH-COLLAPSE	PUBLIC_PROBE	probes/P-LAMBDA-COCYCLE-ANGLES-1	6fa30375944a0c5ad2ed84705191552442dc1024b4248046a1382f5a0caf7710	bundle-manifest-sha256-v1	two-architecture
LAMBDA-COCYCLE-GRID-EQUIVALENCE	EV-LAMBDA-COCYCLE-GRID-EQUIVALENCE	PUBLIC_PROBE	probes/P-LAMBDA-COCYCLE-ANGLES-2	d721d7dea495f447f136a30fc310d99fee27b5fa3af7515c62fb662d120486f2	bundle-manifest-sha256-v1	two-architecture
```

**The two bundle digests above must be recomputed at fold time.** They were
computed from the probe trees as pushed, and any review change to a probe file
changes them. Recompute with the repository's own `bundle_sha256`, which sorts
by repository-relative path and skips `__pycache__`, `*.pyc`, and `RUNS`.

### `canon/NORMATIVE.tsv`

```text
LAMBDA-COCYCLE-BRANCH-COLLAPSE	THEOREM	LAMBDA-COCYCLE-BRANCH-COLLAPSE	T	L6		canon/CANON.md::LAMBDA-COCYCLE-BRANCH-COLLAPSE [T]
LAMBDA-COCYCLE-GRID-EQUIVALENCE	THEOREM	LAMBDA-COCYCLE-GRID-EQUIVALENCE	T	L6		canon/CANON.md::LAMBDA-COCYCLE-GRID-EQUIVALENCE [T]
```

### `canon/DEPENDENCIES.tsv`

```text
LAMBDA-COCYCLE-BRANCH-COLLAPSE	LAMBDA-COCYCLE-ANGLES	BOUNDED_BY	the collapse is proved inside the declared cocycle-vector class of that hypothesis and states nothing outside it
LAMBDA-COCYCLE-GRID-EQUIVALENCE	LAMBDA-COCYCLE-BRANCH-COLLAPSE	REQUIRES	the converse uses the residual identity and the second-difference agreement proved by the collapse
LAMBDA-COCYCLE-ANGLES	LAMBDA-COCYCLE-GRID-EQUIVALENCE	BOUNDED_BY	the hypothesis is now known to be equivalent to RH together with the grid condition, which bounds every route that can fire it
```

### `canon/HISTORY.tsv`

Two `DECLARE` events and one `SCOPE_CHANGE`, at the next event sequence for
release `canon-v39`.

```text
CANON39-DECLARE-LAMBDA-COCYCLE-BRANCH-COLLAPSE	1	YYYY-MM-DD	canon-v39	LAMBDA-COCYCLE-BRANCH-COLLAPSE	DECLARE	-	T	60bd8424c6cc6608211ac0c5d690a6ee38b57639a5cbf5ceb26dbed648059a05	EV-LAMBDA-COCYCLE-BRANCH-COLLAPSE	probes/P-LAMBDA-COCYCLE-ANGLES-1	<bundle digest>	Public Canon v39 registers the exact Cayley-unit identity and the nonnegative residual form proved by the public two-architecture probe, which retires the finite Li profile as an attack on the wall and collapses the second-difference falsifier branch into the angle branch
CANON39-DECLARE-LAMBDA-COCYCLE-GRID-EQUIVALENCE	2	YYYY-MM-DD	canon-v39	LAMBDA-COCYCLE-GRID-EQUIVALENCE	DECLARE	-	T	9d4025a4d520070e6b532f4eca26d76783d3ce875e854117e6277eb3742ddd74	EV-LAMBDA-COCYCLE-GRID-EQUIVALENCE	probes/P-LAMBDA-COCYCLE-ANGLES-2	<bundle digest>	Public Canon v39 registers the orbit structure of J on the lambda-adic character group, identifying the registered grid as the point spectrum of U_J and the index sequence n_A as its orbit size, and upgrading the cocycle-vector hypothesis to an equivalence
CANON39-SCOPE-LAMBDA-COCYCLE-ANGLES	3	YYYY-MM-DD	canon-v39	LAMBDA-COCYCLE-ANGLES	SCOPE_CHANGE	H	H	ad67abe65c1d0857dc73639b0573198aa25c3aaecc8155f709d9309738a65924	EV-LAMBDA-COCYCLE-ANGLES	probes/P-R2-LAMBDA-HAAR-1	811c41d0d1b1ec00fa1d114385c7915bd648dfea8c0e773ca41c292768156bdc	Public Canon v39 records that the three registered falsifier branches of the hypothesis are proved to coincide, so the row is stated as an equivalence with an arithmetic condition on the zeros; the status is unchanged and the row is not fired
```

The scope hash on the third row is the hash of the **amended** scope text below.
If the owner declines the amendment, drop that row and leave the scope untouched.

## Amendment proposed for `LAMBDA-COCYCLE-ANGLES [H]`

This is the one judgement call in the fold and it is deliberately isolated so it
can be refused without affecting the two `T` rows.

Status stays `H`. The row is not fired and is not retired. Proposed new scope:

```text
the compact lambda-adic boundary route remains open only in the cocycle-vector
form: there exists v in L^2(O_lambda,Haar) with
||sum_(k=0)^(n-1) U_J^k v||^2 = lambda_n for every n >= 1; by
LAMBDA-COCYCLE-GRID-EQUIVALENCE such a v exists if and only if RH holds and
every Cayley angle 2 arctan(1/(2 gamma)) lies in 2 pi (1/4) Z[1/5],
equivalently every nontrivial zero is rho = 1/(1 - xi) for a 4 . 5^a-th root of
unity xi
```

`sha256 = ad67abe65c1d0857dc73639b0573198aa25c3aaecc8155f709d9309738a65924`

Proposed new falsifier:

```text
fires through the Cayley-angle branch: an exact proof that one ordinate Cayley
angle 2 arctan(1/(2 gamma)) lies outside 2 pi (1/4) Z[1/5], equivalently that
one nontrivial zero is not 1/(1 - xi) for a 4 . 5^a-th root of unity xi; the
second-difference branch and the all-vector class-contradiction branch are
proved to coincide with that branch by LAMBDA-COCYCLE-BRANCH-COLLAPSE and
LAMBDA-COCYCLE-GRID-EQUIVALENCE, and no finite Li profile can fire it
```

**Read this before accepting it.** The wording narrows three listed routes to
one. That is a record of a proved equivalence, not a reduction in
falsifiability: every route that fired the old text still fires the new one, and
the two `T` rows are the proof. But it is still a live-hypothesis scope change,
so it belongs to the owner and not to a probe. Refusing it costs nothing except
that the frontier keeps advertising three routes that are known to be the same.

## Queue change proposed for `canon/FRONTIER_PROGRAMS.tsv`

```text
current   LAMBDA-COCYCLE-ANGLES	ENRICHMENT	ROOT	READY	ENRICHMENT
proposed  LAMBDA-COCYCLE-ANGLES	ENRICHMENT	ROOT	BLOCKED	ENRICHMENT
```

Rationale: `READY` advertises actionable work. After these two probes the only
route that can fire the row needs an arithmetic or transcendence exclusion of one
zeta ordinate from an explicit dense countable set, which is an external open
problem. `BLOCKED` is the honest label and is already used elsewhere in the
frontier, for example by `NEUTRON-DELTA-EM [O]`. This is the only live
`ENRICHMENT` row, so the program will have no `READY` member afterwards;
confirm that is acceptable before folding.

## Canon text

`canon/CANON.md` section 18 currently carries one `LAMBDA-COCYCLE-ANGLES [H]`
paragraph. The fold should replace it with the amended statement above and add
two short theorem paragraphs, one per new row, in the section's existing style.
Suggested content, to be written in the Canon's own voice rather than pasted:

- the Cayley factor is exactly `e^(i alpha_gamma)` on the critical line, giving
  the nonnegative residual form and the collapse of the second-difference
  branch, with the explicit statement that no finite Li profile can fire the
  row;
- the orbit structure of `J`, the identification of `n_A = 4 . 5^A` as the orbit
  size at level `4A`, the point spectrum of `U_J`, and the resulting
  equivalence;
- the restatement of the wall in arithmetic terms: the hypothesis holds exactly
  when every nontrivial zero is `1/(1 - xi)` for a `4 . 5^a`-th root of unity.

## Generated files

Do not hand-edit these. Run the repository's own generator after the TSV rows
are in place:

```sh
python3 tools/generate_canon_views.py
```

It regenerates `canon/FRONTIER.md`, `canon/STATUS_COUNTS.tsv`, the `CORE.md`
claim block, and the changelog counts from `REGISTRY.tsv` and
`FRONTIER_PROGRAMS.tsv`. Two new `T` rows change the status counts, and the
queue change changes the frontier rendering.

`canon/SHA256SUMS` is refreshed last, over the five normative files.

## Checks before the release-form commit

```sh
python3 tools/check_policy.py
python3 tools/check_canon.py
python3 tools/check_ledger.py
python3 tools/check_verifier.py --base <merge base>
python3 tools/check_reproduce.py --base <merge base>
```

Then the release form per `AGENTS.md` section 6.9: one content fold commit, then
one release-form commit changing exactly `STATUS.md`, `README.md` and
`CITATION.cff` and naming the content commit; merge without squash or rebase;
tag `canon-v39` only after public readback; publish assets only after tag
readback.

## What this fold does not do

It does not fire `LAMBDA-COCYCLE-ANGLES [H]`, retire it, or change its status.
It proves nothing about RH, decides nothing about whether the declared class is
nonempty, and excludes no ordinate from the grid. It records two exact theorems
and, if the owner accepts, restates a live hypothesis in the sharper form those
theorems justify.
