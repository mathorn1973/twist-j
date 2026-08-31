# Result: FCC global remainder and exact zero locus

Status: `T` proposed by exact proof; non-canonical candidate until a separate fold.
Outcome: `REMAINDER-PROVED`, subject to required exact-head PR acceptance.

## Earned mathematical scope

For precisely the five complete weighted shells and normalization frozen in
PREREG, put r=|k| and s(k)=L(k)/324. The self-contained proof establishes,
for every real k in R^3,

```text
0 <= r^2-s(k) <= (11/27) r^4,
0 <= s(k)-r^2+(11/27) r^4 <= (38/405) r^6,
0 <= s(k) <= 16/9,

s(k)=0 iff
k in 2 pi Z^3 union (pi(1,1,1)+2 pi Z^3).
```

For every epsilon>0 and s_epsilon(k)=s(epsilon k)/epsilon^2,

```text
0 <= r^2-s_epsilon(k) <= (11/27) epsilon^2 r^4,
0 <= s_epsilon(k)-r^2+(11/27) epsilon^2 r^4
  <= (38/405) epsilon^4 r^6,

sup_(|k|<=R) |s_epsilon(k)-|k|^2|
  <= (11/27) epsilon^2 R^4, for every R>=0.
```

Thus the rescaled spatial symbol converges compact-uniformly to |k|^2.
No sharpness claim for the constants is made.

The proof uses the global scalar second-derivative chain with zero initial
data and evenness, positive weighted summation, the explicit nonnegative
sextic polynomial gap, the complete support span D3, both inclusions of
its reciprocal zero lattice, and exact positive-epsilon substitution.
Finite samples of k or epsilon are not used as a universal proof.

## Exact audit and falsifiers

The first formal run at the public preregistration pin completed with all
16 gates passing, exit 0 and empty stderr. EXPECTED and RUN contain its
actual bytes and neutral environment receipt. The accepted code, proof and
thresholds remain identical to the pin.

The independent negative controls were all rejected by their respective
exact certificate predicates: altered weight, missing shell vector,
incorrect scalar sign, incorrect remainder constants, incorrect dual
basis despite unchanged residue classes, and incorrect scaling exponent.

No frozen mathematical falsifier fired. No missing execution was hidden,
no threshold moved, and no failed result was reclassified. All conclusions
and constants were analytically exposed before pinning, as disclosed in
PREREG; the run is reproducible proof auditing, not blind confirmation.

The required PR architecture jobs must reproduce these same bytes at the
exact head before merge. This result does not claim that the local run alone
is a two-architecture computation gate.

## Boundary preserved

The result is L2 ONLY. It strengthens the analysis of the one displayed
abstract spatial symbol. It does not select a physical carrier, quotient,
weights, flux, normalization or temporal rule. Its two zeros on the
displayed Z^3 Fourier torus are not two photons or two polarizations.

It supplies no spacetime cone identification, physical continuum limit,
Gibbs state, massless phase, propagator, decoder, apparatus or SI readout.
PHOTON-CONE-CONVERGENCE and PHOTON-MASSLESS-PHASE remain open;
PHOTON-KAPPA-LEMMA and PHOTON-WINDOW-PROOF remain terminally falsified.

The sealed SYMBOL-1 predecessor is unchanged. No Canon, registry, evidence,
dependency, gate, status, tag or release file is modified. Promotion of this
new exact scope requires a separate reviewed public Canon fold.
