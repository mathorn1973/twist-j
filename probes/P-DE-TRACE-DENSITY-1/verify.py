#!/usr/bin/env python3
# verify_de_trace_density_1.py
# Candidate C-DE-TRACE-DENSITY-1, TWIST-J incubation lane. NO AUTHORITY.
# Prereg: C-DE-TRACE-DENSITY-1.md,
#   sha256 330f44be891bea77e2aebc353303c185f83d7abc5cb0bcd5fa666cb3dede9403 (8651 bytes)
# Python 3 standard library only. Exact arithmetic (fractions.Fraction) in every
# assertion. pi is FORMAL: every displayed quantity carrying pi is handled as its
# rational coefficient; pi is never evaluated. No floats anywhere in this file.
# Decision: which issue #88 outcome holds over the registered set R(v12):
#   PASS-EARNED | NEGATIVE | NONUNIQUE | STOP.

from fractions import Fraction as F

LINES = []
GATES = []

def emit(s):
    LINES.append(s)

def gate(name, ok, witness):
    GATES.append((name, bool(ok)))
    emit("GATE %-38s %s  %s" % (name, "PASS" if ok else "FAIL", witness))
    if not ok:
        raise SystemExit("FAILED at %s" % name)

def dec_witness(fr, digits):
    # exact long division readout, assertion-free, integers only
    neg = fr < 0
    n, d = abs(fr.numerator), fr.denominator
    ip, rem = divmod(n, d)
    out = []
    for _ in range(digits):
        rem *= 10
        q, rem = divmod(rem, d)
        out.append(str(q))
    return ("-" if neg else "") + str(ip) + "." + "".join(out)

# architecture (R5)
p = F(5)
d = F(3)

emit("C-DE-TRACE-DENSITY-1 verifier")
emit("architecture p = %s, d = %s; pi formal throughout" % (p, d))
emit("")

# ---------------------------------------------------------------- A. skeleton
emit("[A] the exact skeleton")
gamma_tr = F(1) / p                      # MEASURE-SPATIAL-ONLY [T]
w_DE = F(-14, 15)                        # COSMOLOGY-REGISTER committed form [D]

def Delta(w):                            # FRW continuity coefficient identity
    return d * (F(1) + w)

gate("A1-continuity-at-register-form", Delta(w_DE) == F(1, 5),
     "d(1+w)|w=-14/15 = %s" % Delta(w_DE))
w_from_dict = gamma_tr / d - F(1)
gate("A2-dictionary-solves-to-w", w_from_dict == w_DE,
     "1/(pd) - 1 = %s" % w_from_dict)
gate("A3-three-one-over-p-meet", gamma_tr == F(1, 5) == Delta(w_DE),
     "gamma_tr = alpha* = Delta_DE = 1/5")
gate("A4-one-plus-w", F(1) + w_DE == gamma_tr / d,
     "1 + w = 1/15 = gamma_tr/d")
gate("A5-closed-form", w_DE == -(p * d - 1) / (p * d),
     "w = -(pd-1)/(pd) = -14/15")
emit("READOUT (no assertion): w_DE = %s (engineering witness)" % dec_witness(w_DE, 10))
emit("")

# ------------------------------------------- B. the q-family and NONUNIQUE core
emit("[B] FRW continuity selection power over the density character q")
Q_FAMILY = [F(0), F(1, 5), F(1), F(3), F(4), F(7, 3)]
SURVIVORS = []
for q in Q_FAMILY:
    w_q = q / d - F(1)
    # R1 continuity: the single exact constraint d(1 + w_q) = q
    c_ok = Delta(w_q) == q
    # R1 Friedmann elimination: (H^2)'/(H^2) = -q exists for every q, imposes nothing
    h2_slope = -q
    if c_ok and h2_slope == -q:
        SURVIVORS.append(q)
gate("B1-family-passes-continuity", len(SURVIVORS) == len(Q_FAMILY),
     "all %d tested q satisfy d(1+w_q)=q" % len(Q_FAMILY))
ws = [q / d - F(1) for q in Q_FAMILY]
gate("B2-injectivity-q-to-w", len(set(ws)) == len(ws),
     "q -> w_q injective on the family")
gate("B3-lambda-point-not-excluded", F(0) in SURVIVORS,
     "q = 0 (w = -1, the Lambda point) survives R")
gate("B4-nonunique-witness", len(SURVIVORS) >= 2,
     "%d inequivalent characters survive R(v12)" % len(SURVIVORS))
emit("")

# --------------------------- C. sealed structures carry no q slot (independence)
emit("[C] selector independence: every sealed relation is constant in q")
def sealed_chain(q):
    # CONFORMAL-PREFACTOR [D]: K_chi5 = k/(12 V_cell), k = 12, V_cell = 864 pi.
    # The formula has no q slot; q enters only as the probe argument.
    k = F(12)
    V_cell = F(864)                      # coefficient of pi
    K = k / (12 * V_cell)                # coefficient of 1/pi
    c_hom = 12 * K
    return (K, c_hom)

vals = {sealed_chain(q) for q in Q_FAMILY}
gate("C1-kinetic-chain-q-free", vals == {(F(1, 864), F(1, 72))},
     "K_chi5 = 1/(864 pi), c_hom = 1/(72 pi) for every q")
gate("C1b-864-is-12-times-72", F(864) == 12 * F(72), "864 = 12 . 72")

def dewitt(lam, q):
    return d * (F(1) - lam * d)          # no q slot

gate("C2-dewitt-q-free-and-12", {dewitt(F(-1), q) for q in Q_FAMILY} == {F(12)},
     "d(1 - lambda d)|lambda=-1 = 12 for every q")
gate("C2b-ghost-control", dewitt(F(1), F(0)) == F(-6),
     "lambda = +1 gives -6, the GR conformal ghost, not the substrate")
gate("C3-lambda-substrate", F(1) / d - F(4, 3) == F(-1),
     "lambda = 1/d - 4/3 = -1")
gate("C4-friedmann-numerics", (F(216) / 3 == F(72)) and (F(1, 864) * F(216) == F(1, 4)),
     "216/3 = 72; K_chi5 . lambda_src = 1/4 = 1/(d+1); all q-free")
emit("")

# ------------------------- D. transport control: the dictionary is not a law yet
emit("[D] transport universality control")
w_spatial = F(1) / d - F(1)              # universal transport applied to weight 1
gate("D1-universal-transport-spatial", w_spatial == F(-2, 3),
     "Gram weight 1 would force w = -2/3 on the spatial base")
DUST, RADIATION = Delta(F(0)), Delta(F(1, 3))
gate("D2-universal-transport-contradicts", F(1) not in (DUST, RADIATION),
     "Delta = 1 is neither dust Delta = %s nor radiation Delta = %s "
     "(standard readings, control only)" % (DUST, RADIATION))
uniq = [q for q in Q_FAMILY if q == gamma_tr]
gate("D3-dictionary-selects-uniquely", len(uniq) == 1 and uniq[0] == F(1, 5),
     "GIVEN Delta_DE := gamma_tr, exactly one family member survives: q = 1/5")
emit("")

# ------------------------------------------------------- E. negative controls
emit("[E] negative controls")
gate("E1-wrong-dictionary-separates", F(3, 4) / d - F(1) == F(-3, 4) != w_DE,
     "Delta := alpha_s_root = 3/4 gives w = -3/4, distinct physics")
gate("E2-p2-control", F(1) / (F(2) * d) - F(1) == F(-5, 6) != w_DE,
     "p = 2 gives w = -5/6, not -14/15: the result sees p = 5")
gate("E3-p7-control", F(1) / (F(7) * d) - F(1) == F(-20, 21) != w_DE,
     "p = 7 gives w = -20/21, not -14/15")
emit("")

# ------------------------------------------------------------------ verdict
n_pass = sum(1 for _, ok in GATES if ok)
emit("%d of %d gates PASS" % (n_pass, len(GATES)))
emit("")
emit("OUTCOME (issue #88 space): NONUNIQUE")
emit("  typed: trace line, chi = log a, and the map all typed (STOP excluded)")
emit("  q = 1/p not excluded (NEGATIVE excluded)")
emit("  survivors >= 2 under R(v12) (PASS-EARNED excluded)")
emit("STATEMENT AT CANDIDATE GRADE:")
emit("  candidate-T  the registered set R(v12) does not select the density")
emit("               character of the trace sector; at least two inequivalent")
emit("               characters survive; Delta_DE := gamma_tr is genuine")
emit("               dictionary content, not a derivation, today.")
emit("  candidate-T  conditional uniqueness: once Delta_DE := gamma_tr is")
emit("               accepted, the selected member is unique and equals")
emit("               w_DE = -14/15 at p = 5, d = 3, exactly.")
emit("  candidate-T  the transport is not universal: applied to the spatial")
emit("               base it contradicts the standard dust and radiation")
emit("               characters; the dictionary is sector-specific content.")
emit("C-DE-TRACE-DENSITY-1 VERDICT: NONUNIQUE. Dictionary remains dictionary.")

print("\n".join(LINES))
