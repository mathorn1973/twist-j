# Li cocycle lane: cross-branch consolidation

```text
STATUS:          NON-CANONICAL CONSOLIDATION MAP
AUTHORITY:       none
PUBLIC CANON:    v6, unchanged
PUBLIC CLAIMS:   none created here
DATE:            2026-07-16
```

This is the repository-side source of truth for the currently visible Li
cocycle lane.  It consolidates only bytes and git objects actually audited in
this environment.  Owner-side attestations whose artifacts are absent remain
explicitly marked as reported.

## 1. Authority and public baseline

The normative public baseline remains

```text
repository       mathorn1973/twist-j
branch           main
commit           6bb013bafb2d1c06fcb295fdbfce0f86198fd685
tag              canon-v6
Public Canon     v6
```

The public probe branch `probe/P-PENTAGON-WEIL-1` is visible at
`a7ff0056...`; it records an x86_64 witness.  Nothing under this incubation
directory changes that branch, the public registry, or the Canon.

## 2. Visible branch and artifact map

### Repository-side line

```text
6bb013b  Public Canon v6 baseline
  |
913d1ea  preserve exact J-LI-SCHOENBERG-2 verifier and stdout
  |
1678d7b  record first cross-branch transfer audit
  |
a62b040  prove the infinite cyclic-carrier boundary
  |
current  atom normalization, verified patch audit, and T_2/K_3 incubation gate
```

The named local branches before the current update are

```text
agent/j-li-schoenberg-2-incubation  913d1ea6ab6493af29b404a963c399ab580115fc
agent/j-li-cross-branch-staging     a62b04090608049e946daf237281cd251ea26fbf
```

The earlier thin handoff from the staging line is

```text
bundle  ee06fc0d85fd5a826022770bb40000e10697f7199ffdd23578840daece9ad26a
patch   762fa6438807ff85f7ad999a519adb795cab9bef12f446fc251d12a4f68b9cc0
```

It ends at `a62b040`; a later handoff may supersede it without rewriting it.

### Owner-side incubation line

The separately reported history is

```text
base             6bb013bafb2d1c06fcb295fdbfce0f86198fd685
commit           aee7a3762d6fffb1936ae54121dd77d74078b25b
reported branch  agent/c-li-cocycle-1-incubation
```

The received format patch is exact and audited:

```text
patch sha256     4e3f43c67d2cc29c3abfc4e8200bdc009c5e769270b8a6cb887755d4a2fdefa8
stable patch-id  5a7dc9151e1304d3e2566a530d5ce5eed4009e13
applied tree     d78156ecba0782d61bdc46771ceb2c96d15fb82d
```

It applies cleanly to `6bb013b`, stays under `notes/incubation/`, passes all
three embedded manifests, and reproduces all six embedded stdout records.
The complete audit is in `CROSS_BRANCH_AUDIT.md`.

The patch does not carry parent and committer metadata and therefore cannot
recreate the reported commit object.  The reported bundle with SHA-256 prefix
`373fde1e...9169` is not present in the attachment surface visible here.
Accordingly, the content is verified but the exact history merge remains
blocked.

## 3. Mathematical crosswalk

| Repository-side identifier | Parallel spelling | Exact scope | Current status here |
| --- | --- | --- | ---: |
| `PENTAGON-NORMALIZATION` | G0/G1 normalization | \(Z_J=\zeta\), \(\xi_J=\xi\) after root-filter division | mathematical T candidate |
| `J-LI-CND-EQUIVALENCE` | positive normal form | RH iff the even Li sequence is CND | mathematical T candidate |
| `J-LI-TOEPLITZ-EQUIVALENCE` | moment wall | RH iff every \(T_N\) is PSD | mathematical T candidate |
| `J-LI-COCYCLE-NORMAL-FORM` | `J-LI-ALL-N` spine | abstract unitary cocycle norm identity | T as an equivalence |
| `J-LI-SCHOENBERG-2` | first joint gate | exact \(T_1/K_2\) certificate | candidate-T-ready; public unregistered |
| `J-LI-SCHOENBERG-3` | \(\sigma_3\to\lambda_3\to T_2\) | exact two-architecture interval certificate | candidate-T-ready |
| `J-LI-CYCLIC-CARRIER-DIMENSION` | finite-support no-go | no fixed finite cyclic carrier can realize all Li coefficients | mathematical T candidate |
| `J-LI-ATOM-TEST` | atom/increment test | no atom at 1 iff \(\Delta\lambda_n=o(n)\) inside the PD frame | T as an equivalence |
| `J-LI-FEJER-SCALING` | averaged carrier shape | all-\(n\) realization forces logarithmic Fejér means | T as necessary implication |
| `J-LI-MOMENT-BRIDGE` | exact Fourier lift | independently constructed J moments equal Li moments for all indices | O |
| `COCYCLE-BY-FINITE-FIT` | finite carrier guard | F only when it means one fixed finite spectral carrier for every \(n\) | proposed F, scoped |
| `J-LI-COCYCLE-REALIZATION` | `J-LI-ALL-N` open lift | uniform J-native construction without hidden import | O |
| `RH` | G5 wall | all nontrivial zeta zeros on the critical line | O |

A different finite-dimensional fit for each cutoff is not excluded.  It is
not an all-\(n\) realization and must not be classified by the scoped no-go.

## 4. Atom-test correction to the owner-side wording

Let \(\mu_v\) be the spectral measure of the cocycle vector and let

\[
\sigma=\mu_v+\iota_*\mu_v,
\qquad \iota(z)=\overline z.
\]

Then

\[
\mu_v(\mathbb T)=\lambda_1,
\qquad
\sigma(\mathbb T)=2\lambda_1,
\qquad
\widehat\sigma(n)=t_n.
\]

Thus the two measures are related but are not identical.  Their atom formulas
are

\[
\mu_v(\{1\})
=\lim_{N\to\infty}
\frac{\lambda_{N+1}-\lambda_N}{2N+1},
\]

and

\[
\sigma(\{1\})
=\lim_{N\to\infty}
\frac{2(\lambda_{N+1}-\lambda_N)}{2N+1}.
\]

The exact consequence is \(\Delta\lambda_N=o(N)\).  The standard Lagarias
estimate for \(\lambda_N\) cannot be differenced termwise to obtain
\(\Delta\lambda_N\sim\tfrac12\log N\); that stronger kill-test needs an
independent theorem.  `ATOM_TEST.md` freezes the corrected statement.

## 5. Newly closed finite gate

The new pinned source

```text
verify_lambda3_t2.py
sha256  49cdaa5769104fda39a18d5a3e75dd4f2da6526e4a2e93201f89345058ebad2a
```

derives

\[
\sigma_3
=1+\gamma^3+3\gamma\gamma_1
+\frac32\gamma_2-\frac78\zeta(3),
\]

\[
\lambda_3=3\sigma_1-3\sigma_2+\sigma_3,
\]

and certifies \(T_2\succ0\), equivalently \(K_3\succ0\), by exact integer
interval arithmetic.  Its first x86_64 run and an immediate byte comparison
both match

```text
LAMBDA3_T2_EXPECTED.txt
sha256  678bd1b4e88b12f074c5c46ed06c69f98984570cc3c312a64921a9ac4b0ef60a
11 PASS, 0 FAIL, exit 0
```

An independent analytic audit reproduced the output and independently checked
the \(\gamma_2\) and \(\zeta(3)\) enclosures by a sharper Euler--Maclaurin
calculation.  A later Ubuntu 24.04.4 AArch64 run with Python 3.12.3 reproduced
the same 1542 stdout bytes, exit zero, and empty stderr.  The neutral record is
`LAMBDA3_T2_AARCH64_RUN.md`; the finite gate is now candidate-T-ready but
publicly unregistered.

## 6. Exact unblock sequence

To preserve both histories:

1. attach the actual `373fde1e...9169` git bundle, not another prose export or
   format patch;
2. verify its full SHA-256 and run `git bundle verify`;
3. import it into a new non-public ref and require the tip to be exactly
   `aee7a3762d6fffb1936ae54121dd77d74078b25b` with parent `6bb013b...`;
4. compare the imported tree to the already audited patch tree;
5. merge it with `--no-ff`, with the then-current repository-side staging tip
   as first parent and `aee7a376...` as second parent;
6. rerun all manifests and exact stdout comparisons;
7. produce one new thin consolidation bundle without rebasing either line.

No authentication is needed for these local object operations.  Push and any
public promotion remain separate owner-authorized actions.

## 7. Frozen wall

```text
FINITE NORMAL-FORM RESULTS       exact mathematical/candidate results only
UNIFORM J-NATIVE REALIZATION     O
G5 POSITIVITY FOR ALL n          O
RH                               O
PUBLIC REGISTRATION              absent
```

The next mathematically meaningful work is structural: freeze one explicit
J-native carrier and subject it to the L6 shape protocol in
`P-J-LI-FEJER-CARRIER-1_PREREG_DRAFT.md`.  The shape probe remains blocked
until that object exists.  The separate all-m moment bridge remains the
RH-hard wall.  Computing further finite Li gates is useful for calibration and
falsification, but no finite prefix moves the all-\(n\) wall.
