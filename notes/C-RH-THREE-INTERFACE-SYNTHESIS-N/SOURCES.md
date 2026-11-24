# Pinned source correspondence

NON-CANONICAL. Read-only source audit, 2026-11-24. This file records what was
inspected; it does not upgrade any source status.

## Public authority and existing owners

Public Canon v117:

- main and annotated tag target: `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`;
- content: `d65e32c4b8e9a14496d3b7aba46fc384f51f81dc`;
- tag object: `63ff3d2f7edc0c921a6c8ddd033badb59b632436`;
- Canon SHA-256: `93a8d0c17ed88d93a62b56c44d65b6903c980654f7e5ea82da7e363a510a22a9`;
- Canon bytes: 1624192.

All five normative file hashes matched locally. The local repository runner
reported `CANON PASS v117 claims=639` after fetching sufficient ancestry.
The initial shallow checkout could not resolve the content commit; no hash
mismatch occurred. GitHub's compare endpoint independently showed the content
as the merge base, with main two commits ahead and zero behind.

Exact-main workflow [45388050270](https://github.com/mathorn1973/twist-j/actions/runs/45388050270)
reported successful x86_64, aarch64 and aggregate checks. Tag and release
publication runs [45388370632](https://github.com/mathorn1973/twist-j/actions/runs/45388370632)
and [45388990366](https://github.com/mathorn1973/twist-j/actions/runs/45388990366)
reported successful publication jobs. These are existing authority receipts,
not executions of this package's mathematics.

| Existing owner | Inspected immutable input | Role |
|---|---|---|
| Canon CM5 and rapidity statements | Public main above, relevant CANON, REGISTRY, EVIDENCE and probe records | Registered inputs; no reinterpretation of their scopes |
| #2080 local defect | `bddd14b4eb684f613db3ec51df56527eea2dd480` | Previous two-place defect arithmetic |
| #2065 centered frame | `18e325c068c09d98ddf8383724a8c1c9f15dc021` | Exact centered bound and integrated source chord |
| #2070 actual period/frame | `948ddd240340e14d6bbac96baade3039e8b9f263` | R17 algebra/commutant distinction and R19 affine source-loss estimate |
| #2087 arithmetic kernel | `59a41b28b9c6cedaf2fa3ef4a0a23e197a87d1cd` | Periodic kernel, short-support estimate and signed power-window lemma |

The older project attachments were not used as current authority. Existing
owners retain their claims; this package only supplies the explicitly
identified comparisons and deductions.

## External proof and explanatory sources

The external Lean archive is
[`leanprover-community/riemann-hypothesis` at `40e56bab026552e089d7afcfeff08d2defb9c005`](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005).
FRAME.md links the exact statements and consumers. Root additionally read
`StatementFrameF.lean`, the threshold/count and lattice-inclusion portion of
`TheoremFSharp.lean`, and `RecBridge.WordFacts` at that pin.

The [Lean FRO and Mathlib joint statement](https://leanprover-community.github.io/blog/posts/riemann-hypothesis/),
dated 2026-11-21, reports independent theorem-statement comparison and checking
of the inert exported proof. This is distinct from the state of any particular
compression challenge or our proposed independent route.

The [Waterloo version-2 exposition](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf),
dated 2026-11-22, is a working explanation and marks its conditional classical
reductions explicitly. Local notation comes from III.5-III.6; the period and
slope interfaces are in III.10-III.11. The separate
[Zhang preliminary note](https://www.ihes.fr/~rzhang/files/GRH%20note.pdf)
is another exposition, not an independent complete proof used here.

The publicly retrieved [English Matematyka RH page](https://matematyka.cz/en/rh)
reports its neutral-coefficient Lean result and describes its orientation
cutoff proof as written, not Lean-checked. This package derives the neutral
and cutoff estimates on paper; it does not adopt a reported build as its own
execution evidence. The user's Czech route is [matematyka.cz/rh](https://matematyka.cz/rh).

## Compression project: verified module is not an integrated replacement

The [live dashboard](https://riemann.verifytask.cn/) describes 39 pillars
covering a deduplicated subset, separately from full-proof checking.
Its dated phase-3 notice and the repository README describe different
coverage snapshots; their figures must not be silently combined.

The following three staged submissions were read at their immutable heads,
including the PR body, frozen target statement and author-described proof
method. The mathematical source statements, rather than a compression
percentage, determine relevance.

| Pillar | Pin and primary record | Actual target and reported shortening | Relevance here |
|---|---|---|---|
| Core 6 | `d9942073f3ef3314068344b6ce67f0a49a4a4e11`, [PR #7](https://github.com/Osgood001/riemann-hypothesis/pull/7) | CM j-invariant and formal-group integrality; replaces custom analytic machinery with established Mathlib estimates and zero factorization | It concerns integral models and analytic inputs, not just J's residue Frobenius. |
| Core 12 | `b35625028c5dc22844761411db7cdc7574f11cb7`, [PR #13](https://github.com/Osgood001/riemann-hypothesis/pull/13) | Eight cyclotomic power-series statements; reorganized through polynomial algebra-map extensionality and power-series conversion | A promising simplification pattern after matching the actual coefficient ring, substitutions and eight consumers. |
| Core 13 | `7a1531bf5cf905cb4ebe26f8152516516fbda282`, [PR #14](https://github.com/Osgood001/riemann-hypothesis/pull/14) | Box sums, sharp recursion and leading-minor counts; shorter inequalities using existing library results | A different supplier from the full common-image/HN interface; its title does not identify the two. |

The inspected PRs explicitly await author/license clearance and toolchain and
interface integration. They report standalone challenge checks. This package
imports none of their implementations. A future code transfer must resolve
those recorded conditions before copying or integration. The present original
paper proofs and bibliographic links do not require such a code transfer.

## Additional mathematical sources

- Galbraith and Pujolas, [Distortion maps for genus two curves](https://www.math.auckland.ac.nz/~sgal018/jordi-paper.pdf),
  section 3, for the fixed genus-two Frobenius example.
- Rachel Pries, [The Torelli locus and Newton polygons](https://arxiv.org/abs/2509.00998),
  section 4.3, for Cartier/Verschiebung and the hyperelliptic coefficient rule.
- The prior centered-frame note credits Jose Brox and the
  [Hexagon note](https://hexagonmath.org/2611.00828v1) for its source ingredients;
  this attribution is retained, with no historical-priority assertion here.
- Fujisawa and Minamide, [On partial sums of the Mobius and Liouville functions for number fields](https://arxiv.org/pdf/1212.4348),
  Theorem 1.3 with the rational field, for the classical RH/Mertens equivalence.

Only original derivations, source correspondence and references are authored
in this directory. No third-party source implementation or full exposition
is copied into the package.
