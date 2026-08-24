# PROMO-C-QDD-ERASURE-LATTICE-1

Promotion proposal from the incubation lane. NO AUTHORITY. A public fold may
consume this document alone. Basis: Public Canon v58 (canon-v58, content
05a0749e, CANON_SHA256 647822f5..., 304010 B).

## Candidate

```text
id:        C-QDD-ERASURE-LATTICE-1
decision:  ERASURE-LADDER (all five expected statements earned)
target:    public line, QDD-INSTRUMENT-APPARATUS [O], blocker O2, L4 only
```

## Exact statement (frozen class of the sealed record lane)

On `(Q^4, G)` with the public J simplex `u_x = D^x e_0`, motor
`D = M_J - I = rho((01234))`, record token `k`, admitted laws
`T P_k = P_k T = 0`, `T^sharp T = Q_k`, sign equality `T ~ -T`:

```text
1  The symmetry premises between the architecture residual
   H_k = AGL_1(F_5) cap S_k ~= C_4 and the record stabilizer S_k ~= S_4
   are exactly H_k < D_k < S_k, D_k the unique dihedral order-8 group.
2  Moving-space centralizer dimensions 3 / 2 / 1, bases {R,C,J}, {R,C},
   {Q}.
3  Admitted classes per rung: H_k a rational circle (injective family,
   nonselection); D_k exactly two physical classes [Q] and [R - C];
   S_k exactly one class [Q], idempotence selecting +Q.
4  R - C = rho(x -> 2k - x) Q: the second D_k class is Lueders composed
   with the central involution, multiplier a = -1; Z(S_k) trivial.
5  The motor commutant is Q[D] and contains no admitted law; the class is
   EMPTY for every subgroup of S_5 containing the motor cycle. The motor
   transports the ladder token to token; dims 3-2-1 at all five tokens.
```

Reading (D-grade, one sentence): in this class the unique minimal selecting
premise is full erasure S_k, the residual gap below it is exactly the one
orientation bit x - k versus k - x, and no selecting symmetry can come from
the flow.

## Falsifiers (as frozen)

An intermediate subgroup outside {H_k, D_k, S_k}; any centralizer dimension
or basis differing; any rung class count or member differing; a nonzero
motor-equivariant admitted law; transport failure at any token. Any one
fires the corresponding F branch of the preregistration.

## Pins

```text
PREREG    6ba0d1e947e310e1c8952e83bdb59bdac8642eff72b28a1d9504aa402adbb921
verify    e482ed41ffa7471a7307ee0cf02d1d2d7bd3f6cab2be39318b2c7978a471c9b8
  stdout  eaa53d32a8f2eace3d4d2e993993588fea9afd309d38d1def07a1ba4fd36a140
  45/45 PASS, exit 0, empty stderr, single formal run, 5 s
breaker   c1223b967bfdf864ef9f8a38bf11515bfbc2f5d28171a68234079cfb5eb6f89b
  stdout  9c3ef3ae4e0996bd1aa0ac2a9c4ec597ba9c19bfb9ba72e38e4998b9edec263a
  10 attacks, 9 HOLDS, 1 fired auxiliary expectation (B4b), archived
diag      3fa07d6eb1b9b279756bb4b6908c426407c050a962169057578fce0ecf81fb28
  stdout  e85f5203614797555743e4bba2f6a5718fd8de0fa1716ed74d9886787523517b
  B4b survivors = exactly the four members of statement 3; E3 confirmed
```

All programs Python standard library, integer and Fraction arithmetic only,
no float in any assertion, zero arguments, deterministic stdout, run with
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.

## Path to canon (what a fold would do)

1. Fresh public probe `P-QDD-ERASURE-LATTICE-1` under POLICY: claim lock
   issue, PREREG.md with the six fields above, verify.py rebuilt from this
   candidate (breaker checks folded in as gates), pin before execution,
   two-architecture byte-identical stdout.
2. On success, registry rows (restricted L4 statements, scope only the
   frozen class of the sealed record lane; conventions of the fold govern):

```text
QDD-RECORD-SYMMETRY-LATTICE   T   statements 1, 2, 5 transport
QDD-ERASURE-RUNG-CLASSES      T   statements 3, 4
QDD-MOTOR-EQUIVARIANCE-EMPTY  T   statement 5 emptiness
```

3. Optional conservative scope extension of QDD-INSTRUMENT-APPARATUS [O],
   appending one sentence to the O2 clause: "within the frozen simplex
   record class the admissible symmetry premises are exactly
   C_4 < D_4 < S_4, selection occurs only at S_4, and the residual gap is
   the erasure of the central involution x -> 2k - x". No status change.

## Dependency edges

Reads: the sealed probes P-QDD-J-CENTRALIZER-TERMINALITY-1,
P-QDD-RECORD-COMPLETE-STABILIZER-1, P-QDD-RECORD-NATURALITY-FORK-1,
P-QDD-FRESH-RECORD-NOFEEDBACK-2 (record-sufficiency equivalence),
P-QDD-J-AFFINE-APPARATUS-1. Creates no edge to QUADRATIC-DECODER-DATA,
no decoder-completion field, no L5/L6 object. O1 and O2 remain open;
SAMPLING NOT PROVIDED.

## Non-claims

No terminality derivation, no record-sufficiency derivation, no Born or
measure claim, no uniqueness of the frozen class itself, no statement about
premises not containing H_k (for example A_4), no naturality axis claim.
