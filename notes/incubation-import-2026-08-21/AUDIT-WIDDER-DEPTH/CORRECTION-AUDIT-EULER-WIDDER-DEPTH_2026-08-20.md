# CORRECTION: owner review of AUDIT-EULER-WIDDER-DEPTH, both errors confirmed

```text
Status      NON-CANONICAL correction by addendum to the Widder audit. The
            published audit record and its handoff directory are not edited;
            this correction stands beside them. RH remains O. Canon v57
            untouched; current main d44645a2 carries only QDD probe
            additions since the v57 activation, normative delta zero.
Session     AUDIT-EULER-WIDDER-DEPTH, leg 2 and leg 2B, 2026-08-20.
Input       the owner review deriving from issue #477 and branch
            notes/c-rh-widder-angle-sweep-correction-1-n (head 5d89e26c,
            integrity STOP before verifier execution, verified below).
Disclosure  RESULT-EXPOSED / IMPLEMENTATION-INDEPENDENT / NOT BLIND.
Decision    both owner corrections CONFIRMED by independent exact
            computation, including the counterexample to the exact reduced
            fraction; the finite-prefix no-go CONFIRMED; one gate of leg 2
            fired on an audit-code representation defect and was closed by
            leg 2B, 5/5.
```

## 1. What was wrong in my audit, precisely

Two auxiliary claims, both mine, both now corrected with the owner's
formulations adopted.

First, the per-level sign criterion. I wrote: the pair contribution P_k is
negative for some u > 0 iff Re[(A - iB)^k] < 0. That is FALSE for general k.
The swept angle k(2 phi - theta) covers the open interval (-k theta,
k theta); once k theta exceeds pi/2 the negative cosine window is inside the
sweep FOREVER, while the endpoint power (A - iB)^k can return to the right
half-plane. Verified counterexamples:

```text
A = B = 1, k = 8:  Re[(1-i)^8] = 16 > 0, yet
    P_8(1,1;1/2) = -172056926056081143103488000/51185893014090757 < 0,
    the owner's exact reduced fraction, matched digit for digit.   [CG1]
A = 2, B = 1, k = 14 (non-resonant): Re[(2-i)^14] = 76443 > 0 while
    Re[(2-i)^4] = -7 < 0, and u = 3/8 is an exact negative witness. [CG3]
```

The corrected criterion, adopted:

```text
P_k < 0 somewhere  iff  k theta > pi/2  iff  some j <= k has
Re[(A - iB)^j] < 0.
```

The prefix form is equivalent because theta < pi/2 always: the first j with
j theta > pi/2 lands in (pi/2, pi), where the cosine is negative. Verified in
both directions on the declared grid, 83 prefix-negative cases each carrying
an exact rational witness. [CG4]

Second, the depth law. My ceiling form fails exactly at resonance, where
pi/(2 theta) is an integer. The correct form, adopted:

```text
k_min = floor(pi/(2 theta)) + 1 = min{k >= 1 : Re[(A - iB)^k] < 0}.
```

At A = B = 1 the integer certificate (1-i)^4 = -4 fixes theta = pi/4 with no
transcendental input; the level-2 sign polynomial is EXACTLY

```text
Re[(1-i)^2 ((u+1)+i)^4] = 8u(u+1)(u+2),
```

positive on (0, infinity), zero only at the boundary u = 0, so the resonant
level never goes negative at finite u and k_min = 3, not 2. Verified by two
independent routes (normalized symbolic expansion; five-point evaluation
certificate at degree bound four). [B2-02, B2-03, B2-05]

One mitigating fact, stated for accuracy, not excuse: my verifier's
kmin_isolated used the min-Re form, which IS correct including resonance. So
the 38-row depth table, the owner control points 2 and 32, and every number
the first audit printed remain correct; the false statements lived in the
prose and the prereg, and my gates could not catch them because nothing
tested levels above the first crossing. That gate-design gap is the real
lesson: the audit tested exactly the region where its own claim was true.

## 2. What stands, and what is strengthened

Everything else of the first audit stands: the pole calculus, unconditional
f > 0 and W_1 > 0, the depth table, the vacuity theorem and the safe-level
bound (both are first-crossing statements and use the correct form; at
gamma >= 1 the strict chain B < A gives 2 theta < pi/2 strictly, so W_2 >= 0
unconditionally survives unchanged), and the strategic conclusion.

The owner's strengthening is confirmed and supersedes my masking argument:

```text
[candidate-T inputs verified; quantifier by the corrected sweep theorem]
For rho_N = 3/4 + iN: A_N = N^2 + 3/16, B_N = N/2, and the exact chain
B_N/A_N < 1/(2N) gives k theta_N < 1/2 < pi/2 for every k <= N. One
symmetric off-critical configuration alone passes the first N Widder
levels as full functions of u. No finite prefix of the hierarchy
characterizes RH in the symmetric pole class. No masking needed. [CG6]
```

My leg-1B masking result remains true but is now the weaker statement: it
needed a background; the prefix no-go needs nothing. Together with W_1 > 0
against W_2 < 0 at rho = 9/10 + i/2 [CG7], level-to-level induction on a
single pair is dead, and the surviving routes are exactly the owner's two:
construct the positive Stieltjes measure directly, or produce one global
Euler and archimedean object yielding every level at once. The three-wall
pattern (Toeplitz support, Hankel height horizon, Widder prefix horizon)
gains its cleanest instance: here the horizon statement is a theorem, not a
measurement.

## 3. The owner's STOP, verified from the remote

```text
branch notes/c-rh-widder-angle-sweep-correction-1-n, head 5d89e26c;
STOP.md present and reporting: formal verifier NOT RUN, breaker executed
once (652 B stdout, sha a0e838a6..), no scientific result earned;
the remote accepted-verifier blob is 98973ce7a5895e7b63a8f1ecd9c45c561ca525fc,
byte-equal to the mismatch value in the STOP record, consistent with the
recorded local frozen blob 98b64b9b.. differing. The STOP is properly
first-class; any formal return needs a fresh identity, as the review states.
```

This correction is a notes-grade addendum and does not perform that formal
return.

## 4. One fired gate of this correction, archived

Gate CG2 of leg 2 fired on an audit-code representation defect: the
polynomial equality test compared a computed coefficient list carrying one
structural trailing zero (length from the product shape) against a length-4
target. The mathematics was right; the comparison was wrong. Same defect
class as leg 1's A3-07 Horner trailing zero, which is itself worth recording:
two of two polynomial-identity gates in this audit series failed first on
list-length hygiene. Leg 2B closed it with lengths normalized plus an
independent five-point evaluation certificate, 5/5 PASS. The pinned leg-2 run
stands as recorded, 7/8, exit 2.

## 5. Run record

```text
environment  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
             TZ=UTC; Linux x86_64; CPython 3.11.15. Single platform,
             candidate labels only. Prereg and program frozen together
             before each run, ast.parse only, one run per leg.
leg 2        prereg aafb86fbea371cd1e4001cce1959a6b834c313a7b54105503a19e102345f896d (6558 B)
             code   4b6540004498c957c33ea54e6c45b6ab913a105cebd16902e4fdea72ed017484 (10531 B)
             stdout 523ef2a3d98244592cdf463234c2905bc2802a2a3c714729f94a1a7e38757ed4 (1628 B)
             7/8 PASS, CG2 fired (representation defect), exit 2
leg 2B       prereg 799ae461fb3b57af1c6d4e00a0412d51b77081210851f30c0a88933c520fe5b4 (1357 B)
             code   5297da6c658acf83297c81ac256acf6cd299c9ecc6498f418a606cf413d22e7a (2853 B)
             stdout 93efc7a0e0ad409c6837fb28ca9cee2cc2a9e030a25aff09eaa6fcf0700560b2 (602 B)
             5/5 PASS, exit 0
pins         AUDIT_PIN-WIDDER-2.txt 7ddf28d3.., AUDIT_PIN-WIDDER-2B.txt e072d167..
witnesses    (2,1,k=14): u = 3/8; (rho = 9/10 + i/2, W_2): u = 1/1000;
             83 prefix-negative grid cases each with an exact witness.
```

## 6. Scope firewall

L6 only, candidate grades only, single platform. Nothing here moves RH, the
owner's STOP, or any public row. The QDD side notes of this session are
unaffected; the two new sealed probes on main (record-complete stabilizer,
naturality fork) carry the positive conditional branch the owner describes,
and O2 remains open because record-partition completeness is an added
physical premise, exactly as the review states.
