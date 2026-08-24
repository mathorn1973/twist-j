# PROOF: PROP-1, written out (C-PRIME-ORDER-READING-1)

Status: candidate-T support document. Replaces the prereg sketches of A1 and
A2 with full proofs. NOT independently reviewed; that review is the open item
before any promotion talk. No canon effect. 2026-08-11.

Setting. F = Q(sqrt5), O = Z[phi], phi^2 = phi + 1, nontrivial automorphism
sigma, norm N(x) = x sigma(x), units O^x = {+-phi^m : m in Z} (Dirichlet;
phi fundamental), N(phi) = -1. A split rational prime p (p = +-1 mod 5)
factors as pO = P sigma(P) with P != sigma(P); by class number one P = (w),
N(w) = +-p. For a generator w write |w|_1 |w|_2 = p at the two real places
and |w|_1 = sqrt(p) e^(t(w)). Replacing w by +-phi^j w shifts t by
j log phi; replacing w by sigma(w) negates t. The canonical unordered class
is R(p) = {t, -t} in (R/(log phi)Z)/{+-1} (SPLIT-PRIME-RAPIDITY-CLASS [T]).

LEMMA 1 (rational squares of F). A rational c is a square in F exactly when
c is a rational square or five times one.
Proof. (a + b sqrt5)^2 = a^2 + 5 b^2 + 2ab sqrt5 lies in Q iff ab = 0,
leaving a^2 or 5 b^2. Both families are indeed squares. qed

LEMMA 2 (norm-one units). z in O^x with N(z) = +1 implies z = +-phi^(2j).
Proof. N(+-phi^m) = (-1)^m. qed

PROPOSITION A1 (reduction, generator-free tests). Let p != q be split with
any generators w_p, w_q, and put y_dir = w_p sigma(w_q), y_con = w_p w_q,
n = pq. Then
(i)   matching-orientation equality of the oriented classes holds iff
      n | y_dir^2 in O;
(ii)  opposite-orientation equality holds iff n | y_con^2 in O;
(iii) R(p) sits at a fixed point of the involution iff p | w_p^2 in O,
      and the half-period fixed point is impossible outright.
All right-hand sides are independent of the generator choices.

Proof. Generator changes multiply y by a unit, and unit squares do not
affect divisibility by a rational integer. (i), forward: t(w_p) - t(w_q) =
k log phi gives |y_dir|_1 = sqrt(n) phi^k, |y_dir|_2 = sqrt(n) phi^(-k).
Set u = y_dir^2 phi^(-2k) / n in F. Then |u|_1 = |u|_2 = 1; writing
u = a + b sqrt5 with a, b rational, equal absolute values at the two real
places force ab = 0. The branch a = 0 gives N(u) = -5 b^2 < 0, while
N(u) = N(y_dir)^2 N(phi)^(-2k) / n^2 = +1; so b = 0 and u = +-1. The
place-1 image of u is positive (y^2, phi^(-2k) and n are all positive
there), so u = +1, y_dir^2 = n phi^(2k), and n | y_dir^2.
(i), converse: n | y_dir^2 gives z = y_dir^2 / n in O with N(z) = +1, so
z = +-phi^(2j) by Lemma 2; the minus sign dies on place-1 positivity;
y_dir^2 = n phi^(2j) then forces |y_dir|_1 = sqrt(n) phi^j, which is the
matching-orientation equality with k = j. (ii) is the same computation
with t(w_p) + t(w_q). (iii): a fixed point means 2 t(w_p) = m log phi.
If m is odd, the same argument gives w_p^2 = p phi^m, whose norm is
p^2 (-1)^m = -p^2 < 0, contradicting N(w_p^2) = p^2 > 0: the half-period
fixed point cannot occur at all. If m is even, w_p^2 = p phi^m and
p | w_p^2; the converse runs as in (i). qed

PROPOSITION A2 (emptiness = PROP-1). The divisibilities of A1 never hold:
for distinct split p, q and both match types, pq does not divide y^2, and
for every split p, p does not divide w_p^2.
Proof. By A1 a divisibility forces y^2 = n phi^(2j), i.e.
(y phi^(-j))^2 = n with n in {pq, p}. By Lemma 1, n would be a rational
square or five times one. pq is a product of two distinct primes, both
different from 5, hence squarefree and not divisible by 5: neither branch.
p is a prime different from 5: neither branch. qed

COROLLARY. The unordered rapidity class map is injective on split primes
and its image avoids both fixed points of the involution, as exact real
classes, not merely at audited range. Combined with the v44 floor that the
winding integer is unit gauge: the canonical J-side data separates split
primes completely, and the entire order deficit is the winding number.

REMARK on the computations. The accepted verifier (21170 pair tests, two
paths, 30/30 controls) and the breaker (gauge invariance on 2280 variants,
phi-coordinate rederivation of Lemma 1 on 10731 moduli, scan to 10000 with
370272 pair tests, broken=0) are audits and attack survivals, not the
evidence for the universal statements; the proofs above are.
