# PREREG C-LI-COCYCLE-1 (frozen before first execution)

```
CANDIDATE:  C-LI-COCYCLE-1, incubation lane, continuation directed by the
            owner: "zkus pokracovat na J nativni uniform cocycle"
            (target row J-LI-COCYCLE-REALIZATION [O]).
DATE:       2026-07-16 (frozen before the single run of the verifier)
LAYER:      L5 finite exact statements plus exact real-interval gates
            attached to the sealed normalization xi_J = xi. The target O
            is L6. No lift is claimed; every lift needs its own named gate.
```

## Equation (the frozen statements)

```
CO1  Symbol algebra over the basis (1, gamma, gamma^2, gamma_1, pi^2,
     log 4pi), exact Fractions, with the imported identities
     sigma_1 = 1 + gamma/2 - log(4pi)/2 and
     sigma_2 = 1 + gamma^2 + 2 gamma_1 - pi^2/8:
       lambda_1 = sigma_1;  lambda_2 = 2 sigma_1 - sigma_2;
       t_0 = 2 lambda_1;  t_1 = lambda_2 - 2 lambda_1 = -sigma_2;
       t_0 + t_1 = lambda_2;
       M_1 := t_0 - t_1 = 2 sigma_1 + sigma_2
            = 3 + gamma + gamma^2 + 2 gamma_1 - pi^2/8 - log(4pi).
     T_1 (2x2 Toeplitz) PSD iff M_1 >= 0 and lambda_2 >= 0.
CO2  gamma_1 by second-order Euler-Maclaurin bracket at N = 10^5 with
     f(x) = ln x / x:
       gamma_1 in [A_N - f(N)/2, A_N - f(N)/2 + 2B],
       B = (ln N - 1)/(12 N^2),
     where A_N = sum_{k<=N} f(k) - ln^2(N)/2, all in directed integer
     intervals at scale 10^18. Assertions: the interval is strictly
     negative, width < 10^-9, and lies inside the amendment-1 elementary
     bracket [-72873410205792217, -72758280940973182] * 10^-18.
CO3  The T_1 gate: M_1 > 0 by exact interval, M_1 < 10^-4;
     lambda_2 > 0 with width < 10^-8; det T_1 = M_1 * lambda_2 > 0.
CO4  The J-native finite exemplar: U = the primitive 10th roots of unity,
     which are exactly the mixed 2-form eigenvalues of the plenum step
     (assert -zeta_5^k = zeta_10^((2k+5) mod 10) in Z[zeta_20], exponents
     {1,3,7,9}); cocycle b(n) = (U^n - I)(1,1,1,1) has
     ||b(n)||^2 = psi(n) = 8 - 2 c_10(n) exactly, with frozen values
     psi(0..10) = 0,6,10,6,10,16,10,6,10,6,0, period 10;
     second differences t_m = psi(m+1) + psi(m-1) - 2 psi(m) (psi even)
     equal (12, -2, -8, 8, 2) for m = 0..4;
     the normal form K = L T L^T holds exactly (K_{jk} = psi(j) + psi(k)
     - psi(|j-k|), j,k = 1..5; L lower-triangular ones; hand proof by
     telescoping, recorded in the candidate doc; the owner's 1/2
     normalization is an equivalent scaling of K);
     PSD audit: all leading principal minors of K and T nonnegative,
     the 4x4 minors strictly positive, the 5x5 determinants exactly 0
     (rank 4 = number of spectral atoms).
CO5  Erratum pins for the additive-branch wording (owner audit 3):
     b(n) = sum_{chi mod 5} chi(n) = 4*[n = 1 mod 5];
     b(1) = 4 != 1 = a_K(1);  b(5) = 0 != 1 = a_K(5);
     b(6) = 4 != 0 = a_K(6);
     in the ordered unramified prime-power list (2,3,4,7,8,9,11,13,16)
     the first index with b != a_K is 16, with agreement at 11.
CO6  Chain regression: lambda_1 recomputed by the same machinery lies in
     the rev1 pinned interval [23095708964233559, 23095708972138893]*10^-18.
```

## Code version

C-LI-COCYCLE-1_verifier.py, sha256 pinned below at freeze, single
execution after the pin. Python 3 stdlib only; no floats anywhere in the
file; directed integer intervals; exact cyclotomic and rational
arithmetic.

## Carrier / dataset

None. No zero lists, no prime tables. The exemplar is generated from the
declared architecture (the Lambda^2 torsion sector of the plenum step).
gamma, gamma_1, pi, log(4pi) enter only through elementary bracketed
series of the sealed normalization.

## Systematics

Conventions frozen: psi even with psi(0) = 0; t_m = psi(m+1) + psi(m-1)
- 2 psi(m); K = L T L^T without the factor 1/2 (owner's K differs by an
overall scaling, positivity unaffected); Euler-Maclaurin second order
with f'' = (2 ln x - 3)/x^3 one-signed for x >= 5, so the remainder bound
is int |f''| = |f'(N)| = (ln N - 1)/N^2 and |R| <= (ln N - 1)/(12 N^2);
Stieltjes convention zeta(1+t) = 1/t + gamma - gamma_1 t + O(t^2); scale
S = 10^18 with floor/ceil directed rounding; imported: sigma_2 identity,
Machin bracketing, harmonic bracket, Levy-Khintchine uniqueness (doc
text only, no machine check).

## Failure threshold

Any single exact assertion FAIL fires. Per the frozen negative-vector
discipline, a fired M_1 gate before G2-G4 closure indicts the machinery
or the imported sigma_2 identity, not RH. Thresholds never move.
