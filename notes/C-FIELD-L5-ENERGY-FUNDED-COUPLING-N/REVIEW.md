# Independent implementation, proof and scope review

PUBLIC / NON-CANONICAL, L1. Review supports a candidate, not Canon authority.

## Review before the joint code pin

The primary author read the frozen definitions and wrote verify.py. A fresh
challenger author received only frozen PREREG and the public base rules and
wrote break.py without access to primary, PROOF, predecessor programs or
execution output. The challenger declared its source ready at SHA-256
`d581ab780dc74b053ac51220df87c6adb6ed67af2429b4480dae892b76e5e89f`.
The primary author first read that source after the joint public code pin.

A separate reviewer inspected primary and PROOF without reading break.py.
It found no blocking defect in the raw energy matrix, inverse shear,
integer split/image guards, zero-field funding, actual charged account,
complete inverse, frozen finite fixtures or recurrence proof.

The proof author then statically reviewed break.py without reading primary.
It found no blocking defect: all required fixtures were present, the independent
modulo-five/N certificate gave a valid alternative image proof, and the direct
field updates and flat state agreed with the frozen contract. No reviewer
executed or imported scientific code or performed scratch numerical runs.

One harmless witness difference was checked explicitly: PROOF demonstrates
branch-conflation failure at zero field with resource two, while primary uses
resource zero. Both give identical projected inputs with different projected
outputs and establish the stated information-loss boundary.

After the reviews, the primary's period loop was statically limited to exactly
ten updates (states k=0 through10); no eleventh uninspected step is computed.
AST parsing passed. All scientific files were then committed together in
`9645330e26e4dcae91d5db019c8a7145e9c0004b`, pushed and read back.

## Execution and scope

After the public joint pin and first execution, the challenger author also
cross-reviewed primary, PROOF and the bridge. It found no material correctness,
scope or security issue, specifically checking all-carrier rejection behavior,
the full energy account, actual D, nonsplit/image invariance and the period-ten
proof. This later cross-review is separate from independent authorship before
the pin. It made no edits and performed no further scientific execution.

The unchanged runner's first local execution passed both independently authored
implementations with exact output identity, exit zero and empty stderr.
The universal claims rely on the full proof and exact certificates, not merely
the finite fixtures. Public two-architecture replay is still PENDING and must
be recorded from actual job logs before final acceptance.

The result's period-ten boundary, full spectator/resource accounting,
pointwise charge preservation, literal state equality and chosen architecture
were reviewed explicitly. It does not promote the unmerged predecessor,
replace the old law, assert multicell transport or discharge any physical gate.

## Security and repository boundary

The public payload consists only of one notes candidate and its minimal
standard reproduction. Scientific code is standard-library-only, with exact
integer/rational arithmetic. The primary reads six named public source files
for hash checks; the thin bridge reads and executes only its three hash-bound
local inputs. The challenger does not read files, spawn processes, use the
network or write files. Success emits only the specified deterministic lines.

No private paths, credentials, archival payloads, binaries, caches or external
dependencies are included. Canon, sealed probes, checker rules, workflows,
release records and other owners' files are untouched. A separate final
diff/manifest check binds the delivered files to the frozen source pin.

The unchanged local policy, Canon, ledger and gate-contract checks passed.
The repository unit suite passed 172 tests with one platform skip on Windows
Python 3.12; its deliberate failing-checker fixtures are successful unit tests,
not failures of this candidate's scientific execution.
