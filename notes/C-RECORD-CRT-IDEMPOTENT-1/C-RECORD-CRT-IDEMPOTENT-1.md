# C-RECORD-CRT-IDEMPOTENT-1

**Title:** Record structure of finite quotients of `Z[zeta_5]`: support forces
the Boolean algebra, exponents carry the thickness

**Status:** NON-CANONICAL INCUBATION CANDIDATE. No public T/D/C/H/O/F status is
created here. Proposed status on promotion: T, narrow arithmetic scope.

**Date opened:** 2026-08-22

**Layer:** L1 arithmetic only. No decoder, measure, physical reading, or
cross-layer lift is claimed.

This note changes no Canon, Registry, Frontier, dependency, gate, evidence,
verifier, status, release, decoder, or layer assignment. It touches no file
under `canon/`.

---

## 0. Public authority and readback

Read from the public head on 2026-08-22: `STATUS.md` declares `STATE: ACTIVE`,
`CANON: Public Canon v60`, `TAG: canon-v60`, `CONTENT_COMMIT:
18b21bdaf2c2236c9444b120900277ccfb63e050`, `CANON_SHA256:
9387b75f2036ac6aff5737255956b93fb9b906511b8184ae4c1c999e8ed46db0`,
`CANON_BYTES: 329876`. The content commit is an ancestor of `main` and the
declared hash agrees with `canon/SHA256SUMS`. A fold session must re-confirm
the head before acting on this note.

## 1. Claim

Let `R = Z[zeta_5]`, a Dedekind domain, and let

```
I = prod_{i=1}^{r} p_i^{e_i},        r = |Supp(I)|,
```

be a nonzero ideal with distinct prime ideals `p_i`.

**(R1) CRT decomposition and Boolean skeleton.**

```
R/I  ~=  prod_{i=1}^{r} R/p_i^{e_i},
```

each factor local. Hence, as Boolean algebras,

```
Idem(R/I)  ~=  F_2^r  ~=  Idem(R/sqrt(I)).
```

**(R2) Support versus thickness.** `Supp(I)` alone determines the Boolean
algebra of outcomes; the exponent vector `(e_1, ..., e_r)` is invisible to the
idempotent layer and carries the local thickness (the nilpotent filtration
`sqrt(I)/I`).

**(R3) Local correction.** `|Supp(I)| = 1` implies `|Idem(R/I)| = 2` even when
`R/p^e` is not a field. The correct statement is about support cardinality, not
about being a field.

**(R4) Minima.** Smallest rational conductor with two channels is `m = 6`, with
`R/(6) ~= F_16 x F_81` and `|R/(6)| = 6^4 = 1296`. In the full ideal class the
smallest two-channel square-free ideal is `lambda p_11` of norm `55`, and the
smallest square-free ideal whose support contains both a prime over 5 and a
prime over 2 is

```
I = lambda (2),      N(I) = 5 * 16 = 80,      R/I ~= F_5 x F_16.
```

**(R5) Extreme points are not apparatuses.** Both minimal kernels give a single
channel and therefore zero Boolean resolution. Nontrivial Boolean distinction
requires at least two distinct prime-ideal components; a one-prime record
cannot be an apparatus.

**(P) Three arithmetic positions of `J = 1 + zeta_5^2`.** With
`lambda = 1 - zeta_5` and the reduction `zeta -> 1`:

| position | phase | scale | `J` |
|---|---|---|---|
| ramified residue `lambda` | order 1, dies | order 4 shadow | `J = 2` in `F_5^x`, order 4 |
| binary residue `(2)` | order 5, exact | order 3 shadow | order 15, primitive in `F_16^x` |
| archimedean | infinite | infinite | `sigma_1(J) sigma_4(J) = phi^-2` exactly |

Both finite positions are torsion: every finite quotient has a finite unit
group, so no finite position carries an infinite scale direction. The
archimedean position is the only one that does.

**(S) `J`-specificity of the binary position.** `Phi_5 mod 2` is irreducible,
so `R/(2) ~= F_16` is a field: one channel, no splitting, no thickness. This
fails in neighbouring rings — `Z[i]/(2)` has the nonzero nilpotent `1 + i`, and
`Z[zeta_7]/(2) ~= F_8 x F_8` splits.

**(U) Cyclotomic unit-rank minimality, modest form.** For prime `p` the unit
rank of `K_p` is `r = (p-3)/2`, so `p = 5` is the first prime with a nontrivial
finite phase and exactly one infinite unit direction. Dropping primality,
`r = 1` iff `phi(n) = 4` iff `n in {5, 8, 10, 12}`; in the full cyclotomic class
the rank-1 condition is therefore *equivalent to quarticity* and is not an
independent selector. In discriminant order the class runs
`K_5 (125) < K_12 (144) < K_8 (256)`.

## 2. Guards (what is NOT claimed)

**G1 (classification is not selection).** `Spec R` catalogues the possible
kernels; it does not select which `I` a physical apparatus realizes, and it does
not by itself determine `I` (the exponents are extra data). Which `I`
corresponds to which apparatus is not claimed here.

**G2 (no event semantics).** Nothing here says that a physically completed event
must land in the idempotent/saturation class. The public theorem
`COMM-SAT(T) iff Xi_T = 0 iff T = +/-Q iff class(T)^2 = class(T)` is an exact
algebraic characterization *once COMM-SAT is posited*; whether physical event
completion implies it is exactly `QDD-TERMINAL-EVENT-SEMANTICS [O]`, whose fence
forbids COMM-SAT, idempotence, `+/-Q`, Lueders, or target effects as
construction inputs. This note adopts no such law and supplies no input to it.

**G3 (Boolean algebra is a space, not an outcome).** `Idem(R/I)` determines the
space of possible Boolean events. It does not determine which atom occurs;
atom selection remains a dynamical problem and is not addressed.

**G4 (no physical names).** The three positions are named arithmetically
(ramified residue, binary residue, archimedean). Any reading of them as
write / read / scale is a dictionary act, out of scope here and separate from
`TWO-PLACE-PHYSICS [D]`. In particular `(2) subset Z[zeta_5]` is *not* asserted
to be the `K_8 = Q(zeta_8)` read place; those are two distinct binary objects
and a bridge between them is not claimed.

**G5 (no measure, no coarse-graining).** No `mu`, no L6 measure, no RG flow, no
continuum limit, and no scaling theorem is claimed. The spectral `2+2` splitting
of `M_J` is not asserted to be an RG relevant/irrelevant decomposition.

**G6 (no unconditional selection of 5).** Nothing here selects the prime 5, the
cycle, the exponent, or a physical reading unconditionally; the public
`CARRY-PENTAD [T]` guard applies unchanged and is not routed around.

## 3. Relation to public rows (predecessor authority)

The public predecessors, to be re-confirmed at claim time, are:

- `CARRY-PENTAD [T]` (`canon/REGISTRY.tsv` row 232) — pentad on `F_2^4`,
  `O(q) = O^-(4,2) ~= S_5`, `I + C^2` integrally conjugate to `M_J`, all
  `I + C^a` read as 2. The identity `J = 2` at the ramified position is the same
  carry token; this note does not re-derive it.
- `J-BINARY-NORM-DESCENT [T]` (row 16) — `O_5/(2) ~= F_16`,
  `q_2 = Tr_(F_4/F_2) o N_(F_16/F_4)`, singular locus exactly `mu_5`, the
  `A4/2A4 -> O_5/2O_5` isometry and transport to the pentad form. The binary
  position of the table above is this row's carrier.
- `CARRY-QUADRATIC-SYMMETRY [T]` (row 15).
- `QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]` and
  `ABELIAN-CM-UNIQUE-EVEN-BIT-DISCRIMINANT-MINIMUM [T]` for clause (U): those
  are separate frozen classes and this note adds a third reading, not a
  selection chain.

Origin of idea, not predecessor authority: an internal incubation freeze of
2026-07-19 (`C-CARRY-PENTAD-1`), superseded for public purposes by the rows
above.

## 4. Preregistration (frozen fields)

```
Equation:    clauses (R1)-(R5), (P), (S), (U) above.
Code:        verify_record_crt_idempotent.py, Python standard library only,
             exact integer arithmetic, no floats anywhere, deterministic,
             single process, no file writes, runtime well under 120 s.
             Run with LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
             PYTHONHASHSEED=0 TZ=UTC.
Carrier:     R = Z[X]/Phi_5 with basis (1, z, z^2, z^3); quotients R/(m)
             enumerated exhaustively for m in {2,3,4,5,6,10,11,20};
             prime-ideal data from the splitting law in Q(zeta_5);
             unit ranks from Dirichlet; conductors n < 200 for phi(n) = 4.
Systematics: none (exact integers, full enumeration, not sampling).
             ONE platform this session (x86_64, Python 3); the
             two-architecture byte gate belongs to a public probe at
             promotion, not to this incubation run.
Threshold:   any single gate FAIL fires the falsifier; no threshold moves
             after the result.
Layer:       L1 only. No lift to L2..L6 claimed.
Falsifier:   an ideal I with |Idem(R/I)| != 2^|Supp(I)|; an ideal with
             Idem(R/I) not isomorphic to Idem(R/sqrt I); a one-support ideal
             with more than two idempotents; a two-channel square-free ideal
             of norm below 55; a square-free ideal of norm below 80 whose
             support meets both 5 and 2; a nontorsion element in a finite
             quotient; Phi_5 mod 2 reducible; a cyclotomic field of unit
             rank 1 outside {K_5, K_8, K_12}.
```

## 5. Result

40 gates, all OK, exit 0, empty stderr, runtime 0.59 s on one platform.

```text
verifier:  verify_record_crt_idempotent.py
           sha256 f3e1b167f53503d8fd06f1ddc9f6b803d7ccaa832f3e92e469e89ed6828b1b48
stdout:    record_crt_idempotent.stdout.txt   (3104 bytes, LF line endings)
           sha256 6c1ce9c627d3d4e8c5c108701bb3119bcf5b374b747683f6ed36e1ec00b7f6df
platform:  x86_64, Python 3, neutral env; ONE platform only. A public probe
           must reproduce byte-identically on a second architecture before
           any T. Re-running the verifier reproduces the pinned stdout
           exactly; the pin is taken on LF endings, so compare after the
           repository's `text=auto eol=lf` normalization.
```

Two falsifier clauses are retired to proofs rather than tests: every finite
quotient has a finite unit group (so no finite position can carry a nontorsion
element), and `R/(2)` is a field iff `ord_5(2) = 4`.

## 6. Settled formulation

> `J` determines reversible arithmetic motion; `I` determines the loss;
> `Supp(I)` forces the Boolean algebra of outcomes; `(e_i)` carry the
> thickness; `mu_I` remains physics.

Signature of a measurement, at this level of description:

```
M = (I, tau, mu_I),        B_I = Idem(R/I) forced.
```

`tau` (the event-completion law) and `mu_I` (the weight) are open and are not
addressed here; `tau` in the nilpotent filtration `sqrt(I)/I` is recorded as an
`[H]` direction in the companion synthesis note, valuable precisely because it
uses neither COMM-SAT nor idempotence as an input, and still short of the
`QDD-TERMINAL-EVENT-SEMANTICS [O]` fence until it predicts something
independent and attaches to a physically chosen `I`.
