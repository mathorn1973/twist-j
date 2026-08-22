# C-RECORD-CRT-IDEMPOTENT-1

**Title:** Record quotient calculus of `Z[zeta_5]`: support forces the Boolean
algebra, exponents carry the thickness, reductions are classified by ideal
inclusion

**Status:** NON-CANONICAL INCUBATION CANDIDATE, revision 2. No public
T/D/C/H/O/F status is created here. Proposed status on promotion: T, narrow
arithmetic scope.

**Date opened:** 2026-08-22. **Revision 2:** 2026-08-22, after the rev1 run
was archived as defective (section 6).

**Layer:** L1 arithmetic only. No decoder, measure, physical reading, event
semantics, or cross-layer lift is claimed.

This note changes no Canon, Registry, Frontier, dependency, gate, evidence,
verifier, status, release, decoder, or layer assignment, and touches no file
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

## 1. Scope

This candidate covers the record quotient calculus **R1-R6 only**. The
following material, present in earlier drafts of this note, is deliberately
**excluded** from the candidate and from its verifier, and remains in the
companion synthesis note as unverified non-probe material:

- the reading of the three arithmetic positions of `J` as write / read / scale,
- the neighbouring-ring census (`Z[i]`, `Z[zeta_7]`),
- cyclotomic unit-rank minimality,
- apparatus terminology and the `M = (I, tau, mu)` signature,
- all renormalization-group and continuum language.

## 2. Claim

Let `R = Z[zeta_5]`, a Dedekind domain, `lambda = 1 - zeta_5`, and let

```
I = prod_{P in Supp(I)} P^{e_P}
```

be a nonzero proper ideal, `r = |Supp(I)|`.

**(R1) Canonical Booleanization.** By the Chinese remainder theorem
`R/I = prod_P R/P^{e_P}` with every factor local, so an idempotent is a choice
of `0` or `1` in each factor:

```
Idem(R/I)  ~=  P(Supp I),
```

the **power set of the support**, as Boolean algebras. The atoms are labelled
by the primes themselves; no numbering or ordering of the primes is used.

**(R2) Radical invariance.** The reduction `R/I -> R/rad(I)` induces a
bijection `Idem(R/I) -> Idem(R/rad I)`. The exponent vector is therefore
invisible to the idempotent layer.

**(R3) Exact Loewy profile.** With `n_I = rad(I)/I` and the convention
`n^0 = R/I`, layer `k` is `n^k/n^(k+1)` for `k >= 0`, so the first layer is
`n^0/n^1 = R/rad(I)`. Then

```
|n^k / n^(k+1)|  =  prod { N(P) : e_P > k },
L(R/I)           =  min{ L : n^L = 0 }  =  max_P e_P.
```

Starting the layer list at `n^1` yields a different, wrong table; the
verifier exhibits that difference against a route that never forms the chain.

**(R4) Reductions are forced.** For nonzero proper ideals `I, J`,

```
Hom_{R-alg}(R/I, R/J) = { the canonical projection r + I -> r + J }   if I subset J,
                        empty                                        otherwise.
```

`R/I` is generated as an `R`-algebra by the image of `R`, so the map is
determined; well-definedness is exactly `I subset J`. The category of finite
record rings `R/I` with `R`-algebra maps is therefore **thin**. Unitality is
what makes it thin: dropping unitality, the multiplicative `R`-linear maps are
exactly the idempotents of `R/J` annihilated by `I`, and there are up to four
of them in the verified family.

**(R5) Irreversibility.** A strict quotient `R/I -> R/J`, `I` strictly inside
`J`, has no `R`-algebra section. Record coarse-graining is irreversible.

**(R6) Negative result: the Boolean layer does not fix the depth.** For
`I_L = lambda^L (2)`, every `L >= 1` gives the same support `{lambda, (2)}`,
the same radical, the same reduced record `R/rad = F_5 x F_16`, and the same
Boolean algebra of size 4, while `L(R/I_L) = L` is unbounded. Hence the
Boolean skeleton and the reduced record **cannot determine the filtration
length**.

## 3. Guards (what is NOT claimed)

**G1 (classification is not selection).** `Spec R` catalogues the possible
kernels and `R1-R5` classify the maps between the resulting records. Nothing
here selects which `I` a physical apparatus realizes, and `Spec` alone does
not even determine `I`, since the exponents are extra data.

**G2 (no event semantics).** Nothing here says that a physically completed
event must land in an idempotent class. The public theorem
`COMM-SAT(T) iff Xi_T = 0 iff T = +/-Q iff class(T)^2 = class(T)` is an exact
algebraic characterization *once COMM-SAT is posited*; whether physical event
completion implies it is exactly `QDD-TERMINAL-EVENT-SEMANTICS [O]`, whose
fence forbids COMM-SAT, idempotence, `+/-Q`, Lueders, or target effects as
construction inputs. This note adopts no such law and supplies no input to
one. R6 is a *negative* result and is stated so that it constrains any future
depth-based completion law without supplying one.

**G3 (a space of events, not an event).** `Idem(R/I)` determines the space of
possible Boolean events. It does not determine which atom occurs; atom
selection remains a dynamical question and is not addressed.

**G4 (orders, not modules).** R3 is verified as an identity between **orders**.
The finer statement that each layer decomposes as a direct sum of
one-dimensional `kappa(P)`-spaces is *not* verified here and is not claimed;
an earlier draft asserted it on the strength of a cardinality comparison, and
that is exactly the defect class recorded in section 6.

**G5 (no lifts).** No measure, no coarse-graining calculus, no RG flow, no
continuum limit, no physical naming of the positions. Any lift between layers
requires its own named public gate, and none is claimed.

## 4. Relation to public rows

Public predecessors, to be re-confirmed from the head at claim time:
`CARRY-PENTAD [T]` (`canon/REGISTRY.tsv` row 232), `J-BINARY-NORM-DESCENT [T]`
(row 16), `CARRY-QUADRATIC-SYMMETRY [T]` (row 15). Those rows already carry the
carry-geometry, pentad, `S_5`, and mod-2 material; this candidate does not
re-derive any of it and adds only the quotient calculus above. The standing
guard of `CARRY-PENTAD [T]` — that it selects neither the prime 5, nor the
cycle, nor the exponent, nor a physical reading — applies here unchanged and
is not routed around.

## 5. Preregistration (frozen fields)

```
Equation:    clauses (R1)-(R6) of section 2.
Code:        verify_record_quotient.py, Python standard library only, exact
             integer arithmetic, no floats anywhere, deterministic, single
             process, no file writes, no network. Ideals are Hermite normal
             forms of sublattices of Z^4, so ideals that are not rational
             conductors (lambda^L (2)) are handled directly.
             Run with LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
             PYTHONHASHSEED=0 TZ=UTC.
Carrier:     R = Z[X]/Phi_5 with basis (1, z, z^2, z^3); the eleven-ideal
             family of section "Part 2"; primes above 2, 3, 5, 11; the
             Hom family restricted to ideals of norm at most 2000; the R6
             family I_L = lambda^L (2) for L = 1..5, of norms 80 to 50000.
Systematics: none (exact integers; exhaustive enumeration over each quotient,
             not sampling).
             ONE platform this session (x86_64, Python 3). The POLICY
             section 4 two-architecture gate is NOT claimed.
Threshold:   any single gate FAIL fires the falsifier; no threshold moves
             after the result.
Layer:       L1 only.
Falsifier:   an ideal with |Idem(R/I)| different from 2^|Supp(I)|; an
             idempotent whose residue is neither 0 nor 1 at some prime of the
             support; a failure of the Boolean isomorphism on any pair; an
             ideal with Idem(R/I) not in bijection with Idem(R/rad I); a
             layer order differing from prod{N(P) : e_P > k}; a Loewy length
             differing from max_P e_P; an R-algebra map R/I -> R/J with I not
             inside J, or two distinct unital ones, or a unital section of a
             strict quotient; a member of the I_L family whose support,
             radical, or idempotent count differs from the others.
```

## 6. Dead-run record: rev1 is archived, not corrected

The rev1 verifier and its stdout are kept **unchanged** as

```
ARCHIVE_verify_record_crt_idempotent_rev1_DEFECTIVE.py
    sha256 f3e1b167f53503d8fd06f1ddc9f6b803d7ccaa832f3e92e469e89ed6828b1b48
    9288 bytes
ARCHIVE_verify_record_crt_idempotent_rev1_DEFECTIVE_stdout.txt
    sha256 6c1ce9c627d3d4e8c5c108701bb3119bcf5b374b747683f6ed36e1ec00b7f6df
    3045 bytes, 43 gate lines and 1 RESULT line
```

**What the dead run reported.** `RESULT: ALL GATES OK`, exit 0, empty stderr.

**Cause, stated mechanically per defect.** An owner review found seven, all
confirmed:

1. the note claimed 40 gates; the verifier had 43;
2. the note recorded the stdout as 3104 bytes; after LF normalization the
   file and the published blob are 3045 bytes, and the byte count was not
   regenerated with the hash;
3. gate `S3` had the literal `True` as its condition and therefore tested
   nothing;
4. gate `P4` claimed `(5) = lambda^4` but evaluated `625 == 625`; the ideal
   identity is true, the element identity is false, and the gate tested
   neither. Exactly, `(1 - z)^4 = 5 u` with `u = -z + z^2 - z^3`, `N(u) = 1`;
5. gate `M2` claimed `R/(6) = F_16 x F_81` but evaluated `6^4 == 16 * 81`;
6. the position table called the archimedean phase infinite, when `zeta_5` has
   order 5 in every embedding and it is the free unit direction that is
   infinite;
7. the phrase "neither minimal kernel is an apparatus" and its gate used
   apparatus language, which is not an L1 notion.

**Diagnosis.** The mathematics stood; the verification did not. Defects 3-5
are one class: a condition that cannot fail. A successor draft, written to fix
them, reproduced the same class in three further places and was discarded
without publication; only rev1 was ever published, so only rev1 is archived.

**Preservation.** Both rev1 artifacts are kept, not deleted, and archived
unchanged; their bytes equal the blobs published on the pull-request branch.
No threshold moved. The claims themselves are unchanged in substance and were
independently re-derived by routes that share no code with either verifier.
A corrected preregistration (section 5) was frozen before the rev2 execution.

## 7. Result

```
verifier:  verify_record_quotient.py
           sha256 9f36d76cf89c128db1c0388a623c87c634451718e839ef4822440fbc5226f824
           22191 bytes
stdout:    record_quotient.stdout.txt
           sha256 079e35b5c93c9509d98da52d4140cf1f4e8f1bbf34a45ae105ff18977bf14e6e
           4663 bytes, LF endings, 31 gate lines and 1 RESULT line
harness:   mutation_test.py
           sha256 228be8a98ff1cc258badd9323b315fc55e60a8137b1a605cddbec80ad6175fc9
           12595 bytes
platform:  x86_64, Python 3, neutral env; ONE platform only. A public probe
           must reproduce byte-identically on a second architecture before
           any T. Two runs of the verifier reproduce the pinned stdout
           exactly; pins are taken on LF content, per the repository's
           `text=auto eol=lf` normalization.
```

31 gates, all OK, exit 0, empty stderr, runtime about 1.1 s.

**The guarantee that the gates test something.** Not a source scan: a source
scan for literal constants is blind to construction-true conditions, which is
how three rounds of this file failed. Instead `mutation_test.py` breaks, one
at a time, the thing each gate claims to test, and requires the gate to
notice. It enforces four conditions and exits 0 only if all hold:

- every mutation kills at least one gate (a surviving mutation is a proven
  tautology);
- every mutation kills the gates it declares as targets;
- every gate is killed by at least one mutation with a clean attribution —
  **31 of 31 gates are covered**;
- a deliberately tautological gate injected into a scratch copy is reported
  as uncovered, which is the harness's own self-test, and it passes.

Result: 31 mutations, all killed their targets, 31 of 31 gates covered,
self-test passed, exit 0, runtime about 72 s.

The harness earned its place during the rev2 build: it showed that an earlier
form of gate `L5` compared two routes that both called `radical()`, so a
broken radical moved both sides together and the gate could not fail. `L5`
now takes its second route from the residue-field sizes over the support and
forms no radical ideal; mutation `M18` exists to keep it that way.

## 8. Settled formulation

> `J` determines reversible arithmetic motion; `I` determines the loss;
> `Supp(I)` forces the Boolean algebra of outcomes; `(e_P)` carry the
> thickness; the weight remains physics.

What is open, and is not addressed here: which `I` a physical apparatus
realizes, the law of event completion, and the measure. R6 says only that the
first of these cannot be read off the Boolean layer.
