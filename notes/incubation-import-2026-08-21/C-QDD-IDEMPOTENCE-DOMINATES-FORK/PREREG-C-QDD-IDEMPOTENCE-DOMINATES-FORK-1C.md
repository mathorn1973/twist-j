# PREREG-C-QDD-IDEMPOTENCE-DOMINATES-FORK-1C (second correction)

```text
CANDIDATE: C-QDD-IDEMPOTENCE-DOMINATES-FORK-1C
HISTORY:   run 1  CF4 FIRED at CA6-02. Gate compared parameter tuples, not
                  operators. Diagnosis: the map (h, X) -> rho(h) X is 432 to
                  240; the surviving OPERATOR set was already exactly
                  {+Q_k, -Q_k}. Prereg 8bec4313.., verifier and stdout
                  archived unchanged.
           run 1B DF1 FIRED at DA3-01. The gate carried an un-preregistered
                  second conjunct, pool size greater than 1000. Diagnosis:
                  zero violating operators at every token; actual pool sizes
                  852, 952. Prereg 9e33bdd2.., verifier and stdout archived
                  unchanged.
           Both fired gates are defects in my own bookkeeping assertions, not
           in the mathematics. Both stay published. No threshold was moved.
           This prereg removes every assertion about bookkeeping and states
           only properties of the operators, plus set inclusions that name
           what the sweep must contain.
KIND:      incubation-lane candidate. NON-CANONICAL. No authority, no repo
           edit, no registry motion, no canon change, no fold.
BASIS:     Public Canon v57 ACTIVE, clone HEAD d44645a2, SHA256SUMS 5 of 5 OK.
LAYER:     L4 apparatus and support. No lift. O1 untouched.
DATE:      2026-08-20
```

## Falsifiers first

```text
EF1  GENERAL dead: some operator T in the swept family with T^sharp T = Q_k
     and Q_k T = T, other than +Q_k and -Q_k, satisfies T^2 = +T or T^2 = -T
     exactly, at any token.
EF2  SWEEP dead: some member of the swept family fails the effect equation or
     the support condition, so the sweep is not inside the family it claims,
     or the sweep fails to contain a named required subset.
EF3  ENLARGED dead: the surviving operator set of the enlarged fork family is
     not exactly {+Q_k, -Q_k} at some token.
EF4  CEILING dead: the run 1 regression gates CA1 to CA5, CA8, CA9 do not all
     reproduce; any disagreement between runs is itself a fired falsifier.
EF5  ROUTE dead: the independent breaker route disagrees with the verifier on
     any shared statement.
EF6  INTEGRITY: float in an assertion, nondeterminism, non stdlib dependency,
     runtime over 120 seconds per program, or target comparison before the
     last gate.
```

## Field 1. Equation

The LEMMA, derived by hand and unchanged from prereg 1B:

```text
If T^sharp T = Q_k and Q_k T = T then T restricted to W_k is a G-orthogonal
automorphism O and T = O Q_k with Q_k O = O Q_k on the support, so
T^2 = O^2 Q_k. Then T^2 = delta T with delta = +-1 forces O^2 = delta O, and
O is invertible on W_k, so O = delta identity and T = delta Q_k. Both signs
occur. No symmetry group enters.
```

```text
EA1 regression  run 1 gates CA1 to CA5, CA8, CA9 reproduce identically.
                                                               [candidate-T]
EA2 enlarged    the surviving OPERATOR set of {rho(h) X} is exactly
                {+Q_k, -Q_k} at every token; every surviving parameter tuple
                is affine; the tuple to operator collapse is reported as a
                measured number, not asserted against a threshold.
                                                               [candidate-T]
EA3 GENERAL     every swept operator satisfies the effect equation and the
                support condition, AND no swept operator other than +Q_k and
                -Q_k satisfies T^2 = +-T. The sweep is required to contain,
                as sets: the 48 normalizer members, the enlarged family
                operators, every Cayley operator from the declared grid, and
                every Cayley times normalizer product. Finite range.
                                                               [candidate-C]
EA4 structure   every swept T factors as O Q_k with O = T on W_k, and the
                machine-checkable half of the LEMMA holds on the sweep.
                                                               [candidate-T]
EA5 breaker     an independent route, 5x5 label-basis operators with equality
                tested modulo the all-ones kernel line, plus the
                Q direct-sum Q(i) coordinate algebra, reproduces EA1 CA5,
                EA2 and EA3 and records the adversarial attempts listed in
                Field 4.                                       [candidate-T]
```

## Field 2. Code

```text
verify_qdd_idem_dominates_1c.py   gates EA1 to EA4, own Fraction kernel, no
                                  import from any probe directory, target
                                  gate last.
breaker_qdd_idem_dominates_1c.py  EA5, independent representation and grid.
```

Python standard library only, Fraction and int only, no float, deterministic,
exit nonzero on any FAIL, each under 120 seconds, run from repository root
under LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

## Field 3. Carrier and frozen lists

As prereg 1B, unchanged: (Q^4, G); all five tokens; all 48 normalizer members
per token; circle list t in 0, 1, -1, 1/2, -2, 3, 1/3, -1/5, 7/2; Cayley grid
coefficients -2, -1, 0, 1, 2 on the declared three element G-skew basis;
products against all 48 normalizer members using the subgrid -1, 0, 1.
Breaker route additionally: wide circle t = p/q for p in -4..4 and q in 1..4,
deduplicated; and its own Cayley grid -3, -1, 1, 3 in the label basis.

## Field 4. Systematics and declared adversarial attempts

```text
S1 no assertion about counts of my own bookkeeping. Counts are printed as
   measured values inside gate labels only where the label states them as
   observed, never as a threshold.
S2 target gate last.
S3 sealed code is never imported; the reproduction leg is a subprocess.
S4 declared adversarial attempts, to be recorded whether or not they succeed:
   B1 search all 24 stabilizer elements at all five tokens for rho(h)
      restricting to minus the identity on W_k.
   B2 search the normalizer times the wide circle list for any operator
      beyond +-Q_k satisfying class level idempotence.
   B3 independent Cayley sweep in the label basis on its own grid.
   B4 attempt to satisfy T^2 = +-T while breaking only the support condition
      Q_k T = T, to confirm that support, not idempotence alone, is doing
      the work; a success here is not a falsification of EA3 and must be
      reported as a boundary of the LEMMA.
S5 a fired falsifier is archived and published, never repaired in place.
```

## Field 5. Failure threshold

Exact, no tolerance, no retry. PASS only if every declared gate passes
exactly. Any FAIL fires the matching EF and becomes the result.

## Field 6. Action layer

L4 apparatus and support. No lift. Only permitted output on success is
PROMO-C-QDD-IDEMPOTENCE-DOMINATES-FORK-1.
