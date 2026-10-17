# PREREG: P-KERNEL-MIRROR-TRIANGLE-CENSUS-1

PUBLIC-source; NON-CANONICAL; L1. Owner: A. M. Thorn, session 2026-10-05.
Public claim: [issue 1380](https://github.com/mathorn1973/twist-j/issues/1380).
Branch: `probe/P-KERNEL-MIRROR-TRIANGLE-CENSUS-1`.
Basis: main and `canon-v98` at
`b9f7af5f1b58c76956e280e33bd345c90bd88d1f`; content commit
`e62613db629de237fe15715ae2a9235f4e207b2c`.

This is a prospective public verification of already-known finite results,
not a blind discovery experiment. The attached incubation package, including
its claimed prior chronology, is described and corrected in SOURCE.md.
No original frozen file is rewritten. No Canon fold is authorized here.

## 0. Authority, collision scan and prior knowledge

On 2026-10-05 the five normative hashes matched; the declared content commit
is an ancestor of main, and the public tag dereferences to main. Required
architecture and publication checks are successful. Scans of all 205 remote
heads, open issues and pull requests, all-state exact-name issue/PR searches,
public probes and registry found no competing letter/triangle census lane.
The claim issue was created before the first public pin.

All entries in the table below, full translation rank six, group order
3125000, and all ten orientability flags were known from the supplied
incubation result before this freeze. Its original verifier reports 23/23
PASS and its independent crosscheck NO BREAK on one declared architecture.
The original status promise based on that agreement is not adopted.

Registered public inputs already establish affinity, linear image order
200, and the specified fired commutators. The public census replay already
checks `(bc)^5 = id`; the definitions show b and c distinct, hence exact
order five. Neither this pair nor absence of three is a new blind prediction.
The analytic translation and orientation arguments in PROOF.md and
SURFACES.md were also known before this public freeze.

## 1. Equation

Work over F5 on `X = F5^6`, in coordinate order
`(p1,p4,p1p,p4p,q,r)`; `r` is the source code's sixth coordinate `t`.
Use exactly the five affine involutions displayed in PROOF.md, composition
`gh = g o h`, and `[g,h] = ghg^-1h^-1`.

Let `G5 = <a,b,c,d,e>`, `L = lin(G5)`, and `T = ker(lin|G5)`.
The exact target is

```text
T = all translations F5^6
|L| = 200, dim(T) = 6, |G5| = 200 * 5^6 = 3125000
orbit of zero = 15625, point stabilizer order = 200
```

Consequently three divides neither |G5| nor the order of any subgroup,
quotient or section. Thus no element of order three, A5 section or binary
icosahedral section occurs in G5. This part applies to every word. It does
not classify arbitrary triples of involutory words.

For each literal pair, `m_gh = ord(g o h)`; the frozen expected orders are
2 for ab, 5 for bc and de, and 10 for the other seven pairs. For each
literal triple g,h,k, set `H = <g,h,k>` and
`e = 1/m_gh + 1/m_gk + 1/m_hk - 1`. The tuple order is always gh,gk,hk.

| Triple | Pair orders | Excess | Order of H | chi | Orientable genus |
|---|---|---|---:|---:|---:|
| abc | (2,10,5) | -1/5 | 100 | -10 | 6 |
| abd | (2,10,10) | -3/10 | 200 | -30 | 16 |
| abe | (2,10,10) | -3/10 | 200 | -30 | 16 |
| acd | (10,10,10) | -7/10 | 5000 | -1750 | 876 |
| ace | (10,10,10) | -7/10 | 5000 | -1750 | 876 |
| ade | (10,10,5) | -3/5 | 100 | -30 | 16 |
| bcd | (5,10,10) | -3/5 | 2500 | -750 | 376 |
| bce | (5,10,10) | -3/5 | 2500 | -750 | 376 |
| bde | (10,10,5) | -3/5 | 100 | -30 | 16 |
| cde | (10,10,5) | -3/5 | 100 | -30 | 16 |

The intermediate `(linear-image order, translation rank)` pairs, in the
same row order, are `(100,0), (8,2), (8,2), (40,3), (40,3), (4,2),
(20,3), (20,3), (4,2), (4,2)`. These already-disclosed decomposition
values are also checked, not treated as additional predictions.

The surface has one typed triangle per element h of H. Its side i is glued
to side i of h g_i, preserving endpoint types. SURFACES.md proves it is a
connected closed surface, with

```text
F = |H|, E = 3|H|/2, V = sum_(i<j) |H|/(2*m_ij)
chi = (|H|/2) * e
ell = (1,-1,1,-1,0,0), ell M_g = -ell for every letter
```

The common sign character proves all ten surfaces orientable. Numeric chi
and genus still depend on the pair and subgroup orders. The carrier is the
regular chamber set H, not the original action on X.

## 2. Code and pin

The accepted public implementation comprises `verify.py` and
`crosscheck.py`, both in this directory, using Python standard-library
integers and Fractions only. Their final SHA-256 values are recorded below
before committing this preregistration:

```text
verify.py     c93b6c6c2643af149d4464244cc639163cbada04da8904985d3b26d1c52d6c5f
crosscheck.py 880f670d8cd9eda087c8b145527c70743c376bfca9ccb3290822c948f088c9b9
```

`verify.py` adapts the supplied affine verifier. It enumerates the linear
quotient, takes the F5 rank of Schreier translation generators, computes
pair orders and triple records, checks the frozen targets, and audits the
explicit translation and covector identities from the proof. It invokes
`crosscheck.py`, which independently builds permutations from separate
coordinate formulas and calculates pair orders by cycle decomposition and
group orders by orbit/stabilizer. The two sets of structured records must
agree; the comparison is automatic. Before importing the companion, the
pinned verifier checks its exact SHA-256. The independent route uses affinity
to encode a zero stabilizer by images of six basis points. It independently
checks triple orders and surface fields, not their linear/translation
decomposition; that decomposition is checked by the affine route.

The public copy excludes the original bounded word search. The source
archive and its transcripts remain unchanged. No original transcript is
installed as this probe's EXPECTED.txt.

Commit and push this PREREG, both code files and the proof texts before the
first formal execution. Read back the exact remote commit and source bytes.
Record that immutable commit and every code hash in RUN.md. Do not amend
or force-push the pin. Compilation/static inspection before the pin is
allowed; no formal scientific computation was performed in this public
preparation lane before the pin.

Run from the repository root on Linux or a Linux-compatible environment:

```sh
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-KERNEL-MIRROR-TRIANGLE-CENSUS-1/verify.py
```

Save actual stdout byte for byte as EXPECTED.txt; require exit zero and
empty stderr. The existing PR workflow repeats the same entry point on
clean x86_64 and aarch64 runners and compares to that one transcript.

## 3. Carrier and inputs

There are no measured or fitted data. The entire source state set is X,
all 15625 points. All ten unordered pairs and all ten unordered literal
triples are included; no selected outcome is removed. Both implementations
carry explicit formulas for the same five public maps. The affine verifier
checks affinity and involutivity on every point. The independent permutation
route separately checks its affine reconstruction on all points.

The following registered results are public context and audit obligations:

- KERNEL-WEDGE-AFFINITY: public affine definitions and determinant checks.
- NATIVE-LINEAR-HODGE-ORDER5-OBSTRUCTION: linear image order 200 and the
  smaller fired linear subgroup. PROOF.md also gives a structural derivation
  of the order 200.
- FIRED-COMMUTATOR-NOGO: fired translations used as an independent check;
  the proof derives its needed translations directly from the definitions.
- KERNEL-WEDGE-COUPLING: comparison only. The CSUM example in PROOF.md is
  not an input to the single-cell census or a new coupling claim.

SOURCE.md identifies the public basis and original supplied hashes. The
general polyhedra note, Schlafli/golden-ratio scripts, P1--P5 observations,
exponent ten, arbitrary-word triangle classification and ion calibration
are not carriers or targets of this probe.

## 4. Systematics

1. Affine and permutation algorithms use independent coordinate formulas
   and distinct group-order routes. They share the declared F5 carrier and
   mathematical affinity, not implementation helpers or inferred results.
2. Product convention is explicit; both g h and h g pair orders are checked.
   The exact Schreier construction is justified by the linear quotient;
   point-stabilizer compression in the other route is justified only after
   exhaustive affine checks. Bounded enumeration caps fail closed.
3. Translation words and the common covector are checked directly, rather
   than inferred only from rank and boolean orientability output. The
   covector identity concerns linear parts, not full affine scalar values.
4. Vertex links are alternating cycles of length 2m. The regular chamber
   action removes original-state stabilizers from the surface count.
   Negative excess labels a hyperbolic reflection-triangle presentation;
   its finite image H is not the infinite triangle group.
5. All computation is exact. There is no statistical tolerance, fitting,
   randomized seed or physical error budget. Test duration and architecture
   metadata are not numerical evidence. A missing architecture is an
   incomplete gate, not a demonstrated disagreement.

## 5. Failure thresholds and decision

Zero tolerance, frozen before public execution.

- Any source mismatch, unexplained consistency/identity check failure, unresolved cap,
  malformed record, nonzero exit, nonempty stderr, disagreement between
  implementations or differing architecture transcript causes integrity
  STOP unless an independent exact check establishes a mathematical
  counterexample as below. A failed implementation assertion alone is not
  an algebraic disproof.
- An independently verified exact pair/subgroup order or surface count different from a
  frozen target, a failed translation identity, a nonorientable listed
  surface, or a genuine element of order three fires the relevant candidate
  claim. Record the counterexample with its scope. Do not change the target
  after seeing the result or suppress an adverse completed run.
- Complete matching output is verification PASS for this finite scope.
  One architecture leaves the tabular computation at candidate-C. Both
  required architecture jobs with byte-identical output satisfy the public
  computation gate. Independent analytic arguments remain candidate-T for
  public review. No result of this probe automatically changes any Canon
  registry status or closes a physical obligation.

If a pinned gate cannot complete, disposition follows POLICY.md's abandoned
pin rule; the identifier is not silently reused. If a result exists, it is
recorded as a completed result rather than relabelled abandonment.

## 6. Action layer and boundary

L1 finite state/group algebra only. The attached surface is an auxiliary
combinatorial object; there is no L2--L6 physical lift. The comparison with
independent labelled copies and with the registered CSUM operations merely
distinguishes copying the carrier from changing permitted operations.

No dynamics, instrument, calibration, event, causality, physical curvature,
space or time is inferred. No change to U/J, registry, EVIDENCE, DEPENDENCIES,
GATES, frontier, Canon, or physical HOLD is part of this public probe.
