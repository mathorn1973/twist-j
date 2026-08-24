# PREREG C-PRIME-ORDER-READING-1, ADDENDUM 1 (Field 2 correction, pre-code)

DATE 2026-08-11, after the freeze of PREREG-C-PRIME-ORDER-READING-1.md
(sha256 6f90df5d23c8900c80a08c69a06eb70279a8692f18cb53365566320e58cfee21),
BEFORE any verifier code was written and before any computation was run.

DEFECT DISCLOSED. Field 2 path B as frozen ("collision exactly when reduced
tuples coincide") is vacuous on cross-prime pairs: canonical reduced tuples
of generators of distinct primes always differ, already by their norms, so
the test cannot fire on the main audit and a printed PASS would claim an
independent confirmation it does not perform. This is the id-1 class of
defect (a gate exceeding its test), caught at specification time, disclosed
here, and corrected before code. Field 1 (claims), Field 5 (thresholds) and
Field 6 (layer, falsifier) are untouched; no threshold moves.

CORRECTED PATH B, replacing Field 2 path B on cross-prime pairs and fixed
points. Exponent enumeration with certified window: a collision of witness
y against modulus n holds iff there is an integer m, |m| <= B = 200, with
y^2 = +- phi^m n as exact coefficient pairs in Z[phi]. Coverage is
certified in integers: the coefficient magnitude of phi^m n is strictly
monotone in |m| beyond small |m| (Fibonacci growth), and the verifier
asserts at the enumeration boundary that the magnitude strictly exceeds
that of y^2, so no solution can exist outside the window. The enumeration
may terminate early at the certified magnitude crossing; that is the same
window, entered from below.

Reduced-tuple comparison is RETAINED where it is not vacuous, and only
there: negative controls, the construction diagonal (same ideal versus
conjugate ideal), and fixed points (phi-orbit of w against the phi-orbit of
sigma(w)); on those tests it must agree with the enumeration and with
path A, and disagreement is an integrity STOP as frozen.

Everything else in the frozen preregistration stands verbatim.
