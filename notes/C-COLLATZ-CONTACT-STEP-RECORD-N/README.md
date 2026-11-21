# A finite contact Collatz step with two retained depth records

**NON-CANONICAL / L1.** Candidate-T mathematical construction and candidate-C
finite exact evidence. Public lock: [issue #1860](https://github.com/mathorn1973/twist-j/issues/1860).

One fixed word of **18,280 literal relative contacts** on **49 slots**, with
conserved account **98**, performs two successive accelerated Collatz steps
for each odd initial input 1..15. It writes their ordered division depths
into two archives. The third identical word skips arithmetic and preserves
both archives at its boundary. Every work register is ready again; the old
source value is cleared rather than retained as hidden work data. The full
primitive inverse restores every initial slot.

This is a supplied finite truth-table program in an ordinary binary code.
The input/output code and common auxiliary preparation are independent of
the desired answer, but the rule being compiled is explicitly Collatz.
This proves finite contact programmability, not that J selects that rule,
an unbounded Collatz algorithm, original-native-U realization, physical
energy, measured time, occurrence, or global convergence.

## Exact finite scope

| Initial input | After two steps | Ordered depths |
|---:|---:|---|
| 1 | 1 | (2,2) |
| 3 | 1 | (1,4) |
| 5 | 1 | (4,2) |
| 7 | 17 | (1,1) |
| 9 | 11 | (2,1) |
| 11 | 13 | (1,2) |
| 13 | 1 | (3,4) |
| 15 | 35 | (1,1) |

The complete active table also contains inputs 17 and 23, making all eight
two-step experiments closed at their active inputs. A third active step is
not promised. Source 35 is allowed at the final skip.

Both exact implementations pass the eight complete three-word trajectories,
80 occupied-first-archive continuations and their full primitive inverses.
The 4096 skip cases use the proved token-macro semantics, not 4096 primitive
replays. All primitive pair sums, accounts and labelled mod-five residues
are checked for every distinct ordered pair used.

The breaker was written from PREREG.md without reading verify.py or its
output, then publicly frozen before its first execution and comparison.
It uses a separate compiler and the rho basis rather than the author's j
basis. Both generate the same literal word and identical complete trajectory
boundary states after an explicit outer-JSON-layout conversion. Both runs
are on x86_64; this is not a public two-architecture scientific gate.

## Evidence and replay

- PREREG.md and verify.py: public source pin
  `5aef722e8f1c3d5cd3c9c25b164b5ed91f660aa2`, read back before execution.
- break.py and BREAK-SCOPE.md: independent public pin
  `17caea0066ec0dff2d5c2b8227e352edb0653023`, read back before its execution.
- PROOF.md: symbolic proof of the construction and distinct raw-scalar
  obstructions; also a direct contact halving-with-J-twist lemma whose
  missing numerator synthesis is explicitly stated.
- RUN.md, EXPECTED.txt, BREAK-EXPECTED.txt, REVIEW.md: actual execution and
  independent comparison records. SHA256SUMS binds the package files.

From the repository root:

```sh
python3 notes/C-COLLATZ-CONTACT-STEP-RECORD-N/verify.py
python3 notes/C-COLLATZ-CONTACT-STEP-RECORD-N/break.py
```

Ordinary repository CI checks notes/ for integrity but does not replay its
scientific verifiers. The fourth write, permanent records, arbitrary fresh
post-start inputs, native U and the physical apparatus owner remain outside
this construction. No minimum slot, account or word-length claim is made.

## Sources

- Declared integral relative contact and residue boundary: public Canon v107,
  content `f5615ed4dcdfc672dc2e468399284a1dc03ce805`.
- Exact Collatz inverse and blocks: PR #1859, head
  `b9a163e0dc1066429ed3fe367ac0756ef433c021`.
- Related but distinct variable-arrival apparatus: PR #1857, head
  `377a99ae11b885e27e863e2323c9a2f6e7d68510`.

The Boolean controlled-swap mechanism is rederived explicitly here; no
unattached code or unpublished asset is a runtime dependency.
