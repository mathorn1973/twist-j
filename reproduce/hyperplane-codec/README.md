# Hyperplane and codec witness

The boundary hyperplane of the kernel census and the trace codec, in
exact arithmetic: integers, rationals, Q(sqrt5) pairs, and the
cyclotomic ring Z[zeta_5]. No floats anywhere. The census part
replicates the registered kernel census protocol exactly (warmup 400
ticks, window 300 ticks, second independent window) and reads the
boundary partition off the attractor supports. Fired falsifiers are
first class boundary records and nothing here revives or reargues
them; the open rate clause is carried without any witness by design.

Verified: the boundary class by full enumeration of all 15625 states,
S = M cap {s = 0} with M the z5 sheet {1, 4} and s the piston sum
Tr_4: |M| = 6250, |S| = 1250 (the v101 class), charged complement
5000 in two sheets of 2500, boundary fibers 625 + 625; the census
window realization of S as the union of the 63 = (p^3 + 1)/2 boundary
attractors, 62 of size 20 and the singlet of size 10, with the
charged sector the remaining 250 and no straddling attractor; the
trace codec: the step matrix M_J is multiplication by J = 1 +
zeta_5^2 column by column, its characteristic polynomial is
Phi_5(x - 1) = x^4 - 3x^3 + 4x^2 - 2x + 1 with trace 3 and
determinant 1, det(2I - M_J) = 5 = p over Z, the polynomial collapses
to (x - 2)^4 over F_5, the piston sum satisfies the integer identity
Tr_4(M_J x) = 2 Tr_4(x) - 5 x_c and doubles in F_5, and over all 625
covectors and all five multipliers the only solutions of
f(M_J x) = lambda f(x) are the scalar multiples of Tr_4 at
lambda = 2; and the finite fusion ring boundary behind the fired
falsifier: the phibit ring is the group ring of Z_5 with five
invertible simples of dimension 1, the Fibonacci ring has two simples
with tau tau = 1 + tau and dimension phi, and no identification
survives.

Evidence for registry claims HYPERPLANE-BOUNDARY-CLASS,
HYPERPLANE-BOUNDARY-REALIZATION, CODEC-TR4, PHIBIT-NOT-TAU. The open
row CODEC-RATE-SCOPE carries no witness here: the internal rate 4/5
clause waits for its coding scope and nothing in this file claims it.
Check map: 01 HYPERPLANE-BOUNDARY-CLASS; 02
HYPERPLANE-BOUNDARY-REALIZATION; 03, 04 and 05 CODEC-TR4; 06, 07 and
08 PHIBIT-NOT-TAU.

Run from the repository root:

```
python3 reproduce/hyperplane-codec/verify.py
```

Expected: byte identical to EXPECTED.txt, RESULT 8/8 ALL PASS,
exit 0, no stderr.
