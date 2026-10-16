# Custody qualification and unresolved predecessor record

PUBLIC / NON-CANONICAL. Source-analysis and evidence-disposition record,
not an execution receipt. A. M. Thorn; scope #1539.

## Verified source objects

The seven frozen files of AUDIT-1 are unchanged between input
8edb5ea97bf38337d9c65f08964a0ae9e2ed7743 and declaration
d9a20f7bba60ae868aa467b5b076960ac5e88b7d. The seven frozen files of AUDIT-2 are unchanged
between 731d825d966d9b6df5678c4c059ea1e3d068c67a and
d36c23e0789e74c8d052de3d2061bd1717acbb74.
Both sets were compared as complete Git-object bytes, not names alone.
All twelve historical source rows in AUDIT-2/SOURCES.tsv were separately
fetched by their exact Git identifiers and checked for SHA-256 and length.
The exact identities of the material used here are in this SOURCES.tsv.

The old AUDIT-2 verifier itself verifies its six local input hashes and
checks the syntax of external source rows. It does not fetch those source
objects or compare their bytes at execution time. Its 'sources=12' output
must not be represented as a runtime historical-source-byte audit. The
external comparison above is a distinct administrative custody check.
Likewise this new verifier hashes its local frozen packet; historical Git
source validation is explicitly pre-pin administrative evidence.

## What the AUDIT-1 source says

At input 8edb5ea9, PREREG section 5 defines a scientific mismatch to be a
printed SCIENTIFIC_FAIL with zero exit, while unexpected exceptions and
execution failures have a different disposition. The pinned functions show:

    check(False, stage, message) -> raises ExactAuditFailure
    main: catches ExactAuditFailure around each stage
          prints failed stage and dependent NOT_RUN markers
          prints VERDICT SCIENTIFIC_FAIL
          returns 0
    verify.py: returns int(module.main()) and sys.exit(main()).

The false 'len(expected_tail_zqr)==10' test calls this check function.
Its expression has twenty elements, as proved in PROOF section 6. Therefore,
IF a supported-runtime execution with intact inputs reaches that test,
the specified path is a handled negative verdict and zero return, not an
uncaught fixture crash. This source-level conclusion needs no execution
of the old file. It does not prove that a particular historical invocation
reached it, completed printing, or was captured without interruption.

The separate bit_count call can fail on Python3.9.6 before that test. The
pinned contract required Python>=3.10. A crash in an unsupported interpreter
and a handled check failure in a supported interpreter are not one event.

## What the available historical record does and does not establish

AUDIT-1/RESULT.md declares ABANDONED and records no EXPECTED.txt or RUN.md.
Its prose combines the Python3.9.6 invocation and the tail-fixture issue.
The user supplied a command-only transcript containing a later Python3.13
invocation and a subsequent removal of EXPECTED.txt. It contains no raw
returncode/stdout/stderr from either invocation. That conversational excerpt
is reference information, not a replacement immutable run record; it is not
copied into the repository. The public issue comments, committed path
history, and submitted result contain no contemporaneous capture sufficient
to decide the second invocation's complete outcome.

The blanket claim 'a fixture error occurred, therefore no completed gate'
is not justified by the actual pinned failure contract. Conversely, this
review does not invent the missing first stdout, an exit code, a date or a
new RUN.md under the old identifier. No old verifier is imported or run.

Disposition: HOLD_PENDING_ORIGINAL_CAPTURE for acceptance of AUDIT-1's
historical classification and hence for unqualified custody closure of
#1534/#1537. The old identifier remains consumed. Its source and existing
ABANDONED declaration remain unchanged as a historical record, not endorsed
as a resolved classification. Successful AUDIT-2 mathematics and replay are
separate evidence and are not relabelled as an AUDIT-1 success.

## Exact remaining evidence, not another scientific search

Recover the contemporaneous record of the reported Python3.13 invocation:
actual return code, exact stdout and stderr, interpreter version, executed
pin and its input-byte identity. Neutral descriptors suffice; do not publish
private machine paths or raw private execution logs.

If it contains the handled SCIENTIFIC_FAIL, preserve that original negative
output and give it the completed-result disposition required by the pinned
contract. If it contains a genuinely uncaught/aborted run, document that exact
failure separately from the handled fixture predicate. If the capture is
irrecoverable, state that loss explicitly and retain an evidence gap; a
later reproduction cannot become the historical first run. Any subsequent
replay would require a separately authorized, correctly scoped record and
must not resume the consumed identifier.

This is a scientific-record accuracy problem, not evidence of intent by the
original author. No accusation about motive is made. Repository acceptance
must distinguish what is proved, what was executed, and what is missing.

## Precedence for the proposed correction

Read #1537 PROOF with E1-E3 in this PROOF.md; its blanket '0 mathematical,
computational, or scope discrepancies' statement does not cover the three
false prose statements. The seven underlying coordinate-readout conclusions
retain their correct replacements. This new correction is authored with
full exposure to both implementations and needs its own reviewer. It cannot
retroactively make the original proof independently error-free.
