# Contraction and reconstruction audit

## Frozen objects

The evaluator uses the four descriptors verbatim:

```text
D0 = (1032, 2301, 3210)
D1 = (1032, 2310, 3201)
D2 = (1230, 2301, 3012)
D3 = (1230, 3012, 2301)
```

For colour `q`, the direct factor `A_r` carries wire `(q,r)`.  The conjugate
factor `B_s` carries `(q,sigma_q^{-1}(s))`.  Thus the code realizes exactly
the preregistered orientation “colour-q edge maps tensor copy r to conjugate
copy sigma_q(r)”.  A startup assertion checks that every one of the sixteen
wires occurs exactly twice.

## Independent modular network

The preregistered generic tree is not used.  The modular evaluator is a
frontier dynamic program in the order

```text
A0, B0, A1, B1, A2, B2, A3, B3.
```

A state is the lexicographically ordered assignment of the open boundary
wires.  Adding a factor looks up only support entries compatible with already
assigned wires, multiplies their coefficient modulo 241, sums equal new
boundary states, and removes every newly closed wire.  All keys, factor
supports, and iterations are deterministic.  The maximum boundary rank is
eight, as required, but support sparsity and modular aggregation reduce the
work to the following transition counts:

| target | D0 | D1 | D2 | D3 |
|---|---:|---:|---:|---:|
| golden | 594,141 | 598,152 | 444,507 | 438,931 |
| sym | 2,084,940 | 2,084,454 | 2,440,044 | 2,430,324 |
| sparse | 1,503,792 | 1,502,352 | 2,432,790 | 2,428,812 |

This is far below the preregistered dense fallback of about 122 million
multiply-adds per core.

## Distinct direct replay

Every prospective witness is replayed by a second algorithm.  It performs
depth-first compatible-tuple enumeration, without frontier aggregation, in
the different order

```text
A3, B1, A0, B3, A2, B0, A1, B2.
```

For the frozen first witness D0, the leaf counts are:

| target | compatible 8-factor tuples | mod-241 sum |
|---|---:|---:|
| golden | 107,688 | 209 |
| sym | 2,385,072 | 171 |
| sparse | 2,437,776 | 171 |

The direct residues agree with the frontier-DP residues for all three
replayed targets.

## Exact reconstruction

Golden leaves are accumulated into 561 nonzero integer bins
`N(n_a,n_b,n_c,E)` with `E in Z/20`; their total count is 107,688.  Only
after enumeration are the frozen elements `a,b,c` and `xi^(6E)` evaluated
in the 32-dimensional rational power basis of `Q(zeta_120)`.

Artisanal leaves are accumulated in the exact two-dimensional ring
`Z[zeta_6]`, using `zeta_6^2=zeta_6-1` and conjugation
`bar(zeta_6)=1-zeta_6`.  Both D0 numerator sums are
`287214336 + 0*zeta_6`; division by `6^8=1679616` gives exactly `171`.

The exact difference convention is `golden - target`.  For both targets its
coefficient vector in the basis `1,xi,...,xi^31` is

```text
[-57/4,0,0,0,0,0,3,0,3/2,0,0,0,3/2,0,0,0,
 0,0,-3,0,0,0,0,0,0,0,0,0,-3/2,0,3/2,0].
```

Substitution `xi -> 3 mod 241` gives `38`, exactly matching
`209-171 mod 241`.  The nonzero residue proves the cyclotomic element is
nonzero; this is a rigorous exact inequality certificate.

## Integrity gates and scope

- golden source pins: pass;
- parsed support sizes: golden 112, sym 180, sparse 180;
- three `2|2` flattenings for each target over F241: pass;
- frozen `GL(2,F3)` action: 24 distinct function tables for each artisanal
  representative;
- all twelve D0--D3 modular contractions completed;
- both first frozen mismatches exactified and independently replayed.

This package is deliberately a third audit of contraction correctness,
efficiency, and exact witness reconstruction.  It does not replace the
primary verifier's full exact G0/G1 construction audit.

