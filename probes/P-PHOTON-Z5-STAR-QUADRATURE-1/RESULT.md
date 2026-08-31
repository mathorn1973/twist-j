# Result: exact five-phase star quadrature

Status: `C` proposed for the complete finite classification after required
reproduction; NON-CANONICAL until a separate reviewed fold.

Outcome: `CLASSIFIED / FAIL_HALF / PASS_UNIT`, subject to required exact-head
PR acceptance. Both frozen predicates are retained without modification.

## Complete finite result

Use exactly the polynomial class, principal embedding and coefficient
conventions in [PREREG.md](PREREG.md). For all 462 count vectors with total
degree zero through six, the exact classification is:

| Degree | Count | Maximum of abs(F)/D | Maximizer count |
| --- | ---: | --- | ---: |
| 0 | 1 | 0 | 1 |
| 1 | 5 | 0 | 5 |
| 2 | 15 | 0 | 15 |
| 3 | 35 | 0 | 35 |
| 4 | 70 | 0 | 70 |
| 5 | 126 | 1/2 | 1 |
| 6 | 210 | (82+50 sqrt(5))/361 | 5 |

Thus the sharp pointwise constant for the entire declared class is

```text
theta_star = (82+50 sqrt(5))/361,
1/2 < theta_star < 1,
abs(F) <= theta_star D,     D=C0+F>0.
```

Exactly five count vectors attain the global maximum, and exactly these
five violate HALF:

```text
(0,2,0,2,2)
(0,2,2,0,2)
(2,0,2,0,2)
(2,0,2,2,0)
(2,2,0,2,0)
```

For each of them,

```text
C0 = 79-29 sqrt(5),
F  = 4-4 sqrt(5),
D  = 83-33 sqrt(5).
```

The unique degree-five maximizer is (1,1,1,1,1), with C0=2,F=2,D=4.
Multiplicity counts phase-count vectors only, not ordered factor lists,
edge backgrounds or physical configurations. EXPECTED prints every
degree/global extremizer and every threshold counterexample.

## Fired falsifier and independent witness

At k=(2,0,2,0,2), take

```text
P(z)=(1+z)^2(1+zeta^2 z)^2(1+zeta^4 z)^2,
zeta=exp(2 pi i/5).
```

Direct expansion, independently checked in the accompanying
[conditional proof note](../../notes/canon/PHOTON-UNSIGNED-CURRENT-SUPPRESSION.md),
gives the C0,F,D above. Since F<0, HALF would require C0+3F>=0. Instead

```text
C0+3F=91-41 sqrt(5)<0,     91^2=8281<8405=5*41^2.
```

This exact written witness alone refutes HALF. Rationalizing abs(F)/D
gives theta_star, and

```text
1-theta_star=(279-50 sqrt(5))/361>0,
279^2 > 5*50^2.
```

The witness alone does not establish the global upper bound or exhaust all
maximizers; those conclusions consume the complete finite classification.
The sharper conjectured HALF bound is not relabelled as passing because
the separately frozen STRICT_UNIT predicate passes.

## Reproduction and provenance

The first formal Linux/aarch64 execution completed after public pin
66bcc0714cac5789292954bea300e398689ffd0a and its public receipt, with all
internal certificates passing, exit 0 and empty stderr. [RUN.md](RUN.md)
and [EXPECTED.txt](EXPECTED.txt) preserve the actual receipt and bytes.
Static independent code review preceded pinning; independent post-run
review checked the raw output against the written witness and scopes.

The code checks all 462 distinct vectors, degree counts, exact signs,
positive denominators, independent five-point evaluations, coefficient
identities, shift/reflection invariance and the preregistered positive
HALF saturation control. No floating point or external input is used.
Required PR jobs must reproduce byte-identical stdout on both declared
architectures at the exact head before merge. No local-only result is
represented as satisfying that gate in advance.

Analytic exposure, including a manually suspected HALF counterexample,
was disclosed in PREREG before pinning. This is an exact classification,
not blind confirmation. A fired falsifier is preserved as a result;
this completed probe is not abandoned and must not be reused or resumed.

## Scope boundary

This probe is L4 ONLY: finite algebraic factors and scalar quadrature.
It proves no probability, correlation decay, screening or phase theorem.
The separately written NON-CANONICAL conditional note consumes the finite
bound to derive unsigned current-cylinder inequalities under its explicit
finite-product-model assumptions and named conditional L4-to-L6 gate.
That application is not a change to this preregistration or its status.

Neither result adopts the physical action/state/source or closes
PHOTON-MASSLESS-PHASE or PHOTON-CONE-CONVERGENCE. The old KAPPA and WINDOW
claims remain terminal F. Canon, registry, evidence, dependencies, gates,
STATUS, tag, release and workflows are unchanged. No fold is performed.
