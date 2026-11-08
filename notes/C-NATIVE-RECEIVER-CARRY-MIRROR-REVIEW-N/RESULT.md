# Result of the independent review of PR #1884

**NON-CANONICAL / L1.** Target: P-NATIVE-RECEIVER-CARRY-MIRROR-1, PR
#1884, head c9bd0bc5ac97ad034be399e6619695c7fc2c4a61. Review lock: #1885.

## Verdict

No mathematical error was found, and no frozen check fired. The four
declared v109 review scopes are mathematically sound at their stated
scope:

| Scope | Verdict | Conditions for a Canon wording |
| --- | --- | --- |
| 1. Receiver transfer and unique affine port | Accept | E9 wording |
| 2. Marked carry pairing and the four-register circuit | Accept | E1 conjugation order; E2a dependence on (2/5)=-1; E2b convention-free sign content; E6 |
| 3. Fixed-input discrimination at the next carry precision | Accept | E8 required: the result is minimal among carry-only readers, since (output letter, carry) already separates J and J^-1 in F5; E3 |
| 4. Finite 62-cell, 500-input compiled realization | Accept as candidate-C finite evidence | E4 the inverse is the literal reverse of the forward word; E5 vendored compiler from open PR #1819 |

MATHEMATICAL-REVIEW.md gives the derivations and the corrections E1 to E9.
Section 7, the trace-port obstruction, is also confirmed; see E7.

## Independent execution

The code-independent checker review.py was frozen before execution, with
the preregistration frozen first and the checker pinned at c6855cb. After
public readback, its single run gave:

- exit 0 and empty stderr;
- 7022 bytes of stdout, SHA-256 42176dd0…;
- 153,338,125 executed primitives and 1254 counted native origin ticks
  (1250 in R11 and 4 in R8; the enumerations in R1 and R3 are not
  counted as ticks).

That covers:

- **R1–R3:** the Canon and PROOF.md generator forms agree on all 5^6
  states. The four first-tick rows and the unique port (1,1,2) are
  confirmed. Trace closure holds on all 5^6 states for both clock bits,
  tau_0=(0,4,0,4,4) and tau_1=(2,1,1,3,1), and no binary clock word of
  length 1 to 10 realizes s -> 2s. The words were checked at both trace
  level and state level, and so was the actual clock 0110100110.
- **R4–R6:** O=Z[j] was treated with exact norm valuations. The checks
  confirm:
  - v_lambda(5)=4, and the 25 classes modulo lambda^2 are distinct;
  - F and I recovered by valuation search;
  - L and L^2=id on all 625 states, with the correct conjugation order;
  - for both sections, the exact identity C_mirror=-J^-1 C, the residues
    3b and b, the same-input residue 3b, and second coefficients b and -b
    with slopes 2 and 3 for both reader lifts.

  A stress test over every integer b and every integer lift with
  |b|,|a|<=30 (745 cases per multiplier) confirms that the arguments do not
  depend on the section.
- **R7–R8:** the omitted offset gives 500 wrong marks, with 125 sign-only
  agreements, exactly the s=1 sheet. The second device's reader equals
  chi(a)=-chi(b).
- **R9:** the hash-bound compiler emits a word of 40348 primitives with
  the declared inventory, every wire in 0..49. With the checker's own
  interpreter, the word gives F and the checker's own inverse gives I on
  all 25 inputs. The workspace and an external sentinel are restored.
- **R10 (beyond the target audit):** the compiled occupied circuit runs on
  all 625 (q,r,h,k) and equals the closed L. A literally executed second
  pass restores the complete 62-cell memory.
- **R11:** the integrated carrier runs on all 625 piston tuples, 80705
  primitives and two native origin ticks each. The 500 admitted tuples
  restore the primary post-tick checkpoint, give archive 3s and high s, and
  leave the secondary output equal to U at the origin applied to
  (4+2s,0,0,0,0,1). The work cells are clean at all four multiplier
  boundaries. The tuples form four boundary classes of 125. The 125 s=0
  controls form one restored class with mark 3, high 3 and archive 4, as
  the closed L predicts.

**Post-run comparison with the target's EXPECTED.txt.** Only the values
were compared, because the two serializations differ by design. The values
agree on every shared quantity:

- the native rows and port;
- tau_0 and tau_1;
- the word length and inventory;
- the 25-input F/I tables, which determine the target's five mirror
  rows;
- each boundary row's (s, receiver, a, v, w, native sign, paired sign) and
  secondary receiver;
- 500 inputs, 80705 primitives per input, and two ticks.

The digests differ because the serialization formats differ. They are not
comparable byte for byte, and no byte equality is claimed.

**CI.** The target's two-architecture gate was audited from the actual job
logs; see CI-AUDIT.md. Both architectures show an identical
`VERIFY PASS … d9968f83… 085d8c3d…`, and the tested merge tree is identical
to the head tree.

## Independence and limits

- **The results were exposed.** All outcomes were published before this
  review began, so this is result-exposed review, not blind discovery.
- **The coordinator saw the author's code.** The coordinator of this review
  read the target verifier before writing the symbolic review. Only the
  checker writer was verifier-blind.
- **Both are Claude sessions.** The coordinator and the checker writer are
  Claude Code sessions with no access to the authoring session's context.
  Whether that counts as the independent acceptance required for a Canon
  fold is for the Canon owner to decide.
- **Local checker run.** The checker ran once, on x86_64 only. That makes it
  a reproduction, not a gate.

This review changes no probe, registry row, status, Canon text or release.
It does not establish any of the following:
- that bare U derives the interconnection;
- a native inverse;
- a physical time direction or Hermitian-time identification;
- pulse dynamics, archive regeneration or autonomous operation;
- an L1-to-L4 bridge;
- any connection to the contact-bank carrier of PR #1879.

Canon remains v108.
