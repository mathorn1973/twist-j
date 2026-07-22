# PREREG. P-C8-BILINEAR-SHADOW-1

Public lock: owner directive of 2026-07-22 ("dej oboji ven"), recorded with the
incubation candidate C-C8-BILINEAR-SHADOW-1 in the project lane; the promotion
queue is empty and no competing claim exists. The owner attaches the issue
number at pull-request time; this session is the single probe owner. Base:
Public Canon v15, tag canon-v15, Canon content commit
`a850753348583e611bf7ccd5aa074030dc7e12f5`, branch base `origin/main`
`434e02a01903ef7a237053eac1231dbe7496bbf5`.

```text
LAYER:  L1 state and readout arithmetic. No lift to L2-L6 is claimed.
TARGET: the visibility decomposition of the order-eight lift: the axes form
        of <tau>, the Galois identity of the registered branch involution,
        the branch-invariant base-valued record with its strict mod-8
        refinement, while leaving SQRT-PHI-TIME-GRAVITY [O] open.
```

No scientific status is earned by this preregistration. Any eventual Canon,
registry, dependency, or frontier disposition is separate reviewed work.

## Frozen model and inherited objects

Work in the exact pair model

```text
K = F_25 = F_5[tau]/(tau^2 - 2),
(a,b) = a + b tau,
(a,b)(c,d) = (ac + 2bd, ad + bc) mod 5,
J = 2,  phi = 3 = J^-1,  eta = tau^3,  N(x) = x^6,
Frob(x) = x^5.
```

Inherit the registered theorems RAMIFIED-TM-LIFT (`Theta_n = J^s2(n)`,
`q(Theta_n) = theta_n`) and SQRT-PHI-DIGIT-LIFT (`Y_n^epsilon =
r_epsilon^s2(n)` for `r_+ = eta`, `r_- = -eta`; `N(Y_n^epsilon) = Theta_n`;
`Y_n^- = (-1)^theta_n Y_n^+`; successor multiplier `r_epsilon^(1-nu_2(n+1))`).

## Frozen statement

```text
(A) AXES      <tau> = F_5^* union tau F_5^* exactly: the even layer of the
              eight-wheel IS the base line as a set, the odd layer is its
              tau-translate. The order-8 elements of K^* are exactly
              {tau, -tau, eta, -eta}; every one squares into {J, phi}; the
              solutions of x^8 = 1 number exactly eight.
(B) GALOIS    Frob is conjugation a + b tau -> a - b tau; it fixes the even
              layer pointwise, negates the odd layer, and N(x) = N(-x) on
              all of K.
(C) SWAP      Frob(Y_n^+) = Y_n^- for every n >= 0: the registered branch
              involution (-1)^theta_n of SQRT-PHI-DIGIT-LIFT IS the Galois
              action; the sign branch is a Galois gauge choice.
(D) RECORD    the record V = (Theta_n for all n; Y_n^epsilon whenever s2(n)
              is even; Y_n^epsilon Y_m^epsilon whenever s2(n) and s2(m) are
              both odd) is F_5-valued and equal on both branches; the two
              branch trajectories differ exactly at the odd times;
              mixed-parity products lie off the base line and are
              branch-dependent, so the parity condition cannot be dropped.
(E) REFINE    the norm channel reads exactly s2 mod 4 (2^s = 2^t iff
              s = t mod 4); the even-layer value phi^(s/2) is injective on
              even classes mod 8; the odd-pair value phi^((s+t)/2) is
              injective in (s+t) mod 8; hence V reads s2 mod 8 at even times
              and s2(n)+s2(m) mod 8 at odd pairs, strictly beyond the norm
              channel. Witnesses: Theta_15 = Theta_255 = 1 with Y_15 = -1,
              Y_255 = 1; Theta_1 = Theta_31 = 2 with Y_1 Y_1 = phi,
              Y_1 Y_31 = phi^3. At even classes Y^2 = Theta^-1 and Y itself
              selects one base root, branch-invariantly.
```

Reading at the frozen scope (carries no more than the clauses): the C8 lift
hides from the base field exactly one datum, the global sign of the odd
layer, and that datum is the Galois bit; everything else is base-visible.
The phase is gauge; the bilinear is arithmetic.

## Frozen all-n proof

1. The scalar squares in F_5 are {0,1,4}, so x^2 - 2 is irreducible and K is
   a field of 25 elements; Frob(tau) = tau^5 = (tau^2)^2 tau = 4 tau = -tau,
   so Frob is conjugation and N(a + b tau) = a^2 - 2b^2.
2. (A): even powers tau^(2k) = J^k run over <2> = F_5^*; odd powers are
   tau J^k, the tau-translate; both sets have four elements and are
   disjoint, which exhausts the eight. An order-8 element x has x^2 of
   order 4, and the order-4 elements of F_5^* are exactly J and phi, so
   x^2 lies in {J, phi}; the four listed elements realize exactly these
   squares, and x^8 = 1 has at most eight roots in a field.
3. (B): conjugation fixes (a, 0) and negates (0, b); N(-x) = (-x)(-x)^5 =
   x x^5 = N(x).
4. (C): Frob(Y_n^+) = Frob(eta)^s2(n) = (-eta)^s2(n) = Y_n^-, using
   Frob(eta) = Frob(tau)^3 = -tau^3 = -eta.
5. (D): (-eta)^s = (-1)^s eta^s, so both branches agree exactly at even s;
   for even s, eta^s = phi^(s/2) lies in F_5; for odd s and t, eta^(s+t) has
   even total degree and equals phi^((s+t)/2) in F_5, and the branch signs
   (-1)^s (-1)^t = +1 cancel; for mixed parity the product is tau times a
   base unit (off-base) and the branch signs do not cancel.
6. (E): ord(2) = 4 gives the mod-4 law; ord(phi) = 4 makes phi^(e/2)
   injective on e in {0,2,4,6}; the same for pair sums; the witnesses are
   direct evaluations; (eta^s)^2 = phi^s = (2^s)^-1 = Theta^-1 at class s.

The proof, not the finite audit prefix, is the proposed basis for theorem
status at the frozen L1 scope.

## The six frozen fields

```text
EQUATION     Statements (A)-(E) exactly as written above. The novel content
             is the axes decomposition, the Galois identity of the branch
             involution, the branch-invariant record with its parity
             boundary, and the strict mod-8 refinement. Inherited
             RAMIFIED-TM-LIFT and SQRT-PHI-DIGIT-LIFT remain premises, not
             newly earned results.

CODE         verify.py, SHA-256
             542823134665618e8f1211aeabafafd22aa104654144bec8ac52ea72f56546d6
             (6217 bytes). Python standard library only; exact integer
             pairs; deterministic; no floats, files, network, or
             subprocesses. Run from the repository root with LC_ALL=C
             LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

CARRIER      theorem: all 25 elements of K, the full <tau>, both roots, and
             every n in N_0. Audit: all 25 elements for the field, axes,
             Galois, and norm gates; all exponent classes mod 8 for record
             and refinement; both digit branches with recursion against
             closed form and the Galois swap for 0 <= n < 2^16. No external
             dataset.

SYSTEMATICS  exact proof has no numerical approximation. Audit limitations
             are the frozen finite prefix and implementation correctness;
             they do not enlarge the all-n scope. Source material, not
             formal evidence: incubation candidate C-C8-BILINEAR-SHADOW-1
             (project lane, frozen and executed 2026-07-22: prereg sha256
             8f3a43a4..., verifier b4202774..., stdout 2298c8ca..., 28/28;
             independent break 13/13 survived, fcac728a.../66acab2f...),
             and one informal x86_64 dry run of this verify.py with stdout
             sha256
             cc194c8da06d4873d6b279bbc658d2aade71be70dfa877dbdb0ab892d15c3a62.
             A defect found in PREREG.md or verify.py after
             the pin invalidates this named probe: execution stops, neither
             frozen file is amended, and a new named probe and pin are
             required.

THRESHOLD    KILL the theorem candidate on any incorrect axes, order-8
             census, Galois, swap, record, boundary, or refinement
             statement; any counterexample in the declared carriers; a
             proof gap or dependency conflict; or any unreconciled FAIL in
             gates 01-06. A formal leg passes only with exit 0, empty
             stderr, all six PASS lines, the RESULT 6/6 ALL PASS line, and
             byte-identical stdout on the recorded aarch64 and GitHub
             x86_64 runs.

LAYER        L1 only. No state-to-manifold, boundary, support, stream,
             measure, clock dictionary, or force lift is asserted.
```

## Dependencies and scope firewall

Frozen theorem premises:

```text
PENTIT-ROOT-FACTS [T]      J=2, phi=3, and the exact tau root block in F_25
QUBIT-FROM-F5 [T]          the C4 -> C2 sign quotient
RAMIFIED-TM-LIFT [T]       Theta_n = J^s2(n), q(Theta_n) = theta_n
SQRT-PHI-DIGIT-LIFT [T]    the two-branch Y sequences and the branch law
```

`TIME-QUANTUM-TOWER [C]`, `METRO-TICK [T]`, and `FIB-ROOT-TIES [T]` are not
premises.

This probe does not select a sign branch, does not construct a canonical
selector, does not claim completeness beyond the stated record class, and
does not identify any state with a physical tick, spin, clock, or gravity
channel. The live SQRT-PHI-TIME-GRAVITY [O] obligation remains open and
untouched; a later reviewed fold may cite the record-class sign invariance
for its branch-equivalence clause, but that disposition is not part of this
probe.

Before the first formal execution, this file and `verify.py` must be
committed and pushed together. After that public pin they are immutable for
this probe.
