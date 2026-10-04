# Result: no early SUM in the frozen native affine class

**Decision: NO_SUM_IN_FROZEN_CLASS.** The first publicly pinned execution
completed with wrapper `PASS`, primary `NO_SUM_IN_FROZEN_CLASS`, independent
`PASS`, exit zero and empty stderr. Both independently authored programs
found zero receiver survivors at all three times and all five source sums.

The complete negative theorem is **candidate-T**, supported by the
[symbolic proof](PROOF.md) and the separately derived sign-profile proof in
[the independent review](REVIEW-STATIC.md). The finite execution counts and
artifacts have also passed the required clean x86_64/aarch64 byte-identity
gate; exact jobs and hashes are recorded in [CI-VERIFICATION.md](CI-VERIFICATION.md).
Code independence and architecture reproduction are separate evidence.
The result remains non-canonical; no Canon status is changed.

## Exact decided class

For every x,y in F5, preparation is

    (n,P,F)=(0,P0+v*x,F0+w*y),  v!=0, w!=0.

All four piston coordinates belong to the source block; the fibre F=(q,r)
initially depends only on y. Offsets and transverse resources are common.
The same fixed affine block-local readers decode preparation and output:

    X(P)=A.P+a,  A.v=1, a=-A.P0,
    Y(F)=B.F+b,  B.w=1, b=-B.F0.

One common t in {1,2,3} is chosen for each candidate. The actual unchanged
origin-zero U, including its state-dependent selector and counter, must
return X(P_t)=x and Y(F_t)=y+x on all 25 inputs. No external generator
word, original-input oracle, extra register or hidden source copy is allowed.

The full class contains 438750000000 parameter tuples including time.
Its exact source-sum projection gives 75000 necessary receiver configurations
at each time. Every source-sum class, including zero sum with a nonzero
source line, has an admitted full preparation and initial source reader.
Receiver impossibility therefore excludes the full class; the independent
source-output retention requirement has not been removed.

## Why the theorem is not an extrapolated census

The source affects the fibre only through the closed (kappa,q,r) port.
When the source-line sum s is zero, the receiver cannot depend on x.
For s!=0, the actual first three steps give an exact fibre action table:
at step two the initial trace values 1 and 2 give the same fibre for fixed
y; step three equals step one followed by translation by (1,1). At step
one, the required affine SUM reading would force B.w=0, contradicting its
initial decoding condition B.w=1. These arguments cover all three times.

The independent proof instead uses the nonconstant sign profiles
(+,-,-,-,-), (-,+,+,+,+), and (+,-,-,-,-). At fixed initial trace, a
successful same-reader SUM would require a coefficient of y independent
of that trace; each profile contradicts this condition. The proofs are
complete over the frozen class, without a word-length or parameter sample.

The later same-fibre continuation boundary is inherited from
KERNEL-Z6-SYNCHRONIZATION, QDD-U-INDUCED-CHANNEL and
U-NATIVE-APPARATUS-HISTORY-FACTOR, including the prior late-tail evidence
and #1342's common-selector rule. It is not a new claim of this probe.

## Completed exact audit

| Audit surface | Actual coverage | Result |
| --- | --- | --- |
| Complete original checkpoints | 15625 | All retained |
| Actual first-three-step transitions | 46875 | Full states, counters and selected indices checked |
| Five-generator projection checks | 78125 | All agree with the closed port |
| Initial (z,q,r) fibre action table | 125 rows | Actual selected actions agree |
| Receiver configurations per time | 75000 at each of t=1,2,3 | Complete enumeration |
| Receiver/time configurations | 225000 | All rejected |
| Input/time equations | 5625000 | All 25 inputs checked for every configuration and time |
| Survivors by time | (0,0,0) | None |
| Survivors by time and source sum | All 15 entries zero | None |

Every rejected configuration has its first lexicographic failing input
recorded with the complete initial/final native checkpoint, counters,
actual and required receiver values, and representative source readout.
The audit continues through all 25 inputs after finding that witness.
No scientific falsifier fired; no scope or threshold changed after pinning.

The independent implementation additionally recorded mismatch-count
histograms. At t=2 the least observed number of failing inputs was nine
(100 configurations); at t=1 and t=3 it was fourteen (2400 configurations
each). These are finite audit data, not additional universal claims or
resource minima.

## Evidence and custody

Public preregistration pin:
`9754d85622844d40212288d2204fc240e6cd8e31`.
The scientific source remains Public Canon v97/main
`5e872c22a18043c8126945a982efad55472cea82`.
All 13 frozen local dependencies and 11 public source files passed their
byte checks before scientific evaluation.

The first run used `python3 probes/P-U-EARLY-SOURCE-FIBRE-CONTACT-1/verify.py`,
Python 3.12.10 on Windows 11, architecture x86_64. It began at
2026-10-03T23:24:38.773316+00:00 and completed at
2026-10-03T23:24:43.214726+00:00. Its one-line stdout is 2377 bytes,
SHA-256 `613ac47b49187ee1e7b89f7587ca393d8b82c71815d7d55a20605fbf7756925e`;
stderr is empty. The wrapper hash is
`58a9ce2a846572842927f2fb18307a30bd7fe216b16233af3c35f53e319191c4` and the
input-manifest hash is
`ff17153e65f0ef8a61e2f423623d92adc58095320eab87b8266d6e24e81f1ea4`.
The detailed command/environment receipt belongs to [RUN.md](RUN.md).

The following files were materialized by that same first execution; no
scientific rerun was used to reconstruct them:

| Evidence | Bytes | SHA-256 |
| --- | --- | --- |
| [Complete native trajectories](evidence/NATIVE-STEPS.csv) | 1051563 | `a821aedf52252349ab1fa3544c68d00bd0eccac9b3a7376655a94a4c99329af1` |
| [Actual fibre table](evidence/FIBRE-TABLE.csv) | 3081 | `1a8971d74424b8e3a6f75ffdd895de8f94832919259e2dd47cad8d9a2a0949bd` |
| [All t=1 falsifiers](evidence/FALSIFIERS-T1.csv) | 4554977 | `c2c94222f4ca6debf0a3b27eeadc798f3777636b10de453f75104a422261750c` |
| [All t=2 falsifiers](evidence/FALSIFIERS-T2.csv) | 4555030 | `6a4bcdbe5de90570881605970fd1f3c80eee94790056e51d452a226c624e52e4` |
| [All t=3 falsifiers](evidence/FALSIFIERS-T3.csv) | 4554075 | `9527107f33172eaa4f8b88e44e8540c96e6a88d019e50b70b8c7c10ec6053405` |
| [Receiver survivors, header only](evidence/RECEIVER-SURVIVORS.csv) | 27 | `4aff7e615606d895172df212f146e85985104da0b0e2b0a74e8d0158363abd71` |
| [Independent complete histories](evidence/INDEPENDENT-FULL-HISTORIES.json) | 2156253 | `9253716927d6c0d88f09e8e76d0330bb559fe6f980acc34fd0de7991a4274831` |

Every listed artifact is individually below 5 MiB. The independent optional
raw witness JSONL is retained locally, as [INTEGRATION.md](INTEGRATION.md)
specified before the run; it is not a required Git artifact or an additional
gate. The complete primary falsifier CSVs carry the required public witness
surface. Known targets were disclosed, while independent code was frozen
before primary-code exposure; those are separate statements.

## Limits and remaining gates

The result is a negative classification of this independent affine
preparation and same-reader class for the actual three early times. It is
not a prohibition of nonlinear readers, another source/receiver partition,
history access, a different launch contract, or an extended architecture.
The q-source/piston-pointer and partition results of #987/#1003, the fibre
representation #1342 and synchronized fixed-reader permanent-write result
#862 retain their original scopes and ownership.

No physical carrier, energy account, native inverse, reuse, renewal,
apparatus, occurrence measure or #1349 complete-state/counter preservation
and timing contract is supplied. The required x86_64/aarch64 reproduction gate has passed for the same
frozen bundle and stdout. A later reviewed Canon fold is separate from
either publication or CI.
