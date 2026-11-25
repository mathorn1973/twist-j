# Received RECON archive: custody, replay and remaining limits

**PUBLIC / NON-CANONICAL / L1 / no authority.**
Recorded finite results: candidate-C. The separate written results in
RECON-REVIEW.md remain candidate-T at their stated scope.
Author: A. M. Thorn <thorn@twistj.com>.
Owner session: codex-zero-root-20261125, reservation #2097.

## 1. Disposition

The received archive reproduces the central finite results. Four new
outputs match its stored outputs byte for byte. Additional frozen checks
confirm the two-early-cut result for every common preparation, all 125
listed preparations, the exposed receiver collision, and a correction
to a contact-code comment. Every scheduled stage exited zero with empty
stderr. No received source byte was changed.

This is a same-session source audit and one-architecture reproduction.
It is not an independent external confirmation, a retroactive
preregistration, a native two-sample archive, or a Canon promotion.
The original exploration's author roles, execution environment and
provenance cannot be established from its source comments alone.

## 2. Exact custody and execution pin

The owner supplied `twistj-recon-2026-11-25.tgz` as an attachment.
Its size is 36076 bytes and its full SHA-256 is

```text
137a48e98c1643fdc0fa6134279778333e2a7044dae68b529a7f5b8c8f43aa5d
```

There are 29 regular files with 167165 uncompressed bytes and four
directories. [ARCHIVE-MANIFEST.tsv](ARCHIVE-MANIFEST.tsv) records every
regular member's path, length and hash. The received archive has no
symlinks, device members, repeated names or traversal paths.

The current public basis was freshly checked: Public Canon v117,
main and tag `6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed`, content ancestor
`d65e32c4b8e9a14496d3b7aba46fc384f51f81dc`, all five normative hashes
matching. CANON.md has 1624192 bytes and SHA-256
`93a8d0c17ed88d93a62b56c44d65b6903c980654f7e5ea82da7e363a510a22a9`.
No attachment was treated as current Canon authority.

All original outputs and later predictions were exposed before this
review. The prospective replay protocol was pushed at
`aba3d1a311cbacc6ef48ecb034903a96dec7eae9`. Static review caught a prose
selector error before any archive code execution: popcount must first
be reduced modulo2. The unchanged executable already did this correctly.
[ARCHIVE-EXECUTION-SCOPE.md](ARCHIVE-EXECUTION-SCOPE.md) records the
correction without rewriting that earlier pin. The complete execution
pin, pushed and read back before the run, is

```text
a8607e770058b5efe5cdd318101b615b9337bc44
```

| Pinned file | Bytes | SHA-256 |
| --- | ---: | --- |
| ARCHIVE-PREREG.md | 8304 | 88f565786223bd79066e2de1f823f6336630a53266ec889a2accfcfc4c89617c |
| ARCHIVE-EXECUTION-SCOPE.md | 1635 | 80e874de2afaab1da94bf99e63570f03c8b452071c4f1e94a58afccbb47fb410 |
| ARCHIVE-MANIFEST.tsv | 2556 | 73d2421a85ff3541498348b1fe35491a359f809aabdadfed179cb8aea1892992 |
| archive_replay.py | 11584 | baf13e35b5ff5bfc83533c76c644097d8882853fc4ff537a1d6082a882d4ffec |

Command, with the external input and a fresh output directory outside Git:

```text
python3 -I -B notes/C-J-ZERO-ROOT-N/archive_replay.py ARCHIVE NEW_OUTPUT_DIRECTORY
```

Execution date: 2026-11-25, 17:15:14 to 17:16:09 UTC.
Platform: Debian GNU/Linux 13.7, Linux x86_64.
Runtime: CPython 3.12.14. Compiler: GCC 14.2.0, flags
`-O2 -std=c99 -Wall -Wextra`.
The outer process exited 0 with empty stderr. The wrapper recorded every
child's status, output lengths and hashes, and its final complete flag.
The exact individual time limits remain in ARCHIVE-PREREG.md.

## 3. What was actually rerun

| Stage | Checked range | Result and qualification |
| --- | --- | --- |
| B | 37 checks; 6561 bounded u,v pairs; 625 residue classes; the documented representative-shift samples | Stored 3049-byte output reproduced exactly. Integral-contact law, not native U. |
| C32 | All 62 nonempty proper coordinate splits, every common complement, counter 0, cuts 0..32 | Stored 6720-byte table reproduced exactly. |
| C-matrix | Separate affine-matrix implementation; selector words to 4096; 20 observed tail maps and the comparison of all 62 splits | Stored 4487-byte output reproduced exactly. The finite horizon alone is not an all-time proof. |
| Early cuts | Six piston pairs, 625 common preparations each, 25 sources each, cuts 0..3; histories begin at cut 1 | Every crossing pair has 25 distinct ordered histories at cuts 1,2 for every preparation. Maximum current counts are 17 crossing and 9 same-index. |
| A-million | All 25 E inputs to cut 1000000; all 15625 raw states to cut 200; generator and invariant checks | Stored 1374-byte output reproduced exactly. |
| A125 | All 125 distinct rows in the received preparation list, all 25 messages per row, cuts 0..200 | Passed. No stdout for this script was stored in the archive; this is a fresh audit of the list, not byte reproduction of an old run. |
| Witnesses | The two fixed cases in ARCHIVE-PREREG.md | Passed with the exact expected 145-byte output. Reuses received arithmetic and motor modules. |

The six early-cut checks cover 3750 common preparations across the six
splits. All four crossing pairs pass the universal 25-source claim on
their 625 preparations each. This now has direct finite coverage in this
session in addition to the previous written argument.

The finite horizons do not replace the all-time arguments. The bounds
for every tick and the complete
zero-output-history count remain the consequences proved in
[RECON-REVIEW.md](RECON-REVIEW.md), using the canonical synchronization,
sheet bijections and invariant recurrence at the pinned basis.

### Exact scientific stdout receipts

All listed return codes are 0. Every stderr has 0 bytes, with SHA-256
`e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855`.
The compiler emitted neither stdout nor stderr. Its version check emitted
the expected 7 bytes `14.2.0` followed by a newline. Raw local execution
files are not added to the repository.

| Stage | Stdout bytes | SHA-256 | Comparison |
| --- | ---: | --- | --- |
| B | 3049 | abb1f808534748f49c85bb871024ba338b6d08f6873e0d1419c9e4f58e301dab | Received output |
| C32 | 6720 | 9fbdd0b9640ba55c8336fa39646f02559d6441a5e906a78fe74a7ff7d180aeda | Received output |
| C-matrix | 4487 | ab44cecb040e7d8bbd63efe449188e855902d1d9550feab987b7ce0de3ea3c73 | Received output |
| early-3 | 83413 | 87b01cfc8f9d86b986d2d874c2c13ac2906b315f8f4e92d68189e88f831e690c | Frozen coverage assertions |
| early-5 | 79665 | 7bdecb12745d621c459238c73e42a7115a7b71647b5cb62001b038a347a0c7f8 | Frozen coverage assertions |
| early-6 | 83413 | 1f48678fb2dc9eb61b22351ae15f72cfa14fbbf84b734ccbde7e51b7dcf3f5a7 | Frozen coverage assertions |
| early-9 | 83413 | 745444d4cc75e4773480524b71790944c570f1e9fc9ec90c761833a21a545f02 | Frozen coverage assertions |
| early-10 | 82160 | 8a9a8af4011de3b3a8343addbecdfcc96f1e901020468291c9f27ab430fd8fb1 | Frozen coverage assertions |
| early-12 | 85913 | b4ea4704dddf0b05a0e08fa517eff4120eb34c6f548c73c11bc0848fdfe84d4f | Frozen coverage assertions |
| A-million | 1374 | 525fe28ef7cad0491bf11977f68af29eb371c884fdbb2a3974dbecde76478501 | Received output |
| A125 | 690 | 41c4fa87392314ab13e67695794fcf66246e47d7ed6e23bad5fdcb3e165e2850 | Frozen 125-row audit |
| witnesses | 145 | e88c5b6c8abd61b24bd7188d0d247864699e62fe9f81e5d37b81b9d48686660a | Prospective literal expectation |

The wrapper's local metadata field `byte_identical_to_received` is also
used for compiler and witness literal expectations. Only the four rows
explicitly marked Received output above compare against archive stdout.
No older witness execution is inferred from that generic field name.

## 4. Consequences that survive the source audit

### Native capacity and the exact collision

For common complementary receivers and two free source pistons, the
previous maxima 9,17,25 survive. The full finite table agrees between
direct-state C and affine-matrix Python implementations. This establishes
agreement of these two code paths here; comments calling their original
authors independent do not supply an authorship or blindness record.

The exposed receiver collision also occurs exactly as stated:

| Prepared message | Cut | Receiver (p4,p4p,q,r) | Correct PRESENT payload |
| --- | ---: | --- | --- |
| E(3,0) | 3 | (4,0,4,2) | (4,0) |
| E(2,4) | 28 | (4,0,4,2) | (0,1) |

Thus a fixed function of just this receiver cannot read every E payload
without counter or source references. This does not contradict a reader
that sees the complete current state, or a decoder supplied with the tick.

### Zero is not an absence flag

The A output reproduces 360 E-timed raw launches reading PRESENT(0,0).
The written proof counts exactly 360 launches with the full same output
history as E(0,0), including E(0,0) itself. Hence 359 lie outside E.
Output equality does not mean complete-state equality. Every origin-zero
launch becomes PRESENT by cut 3 under the specified reader; there is no
forever-BLANK launch. The special meaning of the zero record is secured
by the preparation contract, not by the pair (0,0) alone.

### Contact selector and mark value are different statements

The B program correctly tests that the overwrite is admitted exactly
when x is congruent to w modulo4O. One source comment instead says that
the mark equals J exactly in that congruence class. That stronger literal
claim is false. The new fixed witness x=w+4 gives

```text
pointer = 2*(1-rho)
mark = J + (1-rho)^2
mark-J = (0,-1,-3,-1) in the basis (1,j,j^2,j^3), nonzero modulo5.
```

The executing B assertion uses the correct varying mark formula. The
comment error therefore does not invalidate its 37 passing checks.
The earlier -3w,+3w,+5w,-5w examples still disprove interpreting this
branch selector as the sign of the oriented multiplier.

The conditional native obstruction also retains its precise scope:
if the entire preparation, counter origin and observation inputs factor
through x modulo5O, opposite branches on +5w and -5w cannot be obtained.
Supplying an externally read modulo4 label changes that input interface.

## 5. Code qualifications that must remain visible

- `C/break_splits.py` compares only rows actually present in its input.
  Without a separate completeness check, even an empty comparison file
  can reach its agreement message. The new wrapper checks all 62 ordered
  row identifiers before calling it and compares its output exactly.
  The received implementation is preserved unchanged.
- `C/layer_pairs.py` contains an `or True` in an early ell^4 check,
  making that particular assertion vacuous. Separate square-zero tests
  elsewhere in that source have their own coverage. This script was
  statically reviewed, not rerun here.
- `C/coset_check.py` must not be read as asserting universal recovery
  from arbitrary late windows. Its own stored output reports 615 of 625
  preparations for one crossing pair and 600 of 625 for another. This
  does not affect the universal origin-time cuts 1,2 result just rerun.
- The a,c comment in `A/check_A.py` must not be read as saying that
  both generators change AB. Its following check concerns AB alone
  and reports zero changes for a and 12500 for c; a exchanges A and B,
  preserving AB. The actual assertions that both products are invariant
  are correctly restricted to b,d,e.
- `A/subclass_A.py` does not apply its headline cut 3..64 range to every
  subclass: the second subclass calls its helper with horizon 8. It also
  observes a bare piston pair in one comparison, not the complete
  receiver used in the 9/17 theorem.
- B's representative-change sampling covers 125 classes with five
  specified shifts; its C-invariance check uses all 625 classes but only
  the shift 5j. These are finite checks, not exhaustive proofs for all
  integral representatives. Its forms B and C are reconstructed in the
  delivered code. No claim that they were recovered from an earlier
  original manuscript is made.

The full 5^12 search, subclass search, auxiliary C programs, alternative
counter origins, T96 run and X comparison were not executed in this
replay. A125 validates the list it was given; completeness of 125 and the
count 12000 rely on the separate symbolic classification. X imports the
A motor and cannot be counted as another independent implementation.
The code also contains private working-path examples that were neither
followed nor published.

## 6. What the delivery does not contain

The archive has no 25-cell preparation list, fixed contact schedule,
output table or executable test of the claimed 25-cell archive. Its
REPORT2.md is an owner-pasted report from another session and explicitly
labels itself unverified there. The claimed 625 output-cell checks and
x=0 versus x=5 boundary are text assertions in that report. The B replay
does not test that construction.

The latest corrected RECON note and the later personal recheck script
reported by the owner are also absent. This does not refute their
existence or their results; it limits which exact files this intake can
attribute and reproduce. The early-cut and collision assertions have
nevertheless now been checked by the pinned adapter in this session.

The earlier zero-root audit note, its original four reservations and
original scripts remain a separate custody obligation in PROVENANCE.md.
This RECON archive is not that missing first audit. Its successful replay
must not erase that distinction.

There is no licence or reliable author attribution for the received
originals in the archive. Their source bytes and raw development logs
are retained as received references, not copied into the public repo or
relabelled with this package's author. Public files added by this review
are newly authored commentary, hashes and the adapter under repository
terms. Republishing original sources remains blocked on that provenance
and licence question, as required by POLICY.md and AGENTS.md.

## 7. Remaining scientific question

The crossing receiver's ordered observations at cuts 1 and 2 distinguish
all 25 inputs, while no single current receiver in the declared common
preparation class distinguishes more than 17. Waiting alone cannot create
a 25-message current record in that same class. A two-sample observer
already assumes memory outside that current receiver. A new proposal
must specify where the first sample is retained, which native states
carry that memory, how the second is combined with it, and who observes
the final result. Any change of carrier, common-preparation condition,
source split or allowed observation must be named explicitly.

No such native retention mechanism is supplied by this archive replay.
No live canonical O is closed. The arithmetic code, retained invariant
and supplied E preparation keep their earlier scope. Original candidate
verifiers, preregistrations, expected outputs and RUN.md are unchanged.
