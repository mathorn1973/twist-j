#!/usr/bin/env python3
"""verify_f_watch.py -- F-watch state recorder for the TWIST-J RH line.

NON-CANONICAL. Status R (report). This script checks NOTHING about zeta(s).
It records the watch state of 2026-09-15: which queries and fetches were
attempted, whether each was reachable through the session's network, and
whether any reachable source returned an independent public record (exact
enclosure or machine-checked proof) of a nontrivial zero of zeta(s) with
Re(s) != 1/2.

The SOURCES table below is a hand-typed transcription of the session's
search and fetch results; the raw results are not saved next to this file.
The checks are therefore consistency checks on the table (and one exact
shape test of the checklist's box condition), not a certification of the
scan itself.

Exact arithmetic only (int, fractions.Fraction); no floating point; standard
library only.
Run: LC_ALL=C PYTHONHASHSEED=0 python3 verify_f_watch.py ; exit 0 on success.

Repaired 2026-09-15 after two referee reports (see the Review record of
F-WATCH-2026-09-15.md): proof-direction claims now file as NONE per step 4
of the watch procedure, check 5 tests the STOP-filed list exactly, check 3
also counts distinct unreachable hosts, and check 7 is new.
"""
import sys
from fractions import Fraction as Fr

DATE = "2026-09-15"
BASIS = "Public Canon v86, tag canon-v86"

# (kind, target, reachable, finding)
# finding vocabulary (closed; matches section 3 of the markdown):
#   NONE            reachable; no off-critical-zero record and no disproof
#                   claim surfaced.  Unconfirmed PROOF-direction claims file
#                   here (watch procedure step 4: "not even STOP; NONE");
#                   they are annotated in the target text.
#   CLAIM-ONLY      a DISPROOF claim (an off-line zero asserted) surfaced
#                   without a record; action STOP-on-sight per step 3, not F
#   T-DIRECTION     partial result toward RH, promotes nothing
#   RECORD          an independent public record of an off-critical zero
#                   (would flip the final line; none today)
#   BLOCKED         host unreachable, no finding possible
# The target field of a search row is the query as typed on 2026-09-15;
# bracketed text after it is an annotation added at repair, not part of
# the query.
SOURCES = [
    ("search", "2026 nontrivial zero of Riemann zeta function off the critical line counterexample", True, "NONE"),
    ("search", "2026 proof of Riemann hypothesis Lean formalization machine-checked", True, "T-DIRECTION"),
    ("search", "Riemann hypothesis verified height zeros Platt Trudgian 3e12 new record 2025 2026", True, "NONE"),
    ("search", "arXiv September 2026 Riemann hypothesis proof [proof-direction claims surfaced; NONE per step 4]", True, "NONE"),
    ("search", "Riemann hypothesis false disproof 2026 zero found critical line announcement [Liu 2404.06306 disproof claim, no zero exhibited; STOP]", True, "CLAIM-ONLY"),
    ("search", "Hatem A. Fayed A Simple Proof of the Riemann Hypothesis arXiv 2209.01890 submitted date [proof claim; NONE per step 4]", True, "NONE"),
    ("search", "rigorous verification zeros of zeta up to height 10^13 interval arithmetic 2026 extension Platt Trudgian [query as typed; 10^13 is a zero count, not a height, see section 2]", True, "NONE"),
    ("search", "Alpoge Furman 2609.02882 67.25 percent zeros critical line Lean formalization Riemann [query as typed; 2609.02882 is by Lamzouri, see section 2]", True, "T-DIRECTION"),
    ("search", "Riemann hypothesis Lean 4 mathlib formal proof complete 2026 announcement off the critical line OR counterexample [unreachable ResearchGate proof claim; NONE per step 4]", True, "NONE"),
    ("fetch", "arxiv.org (author listing platt_d_1)", False, "BLOCKED"),
    ("fetch", "export.arxiv.org (API query Riemann hypothesis, newest 40)", False, "BLOCKED"),
    ("fetch", "ar5iv.labs.arxiv.org (2609.02882)", False, "BLOCKED"),
    ("fetch", "research-information.bris.ac.uk (Platt-Trudgian record page)", False, "BLOCKED"),
    ("fetch", "www.mathlumen.com (2026 status report)", False, "BLOCKED"),
    ("fetch", "www.lmfdb.org (zeta zeros table)", False, "BLOCKED"),
    ("fetch", "www.alphaxiv.org (2609.02882)", False, "BLOCKED"),
    ("fetch", "www.cambridge.org (Engage preprint 697821239a5b4152c69c4c62)", False, "BLOCKED"),
    ("fetch", "www.jtpmath.com (review of Liu 2404.06306)", False, "BLOCKED"),
    ("fetch", "www.researchgate.net (396900027 Machine-Checked Proof of RH in Lean 4)", False, "BLOCKED"),
    ("fetch", "github.com/vstaln/riemann (README)", True, "T-DIRECTION"),
    ("fetch", "github.com/GoldenPhysicsProject/GPPVerify (README) [conditional Lean development, True := trivial stubs and one axiom; proof direction; NONE per step 4]", True, "NONE"),
    ("fetch", "github.com/dbsanfte/RiemannGaussian (README)", True, "T-DIRECTION"),
    ("curl", "export.arxiv.org via HTTPS proxy (CONNECT answered 403)", False, "BLOCKED"),
]

# Rows filed STOP in the markdown (section 2, task (a)), by 0-based index into
# SOURCES.  Check 5 requires the CLAIM-ONLY rows to be exactly these rows.
# On a clean watch both sides are empty and the check passes.
STOP_FILED = [4]

ALLOWED = {"NONE", "CLAIM-ONLY", "T-DIRECTION", "RECORD", "BLOCKED"}


def host_of(target):
    """First whitespace-separated token of a fetch/curl target is its host."""
    return target.split()[0]


def box_shape_admissible(a1, a2, b1, b2):
    """Arithmetic part of checklist item 2 (section 3, step 2) as corrected:
    rational endpoints, box inside the open strip 0 < Re(s) < 1, nondegenerate,
    and 1/2 outside [a1, a2].  This tests the SHAPE of a candidate box only;
    it says nothing about whether any box contains a zero of zeta."""
    for x in (a1, a2, b1, b2):
        if not isinstance(x, Fr):
            return False
    if not (Fr(0) < a1 < a2 < Fr(1)):
        return False
    if not (b1 < b2):
        return False
    if a1 <= Fr(1, 2) <= a2:
        return False
    return True


def main():
    checks = []
    print("F-WATCH DATE: " + DATE)
    print("BASIS: " + BASIS)
    print("SOURCES CHECKED (rows are attempts; bracketed text is repair annotation):")
    for kind, target, reachable, finding in SOURCES:
        print("  [%s] %-11s %-12s %s" % (kind, "reachable" if reachable else "unreachable", finding, target))

    # check 1: every finding is in the vocabulary
    ok = all(f in ALLOWED for _, _, _, f in SOURCES)
    checks.append(("finding vocabulary closed", ok))

    # check 2: unreachable <=> BLOCKED (a blocked host records nothing else)
    ok = all((not r) == (f == "BLOCKED") for _, _, r, f in SOURCES)
    checks.append(("unreachable sources carry no finding", ok))

    # check 3: exact counts (int arithmetic); rows are attempts, and the
    # unreachable attempts are also counted by distinct host
    n_total = len(SOURCES)
    n_reach = sum(1 for _, _, r, _ in SOURCES if r)
    n_block = n_total - n_reach
    blocked_hosts = []
    for _, t, r, _ in SOURCES:
        if not r:
            h = host_of(t)
            if h not in blocked_hosts:
                blocked_hosts.append(h)
    n_hosts = len(blocked_hosts)
    n_arxiv_hosts = sum(1 for h in blocked_hosts if "arxiv" in h)
    ok = (n_total == 23) and (n_reach == 12) and (n_block == 11) and (n_hosts == 10) and (n_arxiv_hosts == 3)
    checks.append(("attempt counts total=%d reachable=%d unreachable=%d; distinct unreachable hosts=%d (arXiv hosts %d, other %d)"
                   % (n_total, n_reach, n_block, n_hosts, n_arxiv_hosts, n_hosts - n_arxiv_hosts), ok))

    # check 4: no reachable source recorded RECORD
    n_record = sum(1 for _, _, r, f in SOURCES if r and f == "RECORD")
    checks.append(("no RECORD finding among reachable sources", n_record == 0))

    # check 5: the CLAIM-ONLY rows are exactly the rows the markdown files
    # STOP (disproof claims only).  Passes with 0 rows on a clean watch.
    claim_rows = [i for i, (_, _, r, f) in enumerate(SOURCES) if r and f == "CLAIM-ONLY"]
    ok = (claim_rows == sorted(STOP_FILED)) and all(SOURCES[i][2] for i in STOP_FILED)
    checks.append(("CLAIM-ONLY rows equal the STOP-filed list (disproof claims only): %d" % len(claim_rows), ok))

    # check 6: arXiv itself was not reachable, so the listing scan is partial;
    # this must be recorded, not hidden.
    arxiv_blocked = any(("arxiv" in t) and (not r) for _, t, r, _ in SOURCES)
    checks.append(("arXiv unreachable is recorded explicitly", arxiv_blocked))

    # check 7: the corrected checklist item 2 rejects the referee's
    # trivial-zero box [-21/10, -19/10] x [-1/10, 1/10] (which contains only the
    # trivial zero s = -2) and admits the shape of a strip box with 1/2 outside
    # its real range.  Shape test only; no zero is asserted anywhere.
    trivial_box = (Fr(-21, 10), Fr(-19, 10), Fr(-1, 10), Fr(1, 10))
    strip_box = (Fr(51, 100), Fr(53, 100), Fr(14), Fr(15))
    line_box = (Fr(49, 100), Fr(51, 100), Fr(14), Fr(15))  # 1/2 inside: must be rejected
    ok = (not box_shape_admissible(*trivial_box)) and box_shape_admissible(*strip_box) and (not box_shape_admissible(*line_box))
    checks.append(("item-2 box shape: trivial-zero box rejected, line-straddling box rejected, strip box shape admitted", ok))

    passed = 0
    for name, ok in checks:
        print(("PASS " if ok else "FAIL ") + name)
        passed += 1 if ok else 0
    print("CHECKS: %d of %d PASS" % (passed, len(checks)))

    if n_record == 0:
        print("F-WATCH: no record of an off-critical zero found in the reachable sources")
    else:
        print("F-WATCH: a reachable source reports a record of an off-critical zero; VERIFY EXACTLY BEFORE ANY FOLD")
    if passed != len(checks):
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
