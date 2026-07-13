# P-SPIN-LIFT-FORCED-1 preregistration

Status: PRE-PIN DRAFT

This document defines the complete decision surface for the first public
attack on `SPIN-LIFT-FORCED`. It contains no gate output and earns no
scientific status. The formal gate must not run until this document and the
accepted verifier have passed reciprocal source review, been committed, and
been pushed as the immutable preregistration pin.

## Public identity

- Claim: `SPIN-LIFT-FORCED` [O]
- Public lock: issue 12
- Owner: master B session
- Branch: `probe/P-SPIN-LIFT-FORCED-1`
- Path: `probes/P-SPIN-LIFT-FORCED-1/`
- Initial base: `5d20a194201bec46b0a6d11c028a02f3fa5cf447`
- Action layer: L3, electron and ladder

Pinned owner ruling, the definitional source of every term below:

```text
ruling merge SHA:  5d20a194201bec46b0a6d11c028a02f3fa5cf447   (public main)
ruling file:       notes/canon/P-SPIN-LIFT-FORCED-RULING-1.md
ruling SHA-256:    0a0712dd8c2b87c31263269b0de04414489204a6b2b89a5fce04478daed62520
ruling size:       14579 bytes, 409 lines
```

## Equation

Work over the field with five elements. Matrices are row-major 4-tuples
`(a, b, c, d)` for `((a, b), (c, d))`, entries `0` to `4`. Define

```text
G    = SL_2(F_5), the 120 matrices of determinant 1,
z    = -I = (4, 0, 0, 4),
Z    = {I, z},
Gbar = G / Z,
pi(g) = gZ = {g, zg}.
```

The base group is the marked `D5` of the ruling D1: elements
`('rot', a)` and `('ref', a)` for `a` in `0..4`, multiplication

```text
rot(a) rot(b) = rot(a+b),   rot(a) ref(b) = ref(a+b),
ref(a) rot(b) = ref(a-b),   ref(a) ref(b) = rot(a-b),
```

indices mod 5, with the marked ordered pair `r = ('rot', 1)`,
`s = ('ref', 0)` and relations `r^5 = e`, `s^2 = e`, `s r s^-1 = r^-1`.

An admissible lift is a triple `(iota, R, S)` with
`iota : D5 -> Gbar` a monomorphism and `R, S` in `G`, satisfying exactly

```text
A1  pi(R) = iota(r)
A2  pi(S) = iota(s)
A3  R^5 = z
A4  S^2 = z
A5  S R S^-1 = R^-1
A6  <R, S> = pi^-1(iota(D5))
A7  |<R, S>| = 20
```

`iota` is derived from `(R, S)`: `iota(r^a) = pi(R)^a` and
`iota(r^a s) = pi(R)^a pi(S)`. The derived map must be a total
homomorphism and injective on all ten elements; a pair whose derived map
fails this typing is not a candidate. Per the pinned ruling, A3 is the
single imported membership choice (`ELECTRON-G-DOUBLE-COVER`); A4, A5, A6,
A7 are entailed integrity gates and are still checked exactly.

Two admissible triples are equivalent (ruling D4) if and only if one
`g` in `G` satisfies

```text
R' = g R g^-1,   S' = g S g^-1,   iota' = c_pi(g) o iota,
```

jointly. The observable is

```text
N = the number of D4 equivalence classes of admissible triples.
```

The preregistered hypothesis is `N = 1`: the dicyclic spin lift of the
marked axiom pair is forced, not chosen. No value of `N` is asserted before
the run.

## Witness (ruling section W, procedural)

```text
source commit:   f4fb064c2a08cd21b9a2bc2bcfd4daf46da47bcb
source file:     reproduce/color-ladder/verify.py
source SHA-256:  5cd3a40c66a6d2b6ca30ffc600d0ca13ebf1f2c7743a21e2bc56d6f572a1ebd8
```

Order `G` lexicographically by the 4-tuple. `R_w` is the first matrix of
exact multiplicative order 10; `S_w` is the first matrix, in the same
order, satisfying `S_w R_w S_w^-1 = R_w^-1`; `iota_w` is derived from
`(R_w, S_w)` as above. The verifier reconstructs `(iota_w, R_w, S_w)` by
this exact procedure and asserts its admissibility. A witness outside the
admissible set is `STOP`, an invalid execution, not a scientific result.

## Carrier and exact arithmetic

The carrier is finite and internal: `G` (120 elements), `Gbar` (60 cosets,
each represented by its lexicographically smaller member), the abstract
`D5` (10 labeled elements), and the full pair space `G x G` (14400 pairs).
All arithmetic is exact integer arithmetic modulo 5. Floating point,
sampling, tolerances, randomness, timestamps, external data, and external
packages are forbidden. No downstream reading (character value, Plancherel
mass, edge module, magnetic face measure) enters the predicate.

## Code and completeness certificates

The accepted code is `verify.py` in this probe directory. It must:

1. build `G` sorted lexicographically and verify `|G| = 120`, the unique
   involution `z`, and the kernel of `pi`;
2. verify the marked `D5` presentation (order 10, the three relations);
3. enumerate all monomorphisms `iota : D5 -> Gbar` directly in `Gbar` and
   print their count;
4. enumerate all pairs `(R, S)` in `G x G`, apply A3, A4, A5, derive
   `iota`, apply the typing check, then A6 and A7; print the count of
   raw admissible triples and the count of pairs excluded by typing;
5. verify that the derived `iota` of every admissible pair occurs in the
   monomorphism list;
6. partition the admissible set into D4 orbits by joint conjugation over
   all 120 elements of `G`; verify the set is closed under conjugation;
   print the sorted orbit size multiset and `N`;
7. for every class print the canonical representative (the
   lexicographically minimal pair), the orbit size, the stabilizer size,
   and the A5 confirmation; verify orbit size times stabilizer size
   equals 120 for every class;
8. print the central-retwist pairing table: the class of `(R, zS)` for
   every class representative; verify the pairing is an involution on
   classes and that every retwist is admissible;
9. reconstruct the witness, assert admissibility, and print its class;
10. print the decision and the audit tally.

The full pair enumeration is the exact finite proof at the declared scope.
The monomorphism count, conjugation closure, orbit-stabilizer products,
retwist involution, and witness location are internal completeness
certificates, not replacements for the enumeration.

## Scientific decision

- `POSITIVE` if `N = 1`: the obligation closes positively, the dicyclic
  lift is the unique lift of the marked axiom pair under the frozen
  constraints.
- `NEGATIVE` if `N >= 2`: a second inequivalent lift survives the same
  frozen constraints; the obligation closes negatively. This is a valid
  first-class outcome.
- `STOP` if the witness is not admissible or any audit gate fails: an
  invalid execution, no scientific outcome.

The verifier exits zero when all exact audit checks pass, whether the
printed decision is `POSITIVE` or `NEGATIVE`. It exits nonzero only when
the computation or an audit invariant fails. `RESULT.md` must preserve
that distinction.

## Systematics frozen at the pin

- The base pair is marked and ordered; no quotient by `Aut(D5)` or by any
  base relabeling (ruling D6).
- Equivalence is joint conjugation by the full `G = 2I`, nothing else
  (ruling D4).
- Independent central retwists are not identified by convention:
  `(iota, R, S)` and `(iota, R, zS)` are distinct unless D4-conjugate
  (ruling D5).
- The conjugation relation carries no sign choice: A5 is entailed by A1
  to A3 (ruling B2); the verifier still asserts it per class.
- `iota` is data of the candidate, derived from the pair; the typing
  check is part of membership.
- Matrices are compared and printed as row-major 4-tuples; every printed
  sequence is sorted; class representatives are lexicographic minima; no
  set or dict iteration order reaches any print path.
- No physical uniqueness, cross-place lift, or continuum statement is
  inferred from `N`.

## Failure thresholds and fired falsifiers

The probe run is invalid (`STOP`, nonzero exit) if any of the following
occurs:

1. `|G|` differs from 120, the involution census differs from exactly one,
   or the kernel of `pi` differs from `Z`;
2. the marked `D5` presentation fails any of its three relations or its
   order;
3. a derived `iota` of an admissible pair is missing from the independent
   monomorphism enumeration;
4. the admissible set is not closed under joint conjugation, an
   orbit-stabilizer product differs from 120, or the retwist pairing
   fails involution or membership;
5. the witness reconstruction fails or the witness is not admissible;
6. the verifier writes stderr, exits nonzero, or its formal output
   differs across the required architectures.

The scientific decision fires negatively, without invalidating the
enumeration, exactly when `N >= 2`. Thresholds and semantics never move
after the pin.

## Budget, run, and stop rule

- Python standard library only; single file; no imports beyond `sys`.
- Public CI budget: less than 15 minutes; intended verifier budget:
  less than 60 seconds on a current general-purpose core.
- Formal local evidence: Linux or Linux-compatible `aarch64`, neutral
  public environment fields, exit code 0, empty stderr.
- Independent public check: GitHub `x86_64`, byte-identical stdout.
- `EXPECTED.txt`, `RUN.md`, and `RESULT.md` are forbidden before the
  formal post-pin execution.
- Any change after the pin to the predicate, the equivalence, the witness
  procedure, a threshold, the action layer, or the verifier invalidates
  the run and requires a new probe name. The pinned branch must never be
  amended, rebased, squashed, or force-pushed.
