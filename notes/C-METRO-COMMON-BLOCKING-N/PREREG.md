# PREREG C-METRO-COMMON-BLOCKING-N

Status: NON-CANONICAL incubation candidate, no authority, promotes nothing.
Target line on promotion: public, as a probe P-METRO-COMMON-BLOCKING-1 under
METRO-REDUCTION-CALCULUS [O], obligation D only. Session: Claude (Cowork),
2026-09-22. Basis: Public Canon v91 (main 11b66d4, STATUS ACTIVE, SHA256SUMS
5 of 5 OK), canon/CANON.md section 15.

Known-result disclosure: a read-only scratch exploration by a helper agent in
this session computed census counts for these boxes before this freeze. Those
numbers are therefore exposed and this is a known-result protocol, not blind
discovery. The frozen verifier below is new code written after that
exploration and does not import it.

## Reading that needs owner confirmation

Canon fixes enc_q only as "a fixed digit and padding convention". This probe
declares the encoding family ENC4 and decides obligation D inside it:

    MSD-E0  enc(0) = empty word; n > 0: base-q digits, most significant first,
            no leading zero.
    MSD-Z0  as MSD-E0 but enc(0) = "0".
    LSD-E0  enc(0) = empty word; n > 0: base-q digits, least significant
            first, no trailing zero.
    LSD-Z0  as LSD-E0 but enc(0) = "0".

Letters of a word are applied in reading order: D_i(u_1 ... u_m) =
delta_(i,u_m) o ... o delta_(i,u_1). state_P(s,n) = D_a(enc(n_a)) o ... o
D_1(enc(n_1)) (s), Stream_P(s,n) = w(state_P(s,n)), as in section 15.
"Common q^k blocking" is read as one block length k for every coordinate.

## 1. Equation

Blocking. For k >= 2 let word_k(U), U in {0,...,q^k - 1}, be the length-k
base-q word of U in the convention's reading order, zeros kept. Define

    Blk_k(P) = (q^k, a, r, S, A0, {Delta_(i,U)}, enc_(q^k), w),
    Delta_(i,U) = D_i(word_k(U)),

with enc_(q^k) the same convention in base q^k, and start, input-index and
output transports the identity (tau = id).

L0 (flattening). With rho = (-|enc_q(n)|) mod k, the concatenation of the
super-digit words of enc_(q^k)(n) is 0^rho enc_q(n) under MSD and
enc_q(n) 0^rho under LSD, for E0 and Z0 alike. The vector
(rho_1,...,rho_a) is the exponent-residue vector.

Pairs. Pairs_0 = {(s,s): s in A0};
Pairs_i = {(D_i(pad(v)) x, D_i(v) y): (x,y) in Pairs_(i-1), v in Enc},
where Enc is the image of enc_q and pad(v) is the flattening of L0. Each
Pairs_i is computed by a finite automaton search over (x, y, rho guess,
|v| mod k, canonical-prefix flag). Pre_blk(P,k) holds iff w(x) = w(y) for
every (x,y) in Pairs_a.

D1 (exact admission criterion). Pairs_a = {(state_Blk(s,n), state_P(s,n)):
s in A0, n in N^a}. Hence Blk_k is an admitted arrow of section 15 (pointwise
stream intertwining for every allowed start and input) iff Pre_blk(P,k).

D2 (transport). Under Pre_blk the complete stream family over allowed starts
is unchanged, so every decision and terminal value that is a function of it,
in particular Adm_direct and its terminal L, is unchanged. Blk_k maps
commuting tuples to commuting tuples.

D3 (augmented blocking, MSD only). Blk#_k(P) has carrier S x {0,1}^a,
starts A0 x {0^a}, output w#(x,f) = w(x), and maps
Delta#_(i,U)(x,f) = (D_i(word_k(U)) x, f) if f_i = 1, and if f_i = 0:
(D_i(strip(U)) x, f with f_i := 1), where strip(U) is word_k(U) with leading
zeros removed for U != 0, strip(0) = "0" under Z0 and the empty word under E0.
Claim: state_Blk#((s,0),n) = (state_P(s,n), f(n)) with f(n)_i = 1 iff
enc_q(n_i) is nonempty; so Blk#_k is exact with no precondition, and it maps
commuting tuples to commuting tuples.

Witnesses. W-D1: q=2, a=1, S={0,1}, A0={0}, delta_0 = swap, delta_1 = id,
w = (0,1), MSD-E0, k=2: Stream_P(0,1) = 0 and Stream_Blk(0,1) = 1.
W-D2: q=2, a=2, S={e,o}, A0={e}, every delta_(1,u) = swap, every
delta_(2,u) = id, W5(e) = (1,0), W5(o) = (0,1), MSD-E0, k=2. On the translated
boxes R((2^m,0),(2^m,2^m)) the normalized average is PROBABILITY(1,0) for odd
m and PROBABILITY(0,1) for even m, so Adm_direct(P) = INADMISSIBLE, while
Blk_2(P) has constant stream W5(e), so Adm_direct(Blk_2 P) =
ADMISSIBLE(PROBABILITY(1,0)). The tuple is commuting (inside C_dim).

## 2. Code

verify.py, Python 3 standard library only, integers and Fraction, no float.

## 3. Carrier and data

Box B1: q=2, a=1, S={0,1,2}, A0=S, all delta_0, delta_1 in S^S, all
w: S -> {0,1}: 27*27*8 = 5832 tuples, k in {2,3}, all four conventions.
Box B2: q=2, a=2, S={0,1}, A0={0}, all four digit maps in S^S, all
w: S -> {0,1}: 256*4 = 1024 tuples, k in {2,3}, all four conventions;
commuting subclass reported separately.
Brute-force horizon: every n with all coordinates < 2^HB, HB = 7 for B1 and
HB = 5 for B2. L0 checked for n < 2^10, k in {2,3,4}, q in {2,3}.

## 4. Systematics

The automaton is exact and decides Pre_blk for all n in N^a; the brute force
covers a finite horizon only and is a consistency check, not the proof.
Census counts are computation at declared finite range (candidate-C). D1 to
D3 are written proofs (candidate-T on review). The LSD augmented
construction is out of scope; for LSD only Pre_blk is decided.

## 5. Failure threshold (falsifier, fixed before computation)

The candidate fires (is falsified) if any of:
  F1 for any tuple, k and convention: (a) the brute force below the horizon
     finds n with Stream_Blk != Stream_P while the automaton says Pre_blk
     holds, or (b) the automaton says Pre_blk fails but the explicit input n
     reconstructed from its failing path does not give Stream_Blk !=
     Stream_P when evaluated directly with both encoders;
  F2 Blk#_k disagrees with Stream_P at any tested (s,n) (MSD);
  F3 L0 fails for any tested n;
  F4 W-D1 or W-D2 does not reproduce exactly;
  F5 Blk_k or Blk#_k maps a commuting tuple to a noncommuting one.

## 6. Action layer

L5 (pointwise stream and reduction calculus). No L6 lift: Adm_direct in W-D2
is evaluated only on the explicit box family displayed, by exact counting.

## Break plan

Second path: realize every automaton pair by an explicit input n (shortest
witness words), and recompute Blk# streams by building the blocked tuple
explicitly as a U_RF tuple and running its own encoder, not the flattening
lemma.
