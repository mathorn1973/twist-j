# Static security and scientific scope review

**NON-CANONICAL. Source review before first execution.**

The accepted source uses Python's standard library only. It does not load
an old numerical module, binary solver, MPFR library or checkpoint. The
only subprocess calls are read-only `git rev-parse` and `git status` checks
of the exact accepted checkout. There is no network client, shell execution,
dynamic code from inputs, credential access, write into the source checkout
or write into the preserved campaign.

All production input filenames are fixed in code. Hashes cover all five
endpoint inputs, serialized input, final-custody, inventory and campaign
summary. The internal input-binding file is hash-checked. Exact source-file
inventory and hashes are checked before and after evaluation. JSON duplicate
keys, nonfinite numbers and boolean/numeric impersonation are rejected on
the declared fields. Binary endpoints are decoded by bit pattern and their
length/order is independently checked against the frozen basis/layout.

Output is a newly created directory outside source and inputs, with exclusive
file creation. Scientific output has no machine nickname, host address or
credential. Neutral platform/architecture/version/timing is kept in a run
receipt. Original input paths need not be published.

Parent and child process address spaces are bounded. Fork and cleanup
registration are protected from timer/termination/interrupt signal races.
The parent watchdog, worker budget checks and external process-group
supervisor enforce the frozen time contract; any timeout is non-certified.
Cleanup adds no scientific work. Python decimal conversion has a finite
32768-digit limit with the bound stated in the derivation.

Public evidence must distinguish independent implementation from blind
reproduction: the old formulas, saved schema and custody hashes were read.
Parameter-interval validity and propagation/thermal radii are inherited
premises, not regenerated certificates. Same-session static review is not
an independent laboratory or a physical observation.
