# Prospective descriptive localization specification

Status: NON-CANONICAL engineering diagnostic. This file freezes a descriptive
decomposition of already consumed samples; it does not preregister fresh data,
an inferential test, a confidence interval, a phase claim, or P1 closure.

## Inputs and execution boundary

All source bytes are read with `git show` from immutable commit
`fc16df1b06d971ca7ef4e2f35eab92d8b9637bdb`, never from a moving checkout.
`INPUTS.json` has fields `commit` and `sha256`, where `sha256` maps repository
paths to lowercase SHA-256 digests. Every consumed blob must match its listed
digest before any arithmetic is performed.

The fixed inputs below have prefix
`notes/C-PHOTON-TWIST-SNAKE-SECTOR-N/ENGINEERING/`:

- `L{L}_k{k}_classMinus_c{c}.tsv` for every `L` in `{4,6,8,10}`, `k` in
  `{1,2}`, and `c` in `{0,1}`: all sixteen up-only CM ladders;
- `analysis.json`, used only to compare reconstructed `log_l_by_chain` values
  and recorded reset totals with the existing frozen analysis.

The parent sources `analyze.py` and `sample.cpp` define the inherited estimator
and reset semantics. No sampler is executed or imported. The script is run
only after the owner has pinned the prospective files and authorized the run:

```sh
python3 notes/C-PHOTON-RESTRICTED-REACHABILITY-N/localize.py \
  --repo . \
  --inputs notes/C-PHOTON-RESTRICTED-REACHABILITY-N/INPUTS.json \
  --output notes/C-PHOTON-RESTRICTED-REACHABILITY-N/ENGINEERING/localization
```

## Frozen arithmetic

For each chain separately and each visited ensemble `m=1,...,L^2`, use all its
recorded 512-sweep blocks. The recorded finite decimal strings are converted
to exact rational numbers. This is exact arithmetic on rounded output records,
not an assertion that the original floating-point measurements are exact.

For each estimator `X`, let `x_b` be its block sum divided by 512, `B` the
number of blocks, and `mu = sum_b x_b/B`. Its frozen log is

\[
\lambda_X=\log\mu+\frac{s_X^2}{2B\mu^2},\qquad
s_X^2=\frac{\sum_b(x_b-\mu)^2}{B-1}.
\]

Use `F=sumFi`, `PF=sumPFi`, `PB=sum(hB0,...,hB4)`, and `Bw=sumBi`.
Forward estimators are used at `m<L^2`; reverse estimators at `m>1`.
The reverse estimator recorded at `m=1` is ignored, as in the frozen parent.
All means, variances, relative variances, and additive bias corrections are
rational. Only logarithms and combinations containing logarithms use Python
binary floating point, explicitly labelled engineering values.

For every step `n=1,...,L^2-1`, retain

\[
a_n=\lambda_{F,n}-\lambda_{PB,n+1},\qquad
b_n=\lambda_{PF,n}-\lambda_{Bw,n+1},\qquad
t_n=(a_n+b_n)/2.
\]

Retain the raw log term and exact rational bias correction separately, both
pairings, every `t_n`, and every cumulative sum in increasing `n`. There is
no sorting or selection by observed size. Recombine all steps to recover
the parent chain value. Compare it with the frozen `analysis.json` value at
absolute tolerance `1e-9*(1+abs(reference))`. This tolerance checks arithmetic
reproduction only; it is not a statistical acceptance threshold.

Also retain the ensemble contribution

\[
c_m=\tfrac12\mathbf1_{m<L^2}(\lambda_{F,m}+\lambda_{PF,m})
-\tfrac12\mathbf1_{m>1}(\lambda_{PB,m}+\lambda_{Bw,m}).
\]

Check that its sum equals the step sum at the same arithmetic tolerance.
Report the fixed decomposition into `m=1`, `2<=m<L^2`, and `m=L^2` and their
sum. These are an ensemble decomposition, not three independent estimators.

## Pairing, resets, and coverage

For every `(L,k)`, subtract chain 1 from chain 0. Output every step difference,
every cumulative difference, and every ensemble difference. Retain both
chains' reset flags at each step's source and destination ensemble, plus the
number of steps since each chain's most recent recorded twist-advance reset
(null before the first such recorded reset).

`forced=1` at reached ensemble `m` means that the preceding twist advance
`m-1 -> m` reset the newly twisted slice `m-1`, followed by 512 discarded
sweeps. The flag is repeated on all blocks of that ensemble; it is counted
once. No twist-advance reset is recorded at the initial ensemble `m=1`.
Initialization may force slice zero into the chosen class; that operation
is outside these flags and totals. A null reset-distance field therefore
does not assert the absence of initialization forcing.

Report exhaustive, disjoint sums by the four destination-flag pairs
`(0,0),(0,1),(1,0),(1,1)`. For steps, this uses flags at `n+1`; for ensemble
contributions, flags at `m`. Every category is output even if empty. These
partitions record association only. A contribution containing two ensembles
cannot attribute a discrepancy causally to the destination reset, and long
memory can persist between resets. No regression, significance test, gate,
change-point search, threshold scan, cross-size fit, or post-hoc subset is used.

The sixteen ladders are the whole fixed comparison scope, including groups
that previously passed and failed. The separate chain 2 dwells only at the
endpoint and is excluded. Thus the reconstruction matches parent
`log_l_by_chain` for chains 0 and 1. It does not reconstruct the parent's full
G3 `own` versus `others` statistic: the latter includes chain 2 at the endpoint
on the `others` side. This distinction must accompany any interpretation.

## Validation and zeros

Before estimating, validate hashes, unique table fields, run identity,
metadata, exact expected ordering, 512-sweep block counts, four blocks at
every intermediate ensemble and 64 endpoint blocks, class-minus membership,
histogram count bounds, consistent segment reset flags, final reset total,
and the parent's sweep-count identity. No row is silently dropped.

Negative or malformed estimator data, inconsistent metadata or schedule,
missing or hash-mismatched inputs, or an arithmetic reproduction discrepancy
raise an error and leave no success report. No repair, substitution, retuning,
or selective rerun is permitted in this pinned version.

A zero estimator mean is a recorded sampling outcome, not a custody failure.
Its log and every dependent local value are null with the explicit label
`ZERO_ESTIMATOR_MEAN`. Unaffected local values remain visible. A cumulative
sum becomes null at its first undefined term and stays null. Complete sums
are null if any constituent is undefined; sums over the remaining terms are
never represented as complete sums. A null chain sum must match the parent's
null chain value. The zero locations are retained without pseudocounts.

## Outputs

- `localization.json`: provenance and input hashes; exact rational estimator
  records; all sixteen chains with step/ensemble tables and fixed summaries;
  all eight paired differences and exhaustive reset partitions; arithmetic
  reproduction checks. Its status is `DESCRIPTIVE_ONLY`.
- `steps.tsv`: every chain step and cumulative value, including both pairings,
  exact rational bias correction, raw logarithmic term, and both reset flags.
- `paired_steps.tsv`: every paired step/cumulative difference and four flags.
- `paired_ensembles.tsv`: every paired ensemble difference and two flags.
- `SHA256SUMS`: checksums of those four outputs.

No output changes the parent disposition `INCONCLUSIVE_EQUILIBRATION` or
establishes equilibration, graph connectivity, mixing time, or physical closure.
