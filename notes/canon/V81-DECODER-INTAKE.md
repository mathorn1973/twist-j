# Public Canon v81 decoder intake

**NON-CANONICAL / FOLD RECORD / NO AUTHORITY.**

Date: 2026-09-08. Author of the scientific content: A. M. Thorn, in the
eight merged public probes and six incubation notes named below. This
document records how that content was folded into a Public Canon v81
candidate. Unlike the v80 r3 fold, no manifest was frozen before this fold;
the registry scope strings, falsifiers, dependency bases and Canon
condensations below were written during the fold from the merged proofs
and are exposed for review in the candidate pull request. The written
probe proofs, not the condensations, carry the universal quantifiers.

## 1. Basis

```text
public main            ea90a0e (merge of #902)
STATE                  ACTIVE
Public Canon           v80
activation commit      4577448dba85c492b27773a64e5fd557abc02b30
content commit         b00171ef21ecb0d905593224f66f5e8a0f6c28e5
CANON sha256           8b076ee3d940e4a3639d3ffca06ae86e7df69dfc87f90d06ea99d4f9fca6b66c
CANON bytes            541516
```

Between the v80 activation and the basis, public `main` added exactly eight
probe directories and seven notes files. No `canon/`, `STATUS.md`,
`README.md`, `CITATION.cff`, `POLICY.md`, `AGENTS.md`, `tools/` or workflow
byte moved. The fold therefore starts from the v80 content bytes on `main`
with no transport step.

## 2. Sources

Each merged probe is proof-first and result-exposed, ran once locally on
Linux x86_64 with exit 0 and empty stderr, and was reproduced on both
GitHub architectures with the aggregate check passing on its reviewed head.

| Probe | Lock | PR | Two-architecture run |
| --- | --- | --- | --- |
| P-BINARY-RECORD-QUADRATIC-SELECTION-1 | #885 | #886 | actions/runs/34153166259 |
| P-RECORD-OCCURRENCE-SYMMETRY-1 | #887 | #888 | actions/runs/34154929454 |
| P-RELATIONAL-GROWTH-SATURATION-1 | #889 | #891 | actions/runs/34156973318 |
| P-U-FINITE-READER-INDEPENDENCE-1 | #890 | #892 | actions/runs/34157199966 |
| P-SNAP-OCCURRENCE-IDENTITY-1 | #893 | #894 | actions/runs/34159964052 |
| P-SNAP-INTERACTION-READBACK-1 | #895 | #896 | actions/runs/34162404423 |
| P-REGISTRATION-PAIR-RECOVERY-1 | #899 | #900 | actions/runs/34166753111 |
| P-TRC1-END-TO-END-IDENTIFIABILITY-1 | #901 | #902 | actions/runs/34169382593 |

The incubation notes `C-RELATIONAL-READING-ARITY-N`,
`C-GEOMETRY-RELATIONAL-ACCUMULATION-N`, `C-SNAP-OCCURRENCE-IDENTITY-N`,
`C-REGISTRATION-PAIR-RECOVERY-N` and `C-TRC1-END-TO-END-IDENTIFIABILITY-N`
are the programme narrative; they authorize nothing and are not evidence.
`C-SNAP-PHYSICAL-REGISTRATION-N` is a retrospective external source audit
with no formal run; it contributes no row and is retained unchanged.

## 3. Registered rows

Eight theorem rows, all `T / L1 / THEOREM`, Canon section
`2. Time, space, and the decoder`, evidence `probes/<probe>/RESULT.md`,
evidence kind `PUBLIC_PROBE`, hash mode `bundle-manifest-sha256-v1`,
architecture requirement `two-architecture`, one `DECLARE` history event
each with `previous_status` `-`, release `canon-v81-candidate`, date
2026-09-08. The exact rows are the first eight lines after the header of
`REGISTRY.tsv`, `NORMATIVE.tsv`, `EVIDENCE.tsv` and `HISTORY.tsv`, in this
order:

| Claim | Probe | Scope SHA-256 |
| --- | --- | --- |
| TRC1-CALIBRATION-IDENTIFIABILITY | P-TRC1-END-TO-END-IDENTIFIABILITY-1 | `141b882d26ab044aa33f5849300a8116a3bd0f3b81691865773b7d9c212818f8` |
| REGISTRATION-PAIR-RECOVERY-INVERSE | P-REGISTRATION-PAIR-RECOVERY-1 | `b6157f57e07a8622e38ee313fcbaaf152f26c40b7eabc32aa5b1f039d22bc88b` |
| RECORD-LOADER-RETENTION-CLASS | P-SNAP-INTERACTION-READBACK-1 | `859548877d01a5b6a86dab558a12f9a8953885d324c5cc962685c9cff30ae896` |
| OCCURRENCE-ADDRESS-AND-LOG-EQUALITY | P-SNAP-OCCURRENCE-IDENTITY-1 | `2d516e5d40254967bcff70cc57532900ed1036d5700c5164db06f8356b2bbef5` |
| U-FINITE-READER-INDEPENDENCE-OBSTRUCTION | P-U-FINITE-READER-INDEPENDENCE-1 | `956e01781ad1f9ddaf0f3c2ed5534e075125e1b385cd0797ba62dc61e929e974` |
| RELATIONAL-GROWTH-SATURATION-BOUNDARY | P-RELATIONAL-GROWTH-SATURATION-1 | `f993d963f301a8b4434cfb30d79f357af401f7db8d2887307b4142976f310a7d` |
| RECORD-OCCURRENCE-SELECTION-CRITERIA | P-RECORD-OCCURRENCE-SYMMETRY-1 | `e96887bb3e9a8749536097b66c9e7b3574bf622a11e9816672e743af8352ed8b` |
| BINARY-RECORD-VALUATION-NONSELECTION | P-BINARY-RECORD-QUADRATIC-SELECTION-1 | `9051ade7f62600e0b60d6774c40237ca8d6fb0c0d49da5ad24e1237d19fae96e` |

Bundle manifest hashes of the eight probe directories, computed by
`tools/check_ledger_core.py::bundle_sha256` over the merged bytes:

```text
P-BINARY-RECORD-QUADRATIC-SELECTION-1   6bf433d1594b1ed19441033790f1ef0df7a5da17f68fd575c0d1a5521b9e11c9
P-RECORD-OCCURRENCE-SYMMETRY-1          65ce6a38beddbd27cd809b4ae505cf87dcf05bd04424a76647d9f74097f9dd46
P-RELATIONAL-GROWTH-SATURATION-1        0d1161f53fcfadedbc96ce104dd435de97f920ebe1e01ecb1de35528ebe2ec65
P-U-FINITE-READER-INDEPENDENCE-1        f92442e562b04743bcd1c77eae4c24143c72d9a172bf79207200eac502abf5b0
P-SNAP-OCCURRENCE-IDENTITY-1            7218d3848c5b089316eaa8a50ac919f12b9cf82fbf1c5f431b70f065afc90f7a
P-SNAP-INTERACTION-READBACK-1           d67d6cb185640e24430fa69dcbca22837b5230b00e762d38ba349cbeb4a47a9e
P-REGISTRATION-PAIR-RECOVERY-1          0277e3c0e8d6356836a3ce741b2ff02aa62cb2e088e4307e547ad738ab056725
P-TRC1-END-TO-END-IDENTIFIABILITY-1     28dde06306d6799f33ff0f8aabcdaad753f66866a6f8c2e65e9576aa02b9520e
```

Claim identifiers were chosen in this fold, since the probes and locks
proposed none. They name the theorem rather than the probe; the probe of
origin is recorded in every evidence and history row. The incubation
notes use "Snap" for the sought physical record event; the two rows drawn
from the SNAP probes are named for their mathematical content, because no
physical Snap is registered.

## 4. Dependencies

Twenty-nine rows, the first twenty-nine lines after the header of
`DEPENDENCIES.tsv`. Every `REQUIRES` target is an L1 theorem or the L1
definition `DEF-AUTONOMOUS-STATE`, so no dependency crosses a protocol
layer and no gate is created. Every `BOUNDED_BY` target is a MULTI-layer
open owner: `QDD-INSTRUMENT-APPARATUS`, `QDD-TERMINAL-EVENT-SEMANTICS` or,
for the growth boundary, `TRACEKERNEL-CURVATURE-FORCING`.

| Claim | REQUIRES | BOUNDED_BY |
| --- | --- | --- |
| BINARY-RECORD-VALUATION-NONSELECTION | QDD-CONDITIONAL-INCIDENCE-AND-SYMBOLIC-RECORD | APPARATUS |
| RECORD-OCCURRENCE-SELECTION-CRITERIA | BINARY-RECORD-VALUATION-NONSELECTION; QDD-INCIDENCE-FIRST-HIT-CLASSIFICATION | TERMINAL; APPARATUS |
| RELATIONAL-GROWTH-SATURATION-BOUNDARY | BINARY-RECORD-VALUATION-NONSELECTION; FIRED-COMMUTATOR-NOGO | TRACEKERNEL-CURVATURE-FORCING |
| U-FINITE-READER-INDEPENDENCE-OBSTRUCTION | DEF-AUTONOMOUS-STATE; U-NATIVE-CHART-AND-QDD-READBACK; U-FINITE-HISTORY-CLOCK-PHASE | TERMINAL; APPARATUS |
| OCCURRENCE-ADDRESS-AND-LOG-EQUALITY | U-FINITE-READER-INDEPENDENCE-OBSTRUCTION; RELATIONAL-GROWTH-SATURATION-BOUNDARY | TERMINAL; APPARATUS |
| RECORD-LOADER-RETENTION-CLASS | DECODER-RESERVOIR-RECORD-ACCOUNTING; BINARY-RECORD-VALUATION-NONSELECTION | APPARATUS |
| REGISTRATION-PAIR-RECOVERY-INVERSE | none | APPARATUS; TERMINAL |
| TRC1-CALIBRATION-IDENTIFIABILITY | DECODER-RESERVOIR-RECORD-ACCOUNTING; DECODER-RESERVOIR-QUADRATIC-PARTITION; DECODER-RESERVOIR-QDD-POSTPROCESSING-OBSTRUCTION; POINTED-DECODER-PREFIX-CONSISTENCY | APPARATUS; TERMINAL |

Two requirements the proofs invoke were deliberately not declared as
`REQUIRES` because they would cross a layer without a gate:
`QDD-SIMPLEX-PAIR-INCIDENCE` (L4), whose p=5 channel forms are instead
taken from the L1 owner `QDD-CONDITIONAL-INCIDENCE-AND-SYMBOLIC-RECORD`,
and `DEF-NATIVE-WORD-CURVATURE-CLASS` (L2), whose finite carrier bound is
instead taken from the L1 theorem `FIRED-COMMUTATOR-NOGO`. Both remain
cited in the Canon text.

## 5. Canon insertion

The body of `V81-CANON-INSERT.md` was inserted immediately before
`## 3. The kernel and the census`, after the v80 entries, with a single
blank line on each side. The five release-identity strings of `CANON.md`
were changed from v80 to v81. No existing Canon line was edited. The
generated views were regenerated by `tools/generate_canon_views.py`;
`CORE.md` gained one hand-written orientation paragraph after the v80
paragraph, and `CHANGELOG.md` gained the v81 entry.

## 6. Counts and hashes

```text
claims             406        normative items    455
T                  274        dependencies       773
D                   45        evidence           406
C                   39        history            939
H                    2        gates               15
O                   28        frontier programs    8
F                   18        live H/O            30

evidence architecture   none 50   one 9   recorded-audit 31   two 316
architecture map        direct 182   transitive 265   terminals 63
```

Direct architecture requirements are unchanged. Seven new theorems reach
the architecture transitively through registered native rows; the renewal
inverse declares no requirement and is not a terminal because it declares
owner boundaries.

```text
canon/CANON.md       568924 bytes
                     940e1d192f729c16fcb74b6e6ac1b8f02d1050326b6164affb276684c8696fbf
canon/CORE.md        6788bcc2f7e69c84083638b992c07c43986de6fa7f294e55015805c8cd69eae0
canon/FRONTIER.md    428a97bb24f10f25fa700a32f053f774a2b63316feaebd98c495540de6d31cd4
canon/REGISTRY.tsv   ce8906de1b427d0b79714a2abece6d8b7efe5f74ebd53ec46f8b195373a354eb
canon/CHANGELOG.md   8610dca0609b943b4c120e02f2a2e076da12d7469b19eb9ff08d1a25ca53b8b3
```

`FRONTIER.md` is byte-identical to v80: no H or O row moves.

## 7. Physical firewall

`QDD-INSTRUMENT-APPARATUS`, `QDD-INSTRUMENT-CLASS-COMPLETENESS` and
`QDD-TERMINAL-EVENT-SEMANTICS` retain byte-identical registry, normative,
evidence, frontier and history rows and remain `O / STOP`. Every one of
the eight results is L1 mathematics whose own result file declares the
physical Snap, occurrence, apparatus and geometry questions
STOP-DEFINITION. The fold registers exact boundaries, counterexamples and
conditional constructions; it registers no physical effect, apparatus,
event equality, occurrence law, sampling law, persistence or reset law,
spatial dimension or L6 measure, and no gate.

## 8. Maintenance

`reproduce/status-separation/verify.py` gains the outermost
`V81_LEDGER_PATCH` layer, chained into the unchanged v80 and v79
reconstructions, the updated count anchors, and two checks,
`V81-PRIOR-LEDGERS` and `V81-DECODER-BOUNDARY`; it reports 79/79.
`tools/test_architecture_map_report.py` anchors the new counts and asserts
the architecture-map membership of all eight rows.
