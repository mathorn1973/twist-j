#!/usr/bin/env python3
# P-DE-W-ARMING-2 verify.py
# Evaluation of frozen rule R1 of P-DE-W-ARMING-1 on the DESI DR2 flat
# constant-w (wCDM) posterior readback. The rule is inherited verbatim; the
# record is one quoted published posterior summary; the decision is one
# exact rational comparison.
#
# Python standard library only. Exact Fraction arithmetic. No float appears
# in any assertion, comparison, or printed value. Deterministic output.
#
# Source:
#   [S1] DESI collaboration, DESI DR2 Results II, arXiv:2503.14738v3
#        (Phys. Rev. D 112, 083515), table 5, flat wCDM, DESI+CMB:
#        w = -1.055 +/- 0.036. HEADLINE per the abstract's own designation.
#        Readback provenance and the misquote defect clause: PREREG.md,
#        SYSTEMATICS (a); the drafting environment could not reach the
#        source, and the quoted values entered on the owner's public
#        readback of 2026-08-26 recorded in issue #576 before the pin.

import sys
from fractions import Fraction

assert len(sys.argv) == 1

TARGET = Fraction(-14, 15)
D_DIM = 3
P_PRIME = 5
R1_BAR = Fraction(322, 125)     # inherited 99 percent two-sided witness bar
ARMING1_R1_BAR = Fraction(2576, 1000)   # the P-DE-W-ARMING-1 constant
CARRIER = ("CMB-S4", "DES", "DESI", "Euclid")

# The single frozen wCDM entry of this record. Decimals are the printed
# survey values; the exact rationals beside them are the frozen entry.
WCDM_ENTRIES = (
    {"collab": "DESI", "release": "DR2", "fit": "wCDM",
     "combo": "DESI+CMB", "headline": True,
     "w_mean_printed": "-1.055", "sigma_printed": "0.036",
     "w_mean": Fraction(-211, 200), "sigma": Fraction(9, 250),
     "override_statement_printed": False, "source": "S1"},
)

# No w0waCDM entry is on this record; rules R2 and R3 live on the
# P-DE-W-ARMING-1 record and are not re-evaluated here.
W0WA_ENTRIES = ()

checks = 0

def gate(name, condition):
    global checks
    assert condition, name
    checks += 1
    print("%s PASS" % name)

print("P-DE-W-ARMING-2 verify")
print("rule: R1 of P-DE-W-ARMING-1, inherited verbatim; record: DESI DR2"
      " wCDM readback")

# G1 the register identities, exact (unchanged from P-DE-W-ARMING-1)
gate("G1 register identities: -14/15 = -1 + 1/(d p), d=3, p=5;"
     " density exponent -3(1+w) = -1/5",
     TARGET == Fraction(-1) + Fraction(1, D_DIM * P_PRIME)
     and Fraction(-3) * (1 + TARGET) == Fraction(-1, 5))

# G2 the inherited bar is the P-DE-W-ARMING-1 constant, exactly
gate("G2 inherited threshold: R1 bar 322/125 equals the P-DE-W-ARMING-1"
     " constant 2576/1000, immutable",
     R1_BAR == ARMING1_R1_BAR and R1_BAR == Fraction(322, 125))

# G3 record integrity: one entry, in carrier, exact decimal-to-rational
e = WCDM_ENTRIES[0]
gate("G3 record integrity: 1 wCDM entry, collaboration in carrier,"
     " printed decimals equal the frozen rationals exactly",
     len(WCDM_ENTRIES) == 1
     and e["collab"] in CARRIER
     and Fraction(e["w_mean_printed"]) == e["w_mean"]
     and Fraction(e["sigma_printed"]) == e["sigma"]
     and e["sigma"] > 0)

print("record:")
print("  [%s] %s %s %s %s%s w = %s +/- %s (frozen: %s, %s)"
      % (e["source"], e["collab"], e["release"], e["fit"], e["combo"],
         " HEADLINE" if e["headline"] else "",
         e["w_mean_printed"], e["sigma_printed"], e["w_mean"], e["sigma"]))

# G4 the HEADLINE designation is frozen data on this record
gate("G4 HEADLINE designation: the DESI+CMB wCDM fit is frozen HEADLINE on"
     " the abstract's own designation (readback of PREREG SYSTEMATICS a)",
     e["headline"] is True)

# G5 the override clause status is frozen data on this record
gate("G5 override status: no printed credible-interval or exclusion"
     " statement about w = -14/15 is on this record, so the Gaussian"
     " witness governs",
     e["override_statement_printed"] is False)

# G6 the Gaussian witness, exact
z = abs(e["w_mean"] - TARGET) / e["sigma"]
print("  witness: |z| = |%s - (%s)| / %s = %s"
      % (e["w_mean"], TARGET, e["sigma"], z))
gate("G6 Gaussian witness: |z| = |w_mean + 14/15| / sigma = 365/108"
     " exactly",
     z == Fraction(365, 108)
     and abs(e["w_mean"] + Fraction(14, 15)) == Fraction(73, 600))

# G7 the comparison, exact, with the frozen at-or-above semantics
margin = z - R1_BAR
print("  comparison: 365/108 vs 322/125; cross products 45625 vs 34776;"
      " margin = %s" % margin)
gate("G7 R1 comparison: witness at or above the bar; margin 10849/13500"
     " positive",
     z >= R1_BAR
     and 365 * 125 == 45625 and 322 * 108 == 34776 and 45625 > 34776
     and margin == Fraction(10849, 13500)
     and margin > 0)

# G8 scope guard: rules R2 and R3 are not evaluated on this record
gate("G8 scope guard: no w0waCDM entry on this record; R2 and R3 remain on"
     " the P-DE-W-ARMING-1 record, untouched",
     len(W0WA_ENTRIES) == 0)

# G9 the decision
gate("G9 R1 decision: a HEADLINE flat wCDM fit of a carrier release"
     " excludes w = -14/15 at or above the 99 percent two-sided witness"
     " bar; R1 FIRES on this record",
     e["headline"] is True
     and e["override_statement_printed"] is False
     and z >= R1_BAR)

print("DECISION: R1 FIRED on the DESI DR2 HEADLINE wCDM readback;"
      " DE-W-CONSTANT [H] -> F at the next sealed fold")
print("RESULT %d/%d ALL PASS" % (checks, checks))
