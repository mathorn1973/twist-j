# RF3 2025 Source Disposition

## Control

- Review basis: public `main` commit `8c53ed0f1ab0ed60e10566cc4e3b5ae74334e0e9`.
- Scope: sixteen user-supplied ZIP archives and the corresponding already-extracted `main.tex` files.
- Disposition: quarantined source index only.
- Payload import: no.
- Scientific effect: none.
- Registry, evidence, and claim-state effect: none.

This note is an intake firewall, not scientific authority. It does not reproduce source payloads, make or promote claims, supply evidence, or change any status. No raw prose, formula, figure, bibliography, contact string, or code from the sources is copied here.

## Archive and format safety

Static inspection found sixteen small ZIP archives. Each archive contains exactly one regular file named `main.tex`; no absolute path, parent traversal, symlink, archive comment, or additional member was present. No active TeX external-file inclusion or shell-execution command was found. This does not certify the sources as safe to compile: any later rendering must still use an isolated environment with shell escape disabled.

The extracted corpus copies match their ZIP payloads byte for byte in all sixteen cases. The archive set totals 80,113 bytes; the uncompressed TeX payloads total 188,077 bytes. The set contains no PDF, figure, bibliography database, machine-readable data, executable verifier, expected-output file, or run log.

## Exact source index

| # | Supplied archive | ZIP bytes | ZIP SHA-256 | `main.tex` bytes | `main.tex` SHA-256 |
|---:|---|---:|---|---:|---|
| 01 | `01-Four-TWIST-Fundamentals.zip` | 2,931 | `b5087b6584c5b37850542376dc840e47c08a1b2fc716caf5cd167d68a6602998` | 5,979 | `39cf90ccfff544b583ab52504e536d2b02c4e6cded2cfcf2d3438f9badd77760` |
| 02 | `02-PhilosphyTWIST.zip` | 6,785 | `fe53e8b86cb9484fffe8f6d89b8ad8d2eca01a25b70180a069125d1d072205ff` | 16,881 | `56af123d2126ff26567c5d7aa409e93ed0c074080465abc60add24018402db4a` |
| 03 | `03-GeneralRelativity.zip` | 7,223 | `83e6af437f0f57507a6e4b5883128b13c2e2742c83c60727e52cf347493c38e6` | 17,511 | `5302d47eb750fecf856159b744f6870acd5521a0d9539ae29fdfb86d5faacc0e` |
| 04 | `04-Bell-Article.zip` | 4,159 | `dfebb3d844f8c46108be53e3f97ef5d68f429f83bb684eed84b6c0abe602c5b0` | 8,757 | `d9605eefd166171400054ad47d31c8ff056210471f2b260110b37efe5d6cc160` |
| 05 | `05-TWIST-Particle-Physics.zip` | 6,418 | `8a916f083463dff2296b9d6ef63237e8c11e90557f7b7a3d3f07aa0a9a5aba1d` | 15,126 | `85820a9ba9467fc00bffea5a431eabbd63b760fa707be55e604fe09b5628b26f` |
| 06 | `06-TWIST-Bridge-B.zip` | 4,398 | `7ef30dc3ccb6ccdde7febfcabcc34d63a9e38c009e88747fb9abb9ac77648293` | 9,228 | `02ded2be9e3864e4fa78e0f73ae3484650d7ceceacb568da4ad457fc3c1bbe54` |
| 07 | `07-TWIST-Alpha-Gometry.zip` | 5,361 | `dfd227bd1b55b1f681bb6c232ef4b700d5361c2bcc330cd9937f85a28534ecb9` | 12,442 | `95637469b9a28452c142ed9fef8530d54134a9d267666b9db64aac2c56dc7cf9` |
| 08 | `08-Golden-Constant-TWIST.zip` | 10,071 | `0baa85bc50083ed2822fdbf686d1d9b4d24f27758feaf364db2ab811c5df5002` | 25,006 | `5a23e8630321243a2a64e815de05952266dde6b06981540f4341dc77e4308a27` |
| 09 | `09-TWIST-quick-quantum-mechanics.zip` | 5,547 | `e930c6dcef6e852265a822f134277f34083182cd5f577ab0d37a611aace46ae2` | 11,751 | `a8321286558f97f6aa3358735ba9ae2e6094a8110698d8c90bdd3ca680497f4c` |
| 10 | `10-Introduction-to-TWIST.zip` | 5,292 | `9b1e6a5c41ac585a03e1e4c8b08a88ec147e0d2ec1504b49f69b114eb90e9e9f` | 13,004 | `179c3e68acf527e4b18c9bae229430a848b3d4bc0217f7a7082ddfe57a288301` |
| 11 | `11-TWIST-Dark-Weave.zip` | 5,706 | `927c59fe0b4ce532302c6c18d4b207dbabc0be3ef15795029c23b70e6ff22012` | 13,634 | `b095cf0ca56e9ebaecd42e3f8f69b56c3e4afcc9126238a51ee9de3394aedd1a` |
| 12 | `12-TWIST-UNITY.zip` | 3,141 | `428dd09584a281c34f50a824fe149dcead16e120eca1bb78bd1bd316b0929e8d` | 8,156 | `e09a70e48c07529fda45056a4c008c165c6e6935cbbe1378b2b06435853326cd` |
| 13 | `13-Testy-TWIST.zip` | 1,337 | `e29ca1721baae840916fa628986ca0f1128358f68e9d189f4d81feec2bb7754a` | 2,668 | `112a89dd7798b475e00e3fe72f1742b2d0d12af4fdd99fcf60f5606804fd4c0a` |
| 14 | `14-qIck-TWIST-Reference.zip` | 4,455 | `e5d8e8177431a59b67b4e53981a19c71c9dab35f8264527f3282951e36d63d23` | 12,503 | `f12450184eb673b2b558445402d15a1e42163ceba973dbb90bf490833e7411a5` |
| 15 | `15-With-a-TWIST.zip` | 2,231 | `0006b4c6449f860f08c692846569e7309578436b95c992a02dfd1d0b8494f967` | 4,627 | `c2a52c809b01f499410629291ed045acc01cbdf38e692c0ae579c31b5c35ec6a` |
| 16 | `16-TWIST-Gearbox.zip` | 5,058 | `12f0e80e8798f8ed7c2a0ccfc2547026777caf942abcb093981582f0b7b11d39` | 10,804 | `ee2fcf96e742fde3f362e0edf6b7aa3cf5b2510e99867966df66f6dd2e916b95` |

## Authorship, licence, and personal-data firewall

No source carries a licence, SPDX identifier, or explicit redistribution grant. Eleven name A. M. Thorn as author; four contain no explicit author; one uses unresolved author, institution, contact, archive, and funding placeholders. Several sources contain personal contact or social-account strings, intentionally omitted from this index.

Receipt of the files does not establish authorship, ownership, permission to redistribute, or compatibility with the repository licence. Accordingly:

1. Do not commit the ZIPs or extracted TeX.
2. Do not copy source prose, equations, figures, bibliographies, acknowledgements, contact strings, or metadata into public work.
3. Before any later quotation or payload import, establish ownership and a compatible explicit licence, resolve placeholders, and perform a personal-data review.
4. Any scientific proposition suggested by the sources must be restated independently, typed against the then-current public interfaces, and pass the ordinary proof or preregistered computation gates. Source prose is never evidence.

## Per-source quarantine reasons

| # | Disposition reason |
|---:|---|
| 01 | The advertised “operational proofs” do not follow: reproducibility, locality, and Ramsey-style composition do not by themselves yield the asserted unitary group or Stone generator; the later uniqueness and scale conclusions are likewise unproved. Fragmentary and unattributed. |
| 02 | The proposed “Topo-Noether” step is ill-typed: the listed reindexing, local mutation, and tick transformations are discrete, while the argument invokes an unfrozen one-parameter generator. The carrier, action, transformation class, and equality notion are not fixed. One program cue is retained below, without the claimed theorem. |
| 03 | Core discrete-calculus identities are mistyped: same-degree self-compositions replace the typed boundary/coboundary identity. A displayed gravitational coefficient changes form without derivation, and the Einstein equation is asserted rather than derived. |
| 04 | Generic Bell exposition duplicates current Bell work and contains a false operator bound in its Tsirelson sketch. It supplies neither a TWIST apparatus map nor the still-required causal-accounting bridge. |
| 05 | Particle assignments, proposed new states, stability statements, and gaps are unsupported. The “no monopoles” statement conflicts with the current monopole result, and the unique-photon claim exceeds the current open phase/cone bridge. One predefinition cue is retained below; no species assignment is retained. |
| 06 | The proposed bridge is built from superseded legacy quantities and becomes largely tautological after those definitions. No typed bridge to the current carrier or current gravity interfaces is supplied. |
| 07 | The advertised finite carrier is not reproducible: Hodge matrices and a pointwise ledger are absent. Its quoted fine-structure value conflicts with the current digit row. |
| 08 | Authorship, institution, contact, archive, and funding metadata remain placeholders. The headline cosmological “one-number test” is circular because it reuses the same Friedmann/critical-density relations; the draft itself notes a missing correction. Dark-sector conclusions are unsupported. |
| 09 | Standard diagonalization and FFT ideas are presented without runnable code, data, frozen inputs, or expected outputs. The speed comparison uses an unnecessarily iterated baseline and does not establish physical evidence or the advertised complexity conclusion. |
| 10 | A quantity is defined as an action but then used as an evolution time step, producing a dimensional/type mismatch. Emergent Minkowski and Lorentz conclusions are asserted without a current bridge. |
| 11 | The microscopic derivation of the effective coupling is explicitly deferred, while an illustrative choice is used to select a cosmology. This exceeds the current dark-energy underdetermination and conformal-weight boundary. |
| 12 | The scaling discussion uses mutually incompatible powers for the same information quantity under nominally fixed conditions. Its quantum and gravity conclusions are summary assertions rather than derivations. |
| 13 | The testing dashboard treats external Bell/CHSH experiments as confirmation of TWIST without a TWIST apparatus map or causal bridge. It contains no reproducible test object. |
| 14 | Legacy quick-reference material duplicates or predates current definitions, has no explicit author or licence, and supplies no proof or executable test. |
| 15 | The clock relation conflicts with the surrounding legacy convention, the proposed Newton coefficient is dimensionally wrong, and the cosmological form is inconsistent with other sources in the same set. No explicit author or licence is present. |
| 16 | The scalar-log-scale plus Poisson route may be recognizable as an implementation idea, but it has no current carrier, source map, action proof, normalization, or bridge. It is already subsumed by existing inhomogeneous-FRW and curvature obligations, so it creates no separate cue. |

## Retained program cues

Only the following two directions survive semantic triage. They are independently restated work-program prompts, not imported propositions, claims, evidence, or commitments for v75.

### 1. Action/invariance realization audit

On an already selected current TWIST-J carrier, freeze the exact action or functional, the transformation class, and the equality notion. Classify separately:

- state or cell relabelling;
- local carrier mutation constrained by a frozen equivalence or defect class;
- clock blocking or reparameterization.

For each class, first prove a well-typed invariance statement. Only after that proof should the program seek an exact conservation law or cocycle theorem. The legacy label “Topo-Noether” must not be reused as an established result.

### 2. Matter topological-carrier predefinition

Before any particle-species assignment, freeze:

- layer and state/configuration carrier;
- action or dynamics and equivalence relation;
- topological invariant and allowed defect class;
- stability criterion;
- spectral or gap operator, domain, and normalization;
- proof obligations for stability and the gap;
- a typed bridge to the current algebraic matter decoder and mass-ladder interfaces.

Only a construction that closes those obligations may later support a species-identification probe. Names or numerical matches from the legacy sources do not survive intake.

## Routing recommendation

Retain this single noncanonical disposition note only. Do not import or split the legacy payloads, and do not create legacy-derived evidence or claim rows. If v75 ownership accepts either retained cue, it should be rewritten as a fresh current-interface work item with independent derivation and provenance; otherwise no further repository action is warranted.
