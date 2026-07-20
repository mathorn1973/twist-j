# RESULT. P-DE-TRACE-DENSITY-1

21 of 21 verifier gates PASS; the adversarial break path failed to kill.
Outcome in the frozen issue #88 space:

```text
OUTCOME: NONUNIQUE
  STOP excluded         the trace line, chi = log a, and the map all typed
  NEGATIVE excluded     q = 1/p survives every registered constraint
  PASS-EARNED excluded  at least two inequivalent characters survive R(v12),
                        including q = 0 (w = -1, the Lambda point)
```

Statements supported at computation grade (status pending the PR-time
x86_64 check; no registry or Canon change is made by this probe):

```text
UNDERDETERMINATION   the registered set R(v12) does not select the density
                     character of the trace sector; every sealed relation in
                     R1..R4 is exactly constant in q; the only selector is
                     the dictionary itself (circularity witnessed).
CONDITIONAL UNIQUE   given Delta_DE := gamma_tr, the selected member is
                     unique: q = 1/5, w_DE = 1/(pd) - 1 = -14/15 exactly at
                     p = 5, d = 3. One decision, zero residual freedom.
NOT UNIVERSAL        the same transport applied to the spatial base (Gram
                     weight 1) gives w = -2/3, contradicting the standard
                     dust (Delta = 3) and radiation (Delta = 4) readings
                     (controls only): the dictionary is sector-specific
                     content, not a general law over sectors.
```

Consequences for the frontier row DE-CONFORMAL-WEIGHT [O]: its positive
closure as currently worded (close by DERIVING the weight) is not earnable
from R(v12); this probe proves why. The remaining legal dispositions are an
explicit owner decision accepting the dictionary at D-grade dictionary scope
(with the physical falsifier F-DE-W armed), or leaving the row open. That
decision belongs to the owner and to a sealed fold; it is out of scope here.

A fired MATH falsifier (a registered non-circular selector) would kill the
NONUNIQUE closure; it stays armed permanently. Negative controls all fired
correctly: lambda = +1 gives the conformal ghost -6; Delta := 3/4 gives
w = -3/4; p = 2 gives -5/6; p = 7 gives -20/21.
