# Source qualification: extraction versus acquisition metadata

**NON-CANONICAL / DOCUMENTATION QUALIFICATION / NO OUTCOME ACCESS.**
Audit date: 2026-09-16. Active authority: Public Canon v87. The freshly
checked audit-start main was `fd512f50d90382124e7c00afa926c8083fd56e06`.
Subsequent evidence integration retains the same normative Canon. This note creates
no probe, physical certificate, source admission or claim promotion.

**Decision after schema review: CURBy supplies a genuinely new documented
apparatus/certificate lead, but `/params` does not establish a route to the
missing acquisition calibration. Its demonstrated contract is entropy
extraction. No inspected source qualifies the eight-port energy prediction,
the old Alice run3 test, or a new physical count test.** The useful result is
an exact distinction between extraction metadata and the still-unlocated
physical timing/coverage certificate.

## 1. Basis and genuinely new evidence

The local authority-context reads were `V81-TRC1-SIGNED-RESPONSE-SOURCE-QUALIFICATION-1`,
`V81-NIST-CALIBRATION-QUALIFICATION-1`, `DECODER-OPEN-DATA-BRIDGE-1`,
and the latest `notes/canon/PASSIVE-QDD-V88/PHYSICAL-NEXT-TEST.md`.
None of those three earlier source notes names CURBy, arXiv:2411.05247,
NIST DOI 10.18434/T4/1425490 or CORA DOI 10.34810/DATA3116
(literal-ID check). This establishes novelty relative to these audits,
not priority across all repository history or literature.

Kavuri et al.'s [2025 paper](https://www.nature.com/articles/s41586-025-09054-3)
identifies the [CU public archive](https://random.colorado.edu/) and
[author GitHub organization](https://github.com/buff-beacon-project).
Its [author methods, II.1 and supplement I–II](https://arxiv.org/html/2411.05247v1)
document a trial marker on each attempt, a detection window fixed before the
demonstration, and a spacelike-separation certificate supplied with each data
chunk. Fixed trusted latencies are combined with contemporaneous timing;
timing-invalid data produces an error. The reported trial alphabet is binary
detection/no-detection, aggregating fourteen pump pulses. These are documented
methods, not a certificate independently validated here.

The [official HTTP API documentation](https://random.colorado.edu/api-docs)
separately names `/curbyq/round/{round}/params`, `/data` and `/result` under
`https://random.colorado.edu/api`. It also describes retrieval by chain/pulse
content identifiers and by index. **Only the documentation was inspected;
no API endpoint was invoked.** Search indexing exposed this documentation;
direct web rendering returned the application's shell. Endpoint liveness,
payload fields and historical coverage are therefore unverified.

The [official client documentation](https://curby.gitbook.io/curby-js-client)
describes signature and causal-order checks, while explicitly excluding DIRNG
certificate/extraction validation from that client alone. The associated
[verifier README](https://github.com/buff-beacon-project/curby_verify) states
that execution fetches raw data; it was read, never executed. Author-client
repository metadata pins its inspected main to
[`95397f5e9fcc8ad57ef410c54473862e0b83bc59`](https://github.com/buff-beacon-project/curby-js-client/commit/95397f5e9fcc8ad57ef410c54473862e0b83bc59).
No software was installed or imported. The following additional review read
only source text at public commit pins; it invoked no client, server or route.

## 2. What `/params` actually means

The pinned [client method, lines 422–438](https://github.com/buff-beacon-project/curby-js-client/blob/95397f5e9fcc8ad57ef410c54473862e0b83bc59/src/dirng.ts#L422)
requires a result pulse, hashes the returned parameter text with SHA3-512
against that pulse's `paramsHash`, then returns unrestricted `JSON.parse`.
There is no closed response-field schema. Its seed validator consumes
`params.seed`; it does not validate apparatus timing.

The pinned [verification orchestrator, lines 135–182](https://github.com/buff-beacon-project/curby_verify/blob/ddcc8c61b195acf4689d81e480433fd35132423f/index.ts#L135)
distinguishes request-pulse `parameters` (entropy test) from fetched
`/params` (the `extract` command). It fetches raw Bell data separately and
adds it as `data`. This establishes extraction use; it does not establish that
an HTTP producer forbids additional undocumented keys.

| Surface / exact known field inventory | Meaning established by pinned source | Acquisition information established? |
| --- | --- | --- |
| `/params` extraction consumer: `seed`, `entropy`, `nBitsOut`, `errorExtractor`, `stoppingCriteria`, `isQuantum`; separately supplied `data` | These are the fields read by [`run_extractor`](https://github.com/buff-beacon-project/trevisan_python_interface/blob/a8becf7b656f878123fcc41b04093fa2efbc97d8/python/extractor_jobs.py#L160). | No window, clock uncertainty, skipped-attempt/order ledger or timing-certificate reference is read here. |
| Request precommit fields: `nBitsOut`, `nBitsThreshold`, `errorSmoothness`, `errorExtractor`, `epsilonBias`, `seedLength`, `stoppingCriteria`, `beta`, `isQuantum`, `pefs` | This is the explicit list in the [extractor-server README](https://github.com/buff-beacon-project/trevisan_python_interface/blob/a8becf7b656f878123fcc41b04093fa2efbc97d8/README.md). It concerns the entropy/extraction protocol. | `stoppingCriteria` counts analysis trials; it is not an independently measured live-time or coverage certificate. |
| Client linkage fields: result `paramsHash`; request `parameters`; Bell response `ref`, `dataHash`; precommit `dataHash` | Known object linkage and integrity checks in the client/orchestrator. | No documented link here to the physical certificate described in the paper. A Bell response match is not validation of that certificate. |
| Default extractor record layout: `SA`, `SB`, `OA`, `OB`, each `u1` | The [server's aggregate mode](https://github.com/buff-beacon-project/trevisan_python_interface/blob/a8becf7b656f878123fcc41b04093fa2efbc97d8/python/extractor_server.py#L7) specifies this consumer layout. | No timestamps, original trial-index field, gap/invalid flag or multiplicity field is declared in that layout. Stored order still needs a physical-attempt map. |

Two details prevent a false qualification. `entropy` is an input to extraction,
so the endpoint name does not promise purely pre-acquisition metadata. Also,
the extractor [can zero-pad a short outcome array](https://github.com/buff-beacon-project/trevisan_python_interface/blob/a8becf7b656f878123fcc41b04093fa2efbc97d8/python/extractor_jobs.py#L172)
to the requested analysis length. This is a software-contract observation,
not a claim that any published round was short. Its analysis length cannot
be adopted as proof of observed physical no-detections.

The inspected public surface contains no HTTP route producer or OpenAPI
closed schema establishing the complete `/params` body. The exact **consumer**
inventory above is verified by source inspection; absence of undocumented
extra HTTP fields is not proved. Nevertheless no required acquisition field
has positive support in this route, so its physical-calibration eligibility
is **NOT ESTABLISHED**, not “available pending download.”

## 3. Source eligibility matrix

Here **present** means documented at the indicated level. **Uninstantiated**
means that no exact source object has been admitted. **Not established**
means absent from the inspected evidence, not globally nonexistent.

| Requirement | New route: what is present | Exact missing input / decision |
| --- | --- | --- |
| Public authority and retrieval route | Author paper, official client, named archive; `/params` has a demonstrated extraction contract | The acquisition-certificate locator/schema remains unresolved. Historical round ID, immutable response/configuration IDs and byte custody are uninstantiated. |
| Same-run timing rather than neighboring-run transfer | Per-chunk certificate described in the methods | Obtain the certificate for one declared new round and its binding to that round; do not transfer validity to 2015 run3. |
| Observation-window definition | A fixed window is documented | Numeric endpoints relative to the trial marker, pulse indexing, units, closed/open endpoint convention and a justified uncertainty bound remain uninstantiated. |
| Attempt denominator and local adjacency | Per-attempt marker and binary trial alphabet described | Establish the map from original attempt indices to archived rows, gaps, acquisition boundaries and failed/invalid attempts; chain-pulse order is not physical trial adjacency. |
| Zeros and multiplicities | Binary no-detection is represented in the described alphabet | Prove that a zero corresponds to a covered physical attempt. Full registration multiplicity is not supplied by a binary outcome schema. A binary statistic needs its own explicit scope; it cannot silently replace NMC1's underlying alphabet. |
| Integrity and ordering | Public content-addressed audit route and client signature/order checks | A valid hash authenticates stored bytes, not missing acquisitions, detector live time or physical-window containment. Nothing has been verified here. |
| Physical source and port dictionary | A documented Bell apparatus | No map to the specified balanced five-site cold head, finite stencil, first cut, or eight marked gamma=1 ports is established. |
| Absolute source/output energy and error budget | No qualifying field established | Need independent launched coefficients, E_star in joules, input E_star*m/2, eight exported E_star*D values, gains/reference planes and bounded combined systematics. Wavelength or Bell efficiency cannot replace these. |
| Sequential TRC1 comparison | No qualifying field established | Need a declared source law and same-history or repeated-preparation interpretation, Gamma/q, retained state/reset and a prospective finite decision rule. No law follows from U alone. |

The gain is limited but useful: the published per-chunk certificate claim
identifies a different-source documentation target, while source inspection
rejects the tempting substitution of extractor parameters for that target.
The old run3 timing fault remains unresolved.
Neither cryptographic provenance nor a spacelike-separation certificate alone
proves the full timing/coverage premises of the proposed local statistic.

## 4. Two supporting locators, without widening access

| Locator | Exposed documentation/metadata | Disposition |
| --- | --- | --- |
| [NIST 2017 archive, DOI 10.18434/T4/1425490](https://catalog.data.gov/dataset/experimentally-generated-randomness-certified-by-the-impossibility-of-superluminal-signals) | The complete displayed distribution list has fourteen `.bin` objects, fourteen SHA-256 sidecars and the DOI link. No standalone README/configuration appears in that list. The catalogue labels the binary objects `text/plain`; that label is not permission to read outcomes. | Weaker than CURBy. No object or sidecar opened. The [associated methods](https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=922766) describe aggregated binary trials, not the required TWIST-J energy map. |
| [CORA replication archive, DOI 10.34810/DATA3116](https://dataverse.csuc.cat/dataset.xhtml?persistentId=doi%3A10.34810%2Fdata3116) | Indexed primary metadata names V1.0, publication 2026-03-16, two supplement CSVs and a separately listed `Readme.txt` (8.0 KB; publisher MD5 `1907fee6daa38e4da6d1f451291a781b`). The indexed licence is CC BY-NC 4.0. | Specific documentation lead; direct page/API readback failed. README contents, CSV columns and applicability remain unknown. No file or ZIP was opened; the publisher MD5 was not locally verified. |

The CORA filenames are recorded in the accompanying JSON solely as catalogue
metadata. Their names do not establish that they contain original trial
records or the missing timing certificate. Nothing from this archive should
be copied into Apache-2.0 repository content without a separate licence review.

## 5. Small next action that can decide this route

The next bounded documentation target is the separately listed CORA README
and the producer/schema of the paper's **per-chunk spacelike certificate**.
Require an actual locator for numeric window and coverage metadata before
proposing acquisition of any round. The `/params` semantic question is
settled at its known consumer scope and is not a reason to query rounds.
Do not use `latest`, browse results to choose a favorable round, or invoke
the verifier's automatic fetch. If the required configuration is only embedded
in outcome-bearing pulses or analysis containers, that requires a separately
declared custody/exposure scope before opening it.

Before selecting a concrete round, fix a metadata-based rule and preserve
failure. For example, after confirming a metadata-only ordering inventory,
choose its first request at or after a fixed UTC boundary in the authors'
documented demonstration period, regardless of its later success/failure;
pin its request/response IDs. This is a proposed selection procedure, not an
already selected or admitted round. Do not skip a timing-invalid request.

The next qualification question has a finite answer: **does that one bound
configuration supply a numerical observation window plus complete attempt
coverage and original order?** If yes, a separate NMC1 extension can be
specified and preregistered. If only binary trial data are available, decide
that limited observable explicitly and keep the multiplicity obligation open.
If not, report the specific missing field for this round. In either case the
eight-port energy test still needs its independent physical dictionary and
calibration; generic photonic data are not its realization.

## 6. Exposure and limits of this audit

The permitted surface was public papers/methods, catalogue entries, READMEs,
documentation, repository metadata and statically inspected author source.
The server README contains illustrative frequency/PEF arrays; those examples
were visible but were not evaluated or treated as an admitted dataset.
No detector file, archive member,
HDF5 object, pulse payload, raw-data endpoint, simulation or formal verifier
was opened or run. No contact/message was sent. Published aggregate results
and figure captions were incidentally visible while locating methods; this
is retrospective qualification, not blind empirical evidence. Earlier failed
2015 catalogue searches were not rerun. No public file or Git branch changed.

The accompanying `source-qualification.sources.json` records evidence levels,
URLs and missing fields; null content hashes mean no experimental bytes were
accessed or verified. All old O/H statuses and the run3 disposition remain.
