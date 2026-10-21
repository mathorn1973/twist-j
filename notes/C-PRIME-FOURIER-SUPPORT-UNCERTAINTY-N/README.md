# C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N

> **NON-CANONICAL, L1.** This note is not a formal public probe, carries no
> evidence credit, and changes no Canon, Registry, Frontier, gate or program
> status.

**Owner:** A. M. Thorn, session `fourier-support-2026-10-20`.
**Custody:** [issue #1682](https://github.com/mathorn1973/twist-j/issues/1682).
**Basis:** public `main` `5f20429944b409d912202d141e158fdfec145c41`, Public
Canon v103, content `01fb76f6b3b14a6a5ec05d0017ea922390ab6f66`.

## Outcome

```text
RESULT:      candidate-T / L1 for the p = 5 statements (proof plus exhaustive exact check)
             candidate-C for the finite breaker range
VERIFIER:    5/5 PASS
BREAKER:     3/3 HOLDS (second code path by the same author, not independent review)
EXPOSURE:    result-exposed; no preregistration or pre-execution pin is claimed
PLATFORMS:   one x86_64 environment
IMPORT:      Chebotarev's lemma on minors of the prime-order Fourier matrix,
             and the additive support bound it implies for cyclic groups of
             prime order (Tao, 2005)
```

## Statement

Let `z = zeta_5`, let `f: Z/5 -> C`, and let

```text
fhat(k) = sum_x f(x) z^(-x k),        F = [ z^(x k) ]  for x, k in Z/5.
```

**(A) Minors.** Every square minor of `F` is a nonzero element of `Z[z]`.
There are `C(10,5) - 1 = 251` of them, by size `25, 100, 100, 25, 1`. The
same holds for the conjugate matrix `[z^(-x k)]`, its image under
`z -> z^(-1)`.

**(B) Support bound.** For every nonzero `f`,

```text
|supp f| + |supp fhat| >= 6 = p + 1,
```

and the bound is attained at every split `a + (6 - a)`, `a = 1, ..., 5`.

**(C) Sampling form.** If `fhat` is supported on a set `K` of `b`
frequencies, then `f` is uniquely determined by its values on any set `X` of
`b` positions, regular or not.

**(D) Attribution.** (A) to (C) hold with five replaced by any prime `p`,
with bound `p + 1`; this packet checks `p = 2, 3, 7`. They fail for composite
length: at `N = 4` and `N = 6` vanishing minors exist, and the indicator of a
proper subgroup has support sum `2 + 2 = 4` and `2 + 3 = 5`, below `N + 1`.
The prime matters. Five is not selected by anything in this note.

## Proof

(A) is Chebotarev's lemma for `p = 5`. Independently of the import, the
verifier evaluates all 251 minors exactly. Each Leibniz term is a single power
of `z`, so each minor is an integer combination of `z^0, ..., z^4`; it is
reduced modulo `Phi_5` and tested for zero, which is exact because `Phi_5` is
the minimal polynomial of `z`.

(A) implies (B). Suppose `f != 0`, `supp f` is contained in `S`, `supp fhat`
is contained in `T`, and `|S| + |T| <= 5`. Then `fhat` vanishes on the
complement of `T`, which has at least `|S|` elements. Choose `|S|` of them,
`R`. The square block `[z^(-x k)]` with rows `k` in `R` and columns `x` in
`S` sends the restriction of `f` to `S` to zero, and it is invertible by (A)
(over `Q(z)`, hence over `C`). So `f = 0`, a contradiction.

(A) implies (C). The map from the values of `fhat` on `K` to the values of `f`
on `X` is the square block `[z^(x k)]`, `x` in `X`, `k` in `K`, up to the
factor `1/5`; it is invertible by (A).

Sharpness. Put `P_a(t) = prod_(k=1)^(a-1) (t - z^(-k))` and let `f_a(x)` be
the coefficient of `t^x`. Then `fhat_a(k) = P_a(z^(-k))` vanishes for
`k = 1, ..., a-1`, so `|supp f_a| <= a` and `|supp fhat_a| <= 6 - a`; by (B)
both are equalities. The verifier computes all five witnesses.

## Verification

```text
G1  all 251 minors of F and of conj(F) nonzero in Z[z]        PASS
G2  for all 606 pairs (S,T) with |S|+|T| <= 5 the blocking
    minor of the proof is nonzero                              PASS
G3  witnesses realize the splits 1+5, 2+4, 3+3, 4+2, 5+1        PASS
G4  p = 2, 3, 7: all 5, 19, 3431 minors nonzero                 PASS
G5  N = 4: 4 of 69 minors vanish, subgroup split 2+2;
    N = 6: 120 of 923 minors vanish, subgroup split 2+3        PASS
```

Self-break, `break.py`, shares no ring code with `verify.py`:

```text
B1  every one of the 251 minors is certified nonzero by Gaussian
    elimination over F_q under z -> w of order five, q in
    {11, 31, 41, 61, 71}, 20 embeddings; no reduction vanished   HOLDS
B2  all 3124 nonzero integer signals in {-2,...,2}^5, transform in the
    five-coefficient model modulo the all-ones vector: minimum
    support sum 6, attained 64 times                              HOLDS
B3  N = 4, all 80 nonzero signals in {-1,0,1}^4: 8 have support
    sum at most 4                                                 HOLDS
```

B2 is a finite range and supports only candidate-C on that range; the
statement for all complex signals rests on the proof and G1.

## Falsifiers

Each exact claim fires on a concrete witness in the stated arithmetic:

- a square minor of `[z^(x k)]` or `[z^(-x k)]` equal to zero in `Z[z]`;
- a nonzero `f` on `Z/5` with `|supp f| + |supp fhat| <= 5`;
- a witness `f_a` whose support split differs from `a + (6 - a)`;
- a vanishing minor of the prime-length Fourier matrix at `p = 2, 3` or `7`;
- no vanishing minor at `N = 4` or `N = 6`.

## Readings not claimed

In the continuum, Heisenberg's bound is a Fourier concentration statement and
the time-bandwidth sampling count is its sampling form. On `Z/p` both become a
pure count: no variance, no constant, only `p + 1` points. This dictionary is
a reading and stays O. Identifying any scalar here, including the Weyl
commutator scalar `z` of `ZX = z XZ`, with a physical action constant is
STOP. No position or momentum carrier, measurement, apparatus, preparation or
layer lift is supplied, and no entropic or variance form of the bound is
checked.

## Files

```text
README.md              this statement, proof and scope
verify.py              exact verifier, standard library only
EXPECTED.txt           exact verifier stdout
break.py               second-path self-break, standard library only
BREAKER_EXPECTED.txt   exact breaker stdout
RUN.md                 environment and commands
SHA256SUMS             hashes of every other file in this directory
```

Reproduce from the repository root:

```bash
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 notes/C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N/verify.py \
  | cmp - notes/C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N/EXPECTED.txt
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 notes/C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N/break.py \
  | cmp - notes/C-PRIME-FOURIER-SUPPORT-UNCERTAINTY-N/BREAKER_EXPECTED.txt
```
