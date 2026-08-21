# AUDIT. The Arb certificate for T(rho_1) != 0

```
STATUS     NON-CANONICAL audit note. No authority. Promotes nothing.
SUBJECT    /home/marek/twistj-runs/t-rho1-arb-20260810-v2/ on Linux x86_64 leg,
           certificate that T(rho_1) != 0 for the first nontrivial zero of zeta.
CLAIMED    candidate-T by the run's owner.
VERDICT    Reproduction confirmed, derivation audited on the two load-bearing
           lemmas, independent third code path agrees. The claimed status
           stands, with the trust boundary and the single-platform limitation
           named below. Obligation O-TM-T-NONVANISHING is CLOSED.
```

## 1. Reproduction at the source

```
sha256sum -c SHA256SUMS            17 of 17 OK
certificate.json                   fdcf995a84df85cd5af532c9ed505ddee55d1908be71a2a957307bd4fd4528e8
certify_t_rho1.py                  d4c2a4bf140a3dd4404c5e97b491ee7de6cf144b533327b4a4aa0cbef99280ac
SHA256SUMS                         3fbd892d00d1d8134e7bde1693273567b6f62807ae48f21cee0826eb12d0f9e1
EXIT_STATUS                        0, stderr.log and verification.stderr both empty
verify_artifact.py rerun           RESULT VERIFIED, 1146 Arb records, per_j_count 80,
                                   endpoints emitted as exact dyadic rationals
preflight_comparison.log           SCIENTIFIC_PAYLOAD_MATCH on all eight sections
```

The three hashes quoted by the owner match the files. The verifier reruns clean.

## 2. Independent third code path

The certificate evaluates the functional identity
`T(s) = -1 - sum_{j>=1} binom(-s,j) 2^(-s-j) T(s+j)` with dyadic acceleration.
Its own cross-check uses a Mellin representation. A third, unrelated evaluation
was run for this audit: the plain functional recursion at 60 decimal digits with
ladder 60, j-truncation 700 and far-field length 400, on a different machine.

```
Re T(rho_1) = -0.7603356110672142114218582127501785
Im T(rho_1) = -0.1162829988608512552612766655530401
|T(rho_1)|  =  0.7691761679102042825798080998814973
```

All three coordinates lie inside the certified rectangle, near its centre: the
box is 3.87e-14 wide in each coordinate and the independent value sits about
1.93e-14 from each endpoint. Together with the certificate's two Mellin runs
this makes four independent evaluations in agreement.

## 3. Derivation audit, the two load-bearing lemmas

Hashes prove reproduction, not correctness. Both mathematical cores check out.

```
L1  DYADIC ANNIHILATION. For L = 2^k and the shift E,
      prod_{q=0}^{k-1} (1 - E^(2^q))  =  sum_{r=0}^{2^k-1} t(r) E^r.
    Correct and exact: expanding the product indexes subsets S of {0,...,k-1}
    with sign (-1)^|S| and shift sum_{q in S} 2^q; every r < 2^k has a unique
    binary representation, and (-1)^popcount(r) = t(r). The two indexings are
    the same indexing.

L2  BLOCK BOUND. |prod_{q<k}(1-E^(2^q)) f(x)| <= 2^(k(k-1)/2) |(z)_k| x^(-Re z-k)
    for f(x) = x^(-z). Correct: the k-fold difference with steps 1, 2, ..., 2^(k-1)
    is a k-fold integral of f^(k) over a box of side lengths those steps, the
    product of the steps is 2^(0+1+...+(k-1)) = 2^(k(k-1)/2), and
    |f^(k)(x)| = |(z)_k| x^(-Re z - k) is decreasing in x, so the supremum sits
    at the left endpoint.

L3  OUTER TAIL. Consecutive terms of the j-sum have ratio (s+j)/(2(j+1)) in
    modulus, at most (j+15)/(2(j+1)) since |rho_1| < 15. That expression is
    decreasing in j and equals 24/41 at j = 81 = N+1 with N = 80. Geometric
    tail with ratio 24/41 < 1. Correct. The factor |T(s+j)| <= zeta(j+1/2) is
    the standard trivial bound.

L4  SIGN CONVENTION. t(n) = (-1)^popcount(n), t(0) = +1, t(1) = -1, matching the
    convention of the candidate. The script's exact spot checks of
    t(2^k m + r) = t(m) t(r) for r < 2^k are correct, popcount being additive
    under dyadic concatenation.
```

NOT audited: the interval-arithmetic bookkeeping inside `evaluate_shift`, the
radius propagation, and the decimal inter-process transport, where the script
states the correct requirement that transport may only widen an Arb object.
That code was reproduced and cross-checked numerically, not read line by line.

## 4. What follows, and what does not

The consequence needs LESS than the candidate's addendum 3 assumed.

```
1  The partial sums of t lie in {-2,-1,0}, so T converges and is analytic on
   Re(s) > 0. That alone puts rho_1 = 1/2 + 14.134...i inside the domain of
   analyticity. The functional equation and the entirety of T are NOT
   load-bearing here; they are only the vehicle the certificate evaluates
   along. The outstanding technical debt about locally uniform convergence of
   the j-sum therefore does not touch this result.
2  T(rho_1) != 0, certified.
3  If the abscissa of convergence sigma_c of sum c(n) n^(-s) were below 1/2,
   then C would be analytic at rho_1, the identity T = zeta . C would extend
   there by continuation, and T(rho_1) = zeta(rho_1) C(rho_1) = 0. Contradiction.
   Hence sigma_c >= 1/2.
4  For a Dirichlet series with positive abscissa,
   sigma_c = limsup log|R(x)| / log x with R(x) = sum_{n<=x} c(n).
```

```
THEOREM (unconditional).  sum_{n <= x} c(n)  is not  O(x^(1/2 - eps))
for any eps > 0.
```

So the first zero of zeta is visible in the summatory function of an elementary
arithmetic function defined by binary digit parity and Moebius inversion, with
no hypothesis assumed anywhere.

What does NOT follow, stated plainly:

```
-  No upper bound. The matching O(x^(1/2 + eps)) is the RH-grade statement that
   was withdrawn from the preprint for want of a proof. The picture is
   asymmetric: lower bound unconditional at 1/2, upper bound open.
-  Nothing about the location of any zero of zeta, and nothing about RH.
-  Nothing about zeros of T other than rho_1. The same argument at any zeta
   zero rho with T(rho) != 0 gives sigma_c >= Re(rho); no such certificate
   exists for any other rho.
```

## 5. Two limitations to close

```
LIM1  TRUST BOUNDARY. The chain rests on FLINT's acb.zeta_zero, documented as
      certified Hardy-Z isolation with Turing counting, recorded in the run as
      N_zeta(14) = 0 and N_zeta(15) = 1. That is a library dependency, not a
      hand proof, and should be named as one wherever the result is stated.
      Environment pinned: FLINT 3.6.0, python-flint 0.9.0, CPython 3.13.5.
LIM2  ONE PLATFORM. The run is Linux x86_64 leg x86_64 only. The house standard for a
      computation-grade result is two architectures. This is exact dyadic
      interval arithmetic, so the endpoints should be bit-identical on a second
      machine, which makes the check meaningful rather than cosmetic. A leg is
      cheap: PIS is aarch64 with CPython 3.13.5, and the matching wheel
      python_flint-0.9.0-cp313-cp313-manylinux aarch64 downloads cleanly there.
      Same pin as requirements.lock.
HOUSEKEEPING  the run directory carries both COMPLETE and RUNNING as empty
      marker files. RUNNING should be cleared on completion; an archive that
      reads RUNNING forever is ambiguous to a later reader.
```

## 6. Placement

This does not belong in the divisor-cube preprint, which is a finite and
combinatorial paper framed on Gelfond and Mauduit and deliberately carries no
analytic section. The certificate is the centrepiece of its own short note,
together with claims A17 to A21 of addendum 3, where the deposit can be the
certificate rather than an appendix to something else.
