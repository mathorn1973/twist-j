# Exact field-window successor audit

PUBLIC / NON-CANONICAL incubation, L1. Authority: none.
Scientific candidate: ../../notes/C-FIELD-CYCLOTOMIC-WINDOW-AUDIT-N/.
Owner/reservation: A. M. Thorn / codex-field-cyclotomic-window-audit-20260930,
issue #1303. This is a minimal reproduction for that one candidate.

The predecessor #1301 / #1302 has a preserved failed primary implementation;
it is neither executed nor repaired here. The new primary explicitly adapts
that public source, while the new challenger is independently authored from
the frozen preregistration without either primary, old breaker, proof or
outputs. Targets and predecessor defects were already exposed.

## Frozen inputs and source closure

Preregistration commit: 08e8acbc0390256571263f211e023391f2eaee93.
PREREG SHA-256: c1d6585c03c703948d7ebafd98af4fddff8d456a2947d95b8e5c252d0c4b893c.
Base authority: b8ba1a07ad776cdd8d878fe0a407e07312c0e263, Public Canon v95.

The bridge's literal guards bind the notes PREREG.md, verify.py and break.py
to their exact bytes. It calls the two scripts sequentially with stdlib
runpy, without sharing their scientific implementations. The primary also
checks the six public source hashes listed in PREREG (Canon, registry,
evidence, dependencies, gates and composition plan). No private input,
network access, external package or historical checkout is needed.

The independently reviewed PROOF.md supplies universal arguments and all
integral matrices; finite checks alone do not prove the general theorem.
Both implementations, this bridge, README and EXPECTED are frozen together
before their first execution. The complete code commit, file hashes and
observed run evidence are recorded afterwards in the candidate's RUN.md.

## Prospective stdout and unchanged execution

EXPECTED.txt is the literal five-line success target specified in PREREG,
committed BEFORE execution. It is not a claim that a run already happened.
Each implementation emits its success line only after every assertion
passes; the bridge's final line requires both implementations to complete.
Only the observed unchanged repository runner can establish equality.

From the repository root, with the new reproduction committed:

```text
python3 tools/check_reproduce.py --base b8ba1a07ad776cdd8d878fe0a407e07312c0e263
```

The existing runner owns deterministic environment, the shared 120-second
budget, exit-zero and empty-stderr requirements, and exact stdout comparison.
The bridge copies none of those runner rules. Local declared environment is
Ubuntu22.04 x86_64 / Python3.10.12. The unchanged pull-request workflow runs
this same source and expected output on Python3.12 x86_64 and aarch64.
Both jobs must report REPRODUCE PASS for this identifier and identical
wrapper/stdout hashes; green notes-only CI would not be sufficient.

## Scope

Exact finite C5 carrier, saturated active lattice and cyclotomic module,
L5 energy/index/image/inverse, all625 image residues, all625 gluing
residues, actual D charges, both predecessor regressions and the declared
zero/rectangular/rank-deficient/critical/unstable negative controls.
The candidate proof distinguishes inherited v95 results, new conditional
construction and false overextensions. No whole-shell bijection, full-lattice
integer charge-preserving extension, completed reaction, physical claim or
Canon promotion is inferred. Any mismatch stops this frozen audit and is
preserved; a correction requires a separately named and pinned successor.
