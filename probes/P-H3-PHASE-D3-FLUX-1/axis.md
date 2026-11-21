# Axis-supported radiation from one native site

Use the origin with both coordinates even and matching bit zero.
The material center is zero and its half-gap is 1. Use a radiation
center `c=1+2rho+2rho^2` and half-gap `f=J` in the B1 arm or
`f=J^-1` in the B2 arm. Every other site is vacuum. Since
`c=1 mod 2` and neither selected gap is 1 modulo 2, both radiation
words and both matter words have nonzero residues modulo 2. All
first C contacts with vacuum are refused. The first B gives matter
half-gap J or J^-1 and radiation half-gap 1, so the emitted CLK
and CORR are `c+1` and `c-1`. Conjugation sends c to -c, making
their exact Hermitian weights equal and nonzero. In the next C, both
words are even, so the contact with vacuum sends
`(1-rho)(c+1)/2` to (0,-1) and `(1-rho)(c-1)/2` to (-1,0),
respectively. The neighbor Hermitian weights are again equal and
nonzero. These readings are taken after C and before B.

At every later cut the matter half-gap stays a product of powers of
J with initial half-gap 1. Its residue remains nonzero mod 2 because
J is a unit. Both material contacts into vacuum always refuse, and
a site with zero material gap cannot have an active B. Thus B can
mix radiation rails only at the origin, where their vertical and
horizontal axes intersect. C moves CLK only along its column and
CORR only along its row. Induction at both substeps confines all
radiation to the union of these two axes indefinitely, including
returning field and further source B events. The argument also
applies to the corresponding axes on a periodic torus.

For both arms the checker uses a 24 by 24 torus and ten native steps.
It verifies all inverse steps and complete accounts, records the
first source B and next-C neighbor words and weights, and checks
absolute axis support in both full substeps. An off-axis word, an
altered first event, or a failure of the displayed exact neighbor
law is a recorded falsifier. Inverse or account failures are
integrity failures.

This admissible native point preparation has emission and excludes
a universal all-directions spherical native emission law for such
point preparations. It does not classify multi-site sources,
additional decoders, or a separate continuum or D3 carrier. The
material source and the two emitted rails have no assigned
physical charge or polarization in this test.
