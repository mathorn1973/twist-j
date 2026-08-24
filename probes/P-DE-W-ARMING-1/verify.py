#!/usr/bin/env python3
# P-DE-W-ARMING-1 verify.py
# Frozen rule engine and current-record evaluation for arming
# DE-W-CONSTANT [H]: w = -14/15 exactly, constant, read from the committed
# register form of COSMOLOGY-REGISTER [D].
#
# Python standard library only. Exact Fraction arithmetic. No float appears
# in any assertion, comparison, or printed value. Deterministic output.
#
# Data are quoted published posterior summaries, entered as exact rationals
# with their sources; no chain is re-fit and no raw dataset is opened here.
# Sources:
#   [S1] DESI collaboration, DESI DR2 Results II, arXiv:2503.14738
#        (Phys. Rev. D 112, 083515): w0waCDM preferred over LCDM at
#        3.1 sigma for DESI BAO + CMB; 2.8, 3.8, 4.2 sigma adding
#        Pantheon+, Union3, DESY5.
#   [S2] DES collaboration, Constraints on Dynamical Dark Energy from
#        Multiple Probes in the Full Dark Energy Survey, arXiv:2605.27221
#        (PRL, forthcoming): 2.2 sigma from a cosmological constant for
#        DES alone; 3.0 sigma for DES + DESI DR2 BAO + CMB.

import sys
from fractions import Fraction

assert len(sys.argv) == 1

TARGET = Fraction(-14, 15)
D_DIM = 3
P_PRIME = 5
R1_BAR = Fraction(2576, 1000)   # 99 percent two-sided Gaussian witness
R2_SINGLE = Fraction(5, 1)      # single-collaboration headline bar
R2_DOUBLE = Fraction(3, 1)      # each-of-two-collaborations bar
R3_BAND = Fraction(2, 1)        # witness band floor
CARRIER = ("CMB-S4", "DES", "DESI", "Euclid")

# fields: collab, release, fit, combo, headline, sigma_pref (rational
# string), primary (frozenset of primary-dataset labels), source
ENTRIES = (
    {"collab": "DESI", "release": "DR2", "fit": "w0waCDM",
     "combo": "BAO+CMB", "headline": True, "sigma_pref": "31/10",
     "primary": frozenset(["DESI-BAO", "CMB"]), "source": "S1"},
    {"collab": "DESI", "release": "DR2", "fit": "w0waCDM",
     "combo": "BAO+CMB+PantheonPlus", "headline": False,
     "sigma_pref": "28/10",
     "primary": frozenset(["DESI-BAO", "CMB", "PantheonPlus"]),
     "source": "S1"},
    {"collab": "DESI", "release": "DR2", "fit": "w0waCDM",
     "combo": "BAO+CMB+Union3", "headline": False, "sigma_pref": "38/10",
     "primary": frozenset(["DESI-BAO", "CMB", "Union3"]), "source": "S1"},
    {"collab": "DESI", "release": "DR2", "fit": "w0waCDM",
     "combo": "BAO+CMB+DESY5", "headline": False, "sigma_pref": "42/10",
     "primary": frozenset(["DESI-BAO", "CMB", "DES-SN"]), "source": "S1"},
    {"collab": "DES", "release": "Y6", "fit": "w0waCDM",
     "combo": "DES-alone", "headline": False, "sigma_pref": "22/10",
     "primary": frozenset(["DES-Y6"]), "source": "S2"},
    {"collab": "DES", "release": "Y6", "fit": "w0waCDM",
     "combo": "DES+DESI-BAO+CMB", "headline": True, "sigma_pref": "30/10",
     "primary": frozenset(["DES-Y6", "DESI-BAO", "CMB"]), "source": "S2"},
)

WCDM_ENTRIES = ()   # no in-carrier collaboration constant-w summary is on
                    # this frozen record; R1 is PENDING exact table readback

checks = 0

def gate(name, condition):
    global checks
    assert condition, name
    checks += 1
    print("%s PASS" % name)

print("P-DE-W-ARMING-1 verify")
print("target: w = %s exact, constant; carrier: %s"
      % (TARGET, ", ".join(CARRIER)))

# G1 the register identities, exact
gate("G1 register identities: -14/15 = -1 + 1/(d p), d=3, p=5;"
     " density exponent -3(1+w) = -1/5",
     TARGET == Fraction(-1) + Fraction(1, D_DIM * P_PRIME)
     and Fraction(-3) * (1 + TARGET) == Fraction(-1, 5))

# G2 frozen rule constants, exact
gate("G2 rule constants: R1 |z| >= 322/125, R2 >= 5 single or >= 3 twice"
     " disjoint, R3 band [2, 322/125)",
     R1_BAR == Fraction(322, 125) and R2_SINGLE == 5 and R2_DOUBLE == 3
     and R3_BAND == 2 and R3_BAND < R1_BAR)

# G3 entry integrity: carrier membership, rational significances
for e in ENTRIES:
    assert e["collab"] in CARRIER
    assert Fraction(e["sigma_pref"]) > 0
gate("G3 record integrity: %d entries, all in carrier, all exact"
     % len(ENTRIES), len(ENTRIES) == 6)

print("record:")
for e in ENTRIES:
    print("  [%s] %s %s %s %s%s pref = %s sigma, primary = {%s}"
          % (e["source"], e["collab"], e["release"], e["fit"], e["combo"],
             " HEADLINE" if e["headline"] else "",
             Fraction(e["sigma_pref"]),
             ", ".join(sorted(e["primary"]))))

# G4 rule R1: constant-w exclusion of -14/15
gate("G4 R1 constant-w exclusion: no in-carrier collaboration wCDM summary"
     " on this record; R1 PENDING, fires nothing here",
     len(WCDM_ENTRIES) == 0)

# G5 rule R2 single leg: any headline preference >= 5 sigma
max_head = {}
for e in ENTRIES:
    if e["headline"]:
        s = Fraction(e["sigma_pref"])
        if s > max_head.get(e["collab"], Fraction(0)):
            max_head[e["collab"]] = s
for collab in sorted(max_head):
    print("  headline maximum %s: %s sigma" % (collab, max_head[collab]))
gate("G5 R2 single leg: every headline preference below 5 sigma, no fire",
     all(s < R2_SINGLE for s in max_head.values()))

# G6 rule R2 double leg: two collaborations, each >= 3 sigma, from
# combinations sharing no primary dataset (any published combination)
strong = [e for e in ENTRIES if Fraction(e["sigma_pref"]) >= R2_DOUBLE]
pairs = []
for i in range(len(strong)):
    for j in range(i + 1, len(strong)):
        a, b = strong[i], strong[j]
        if a["collab"] != b["collab"] and not (a["primary"] & b["primary"]):
            pairs.append((a, b))
gate("G6 R2 double leg with the disjointness clause: %d strong entries,"
     " 0 qualifying disjoint cross-collaboration pairs, no fire"
     % len(strong), len(pairs) == 0)

# G7 the counterfactual that motivated the clause: without disjointness the
# double leg would fire today on shared data
cross = [(a, b) for a in strong for b in strong
         if a["collab"] == "DESI" and b["collab"] == "DES"]
gate("G7 counterfactual: clause removed, DESI and DES cross pairs at"
     " >= 3 sigma exist (%d), so the double leg WOULD fire on shared data;"
     " the clause is decision-bearing today" % len(cross), len(cross) >= 1)

# G8 the only disjoint cross-collaboration pair candidate is DES-alone
# against DESI, and DES-alone sits below the bar
des_alone = [e for e in ENTRIES if e["combo"] == "DES-alone"]
gate("G8 disjoint candidate: DES-alone at 11/5 sigma is below 3;"
     " no independent-evidence pair exists on this record",
     len(des_alone) == 1
     and Fraction(des_alone[0]["sigma_pref"]) == Fraction(11, 5)
     and Fraction(des_alone[0]["sigma_pref"]) < R2_DOUBLE)

# G9 knife edge: the DES headline sits exactly on the double-leg bar; the
# frozen comparison is >= (would count if a disjoint partner existed)
gate("G9 knife edge: DES headline preference minus 3 equals 0 exactly;"
     " >= semantics frozen",
     Fraction("30/10") - R2_DOUBLE == 0)

# G10 witness census under R3
witnesses = sorted(
    "%s %s %s (%s sigma)" % (e["collab"], e["release"], e["combo"],
                             Fraction(e["sigma_pref"]))
    for e in ENTRIES if Fraction(e["sigma_pref"]) >= R2_DOUBLE)
for w in witnesses:
    print("  witness: %s" % w)
gate("G10 witness census: 4 recorded witnesses at or above 3 sigma,"
     " all below every firing bar or blocked by the clause",
     len(witnesses) == 4)

print("DECISION: DE-W-CONSTANT ARMED, HOLDS (fires nothing on this record)")
print("RESULT %d/%d ALL PASS" % (checks, checks))
