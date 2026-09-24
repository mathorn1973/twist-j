# ADDENDUM 1 to PREREG-C-PHOTON-CONTRAST-DRIFT-N

Status: NON-CANONICAL. Written 2026-09-22 about 22:24 CEST, while the 20
chains were still thermalizing and before any of their measurements existed or
were read. It does not change the equation, code, data, gates, rule or
terminals of the frozen preregistration (sha256
3a86ca2f0e771ffbeacd77004443953697cf03369f5e853630766c29489ffa62). It narrows
how one terminal may be read, because of a limitation found after the freeze.

## Limitation

The drift statistic compares the contrast at the smallest momentum with the
plateau of the larger momenta. A drop below the plateau at both L = 24 and
L = 32 is what a light mass predicts. It is also what a Coulomb phase with a
scale-dependent coupling predicts: large monopole loops near the confinement
edge can lower the long-distance contrast to a smaller plateau, around the
momentum scale set by the loop size. An analytic form Z + c s cannot make this
drop, because Delta is flat within errors from s = 2 down to s = 0.27 and
falls only below that. A crossover to a lower plateau at a small momentum
scale can make it.

The two readings differ in whether the contrast keeps falling between
L = 24 and L = 32. The B3 massive fit predicts Delta_32(1) - Delta_24(1) of
about -0.017. A lower plateau predicts about 0. With the planned statistics
this difference has a standard error of about 0.009, so this probe cannot
separate the two at 3 sigma. That would take L = 40 to 48, or many more
chains.

## Narrowed reading

DRIFT_CONFIRMED reads only as: the contrast at s below about 1/4 lies
reproducibly below the large-momentum plateau, in independent chains, at
L = 24 and at L = 32. It does not by itself choose a mass over a lower
Coulomb plateau. The phrase "P1 at t = 1 is in doubt at engineering grade" in
the frozen reading is to be read as "not settled by this probe". It is not
evidence against P1. Under a lower plateau near 0.58, P1 would still hold with
a wide margin.

NO_DRIFT, MIXED and STOP_DRIFT: readings unchanged.

The difference Delta_32(1) - Delta_24(1) and its standard error will be
reported as a by-product without decision weight.
