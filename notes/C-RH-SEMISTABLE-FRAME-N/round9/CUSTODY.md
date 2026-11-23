# Round 9 custody

NON-CANONICAL. No authority. One x86_64 lane.

## Pins

- Public authority basis: 93c36089db57032a6cbca482ff62c95884567d0f.
- Prior delivery: e3350f8951cc2a61b3ae3af9e377c44663e10387.
- Local preregistration: 8fbaf717d94a56dedad75ab6d5a3684dbee62b9b.
- Public preregistration, exact identical tree: d598aedb1658f00af9196aedba8944dd6205f533.
- PREREG.md SHA-256: 4da279d9c4ea6457b04e465c165bed937358c43c536178cbc6905e8e18f65f59.
- Development author freeze: c215fec580b132954c1dc786eff73d292790f26e.
- Blind opponent author freeze: 3c7e1e9332b7c384fe20431a7ed68f5adcc12bbe.
- Combined local code and draft proof: e5d27f948dbef7b97c0d5296481044f4f1f0085c.
- Public execution pin, exact identical tree 44f0aada1a60b8b5ce4a34538082f01d5517c628: b83250a7db82d2a27de932617fb39f61cf6af823.

Both programs and the contract were remotely read back byte-for-byte before either scientific execution. The two authors wrote from the frozen contract, in separate worktrees, without reading one another's programs or outputs. Both froze before comparison.

Correct hashes of the frozen program bytes:

- verify_r9.py: 73f36c06df3084af2bfd012a85b1e3bf9a2e938959e3be7752863f2e8eb5f37d.
- break_r9.py: 4abf263516945c9b3bc131299b18f9cbd98e03194ce7fe27942697964ae71b14.

## Preserved pre-execution stop

The first development-driver attempt stopped at its hash assertion BEFORE starting Python on verify_r9.py. Its literal was the malformed 65-character string:

    73f36c06df3084af2bfd012a85b1e3bf9a2e938959e3be7752863f2e8eeb5f37d

The diagnostic was AssertionError at driver line 12. No verify_first artifacts existed and no development scientific program had executed. Root stopped that launch and compared the original author commit, public execution pin and working file: all three were exactly 20,765 bytes with the correct 64-character hash listed above. Thus the discrepancy was an extra letter in the driver's transcription, not a changed source or frozen artifact.

Only that malformed driver literal was corrected. The contract, program, execution pin, mathematical cases and expected results were not changed. This is not a repaired scientific rerun; the next successful launch is the program's first execution. The blind opponent's separate first run completed successfully during that attempted parallel launch and is preserved without rerun.

## Execution records

Scripts are materialized directly from git show at the public execution pin into separate temporary directories, checked by SHA-256, made read-only and invoked by Python with isolated mode. Each has a 180-second wall limit. The six preregistered first-run files preserve output, errors, exit status, architecture, Python version, immutable pin and elapsed nanoseconds.

Actual final outcomes and output hashes are reported in RESULTS.md. Subsequent proof wording corrections are editorial/mathematical review changes; they do not alter the frozen programs or contract.

## Authorship and delivery

Local commits use A. M. Thorn <thorn@twistj.com>. As in round 8, the authenticated connector transports exact Git trees but exposes no author-email override. Its remote commits use the connected account's no-reply address. Local and remote commit objects are distinguished above; identical trees and file readbacks establish content custody.

No Canon, registry, workflow or release was changed. The round 8 frozen scientific evidence is unchanged. Repository validation is separate from the single-architecture scientific checks.

The full round-9 Git whitespace diagnostic reports one terminal blank line in the already frozen PREREG.md (line 128). It is preserved with the published hash. This is a formatting diagnostic, not a scientific falsifier; the frozen contract was not rewritten to remove it. The final delivery delta after the execution pin is checked separately for whitespace.

## Static repository validation

The repository's own tools returned POLICY PASS and CANON PASS v116 claims=634. The final staged delivery delta passed git diff --cached --check. The public main and PR base were freshly read before packaging and remained 93c36089db57032a6cbca482ff62c95884567d0f. The PR was open and draft; it was not merged.

These are repository integrity checks, not additional scientific executions or a second architecture lane.
