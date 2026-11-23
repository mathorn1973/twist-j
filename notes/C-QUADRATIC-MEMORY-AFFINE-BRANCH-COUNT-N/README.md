# Affine alternatives on the common-ready layer: five never suffice, six suffice for rank four with square determinant

**NON-CANONICAL / L1 / analytical note**

Public Canon v116, activation commit
[93c36089db57032a6cbca482ff62c95884567d0f](https://github.com/mathorn1973/twist-j/commit/93c36089db57032a6cbca482ff62c95884567d0f).
The source results are
[DEF-QUADRATIC-MEMORY-L5](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#def-quadratic-memory-l5),
[QUADRATIC-L5-INITIALIZED-CAPACITY](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#quadratic-l5-initialized-capacity-t)
and
[QUADRATIC-L5-NATIVE-OBSTRUCTIONS](https://github.com/mathorn1973/twist-j/blob/93c36089db57032a6cbca482ff62c95884567d0f/canon/CANON.md#quadratic-l5-native-obstructions-t).
The question comes from the note in pull request
[#2063](https://github.com/mathorn1973/twist-j/pull/2063)
(head 5c47b58bd1fcd5702625b12f5766cfb150fc5414), which excludes selectors
with at most four affine alternatives and leaves the sufficiency of five
alternatives open.

Companion files: [`verify.py`](verify.py), an exact audit that uses only
the Python standard library, and [`EXPECTED.txt`](EXPECTED.txt), its exact
output. Labels C01 to C47 below refer to the lines of that output.

## 1. Problem and results

All arithmetic is in F5. Fix a symmetric C on V = F5^6 of rank r and write

```text
q(x) = x^T C x,   B(x,y) = x^T C y,   G(x,y) = (q(x), B(x,y), q(y)) = (a,b,c).
```

The fixed marked B of DEF-QUADRATIC-MEMORY-L5 identifies G with the readout
D_C = B G, and B M = L5 B with M(a,b,c) = (3b, 4a+4b+4c, 3b+3c) (C01). The
carrier is V^2 times {0,1}, and the whole bit-0 layer is ready once.

An affine branch is a map f(z) = A z + t of V^2 = F5^12, with A an arbitrary
12 by 12 matrix and t a vector. Its agreement set is

```text
Z(f) = { z in V^2 : G(f(z)) = M G(z) }.
```

A selector with m affine alternatives is a map of V^2 whose value at each z
is one of f_1(z), ..., f_m(z). A selector among f_1, ..., f_m whose data
output satisfies the readout equation on every ready input, for one
initialized step, exists exactly when the sets Z(f_1), ..., Z(f_m) cover
V^2. Let m*(C) be the least m for which such branches exist. Nothing is
assumed about the selection rule, the ignored register or reversibility.

By QUADRATIC-L5-INITIALIZED-CAPACITY, C is congruent to
diag(1^(r-1), delta, 0^(6-r)) with delta in {1,2}; write (r, delta) for this
class. "Square determinant" refers to the nondegenerate part and means
delta = 1. For r = 1 or 2 some required Gram value has an empty fibre, so no
selector of any kind exists: in the reduced model of section 2 the target
adds q(y)^2 to the Gram determinant, while the attained determinants are 0
for r = 1 and 0 or delta times a nonzero square for r = 2. For r >= 3 all
125 Gram values are attained and 125 constant branches cover V^2, so
1 <= m*(C) <= 125.

| Statement | Status |
|---|---|
| Theorem 1: m*(C) >= 6 for every C of rank 3, 4, 5 or 6 | proved here |
| Theorem 2: m*(C) = 6 for rank 4 with square determinant; this class contains C = K + 0_2 of DEF-RESIDUAL-CONTACT-ARCHITECTURE | proved here; the cover is also verified (C10, C11, C16) |
| Proposition 3: the largest agreement set of one affine branch has 5^(2r-1) + 4 * 5^(r+w-1) elements of the reduced domain, w as in section 7 | upper bound proved here; attainment verified (C23, C25, C26, C27) |
| Proposition 4: m* <= 25 for (4,2), m* <= 29 for (5,1) and (5,2), m* <= 25 for (6,1) and (6,2) | verified by the exact verifier (C30 to C34) |
| Proposition 5: in the classes (3,1), (3,2), (4,2), (5,1), (5,2), (6,2) no six branches of tangent type cover | proved here; two finite lemmas verified (C36, C37) |
| Theorem 3: for rank 4 with square determinant the six branches of Theorem 2, each composed with a suitable output isometry, admit a selector whose data map has all fibres of size at most two | verified by the exact verifier on all 5^8 inputs (C44, C45); reduction to two finite maps, tau on F5^3 and sigma on 150 isotropic classes, proved here (C42, C43) |
| Proposition 6: the data map of Theorem 3 extends to a complete permutation of the carrier with the readout equation on its reachable set | criterion proved here; hypothesis verified (C46) |
| Proposition 7: the data map of Theorem 3 has a complete permutation that selects among six linear maps on the ready layer and among 15 linear maps on its reachable occupied states, with the readout equation on its reachable set; which map is applied on the occupied layer is given by tables derived from the target | verified by the exact verifier: bijectivity on all 781250 states and the readout equation at every reachable state (C47) |
| The exact value of m* outside rank 4 with square determinant; the least number of occupied-layer alternatives and the least reachable set of such a permutation | open |

Sections 2 to 4 prepare the proofs. Every statement carries one of the
labels "proved here", "verified by the exact verifier" or "open".

## 2. Reduction

For a 2 by 2 matrix g = [[p,q],[s,u]] over F5 let g x 1 act on pairs by
(x,y) -> (p x + q y, s x + u y). Bilinearity of B gives, for every C,

```text
G((g x 1) z) = Sym2(g) G(z),
Sym2(g) = [[p^2, 2pq, q^2], [ps, pu+qs, qu], [s^2, 2su, u^2]]        (C03).
```

**Lemma 1 (reduction).** *Status: proved here.*

(a) m*(C) depends only on the class (r, delta), and it equals the covering
number of the nondegenerate form C_0 = diag(1^(r-1), delta) on W = F5^r,
with W^2 = F5^(2r) in place of V^2.

(b) Put g_out = [[0,1],[2,1]], g_in = [[1,1],[3,1]] and
M0(a,b,c) = (a+c, b, c). Then Sym2(g_out) M Sym2(g_in) = M0 (C02), and
f -> (g_out x 1) f (g_in x 1) is a bijection of the set of affine branches
that carries the agreement set of f for M onto (g_in x 1)^(-1) Z(f), the
agreement set of the image for M0. Covers correspond to covers.

*Proof.* (a) If P is invertible and P^T C P = N, then
G_C(Px, Py) = G_N(x, y), so f -> (P x P)^(-1) f (P x P), with P acting on
both cells, carries branches and agreement sets for C to those for N. Let
N = diag(C_0, 0) and split V = W + R with R the last 6-r coordinates. G_N
ignores the R-components. A cover of V^2 by branches F_i gives the cover of
W^2 by the affine maps w -> (W-components of F_i(w)). A cover of W^2 by
f_i gives the cover of V^2 by (w + rho) -> f_i(w) + rho.

(b) If G(f(z)) = M G(z) at z = (g_in x 1) z', then
G((g_out x 1) f (g_in x 1) z') = Sym2(g_out) M Sym2(g_in) G(z') = M0 G(z').
All maps involved are invertible, so the converse holds as well. QED

From here to the end of section 10, W = F5^r with 3 <= r <= 6, C is
nondegenerate, and the target is M0, except where the Canon target M is
named (Propositions 6 and 7 concern iteration and are stated for M). A
branch is written
f(x,y) = (x', y') and its residuals are

```text
rho_a = q(x') - q(x) - q(y),   rho_b = B(x',y') - B(x,y),   rho_c = q(y') - q(y).
```

Z(f) is the common zero set of the three residuals. They are polynomials of
total degree at most 2 in the 2r coordinates. A polynomial in which every
variable has degree below 5 vanishes on all of F5^n only if it is the zero
polynomial (the Canon uses the same fact in
QUADRATIC-L5-NATIVE-OBSTRUCTIONS), so "identically zero" is unambiguous.

A linear map psi of W is called C-skew if C psi is antisymmetric, that is
B(psi y, y') = -B(y, psi y') for all y, y'. Then B(psi y, y) = 0, the rank
of psi is even, and a nonzero psi has at most 5^(r-2) kernel vectors.

## 3. Branches of tangent type

**Lemma 2 (tangent type).** *Status: proved here; the slice counts and the
size formula are also verified for rank 4 (C22 to C25).*

rho_b and rho_c are both identically zero if and only if

```text
f(x,y) = (k(x + psi y), k y),   k in O(C),   psi C-skew.
```

For such f ("tangent type") the agreement set is

```text
Z_psi = { (x,y) : 2 B(x, psi y) + q(psi y) = q(y) }.
```

Over a fixed y it is an affine hyperplane of x (5^(r-1) points) if
psi y != 0; if psi y = 0 it is the whole slice when q(y) = 0 and empty when
q(y) != 0. Consequently

```text
|Z_psi| = 5^(r-1) (5^r - |ker psi|) + 5^r #{ y in ker psi : q(y) = 0 }.
```

*Proof.* Write x' = A11 x + A12 y + t1 and y' = A21 x + A22 y + t2.
Suppose rho_c = 0. Its quadratic part gives q(A21 x) = 0,
B(A21 x, A22 y) = 0 and q(A22 y) = q(y) for all x, y. Hence
A22^T C A22 = C, so k := A22 is invertible and lies in O(C); then A21 x is
orthogonal to all of W, so A21 = 0 because C is nondegenerate. The linear
part gives 2 B(k y, t2) = 0, so t2 = 0. Suppose in addition rho_b = 0, that
is B(A11 x + A12 y + t1, k y) = B(x,y). The part bilinear in (x,y) gives
B(A11 x, k y) = B(x,y) = B(kx, ky), so A11 = k. The part quadratic in y
gives B(A12 y, k y) = 0, so psi := k^(-1) A12 satisfies B(psi y, y) = 0 for
all y, which by polarization is C-skewness. The linear part gives t1 = 0.
The converse is a direct substitution. For f of this form,
rho_a = q(x + psi y) - q(x) - q(y) = 2 B(x, psi y) + q(psi y) - q(y). For
fixed y this is an affine function of x whose linear part x -> 2 B(x, psi y)
is nonzero exactly when psi y != 0, since C is nondegenerate. QED

## 4. Branches that are not of tangent type

**Lemma A (weighted zero count).** *Status: proved here.* Let P be a nonzero
polynomial in N variables over F5 of total degree at most d. For a in F5^N
put w_P(a) = 0 if P(a) != 0, w_P(a) = 2 if P and all its formal first
partial derivatives vanish at a, and w_P(a) = 1 otherwise. Then the sum of
w_P(a) over all a in F5^N is at most d 5^(N-1).

*Proof.* Induction on N. For N = 1, if P(a) = P'(a) = 0 then (u - a)^2
divides P: writing P = (u - a) Q gives P'(a) = Q(a). So the sum of the
weights is at most the number of roots counted with multiplicity, at most d.
For N >= 2 write u = (u', s) with s the last variable and
P = sum_{j=0..t} P_j(u') s^j with P_t != 0; then deg P_t <= d - t. Let
w_t be the weight function of P_t on F5^(N-1). For every a' the claim is

```text
sum over s in F5 of w_P(a', s)  <=  t + 5 w_t(a').
```

If w_t(a') = 0, then P(a', s) is a polynomial in s of exact degree t, and
w_P(a', s) is at most the multiplicity of s as a root of it (weight 2
requires that P and dP/ds vanish). If w_t(a') = 2, the left side is at most
10. If w_t(a') = 1, some dP_t/du_i with i < N is nonzero at a'. The
polynomial dP/du_i = sum_j (dP_j/du_i) s^j, evaluated at u' = a', has exact
degree t in s and vanishes at every s with w_P(a', s) = 2; there are at most
t such s, so the left side is at most 5 + t. Summing the claim over a' and
using the induction hypothesis for P_t gives
t 5^(N-1) + 5 (d - t) 5^(N-2) = d 5^(N-1). QED

Lemma A is the special case, with multiplicities truncated at two and
S = F5, of the Schwartz-Zippel lemma with multiplicities: for a nonzero
polynomial P of total degree at most d over a field F and a finite subset S
of F, the sum of mult(P, z) over z in S^n is at most d |S|^(n-1)
(Z. Dvir, S. Kopparty, S. Saraf, M. Sudan, "Extensions to the method of
multiplicities, with applications to Kakeya sets and mergers", SIAM Journal
on Computing 42 (2013), 2305-2328). The proof above is self-contained and
the reference is not used. C05 checks Lemma A exhaustively for all
univariate polynomials of degree at most 4 and all bivariate polynomials of
degree at most 2.

**Lemma 3 (non-tangent bound).** *Status: proved here.* If f is an affine
branch that is not of tangent type, then |Z(f)| <= 4 * 5^(2r-2).

*Proof.* Put n = 2r and let A be the linear part of f.

*Step 1: rho_a is irreducible of degree 2.* Its quadratic part has the
symmetric matrix S_a = A_x^T C A_x - diag(C, C), where A_x = (A11 A12) is
the r by 2r matrix of the x'-rows and diag(C, C) is the block-diagonal
matrix of q(x) + q(y). Since rank diag(C, C) = 2r and
rank(A_x^T C A_x) <= r, the rank of S_a is at least r >= 3. A product of
two polynomials of degree 1 has a quadratic part of rank at most 2. So
rho_a has degree 2 and no factorization over F5.

*Step 2: rho_b and rho_c are not both multiples of rho_a unless both are
zero.* Suppose rho_b = beta rho_a and rho_c = gamma rho_a with
(beta, gamma) != (0,0). For la = (la_a, la_b, la_c) in F5^3 put
rho_la = la_a rho_a + la_b rho_b + la_c rho_c
= (la_a + beta la_b + gamma la_c) rho_a. Directly from the definitions,
rho_la(z) = la.G(f(z)) - (la M0).G(z). The quadratic form z -> la.G(z) has
the symmetric matrix L(la) (x) C, the Kronecker product with

```text
L(la) = [[la_a, la_b/2], [la_b/2, la_c]],      rank(L(la) (x) C) = r rank L(la),
la M0 = (la_a, la_b, la_a + la_c) =: la',      det L(la') = det L(la) + la_a^2   (C04).
```

On the plane Pi: la_a + beta la_b + gamma la_c = 0 the polynomial rho_la is
zero, in particular its quadratic part:

```text
A^T (L(la) (x) C) A = L(la') (x) C        for all la in Pi.              (*)
```

(i) If la in Pi is nonzero with det L(la) = 0, the left side of (*) has
rank at most r, so rank L(la') <= 1, det L(la') = 0, hence la_a = 0; then
det L(la) = -la_b^2/4 = 0 gives la_b = 0. So la is a multiple of (0,0,1).

(ii) If gamma = 0, then beta != 0 and la = (4 beta^2, beta, 1) lies in Pi
with det L(la) = 4 beta^2 - beta^2/4 = 0 and la_a != 0, contradicting (i).

(iii) If gamma != 0, take la1 = (0, gamma, -beta) in Pi. Then la1' = la1
and L1 := L(la1) has determinant -gamma^2/4 != 0, so (*) for la1 shows that
A is invertible. Take la2 in Pi with first coordinate 1, and put
L2 = L(la2), L2' = L(la2'). Dividing (*) for la2 by (*) for la1 gives

```text
A^(-1) ((L1^(-1) L2) (x) I_r) A = (L1^(-1) L2') (x) I_r.
```

The two sides have the same characteristic polynomial, so
det(t - L1^(-1) L2)^r = det(t - L1^(-1) L2')^r in F5[t]. Both bases are
monic, and unique factorization gives det(t L1 - L2) = det(t L1 - L2').
Since la -> la' and L are linear and la1' = la1, the right side is
det L((t la1 - la2)'), and the polynomial identity
det L(la') = det L(la) + la_a^2 at la = t la1 - la2, whose first coordinate
is -1, gives det(t L1 - L2') = det(t L1 - L2) + 1. This is a contradiction.

*Step 3.* Since f is not of tangent type, rho_b and rho_c are not both
zero. By step 2 there is rho' in {rho_b, rho_c} that is nonzero and not a
scalar multiple of rho_a. Z(f) is contained in X = {rho_a = 0 = rho'}.

*Step 4: |X| <= 4 * 5^(n-2).* Since S_a != 0 and 2 is invertible, there is
a vector d with S_a(d,d) != 0. Complete d to a basis and use coordinates
(u, t) in F5^(n-1) times F5, z = sum u_i b_i + t d. This linear bijection
preserves degrees and zero counts. Then

```text
rho_a = alpha t^2 + p1(u) t + p0(u),    alpha = S_a(d,d) != 0, deg p1 <= 1, deg p0 <= 2,
rho'  = alpha' t^2 + r1(u) t + r0(u),   alpha' in F5,          deg r1 <= 1, deg r0 <= 2.
```

Put rho'' = rho' - (alpha'/alpha) rho_a = b(u) t + c(u), with deg b <= 1
and deg c <= 2. Then rho'' != 0 because rho' is not a multiple of rho_a,
and X = {rho_a = 0 = rho''}. Define

```text
R(u) = alpha c^2 - p1 b c + p0 b^2,      deg R <= 4.
```

Expanding the product gives the polynomial identity

```text
b^2 rho_a = rho'' (alpha b t + p1 b - alpha c) + R.                    (**)
```

R is not the zero polynomial. If b = 0 then R = alpha c^2 and c != 0. If
b != 0 and R = 0, then by (**) and unique factorization in F5[u,t] the
irreducible rho_a divides rho'' or alpha b t + p1 b - alpha c; both are
nonzero of degree at most 1 in t, while rho_a has degree 2 in t.

For u in F5^(n-1) let m(u) be the number of t with (u,t) in X. Then
m(u) <= w_R(u) in each of the three possible cases:

1. b(u) != 0. Then rho''(u,t) = 0 only for t = -c(u)/b(u), so m(u) <= 1,
   and if m(u) = 1 then (**) at that point gives R(u) = 0, so w_R(u) >= 1.
2. b(u) = 0 and c(u) != 0. Then rho''(u,t) = c(u) != 0 and m(u) = 0.
3. b(u) = c(u) = 0. Then m(u) <= 2 because rho_a(u,t) has exact degree 2
   in t. Moreover R(u) = 0, and by the product rule every first partial
   derivative of alpha c^2 - p1 b c + p0 b^2 is a sum of terms each of which
   contains a factor b or c; so all of them vanish at u and w_R(u) = 2.

Summing over u and applying Lemma A to R, with N = n-1 and d = 4, gives
|X| <= 4 * 5^(n-2). QED

C17 evaluates 13 explicit branches that are not of tangent type on all 5^8
inputs for r = 4; the largest agreement set found has 34375 elements, below
the bound 62500. This is a sanity check and not part of the proof.

## 5. Five alternatives never suffice

**Theorem 1.** *Status: proved here.* For every symmetric C of rank 3, 4, 5
or 6, no five affine branches cover the common-ready layer: m*(C) >= 6.

*Proof.* By Lemma 1 work in the reduced model. Let N_r(0) be the number of
y in W with q(y) = 0, let T = {(x,y) : q(y) != 0}, and let
theta = |T| / 5^(2r) = 1 - N_r(0)/5^r. The Canon counts (recomputed in C18
and C19) are

| class | (3,1), (3,2) | (4,1) | (4,2) | (5,1), (5,2) | (6,1) | (6,2) |
|---|---|---|---|---|---|---|
| N_r(0) | 25 | 145 | 105 | 625 | 3225 | 3025 |
| theta | 4/5 | 96/125 | 104/125 | 4/5 | 496/625 | 504/625 |

so theta >= 96/125 in every class. Suppose five branches cover W^2, and
let k of them be of tangent type, with skew maps psi_i. By Lemma 2:

- a tangent branch with psi_i = 0 agrees exactly on {q(y) = 0}, which is
  disjoint from T;
- a tangent branch with psi_i != 0 agrees on at most 5^(r-1) points of each
  slice, except on slices over the at most 5^(r-2) vectors y with
  psi_i y = 0;
- by Lemma 3 a branch not of tangent type agrees on at most
  4 * 5^(2r-2) = (4/25) 5^(2r) points.

*Case A: some psi_i = 0.* That branch covers nothing of T. The other
tangent branches cover at most |T|/5 points of T each, so T would need

```text
((k-1)/5) theta + (5-k) (4/25) >= theta,   i.e.   theta <= 4(5-k) / (5(6-k)).
```

For k = 1, ..., 5 the right side is 16/25, 3/5, 8/15, 2/5, 0, always below
96/125 (C21). Contradiction.

*Case B: no psi_i = 0 and k <= 4.* On a slice over y the tangent branches
cover at most k 5^(r-1) points if psi_i y != 0 for all i, and at most 5^r
points in any case; at most k 5^(r-2) vectors y are killed by some psi_i.
The tangent branches therefore cover at most
k 5^(2r-1) + k (5-k) 5^(2r-3) points, and all five branches at most

```text
5^(2r) ( k/5 + k(5-k)/125 + 4(5-k)/25 ) = 5^(2r) (100 + 10k - k^2) / 125,
```

which for k = 0, ..., 4 is 100/125, 109/125, 116/125, 121/125, 124/125 of
the domain (C20). Contradiction.

*Case C: k = 5 and no psi_i = 0.* Fix y with q(y) != 0. The slice has 5^r
points and each branch covers a hyperplane or nothing, so the five
hyperplanes H_i = {x : 2 B(x, n_i) + q(n_i) = q(y)}, n_i = psi_i y, are
pairwise disjoint, hence pairwise parallel: n_i = s_i n with s_i in
{1,2,3,4}. Two of the five s_i coincide, so two of the n_i are equal, and
H_i is determined by n_i. Two of the hyperplanes coincide. Contradiction.
QED

The theorem uses neither the scalar test of the note in pull request #2063
nor its per-branch bound; it replaces the count over branches by the
structure of Lemma 2 and the bound of Lemma 3.

## 6. Six alternatives for rank four with square determinant

Let

```text
Li = [[0,4,0,0],[1,0,0,0],[0,0,0,4],[0,0,1,0]],
Lj = [[0,0,4,0],[0,0,0,1],[1,0,0,0],[0,4,0,0]],
D+ = Li + 2 Lj,   D- = Li + 3 Lj.
```

These 4 by 4 matrices are antisymmetric, Li^2 = Lj^2 = -I,
Li Lj + Lj Li = 0, D+^2 = D-^2 = 0 and D+ D- + D- D+ = I (C06, C08).
Hence (a D+ + b D-)^2 = ab I for all a, b in F5.

Let W4 be a subspace of W with a basis v_1, ..., v_4 such that
B(v_k, v_l) = sigma if k = l and 0 otherwise, sigma in {1,2}. For y in W
put c_k(y) = B(v_k, y)/sigma and y_4 = sum c_k(y) v_k, so that
q(y_4) = sigma sum c_k(y)^2. For a 4 by 4 matrix X define the map
X^V y = sum_k (X c(y))_k v_k of W. If X is antisymmetric, X^V is C-skew,
because B(X^V y, y') = sigma c(y')^T X c(y). For X = a D+ + b D- one has
X^T X = -X^2 = -ab I, hence

```text
q((a D+ + b D-)^V y) = -ab q(y_4).
```

**Lemma 4 (pencil).** *Status: proved here.* Let kappa, a_0, b_0 in F5 with
a_0 b_0 = kappa, and let (a_1,b_1), ..., (a_6,b_6) be six points of the
cross {a = a_0} or {b = b_0} that lie on six different lines through the
origin of F5^2. Then every (x,y) with q(y) = kappa q(y_4) lies in the
agreement set of one of the six tangent branches (x,y) -> (x + psi_i y, y),
psi_i = (a_i D+ + b_i D-)^V.

*Proof.* By Lemma 2 the residual of the branch with parameters (a,b) at
(x,y) is

```text
2a B(x, D+^V y) + 2b B(x, D-^V y) - (ab + kappa) q(y_4).
```

On the cross ab + kappa = b_0 a + a_0 b: if a = a_0 both sides equal
a_0 b + a_0 b_0, and if b = b_0 both equal a b_0 + a_0 b_0. So the residual
equals a s_1 + b s_2 with

```text
s_1 = 2 B(x, D+^V y) - b_0 q(y_4),   s_2 = 2 B(x, D-^V y) - a_0 q(y_4),
```

which do not depend on (a,b). Six pairwise non-proportional vectors (a,b)
represent all six lines through the origin of F5^2, and one of these lines
is orthogonal to (s_1, s_2). QED

For a_0 != 0 the points (a_0, t), t in F5, and (0, b_0) are six such
points.

**Theorem 2.** *Status: proved here; the cover is also verified on all 5^8
inputs of the nondegenerate part (C10, C14, C16).* Let C have rank 4 and
square determinant. Then m*(C) = 6. For C = I_4 on the nondegenerate part
and psi = alpha Li + beta Lj with

```text
(alpha, beta) in { (3,0), (0,1), (1,1), (2,3), (4,2), (4,3) },
```

the six linear maps (x,y) -> (x + psi y, y) cover the reduced domain for the
target M0, and in Canon coordinates the six linear maps

```text
f_psi(x,y) = ( x + 2y + psi(3x + 4y),  2x + 3y + psi(4x + 2y) )
```

cover the common-ready layer for the Canon target M. On V = F5^6 with
C = diag(1,1,1,1,0,0), psi acts on the first four coordinates of a cell and
the two radical coordinates of each cell may be mapped in any way.

*Proof.* Lower bound: Theorem 1. Upper bound in the reduced model:
psi^T psi = -psi^2 = (alpha^2 + beta^2) I, so by Lemma 2 the branch agrees
at (x,y) exactly when 2 B(x, psi y) + (alpha^2 + beta^2 - 1) q(y) = 0. For
the six pairs alpha^2 + beta^2 - 1 = alpha modulo 5 (C07), so the condition
is alpha s_1 + beta s_2 = 0 with s_1 = 2 B(x, Li y) + q(y) and
s_2 = 2 B(x, Lj y). The six pairs represent the six points of the
projective line over F5 (C07), so one of them is orthogonal to (s_1, s_2).
This is Lemma 4 with W4 = W, kappa = 1: in the coordinates
psi = a D+ + b D- the six pairs are the points (4,4), (4,1), (4,0), (2,4),
(3,4), (0,4) of the cross through (4,4) (C08).

Canon coordinates: by Lemma 1(b) the corresponding branches for M are
(g_out x 1)^(-1) (x + psi y, y) (g_in x 1)^(-1), with
g_in^(-1) = [[2,3],[4,2]] and g_out^(-1) = [[2,3],[1,0]]. Substituting
u = 2x + 3y, v = 4x + 2y into (2(u + psi v) + 3v, u + psi v) gives the
stated formula (C09). The statement for V = F5^6 is Lemma 1(a). QED

For a general C of rank 4 with square determinant choose P with
P^T C_0 P = I_4 on the nondegenerate part and replace psi by P psi P^(-1).
The Canon's C = K + 0_2 with K = antidiag(3,2,2,3) has det K = 1 and

```text
P = [[1,2,0,0],[0,0,1,2],[0,0,4,2],[1,3,0,0]],     P^T K P = I_4   (C15);
```

the six branches f_psi with psi replaced by P psi P^(-1) cover all 5^8
inputs for C = K, and no five of them do (C16).

A selector may choose, at each input, any index i with
alpha_i s_1 + beta_i s_2 = 0, where s_1, s_2 are evaluated at
(u,v) = (2x + 3y, 4x + 2y). An input agrees with exactly one of the six
branches unless s_1 = s_2 = 0, in which case it agrees with all six
(369600 and 21025 of the 390625 reduced inputs, C12). No five of the six
branches cover (C11).

## 7. The largest agreement set of one branch

Let N_s(0; eps) be the Canon's count of isotropic vectors of a
nondegenerate form of dimension s and determinant character eps, with
N_0 = 1. Define w = w(r, delta) by

| class | (3,1), (3,2) | (4,1) | (4,2) | (5,1), (5,2) | (6,1) | (6,2) |
|---|---|---|---|---|---|---|
| w | 1 | 2 | 1 | 2 | 3 | 2 |
| (5^(2r-1) + 4 * 5^(r+w-1)) / 5^(2r) | 29/125 | 29/125 | 129/625 | 129/625 | 129/625 | 629/3125 |

**Proposition 3 (per-branch maximum).** For every affine branch f of the
reduced model, |Z(f)| <= 5^(2r-1) + 4 * 5^(r+w-1), and the bound is
attained by a branch of tangent type. *Status: the upper bound is proved
here. Attainment is verified by the exact verifier: by enumeration of all
skew psi for ranks 3 and 4 (C23, C25, C26) and by explicit branches for
ranks 5 and 6 (C27).* As fractions of the ready layer the maxima are the
last row of the table. The bound 29/125 of the note in pull request #2063
is attained in rank 4 only for square determinant, for instance by
(x,y) -> (x + 2y, 2x + 3y), the map f_psi of Theorem 2 with psi = 0, whose
agreement set is {q(x + 3y) = 0}; its bound 26/125 for ranks 5 and 6 is not
attained.

*Proof of the upper bound.* (1) A totally isotropic subspace U of a
nondegenerate space of class (s, eps) has dimension at most t(s, eps),
where t = 0 if N_s(0; eps) = 1 and t(s, eps) = 1 + t(s-2, eps) otherwise.
Indeed, if U contains x != 0, then U lies in the orthogonal complement of
x, and the image of U is totally isotropic in the quotient of that
complement by the line through x, which by the Canon (zero Gram point count
in QUADRATIC-L5-INITIALIZED-CAPACITY) is nondegenerate of dimension s-2
with the same determinant character. With
N_1(0) = 1, N_2(0; -) = 1 and N_0 = 1 this gives t <= 1, 2, 1, 2, 3, 2 for
the six columns of the table, that is t <= w.

(2) Let K be a subspace of W, R the radical of q restricted to K, rho its
dimension, and K' a complement of R in K. The restriction of q to K' is
nondegenerate, of some class (d', eps'), and q(k_0 + k') = q(k') for k_0
in R, so K has 5^rho N_d'(0; eps') isotropic vectors. By the Canon's norm
counts the excess e(K) = #{k in K : q(k) = 0} - |K|/5 equals
4 eps' 5^(rho + d'/2 - 1) if d' is even and positive, 0 if d' is odd, and
4 * 5^(rho-1) if d' = 0. If e(K) > 0 with d' > 0, then eps' = +1, so K' is
isometric to the identity form of dimension d' (Canon normal form) and
contains the totally isotropic subspace spanned by the vectors
e_(2i-1) + 2 e_(2i); together with R this is a totally isotropic subspace
of dimension rho + d'/2. If d' = 0, K itself is totally isotropic of
dimension rho. By (1), e(K) <= 4 * 5^(w-1) in all cases.

(3) By Lemma 2, |Z_psi| = 5^(2r-1) + 5^r e(ker psi) <= 5^(2r-1) +
4 * 5^(r+w-1). By Lemma 3 a branch not of tangent type has at most
4 * 5^(2r-2) < 5^(2r-1) agreeing inputs (C28). QED

## 8. Upper bounds in the remaining classes

**Proposition 4.** *Status: verified by the exact verifier (C30 to C34),
exhaustively over all inputs of the reduced domain; the mechanism for ranks
5 and 6 is Lemma 4.* There are covers by tangent branches of the following
sizes, so that

```text
m* <= 25 for (4,2),    m* <= 29 for (5,1) and (5,2),    m* <= 25 for (6,1) and (6,2).
```

*Ranks 5 and 6.* The cover consists of psi = 0, which agrees on all
(x,y) with q(y) = 0, and, for several subspaces W4 ("splittings") with a
served set S of values kappa, of the maps (a D+ + b D-)^V for
(a,b) = (1,t), t in F5, and (a,b) = (0,kappa), kappa in S. By Lemma 4 with
(a_0, b_0) = (1, kappa) the six maps (1,t), (0,kappa) cover every (x,y)
with q(y) = kappa q(y_4).

- Rank 5. Let v_1, ..., v_5 be e_1, ..., e_5 for delta = 1 (sigma = 1), and
  e_1 + e_2, e_1 - e_2, e_3 + e_4, e_3 - e_4, e_5 for delta = 2 (sigma = 2,
  C = diag(1,1,1,1,2)). Splitting j, for j = 1, ..., 4, has the basis
  {v_k : k != j} in increasing order of k. The served sets are
  S_1 = {1,2,3,4}, S_2 = {3}, S_3 = {1,3}, S_4 = {3}:
  1 + 9 + 6 + 7 + 6 = 29 branches (C30, C31). This is the family with
  S_2 = {1,3} and 30 branches from which the branch (0,1) of splitting 2 has
  been removed; the exhaustive check shows that the remaining 29 cover.
- Rank 6. For delta = 1 the splittings have the bases (e_3, e_4, e_5, e_6),
  (e_1, e_2, e_5, e_6), (e_1, e_2, e_3, e_4), sigma = 1. For delta = 2
  (C = diag(1,1,1,1,1,2)) put p_1 = e_1, n_1 = e_2 + e_3, p_2 = e_4,
  n_2 = e_2 - e_3, p_3 = e_5, n_3 = e_6; splitting j has the basis
  (p_k, p_l, 2 n_k + 2 n_l, 2 n_k - 2 n_l) with {k < l} the two indices
  different from j, sigma = 1. The served sets are S_1 = S_2 = {1,2,3,4},
  S_3 = {3}: 1 + 9 + 9 + 6 = 25 branches (C32, C33).

*Rank 4 with nonsquare determinant.* For C = diag(1,1,1,2) the 25 skew maps
psi = C^(-1) K are given by the antisymmetric K whose entries
K_12 K_13 K_14 K_23 K_24 K_34 are the digits of

```text
020300 122421 333344 100340 202411 011334 211432 422003 024103 330111
301124 041410 441211 131021 110302 133400 003441 021423 423402 232043
304322 310343 444240 204204 320133
```

This list was found by a randomised greedy search; it has no structural
explanation here and no branch of it is redundant (C34).

In all five classes the verifier enumerates every y, forms for every branch
the level set of x given by Lemma 2 as a bit mask over all x, and checks
that the union is everything; section 11 lists the additional direct
evaluations. No branch of the five covers is redundant, but no minimality
is claimed for them.

## 9. Six branches of tangent type

**Proposition 5.** *Status: proved here; the plane lemma below is verified
exhaustively (C36), and the line case of the hyperplane lemma is
cross-checked (C37).* In the classes (3,1), (3,2), (4,2), (5,1), (5,2) and
(6,2) no six branches of tangent type cover W^2. Hence in these classes
every cover by six affine branches, if one exists, contains a branch that
is not of tangent type. The classes (4,1), where such a cover exists, and
(6,1) are not decided by the argument.

*Hyperplane lemma.* Let at most six affine hyperplanes of F5^N, N >= 2,
cover F5^N, and suppose that no five of them are pairwise distinct and
parallel. Then there are exactly six, they are pairwise non-parallel, and
they contain a common flat of dimension N-2.

*Proof.* Let H_1 be one of them. Some hyperplane H' parallel to H_1 is not
in the family. Members parallel to H_1 do not meet H', and every other
member meets H' in 5^(N-2) of its 5^(N-1) points. So at least five members
are not parallel to H_1; hence there are exactly six members and H_1 is the
only one in its direction. This holds for every member, so they are
pairwise non-parallel. Let m_P >= 1 be the number of members through the
point P and e_P = m_P - 1 <= 5. Then sum e_P = 6 * 5^(N-1) - 5^N = 5^(N-1),
and counting pairs, sum e_P (e_P + 1)/2 = 15 * 5^(N-2) = 3 sum e_P. Since
e (e+1)/2 <= 3e for 0 <= e <= 5 with equality only for e = 0 and e = 5,
every point lies on one member or on all six. The points on all six number
5^(N-2), the size of the intersection of two members, so all six contain
that intersection. QED

*Plane lemma (C36, exhaustive over all 12500 cases).* Let Q be a quadratic
form on F5^2, L a linear form and c != 0. If the zero set of Q + L - c meets
all six lines through the origin, then Q is nondegenerate with exactly two
isotropic lines, each isotropic line contains exactly one zero, and these
two are the only zeros n with Q(n) = 0.

*Proof of Proposition 5.* Suppose Z_psi_1, ..., Z_psi_6 cover W^2. Fix y
with c = q(y) != 0 and put n_i = psi_i y. By Lemma 2 the slice over y is
covered by the hyperplanes H_i = {x : 2 B(x, n_i) + q(n_i) = c}, one for
each i with n_i != 0. Hyperplanes with proportional normals s n,
s in {1,2,3,4}, are determined by s, so no five distinct ones are parallel.
By the hyperplane lemma all six n_i are nonzero and pairwise
non-proportional, and the H_i contain a common flat x_0 + D with
dim D = r-2. Every n_i is orthogonal to D, so the n_i lie in the
two-dimensional orthogonal complement of D and represent its six lines
through the origin. The function n -> 2 B(x_0, n) + q(n) - c on that plane
vanishes at every n_i. By the plane lemma exactly two of the n_i are
isotropic. Therefore

```text
sum over i of #{ y : q(y) != 0, q(psi_i y) = 0 } = 2 (5^r - N_r(0)).        (***)
```

Also psi_i y != 0 for every non-isotropic y, so K_i = ker psi_i consists of
isotropic vectors and is totally isotropic; let k = dim K_i. Then r - k is
even (the rank of psi_i), k <= w by step (1) of section 7, the image of
psi_i is the orthogonal complement of K_i (it is contained in it by
skewness and has the same dimension), and the radical of that complement
is K_i. By step (2) of section 7 and the quotient statement of the Canon
applied k times, the number of y with q(psi_i y) = 0 is

```text
5^k * 5^k * N_(r-2k)(0; eps) = 5^(2k) N_(r-2k)(0; eps),   eps the character of C.
```

The admissible k and the resulting values are: rank 3, k = 1, 25 N_1(0) =
25; class (4,2), k = 0, N_4(0; -) = 105; rank 5, k = 1, 25 N_3(0) = 625;
class (6,2), k = 0 or 2, N_6(0; -) = 3025 or 625 N_2(0; -) = 625. So the
left side of (***) is at most 150, 630, 3750, 18150, while the right side
is 200, 1040, 5000, 25200 (C18, C38, C39, C40). Contradiction. QED

In class (4,2) the direct enumeration of all skew psi gives at most 104
non-isotropic y with q(psi y) = 0 (C38), in agreement with the bound 105.

## 10. Fibres of size at most two

QUADRATIC-MEMORY-NATIVE-CONTACT [O] records that the data projection of a
successful binary contact has fibres of size at most two. With the six maps
of Theorem 2 as stated, 369600 of the 390625 reduced inputs agree with
exactly one branch and some output is the forced image of four of them
(C12, C13). Composing each branch with its own output isometry removes this
obstruction.

Identify W = F5^4 with the quaternions over F5 in the basis 1, i, j, k, so
that q is the norm, B(x,y) is the scalar part of x conj(y), and Li, Lj are
left multiplication by i and j (C41). Then psi_i is left multiplication by
the pure quaternion a_i = alpha_i i + beta_i j, with norm
N_i = alpha_i^2 + beta_i^2. Pure quaternions are identified with F5^3 and
carry the dot product. For a quaternion u of nonzero norm, x -> u x u^(-1)
is an isometry of q; it fixes 1 and acts on F5^3 by a rotation rho_u.

**Theorem 3 (fibres of size two).** *Status: verified by the exact verifier
by direct evaluation at all 5^8 inputs (C44, C45); also proved here through
the reduction below together with the two finite checks C42 and C43.*
Let C = I_4, let psi_1, ..., psi_6 be the maps of Theorem 2 in the order
(3,0), (0,1), (1,1), (2,3), (4,2), (4,3), and let k_i be conjugation by

```text
u_1 = 1,  u_2 = i + 2j + k,  u_3 = i + 3j + k,  u_4 = i + 4j + 2k,  u_5 = 1 + 4k,  u_6 = 1 + 2i + k,
```

that is k_i = 1 (+) rho_i with rho_1 the identity and

```text
rho_2 = [[1,4,2],[4,2,4],[2,4,1]],   rho_3 = [[1,1,2],[1,2,1],[2,1,1]],   rho_4 = [[1,3,4],[3,1,1],[4,1,2]],
rho_5 = [[0,1,0],[4,0,0],[0,0,1]],   rho_6 = [[4,3,4],[2,1,1],[4,4,3]].
```

The rho_i are written in the basis i, j, k and act on column vectors.

Consider the six linear branches, in reduced and in Canon coordinates,

```text
(x,y) -> ( k_i(x + psi_i y),  k_i y )                                        (target M0),
F_i(x,y) = ( k_i(x + 2y + psi_i(3x + 4y)),  k_i(2x + 3y + psi_i(4x + 2y)) )    (target M),
```

and the selector Phi(z) = F_i(z) for the unique i with G(F_i(z)) = M G(z),
and Phi(z) = F_1(z) if all six branches agree at z. Then
G(Phi(z)) = M G(z) for every z, and every output state has at most two
preimages under Phi: 136800 outputs have none, 117025 have one and 136800
have two (C44). The same holds on V = F5^6 for C = diag(1,1,1,1,0,0), with
all counts multiplied by 625, when every branch acts as the identity on the
radical coordinates, and for the
Canon's C = K + 0_2 after conjugating the branches by the matrix P of
section 6 (C45). By Theorem 1 no selector with fewer than six affine
alternatives exists at all, so six is also the least number of affine
alternatives of a selector with fibres of size at most two.

*Reduction to F5^3.* Work in reduced coordinates. The branches are those of
Theorem 2 composed with the isometry k_i on both cells, so the agreement
sets are unchanged: every input agrees with exactly one branch or with all
six.

(a) Slices with q(y) != 0. Write x y^(-1) = s + theta with s in F5 and
theta pure. For pure a, B(x, a y) = q(y) (theta . a), so by Lemma 2 branch
i agrees exactly when theta . a_i = (1 - N_i)/2. These are six planes of
F5^3 through the line l = {(2,0,z)}, and every theta off l lies on exactly
one of them (C42). Since (x + a_i y) y^(-1) = s + theta + a_i and
conjugation by u_i is multiplicative, branch i sends the input with
coordinates (y, s, theta) to the output with coordinates
(u_i y u_i^(-1), s, rho_i(theta + a_i)). Let tau(theta) = rho_i(theta + a_i)
with i the branch of theta, and i = 1 on l. An output (y', s, theta') has
exactly one preimage for every theta with tau(theta) = theta', namely
(k_i^(-1) y', s, theta). So the fibres of Phi over non-isotropic slices are
the fibres of the map tau of the 125 points of F5^3. They have at most two
elements: 46 points have no preimage, 33 have one, 46 have two (C42).

(b) Slices with q(y) = 0, y != 0. The pure c with c y = 0 form an
isotropic line e, and with m the pure part of x conj(y) one has
B(x, c y) = c . m for pure c, hence m . e = 0. By Lemma 2 branch i agrees
exactly when a_i . m = 0; this holds for exactly one i unless m is a
multiple of (0,0,1), when it holds for all six. The inputs with given
(e, m) form a class of 600 points, and branch i maps the class (e, m)
bijectively onto the class (rho_i e, rho_i m). So the fibre of an output in
the class (e', m') has as many elements as there are classes mapped to
(e', m') by sigma(e, m) = (rho_i e, rho_i m), i the branch of the class.
The map sigma of the 150 classes has fibres of at most two elements: 44
classes have no preimage, 62 have one, 44 have two (C43).

(c) Slice y = 0. All six branches agree, the first branch sends (x, 0) to
(x, 0), and outputs with y' = 0 arise only from y = 0.

The counts agree: 2400 * 46 + 600 * 44 = 136800 outputs with two preimages,
where 2400 is the number of pairs (y', s) with q(y') != 0. The passage to
Canon coordinates, to the radical coordinates and to C = K + 0_2 is by the
bijections of Lemma 1 and of section 6, which preserve fibre sizes. QED

The rotations rho_i were found by a computer search. No structural reason
for this particular choice is given here.

**Proposition 6 (abstract continuation).** *Status: the criterion is proved
here; its hypothesis is verified for the selector of Theorem 3 (C46).*
Let X be the data set (W^2 or V^2), let f be a map of X with
G(f(z)) = M G(z) for all z and with fibres of size at most two, and for a
Gram class g let F_m(g) be the number of data points o with G(o) = g and
exactly m preimages under f. There is a permutation T of X times {0,1} with
data projection f on the ready layer, T(z,0) = (f(z), bit), that satisfies
the readout equation on its whole reachable set if and only if there are
integers p(g) with

```text
p(M g) = p(g) + F_2(g) - F_0(M g),      0 <= p(g) <= F_0(g) + F_1(g)       for all g.
```

For every such T the numbers p(g) can be chosen so that F_2(g) + p(g) is
the number of occupied reachable states over g; the reachable set then has
|X| plus the sum of all F_2(g) + p(g) states. Here M is the Canon target
and f is a data map in Canon coordinates; the proof uses only that M
permutes the Gram classes.

On every cycle of M on the Gram classes the sums of F_0 and of F_2 are
equal, because the inputs over g are the preimages of the outputs over
M g. So the recurrence always has solutions, unique on each cycle up to an
additive constant, and the condition is that some constant satisfies the
two bounds.

For the selector of Theorem 3 such p exist. In the least solution
136800 occupied states are created on the first step and 45600 further
occupied states are passed through, so that the reachable set has
390625 + 136800 + 45600 = 573025 of the 781250 states of the carrier
W^2 times {0,1} of the nondegenerate part (C46). This is the least reachable set of any such permutation
with this data map; the minimum over all permutations in
QUADRATIC-L5-INITIALIZED-CAPACITY is 281640625 / 625 = 450625.

*Proof.* Necessity. Let T be such a permutation, R the ready layer and
Omega its reachable set. Omega is finite and T maps it into itself, so T
permutes Omega. The data point o carries as many states of T(R) as it has
preimages under f. For a class g let b(g) be the number of data points o
over g with a single preimage whose image is (o,1), and let p'(g) be the
number of occupied states of Omega over g that are not in T(R). The
occupied states of Omega over g number F_2(g) + b(g) + p'(g), and the ready
states over g outside T(R) number F_0(g) + b(g). A state of Omega outside
T(R) has its preimage among the occupied states of Omega, and by the
readout equation this preimage lies over the class mapped to g by M. Hence T
maps the occupied states of Omega over g bijectively onto the states of
Omega over M g outside T(R):
F_2(g) + b(g) + p'(g) = F_0(M g) + b(M g) + p'(M g). So p = p' + b
satisfies the recurrence, and p(g) <= F_0(g) + F_1(g) because the occupied
states counted by p(g) lie over data points with at most one preimage:
an occupied state of Omega outside T(R) cannot lie over an output with two
preimages, because the bit-1 state of that output is in T(R).

Sufficiency. Give bit 0 to the only or the first preimage of an output and
bit 1 to the second. For every class g choose p(g) occupied states over
data points with at most one preimage, and let E(g) consist of them and of
the F_2(g) states (o,1) over the outputs o with two preimages. By the
recurrence E(g) has as many elements as the set of the ready states (o',0)
over M g with o' not in the image of f together with the chosen occupied
states over M g; let T map E(g) bijectively onto that set. Then T is a
bijection of the union of R and all E(g), it respects the Gram classes
there, and this union contains the reachable set. On all other states let T
be the identity. The numbers belonging to the reachable set of this T form
a solution that is at most p everywhere, so for the least solution p the
union is the reachable set. QED

The maps on the occupied layer in this proof are matchings chosen from the
target. The maps applied there can be taken to be linear maps of tangent
type; which map is applied at which state is still given by tables derived
from the target.

For a pure quaternion a, the shear (x,y) -> (x + a y, y) is the branch of
tangent type with k = 1 and psi = left multiplication by a. It leaves
B(x,y) and q(y) unchanged and adds 2 B(x, a y) + N(a) q(y) to q(x), which
is q(y) (2 theta . a + N(a)) when q(y) != 0. On such a slice it satisfies
the Gram identity exactly at the inputs with 2 theta . a + N(a) = 1, that
is N(theta + a) = N(theta) + 1, and in the coordinates of part (a) it is
(y, s, theta) -> (y, s, theta + a). On a slice with q(y) = 0 the target M0
fixes the Gram value, so every isometry applied to both cells satisfies the
Gram identity there; this is the branch of tangent type with psi = 0.
Conjugation by u acts on the classes of part (b) by
(e, m) -> (rho_u e, rho_u m).

**Proposition 7 (a complete permutation built from linear maps).** *Status:
verified by the exact verifier, bijectivity on all 781250 states and the
readout equation at every reachable state (C47); the passage to
C = K and to V = F5^6 is proved here.* Let C = I_4. Let
Phi_0(x,y) = (k_i(x + psi_i y), k_i y) be the selector of Theorem 3 in
reduced coordinates, where i = beta(z) is the unique branch that agrees at
z = (x,y), and beta(z) = 1 where all six agree. In reduced coordinates
define T on W^2 times {0,1} as follows.

- Ready layer: T(z,0) = (Phi_0(z), b), with b = 1 if Phi_0(z') = Phi_0(z) for
  some z' with beta(z') < beta(z), and b = 0 otherwise.
- Occupied layer, q(y) != 0: if theta, the pure part of x y^(-1), has an
  entry theta:a in the first table below, then
  T((x,y),1) = ((x + a y, y), b).
- Occupied layer, q(y) = 0 and y != 0: if the class (e, m) of (x,y) has an
  entry em:n in the second table, then
  T((x,y),1) = ((u x u^(-1), u y u^(-1)), b) with u = w_n, where
  w_0 = 1 + i + j and w_1 = 1 + i + j + 4k.
- In the shear case b = 0 if the new data point is not a value of Phi_0
  and no occupied state with a lexicographically smaller shear vector a is
  sent to the same data point; otherwise b = 1. In the conjugation case
  b = 0.
- T is the identity on all other states.

Vectors of F5^3 are written as three digits, the coefficients of i, j, k.
The line e is given by its vector whose first nonzero coordinate is 1; m is
not normalised.

```text
first table, theta:a (70 entries, 13 different a)
001:103 002:433 003:201 004:324 011:433 012:304 013:111 014:130 021:421
022:111 023:311 024:402 030:324 031:111 032:304 033:201 034:433 041:311
042:421 043:301 044:402 101:201 104:103 110:301 111:201 112:111 114:324
122:031 134:311 140:130 141:130 144:130 200:402 202:421 203:031 213:002
214:201 220:130 222:031 223:421 230:402 232:103 233:433 234:111 301:304
302:130 303:433 310:311 320:103 321:304 322:031 323:402 330:433 332:421
333:402 340:421 343:002 400:433 401:402 403:031 410:031 411:301 414:304
420:421 430:311 431:301 434:031 440:201 441:301 443:002

second table, em:n (44 entries)
012012:0 012024:0 012031:0 012043:0 013013:0 013021:0 013034:0 013042:0
013121:1 013134:1 013142:0 013213:1 013234:0 013242:1 013313:1 013321:0
013342:1 013413:0 013421:1 013434:1 102132:0 102142:0 102214:0 102234:0
102321:0 102341:0 102413:0 102423:0 120121:1 120242:1 120313:1 120434:1
130130:0 130132:0 130134:1 130210:0 130213:1 130214:0 130340:0 130341:0
130342:1 130420:0 130421:1 130423:0
```

The first table lists the 46 points with two preimages under tau together
with 24 further points. The second lists the 44 classes with two
preimages under sigma, and its conjugations map them bijectively onto the
44 classes with none.

Let T_M be T in Canon coordinates: (g_in x 1)^(-1) is applied to the data
before T and (g_out x 1)^(-1) after it, on both layers. Lemma 1(b) carries
over one step, not the iteration: between two consecutive steps of T_M the
reduced data are changed by (g_in x 1)^(-1) (g_out x 1)^(-1), which is
(x,y) -> (2x + y, 2y). It fixes theta and e and replaces m by -m, and the
set of classes in the second table is invariant under it. All statements
below are therefore checked for T_M itself. T and T_M are permutations of
the carrier. The reachable set of the ready layer under
T_M consists of the ready layer and of the occupied states whose data fall
under the two tables after (g_in x 1)^(-1) has been applied. T_M maps this
set bijectively to itself, and G(pi T_M(s)) = M G(pi s) for every reachable
state s, where pi is the data projection. Of the 781250 states, 585025
are reachable and 194400 of these are occupied. On the reachable set T_M
has 4021 cycles, the longest of length 500 (C47).

On the ready layer T_M selects among the six linear maps F_i of Theorem 3.
On its reachable occupied states it selects among the 13 linear maps

```text
(x,y) -> ( x + 2y + a(3x + 4y),  2x + 3y + a(4x + 2y) ),
```

one for each a of the first table, and the two linear maps
(x,y) -> (u(x + 2y)u^(-1), u(2x + 3y)u^(-1)); theta and the class are those
of the pair (2x + 3y, 4x + 2y). These 21 maps correspond under
Lemma 1(b) to branches of tangent type. The occupied states outside the
two tables are exactly the unreachable ones; there the identity of T
becomes the linear map (x,y) -> (x + 2y, 2x + 3y) in Canon coordinates, and
the readout equation is neither required nor satisfied in general.

For C = K the conjugate of T_M by P, with P acting on both cells, has the
same properties and the same cycle structure, because
G_K(Px, Py) = G_I(x, y). On V = F5^6, for C = diag(1,1,1,1,0,0) and for
C = K + 0_2, the product of the permutation with the identity on the four
radical coordinates has the same properties; its reachable set has
625 * 585025 = 365640625 states.

The two tables were found by a computer search, the first one with an
integer programming solver as a search aid. Only the exact verification
C47 is claimed for them. Neither the number of occupied-layer alternatives
nor the size of the reachable set is claimed to be least possible; by
Proposition 6 no such permutation with the data map of Theorem 3 has a
reachable set below 573025.

## 11. The verifier

`python3 verify.py` uses only the Python standard library and exact
integer arithmetic modulo 5. It is deterministic, writes no file, prints
one line per check and exits with status 1 if a check fails. Its output
must equal [`EXPECTED.txt`](EXPECTED.txt) byte for byte
(`python3 verify.py | cmp - EXPECTED.txt`). On current hardware it runs in
well under a minute on one core.

Exhaustive checks: the marked-reading and reduction identities (C01 to
C04); the structure of Li, Lj, D+, D- and of the six pairs (C06 to C09);
the six-branch cover in Canon coordinates on all 5^8 inputs of the
nondegenerate part, for C = I_4 and for the Canon's K, by direct evaluation
of G(f(z)) and M G(z) at every z, together with the statement that no five
of the six cover (C10, C11, C16); the agreement multiplicities and the
forced fibres (C12, C13); the constants of Theorem 1 (C18 to C21); the
slice counts and the size formula of Lemma 2 for all 15625 skew psi of
rank 4, both classes (C22 to C25); the maxima of Proposition 3 (C23, C25
to C28); the covers of Proposition 4 over all 5^8, 5^10 and 5^12 inputs
(C30 to C35); the finite lemmas and counts of Proposition 5 (C36 to C40);
the isometries, the two finite models and the selector of Theorem 3 on all
5^8 inputs, for C = I_4 and for the Canon's K (C41 to C45); the flow of
Proposition 6 (C46); the permutation of Proposition 7 on all 781250 states
of the carrier of the nondegenerate part, in Canon coordinates and for the
target M, by
direct evaluation of every reachable step (C47).

Sanity checks that are not proofs: Lemma A in small cases (C05) and
Lemma 3 on 13 explicit branches (C17). Lemma 3, Theorem 1 and the upper
bound of Proposition 3 rest on the proofs above, not on the verifier.

The covers of Proposition 4 are checked through the slice description of
Lemma 2: for a tangent branch and fixed y the agreeing x form the level set
{x : B(x, psi y) = 3 (q(y) - q(psi y))} of one linear form, or everything,
or nothing. The verifier builds these level sets as bit masks over all x
from direct dot products and takes their union for every y. Independently
of this description, the cover for rank 4 with nonsquare determinant is
evaluated directly at all 5^8 inputs (C34), and for ranks 5 and 6 the three
Gram conditions are evaluated directly at every x of 25, respectively 12,
slices chosen by a fixed rule (C30 to C33). The six-branch cover of
Theorem 2 is checked without any reduction (C10, C16) and once more with
the level sets (C35).

This verifier is a local audit. It is not a formal evidence directory, a
preregistration or a probe.

## 12. Falsifiers and boundary

- Theorem 1 is refuted by five explicit affine maps of F5^12 whose
  agreement sets cover the ready layer for some C of rank 3 to 6. Its proof
  is refuted by an affine branch that is not of tangent type and agrees on
  more than 4 * 5^(2r-2) reduced inputs (Lemma 3), or by a polynomial
  violating Lemma A.
- Theorem 2 is refuted by a ready input, for some C of rank 4 with square
  determinant, at which none of the six stated branches satisfies
  G(f(z)) = M G(z); for C = I_4 and C = K the verifier would report it.
- Proposition 3 is refuted by an affine branch with a larger agreement set.
- Proposition 4 is refuted by an input not covered by the listed branches.
- Proposition 5 is refuted by six branches of tangent type covering W^2 in
  one of the six named classes.
- Theorem 3 is refuted by a ready input at which the selected branch
  violates the Gram identity, or by an output state with three preimages;
  the verifier would report either (C44, C45).
- Proposition 6 is refuted by a permutation extending a data map whose flow
  conditions (recurrence and bounds) have no solution, or by a solvable flow without an extension.
- Proposition 7 is refuted by a reachable state at which the stated map
  violates the Gram identity, or by two reachable states with the same
  image; the verifier would report either (C47).

Boundary. The covering number concerns one property only: at every ready
input some alternative satisfies the Gram identity for one initialized
step. It says nothing about reversibility, about writing the ignored
register, about occupied-memory continuation or about native admissibility
of the alternatives or of the selection rule.

The six maps of Theorem 2 as stated, with the identity as output isometry
on every branch, are not the data projection of a binary contact: for
C = I_4, 369600 of the 390625 reduced ready inputs agree with exactly one of
the six branches, so their outputs are forced, and 12000 output states are
the forced image of four inputs each (C12, C13). With the output isometries
of Theorem 3 the same six psi_i give a selector whose data map has fibres
of size at most two, and by Proposition 6 this data map extends to a
complete permutation of the carrier that satisfies the readout equation on
its reachable set. By Proposition 7 the permutation can be chosen so that
both bit layers select among finitely many linear maps of tangent type,
with the choice on the occupied layer given by tables derived from the
target.

For QUADRATIC-MEMORY-NATIVE-CONTACT [O] this gives the following and no
more. The three necessary properties of the data projection named there,
non-affinity, fibres of size at most two and failure of injectivity, are
met by a ready-layer map that selects among six linear maps. For C = I_4,
for C = K and for their extensions by a radical there is an explicit
permutation of the carrier that satisfies the readout equation on its
whole reachable set, occupied-memory continuation included, and that
selects among six linear maps on the ready layer and among 15 linear
maps on its reachable occupied states (Proposition 7).

Not addressed are: the independent admission of C and of the reading; the
native admissibility of the linear maps; the selection rules, which
evaluate the Gram identity of each branch on the ready layer and look up
theta or the class (e, m) in a table on the occupied layer; and the bit
writes, which depend on which other state is sent to the same data point.
The two tables of Proposition 7 were obtained from the target by search.
They are fibre matchings of a reduced model, and that item does not accept
target-derived fibre matchings as native primitives. No gate alphabet is
declared and no admitted permutation is supplied. The item stays open.

The result sharpens only the bounded affine-alternative class of
QUADRATIC-L5-NATIVE-OBSTRUCTIONS and of the note in pull request #2063: for
rank at least three the number of excluded alternatives rises from two
(Canon) and four (that note, for rank at least four) to five, and for rank
four with square determinant five is the exact threshold. These are
analytical statements conditional on the marked reader and on C. They do
not select C, admit a gate alphabet or supply a native realization.

## 13. Open

- The exact value of m* for the classes (4,2), (5,1), (5,2), (6,1), (6,2),
  where 6 <= m* <= 25, 29, 29, 25, 25, and for rank 3, where
  6 <= m* <= 125.
- Whether any of these classes admits a cover by six affine branches. By
  Proposition 5 such a cover would need a branch that is not of tangent
  type, except possibly in class (6,1).
- A sharp bound for branches that are not of tangent type. The largest
  agreement set found for such a branch is far below the bound of Lemma 3.
- The least number of affine alternatives on the occupied layer of a
  complete permutation whose ready layer is a six-branch selector. For the
  data map of Theorem 3 it lies between 3 and 15: the upper bound is
  Proposition 7, and at least 182400 occupied data points must be served
  while one affine branch agrees on at most 90625 inputs (Proposition 3).
- Whether the selection rule and the bit rule on the occupied layer can be
  given by formulas instead of the tables of Proposition 7.
- Whether a six-branch selector with fibres of size at most two can reach
  the minimal reachable set of QUADRATIC-L5-INITIALIZED-CAPACITY, which has
  450625 reduced states. The selector of Theorem 3 needs at least 573025,
  and the permutation of Proposition 7 uses 585025.
- Whether, for rank four with square determinant, a cover by six affine
  branches can contain a branch that is not of tangent type.
