# NIST calibration qualification for the first v81 closure step

**NON-CANONICAL / DOCUMENTATION AUDIT / STOP_PHYSICAL.**
Date: 2026-09-08. Repository basis: ACTIVE Public Canon v81, public main
`82d536a71025032d6dd4093db61ecb9f31990250`.
Definition/source lane: [#834](https://github.com/mathorn1973/twist-j/issues/834);
calibration-definition lane: [#830](https://github.com/mathorn1973/twist-j/issues/830).
Scientific owner: `QDD-INSTRUMENT-APPARATUS`; shared apparatus-definition
surface: [#539](https://github.com/mathorn1973/twist-j/issues/539).
This note creates no formal probe, physical certificate, accepted hypothesis,
dictionary, owner closure or Canon change.

**Disposition: SOURCE_NOT_QUALIFIED_FOR_THIS_TEST** under the inspected public
documentation. This applies to the proposed Alice run3 prefix/local setting-0/
single-window lag-one test below. The bounded search found no independently
exposed same-run metadata locator supporting its required timing/window/coverage
premises. The current HDF5 catalogue has no run3 entry, while run3 has an explicit
unsuccessful timing-correction warning. The existing archival reconstruction
remains valid at its scope. Broader archive possibilities remain open; this is
neither global metadata nonexistence nor physical model falsification.

## Evidence actually available

The primary [NIST archive notice](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data)
still describes a mutable, best-effort collection with potentially incomplete
metadata. Its 2025 page-update date is not a run/version pin. This audit read
public methods and catalogue pages; no experimental object, HDF5 dataset,
analysis archive or unread run tail was downloaded, opened or decompressed.
No scientific verifier was run. Published conclusions, aggregate tables returned
with the methods, and earlier prefix diagnostics are known exposure; this is
retrospective qualification, with no new outcome statistic.

At the pinned repository basis, the
[NMC1 JSON](https://github.com/mathorn1973/twist-j/blob/82d536a71025032d6dd4093db61ecb9f31990250/notes/NIST-MEASUREMENT-CONTRACT-1.json)
still has an empty certificate bundle and `physical_profile_ready=false`.
Its admitted record extents are Alice/Bob `00_03_find_sync.T1/T2.dat` in full
and exactly the first 1,048,576 rows of each literal run3 member:
`00_44_CH_pockel_100kHz.run3.alice.dat` and
`00_43_CH_pockel_100kHz.run3.bob.dat`. The existing
[qualification result](https://github.com/mathorn1973/twist-j/blob/82d536a71025032d6dd4093db61ecb9f31990250/probes/P-NIST-RAW-RECORD-QUALIFICATION-1/RESULT.md)
and [local adapter result](https://github.com/mathorn1973/twist-j/blob/82d536a71025032d6dd4093db61ecb9f31990250/probes/P-NIST-LOCAL-OBSERVED-INTERVAL-1/RESULT.md)
establish record ownership, multiplicity and the stated one-hot predicate.
They establish neither complete physical trials nor no-detection coverage.
Different station totals are not paired trial counts. Compressed-object hashes
do not extend semantic qualification to unread tails.

The inspected primary documents give concrete apparatus information:

- [NIST format description](https://www.nist.gov/document/bell-test-data-file-folder-descriptions),
  version 2015-12-23, pp. 1-4: nominal 78.125 ps ticks, common 10 MHz reference
  with different clock origins, approximate PPS jitter/jumps; run3 timing was
  not corrected properly. HDF5 processing metadata is described as carrying
  alignment skips, anomalous syncs and window delays/radii; `cw45` lacks its
  full window definition. Separate T1/T2 files are described as clock-training
  material, without a run3 validity certificate.
- Shalm et al., [Phys. Rev. Lett. 115, 250402 (2015)](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.115.250402),
  pp. 3-5: a pumped optical source, polarization analyzers and SNSPD outputs
  recorded by time taggers; measured system efficiencies and background
  estimates, rather than an ideal detector. The apparatus has a 79.3 MHz pump,
  a 99.1 kHz trial trigger and approximately 200 ns Pockels-cell gates. Fifteen
  optical slots in this description and sixteen storage bits in the archive
  schema require an explicit indexing map. Neither clock is a U/TRC1 clock.
- [Supplementary material](https://journals.aps.org/prl/supplemental/10.1103/PhysRevLett.115.250402/LHFSupplementary.pdf),
  sections II and II F: measured optical/electrical latencies, with a 400 mV
  time-tagger trigger for SNSPD output and system latencies
  `49.9 +/- 0.5 ns` (Alice), `44.5 +/- 0.5 ns` (Bob). These are genuine
  documented calibration measurements. The uncertainty treatment includes
  quadrature addition under an uncorrelated-error assumption; it does not
  supply NMC1's same-run bounded joint certificate automatically.
- [Historical processing flow](https://s3.amazonaws.com/nist-belltestdata/belldata/code/analysis/DataProcessingDescription.pdf),
  2015-12-23: common-PPS alignment, apparatus-fault handling and simultaneous
  setting coarsening were analysis choices. Their provenance must be retained;
  they are not silently adopted by NMC1.

Current catalogue readback resolves an important ambiguity. The
[processed catalogue](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data/repository-bell-test-research-2)
lists HDF5 objects beginning with `01_11_...run4.afterTimingfix`, followed by
`02_54_...run4.afterTimingfix2` and later runs, but no run3 HDF5 object. The
[code catalogue](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data/repository-bell-test-research-0)
lists a 750.7 MB analysis archive and small acquisition archives; it does not
expose a separately linked run3 YAML file. These are absences from those
inspected catalogues, not proof that run3 metadata is globally unavailable.
No contents of the analysis archive were inspected. The
[2017 addendum](https://s3.amazonaws.com/nist-belltestdata/belldata/File_Folder_Descriptions_Addendum_2017_02.pdf)
explicitly adds later formerly blind data and the `02_54` HDF5 object; it does
not identify a run3 calibration object. Later-run metadata cannot certify run3
without an independently supported transfer of validity.

## Why these measurements do not yet fix TRC1

The pinned [TRC1 contract](https://github.com/mathorn1973/twist-j/blob/82d536a71025032d6dd4093db61ecb9f31990250/notes/TWISTJ-REALIZATION-OCCURRENCE-CONTRACT-1.md)
requires one prepared head and fixed `c=(Gamma,q,N)`, followed by retained
state evolution. Its physical observation equation is an obligation, not a
map obtained by renaming foreign packets.
The following are qualification inferences under those TRC1/NMC1 obligations;
they do not attribute TWIST-J claims to the NIST authors.

| Required identification | Evidence provided and precise missing step |
| --- | --- |
| `Gamma` and marked port/site | Optical efficiencies characterize response in the reported apparatus. They are not TRC1 conductances. No inspected source supplies the physical port variables, their units/normalization or a measured response corresponding to the signed warm-port relation `b/A=(2-g)/(2+g)`. Identifying `g` from target click frequency would be circular. |
| Heat threshold `q` | The supplementary 400 mV trigger identifies an electrical discrimination threshold. TRC1 uses accumulated reservoir heat divided by an energy threshold. A calibrated energy/voltage transfer, impulse and integration law, gain/threshold uncertainty and ordinal-to-registration map are missing. Photon wavelength alone supplies none of these. |
| Physical clock and horizon | Pump pulses, trigger trials and recorded sync intervals are distinct. No independently supported correspondence selects which is one TRC1 update, fixes `N`, or establishes same-run validity, window endpoints and candidate containment. Earlier sync measurements and the published timing diagram do not repair run3 by themselves. |
| Finite head family, ensemble and calibration matrix `A` | Optical preparation and reported response measurements do not assign U heads or their probabilities. No independently available head-discriminating row on a fixed admitted head family has been identified in the inspected sources. A polarization setting label is not a source-indicator row. |
| Complete denominator and no-detections | The archival partition conserves recorded rows. Missing trials, loss/live boundaries, uncertainty-aware window membership and registration latency/order remain uncertified. An empty packet interior is not a covered physical no-detection. NMC1 requires coverage even for positive registrations. |
| Response, retained memory and reset | Published efficiencies, background and latency measurements are useful partial evidence. They do not identify the source-dependent sequential response, recovery/afterpulsing bounds, post-state or TRC1 retained tape. The inspected documents provide no complete run3 reset certificate. Repetition of optical trials is not proof of a fresh TRC1 preparation or its disabled-reset contract. |

For the ensemble problem, the
[sealed TRC1 identifiability proof](https://github.com/mathorn1973/twist-j/blob/82d536a71025032d6dd4093db61ecb9f31990250/probes/P-TRC1-END-TO-END-IDENTIFIABILITY-1/PROOF.md)
already decides what would suffice: on the same finite head family, the desired
prediction rows `B` must lie in `rowspan([1;A])`. The actual-chain `e0/e1`
witness has equal scalar QDD calibration but different crossing predictions.
Adding an assumed source-indicator row proves algebraic sufficiency only.
The next physical calibration must name a measurable distinguishing procedure
and its independent head interpretation; copying the model's indicator is not
that procedure. With uncertain calibration, retain the whole compatible mixture
and context set and its prediction range, rather than selecting a fitting point.

## One narrow target and the next admissible action

Select **Alice run3's already exposed prefix, local setting 0, a single
metadata-defined observation window, and lag-one registration dependence**
as the first qualification target. Alice is the first station in the existing
source inventory; the existing prefix avoids selecting a new run by outcomes.
Setting 0 has a documented Pockels-cell-off interpretation in the paper. The
local scope uses the documented local trial trigger and avoids requiring
cross-station alignment for this first target. It still requires same-run
local timing, apparatus activity and coverage. No numerical window or pulse
slot is chosen from detector timing histograms; failure to identify one from
independent documentation retains STOP.

The proposed single ordered statistic is

```text
S11 = sum over k in I of 1[Y_k >= 1 and Y_(k+1) >= 1].
```

Here `Y_k` is the full registration multiplicity in the fixed window of physical
trial k. `I` consists of adjacent physical trial indices inside the independently
certified contiguous scope, with setting 0 at both trials. It is not adjacency
after filtering a click list or joining separated setting-0 trials. Record
`|I|`, the whole attempt ledger, every excluded setting pair, invalid attempt
and unresolved gap. A required unresolved timing/coverage premise prevents a
physical statistic; do not delete it and renormalize. Zero and multiple counts
remain in the underlying alphabet. This is a proposed statistic form, not a
completed preregistration, test result or p-value.

Comparing `S11` with TRC1 additionally requires a justified map from the two
physical trials to two cuts of the same prepared TRC1 history, or a separately
specified law on repeated preparations. Those are different models. The
once-selected ensemble cannot be resampled at every trial by implication.
Fix the dependence law, uncertainty propagation, finite rejection rule and
error allocation before any evaluation. The supplementary Bell test's
memory-robust bound concerns its own local-realism null and statistic; it does
not calibrate the distribution of `S11` or establish an iid source.

## Completed bounded metadata availability record

The search on 2026-09-08 was confined to independently exposed NIST catalogue/
documentation pages and the Bitbucket repository name explicitly referenced
by NIST. No archive or outcome-bearing member was inspected. Search-engine
absence is recorded only as failure to discover a locator on this bounded pass.

| Checked public surface | Exact inspection/search scope | Disposition |
| --- | --- | --- |
| [NIST repository index](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data/repository-bell-test-research) and [code catalogue](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data/repository-bell-test-research-0) | Exposed document/code/configuration links, including the analysis and acquisition sections | The PDF and three ZIP archives are listed. No standalone run3 YAML/configuration or author-repository URL is exposed here. ZIP contents remain uninspected. |
| [Raw catalogue](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data/repository-bell-test-research-3) and [compressed catalogue](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data/repository-bell-test-research-1) | Literal Alice `00_44_...run3` and Bob `00_43_...run3` names; adjacent synchronization/configuration links | Raw run3 archives and distinct sync archives are listed. No exposed same-run calibration/configuration locator was identified. No inference of timing validity from neighboring filenames. |
| [Processed catalogue](https://www.nist.gov/pml/applied-physics-division/bell-test-research-software-and-data/repository-bell-test-research-2) and [2017 addendum](https://s3.amazonaws.com/nist-belltestdata/belldata/File_Folder_Descriptions_Addendum_2017_02.pdf) | Complete exposed HDF5 listing and named additions | No run3 HDF5 entry. Listed later-run objects are not substitutes. |
| [NIST documentation](https://www.nist.gov/document/bell-test-data-file-folder-descriptions), with NIST-domain search | Queries `site:nist.gov "00_44_CH_pockel_100kHz.run3" yaml`, `site:nist.gov "00_43_CH_pockel_100kHz.run3" config`, `site:nist.gov "run3" ("yaml" OR "yml" OR "configuration")`, and `site:nist.gov "build_file_txt.py"` | Returned relevant primary hits were the known catalogues/format description. No separately exposed run3 YAML/configuration locator was discovered. |
| NIST's named Bitbucket `bell_analysis_code` lead, grounded in the [format PDF](https://www.nist.gov/system/files/documents/2016/10/27/file_folder_descriptions.pdf) | `site:bitbucket.org` searches for exact `bell_analysis_code`, `build_file_txt.py`, and each full run3 stem above | No matching author-repository/configuration locator was returned. The PDF names a repository but supplies no resolved URL; no repository ownership or path was guessed. |

This completes the bounded availability decision for #834: **do not open a
physical `S11` evaluation on the selected prefix**. Its source qualification
is negative under the inspected documentation, while physical use remains
STOP. Advancing this exact target requires genuinely new independently
applicable evidence, not another pass over the same catalogues. If metadata
must instead be recovered from a mixed analysis ZIP/HDF5 container, first
define and publish its separate custody/semantic-access scope; that is outside
this completed audit. No message to NIST was sent.

Even successful timing metadata would leave the `Gamma/q` and source-head
identification discussed in the #830 definition lane unresolved under the
scientific owner `QDD-INSTRUMENT-APPARATUS`. A different run requires an
explicit source choice from documentation and its own custody/exposure
disposition. No negative theorem about NIST, its Bell result, all physical
TRC1 realizations or evidence elsewhere is claimed.

The [earlier discovery note](https://github.com/mathorn1973/twist-j/blob/82d536a71025032d6dd4093db61ecb9f31990250/notes/DECODER-OPEN-DATA-BRIDGE-1.md)
and [manifest](https://github.com/mathorn1973/twist-j/blob/82d536a71025032d6dd4093db61ecb9f31990250/notes/DECODER-OPEN-DATA-BRIDGE-1.sources.json)
remain historical source proposals. This qualification advances their
availability question without promoting their unadmitted sources. The
[NMC1 definition](https://github.com/mathorn1973/twist-j/blob/82d536a71025032d6dd4093db61ecb9f31990250/notes/NIST-MEASUREMENT-CONTRACT-1.md)
and all physical owner statuses remain unchanged.
