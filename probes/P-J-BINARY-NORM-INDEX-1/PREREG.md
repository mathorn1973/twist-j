# P-J-BINARY-NORM-INDEX-1 preregistration

Date: 2026-08-22

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No scientific
result is earned by this file. The accepted `verify.py` may be parsed, compiled
and inspected statically, but it is not imported or executed before this file
and `verify.py` are committed together, pushed, and read back byte for byte
from the public remote.

Public claim lock: issue 522, opened before this file was committed.

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v60
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v60
CONTENT_COMMIT: 18b21bdaf2c2236c9444b120900277ccfb63e050
CANON_SHA256:   9387b75f2036ac6aff5737255956b93fb9b906511b8184ae4c1c999e8ed46db0
CANON_BYTES:    329876
BASE_COMMIT:    41754210a3a0e70b52f98988e566a73bba9b9666
LAYER:          L1 exact arithmetic only
```

Gate performed against a clean clone of public `main`, not an attachment and
not a rendered page: `canon/SHA256SUMS` five of five OK, the recomputed hash
and byte count of `canon/CANON.md` equal the declared fields, and both
`canon-v60` and the content commit are ancestors of `main`. `BASE_COMMIT` is
the head of `main` at lock time and is the parent of the pin commit.

The probe changes exactly `probes/P-J-BINARY-NORM-INDEX-1/`. Canon, registry,
frontier, evidence, gate, release and workflow files are excluded.

## Collision search

Searched before drafting: open and closed issues, remote branches, `probes/`,
and the registry. No issue, branch, probe path or claim named
`P-J-BINARY-NORM-INDEX-1` or `J-BINARY-NORM-INDEX` exists at lock time.
Adjacent public objects, named here so that no reader mistakes this for a move
on any of them:

```text
J-BINARY-NORM-DESCENT [T]             the parent lane, issue 499, PR 500. It
probe/P-J-BINARY-NORM-DESCENT-1       already owns O/(2) = F16, the norm-trace
                                      form of the reduction, the A4/2A4
                                      isometry, the negative theorem
                                      bar(D_J) != Frob_2, and the controls
                                      showing that field integrity modulo two
                                      does not uniquely select J or
                                      characteristic two. This probe recounts
                                      none of that. Its new content is one
                                      index lemma and one order statement.

issue 398                             P-J-NORM-VERTICAL-AMPLIFICATION-1, open
                                      and unpinned, no probe directory. Its
                                      object is the RELATIVE norm
                                      N_(K/K+)(x + Jy) as a binary quadratic
                                      form at completely split primes
                                      p = 1 mod 5. This probe is about the
                                      ABSOLUTE norm N_(K/Q) = 1 and residue
                                      fields at INERT primes. Disjoint objects,
                                      disjoint prime classes, no shared claim
                                      identifier. Not touched.

issue 503                             the canon cleanup lock over the carry and
                                      J-binary material. It blocks Canon
                                      writes, not probes. This pull request
                                      changes only its own probe directory and
                                      no canon/ file. The later fold that would
                                      register the rows below lands in the same
                                      Canon area and must be sequenced through
                                      503, not around it.

notes/C-RH-WEIL-NORM-JUNCTION-1-N     issue 374. Analytic and operator
                                      theoretic; its word "norm" is a pairing
                                      on zeta zeros, not N_(K/Q). Not touched,
                                      not cited as support.

notes/C-J-LI-RA0-FROBENIUS-SQUARE     RECON, FIRED. Its word "Frobenius" is an
                                      Euler-product operator route. Not
                                      touched. A fired analytic route is not
                                      revived by anything here.

J-UNIT [T], J-MAHLER-MEASURE [T]      already carry N(J) = 1 and the minimal
                                      polynomial. Imported, not re-derived.
```

### Compatibility with the parent negative theorem

`J-BINARY-NORM-DESCENT` denies that field integrity modulo two selects `J` or
characteristic two. This probe asserts no such selection either. Its
Theorem A is a statement about the order of `F_p^x`, generic in every field
degree by A3, and its Theorem B is Galois invariant across all four
`1 + zeta_5^a` by D2. What is stated is only that the question "can a norm-one
unit generate the inert residue field" has a positive answer at `p = 2` and a
negative answer at every other inert `p`. Reading that as a selector for the
axiom, for the exponent, or for characteristic two is outside scope and is a
STOP condition of this preregistration.

## Result exposure

RESULT-EXPOSED, not blind. The two theorems and the finite census below were
derived and exercised in non-canonical incubation work on this same date, by
two implementations with different representations, and recorded there as an
audit. Those bytes, runs and outputs are discovery context only and are not
evidence. The accepted `verify.py` here is a fresh implementation in repository
output form and has never been imported or executed at the moment of this pin;
it carries the residual implementation risk that the pin deliberately forbids
pre-testing. The census constants 2, 3 and 156 appear inside `verify.py` as
preregistered thresholds, which is what preregistering a finite census means.

## Field 1: equation

Let `K = Q(zeta_5)`, `O_K = Z[zeta_5]`, `N = N_{K/Q}`, `Phi_5 = 1 + x + x^2 +
x^3 + x^4`, and `J = 1 + zeta_5^2`, so `(J - 1)^3 = zeta_5` and `N(J) = 1`.

### L1 residue field

For a prime `p` with `ord_5(p) = 4`, equivalently `p = 2` or `p = 3` mod 5,
`Phi_5` stays irreducible over `F_p`, `(p)` is inert, and

```text
O_K/(p) = F_p[x]/(Phi_5) = F_(p^4),
```

with Frobenius `y -> y^p` generating its Galois group over `F_p`.

### L2 norm descent

The residue norm is `N_(F_(p^4)/F_p)(y) = y^(1 + p + p^2 + p^3)` and reduction
commutes with it, so for `u` in `O_K`,

```text
N_(F_(p^4)/F_p)(ubar) = N(u) mod p.
```

Hence `N(u) = 1` forces `ubar` into the kernel of the residue norm.

### L3 index

The residue norm is surjective onto `F_p^x`, so its kernel is cyclic of order

```text
(p^4 - 1)/(p - 1) = (p + 1)(p^2 + 1) = 1 + p + p^2 + p^3,
```

and its index in `F_(p^4)^x` is exactly `p - 1`.

### Theorem A, uniqueness of the binary place

By L2 and L3, a unit `u` of `O_K` with `N(u) = 1` can have `ubar` generating
`F_(p^4)^x` only when `p - 1 = 1`, that is only at `p = 2`. At every other
inert prime `ord(ubar) <= (p + 1)(p^2 + 1) < p^4 - 1`.

### Theorem B, attainment

At `p = 2`, `ord(Jbar) = 15 = |F_16^x|`, so `J` realizes the one possibility
Theorem A leaves open. Proof: `J^3 = x^3` has order five, `J^5 = x^2 + x^3 = a`
with `a^2 + a + 1 = 0` has order three, so the order is divisible by three and
by five and divides fifteen.

### Remark 1, no selection

The four elements `1 + zeta_5^a` are one Frobenius orbit, `J, J^2, J^4, J^8`.
Generating `F_16^x` is therefore Galois invariant and selects no exponent `a`.
This is the same conclusion the parent row already records for field integrity
modulo two, reached on a second invariant.

### Remark 2, the mechanism is generic

The index in L3 is `p - 1` for every field degree, so Theorem A is a statement
about `F_p`, not about `J`, not about the prime five, and not about degree
four. Only Theorem B is specific to `J`.

### Claim C, finite census

The Galois-invariant sharpening asks whether `ubar` generates the whole
norm-one subgroup rather than the whole group. Among the 156 primes inert in
`K` below 2000, `Jbar` generates it exactly at `p = 2` and `p = 3`. This is a
finite-range statement and is claimed at `C`, never above it.

## Field 2: code

Accepted file:

```text
probes/P-J-BINARY-NORM-INDEX-1/verify.py
```

Standard library only, and in fact no import at all; integers and integer
coefficient tuples only. No float, no complex, no approximation, no randomness,
no network, no subprocess, no external data, no import of incubation or scratch
material, no filesystem read or write, and no read of `canon/`. Zero arguments.
Deterministic stdout with no environment, platform, timing or path field, so
stdout is byte-identical on every architecture. Empty stderr. Exit zero on a
clean pass and nonzero on any fired check.

## Field 3: carrier

```text
field:            K = Q(zeta_5), O_K = Z[zeta_5]
element:          J = 1 + zeta_5^2, carried as the tuple (1, 0, 1, 0)
residue model:    F_p[x]/(Phi_5) as coefficient 4-tuples mod p
census range:     every prime inert in K below 2000, of which there are 156
norm-path range:  every such prime below 300, for the two independent norm
                  routes
controls:         zeta_5 itself, of norm one and order five at p = 2;
                  w = 2 + zeta_5, of norm eleven, which is not confined to the
                  norm-one subgroup; and the degree ladder 2, 3, 4, 6, 8 for
                  the genericity of the index
```

No external data.

## Field 4: systematics

No tolerance anywhere: every assertion is an exact equality of integers or of
integer tuples. Known hazards and their controls:

```text
"the exponent 2 in the axiom is the reason"   block A3 shows the index is p-1
                                              in every degree, so the mechanism
                                              is not about J, five, or four
attainment read as selection                  block D2 is the Galois-orbit
                                              control, and the parent row is
                                              quoted rather than moved
finite census read as a theorem               claim C is labeled C, its range is
                                              in the row, and no summary may
                                              exceed it
one norm route trusted alone                  blocks B1 and B2 are the Frobenius
                                              product and the exponent path and
                                              must agree
any zeta, Dedekind, Artin, Weil or Riemann    out of scope entirely. This probe
statement                                     makes none. Named because the
                                              discovery context was an audit of
                                              a text that did make them.
```

Runtime limit 120 seconds. Float in an assertion, pre-pin execution, post-pin
mutation, an unnamed layer lift, or any sentence reading Theorem B as a
selection of the axiom exponent or of characteristic two is STOP.

## Field 5: failure threshold and decision

Thresholds never move after this pin.

```text
J-BINARY-NORM-INDEX-CONFIRMED
  every check passes: the residue-field and irreducibility pins hold, the index
  of the norm-one subgroup is p - 1 at every inert p in range and in every
  tested degree, p = 2 is the only inert p in range where that subgroup is the
  whole group, both norm routes return one and agree, ord(Jbar) = 15 at p = 2
  by exhaustion, p = 2 is the only inert p in range where ord(Jbar) = p^4 - 1,
  all four 1 + x^k have order fifteen and are one Frobenius orbit, the census
  set is exactly {2, 3} with 156 inert primes in range, and both controls hold.

J-BINARY-NORM-INDEX-FIRED
  any check fails. First-class outcome: the run is recorded and merged, the
  probe is closed, and no threshold is adjusted.
```

The candidate falsifiers, one line each:

```text
an inert p > 2 and a unit u of O_K with N(u) = 1 whose reduction generates
F_(p^4)^x; an exponent n < 15 with Jbar^n = 1 in F_16; an inert p at which the
index of the residue norm kernel is not p - 1; an inert p at which the two norm
routes disagree or either fails to return one; a third prime below 2000 at
which Jbar generates the whole norm-one subgroup, or a failure at 2 or 3; a
Galois-invariant condition separating 1 + zeta_5 from 1 + zeta_5^2.
```

Maximum later rows, claimed only at the earned status and scope:

```text
J-BINARY-NORM-INDEX          [T]  L1
J-BINARY-NORM-ORDER-CENSUS   [C]  L1, finite range below 2000
```

The first rests on the written proof of L1 to L3 and Theorems A and B; the
verifier audits it. The second is finite-range computation and stays at `C`.
Neither creates a selector, a decoder, an apparatus, an event, or a measure,
and neither may be summarized beyond that scope.

## Field 6: layer

`L1` state only. No `L2` manifold, `L3` boundary, `L4` support, `L5` stream or
`L6` measure statement is made, and no lift is named or attempted. No zeta
function, no Dedekind zeta, no Artin factorization, no Weil conjecture and no
Riemann hypothesis statement is made anywhere in this probe.

```text
SAMPLING NOT PROVIDED.
```

## Formal order

`PREREG.md` and `verify.py` are committed together and pushed; both are read
back byte for byte from the public remote into a separate clean checkout; one
formal run from the repository root of that checkout; `EXPECTED.txt`, `RUN.md`
and `RESULT.md` are added without changing the pin; one probe-only pull
request; byte identity on x86_64 and aarch64; aggregate `check`; merge with a
merge commit only. Registry, frontier and Canon treatment is a separate later
fold and is sequenced through issue 503.
