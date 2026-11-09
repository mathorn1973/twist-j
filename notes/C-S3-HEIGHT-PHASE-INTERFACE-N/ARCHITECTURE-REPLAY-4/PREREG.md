# S3-ARCHITECTURE-REPLAY-4: prospective reproduction contract

NON-CANONICAL / L1. This is a reproduction of existing frozen evidence,
not a new search, construction, independent review or Canon promotion.
Reservation #1960; draft PR #1961.

## Fixed sources and comparison

Source checkout: 73f3cb4946b05f5d63aba1c279642f77c699caef.
The four programs and all their criteria remain byte-identical.
SOURCES.json binds all 24 note files and the unchanged WORD535.txt fixture
by path, bytes, Git blob and SHA256 at that commit.
The original pins remain 7406c1468bd344b6aac311099097a64ff970ff22
and 5a925abb110707e333121b9960370dae8e58d236.

For each of two independently prepared clean checkouts, execute sequentially:

1. CONSTRUCTIVE-3/verify.py, compare to CONSTRUCTIVE-3/EXPECTED.txt.
2. CONSTRUCTIVE-3/audit.py with the captured first stdout, compare to
   CONSTRUCTIVE-3/AUDIT_EXPECTED.txt.
3. CONSTRUCTIVE-3/assembly.py, compare to CONSTRUCTIVE-3/ASSEMBLY_EXPECTED.txt.
4. search.py, compare to the root EXPECTED.txt.

All paths above are under notes/C-S3-HEIGHT-PHASE-INTERFACE-N/.
The fixed original outputs have respective SHA256:
724329795a84ff5f00a908a72ab31ab9ccf8be486def5e58c43a09fcc64c2203,
163342bdcd442a962d2281fd9406cb50dc946ebf0fa7e8d0e526b23446a2e9db,
fcc72a214caf784942ffdc5a0ed1c05b48c69c8a1558148d6987382c7b9ae74f,
b7dcf988c9a6bbcdc900e0fd60f6f8c8c7e8f3720316e118441d276d91c4378a.
The search's INCONCLUSIVE outcome is preserved, not reinterpreted as PASS
of an existence claim.

## Architecture, operation and failure

Run first on x86_64 with Python 3.12, then on aarch64 with Python 3.13.
The planned operating systems are Windows and Darwin, respectively.
arm64 and AMD64 are normalized only for architecture labels.
No floating-point value selects a scientific result. Measured elapsed time
is operational metadata. Each process uses assertions, PYTHONHASHSEED=0,
PYTHONDONTWRITEBYTECODE=1, LC_ALL=C, LANG=C and TZ=UTC.
Original operational timeouts are 120, 120, 600 and 120 seconds.
No process runs until this entire directory is committed, pushed and
publicly read back. Static parsing and hashing are permitted beforehand.

The capture-only replay.py checks the source HEAD, clean worktree and
every source byte before and after execution. It imports no scientific
module. Use a new external output directory for each architecture:

    python replay.py --source SOURCE_CHECKOUT --output NEW_OUTPUT --architecture x86_64
    python replay.py --source SOURCE_CHECKOUT --output NEW_OUTPUT --architecture aarch64

PASS requires every process to exit 0, have empty stderr, and emit bytes
identical to its existing expected file. A mismatch, exception or timeout
stops subsequent dependent work. Preserve original stdout, stderr and
receipt even on failure. Do not repair or rerun this pinned attempt.
A transport timeout is not a new scientific attempt: first inspect the
existing process and its original receipt. Never launch a replacement
while the outcome is unknown. Source corruption is a custody failure,
not a mathematical no-go.

## Review intake and scope

Independent review PR #1962 at c6134c0dff24b04e2597cb1d660bf375add5222c
reports PASS WITH NOTES and zero DIFF-REAL for source head 73f3cb49.
It independently reconstructs the compiler, stopwatch and composed cycles.
Its code/output blindness is declared relative to the author's executables;
the equations, case lists and headline counts were known.

The review preregistration was committed before its first execution.
Its initial implementation failed, was repaired and passed before review.py
was first frozen. The published tree does not include the original failed
source and complete failed stdout promised by that preregistration.
This does not establish a contradiction in the construction, but prevents
certifying that full attempted-run history from the public record.
This replay does not repair, replace or reclassify that history, and it
does not rerun the reviewer's checker.

Successful cross-architecture byte reproduction strengthens the finite
evidence. The all-k result remains an analytical proof with finite audits.
This note does not register a formal probe or change any Canon status.
Future consolidation must supply the governing claim/evidence registration.
Prepared inputs, finite fresh archives and supplied program order remain
premises. No Turing universality, physical energy cost, thermodynamic lower
bound or maximal measurement window follows from this construction.
