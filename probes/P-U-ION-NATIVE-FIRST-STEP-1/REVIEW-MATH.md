# Post-run mathematical and result review

**Disposition: ACCEPT within the frozen conditional ideal-model scope.**
NON-CANONICAL. This record checks the first run's reported result against
the accepted construction; it creates no Canon status or real-device
certificate. The physical HOLD remains unchanged.

The reviewer authored PROOF.md and statically reviewed the two verifiers
before pinning. This is therefore not a newly independent or blinded proof
review. The separately authored independent implementation remains a
distinct check. This post-run review reads the accepted files, output and
records and performs administrative byte/hash comparisons only; it does
not execute or import either scientific program or modify a frozen file.

## Evidence read back

The local nine-file candidate agrees with commit
`9e4978073604f4dcb69d1ab024bdeadc12d75d40`. A named-path Git comparison
found no changes in those files. All seven support-file byte counts and
SHA-256 values agree with INPUTS.json; the primary's embedded manifest
hash agrees with the actual manifest bytes. In particular:

| Object | SHA-256 |
| --- | --- |
| verify.py | `e217dea56c67d0e7628cefe33885938c8b0023ba6b53a26d57b5e80a9c6b457b` |
| INPUTS.json | `831106e859554394d3595745f83713cdeb8fbce265b0b1d3a8c42817f7a9a6f6` |
| PROOF.md | `d5671246aaaddeaa2db17b8bdebd35a97b30238263ae7f8d634f10174711662c` |
| verify_independent.py | `3a610a9fd1e3d8c6f113473840fa2d34bbb706eb740822d9bcc576271c76f21d` |
| EXPECTED.txt | `b8b71baf5255bbba5842bb16abf1d2f61602c168cc62bdc806589a557ba15f9e` |

EXPECTED.txt has 755 bytes and the declared ten-line result. Its reported
independent stdout SHA-256 is
`84d31a7aa605314ca20c303e6abe2223cea472a3b06464910efdf3d86cc0f723`,
also recorded in RUN.md. This review did not generate another independent
stdout. The accepted primary requires the independent subprocess to exit
zero, write no stderr, return PASS and match the five shared audit fields.

RUN.md reports the first post-pin execution on Ubuntu 22.04.5 LTS,
x86_64, CPython 3.10.12, with exit zero, empty stderr and completion within
both timeouts. Its output identity agrees with the bytes inspected here.
The public byte readback and original process metadata are attributed to
that run record; this review does not claim a fresh remote authority check
or another scientific execution. No public CI result is asserted here.

## Corrections remained prospective

The two findings documented in REVIEW-PREREG.md are corrected in the
accepted independent source:

- The shared JSON field is `omitted_ls_success`, matching the primary and
  PREREG.md, and the independent audit requires exactly five successes.
- The normalized equality phase is `-i` for positive g_e and `+i` for
  negative g_e, matching the physical sign convention. Both square to the
  same Z used by the controlled-rotation construction.

These corrected lines were read back before the public pin and again in
this review. They are not post-run repairs. No static blocker from that
review remains open.

## Mathematical interpretation of the observed result

The accepted audit has the required distinct scopes:

- The finite frequency and monomial checks audit the 500-loop coefficient
  identities, the six active-edge layouts, true adjoints and scalar
  spectator/local contributions. The arbitrary-profile scalar formula and
  the untruncated harmonic-mode factorization are analytical statements in
  PROOF.md; no finite oscillator simulation substitutes for them.
- Complete two-ion columns establish each of the twenty controlled
  rotations on false as well as true controls and on target levels outside
  the active pair. The 500 distinct columns are checked for both geometric
  signs, with all monomial and rotation phases retained.
- The twenty-five actual seventeen-register columns and their inverses
  establish the specified first-step subspace action. Their normalized
  amplitudes are +1, so linearity preserves its coherence and reference
  correlations. The common physical scalar Gamma remains in the analytical
  account. Laboratory-frame phases retain MODEL.md's separate convention.

The target table is compared against the original native generators and
the actual selectors in the fixed dictionary. M1=s and M2=1 retain their
physical meanings, S1 and S2 have their complete required outputs, and the
finite counter changes from 0 to 1. In particular s=3 and s=4 have equal
fourteen-data outputs and orthogonal M1 outputs. This construction transfers
the distinction to a counted register rather than contradicting the earlier
data-only unitary obstruction.

The recorded counts are mutually consistent:

```text
312 * 500 = 156000 LS loops,
312 * 61200 = 19094400 echo-frame carrier pulses,
19094400 + 380 + 26*6 + 7 = 19094943 carrier pulses,
19094400 + 380 + 26*6/4 + 8 + 3 = 19094830 units of pi,
19094943 + 156000 + 1 = 19250944 switching boundaries.
```

The observed 380 extra frame pulses are below the frozen bound 936.
Both complete carrier bounds are consequently met with margin 556, while
the target, compiler and thresholds remain unchanged. The independent
greedy compiler's separate resource counts are not presented as a replay
of the primary's canonical cycle compiler.

The omitted-LS control reports five of twenty-five complete target
successes, as preregistered. With the controlled words canceled, only s=0
has both the native data and retained-memory target; all five t are still
allowed. This verifies that the specified word needs its declared coupling.
It does not prove a lower bound for every possible implementation.

RESULT.md accurately limits PASS to this complete first native step on its
supplied input sector. It does not claim a general native map on all
six-pentit states, a reset of M1, or subsequent availability of a blank bank.

## Remaining physical boundary

The adopted seventeen-ion single-COM Hamiltonian, individually addressed
carrier class, fixed response profile, six nonzero geometric couplings and
admissible intensities are explicit conditions. The exact result does not
establish their joint device calibration, neglected-mode closure, carrier
crosstalk suppression, decay or scattering error, practical fidelity, input
preparation or an autonomous finite quantum control/work-source account.

The pulse count is very large; its finiteness alone does not imply a useful
physical error. Motion factorization in the effective model does not reset
finite lasers, batteries or controllers. The output memory is occupied,
and the full two-contact history, archive protection and all later native
steps still require their own construction and resource account.

No inconsistency was found between the accepted mathematics, inspected
output and the bounded conclusion in RESULT.md. That is the extent of
this acceptance; Canon v97 and the physical HOLD are unchanged.
