# Independent tuple-reader review

**PUBLIC, NON-CANONICAL. Verdict: ACCEPT at the frozen L1 successor scope.**
Reviewer: root/tuple_reader_breaker. Completed 1 October 2026. No Canon
promotion or physical-owner change follows from this verdict.

## 1. Immutable identities and independence

The candidate specification was read at
`cba479dcc05fbcadec70007a5a8642547372c1f2`. Only its explicitly admitted
predecessor mathematical sections and canonical premises were available
before deriving this review. The known tuple-subclass failure and census
targets were disclosed in PREREG.md; no result-blindness is claimed.

The review's own PREREG.md, DERIVATION.md and break.py were publicly frozen
and read back at `49fe93dd9854f55a1d5aabb8dca62dadd66ea8d4` before any
scientific execution or successor author-code/proof comparison. Their
SHA-256 hashes and byte counts are:

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| PREREG.md | 7326 | `20a73b15f36b22b2e3c30c2324eda47916c7791bed0dd6f14371e5fd03339684` |
| DERIVATION.md | 6988 | `90ae6ecc28c34d46260375af517b8a3871b50e83bf20afaeb3dda559cf9e63eb` |
| break.py | 14236 | `107f5f861f6da0f07e6bf19f6eb614630f72082630f7871f4820040efa74c197` |

Only after that freeze was the author PROOF.md and verify.py read at
`4fde4fa50409d5df16fd4b210880044a87eb7a2f`. The compared callable is decode
in `notes/C-FIELD-J-TUPLE-READER-N/verify.py`, whose SHA-256 is
`8481877b0582c915340e0d3e2d2262a3345c71b4709849196f7a19d7e10ba818`.
The combined clean public execution tree is
`9e2337869174b4a8edba204ea667109e75fb05be`; all frozen source bytes remain
unchanged. No test or threshold was amended after the review freeze.

## 2. Proof and implementation findings

ACCEPT the complete input normalization contract. The author uses
issubclass(type(value),tuple) on both container levels, then explicit
tuple.__len__ and tuple.__getitem__ storage access. Actual tuple subclasses
are accepted independently of their public views and metaclass hooks;
forged __class__ objects reject without consulting that attribute.
Exact builtin-int checks precede all arithmetic on supplied slots, so bool,
int subclasses and coercible objects reject without executing their hooks.
The only subsequent iteration operates on newly constructed plain tuples
and trusted integer ranges. No original object or metadata is written.

ACCEPT totality, soundness, completeness, uniqueness, output plainness and
normalized-equivalence invariance. The independent derivation recovers the
positive A4 quadratic, complete 1225-point containing box, nonzero norm
bound 31 and the strict separation inequality 625>496. This proves the
four-lift inverse for every well-typed integer datum, including rejection
outside the exact image. Zero is handled exactly. The implementation follows
those checks and creates the specified plain integer tuple outputs.

The universal statements rest on the base-operation argument and exact
mathematical proof, not on enumerating a sample of Python classes. Raising
or nonterminating user hooks cannot affect the reader because its input
path never invokes them. The target's ordinary fixed builtin/runtime and
resource exclusions are retained without adding a new domain restriction.

Both original zero-subclass counterexamples now have the required accepted
result. A malformed underlying tuple remains invalid even when overridden
methods pretend otherwise. Valid-to-valid residue substitution remains
accepted, as required; no general corruption detector is claimed.

No actionable discrepancy was found in the frozen author proof or code.

## 3. Executed independent evidence

Root executed the prescribed own-mode and comparison commands serially from
the clean combined public tree, on Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12,
with the frozen deterministic environment and 600-second envelope. The
reviewer inspected both exact captured stdout files and neutral run metadata.
Both exited zero with empty stderr.

The field-matrix oracle checked all 1225 box elements and found exactly
291 image states, shell counts (1,20,30,60,60,120), maximum norm 31 and no
duplicate key. Each reader passed 71250 semantic keys with all sixteen
outer/inner combinations, totaling 1140000 wrapped calls per reader, plus
1837 fixed fixtures and one metadata preservation case. The latter include
hostile metaclasses and MRO descriptors, class facades, hostile slots, lying
views, every scalar position's bool/int-subclass rejection, huge integers,
both predecessor counterexamples and valid residue substitutions. Zero
input-hook invocations occurred.

The own-mode run took 1.465 seconds. Its stdout has 161 bytes and SHA-256
`41af9b36f1e02ded4e8a862290cf9712721dd301e40c60dd2efa3531f22ec4a5`.
The comparison run took 3.363 seconds; stdout has 238 bytes and SHA-256
`68523bdf64fa423cf37694dd75c8a3302538a3830fc312692a37e65a19e4defa`.
The comparison first revalidated the independent reader and then checked
the author's SHA-bound decode against the same unchanged oracle and fixtures.

This is completed one-architecture finite audit evidence supporting the
separately assessed proof. It is not a two-architecture computation gate,
and a notes-only CI result would not add that gate.

## 4. Disposition and boundary

The successor C-FIELD-J-TUPLE-READER-N is accepted as a proof-supported
candidate-T L1 reader-contract result. The former
C-FIELD-J-ENERGY-READOUT-N Python-contract rejection remains preserved at
its immutable pin; this successor neither repairs nor relabels it.

The accepted result supplies only the exact bounded scalar object reader.
It does not establish transport dynamics, physical acquisition, a clock,
noise tolerance, apparatus realization or any higher-layer reading. The
norm-941/modulo-25 and 3125-label results retain their existing scopes.
Any subsequent transport work needs its own contract, pin and review.
