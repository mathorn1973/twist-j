# Exact retained-program pair source

**NON-CANONICAL, L1.** `C-JM-RETAINED-PAIR-SOURCE-N`, issue #1680.
Analytical claims candidate-T; exact finite audit candidate-C. This is not
native U, an experimental apparatus, or a Born-occurrence derivation.

The source replaces an unspecified fresh-state preparation oracle with a
complete rational operation. It stores a classical integer z, prepares TWO
anchored copies from a common ready pair by an explicit norm-preserving
reflection, swaps them into an occupied output port and archives the complete
previous port state. K ready pairs supply2K outputs, with unchanged program,
retained old correlations and an explicit inverse. No square-root extension,
postselection, copied unknown quantum input, or seam/probability oracle.

The desired target is NOT hidden in the initial stock: every stock pair is
the same program-independent e0 tensor e0. The program, trace metric, reference,
pure stock, exact controlled reflections, swaps and counter are supplied
resources. Norm preservation is not a physical work/energy account. Derivation
of those resources from J or U remains open.

## Run

From the repository root, with Python3.11 or later, no external packages:

    PYTHONDONTWRITEBYTECODE=1 python3 notes/C-JM-RETAINED-PAIR-SOURCE-N/verify.py

Compare stdout with ACTUAL.txt. source.py is a usable exact sparse-vector
implementation, not merely a test of the proposed target. For example from
this directory:

    from fractions import Fraction
    from source import ready_source, tick
    z = (1,0,0,0,-1,0,0,0)
    s = ready_source(z, 14112, 3, {(1,0): Fraction(1)})
    initial = s
    for _ in range(3): s = tick(s)
    for _ in range(3): s = tick(s, inverse=True)
    assert s == initial

The old_port mapping accepts correlations with a retained spectator. Explicit
SourceState inputs permit occupied stock and all-state inverse tests, but dirty
stock is outside the fresh-output guarantee. Arithmetic simulation cost grows
with joint-state size; no efficiency or hardware timing claim is made.

## Evidence and boundaries

PREREG.md, source.py and verify.py were publicly pinned before execution at
760157f57495fb87059b3a8a8e7943be7d0793c1. One actual Linux aarch64 audit passed;
RUN.md explicitly distinguishes it from the originally planned x86_64 lane.
No same-code two-architecture or blind independent-agent verification is claimed.
Ordinary notes-only PR CI does not execute this scientific audit.

PROOF.md gives the general construction, parity boundary, exact integer
certificates, digital capture, occupied-port theorem, HOLD law, resource ledger
and reset constraints. It restates required definitions from the UNMERGED
predecessor PR #1679 without scientific promotion. No Canon, registry, frontier,
gate, workflow or sealed predecessor files change. No merge is performed.
