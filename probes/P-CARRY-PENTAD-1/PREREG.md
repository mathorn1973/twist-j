# PREREG. P-CARRY-PENTAD-1

Public lock: issue #77. Base: Public Canon v10, public `main` commit
`633b6f220fddd5882b73b156ca12161fc6d97938`; Canon content commit
`817275c4ef460d2d500a947db34c975baa651c40`.

```text
LAYER:  L1 arithmetic/state. A4 is an integral algebraic carrier here, not
        an L2 manifold. No lift to L2-L6 is claimed.
TARGET: new CARRY-PENTAD theorem candidate.
```

## Frozen definitions

Fix the coordinate and Hamming-weight frame on

```text
V = F_2^4,              w(x) = popcount(x),
t(x) = w(x) mod 2,      d(x,y) = popcount(x AND y) mod 2,
q(x) = binom(w(x),2) mod 2.
```

Addition in `V` is XOR. Define the polarization

```text
B(x,y) = q(x+y) + q(x) + q(y)
       = t(x)t(y) + d(x,y)                              (A)
```

in `F_2`. Let

```text
P = {1,2,4,8,15}.
```

The word "canonical" below means canonical relative to this frozen
coordinate/popcount frame. It does not mean canonical on an unframed
four-dimensional vector space.

Let

```text
A4 = {(z_0,...,z_4) in Z^5 : sum z_r = 0},
a_i = e_i - e_0,  1 <= i <= 4,
C(e_r) = e_(r+1 mod 5).
```

Write `R = Z[zeta_5]`, `lambda = zeta_5 - 1`, and
`J = 1 + zeta_5^2`. The map

```text
a_i |-> zeta_5^i - 1
```

identifies `A4` with the principal ideal `lambda R` and sends `C` to
multiplication by `zeta_5`.

## Frozen theorem candidate

### C1. Carry strata and the pentad

For every four-bit word, Lucas' theorem gives

```text
bit_0(w) = e_1(x) = t(x),
bit_1(w) = e_2(x) = q(x),
bit_2(w) = e_4(x).
```

Thus `q` is the second binary carry bit in the frozen frame. Its
polarization is (A), `B` is alternating and nondegenerate, and `q` has
exactly six zeros:

```text
q^(-1)(0) = {0,1,2,4,8,15}.
```

Hence `Arf(q)=1`. The five nonzero singular vectors form `P`; for distinct
`u,v in P`, `B(u,v)=1`, and the XOR of all five members of `P` is zero.

### C2. S5 inside S6

Every element of `O(q)` permutes `P`. This action is faithful, and every
permutation of `P` extends uniquely to an element of `O(q)`. Therefore

```text
O(q) = O^-(4,2) ~= S_5,       |O(q)| = 120.             (B)
```

Every quadratic refinement of `B` is uniquely

```text
q_v(x) = q(x) + B(v,x),       v in V.
```

Exactly the six `v` with `q(v)=0` give minus-type refinements. The natural
action of `Sp(4,2)` on these six refinements is faithful. Since

```text
|Sp(4,2)| = 15 * 8 * 3 * 2 = 720,
```

it gives `Sp(4,2) ~= S_6`; the stabilizer of the selected refinement `q`
is the group `O(q) ~= S_5` in (B).

### C3. The raw carry form has no five-fold symmetry

The stabilizer of `d` consists exactly of two families of orthonormal
bases: the 24 permutations of the four unit vectors and the 24 permutations
of their four complements. The complement map is central and has order two,
so

```text
Stab_GL(4,2)(d) ~= S_4 x C_2,       |Stab(d)| = 48.      (C)
```

In particular it contains no element of order five. The five-fold symmetry
belongs to the quadratic refinement `q`, not to the raw form `d`.

### C4. Fixed-five width gate

For positive `m`,

```text
5 divides 2^m - 1  iff  4 divides m,
```

because `ord_5(2)=4`. Since

```text
|GL(n,2)| = product_(i=0)^(n-1) (2^n - 2^i),
```

five first divides `|GL(n,2)|` at `n=4`. Equivalently, the irreducible
factors of `Phi_5` over `F_2` have degree four, and `C mod 2` supplies an
order-five element in dimension four. Thus four is the least binary linear
dimension admitting an element of order five.

This is a theorem with the order five fixed. It does not select `p=5` or
dimension four unconditionally.

### C5. Cyclotomic and J operators

On `A4`,

```text
C^5 = I,                  char(C) = Phi_5(X),
char(I+C^a) = Phi_5(X-1) = X^4 - 3X^3 + 4X^2 - 2X + 1   (D)
```

for every `a in {1,2,3,4}`. Under `A4 ~= lambda R`, `I+C^2` is
multiplication by `J`. Multiplication by `lambda` identifies the power-basis
copy of `R` with `lambda R`, so the matrix `I+C^2` is integrally conjugate
to the public power-basis matrix `M_J`.

For every `a in (Z/5Z)^x`, the coordinate permutation

```text
g_a(e_r) = e_(a r mod 5)
```

is an integral isometry of `A4` and

```text
g_a C g_a^(-1) = C^a,
g_a (I+C) g_a^(-1) = I+C^a.                             (E)
```

Therefore the exponent `a` is not selected by the unfixed integral-isometry
conjugacy class. This does not select a particular cycle, orientation, or
power.

### C6. The actual ramified quotient

The finite quotient

```text
A4/(C-I)A4
```

has order `det(I-C)=Phi_5(1)=5`, hence is `F_5` additively. On it `C=I`,
and for every `a in {1,2,3,4}`,

```text
I+C^a = 2I.                                               (F)
```

This is the precise power-blind ramified channel. Its characteristic shadow
is

```text
char(I+C^a) = (X-2)^4 mod 5.
```

The two determinant pins are

```text
Phi_5(1) = 5,
det(2I-(I+C^2)) = det(I-C^2) = N(2-J) = 5.               (G)
```

### C7. Correctly typed mod-two bridge

The root lattice is even, so

```text
q_A(v mod 2) = (v.v)/2 mod 2
```

is a quadratic form on `A4/2A4`. In the basis `a_1,...,a_4`, its Gram
matrix has diagonal two and off-diagonal one. Therefore

```text
q_A(x) = t(x) + q(x) = q(x) + B(15,x).                  (H)
```

The symplectic transvection

```text
tau_15(x) = x + B(x,15)15
```

is an involution and satisfies

```text
q(tau_15(x)) = q_A(x).                                   (I)
```

It is the declared explicit isometry `(A4/2A4,q_A) -> (V,q)` and maps the
five nonzero singular vectors of `q_A` onto `P`.

Reduction modulo two sends the coordinate Weyl group

```text
W(A4) ~= S_5
```

injectively and onto `O(q_A)`. Conjugation by `tau_15` identifies that image
with `O(q)`. The larger explicitly named subgroup `{+-I}W(A4)` has reduction
kernel exactly `{+-I}` and image `O(q_A)`.

This is a group statement about `O(q_A)` and `O(q)`. Separately,
`Iso(q_A,q)` has 120 elements and is a torsor; it is not itself the reduction
image of `W(A4)` until an isometry such as `tau_15` is declared.

Finally, under `a_i -> zeta_5^i-1`, the five nonzero `q_A`-singular classes
map modulo two to

```text
{1,zeta_5,zeta_5^2,zeta_5^3,zeta_5^4},
```

whose sum is zero. This is the exact mod-two five-term cyclotomic relation.

## Frozen proof

1. For an integer weight `w <= 4`, Lucas gives
   `bit_r(w)=binom(w,2^r) mod 2`. Expanding `e_2(x+y)` over `F_2` gives (A).
   In the standard basis the matrix of `B` has zero diagonal and one in
   every off-diagonal place; its square is the identity, so it is
   nondegenerate. Direct weight counting gives one zero of weight zero,
   four of weight one, and one of weight four. The standard zero-count
   formula in dimension four then gives `Arf(q)=1`. The pair and sum
   statements for `P` follow directly.
2. Any `q`-isometry permutes the five nonzero zeros and acts faithfully
   because the four unit vectors in `P` form a basis. Conversely, any
   permutation of the five vectors respects their sole linear relation,
   their zero `q`-values, and their pairwise `B`-values, so it extends to a
   unique `q`-isometry. This proves (B).
3. Nondegeneracy of `B` makes `v -> B(v,.)` an isomorphism from `V` to its
   dual, so the `q_v` are all refinements. Translation in the quadratic
   Gauss sum gives
   `sum_x (-1)^(q_v(x))=(-1)^q(v) sum_x (-1)^q(x)`, hence exactly the six
   singular `v` give minus type. Counting ordered symplectic bases gives
   `15*8*3*2=720`. An element fixing the six minus refinements fixes their
   linear differences, hence fixes `P` and is the identity. This proves the
   faithful `S_6` action and its `S_5` stabilizer.
4. A `d`-orthonormal basis consists of odd-weight columns. If it contains a
   unit column, orthogonality forces all columns to be the four units. If it
   contains a weight-three column, mixing it with its only orthogonal unit
   would leave only even-norm vectors for the remaining columns; therefore
   all columns are the four weight-three complements. This proves (C).
5. The order computation for `2 mod 5` and the product formula for
   `|GL(n,2)|` prove C4. The reduction of `C` supplies existence at four.
6. The rational augmentation representation has no fixed vector and `C^5=I`,
   so its characteristic and minimal polynomials are `Phi_5`. Replacing an
   eigenvalue by `1+zeta_5^(ar)` proves (D). The ideal identification proves
   the integral `M_J` statement. Coordinate multiplication by `a mod 5`
   proves (E) and preserves the `A4` norm.
7. The determinant of `I-C` is `Phi_5(1)=5`. The identity
   `C^a-I=(C-I)(I+C+...+C^(a-1))` proves (F); (D) reduced modulo five gives
   the characteristic shadow. The same integral multiplication matrix gives
   the norm equality in (G).
8. Expanding the `A4` norm in the declared basis proves (H). Since `q(15)=0`,
   the quadratic identity for a transvection proves (I). Coordinate
   permutations act faithfully on the natural five singular vectors of
   `q_A`, so the order-120 Weyl image is all of `O(q_A)`. The restriction of
   reduction to `W(A4)` is injective; adjoining scalar sign gives precisely
   the two-element kernel. The ideal-basis calculation sends the natural
   singular pentad to the five powers of `zeta_5` modulo two.

The proof, not the exhaustive program, is the proposed basis for theorem
status. The program audits every finite carrier and every displayed integral
matrix identity.

## Frozen fields

```text
EQUATION     C1-C7 and equations (A)-(I), exactly at the scopes stated.

CODE         probes/P-CARRY-PENTAD-1/verify.py
             sha256 55484d3063885966463e755fd92c3b5d735443f776824972f35371bdedcbed0f
             15684 bytes. Python standard library only; exact integers;
             deterministic; no float, file, network, subprocess, or random
             access. Run from repository root with LC_ALL=C LANG=C
             PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

CARRIER      theorem: the full V=F_2^4, its fixed coordinate/popcount frame,
             GL(4,2), Sp(4,2), O(q), the integral augmentation lattice A4,
             all a in (Z/5Z)^x, the exact quotients A4/(C-I)A4 and A4/2A4,
             and the public integral M_J. Audit: all 16 vectors, all 256
             pairs, all 20160 elements of GL(4,2), all 16 refinements, all
             120 Weyl permutations, and the exact 4x4 integer matrices.

SYSTEMATICS  no numerical approximation. The theorem proof is exact. The
             exhaustive audit can fail through an implementation defect;
             it does not enlarge the proof. The supplied incubation program,
             transcript, and dead revision are source material only and are
             not public evidence. The public verifier is newly authored; it
             exits nonzero on any failed gate and uses the typed tau_15
             bridge. A defect found after this public pin invalidates the
             probe and requires a new named issue/probe/pin.

THRESHOLD    KILL on any exact counterexample; any gap in proof steps 1-8;
             any mismatch with J-UNIT [T], J-STEP [T], or CODEC-TR4 [T] at
             their used scopes; any failed gate G01-G18; a nonzero stderr;
             or a byte mismatch between the pinned formal aarch64 run and
             the GitHub x86_64 run. PASS requires exit 0, empty stderr,
             exactly 18 PASS lines, and `RESULT 18/18 ALL PASS`.

LAYER        L1 arithmetic/state only. The lattice is not read as a manifold.
             No lift to L2-L6 is claimed.
```

## Dependencies and fences

Frozen public premises are only the definitions and exact integral step in
`J-UNIT [T]`, `J-STEP [T]`, and the compatible public matrix in
`CODEC-TR4 [T]`. The finite carry geometry, group identifications, width
statement, integral conjugators, ramified quotient, and mod-two bridge are
proved inside this preregistration. `P-RAMIFIED-TM-LIFT-1` is adjacent public
work but is not a premise and is not changed.

This probe does not derive the choice of width four or `p=5` without a frozen
order-five target. It does not select a five-cycle, its orientation, or an
exponent; derive the step form `I+C^a`; identify a conjugacy statement with a
physical gauge; or add a decoder, aperiodicity, entropy, measure, spacetime,
force, or phase reading. It changes no Canon, registry, frontier, dependency,
or status row. Any promotion and any new open obligation require a separate
sealed public fold.
