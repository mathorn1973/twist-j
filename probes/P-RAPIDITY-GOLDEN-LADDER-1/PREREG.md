# P-RAPIDITY-GOLDEN-LADDER-1 preregistration

Status: **FORMAL PUBLIC PROBE PREREGISTRATION / PROOF-FIRST / UNRUN / CANON UNCHANGED**

Date: 2026-09-03.

This probe freezes one exact package of L1 arithmetic and exact `Z[phi]` algebra about the diagonal evaluations of the registered integral rapidity lift. It proves that integrality forces the evaluation points onto the golden unit ladder `t = +-phi^(2k)`, identifies the three anchors of that ladder with registered or merged objects, decomposes every squarefree-restricted ladder sum into split-count layers with an exact finite inversion, and computes the exact connecting units between the full-lift ladder and the shell ladder.

It does not construct a continuation, locate a zero or pole, prove any summatory estimate, or prove or disprove RH or GRH. `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` is untouched.

## Public identity, authority, and action layer

```text
probe:             P-RAPIDITY-GOLDEN-LADDER-1
public claim lock: issue #791
owner:             A. M. Thorn / delegated session 2026-09-03
branch:            probe/P-RAPIDITY-GOLDEN-LADDER-1
path:              probes/P-RAPIDITY-GOLDEN-LADDER-1/
basis main:        4f08791bd5401ee1616270661f7788d743f5fc26
canon:             Public Canon v75, tag canon-v75
TAG_OBJECT:        5a1508f52df2a4481468675d5fe9208404d9472b
TAG_TARGET:        c4f00e1d9c89f503d913224dc3c09dc760dcec9d
CONTENT_COMMIT:    e32e85ed7297d4320df5b345e4488d78323d550c
CANON_SHA256:      44130160a3ce29bfcdc757e255d2d1c25a010b22911edfe66cf6b132be081fbe
CANON_BYTES:       399513
action layer:      NOT_APPLICABLE, exact L1 arithmetic / Z[phi] algebra / Dirichlet-coefficient algebra
layer lift:        none
authority:         none until a later sealed Canon fold
```

The public issue was opened after a collision search across open and closed issues, pull requests, the remote branch list (`git ls-remote --heads origin`), the `probes/` tree, the Public Canon v75 tree, Registry, Frontier, dependencies, gates, evidence, current Notes, and the current rapidity/O5 lanes.

## Origin and predecessor disclosure

This probe is grown from the merged NON-CANONICAL draft `notes/C-RAPIDITY-GOLDEN-LADDER-1/` (Notes PR #595, merged into `main` at the basis commit above). The draft exposed the theorem package, a draft verifier, and its archived non-formal stdout, including the frozen integer readouts repeated in section 9. That draft run created no status and carries no evidence here. Every statement is re-frozen and re-proved in this preregistration, and the accepted verifier is a fresh file under this probe's own pin.

The abandoned pin `P-O5-DEDEKIND-GRH-READ-1` (`Status: ABANDONED`, interpreter stderr injected before verifier startup) is not a predecessor of this lane. Its failure mode is the reason this probe freezes the clean-interpreter startup preflight of `P-O5-SQUAREFREE-CORE-1` before its own pin.

## Collision and ownership boundary

No existing object owns `P-RAPIDITY-GOLDEN-LADDER-1` or `RAPIDITY-GOLDEN-LADDER`. Adjacent work is explicitly separate:

- `J-IDEAL-RAPIDITY-CHARACTER-LIFT [T]` is the public source theorem for the integral rapidity lift `bold_mu` and its local factors. It is consumed as a registered input, not re-proved.
- `ARITHMETIC-RAPIDITY-DECOMPOSITION [T]` registers the unit lattice `O_F^x/{+-1} = <phi>` with `N(phi^n) = (-1)^n` and the Pell alternator `L_n^2 - 5F_n^2 = 4(-1)^n`; `SPLIT-PRIME-RAPIDITY-CLASS [T]` registers the unordered orientation pairs above split primes. Both are consumed as registered inputs.
- `J-RAPIDITY-TERNARY-SHELL-CENSUS [T]` registers `bold_mu(n) = (-1)^b prod_(p split, p|n) (1 - X_p - X_p^-1)` on squarefree `n`. The `tau = -2` anchor below is its diagonal evaluation and adds nothing to that row.
- `J-IDEAL-COUNT-QUADRATIC-CHARACTER [T]` owns `a_F = 1 * chi_5` for `F = Q(sqrt5)`.
- merged `P-O5-SQUAREFREE-CORE-1` (candidate row `O5-SQUAREFREE-CORE`, no Canon status) owns the squarefree core `s_5 = mu a_F 1_((n,5)=1)` and the two-sided `theta > 1/3` summatory transfer to `O_5`. This probe re-derives only the coefficient identity `sigma_3 = s_5` and consumes no transfer statement and no evidence from that lane.
- merged `P-O5-GOLDEN-AXIS-BAND-1` (#611) owns the golden cutoff axis `X_k = L_2k - 1 = floor(phi^(2k))`, the shell partition, and the finite-band theorems for `Q_11`; merged `P-O5-GOLDEN-PROFILE-TRANSFER-1` owns the cutoff/profile state. Neither owns the diagonal *evaluation* ladder `tau = +-L_2k`, which is the object here. This probe re-derives every Lucas fact it uses and consumes no evidence from those lanes.
- merged `P-O5-DEDEKIND-GRH-DIVISOR-READ-1` and the merged or abandoned first-shell, first-missing-shell, Walsh-link, Euler-incidence, orientation-character, and oriented-Euler-Morse lanes remain separate and are not evidence inputs.
- `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` is untouched. Its growing-mode clause is named once in section 6 as the [H] frame this lane may later serve; no statement here is offered against that row.

## Proposed candidate row

At most the following row may be offered to a later sealed fold:

```text
RAPIDITY-GOLDEN-LADDER [candidate-T]

Let bold_mu be the registered integral rapidity lift for F = Q(sqrt5)
and, for a unit t of a commutative ring, let ev_t send every split
rapidity variable X_p to t. Put tau = t + t^-1. Then:

A. ev_t(bold_mu(n)) depends on t only through tau, is unchanged under
   t -> t^-1, and equals the multiplicative function m_tau with
       split p:      m_tau(p) = 1 - tau,  m_tau(p^e) = 2 - tau  (e >= 2),
       non-split p:  m_tau(p) = -1,       m_tau(p^e) = 0        (e >= 2).
   No split orientation is selected by any diagonal evaluation.

B. For t in F^x, every m_tau(n) lies in Z iff t = +-phi^(2k) for some
   k in Z, i.e. iff tau = +-L_2k. The integers m >= 0 with
   m^2 - 5 b^2 = 4 solvable in Z are exactly the even-index Lucas
   numbers L_2k.

C. m_2 = mu identically. On squarefree n with a split and b non-split
   prime factors, m_(-2)(n) = (-1)^b 3^a. With sigma_tau(n) =
   (1-tau)^omega(n) on squarefree pure-split n and 0 otherwise,
   sigma_3(n) = mu(n) a_F(n) 1_((n,5)=1) for every n >= 1.
   m_tau is supported on squarefree integers iff tau = 2.

D. With B_a(x) = sum over squarefree n <= x with exactly a split
   prime factors of (-1)^b(n), for every tau,
       sum_(n<=x) mu^2(n) m_tau(n) = sum_(a>=0) (1-tau)^a B_a(x),
   a finite sum with a <= log x / log 11. The nodes 1 - tau at
   distinct rungs are distinct integers, so the ladder sums at any
   A(x)+1 distinct rungs determine B_0(x), ..., B_A(x) exactly by
   Vandermonde inversion over Q.

E. m_tau = sigma_tau * w_tau (Dirichlet convolution), where w_tau is
   multiplicative with non-split local factor 1 - T and split local
   factor ((1 - tau T + T^2)/(1 - T)) / (1 + (1 - tau) T), whose
   coefficient of T^e is 1 - (tau - 1)^(e-1) for e >= 1. At tau = 2
   the split factor is 1.

No continuation, zero, cancellation, RH, GRH, Hecke, physical, or
L1-L6 claim is included.
```

No status is earned by this preregistration. The written proofs below are the proposed theorem-grade evidence. The verifier is a bounded exact audit of the frozen algebra and negative controls.

## Falsifier first

One exact counterexample to any frozen universal statement below falsifies the corresponding candidate theorem:

1. one value `ev_t(bold_mu(n))` depends on `t` beyond `tau`, changes under `t -> t^-1`, or the local table of A fails at one prime power;
2. some `t` in `F^x` outside `+-phi^(2k)` makes every `m_tau(n)` an integer, or some `+-phi^(2k)` gives a non-integer value;
3. one integer `0 <= m <= 322` with `m^2 - 5b^2 = 4` solvable lies outside `{2, 3, 7, 18, 47, 123, 322}`, or one of these seven admits no solution;
4. one anchor identity of C fails at one positive integer;
5. a squarefree-supported rung with `tau != 2` exists;
6. the layer identity of D fails at one `(tau, x)`, or the Vandermonde system at four distinct rungs fails to recover the layers at `x = 20000`;
7. the connecting-unit identity of E, or the closed form `1 - (tau-1)^(e-1)`, fails at one coefficient;
8. the proof imports a zeta-zero statement, RH/GRH, an equivalent Mertens estimate, a Hecke or automorphic object, a selected split orientation, or any target bound of the bridge row.

A changed pinned byte, stale basis, failed startup preflight, nonzero verifier exit, nonempty stderr, stdout mismatch, architecture disagreement, post-pin threshold change, or out-of-scope claim is STOP, not a mathematical counterexample.

## The six frozen fields

```text
EQUATION
  Statements A-E exactly as displayed, carried by the written proofs
  of sections 2-6 below.

CODE
  probes/P-RAPIDITY-GOLDEN-LADDER-1/verify.py.
  Python standard library only; exact integers; exact Z[phi] pairs;
  exact Fractions; deterministic stdout; no float, complex
  approximation, special function, network, random input, zero table,
  analytic input, or external package.

CARRIER
  F = Q(sqrt5), chi_5, the registered integral rapidity lift and its
  local factors, diagonal unit evaluations, Lucas and Fibonacci
  integers, the registered ideal-count sequence a_F, the squarefree
  split-count layers B_a(x), formal power series over Z[phi], and
  exact rational linear algebra.

SYSTEMATICS
  Split means chi_5(p) = 1; non-split means inert or p = 5. The two
  prime ideals above a split rational prime remain an unordered
  orientation pair; star symmetry makes every diagonal evaluation
  orientation-free. k indexes the registered rapidity lattice. The
  ladder is forced by integrality, not chosen. The merged core s_5
  and the golden cutoff axis of adjacent lanes are not evidence
  inputs.

THRESHOLD
  G01 through G11 must pass exactly. B1 through B5 must fire at their
  frozen witnesses. Stdout must equal one committed LF EXPECTED.txt
  byte for byte; exit zero and empty stderr are required on x86_64
  and aarch64.

LAYER
  NOT_APPLICABLE. Exact L1 arithmetic and Z[phi] algebra. No state,
  manifold, boundary, support, stream, measure, decoder, observable,
  probability, physical dictionary, SI bridge, or L1-L6 lift.
```

## 1. Frozen public inputs

Throughout, `F = Q(sqrt5)`, `O_F = Z[phi]`, `phi^2 = phi + 1`, `psi = 1 - phi = -phi^-1` is the conjugate of `phi`, and `chi_5` is the quadratic character mod 5. A rational prime is split if `chi_5(p) = 1` and non-split otherwise (inert, or the ramified `p = 5`). The smallest split prime is `11`.

Public Canon v75 registers `J-IDEAL-RAPIDITY-CHARACTER-LIFT [T]`: the integral rapidity lift `bold_mu` is the multiplicative function with values in the Laurent polynomial ring over `Z` in the split rapidity variables `X_p`, whose local factor is

\[
\frac{(1-X_pT)(1-X_p^{-1}T)}{1-T}
\qquad\text{at split }p,
\qquad
1-T
\qquad\text{at non-split }p,
\]

with prime-power values `bold_mu(p) = 1 - X_p - X_p^-1` and `bold_mu(p^k) = 2 - X_p - X_p^-1` for `k >= 2` at split `p`, and `aug(bold_mu(n)) = mu(n)` under `X_p -> 1`. Exchanging the two prime ideals above `p` exchanges `X_p` and `X_p^-1`.

Public Canon v75 registers `ARITHMETIC-RAPIDITY-DECOMPOSITION [T]`: `O_F^x/{+-1} = <phi>`, `N(phi^n) = (-1)^n`, and `L_n^2 - 5F_n^2 = 4(-1)^n`, where `L_n = phi^n + psi^n` and `F_n = (phi^n - psi^n)/sqrt5` are the Lucas and Fibonacci integers. `SPLIT-PRIME-RAPIDITY-CLASS [T]` registers the unordered pair of prime ideals above a split prime.

Public Canon v75 registers `J-RAPIDITY-TERNARY-SHELL-CENSUS [T]`: for squarefree `n` with `a` split and `b` non-split prime divisors, `bold_mu(n) = (-1)^b prod_(p split, p|n) (1 - X_p - X_p^-1)`.

Public Canon v75 registers `J-IDEAL-COUNT-QUADRATIC-CHARACTER [T]`: `a_F = 1 * chi_5`, so that `a_F(p^e) = e + 1` at split `p`, `a_F(p^e) = 1` at inert `p` with `e` even and `0` with `e` odd, and `a_F(5^e) = 1`.

Elementary Lucas facts used below, proved here rather than imported: from `phi + psi = 1`, `phi psi = -1`, one has `phi^n = (L_n + F_n sqrt5)/2` (Binet); the even powers `x = phi^2` and `y = psi^2 = phi^-2` satisfy `x + y = 3` and `xy = 1`, hence

\[
L_{2(k+1)} = 3L_{2k} - L_{2k-2},
\qquad L_0 = 2,\ L_2 = 3,
\]

so the even-index Lucas values are `2, 3, 7, 18, 47, 123, 322, ...`; and `L_{-2k} = L_{2k}`. Gate G01 audits the recurrence against the exact `Z[phi]` power route through `k = 6`.

No statement from any O5 probe, from the bridge row, or from analytic number theory below `Re(s) = 1` is used anywhere in the proofs.

## 2. The diagonal evaluation family (proof of A)

Let `t` be a unit of a commutative ring `R` and let `ev_t` be the ring homomorphism sending every `X_p` to `t`. The split local factor of the lift is

\[
\frac{(1-X_pT)(1-X_p^{-1}T)}{1-T}
=
\frac{1-(X_p+X_p^{-1})T+T^2}{1-T},
\]

which depends on `X_p` only through `X_p + X_p^-1` and is symmetric under `X_p -> X_p^-1`. Its image under `ev_t` is

\[
\frac{1-\tau T+T^2}{1-T},
\qquad \tau = t + t^{-1},
\]

and multiplying `1 - tau T + T^2` by `sum_(j>=0) T^j` gives the coefficients

\[
1,\quad 1-\tau,\quad 2-\tau,\quad 2-\tau,\ \dots
\]

The non-split local factor `1 - T` has coefficients `1, -1, 0, 0, ...`. Since `bold_mu` is multiplicative with these local factors, `ev_t(bold_mu(n))` is the multiplicative function `m_tau(n)` with the local table of A, and every value is a polynomial in `tau` with integer coefficients. It is therefore unchanged under `t -> t^-1`, which fixes `tau`.

Exchanging the two prime ideals above a split `p` exchanges `X_p` and `X_p^-1`; under `ev_t` both go to `t` and `t^-1` in the symmetric pair, so the evaluation is the same function of the unordered pair. No diagonal evaluation selects an orientation. Gate G02 audits the local table by exact `Z[phi]` series division at `tau = +-L_2k`, `k <= 4`, from the units `t = +-phi^(2k)` themselves.

## 3. Integrality selection (proof of B)

Let `t` lie in `F^x`. If every `m_tau(n)` is an integer, then `m_tau(11) = 1 - tau` is an integer, so `tau = t + t^-1` lies in `Z`. Conversely if `tau` lies in `Z`, every local value `1 - tau`, `2 - tau`, `-1`, `0` is an integer, and so is every product. Thus integrality of the whole ladder value is equivalent to `tau` in `Z`.

Now `t` is a root of `X^2 - tau X + 1`. If `t` is rational, then it is a rational root of a monic polynomial with integer coefficients and constant term `1`, hence `t = +-1 = +-phi^0`. Otherwise `X^2 - tau X + 1` is the minimal polynomial of `t` over `Q`, so `t` is an algebraic integer of `F` with `N(t) = 1`; it is a unit of `O_F`, hence `t = +-phi^m` by the registered unit lattice, and `N(phi^m) = (-1)^m` forces `m = 2k` even. Conversely `t = +-phi^(2k)` has `t^-1 = +-phi^(-2k) = +-psi^(2k)`, so `tau = +-(phi^(2k) + psi^(2k)) = +-L_2k`, an integer. This proves the first sentence of B.

For the second sentence let `m >= 0` and `b` be integers with `m^2 - 5b^2 = 4`. Then `m^2 = b^2 (mod 4)` because `5 = 1 (mod 4)`, so `m` and `b` have the same parity and `u = (m + b sqrt5)/2` lies in `O_F`, with `N(u) = (m^2 - 5b^2)/4 = 1`. Hence `u` is a unit of norm `1`, so `u = +-phi^(2k)`, and the trace of `u` is `m = +-L_2k`; since `m >= 0` and `L_2k > 0`, `m = L_2k`. Conversely `m = L_2k`, `b = F_2k` solve the equation by the registered Pell alternator at even index. This proves B.

The admissible rungs are therefore exactly `tau in {L_2k} union {-L_2k}`, and the ladder is selected by the house unit group. The rung `k` sits at the lattice point `2k log phi` of the registered rapidity lattice, and `phi^(2k)` and `phi^(-2k)` are the same rung. Gate G01 enumerates the Pell solutions through `m = 322`; breaker B3 checks that the odd unit powers `phi` and `phi^3` give `tau` with nonzero `phi`-component (`tau = 2phi - 1 = sqrt5` and `tau = 4phi - 2 = 2sqrt5`), and breaker B4 checks the near-misses `m = 4, 8`.

## 4. Anchors and uniqueness (proof of C)

At `tau = 2`, the local table reads `1 - 2 = -1` at split `p`, `2 - 2 = 0` at split `p^e` with `e >= 2`, and `-1`, `0` at non-split prime powers: exactly the local table of `mu`. Hence `m_2 = mu` identically. This is the registered augmentation `X_p -> 1` read through the family, since `t = 1` gives `tau = 2`.

At `tau = -2`, the split value is `1 - (-2) = 3`, so on squarefree `n` with `a` split and `b` non-split prime factors `m_(-2)(n) = (-1)^b 3^a`. This is the diagonal evaluation `X_p -> -1` of the registered census `bold_mu(n) = (-1)^b prod (1 - X_p - X_p^-1)`, because `1 - (-1) - (-1) = 3`.

For the shell rung, `sigma_3(n) = (1 - 3)^omega(n) = (-2)^omega(n)` on squarefree pure-split `n` and `0` otherwise. On the other side, `mu` kills every exponent `e >= 2`, and on squarefree input the registered values give `mu(p) a_F(p) = -2` at split `p`, `mu(p) a_F(p) = 0` at inert `p`, and `mu(5) a_F(5) = -1` at the ramified prime, which the indicator `1_((n,5)=1)` removes. Hence `mu(n) a_F(n) 1_((n,5)=1)` equals `(-2)^omega(n)` exactly on squarefree pure-split `n` and `0` otherwise, which is `sigma_3(n)`. This is a coefficient identity for every positive integer; no summatory statement about `s_5` is used or made.

Finally `m_tau(p^2) = 2 - tau` at every split `p`, and split primes exist (`11`), so `m_tau` is supported on squarefree integers if and only if `tau = 2`. The `mu` rung is the unique squarefree-supported rung of the full-lift ladder; every other rung carries a split prime-power tail with constant coefficient `2 - tau != 0`. This proves C.

A closed-form remark, exact and elementary: with `t = phi^(2k)` the split local factor is `(1 - L_2k T + T^2)/(1 - T)`, a constant integer pair `(phi^(2k), phi^(-2k))` at every split prime. For `k >= 1` this pair is not unitary. No Hecke, automorphic, or spectral identification of any rung is claimed, and `L_2k = D_k(3)` is the Dickson orbit of `L_2 = 3`, elementary algebra rather than automorphy.

## 5. Layer decomposition and finite inversion (proof of D)

For squarefree `n` with `a(n)` split and `b(n)` non-split prime factors, the local table gives `m_tau(n) = (1-tau)^a(n) (-1)^b(n)`. Grouping the squarefree `n <= x` by `a(n)` yields

\[
\sum_{n\le x}\mu^2(n)\,m_\tau(n)
=
\sum_{a\ge0}(1-\tau)^a B_a(x),
\qquad
B_a(x)=\sum_{\substack{n\le x\ \text{squarefree}\\ a(n)=a}}(-1)^{b(n)}.
\]

The sum is finite because a squarefree `n <= x` with `a` distinct split prime factors satisfies `11^a <= n <= x`, so `a <= log x / log 11`. At `tau = 2` the identity reads `sum_a (-1)^a B_a(x) = M(x)`, the Mertens function.

Let `A = A(x)` be the largest value of `a(n)` over squarefree `n <= x`, so that the sum runs over `0 <= a <= A`, and let `tau_0, ..., tau_A` be distinct admissible rungs. The nodes `z_i = 1 - tau_i` are distinct integers, so the Vandermonde matrix `(z_i^a)` has determinant `prod_(i<j)(z_j - z_i) != 0` and is invertible over `Q`. Hence the `A + 1` ladder sums at those rungs determine `B_0(x), ..., B_A(x)` exactly, and conversely. This proves D. Gate G06 audits the identity at the frozen checkpoints for `tau in {2, 3, 7, 18, -2, -3}`, and gate G07 performs the exact inversion at `x = 20000`, where `A = 3` (`11 * 19 * 29 = 6061 <= 20000 < 11 * 19 * 29 * 31`), from the rungs `tau = 2, 3, 7, 18` with nodes `-1, -2, -6, -17`. Breaker B5 checks that a repeated node makes the system singular.

The inverse Vandermonde constants grow with `A(x)`. No uniformity in `x` and no analytic statement about any layer is made; the equivalence is finite linear algebra at each fixed `x`.

## 6. Connecting units (proof of E) and the fenced boundary

Both `m_tau` and `sigma_tau` are multiplicative, with split local series `M_p(T) = (1 - tau T + T^2)/(1 - T)` and `S_p(T) = 1 + (1 - tau)T`, and non-split local series `1 - T` and `1`. Define `w_tau` as the multiplicative function with local series `M_p/S_p` at split `p` and `1 - T` at non-split `p`. Then `m_tau = sigma_tau * w_tau` holds coefficientwise, because at every prime power the identity `M_p = S_p (M_p/S_p)` is the local form of the Dirichlet convolution and multiplicativity assembles the local identities. No convergence is needed: this is an identity of formal Dirichlet series over `Z`.

For the closed form put `u = tau - 1`, so `S_p = 1 - uT` and `1/S_p = sum_(j>=0) u^j T^j`, while `M_p = 1 - uT + (1 - u)(T^2 + T^3 + ...)`. The coefficient of `T^e` in `M_p/S_p` for `e >= 1` is

\[
u^e - u\cdot u^{e-1} + (1-u)\sum_{j=0}^{e-2}u^j
=
(1-u)\sum_{j=0}^{e-2}u^j
=
1-u^{e-1},
\]

where the last step is the telescoping identity `(1-u)(1 + u + ... + u^(e-2)) = 1 - u^(e-1)`, valid for every integer `u` including `u = 1`. Hence the split coefficients of `w_tau` are `1 - (tau-1)^(e-1)`: `0` at `T`, `2 - tau` at `T^2`, `tau(2 - tau)` at `T^3`, and so on. At `tau = 2` every split coefficient beyond the constant term vanishes, so the split factor is `1` and `m_2 = sigma_2 * (non-split Mobius factor)` is the trivial split/non-split factorization of `mu`. This proves E. Gate G08 audits the closed form through degree `8` and the convolution identity through `n = 100000` at `tau = 2` and `tau = 3`.

### Fenced boundary (not part of the row; not gated)

Two readings are recorded so that the ladder is not quoted past them. They use two classical prime-density facts, labeled [T-lit] and imported only here: the sum of `p^-s` over the inert primes, and over the split primes, diverges for real `s <= 1` (Dirichlet density `1/2` for each class, from `L(1, chi_5) != 0`).

1. The split part of `w_tau` deviates from `1` first at `T^2`, with coefficient `2 - tau`; for the rungs `tau = L_2k` with `k >= 2` the local split coefficient series converges absolutely at `p^-s` only when `(tau - 1) p^-s < 1`, so at `p = 11` only for `s > log(L_2k - 1)/log 11`, which exceeds `1` from `tau = 18` on.
2. The non-split part of `w_tau` is the full non-split Mobius factor, and the non-split part of `w_tau^-1` is its reciprocal `prod (1 - p^-s)^-1`; by the labeled import both have coefficient `l^1` abscissa `1`.

Therefore no summatory bound below abscissa `1` transfers between `m_tau` and `sigma_tau` at any rung `k >= 1`, in either direction, by this convolution route. The `theta > 1/3` transfer of the merged squarefree core belongs to the shell object `sigma_3 = s_5` and to `O_5`, not to the full-lift rung `m_3`; this probe does not extend it.

The [H] frame, stated once and fenced: `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` leaves admissible a uniform growing-mode diagonal route `h = h(N)` with explicit approximation and transfer error. The golden ladder is a concrete candidate family of diagonal modes, with rung `k = 0` the target augmentation and, by D, joint control of the rungs equivalent to control of the layers `B_a(x)` at each fixed `x`. Whether shell structure supplies joint control with usable constants is OPEN; nothing here is offered against the bridge row, and any future closure must obey that row's own fence: no zeta-zero statement, no equivalent Mertens estimate, and no target bound may enter as input. Layer-count asymptotics are occupied classical ground (integers with a prescribed number of prime factors); an import audit is owed before any analytic statement about `B_a(x)` is even proposed, and none is made here.

## 7. Frozen negative controls

The same local and coefficient constructors used by the positive gates carry five mutations. No mutation changes a threshold after the pin.

```text
B1  replace the shell Lucas value tau = 3 by tau = 4.
    sigma_4 = (-3)^omega(n) on squarefree pure-split n; the identity
    sigma_tau = s_5 first fails at the first split prime, n = 11.

B2  replace the non-split local sign -1 by +1 in the full-lift table.
    The identity m_2 = mu first fails at the first non-split prime,
    n = 2 (mutated value +1, mu(2) = -1).

B3  evaluate at the odd unit powers t = phi and t = phi^3.
    tau = phi + phi^-1 = 2phi - 1 = (-1, 2) and
    tau = phi^3 + phi^-3 = 4phi - 2 = (-2, 4) in Z[phi]; both have
    nonzero phi-component, so 1 - tau is not an integer and the
    selection theorem excludes them, as N(phi) = -1 predicts.

B4  the Pell near-misses m = 4 and m = 8.
    16 - 4 = 12 is not divisible by 5, and (64 - 4)/5 = 12 is not a
    square, so neither admits a solution of m^2 - 5b^2 = 4: the rung
    set has no member between 3 and 7 or between 7 and 18.

B5  Vandermonde with the repeated node list (-1, -2, -6, -1).
    The exact Gauss-Jordan elimination must find a zero pivot column
    and report the system singular.
```

## 8. Frozen verifier gates

```text
G01  even Lucas recurrence against the exact Z[phi] power route through
     k = 6, unit inverses, norm-one conjugates, N(phi) = -1, and the
     Pell enumeration m^2 - 5b^2 = 4 for 0 <= m <= 322 equal to
     {2, 3, 7, 18, 47, 123, 322}
G02  split local table 1, 1-tau, 2-tau, 2-tau, ... through degree 8 by
     exact Z[phi] series division of (1 - tT)(1 - t^-1 T)/(1 - T) at
     t = +-phi^(2k), k <= 4; non-split local table 1, -1, 0, ...
G03  m_2 = mu for every n <= 100000
G04  m_(-2)(n) = (-1)^b 3^a on every squarefree n <= 100000
G05  sigma_3(n) = mu(n) a_F(n) 1_((n,5)=1) for every n <= 100000, with
     a_F built as the Dirichlet convolution 1 * chi_5
G06  layer identity at x = 1000, 10000, 100000 for
     tau in {2, 3, 7, 18, -2, -3}
G07  exact Vandermonde inversion at x = 20000 from the rungs
     tau = 2, 3, 7, 18 recovers B_0..B_3 exactly; layer depth 3
G08  closed form 1 - (tau-1)^(e-1) through degree 8 and the
     convolution identity m_tau = sigma_tau * w_tau through
     n = 100000, for tau = 2 and tau = 3; w_2 trivial at split primes
G09  frozen exact integer readouts of section 9
G10  source firewall: ASCII, LF-only, standard-library imports
     {__future__, ast, fractions, math, pathlib, sys} only, no float
     or complex constant, no float/complex/eval/exec/compile/open call
G11  B1-B5 fire at n = 11, n = 2, phi-components (2, 4),
     near-misses 4 and 8, and the singular repeated-node system
```

The final stdout line is `VERIFY RESULT 11/11 ALL PASS`. The finite ranges audit the written universal proofs. They are not the theorem scope and cannot replace it.

## 9. Frozen readouts

Gate G09 freezes the following exact integers. They are readouts only; they prove no estimate and no cancellation, and gate nothing analytic. The `tau = 2` row reproduces the classical Mertens values as an internal cross-witness of the `mu` anchor.

```text
sum_(n<=x) mu^2(n) m_tau(n)
  tau = 2:    x=10^3: 2       x=10^4: -23     x=10^5: -48
  tau = 3:    x=10^3: 24      x=10^4: 75      x=10^5: 483
  tau = 7:    x=10^3: 252     x=10^4: 647     x=10^5: -4473
  tau = 18:   x=10^3: 2034    x=10^4: -6855   x=10^5: -279792
sum_(n<=x) sigma_tau(n)
  tau = 2:    x=10^3: -64     x=10^4: -395    x=10^5: -2432
  tau = 3:    x=10^3: -103    x=10^4: -381    x=10^5: -925
layers at x = 10^5
  B_0 = -363   B_1 = -53   B_2 = 339   B_3 = 77
```

These values were first exposed by the non-formal draft run archived in the merged Notes PR #595; freezing them here is a pin, not evidence.

## 10. Development disclosure

After public issue #791 was opened and before this pin, a development copy of the verifier was executed exactly once outside the repository, in a scratch directory, to audit the restructured gate list, the readout format, and the breaker routing. It returned `11/11` with empty stderr. That run is non-formal, is not committed, and carries no evidence credit. The accepted `verify.py` under this pin was only read, parsed, and compiled in memory inside the repository before the pin; it was never executed from the probe directory before the immutable public pin and its readback.

## 11. Clean interpreter-startup control and formal execution discipline

The first pushed probe commit contains only this `PREREG.md` and `verify.py`. After exact public readback of the pin, the frozen technical preflight runs first (the clean-interpreter startup control introduced by `P-O5-SQUAREFREE-CORE-1`, in the environment form of the current public probes):

```text
PATH:             /usr/bin:/bin
resolved python:  /usr/bin/python3
preflight:
  env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 \
    PYTHONHASHSEED=0 TZ=UTC \
    /usr/bin/python3 -c "print('PYTHON_STARTUP_CLEAN')"
required:
  exit 0
  stdout exactly: PYTHON_STARTUP_CLEAN plus LF
  stderr: empty
```

The preflight is an integrity and environment check, not a scientific gate. If it fails, this probe is STOP and no scientific output is accepted. Only if it passes may the single accepted scientific command run, exactly once:

```text
env -i PATH=/usr/bin:/bin LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 \
  PYTHONHASHSEED=0 TZ=UTC \
  /usr/bin/python3 probes/P-RAPIDITY-GOLDEN-LADDER-1/verify.py
```

The accepted stdout becomes `EXPECTED.txt`. `RUN.md` and `RESULT.md` are post-pin records only. The required pull-request workflow then replays the unchanged verifier on GitHub-hosted x86_64 and aarch64 under Python 3.12 and requires byte identity with the one committed `EXPECTED.txt`.

## 12. Explicit nonclaims

This probe does not:

- state or prove RH or GRH, locate a zero or pole, or construct or consume a meromorphic continuation of any Dirichlet series;
- make any `o(x)`, `O(x^theta)`, or cancellation statement for any ladder sum, any layer `B_a(x)`, or any other object;
- claim any uniformity in `x` for the layer inversion, or offer the layer equivalence as progress on `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]`;
- identify any rung with a Hecke, automorphic, or spectral object;
- select one split prime ideal, or identify Mobius parity with a permutation sign on any orientation fiber;
- consume the `theta > 1/3` transfer of `P-O5-SQUAREFREE-CORE-1`, the cutoff-axis theorems of `P-O5-GOLDEN-AXIS-BAND-1`, or any statement of the other O5 lanes;
- create a probability, Haar, physical, SI, decoder, or L1-L6 statement;
- change Canon, Registry, Frontier, dependency, evidence, gate, workflow, Note, reproduction, or an existing probe.

A later analytic use may combine independently earned results only through a separately reviewed fold. This probe itself stops at the exact algebra of the golden ladder.
