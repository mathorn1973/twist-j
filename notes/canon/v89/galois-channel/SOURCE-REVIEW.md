# Source review: Galois-channel intake

**NON-CANONICAL / PREPARATION ONLY / NO FORMAL EXECUTION.**
Review date: 2026-09-19. Proposed identifier
`P-U-GALOIS-CHANNEL-OPTIMUM-1` remains unreserved.

## Custody and authority

The attachment is an intake proposal, not an authority declaration,
public probe pin or authorization to promote its embedded claims.
The working authority is Public Canon v88 on public main
`e57d4506d5b28bf8cb4979c4e29db6b10b2441f2`. STATUS, POLICY, AGENTS,
CORE, FRONTIER and the inherited native-code proof were read before
scientific preparation. Global authority/check/collision findings belong
to the surrounding v89 intake record; this source review does not
substitute for a current formal preflight.

The two issue bodies and their custody comments were read through the
public GitHub API. The accepted object trees were freshly retrieved:

| Source | Accepted Git tree | Manifest blob | Inventory |
| --- | --- | --- | ---: |
| [#1037](https://github.com/mathorn1973/twist-j/issues/1037) | `dab9fef95df0b9a38bb1ae0009da691402ac97ef` | `4656a6f6fbb39ddea538f8b66e3e4197f9ba452e` | 8 files |
| [#1038](https://github.com/mathorn1973/twist-j/issues/1038) | `c456edcdc3c1abd6b8ac3443392c9241d0bf15dd` | `b3e1db9bd322ada80706a2b72b1722372c45b12e` | 9 files |

Every file was restored locally from the named public Git blob. For all
17 files, byte count and Git blob SHA-1 matched the corresponding tree;
every manifest-listed SHA-256 matched. Reconstructing each Git tree from
its ordered mode, filename and binary blob identity reproduced its exact
accepted tree SHA-1. The manifests themselves were checked by their tree
blob identities and also hashed below. This establishes custody, not the
scientific truth of the contained stdout.

| Source/file | Bytes | SHA-256 |
| --- | ---: | --- |
| #1037 MANIFEST.json | 2254 | `2ff730844b13a1b95fc02a100eb6b7fdb2c2ace658a59b2d09491400b1622fd9` |
| #1037 PROOF.md | 15765 | `4dac3f45f5a335926afdf15c67463eb73bd4e28eec5dc587c319896614367dcb` |
| #1037 audit.py | 8447 | `ea2d4149d6ff31eb6a27671270be3d58690ef058f82e2ab5fb481445a4c1bbd6` |
| #1037 stdout.json | 2386 | `de8f58d1e8e5b73183b34446cf0e95ae1cf6fcc34d6f68262d92f200d80ac8d5` |
| #1038 MANIFEST.json | 2644 | `d166e8d90a729eb994c6b7c375bb12cb23bb6243483272e76ee1f5617fef6a7f` |
| #1038 PROOF.md | 16199 | `c0ce7f4e72715f4642f9c4b74dd9fd4c8c43039b35c12c5ec9c14a3e6b46c3e7` |
| #1038 audit.py | 11405 | `5d76910bb1a4b993d14dcaad551a191baa14d50b99fcb5b1c031560a2b7642e6` |
| #1038 stdout.json | 7596 | `d13493857ae0492335a2b31f7a541cda8c4c4d7569124c8a610cef73de5346b5` |

Proof blobs are respectively
`f547538e496873de5147b02cec928f05e0e2b037` and
`a93d7d0241d31a4b00624c888953db00e87e130c`.
The complete source inventories also preserve both READMEs, preregistration
references, original RUN.json and empty stderr, plus #1038 REALIZATION.md.
They are kept as local source custody rather than copied as new evidence
records into this notes package. Neither source auditor was imported or
executed during this preparation.

The issue sources identify original proof/code as Apache-2.0. This intake
copies no external textbook or optical paper. The finite channel
representation is explicitly established in the new proof from the Choi
matrix and the finite spectral theorem.

## Mathematical review

| Review target | Finding and proposed scope |
| --- | --- |
| Unchanged code and complex extension | The public coefficients become C after alpha_a=sigma_a(A)/sqrt5. The four-column change of coordinates has positive Gram I4-ones4/5 and is invertible. Full complex source operators are admitted. |
| Common environment and cross terms | Exact transfer on all matrix units forces one common unit environment vector. F filling the entire output makes the complement orthogonal to that full output sector; this justifies complete cross-term removal. |
| Complete-class optimum | Positive effects and sixteen positive slacks give total agreement <=10 for every complex CPTP extension. Explicit Phi17 and Phi5 attain every raw agreement 5/8. No finite channel enumeration supports the universal assertion. |
| Equality in the bound | Vanishing of every positive slack restricts each effect to span_a q_ka. All diagonal and off-diagonal completeness blocks are required. |
| Complex off-block rigidity | Signed conjugation reduces all coefficient equations to the four simplex outer products. Their diagonal-value matrix is (8I4+ones4)/16, invertible over C with determinant 3/32. |
| Unique effects versus global channels | Optimizers have fixed rank-four complement effects. Phi5 and Phi17 differ at raw density entry(0,1), -1/8 versus +1/16, so global channel uniqueness is expressly false. |
| Auxiliary accounting | Projection of the complement dilation into each output coordinate maps into eta-perp. Rank four implies purified auxiliary dimension >=5; five Kraus operators attain it. |
| Required counter-controls | The four-auxiliary exact-code construction gives uniform raw output coordinates, so minimum five is conditional on optimality. The point-exact channel separately fails the coherent target. |
| U20 and factorization | Block multiplication proves full orthogonality. Loader/swap factorization gives all twenty outputs and the Phi5 dilation after explicit relabeling. Matched loader cancellation prevents interpreting matched-code agreement as an independent physical prediction. |

No mathematical defect was found in this review at the frozen comparison
scope. That is an analytical review finding, not accepted public T and
not a completed independent formal breaker. The broad apparatus,
terminal-event and instrument-family obligations remain unchanged.

The sibling reviewer additionally inspected the preregistration without
reading this new proof or verifier and recovered the same complex-block
independence argument. That review is result-exposed: the proposal and
inherited public mathematics were available, and there was no sealed
blind-breaker pin. Its separate review record defines the exact exposure
boundary.

## Draft contents and adaptations

- PREREG-DRAFT.md fixes the class, metric, two conclusions, controls,
  systematics, exact failure thresholds and missing formal sequence.
- PROOF-DRAFT.md is a self-contained mathematical synthesis of the two
  issue proofs. It includes the finite Kraus representation, explicit
  complex off-block proof, both controls, and complete U20 factorization.
- verify.py is a fresh combined Fraction auditor adapted from #1038,
  adding #1037's seventeen-Kraus construction, its full code/cross-term
  tests, all raw output densities, total-agreement certificate and
  point-exact control. It asserts the originally fixed phase-flip control
  exactly, retains the all-port factorization, and checks effect
  completeness. The native antecedent trajectory audit remains inherited,
  not re-imported as a new result.

The adapted verifier imports only fractions and json. It reads no files,
uses no subprocess or network, writes no files and has no floating-point
scientific arithmetic. Its candidate output describes finite certificates,
not earned public status. Static AST parsing succeeded; the file was not
imported or executed.

    verify.py bytes: 14428
    verify.py SHA-256:
    7fdcfefd748bc7f084d845faad665e0cab29b45ec89388c8b1e55d218af371b9

This hash is a preparation inventory item, not a public preregistration
pin. Any later draft edit requires refreshing it before acceptance.

## Readiness and remaining work

The source recovery, bounded statements, proof synthesis and static
verifier preparation are ready for public intake review. The following
are not complete: current formal ownership/collision reservation; accepted
public PREREG/verifier pin; scientific execution of this draft; required
byte-identical two-architecture replays; accepted result and independent
review disposition; sealed Canon fold and release activation.

No EXPECTED.txt, RUN.md or RESULT.md was fabricated. No source output
was relabeled as the new verifier's output. No Canon, registry, frontier,
gate, release pointer or existing probe was modified by this intake.

REALIZATION.md remains noncanonical engineering material. Its ideal
component interpretation, coarse/fine comparison and conditional
calibration bounds supply no measured tolerance, physical source
preparation, native interaction, occurrence, persistent record, reset or
physical cross-layer gate. Neither proposed mathematical claim changes
the public physical QDD owners.
