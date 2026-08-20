# PREREG-AUDIT-WIDDER-DEPTH-2B (correction of fired gate CG2)

```text
KIND:      correction leg for gate CG2 of audit_widder_depth_2.py, which
           FIRED on an audit-code representation defect: the polynomial
           equality test compared coefficient lists of unequal length, the
           computed real part carrying one trailing zero (degree bound 4
           from the product shape) against a length-4 target. The same
           defect class as leg 1's A3-07 Horner trailing zero. The pinned
           leg-2 run stands as recorded, 7/8, exit 2.
CLAIM:     unchanged from CG2: (1-i)^4 = -4; the level-2 sign polynomial at
           A = B = 1 is exactly 8u(u+1)(u+2); it is positive on (0, inf)
           and zero only at the boundary u = 0; k_min(1,1) = 3 by the Re
           form while pi/(2 theta) = 2 exactly, so the ceiling form fails.
METHOD:    two independent certificates: (a) the leg-2 symbolic route with
           trailing zeros normalized away before comparison; (b) evaluation
           at five points u = 0..4: two polynomials of degree at most four
           that agree at five points are equal.
PROCEDURE: this file and audit_widder_depth_2b.py frozen together, ast.parse
           only, pin below in AUDIT_PIN-WIDDER-2B.txt, one run.
DATE:      2026-08-20. NON-CANONICAL, single platform, candidate labels only.
```
