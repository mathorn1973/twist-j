# Selectors among native words: at least 25 alternatives for the registered contact architecture

**NON-CANONICAL / L1 / analytical note**

Public Canon v116, activation commit
[93c36089db57032a6cbca482ff62c95884567d0f](https://github.com/mathorn1973/twist-j/commit/93c36089db57032a6cbca482ff62c95884567d0f).
The source results are
[QUADRATIC-L5-NATIVE-OBSTRUCTIONS](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#quadratic-l5-native-obstructions-t),
[DEF-RESIDUAL-CONTACT-ARCHITECTURE](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#def-residual-contact-architecture),
and KERNEL-WEDGE-AFFINITY and KERNEL-WEDGE-COUPLING, both stated in
[section 3 of the Canon](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#3-the-kernel-and-the-census)
and registered in `canon/REGISTRY.tsv`. This note continues pull request
[#2068](https://github.com/mathorn1973/twist-j/pull/2068), which treats
selectors among arbitrary affine maps.

Companion files: [`verify.py`](verify.py), an exact audit that uses only
the Python standard library, and [`EXPECTED.txt`](EXPECTED.txt), its exact
output. Labels C01 to C27 below refer to the lines of that output.

## 1. Setting and results

All arithmetic is in F5. A cell is a vector x = (p1, p4, p1p, p4p, q, t) of
V = F5^6. W is the space of the four piston coordinates and R = (q, t). A
pair is z = (x, y) in V^2 = F5^12. Following
DEF-RESIDUAL-CONTACT-ARCHITECTURE, C = K + 0_2 with K = antidiag(3,2,2,3)
on W, so that R is the radical, and

```text
G(z) = (p_x^T K p_x,  p_x^T K p_y,  p_y^T K p_y) = (a, b, c),        M(a,b,c) = (3b, 4a+4b+4c, 3b+3c),
```

where p_x, p_y are the pistons of the two cells. The whole layer V^2 is
ready once, as in DEF-QUADRATIC-MEMORY-L5. The Canon writes a cell as
(p, q, r); its r is the coordinate t here, and its shear Q_cs is Q. The
ready set S0 of DEF-RESIDUAL-CONTACT-ARCHITECTURE has r = 0 in both cells
and arbitrary pistons and q, so it is a union of radical slices; the lower
bound below holds on every slice, and the cover of section 8 does not
depend on the radical, so both bounds hold there unchanged. Several
letters (c, t, P, u, e, h) are reused locally; each use is introduced where
it occurs.

**Native words.** KERNEL-WEDGE-AFFINITY supplies five affine bijections
a, b, c, d, e of one cell; KERNEL-WEDGE-COUPLING supplies the couplings
P(x,y) = (x, y+x) and Q(x,y) = (x+y, y). The convention of this note is:

- a generator g gives two maps of V^2, g_x(x,y) = (g(x), y) and
  g_y(x,y) = (x, g(y)); it is applied to one cell while the other cell is
  fixed ("slotwise"). P and Q act on the pair.
- A native word is a finite composition of these twelve maps. Words are
  written as products and applied right to left. N denotes the group they
  generate.
- Inverses add nothing: a, b, c, d, e are involutions and P, Q have order
  five (C01, C02).

This is the word class of QUADRATIC-L5-NATIVE-OBSTRUCTIONS ("every fixed
word in these maps, their inverses and their slotwise actions"). A reading
that allows only diagonal letters (the same generator on both cells at
once), or that drops P and Q, gives a different group and is not covered.

**Native selectors.** A native selector with m alternatives is a map of V^2
whose value at every z is one of omega_1(z), ..., omega_m(z), for fixed
native words omega_1, ..., omega_m. The same m words serve all inputs;
nothing is assumed
about the rule that selects among them. Its data output satisfies the
readout equation on every ready input, for one initialized step, exactly
when the agreement sets

```text
Z(omega_i) = { z in V^2 : G(omega_i(z)) = M G(z) }
```

cover V^2. Let m_nat be the least m for which such words exist. The Canon
excludes m = 1 and m = 2; pull request #2068 excludes m <= 5 for arbitrary
affine maps and shows that six linear maps of tangent type suffice for
C = K + 0_2. By Theorem L below those six cannot all be native.

| Statement | Status |
|---|---|
| Theorem S: N consists exactly of the affine maps of F5^12 described in section 2; its group of linear parts on W^2 has order 8 * 120^4 | proved here; the finite steps are verified (C01 to C09) |
| Corollaries 1 to 3: the affine maps of W^2 induced by native words; the reduction of #2068 keeps the native class; a native cover exists for every radical value | proved here |
| Propositions H, T, U, O: splitting over two halves; the 25 tangent words; the inputs they miss; the inputs missed by all native words of zero translation | proved here; verified on all 5^8 inputs (C10 to C14) |
| Theorem L: m_nat >= 25, already for a single radical value. In particular no native selector with six alternatives exists | proved here; the count 15680 and attainment of 640 verified (C13, C15) |
| Proposition W: a second test set of 12800 inputs on which no native word agrees more than 520 times | proved here, with three finite steps carried out by the verifier (C16 to C18); attained (C19) |
| Statements M1, M2: the largest agreement set of a native word not of tangent type has 40625 inputs; no native word agrees with more than 880 of the 20800 inputs missed by the tangent words | obtained by separate exhaustive exact computations (two independent implementations), not reproduced by the verifier; attainment verified (C20, C21) |
| Proposition C: m_nat <= 65 | verified by the exact verifier (C22) |
| Existence of native selectors whose data map has all fibres of size at most two: by native translations, and by the Canon's word T_alg | proved here from Corollary 1 and the cited Canon results; one count verified (C27) |
| Proposition F: 74 maps induced by native words and an explicit selection rule give a native selector whose data map has all fibres of size at most two; this data map admits the abstract continuation of #2068 | verified by the exact verifier (C23 to C25) |
| The exact value of m_nat; the least number of native alternatives for fibres of size at most two, between 25 and 74; register writes, reversibility and a continuation carried by native words | open |

## 2. The native group

**Generators.** Put alpha(p1,p4,p1p,p4p) = (p4,p1,p4p,p1p),
beta(p1,p4,p1p,p4p) = (-p1p,-p4p,-p1,-p4) and u = (0,1,0,-1). The verbatim
definitions give (C01)

```text
a: (p, q, t) -> ( alpha p,                    q,      t     )
b: (p, q, t) -> ( beta p,                    -q,     -t     )
c: (p, q, t) -> ( beta p + t u + (2,1,2,1),   1 - q,  -t     )
d: (p, q, t) -> ( -p + (2,1,3,4),             1 - q,  1 - t )
e: (p, q, t) -> ( -p + (2,1,3,4),             2 - q,  1 - t )
```

alpha and beta commute and square to 1. Their joint eigenvectors are

```text
e_++ = (1,1,4,4),   e_+- = (1,1,1,1),   e_-+ = (1,4,4,1),   e_-- = (1,4,1,4),
```

the signs being the eigenvalues of alpha and beta. In the coordinates
x = x_1 e_++ + x_2 e_+- + x_3 e_-+ + x_4 e_-- the form K is antidiag(3,2,2,3)
again, that is q_K(x) = x_1 x_4 - x_2 x_3, and u = 3 e_++ + 2 e_-+ (C03, C04).

**Six planes.** For j = 1..4 let Pi_j be the plane with coordinates
(x_j, y_j), the j-th eigen-coordinate of cell x and of cell y. Let Pi_q
have the coordinates (q_x, q_y) and Pi_t the coordinates (t_x, t_y). With
chi_a = (+,+,-,-) and chi_b = (+,-,+,-) the linear parts of the generators
are (C04)

```text
            on Pi_j, j = 1..4            on Pi_q and Pi_t        further part
a_x         diag(chi_a(j), 1)            diag(1, 1)              none
b_x         diag(chi_b(j), 1)            diag(-1, 1)             none
c_x         diag(chi_b(j), 1)            diag(-1, 1)             t_x -> t_x u in cell x
d_x, e_x    diag(-1, 1)                  diag(-1, 1)             none
g_y         as g_x with the two diagonal entries exchanged, and t_y u in cell y for c_y
P           [[1,0],[1,1]]                [[1,0],[1,1]]           none
Q           [[1,1],[0,1]]                [[1,1],[0,1]]           none
```

On Pi_q and on Pi_t every generator acts by the same matrix as on Pi_2, the
plane of e_+-: the sign of a is + and the signs of b, c, d, e are -, on R
and on e_+- alike.

**Theorem S (the native group).** *Status: proved here; the finite steps
are verified (C01 to C09).* N consists exactly of the maps z -> Lin z + v
of F5^12 with v arbitrary and Lin of the following form.

1. Lin maps every plane Pi_j to itself and acts on it by a matrix g_j of
   GL2(F5) with det g_j = +-1 and det g_1 det g_2 det g_3 det g_4 = 1.
   Every such 4-tuple occurs. These 4-tuples form a group Lambda of order
   8 * 120^4 = 1658880000.
2. Lin maps Pi_q to itself and acts on it by g_2; the Pi_t-component of
   Lin restricted to Pi_t is g_2 as well.
3. The only further part of Lin is a linear map Nu from Pi_t to
   Pi_1 + Pi_3.
   Every Nu occurs, independently of (g_1, ..., g_4).

Consequently the group of linear parts has order 5^8 * 8 * 120^4, and N
has 5^20 * 8 * 120^4 elements.

*Proof.* Step 1. The affine maps described in the theorem form a group,
and by the table the twelve generators belong to it: the determinants of
the generators on (Pi_1, ..., Pi_4) are

```text
a_x, a_y: (1,1,-1,-1),    b_x, b_y, c_x, c_y: (1,-1,1,-1),    d_x, d_y, e_x, e_y: (-1,-1,-1,-1),    P, Q: (1,1,1,1),
```

each of product 1. So N is contained in that group, and the determinant
patterns that occur are exactly the eight patterns of product 1 (C05). The
pattern (-1,-1,-1,-1) comes from d or e applied to one cell.

Step 2: the group Lambda_N of the 4-tuples (g_1, ..., g_4) that occur as
linear parts of elements of N contains SL2(F5)^4. By step 1, Lambda_N lies
in Lambda. Write its elements as 4-tuples.
Let t = [[1,0],[1,1]] and t' = [[1,1],[0,1]]; they generate SL2(F5), of
order 120 (C06). Since P and Q act by t and t' on every plane, Lambda_N
contains Delta(s) = (s,s,s,s) for all s in SL2(F5). Let h = diag(-1,1). The
components of a_x, b_x and a_x b_x are (1,1,h,h), (1,h,1,h) and (1,h,h,1).
With [g,s] = g s g^(-1) s^(-1), c = [h,t] = [[1,0],[3,1]] and
c' = [h,t'] = [[1,3],[0,1]], Lambda_N therefore contains

```text
a_x Delta(t) a_x^(-1) Delta(t)^(-1) = (1,1,c,c),     b_x Delta(t) b_x^(-1) Delta(t)^(-1) = (1,c,1,c),
b_x Delta(t') b_x^(-1) Delta(t')^(-1) = (1,c',1,c'),  (a_x b_x) Delta(t') (a_x b_x)^(-1) Delta(t')^(-1) = (1,c',c',1),
```

and hence the commutators

```text
[(1,1,c,c), (1,c',1,c')] = (1,1,1,y),   [(1,1,c,c), (1,c',c',1)] = (1,1,y,1),   [(1,c,1,c), (1,c',c',1)] = (1,y,1,1),
```

with y = [c,c'] = [[2,2],[3,1]], which is not 1 or -1. Conjugation by
Delta(r) replaces y by r y r^(-1). The conjugates of y generate SL2(F5):
they generate a normal subgroup that is not contained in the centre
{1,-1}, the only normal subgroups of SL2(F5) are 1, {1,-1} and the whole
group, and the verifier confirms by enumeration that it has 120 elements
(C06). So Lambda_N contains (1,1,1,s), (1,1,s,1) and (1,s,1,1) for all s, and
then also (s,1,1,1) = Delta(s) (1,s^(-1),1,1) (1,1,s^(-1),1) (1,1,1,s^(-1)).
Together with the eight determinant patterns of step 1, Lambda_N is all of
Lambda, the set of the 4-tuples with determinants +-1 of product 1, of
order 8 * 120^4.

Step 3: the part Nu. The word c_x b_x has the linear part 1 + n_0, where
n_0 sends t_x to a nonzero multiple of u in cell x and vanishes on all
other coordinates; it has nonzero components n_1 into Pi_1 and n_3 into
Pi_3 (C07). Conjugation by an element of N with linear part Lin replaces n_0
by Lin n_0 Lin^(-1), that is n_j by g_j n_j g_2^(-1) for j = 1, 3. The matrices
g - 1, g in SL2(F5), span all 2 by 2 matrices. The elements 1 + n with n
a linear map from Pi_t to Pi_1 + Pi_3 commute and multiply by adding the
n, so the n that occur form a subspace. Varying g_1 alone and subtracting
n_0 gives all (A n_1, 0); varying g_2 afterwards gives all (A n_1 B, 0),
which is every linear map from Pi_t to Pi_1 because n_1 has rank one. The
same holds for Pi_3. So every Nu occurs with g_j = 1, and then with every
element of Lambda (C07: the conjugates span a space of dimension 8).

Step 4: translations. The translations in N form a subspace T of F5^12
that is stable under the linear parts. Three words are translations (C08,
by direct evaluation of the generator functions):

```text
e_x d_x         translation by the unit vector of q_x,
d_x P d_x P     translation by (2,1,3,4,1,1) in cell y,
(c_x d_x)^2     translation by (4,3,4,1,0,3) in cell x.
```

In the six planes their components are

```text
e_x d_x:       Pi_q: (1,0)
d_x P d_x P:   Pi_1: (0,4),  Pi_3: (0,3),  Pi_q: (0,1),  Pi_t: (0,1)
(c_x d_x)^2:   Pi_1: (3,0),  Pi_2: (3,0),  Pi_3: (2,0),  Pi_4: (1,0),  Pi_t: (3,0)
```

For a nonzero vector a of a plane, the vectors (g - 1) a, g in SL2(F5),
span the plane. The first word therefore gives Pi_q inside T (use
elements with g_2 arbitrary). Subtracting the Pi_q part of the second
word leaves a vector with a nonzero Pi_t component; applying 1 + Nu and
subtracting gives all of Pi_1 + Pi_3 inside T, then the Pi_t component
itself and hence Pi_t. The third word then leaves (3,0) in Pi_2 plus (1,0)
in Pi_4; elements with only g_4 different from 1 give Pi_4, and then Pi_2
follows. So T = F5^12; the dimensions after the three words are 2, 8, 12
(C08).

Step 5. By steps 2 to 4 every map described in the theorem is a product
of elements of N. QED

KERNEL-CONNECT-ALL-K is registered with status T in Canon v116. It
concerns diagonal letters and is not used here; the three words above use
slotwise letters.

## 3. Induced maps, the reduction, existence

G depends only on the pistons, and by Theorem S the piston output of a
native word depends on the pistons and on (t_x, t_y) only.

**Corollary 1 (induced maps of W^2).** *Status: proved here.* For a radical
input (q_x, t_x, q_y, t_y) a native word induces on W^2 the affine map

```text
p -> L p + Nu(t_x, t_y) + tau,
```

and every triple (L, Nu, tau) with L in Lambda, Nu a linear map from F5^2
to Pi_1 + Pi_3 and tau in W^2 occurs. For a fixed radical value the
induced maps are therefore exactly the affine maps of W^2 with linear part
in Lambda and arbitrary translation. The linear part does not depend on
the radical, q does not enter, and t enters only through a translation
inside Pi_1 + Pi_3, the pistons fixed by beta.

In the original coordinates Lambda consists of the invertible maps of
W^2 whose four 4 by 4 blocks lie in A = span{1, alpha, beta, alpha beta},
the algebra of the maps that are diagonal in the eigenbasis, subject to
the determinant conditions of Theorem S.

**Corollary 2 (the reduction keeps the native class).** *Status: proved
here.* Lemma 1(b) of the note in #2068 uses g_out = [[0,1],[2,1]] and
g_in = [[1,1],[3,1]] and replaces a branch f for the target M by
(g_out x 1) f (g_in x 1) for the target M0(a,b,c) = (a+c, b, c). On every
plane Pi_j this multiplies the determinant by det g_out det g_in = 4, and
the pattern (4,4,4,4) has product 1 (C09). So the reduction maps the set
of affine maps with linear part in Lambda onto itself. From here on
"reduced coordinates" means the data (2x + 3y, 4x + 2y) of a Canon input
(x, y), the target M0, and outputs (X, Y) standing for the Canon output
(2X + 3Y, X).

**Corollary 3 (one radical value suffices; existence).** *Status: proved
here.* m_nat equals the least number of affine maps of W^2 with linear
part in Lambda whose agreement sets cover W^2. If m native words cover
V^2, their induced maps at one radical value cover W^2; conversely maps
of W^2 with linear part in Lambda lift to native words with Nu = 0, whose
agreement sets do not depend on the radical. In particular a lower bound
needs only one radical value. A native cover exists: all 125 Gram values
are attained on W^2, so for every input z of W^2, every L in Lambda and
every z' with G(z') = M G(z) there is exactly one translation tau with
L z + tau = z', and that map agrees at z.

## 4. Halves, tangent words, and two sets of hard inputs

Work in reduced eigen-coordinates and write v_j = (x_j, y_j). For two
vectors v = (x, y) and v' = (x', y') of F5^2 put

```text
S(v, v') = (x x', (x y' + y x')/2, y y'),        c = y y',        w = y x' - x y'.
```

A triple (a,b,c) is read as the binary form a X^2 + 2b XY + c Y^2; then
S(v, v') is the product of the linear forms x X + y Y and x' X + y' Y, and
M0 adds c X^2. The diagonal half of an input is u = (v_1, v_4), the
antidiagonal half is w = (v_2, v_3). (The letter w is used for the wedge
of a half, for the antidiagonal half and for a point of a half, as in
"w in B'"; native words are written omega.)

**Proposition H (halves).** *Status: proved here; it underlies the counts
of C11 to C22, which are obtained by direct evaluation.* G = S(v_1, v_4) -
S(v_2, v_3). A map with linear part in Lambda acts on the two halves
separately, v_j -> g_j v_j + tau_j. A half-map is h(v, v') =
(g v + tau, g' v' + tau') with det g and det g' in {1, -1}; put
F_h(u) = S(h(u)) - M0 S(u). Then
f = (h_d, h_a) agrees at (u, w) if and only if F_{h_d}(u) = F_{h_a}(w).
The two halves are coupled only by det g_1 det g_4 = det g_2 det g_3.

*Proof.* q_K(x) = x_1 x_4 - x_2 x_3 and its polarization give the first
statement. G(f(z)) = M0 G(z) reads
S(h_d(u)) - S(h_a(w)) = M0 S(u) - M0 S(w), because M0 is linear. QED

**Proposition T (tangent words).** *Status: proved here; verified (C10,
C11).* A map f = (h_d, h_a) is of tangent type when its second and third
residuals vanish identically, that is F^b and F^c of the two halves agree
identically; the halves use disjoint variables, so each of these
components is then constant. For a half-map h the components F_h^b and
F_h^c are constant if
and only if tau = tau' = 0, g = m [[1,psi],[0,1]] and
g' = m^(-1) [[1,-psi],[0,1]]; then F_h = (psi w - (1 + psi^2) c, 0, 0).
Hence the maps of tangent type (in the sense of #2068) with linear part in
Lambda are the (k(x + psi y), k y) with psi = diag(s, r, -r, -s) and k a
diagonal isometry: 25 maps psi, none nilpotent except 0, and 16 isometries.
The agreement set is

```text
{ s w_d - (1 + s^2) c_d = r w_a - (1 + r^2) c_a },
```

with (w_d, c_d) and (w_a, c_a) the invariants of the two halves. Its size
is 90625 for psi = 0, 80625 for the 8 maps with exactly one of s, r equal
to 0, and 78625 for the other 16.

*Proof.* F_h^c = Y Y' - y y' with Y, Y' the second output coordinates.
Constancy forces g and g' upper triangular with g_22 g'_22 = 1 and
vanishing second translation coordinates. Then constancy of F_h^b forces
g_11 g'_22 = 1 = g_22 g'_11, g_12 g'_22 + g_22 g'_12 = 0 and vanishing
first translation coordinates. The value of F_h^a is then
psi (y x' - x y') - (1 + psi^2) y y'. The sizes follow from the numbers of
points of a half with given (w, c): 65 for (0,0), 40 for (w,0) with w
nonzero, 20 for every (w,c) with c nonzero. QED

Subsets of a half (C12, C13):

```text
E   = { c = 0, w = 0 }                              65 points
E0  = { y = y' = 0 }                                25 points
E12 = E without E0                                  40 points    (v = 0, y' nonzero, or v' = 0, y nonzero)
Ez  = { v = 0 or v' = 0 }                           49 points    (E12 and 9 points of E0)
B'  = { c nonzero, w = c or w = -c }               160 points
```

and the sets of inputs, each consisting of the pairs with one half in the
first set and the other half in B':

```text
U  = E x B'  u  B' x E         20800 inputs,
O  = Ez x B' u  B' x Ez        15680 inputs,
U1 = E12 x B' u B' x E12       12800 inputs,          U1 inside O inside U.
```

For u in B' the form M0 S(u) has discriminant (w^2 - 4 c^2)/4, a
non-square, so it is not a product of two linear forms:

```text
(F)    F_h(u) is nonzero for every u in B' and every half-map h.
```

**Proposition U (inputs missed by the tangent words).** *Status: proved
here; verified pointwise on all 5^8 inputs for C = K and the Canon target
(C11, C12).* The inputs that agree with none of the 25 tangent words are
exactly those of U.

*Proof.* An input is missed if and only if the value sets
{psi w - (1 + psi^2) c : psi in F5} of its two halves are disjoint. The
value set is F5 if c = 0 and w is nonzero, {0} if c = w = 0, and has three
elements if c is nonzero. Two sets of three elements meet. So one half has
c = w = 0 and the other has c nonzero and no root of
c psi^2 - w psi + c, that is (w/c)^2 - 4 a non-square, that is w = +-c.
QED

**Proposition O (inputs missed by all linear maps with linear part in Lambda).**
*Status: proved here; verified (C13, C14).* An input of W^2 agrees with no
map p -> L p, L in Lambda, if and only if it lies in O.

*Proof.* Let (u, w) be in O with, say, a zero vector in u and w in B'. A
linear map sends the zero vector to zero, so F_d(u) = 0, while F_a(w) is
nonzero by (F). Conversely, inputs outside U agree with a tangent word.
Let (u, w) be in U but not in O, say u = ((x_1,0),(x_4,0)) with
e = x_1 x_4 nonzero and w in B' with invariants (w_a, c), w_a = +-c. The
reduced map with g_1 = diag(k, 1/k), g_4 = 1 and the tangent half-map psi
on (v_2, v_3) has F_d(u) = ((k-1) e, 0, 0) and
F_a(w) = (c (+-psi - 1 - psi^2), 0, 0). As psi runs through F5 the factor
+-psi - 1 - psi^2 takes the values 2, 3, 4, and for every ratio c/e one of
c/e times these lies in {1, 2, 3} = {k - 1 : k = 2, 3, 4}. The mirror case
is the same. The verifier evaluates these 30 maps and the 25 tangent words
and finds that together they agree with every input outside O and with no
input of O (C14). QED

## 5. At least 25 native alternatives

**Theorem L.** *Status: proved here; |O| = 15680 and the attainment of
640 are verified (C13, C15).* Every map of W^2 with linear part in Lambda
agrees with at most 640 of the 15680 inputs of O. Consequently every
native selector has at least 25 alternatives, m_nat >= 25, and this holds
already for the ready inputs of a single radical value. In particular no
native selector with six alternatives exists.

*Proof.* Let f = (h_d, h_a) and fix w in B'. Consider the inputs (u, w)
with v_1 = 0. Then M0 S(u) = 0, the first output vector of the diagonal
half is the constant tau_1, and the second, V_4 = g_4 v_4 + tau_4, runs
bijectively through F5^2 with v_4. By Proposition H the input agrees if
and only if S(tau_1, V_4) = F_a(w). If tau_1 = 0 this never holds, by (F).
If tau_1 is nonzero, V -> S(tau_1, V) is injective, because a product of
linear forms with one factor fixed determines the other factor. So at
most one input (u, w) with v_1 = 0 agrees. The same holds for v_4 = 0, and
with the halves exchanged for v_2 = 0 and for v_3 = 0. Every input of O
is of one of these four kinds with the other half in B', and B' has 160
points; hence |Z(f) n O| <= 4 * 160 = 640. A cover needs at least
15680/640 = 24.5 maps. The passage to native selectors and to one radical
value is Corollary 3. QED

Remarks.

- The bound is attained: the translation word that is x -> x + t in
  reduced coordinates, t = e_++ + e_+- + 4 e_-+ + e_--, agrees on 640
  inputs of O (C15).
- The proof uses only that f acts on the four planes Pi_j separately and
  bijectively. It therefore applies to selectors among arbitrary maps of
  that kind, affine or not.
- Counting the inputs of O with u = 0 or w = 0 twice (320 inputs) gives
  the total weight 16000 = 25 * 640, while the argument still bounds the
  weight collected by one map by 640. So a native selector with exactly 25
  alternatives would have to cover every input of O exactly once, with
  every word reaching the weight 640 (inputs with u = 0 or w = 0 counted
  twice).

## 6. A second test set

U1 is a subset of O, and a finer count on it gives the same bound by a
different route.

**Proposition W.** *Status: proved here, with three finite steps carried
out by the verifier (C16 to C18); attainment verified (C19).* Every map of
W^2 with linear part in Lambda agrees with at most 520 of the 12800 inputs
of U1, and 520 is attained. Since 12800 > 24 * 520, this again gives
m_nat >= 25.

*Proof.* U1 is the disjoint union of four blocks. For u = (0, v_4) with
y_4 nonzero, F_d(u) = S(tau_1, g_4 v_4 + tau_4), and g_4 v_4 + tau_4 runs
through tau_4 + (F5^2 without the line of g_4 e_1), e_1 = (1,0). So the
number of agreeing inputs in the block {v_1 = 0, y_4 nonzero} x B' is

```text
C1 = #{ w in B' : F_a(w) = S(tau_1, V) for some V with V - tau_4 not on the line of g_4 e_1 },
```

and similarly C2 (v_4 = 0), C3 and C4 (halves exchanged). Each of them is
at most the number of w in B' for which F_a(w), respectively F_d(u), is
divisible by the linear form of the translation involved, and is 0 if
that translation vanishes.

Lemma 1 (evaluation at the root). Let tau be nonzero and P a root of its
linear form, P = (tau_y, -tau_x). For a half-map h = (g, tau_h, g', tau'_h)
the form F_h(u) is divisible by the linear form of tau if and only if

```text
(<v, A> + alpha)(<v', A'> + alpha') = <v, P><v', P> + y y' P_x^2,
A = g^T P,  alpha = <tau_h, P>,  A' = g'^T P,  alpha' = <tau'_h, P>,
```

because a binary quadratic form is divisible by a linear form exactly
when it vanishes at its root, and F_h(u) is the form of
(g v + tau_h, g' v' + tau'_h) minus the form of (v, v') minus y y' X^2.

Lemma 2 (finite, C16). The equation of Lemma 1 is homogeneous of degree
two in P, so P matters only up to scalars. For each of the six root
points P and all 24 * 5 * 24 * 5 values of (A, alpha, A', alpha'), the
number of
points of B' satisfying the equation of Lemma 1 is at most 64, with one
exception: for P = (0,1), that is tau on the x-axis, and
(A, alpha, A', alpha') = ((0,m), 0, (0,1/m), 0) it is 160. The exception
means that g and g' are upper triangular with g_22 g'_22 = 1 and that
both translations of h lie on the x-axis. Call this family of half-maps
H0. For h in H0 the component F_h^c vanishes identically.

Lemma 3 (finite, C17). H0 has 10000 half-maps. For those with both
translations nonzero, F_h^b vanishes at 30 points of B' or more.

Now let f = (h_d, h_a). If h_a is not in H0, then C1 + C2 <= 128 by
Lemma 2; in any case C1 + C2 <= 320. The same holds for C3 + C4 and h_d.
So if one of the halves is not in H0, f agrees on at most 448 inputs of
U1. Let both be in H0. Then all g_j are upper triangular and all
translations are tau_j = (t_j, 0). For t_1 nonzero the forms S(tau_1, V)
with V - tau_4 off the x-axis are exactly the (a, b, 0) with b nonzero, so
C1 = 160 - z(h_a), where z(h) is the number of points of B' at which F_h^b
vanishes; C1 = 0 if t_1 = 0. Likewise for C2, C3, C4. Hence

```text
|Z(f) n U1| = k_d (160 - z(h_a)) + k_a (160 - z(h_d)),
```

with k_d the number of nonzero t_1, t_4 and k_a the number of nonzero
t_2, t_3. By Lemma 3, z >= 30 for a half with two nonzero translations.
Up to exchanging the halves, the cases (k_d, k_a) = (2,2), (2,1), (2,0),
(1,1), (1,0), (0,0) give at most 520, 450, 320, 320, 160, 0 (C18). The value 520 is reached by the map that is
(x + nu y + t, y) in reduced coordinates with nu = diag(0,0,1,1) and
t = e_++ + e_+- + e_-+ + e_--; its agreement set has 18125 inputs (C19).
QED

## 7. Two further maxima

The following two statements are not needed for Theorem L. They were
obtained by separate exhaustive exact computations, in two independent
implementations, and are not reproduced by `verify.py`, which only checks
that the stated values are attained.

**Statement M1.** *Status: separate exhaustive exact computation;
attainment verified (C21).* The largest agreement set of a map with linear
part in Lambda that is not of tangent type has 40625 = 13 * 5^5 inputs.
It is reached by (x + nu y, y) in reduced coordinates with nu the
projector onto one eigenline, which lies in A but is not K-skew. Together
with Proposition T, no map of W^2 with linear part in Lambda, that is no
native word at a fixed radical value, has an agreement set of a size
strictly between 40625 and 78625. The general bound of #2068 for affine
maps not of tangent type is 62500.

**Statement M2.** *Status: separate exhaustive exact computation;
attainment verified (C20).* No map with linear part in Lambda agrees with
more than 880 of the 20800 inputs of U. The value 880 is reached by the
translation word of Theorem L.

*Method.* By Proposition H, |Z(f)| is the sum over F5^3 of the products of
the fibre sizes of F_{h_d} and F_{h_a}, and the same holds for product
subsets such as E x B'. There are 240 * 240 * 625 = 36,000,000 half-maps.
The substitution (v, v') -> (l v, l^(-1) v') of a half preserves S, c and
w, so (g, g') and (l g, l^(-1) g') have the same fibre sizes on E, B' and
the whole half; this leaves 9,000,000 half-maps. The fibre sizes on E
depend only on the two translations and on the first columns of g and
g'. The pairs of halves are then maximised exactly by integer inner
products, with pruning by the Cauchy-Schwarz inequality for M1 and by row
and column maxima for M2. The same computations give 520 on U1 and 640
on O, in agreement with Proposition W and Theorem L. One of them reports
in addition that a map with a nonzero translation agrees on at most 30625
inputs, so that every map agreeing on more than 30625 inputs is linear.

## 8. An explicit cover

**Proposition C.** *Status: verified by the exact verifier on all 5^8
inputs, C = K, Canon target M (C22).* m_nat <= 65: the following 65 maps
of W^2 are induced by native words and their agreement sets cover W^2.

Each word "sr:t1t2t3t4" stands for the map that is, in reduced
eigen-coordinates,

```text
(x, y) -> (x + psi y + t, y),     psi = diag(s, r, -r, -s),     t = t1 e_++ + t2 e_+- + t3 e_-+ + t4 e_--,
```

that is, in Canon coordinates,
(x, y) -> (x + 2y + psi(3x + 4y) + 2t, 2x + 3y + psi(4x + 2y) + t). It
agrees at a reduced input if and only if B(t, y) = 0 and
2 B(x, psi y + t) + q(psi y + t) = q(y). The words with t = 0 are tangent
words.

```text
00:0000 11:0000 22:0000 44:0000 01:0000 10:0000 34:0000 20:0000 02:0000
03:0000 30:0000 14:0000 41:0000 12:0000 00:1111 00:1122 00:1133 00:1144
00:2211 00:2222 00:2233 00:2244 00:3311 00:3322 00:3333 00:3344 00:4411
00:4422 00:4433 00:4444 02:1312 02:1324 02:1331 02:1343 03:4212 03:4224
03:4231 03:4243 24:3300 11:2413 11:2421 11:2434 11:2442 13:3300 30:3113
30:3121 30:3134 30:3142 20:2413 20:2421 20:2434 20:2442 11:1312 11:1324
11:1331 11:1343 11:1414 11:1423 11:1432 11:1441 01:1100 44:4114 44:4123
44:4132 44:4141
```

These are maps of W^2 induced by native words: in reduced coordinates all
blocks are diagonal in the eigenbasis with determinant 1 on every plane,
so Corollaries 1 and 2 apply. As elements of N the words also act on Pi_q
and Pi_t, by the matrix they have on Pi_2, and can be chosen with Nu = 0.
The list was found by a greedy search in this family and is not claimed
to be short. Explicit products of the generators for such maps exist by
Theorem S. A mechanical construction of such products is reported to give
words of about two thousand letters each; they are not reproduced and not
verified here.

## 9. Fibres of size at most two

QUADRATIC-MEMORY-NATIVE-CONTACT [O] records that the data projection of a
successful binary contact has fibres of size at most two. For native
selectors the existence of such a data map is immediate; what is not
immediate is the number of alternatives.

**Existence.** *Status: proved here from Corollary 1 and from the Canon
results cited; the count in (1) is verified (C27).* There are native
selectors whose data map has all fibres of size at most two, for two
independent reasons.

(1) By Corollary 1 every translation of W^2 is induced by a native word.
Hence every map Phi of W^2 with G(Phi(z)) = M G(z) for all z is the data
map of a native selector: at z it uses the translation by Phi(z) - z, and
the number of alternatives is the number of distinct displacements. For
the selector of Theorem 3 of the note in #2068, transported to C = K, all
fibres have size at most two and there are 238985 distinct displacements
(C27).

(2) By
[ALGEBRAIC-RESIDUAL-REALIZATION](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#algebraic-residual-realization-t)
the word T_alg of the extended alphabet acts on the factor, that is on the
pistons, the two coordinates r and the bit eta, by a permutation
Pi_alg(p, r, eta) = (R(p, eta), r), with R independent of r.
[RESIDUAL-STEP-RECORD](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#residual-step-record-t)
states that the domain of T_alg is the reachable closure from the entire
layer eta = 0 and that the step V = A_y T_alg A_x satisfies
G(V z) = M G(z) on S0 ("its global factor action changes g to Mg"); the
two readers preserve the pistons and the bit
at their endpoints, so for z in S0 with pistons p the pistons of V z are
the piston component of R(p, 0). The same result gives the reachable
closure of T_alg from the layer eta = 0, with 450625 piston and bit
states. Because R is a permutation of the 2 * 5^8 pairs (p, eta), the map
that sends p to the piston component of R(p, 0) has fibres of size at most
two. T_alg contains the controls W_a and W_b, which are not native, but by
the paragraph on the registered controls in section 11 its data projection
from one bit value selects among finitely many native maps. So the piston
map of the Canon's residual step on the ready layer is, for every radical
value, a selection among finitely many maps of W^2 induced by native
words, with fibres of size at most two. The number of alternatives of that
selection is not determined here.

**Proposition F (74 native alternatives).** *Status: verified by the exact
verifier on all 5^8 inputs, in the original coordinates with K and M (C23,
C24).* The 74 maps of W^2 listed below are induced by native words, and
the selection rule stated below chooses at every input a listed map that
agrees there, in such a way that no output has more than two preimages:
107714 outputs have none, 175197 have one and 107714 have two. All 74 maps
are used. Lifted to V^2 with Nu = 0, and with the rule applied to the
pistons, this is a native selector with 74 alternatives that satisfies the
readout equation on every ready input for one initialized step and whose
data map on V^2 has all fibres of size at most two.

Each word "n1n2n3n4:t1t2t3t4" stands for the map that is, in reduced
eigen-coordinates,

```text
(u, v) -> (u + nu v + t, v),     nu = diag(n1, n2, n3, n4),     t = t1 e_++ + t2 e_+- + t3 e_-+ + t4 e_--.
```

Every nu is K-skew, n3 = -n2 and n4 = -n1. The maps are of the kind used
in section 8, with the same Canon form and the same agreement condition:
B(t, v) = 0 and 2 B(u, nu v + t) + q(nu v + t) = q(v).

```text
0000:0000 1144:0000 2233:0000 4411:0000 3412:0000 2003:0000 0230:0000 0320:0000
3002:0000 1414:0000 4141:0000 1234:0000 0000:1111 0000:1122 0000:1133 0000:1144
0000:2211 0000:2222 0000:2233 0000:2244 0000:3311 0000:3322 0000:3333 0000:3344
0000:4411 0000:4422 0000:4433 0000:4444 0230:1312 0230:1324 0230:1331 0230:1343
0320:4212 0320:4224 0320:4231 0320:4243 2413:3300 1144:2413 1144:2421 1144:2434
1144:2442 1324:3300 3002:3113 3002:3121 3002:3134 3002:3142 2003:2413 2003:2421
2003:2434 2003:2442 1144:1312 1144:1324 1144:1331 1144:1343 1144:1414 1144:1423
1144:1432 1144:1441 0140:1100 4411:4114 4411:4123 4411:4132 4411:4141 0410:3000
0000:0033 4321:0110 0000:0011 3322:1100 3002:0140 0000:0022 2143:2200 3002:2000
0140:3102 0000:0044
```

*Selection rule.* Use reduced eigen-coordinates (u, v). The 625 inputs
with the same v form a slice, and every listed map sends each slice to
itself. The slices are treated separately. In a slice every output has two
places, a first and a second, and the inputs are taken in lexicographic
order of u = (u_1, u_2, u_3, u_4), with u_1 the leading coordinate. An
input u is placed as follows.

1. Go through the listed maps in list order. A map that does not agree at
   (u, v) is skipped. For a map that agrees let o be its output. If o has
   already been examined since the placing of the current input of the
   lexicographic order began, the map is skipped; otherwise o counts as
   examined from now on.
2. If o has a free place, u takes the first free place of o, by this map,
   and is placed.
3. If both places of o are taken, the input in the first place of o is
   placed anew by steps 1 to 4, with the same record of examined outputs;
   if that succeeds, u takes over its place at o, by this map. Otherwise
   the same is tried with the input in the second place of o. If both
   fail, the list of step 1 is continued with the next map.
4. If the list is exhausted, the attempt for u fails.

At the end every input holds a place, and the selector sends it by the map
with which it holds that place. On V^2 the output radical is g_2 r, with
g_2 the invertible matrix of the chosen word on Pi_2, so an output of V^2
has as many preimages as its piston part.

This is the usual augmenting-path procedure for an assignment with at most
two inputs per output. By the standard theorem on augmenting paths it
places the largest possible number of inputs, so it places every input
whenever an assignment of all inputs exists. The verifier does not rely on
that theorem for Proposition F: it runs the rule and then evaluates
G(f(z)) = M G(z) and the number of preimages directly (C24).

*Continuation.* *Status: verified by the exact verifier (C25).* The data
map of the rule satisfies the hypothesis of Proposition 6 of the note in
#2068 for the Canon target: integers p with
p(M g) = p(g) + F_2(g) - F_0(M g) and 0 <= p(g) <= F_0(g) + F_1(g) exist
on every orbit of M on the Gram classes (orbit lengths 1, 2 and 10). So
the data map extends to a permutation of W^2 times {0,1} that satisfies
the readout equation on its whole reachable set. In the least solution
107714 occupied states are created in the first step and 40866 further
occupied states are passed through; the reachable set then has
390625 + 107714 + 40866 = 539205 of the 781250 states. The minimum in
QUADRATIC-L5-INITIALIZED-CAPACITY, which T_alg attains, is 450625. This
continuation is abstract: on the occupied layer it uses matchings, not
native words.

*Bounds.* Let m_2 be the least number of alternatives of a native selector
whose data map has all fibres of size at most two. By Theorem L and
Proposition F,

```text
25 <= m_nat <= m_2 <= 74.
```

Remarks.

- The 65 maps of section 8 do not suffice for fibres of size at most two:
  with at most two inputs per output they serve at most 388985 of the
  390625 inputs (C26, by the same procedure and the theorem on augmenting
  paths).
- The list and the rule were found by search and are not claimed to be
  optimal. The numbers 107714, 175197, 107714 and 539205 belong to the
  rule as stated; a different order of augmentation is reported to give
  107702, 175221, 107702 and a least reachable set of 539075 states.
- The selection rule is an assignment computed from the target. It is not
  a native primitive and is not given by a formula.

## 10. The verifier

`python3 verify.py` uses only the Python standard library and exact
integer arithmetic modulo 5. It is deterministic, writes no file, prints
one line per check and exits with status 1 if a check fails. Its output
must equal [`EXPECTED.txt`](EXPECTED.txt) byte for byte
(`python3 verify.py | cmp - EXPECTED.txt`). It runs in about fifteen
seconds on one core.

The four constants and the five generators are restated verbatim from
`reproduce/kernel-connectivity/verify.py` (its lines 41 to 73); that file
is not imported.

- C01, C02: the five generators are affine involutions on all 15625 cell
  states; block form of the twelve maps; order of P and Q.
- C03 to C05: eigenvectors, K in the eigenbasis, the table of section 2,
  the determinant patterns.
- C06: step 2 of Theorem S with the explicit elements named in the proof;
  the orders 120 are obtained by enumeration.
- C07, C08: the unipotent part; the three translation words, each
  evaluated directly at the origin and the twelve unit vectors, which
  determines an affine map; the closure dimensions 2, 8, 12.
- C09: the determinant count of Corollary 2.
- C10 to C14: the 25 skew maps and 16 isometries; agreement sets of the
  tangent words on all 5^8 inputs in the original coordinates with K and
  M; the sets U, O, U1 pointwise; Proposition O.
- C15: the count for Theorem L and a word reaching 640.
- C16 to C19: Lemma 2, Lemma 3, the case arithmetic and a map reaching
  520. No symmetry reduction is used: all six root points are tabulated
  and the family H0 is enumerated in full. The verifier relies on
  Proposition H and Lemma 1, which are proved above.
- C20, C21: maps reaching 880 on U and 40625 in total. The maxima of
  section 7 themselves are not checked.
- C22: the cover of section 8, by direct evaluation of G(f(z)) and
  M G(z) at every input for each of the 65 maps.
- C23: the 74 maps of section 9; every input agrees with at least one of
  them, by direct evaluation in the original coordinates.
- C24: the selection rule of section 9 is run slice by slice in reduced
  eigen-coordinates. The result is then re-evaluated in the original
  coordinates: for every Canon input the selected map is applied, the
  three Gram equations for K and M are tested, and the preimages of
  every output are counted.
- C25: the integers of Proposition 6 of the note in #2068 for the Canon
  target, on all 125 Gram classes, and the size of the least reachable
  set.
- C26: the same procedure on the 65 maps of section 8; the number of
  inputs it places is the largest possible by the theorem on
  augmenting paths.
- C27: the selector of Theorem 3 of the note in #2068, rebuilt from its
  six maps psi_i and six isometries and transported to C = K; its
  fibres and its distinct displacements.

This verifier is a local audit. It is not a formal evidence directory, a
preregistration or a probe.

## 11. Falsifiers and boundary

- Theorem S is refuted by a native word outside the stated class, or by a
  map of the stated class that is not a native word; the verifier would
  report a wrong generator table, pattern or translation word.
- Theorem L is refuted by 24 native words whose agreement sets cover the
  ready inputs of one radical value, or by one map with linear part in
  Lambda that agrees with more than 640 inputs of O.
- Proposition W is refuted by a map with linear part in Lambda that
  agrees with more than 520 inputs of U1.
- Statements M1 and M2 are refuted by a map of W^2 with linear part in
  Lambda, not of tangent type, with more than 40625 agreeing inputs,
  respectively by such a map agreeing with more than 880 inputs of U.
- Proposition C is refuted by an input at which none of the 65 listed
  maps satisfies G(f(z)) = M G(z); the verifier would report it.
- Proposition F is refuted by an input at which the map selected by the
  rule of section 9 violates G(f(z)) = M G(z), or by an output with
  three preimages; the verifier would report either (C24). The bound
  m_2 <= 74 is refuted only together with Proposition F.

Boundary. Sections 2 to 8 concern one property only: at every ready input
some alternative satisfies the Gram identity for one initialized step,
with C = K + 0_2 and the Canon target M. The selection rule is arbitrary.
Theorem L is therefore a lower bound on any data-dependent multibranch
control over this word class; it is not a construction of an admitted
contact. Section 9 adds a second property of the data map: with 74
native alternatives and one explicit selection rule all fibres have size
at most two, and this data map admits the abstract continuation of
#2068. What is not said: the selection rule of section 9 is an
assignment computed from the target, not a native primitive; the
register write is not constructed; the maps of the continuation on the
occupied layer are matchings, not native words; and no reversible
native realization of the selector is given.

For QUADRATIC-MEMORY-NATIVE-CONTACT [O] this gives the following and no
more. If the declared gate alphabet is the slotwise word class of
QUADRATIC-L5-NATIVE-OBSTRUCTIONS and the data projection on the ready
layer is a selection among fixed words of that class, then at least 25
distinct words must be selected among, 65 suffice for the Gram identity
alone, and 74 suffice for the Gram identity together with fibres of size
at most two, in each case with an unrestricted selection rule. The
independent admission of C and of the reading, the selection rule, the
bit write and a continuation by native words are not addressed, and no
admitted permutation is supplied. The item stays open.

The registered controls W_a, W_b and the couplings Ucal_i of
DEF-RESIDUAL-CONTACT-ARCHITECTURE are not elements of N: W_i acts on
F5^12 times {0,1} and applies the identity or I_i, that is a_x a_y or
b_x b_y, depending on the cross-Gram component and on the bit, and Ucal_i
permutes the coordinate t of one cell depending on its q. At every input,
however, each of them acts on F5^12 as an element of N: as I_i, as the
identity, or as a translation of that coordinate t. Hence every fixed word
of the extended alphabet, applied from one bit value, has a data
projection that selects among finitely many native maps, at most two for
every occurrence of a control W_i and five for every occurrence of a
coupling Ucal_i, and Theorem L applies to it. In particular the
composition V = A_y T_alg A_x of RESIDUAL-STEP-RECORD, which satisfies
G(V z) = M G(z) on S0, selects among at least 25 distinct native maps on
every slice of S0 with fixed q, and any word of that alphabet with this
property contains n_W controls and n_U couplings with
2^(n_W) * 5^(n_U) >= 25. This is consistent with the Canon, whose word
T_alg is very long. Section 9 uses of that construction only that the
piston map of T_alg from the layer eta = 0 has fibres of size at most
two; nothing here concerns its records or its bit.

The statements depend on the word class as fixed in section 1. For
diagonal letters only, or without the couplings, the group is different
and none of the counts above is claimed.

## 12. Open

- The exact value of m_nat, between 25 and 65. By the last remark of
  section 5 a selector with 25 alternatives would have to cover O exactly
  once.
- Whether test sets other than O and U1, or weights on a larger set of
  inputs, give a lower bound above 25.
- The least number m_2 of native alternatives of a native selector whose
  data map has all fibres of size at most two. By section 9 it lies
  between 25 and 74.
- A lower bound specific to fibres. The only lower bound for m_2 used
  here is Theorem L, which does not use the fibre condition.
- Whether the continuation on occupied memory can be carried by native
  words, and with how many, and whether the selection and the register
  write can be realized natively. Section 9 gives the abstract
  continuation only; the Canon's T_alg realizes a continuation in the
  extended alphabet with the controls W_a and W_b.
- The same questions for the diagonal word class.
