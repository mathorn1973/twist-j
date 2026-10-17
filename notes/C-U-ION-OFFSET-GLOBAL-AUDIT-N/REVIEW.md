# Review of the fixed unequal encoding audit

**NON-CANONICAL.** Analytical and repository review only; no new formal
scientific run, experimental result, status promotion or physical certificate.

Reviewed substantive document: [README.md](README.md), 16344 bytes,
SHA-256 `5b0d4e1ad866e5c176bbefba328934e79ecca0af983719135ece061895c7074a`.
The source basis is public main
`2973a432303e046aacb2cee3cea97254ea3ab8eb`, with #1361 read at
`9f3586dca75d0c74b021d992e4f81bf7b7f3e8de` and #1359 at
`8f43a051e3dba8cc4ed17d379ad8e11b57101591`.

Three independent agent review passes examined the mathematics, physical
accounting, and policy/provenance. Reviewers had the sources and earlier
derivation; this was not blind reproduction. The mathematical reviewer
checked the final hash above. The physical and provenance reviews requested
the clarifications below, which were incorporated before that final review.

## Findings and disposition

| Review | Check | Disposition |
| --- | --- | --- |
| Mathematics | K fixed from preparation, five transformed generators and shifted selector | Correct by direct substitution |
| Mathematics | Both actual contacts, generic contact scope, pre-contact path and n=9 classes | Correct; no claim of generic SWAP |
| Mathematics | Complete 25-history correspondence | Induction establishes it without a new enumeration |
| Mathematics | Unchanged W, translated retention set and inherited collision multiplicities | Correct; remainder bound keeps its pure-code/reversible hypotheses |
| Physics | Exact five-level labels and changed preparation | Consistent with the adopted Hrmo level dictionary |
| Physics | Matched-spectrum contact cancellation and whole-history energy differences | Correct within the stated endpoint assumptions |
| Physics | General fixed Hamiltonian versus additive bare-data energy | Clarified: H_data=sum_i H_i at detached boundaries is required for the f(q) identity |
| Physics | Meaning of evolution supplying excitations | Clarified: physical implementation of contact-free native evolution, not unforced bare-ion evolution |
| Provenance | Basis-label permutation versus coherent SWAP | Clarified: phases and remainder action need their own gate contract |
| Provenance | Three source hashes, lengths and relative links | Match the actual stored inputs; no source verifier executed |
| Scope | Algebraic consistency versus physical realization | Separated throughout; physical HOLD retained |

No remaining blocking error was identified at the reviewed analytical
scope. This does not establish pulse synthesis, actual resource inheritance,
finite common physical times, or archive error bounds.

## Repository validation

Local checks on the notes-only candidate:

```text
python tools/check_policy.py          POLICY PASS
python tools/check_canon.py           CANON PASS v97 claims=492
python tools/check_ledger.py          LEDGER PASS
python tools/check_gate_contract.py   GATE CONTRACT PASS
python3 -m unittest discover -s tools -p 'test_*.py'
                                     172 tests, OK (Linux)
```

These validate repository structure and existing infrastructure; they are
not a new scientific test of the ion candidate. The unit suite's deliberate
failure-fixture messages do not denote a failed scientific probe. Required
public architecture and aggregate checks are read from the PR's exact head,
not inferred from these local results. A notes-only diff introduces no
changed scientific verifier to replay.

Only this note directory is proposed. The Canon, registry, workflows,
previous probe and #1359 audit remain unchanged. Security review found no
credentials, private addresses, private logs, binaries, or third-party
source copies in the two new Markdown files.
