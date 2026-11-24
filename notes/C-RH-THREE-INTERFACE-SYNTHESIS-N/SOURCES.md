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

## Signed-pairing continuation inputs

The same PUBLIC main was read back before the continuation and before its
delivery. The continuation uses the first package commit
`c7bf6ec1014b7d6bdc0e75de95054f2aa58ae84e` for its base definitions.
The prospective scope was exposed in owner issue #2091 before new authoring.

- The large-prime asymptotic is inherited from #2087/#2089,
  [LARGE-PRIME-TAIL.md, Section 4, equation (7)](https://github.com/mathorn1973/twist-j/blob/09ae5168191eed9cee484c08c5d65f58b31494d1/notes/C-RH-ARITHMETIC-KERNEL-N/round3/LARGE-PRIME-TAIL.md)
  at commit `09ae5168191eed9cee484c08c5d65f58b31494d1`, file Git blob
  `24793f2ca47dd618cca46ea0d6fac5863ced5337`. That source derives
  the leading N/(log N)^2 term and leaves identification with the
  original orientation projection to the reader. LOCAL-AVERAGES.md gives
  that exact identification and distinguishes the row mask from the
  direction-support projection. The earlier owner keeps the asymptotic.
- [NIST DLMF, Section 27.8, equation 27.8.6](https://dlmf.nist.gov/27.8.E6)
  records orthogonality over the Dirichlet characters of a finite unit
  group. DIRICHLET-READOUT.md proves the needed orthogonality by the
  explicit dyadic character sums as well. This is a construction on the
  current finite carrier, with no claim of historical priority for
  finite Fourier reconstruction.
- Yamada, [Explicit formulae for primes in arithmetic progressions, I](https://arxiv.org/abs/1306.5322),
  version 4, introduction, records the classical prime-count estimate
  with every fixed logarithmic saving at fixed modulus. The use here is
  solely modulus five. The arbitrary-saving statement is not inferred
  from a finite table of explicit constants.
- Thorner and Zaman, [Refinements to the prime number theorem for arithmetic progressions](https://arxiv.org/abs/2108.10878),
  Corollary 1.4, is another primary reference for the fixed-modulus input
  used in LOCAL-AVERAGES.md. The sharp endpoint proof needs the classical
  estimate to any fixed inverse-logarithmic accuracy.
- Lee and Leong, [New explicit bounds for the Mertens function and the reciprocal of the Riemann zeta-function](https://arxiv.org/abs/2208.06141),
  version 4, Theorem 1.1 and introduction, provide an unconditional
  Mertens bound stronger than every fixed logarithmic saving. No explicit
  numerical constant or finite threshold from that paper was imported in
  the signed-pairing stage. The whole-window stage below additionally
  records a stated example from Theorem 1.2.

The new Dirichlet identity is proved locally at every prime, including
2, 5 and 7. Its Euler-unit estimates are uniform in the sampling modulus;
no uniform zero-free statement for the denominator L functions is used.
The smooth-support theorem concerns the actual absolute sector sum.
Neither its sharp cutoff nor the inherited logarithmic large-prime
expansion supplies the open signed whole-window estimate.

## Whole-window continuation inputs

The continuation starts from package commit
`853237620bc2be69026168f32bb0ad871f668950`. The PUBLIC authority above,
its normative hashes, required checks and tag/content ancestry were
refreshed before the prospective owner-issue extension. The original
R_(1/36) and its complete integer windows remain fixed.

- Katsurada and Matsumoto,
  [A weighted integral approach to the mean square of Dirichlet L-functions](https://www.math.nagoya-u.ac.jp/~kohjimat/L-functions5.pdf),
  Theorem 1, gives the mean square needed for the primitive quadratic
  character of prime modulus five. Here it supplies the bound O(T log T)
  at fixed conductor. It is not used as a uniform assertion for the
  growing character conductors in CHARACTER-WINDOW.md.
- Lee and Leong,
  [version 4](https://arxiv.org/html/2208.06141v4), Theorem 3.1,
  supplies the reciprocal-zeta logarithmic bound on real part one.
  Theorem 1.2 supplies the Korobov-Vinogradov-shaped Mertens estimate.
  Its stated example has C=70179/12500 and c=319/100000 for
  log(x)>=100000. These are rational representations of the published
  admissible constants, not new computations. The later o(1) window
  comparison has no numerical effective threshold claimed here.
- The fixed-modulus prime-count inputs cited above control the smooth
  absolute block, including the second-order saving at c=1/36.
- The rational-field RH/Mertens equivalence in Fujisawa and Minamide,
  Theorem 1.3, is used only in the explicitly external-RH branch of the
  whole-window bound. Root refreshed the Lean FRO/Mathlib joint statement;
  no local verification or new independent RH proof is inferred.
- The adjacent owner #2087/#2089 at
  `d26ca6caab5dda3875333f9d2ba73b74b55ba674` supplies the inspected
  [FINITE-TAPER.md](https://github.com/mathorn1973/twist-j/blob/d26ca6caab5dda3875333f9d2ba73b74b55ba674/notes/C-RH-ARITHMETIC-KERNEL-N/round4/FINITE-TAPER.md)
  and
  [LARGE-PRIME-HIERARCHY.md](https://github.com/mathorn1973/twist-j/blob/d26ca6caab5dda3875333f9d2ba73b74b55ba674/notes/C-RH-ARITHMETIC-KERNEL-N/round4/LARGE-PRIME-HIERARCHY.md).
  Its periodic covariance and generic separated-frequency cutoff through
  exponent 2/3 are attributed. PRIME-CANCELLATION.md uses a distinct
  balanced bilinear carrier, retains its nonpositive square and proves
  its own exact complete-period covariance and finite-window bounds.

All four new notes are original paper deductions and same-session review.
No new scientific executable, enumeration, empirical input or formal
verification was run. Their status remains NON-CANONICAL candidate-D;
the native full positive-energy estimate remains O.

## Long low-frequency signed-energy continuation

The fixed starting package is
2147cba363d90d2772c3d5f883d79c326260d9c9. Its T_low, actual coefficient
normalization, affine shift and integer-window quantifiers are preserved
as the reference object. New carriers are separately named and compared.
The owner-issue scope was exposed and read back before authoring.

- The neighboring #2087/#2089 input is now pinned at
  f55cbcd1bf0eff6de99449c37ac8c03916b8acfe. Root read its
  [round-5 report](https://github.com/mathorn1973/twist-j/blob/f55cbcd1bf0eff6de99449c37ac8c03916b8acfe/notes/C-RH-ARITHMETIC-KERNEL-N/round5/REPORT.md),
  [NUMERATOR-ESTIMATE.md](https://github.com/mathorn1973/twist-j/blob/f55cbcd1bf0eff6de99449c37ac8c03916b8acfe/notes/C-RH-ARITHMETIC-KERNEL-N/round5/NUMERATOR-ESTIMATE.md)
  and
  [SHORT-SUM-TRANSFER.md](https://github.com/mathorn1973/twist-j/blob/f55cbcd1bf0eff6de99449c37ac8c03916b8acfe/notes/C-RH-ARITHMETIC-KERNEL-N/round5/SHORT-SUM-TRANSFER.md).
  The rational finite taper remains from its
  [FINITE-TAPER.md](https://github.com/mathorn1973/twist-j/blob/f55cbcd1bf0eff6de99449c37ac8c03916b8acfe/notes/C-RH-ARITHMETIC-KERNEL-N/round4/FINITE-TAPER.md).
  The actual carriers differ. The geometric numerator argument is
  transported here with the present cofactor and forward-average multiplier;
  the short-sum theorem is applied directly to mu. The adjacent owner
  retains its original arguments and results.
- Matomaki, Radziwill, Shao, Tao and Teravainen,
  [Higher uniformity of arithmetic functions in short intervals II. Almost all intervals](https://link.springer.com/article/10.1007/s00222-026-01408-6),
  Inventiones mathematicae 244 (2026), 967-1091, Theorem 1.1(i) and
  definition (1.4). Root read the full main statement. The fixed circle
  with constant function one admits interval prefixes through the starred
  arithmetic-progression maximum. The source supplies each prescribed
  fixed logarithmic saving outside an exceptional set of controlled measure
  for lengths between X^(1/3+eta) and X^(1-eta). Unit-cell integration
  and the trivial bound account for all integer starts in the square norm.
  No pointwise all-start theorem, fixed-shift cancellation, power saving
  at a larger smoothing width, or uniformity for growing logarithmic
  orders is imported.
- Lee and Leong, version 4, Theorem 1.2, was read again for the exact
  unconditional Mertens input used twice in the central-band derivation.
  That argument proves an estimate for a smooth part of the actual
  balanced spectrum. The complement and affine term remain, and the
  estimate itself does not reach square-root scale.
- The prime-pair diagnostic uses the classical prime number theorem.
  The original reference is
  [Hadamard (1896)](https://www.numdam.org/item/BSMF_1896__24__199_1/).
  Root also read the explicit prime-count asymptotic and error statement
  in [NIST DLMF 27.12](https://dlmf.nist.gov/27.12).
  Subtracting the two fixed-ratio prime-count asymptotics gives the
  stated interval count. No finite numerical prime census was performed.

The three Sol papers and Astra derivation/opposition are original
NON-CANONICAL candidate-D notes. Root and another Sol reconstructed the
central-band proof separately within this session. No scientific executable,
empirical input, enumeration or formal-verifier run was used.
