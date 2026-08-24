# P-RECORD-QUOTIENT-CALCULUS-1 result

Date: 2026-08-22

~~~text
DECISION:   RECORD-QUOTIENT-CALCULUS-CONFIRMED
CHECKS:     31 of 31 PASS, exit 0, empty stderr
PIN:        8a1386ad95ef7210a0d4f957f1fd3e0ae76c1a33
CLAIM LOCK: issue 524
LAYER:      L1 exact arithmetic only
BASIS:      Public Canon v60, tag canon-v60, content 18b21bd,
            CANON_SHA256 9387b75f...d46db0, CANON_BYTES 329876
~~~

No threshold moved after the pin and no falsifier fired. Nothing in this
directory changes canon/, the registry, the frontier, a release or any live H
or O row. A fold is a separate later act and remains sequenced through issue
503.

## 1. Question

For R=Z[zeta_5] and a nonzero proper ideal

~~~text
I = product over P in Supp(I) of P^(e_P),
~~~

what part of the finite quotient R/I is fixed by prime support, what part is
carried by the exponents, and which unital R-algebra reductions between such
quotients are possible?

The load-bearing convention is n_I=rad(I)/I and n_I^0=R/I.

## 2. Earned result

~~~text
RECORD-QUOTIENT-CALCULUS  [T]  L1, exactly clauses R1-R6 of PREREG.md
~~~

The status is earned by the complete written proof in PREREG.md plus the exact
formal audit. This probe does not write the registry; registration is a later
separately locked fold.

The theorem packet is:

1. CRT decomposes R/I into local prime-power factors. A commutative local ring
   has only idempotents zero and one, so

   ~~~text
   Idem(R/I) ~= P(Supp(I))
   ~~~

   canonically as Boolean algebras. The atoms are labelled by the prime ideals
   themselves; no ordering is used.

2. Reduction R/I -> R/rad(I) is bijective on idempotents. The exponent vector
   is invisible to the Boolean layer.

3. The exact layer orders and Loewy length are

   ~~~text
   |n_I^k/n_I^(k+1)| = product {N(P):e_P>k},
   L(R/I) = max_P e_P.
   ~~~

   These are order statements only. No module decomposition is claimed.

4. A unital R-algebra map R/I -> R/J exists exactly when I is contained in J
   and is then the unique canonical projection. The category is thin. If the
   inclusion is strict, the quotient has no unital R-algebra section.

5. For I_L=(lambda)^L(2), L>=1, the support, radical, reduced ring
   F_5 x F_16 and four-element Boolean algebra are constant, while the Loewy
   length is L and is unbounded. Therefore neither the Boolean skeleton nor the
   reduced record determines filtration depth.

## 3. Why the universal statement is T

The verifier is deliberately finite. It audits eleven ideals, every one of the
64 ordered Hom pairs in its norm-bounded family, and I_L for L=1 through 5.
Those data alone would be C and could not establish the word unbounded.

The universal quantifiers instead rest on seven exact proof steps: Dedekind
ideal factorization; CRT; the local-idempotent lemma; reduction of local
factors; the norm ratio for successive prime powers; the fact that an
R-algebra map is fixed by the structural image of R; and the prime
factorization of (lambda)^L(2). The machine audit exercises every formula,
the convention and the failure controls on the frozen carrier.

## 4. Load-bearing controls

All passed.

~~~text
PRIME SUPPORT
  R/(11) has four prime factors and sixteen idempotents, whereas R/(6) has two
  and four. The Boolean map is checked as a bijection with meet, join and
  complement, not as a cardinality coincidence.

KERNEL
  For every selected prime ideal, the verifier checks that the constructed
  ideal lies in the kernel of residue reduction and that equal finite indices
  identify the kernel exactly.

RADICAL MAP
  The verifier first checks I is contained in rad(I), then independently
  enumerates source and target idempotents before asserting a bijection.

LOEWY ORIGIN
  Layer zero is R/rad(I). The wrong n^1 start produces [5,5,5] for (10),
  against the correct [80,5,5,5].

SHARED-ROUTE CONTROL
  The first Loewy layer is compared between an HNF lattice chain and a product
  of residue-field norms that does not construct rad(I).

UNITALITY
  Multiplicative R-linear maps are enumerated before the unital filter. A
  second route counts selectable CRT components from prime valuations and
  agrees on all 64 pairs. The maximum is four multiplicative maps and one
  unital map.

FINITE VERSUS UNIVERSAL
  N1-N4 say all five tested ideals and five distinct depths. The universal
  no-go is stated and proved only in PREREG.md.
~~~

## 5. Scope firewall

~~~text
MAY
  R1-R6 exactly: the canonical Boolean algebra, radical invariance, exact layer
  orders and length, thin unital reductions, no sections, and the fixed-support
  depth no-go.

MAY NOT
  selection of an ideal or atom; apparatus or event semantics; COMM-SAT or an
  event-completion law; orientation or a write/read/scale interpretation;
  decoder, measure or Born weight; neighbouring-ring census; cyclotomic
  unit-rank minimality; coarse-graining, RG or continuum language; any module
  decomposition inferred from layer orders; any L2-L6 lift.
~~~

SAMPLING NOT PROVIDED.

## 6. Disclosure

RESULT-EXPOSED, not blind. PR 521 contained the discovery derivation, a
defective rev1, a discarded successor draft and a passing rev2 finite
implementation. Its mutation harness helped find a shared-radical defect, but a
pre-pin static review found that timeout/exception, snippet and collateral
coverage handling did not establish the advertised guarantee. No theorem or
formal threshold relies on it.

The accepted verifier is byte-new but adapted from that exposed implementation;
the logic is not claimed independent. Its exact bytes were never imported or
executed before the public pin, were read back from a clean public clone, and
were then executed exactly once. The run confirmed the frozen decision with
31 of 31 gates passing, empty stderr and byte-stable expected output ready for
the required x86_64/aarch64 workflow gate.
