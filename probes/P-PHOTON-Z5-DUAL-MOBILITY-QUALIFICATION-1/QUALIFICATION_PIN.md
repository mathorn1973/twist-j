# P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1 immutable pin

Status: PRE-EXECUTION / ZERO EVIDENTIAL WEIGHT

The first commit that adds this final file together with the complete
`SOURCE_SHA256SUMS` and `INPUT_SHA256SUMS` to branch
`probe/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1` is the immutable
qualification pin.  Its full commit SHA and parent are bound in the
pre-execution public receipt.  That receipt URL is copied into the completed
run record.

The identifier was reserved on issue #756 at public comment
`issuecomment-5495515902`.  It does not reopen the consumed Ward cross-check
or alter the immutable #767 source package.

Before this pin, only compilation, exact fixtures and nonformal L3/L4
development matrices were permitted.  No formal seed, L>4 state, primal
reader or Ward value was opened.

After public push and byte-for-byte readback, every pre-execution byte is
immutable.  The formal command is the explicit `--formal --pin-commit
FULL_SHA --pin-receipt ISSUE_COMMENT_URL` invocation frozen in `PREREG.md`.
The receipt is the exact ten-line public qualification-pin record frozen
there, not the earlier reservation comment.  Formal preflight checks it with
`gh api --hostname github.com`, compares all twelve pinned bytes with the
commit, and atomically
claims the persistent local Git ref
`refs/probe-attempts/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1` before build or
formal data.  It then atomically creates the preregistered public branch
`refs/heads/probe-attempts/P-PHOTON-Z5-DUAL-MOBILITY-QUALIFICATION-1` at the
pin, then immediately reads it back from the literal public repository URL.
It may be issued once; neither ref is ever removed.  Allowed post-pin additions
are exactly `EXPECTED.txt`, `RUN.md` and `RESULT.md`.

No kernel, dependency, seed, start, schedule, metric, threshold, terminal,
action layer or conditional schedule map may change after this commit.  A
failed or incomplete execution consumes the identifier under the abandoned
pin rule.
