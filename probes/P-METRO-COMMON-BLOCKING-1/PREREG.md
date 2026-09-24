# PREREG P-METRO-COMMON-BLOCKING-1

```text
probe          P-METRO-COMMON-BLOCKING-1
public lock    issue #1148
owner item     METRO-REDUCTION-CALCULUS [O], obligation D only
layer          L5 reduction calculus and pointwise L5 stream only.
               No lift to L6 is claimed.
scope claimed  obligation D (common q^k blocking) inside the declared
               encoding family ENC4, with one block length k for every
               coordinate
```

This probe does not close `METRO-REDUCTION-CALCULUS`. Obligation E
(completeness of `approx_red`) remains open. The row stays `[O]` and STOP.

Basis: Public Canon v91, tag `canon-v91`, activation/main commit
`11b66d4755a697031157f0e10dc1898a7d5b6379`, content commit
`b89b0c80bb5cebddade567f31a979aaf42f1d9dd`, and `canon/CANON.md` SHA-256
`6d49a9dfce95f2146490ccc9ae76066bca01d1614291549562b599d35b2218e1` with
772678 bytes.

## Commit identity

The requested author is A. M. Thorn. The connected GitHub write interface
uses `A. M. Thorn <221838986+mathorn1973@users.noreply.github.com>` and cannot
supply an author override. The author's prior explicit instruction, "Push s
autorem co umis" (19 September 2026), allowed that connected identity; the
current instruction authorizes publication of this reviewed bundle and D
procedure. This publication uses that same allowed identity transparently.

## Falsifier, first

```text
fires if the pinned verifier's stdout differs from the frozen expectation
below, if any of F1 to F5 fires, if W-D1 or W-D2 fails to reproduce, or if a
tuple, a convention in ENC4 and k are exhibited for which Pre_blk holds and
the blocked stream differs from the original stream at some allowed start and
input
```

A fired falsifier is merged and archived, never hidden. No threshold, family,
layer or scope moves after the pin.

## Prospective-pin and known-result disclosure

This is a transparent known-result protocol, not blind discovery. The
statements, the verifier and the census were developed and executed
beforehand in a non-public incubation record. That record is outside the
repository and is not evidence. Its separately submitted public summary is owned by issue #1147 at
`notes/C-METRO-COMMON-BLOCKING-N`; the self-contained proof below does not
require that note to be merged before this pin.

`verify.py` in this directory is byte-identical to the incubation verifier
(SHA-256 `01cc83c7ee605793eac5388db2af43538388590a192025f5a04589c910a888a5`).
The incubation executions produced stdout SHA-256
`17233b6b7f04af2c2e76836c22213615c666588f3ecedfcf0d894d6cbf684134`, ending in
`FAILURES 0` and `RESULT PASS`. They were two runs on x86_64 with Python 3.11
and one run on aarch64 with Python 3.12. The first formal execution of this
probe is authorized only after the public push and readback of the two-file
pin.

An additional pre-publication review replay on Linux x86_64, Python 3.13.5,
reproduced the same 2099-byte stdout with the hash above, exit 0 and empty
stderr. It was an unpinned review of the NON-CANONICAL note, not a formal
public probe execution. The subsequent publication review checked the
written proof and preserved verifier bytes; it is not blind confirmation.

The unpinned packaging draft named an aarch64 first local leg and a 120-second
external budget. Before this public pin, the execution plan is aligned with
the current repository procedure: x86_64 local first run, followed by both
required Python 3.12 architecture jobs; the runner timeout is 600 seconds.
These are disclosed pre-pin procedural choices. The verifier, mathematical
family, failure conditions and known exact stdout remain unchanged.

## 1. Equation

`P = (q,a,r,S,A0,{delta_(i,u)},enc_q,w)` is a `U_RF` tuple of section 15.
Letters of a word act in reading order:
`D_i(u_1 ... u_m) = delta_(i,u_m) o ... o delta_(i,u_1)`. Then
`state_P(s,n) = D_a(enc(n_a)) o ... o D_1(enc(n_1)) (s)` and
`Stream_P(s,n) = w(state_P(s,n))`.

**Encoding family ENC4.** Canon fixes `enc_q` only as "a fixed digit and
padding convention". The probe decides obligation D for each of

```text
MSD-E0  enc(0) = empty word; n > 0: base-q digits, most significant first,
        no leading zero
MSD-Z0  as MSD-E0 but enc(0) = "0"
LSD-E0  enc(0) = empty word; n > 0: base-q digits, least significant first,
        no trailing zero
LSD-Z0  as LSD-E0 but enc(0) = "0"
```

"Common q^k blocking" is read as one block length `k >= 2` for every
coordinate.

**Blocking.** `word_k(U)`, `U in {0,...,q^k - 1}`, is the length-k base-q
word of U in the convention's reading order, zeros kept.

```text
Blk_k(P) = (q^k, a, r, S, A0, {Delta_(i,U)}, enc_(q^k), w),
Delta_(i,U) = D_i(word_k(U)),
```

with `enc_(q^k)` the same convention in base `q^k`, and start, input-index
and output transports the identity.

**L0, flattening.** Concatenate the super-digit words of `enc_(q^k)(n)`. The
result is `0^rho enc_q(n)` under MSD and `enc_q(n) 0^rho` under LSD, with
`rho = (-|enc_q(n)|) mod k`, for E0 and Z0 alike. Proof: base `q^k` digits
are blocks of k base-q digits of the same number. For `n > 0` the block
containing the most significant digit is padded by exactly `rho` zeros, and
for Z0 at zero, `0^k = 0^(k-1) "0"`. The vector `(rho_1,...,rho_a)` is the
exponent-residue vector of the row.

**Pairs.** `Pairs_0 = {(s,s): s in A0}`, and

```text
Pairs_i = {(D_i(pad(v)) x, D_i(v) y): (x,y) in Pairs_(i-1), v in Enc},
```

where Enc is the image of `enc_q` and `pad(v)` is the flattening of L0.
`Pre_blk(P,k)` holds iff `w(x) = w(y)` for every `(x,y)` in `Pairs_a`.

**D1, exact admission criterion.**
`Pairs_a = {(state_Blk(s,n), state_P(s,n)) : s in A0, n in N^a}`. Hence
`Blk_k` is an admitted arrow of section 15 (pointwise stream intertwining for
every allowed start and input) iff `Pre_blk(P,k)`.

Proof. By L0 the blocked run on `n` applies `D_i(pad(enc_q(n_i)))`, so the
joint runs are exactly the defining recursion of `Pairs`. The padding depends
on `v` only through `|v| mod k`, and canonicity (no leading zero under MSD, no
trailing zero under LSD) is a regular constraint. So `Pairs_i` is the
reachable set of a finite search over
`(x, y, rho, |v| mod k, canonical-prefix flag)` and is computed exactly.
Intertwining at every allowed start and input is, by definition, agreement
of `w` on `Pairs_a`.

Here and below, a commuting tuple means commutation between distinct
coordinates: delta_(i,u) delta_(j,v) = delta_(j,v) delta_(i,u) for i != j
and every u,v, as in section 15 of the Canon. No same-coordinate
commutation of digit maps is asserted or required.

**D2, transport.** Under `Pre_blk` the complete stream family over allowed
starts is unchanged. Every decision and terminal value that is a function of
it is therefore unchanged, in particular `Adm_direct` and its terminal `L`.
`Blk_k` maps commuting tuples to commuting tuples. Proof: each
`Delta_(i,U)` is a composition of maps of coordinate i, and compositions of
pairwise commuting maps commute.

**D3, augmented blocking (MSD only).** `Blk#_k(P)` has carrier
`S x {0,1}^a`, starts `A0 x {0^a}` and output `w#(x,f) = w(x)`. Its maps are

```text
Delta#_(i,U)(x,f) = (D_i(word_k(U)) x, f)                  if f_i = 1,
                    (D_i(strip(U)) x, f with f_i := 1)     if f_i = 0,
```

where `strip(U)` is `word_k(U)` with its leading zeros removed for
`U != 0`, `strip(0) = "0"` under Z0, and `strip(0)` is the empty word under
E0. Claim: `state_Blk#((s,0),n) = (state_P(s,n), f(n))`, where
`f(n)_i = 1` iff `enc_q(n_i)` is nonempty. So `Blk#_k` is exact with no
precondition, and it preserves this cross-coordinate commutation.

Proof by induction over the super-digits of each coordinate. The first
super-digit of a canonical MSD encoding is nonzero unless `n_i = 0` under Z0.
Stripping its leading zeros gives exactly the leading part of
`enc_q(n_i)`. Under Z0, zero gives "0", and under E0 zero gives no letters and
the flag stays 0. Every later super-digit acts by its full word. Maps of
different coordinates touch different flag bits and act on `x` through
commuting maps.

**Witnesses.**

```text
W-D1  q=2, a=1, S={0,1}, A0={0}, delta_0 = swap, delta_1 = id, w = (0,1),
      MSD-E0, k=2:  Stream_P(0,1) = 0 and Stream_Blk(0,1) = 1.
W-D2  q=2, a=2, S={e,o}, A0={e}, every delta_(1,u) = swap, every
      delta_(2,u) = id, W5(e) = (1,0), W5(o) = (0,1), MSD-E0, k=2.
      On the boxes R((2^m,0),(2^m,2^m)), every integer m >= 0, the normalized average
      is PROBABILITY(1,0) for odd m and PROBABILITY(0,1) for even m, so
      Adm_direct(P) = INADMISSIBLE, while Blk_2(P) has constant stream W5(e)
      and Adm_direct(Blk_2 P) = ADMISSIBLE(PROBABILITY(1,0)). The tuple is
      commuting.
```

For W-D2, every integer n_1 in [2^m,2^(m+1)) has exactly m+1 binary
letters. Each letter swaps the first-coordinate state; the second-coordinate
maps are identities. Thus every point of the box has state e for odd m and o
for even m. This proves the displayed alternating averages for all m, and
therefore failure of uniform translated-box convergence. Every two-letter
blocked map is the identity, so the blocked stream is constant on every
input. The verifier's m=2..8 scan audits this all-m proof.

W-D2 rejects a proposed unconditional same-carrier admission rule: such a
rule would purport to admit a map that changes the decision. It does not
falsify the unchanged registered parent, whose admitted arrows require
exact transport. Individual same-carrier instances satisfying `Pre_blk`
remain admitted. The alternative augmentation is scoped to MSD only.

## 2. Code

`verify.py` in this directory is the accepted exact verifier. It uses only
the Python standard library, integer arithmetic and `fractions.Fraction`. It
uses no float, randomness, clock, filesystem access, network access,
subprocess, dynamic evaluation or external data.

After the public pin, run exactly once from the repository root:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-METRO-COMMON-BLOCKING-1/verify.py
```

External budget: 600 seconds, as in tools/check_verifier.py on the frozen
repository basis. Incubation timing is descriptive, not a scientific threshold.

## 3. Carrier or data

There are no experimental data. The carrier is the frozen `U_RF` type.

```text
B1  q=2, a=1, S={0,1,2}, A0=S, all delta_0, delta_1 in S^S, all binary w:
    27*27*8 = 5832 tuples; k in {2,3}; all four conventions.
B2  q=2, a=2, S={0,1}, A0={0}, all four digit maps in S^S, all binary w:
    256*4 = 1024 tuples; k in {2,3}; all four conventions; the commuting
    subclass (232 tuples) reported separately.
HB  brute-force horizon: every n with all coordinates below 2^7 (B1) and
    2^5 (B2); Blk# checked below 2^5 (B1) and 2^4 (B2).
L0  checked for n < 2^10, k in {2,3,4}, q in {2,3}.
```

## 4. Systematics

```text
S1  D1, D2, D3 and L0 are exact statements with written proofs. The finite
    families audit the implementation and the witnesses; they do not
    replace the proofs.
S2  The automaton decides Pre_blk for all n in N^a. The brute force covers a
    finite horizon only and is a consistency check.
S3  Census counts are finite-range computation (at most C as computation).
S4  The augmented construction is proved and checked for MSD only. For LSD
    only Pre_blk is decided.
S5  ENC4 and the reading "one k for every coordinate" are declared readings.
    Other encodings or per-coordinate block lengths are out of scope.
S6  The first formal local leg is x86_64. The required GitHub Python 3.12
    jobs independently reproduce this same pinned verifier on x86_64 and
    aarch64 against one committed EXPECTED.txt; their aggregate check must
    pass. A local same-architecture replay alone does not satisfy the gate.
```

## 5. Failure threshold

```text
F1  (a) the brute force below the horizon finds n with Stream_Blk != Stream_P
    while the automaton says Pre_blk holds, or (b) the automaton says Pre_blk
    fails but the explicit input reconstructed from its failing path does not
    give Stream_Blk != Stream_P when evaluated directly with both encoders
F2  Blk#_k disagrees with Stream_P at any tested (s,n) under MSD
F3  L0 fails for any tested n
F4  W-D1 or W-D2 does not reproduce exactly
F5  Blk_k or Blk#_k maps a commuting tuple to a noncommuting one
```

Frozen expectation: stdout SHA-256
`17233b6b7f04af2c2e76836c22213615c666588f3ecedfcf0d894d6cbf684134`, final
lines `FAILURES 0` and `RESULT PASS`. Any one failed gate fails the probe.

## 6. Action layer

L5 only: a typed reduction arrow and pointwise transported L5 streams.
Decision transport in D2 is a function of the L5 stream family. No L6
normalization, SI bridge, physical reading or other layer lift is claimed.

On success, the probe supplies evidence for obligation D of
`METRO-REDUCTION-CALCULUS`, within ENC4 and one common k. It edits no Canon
file. A later fold would need three owner decisions:

```text
O-D1  confirm ENC4 and the reading "one k for every coordinate"
O-D2  admit Blk_k under Pre_blk, the MSD-only Blk#_k, or both, as arrow 5
O-D3  whether the unconditional same-carrier blocking RULE joins the
      forbidden catalogue as a sixth entry, witnessed by W-D1 and W-D2;
      valid individual instances satisfying Pre_blk are not forbidden
```

Obligation E remains open, and the parent row remains `[O]` and STOP.
