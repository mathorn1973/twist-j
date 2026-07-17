# P-J-LI-TORAL-HAAR-1 preregistration

Status: PREREGISTERED CANDIDATE; FIRST FORMAL RUN PENDING REMOTE PIN READBACK

This document freezes one proof-first public no-go probe. It contains no
formal gate output and earns no scientific status. Formal execution is
forbidden until this exact revision and `verify.py` are committed, pushed,
and read back as one immutable preregistration pin.

## Public identity and action layer

```text
program:          J-LI
probe:            P-J-LI-TORAL-HAAR-1
public lock:      issue 50
owner:            A. M. Thorn
branch:           probe/P-J-LI-TORAL-HAAR-1
path:             probes/P-J-LI-TORAL-HAAR-1/
initial base:     7fe66e7ee8d02068c9717314988500c6022e73d6
action layer:     L6 measure/spectral statement, with the single named
                  M_J/Pillar-A toral specialization; no further layer lift
scientific state: candidate proof-first no-go and necessary conditional
                  spectral target only; RH and every replacement carrier
                  remain open
```

The authority base is Public Canon v6, tag `canon-v6`, activation commit
`6bb013bafb2d1c06fcb295fdbfce0f86198fd685`, content commit
`46f6412943bbd32bd3a686456c36612a1fc8fb3c`, Canon SHA-256
`5b810f0d7d36254d6968f72cd4cefe6956b772e0046ca41f0a9867b3818bb748`,
and Canon byte count 60697. The exact public input used by the named
specialization is the `J-STEP`/`CODEC-TR4` matrix action of `M_J`.

## 1. Equation

Use the Fourier convention

```text
nu_hat(n) = integral_T z^n d nu(z),
lambda_0 = 0, lambda_{-n} = lambda_n,
D_n(z) = sum_(k=0)^(n-1) z^k.
```

Under RH, enumerate positive ordinates of the nontrivial zeros as
`gamma > 0`, with multiplicity `m_gamma`, and define

```text
theta_gamma = 2 arctan(1/(2 gamma)),
sigma_xi = sum_(gamma>0) m_gamma/(gamma^2+1/4)
           (delta_(exp(i theta_gamma)) + delta_(exp(-i theta_gamma))).
```

The frozen target identities are

```text
t_n = lambda_(n+1) + lambda_(n-1) - 2 lambda_n,
sigma_xi_hat(n) = t_n,
sigma_xi(T) = t_0 = 2 lambda_1,
lambda_n = (1/2) integral_T |D_n|^2 d sigma_xi.
```

For

```text
M_xi(eps) = sigma_xi({exp(i theta): |theta| <= eps}),
```

the frozen accumulation statement is

```text
M_xi(eps) = (eps/pi)(log(1/(2 pi eps)) + 1)
            + O(eps^2 log(1/eps))        as eps -> 0+.
```

The positive existence hypothesis under attack is:

```text
d >= 1, A in GL_d(Z), no eigenvalue of A is a root of unity,
U_A f = f o T_A on L^2(T^d, Haar),
exists v such that
  ||sum_(k=0)^(n-1) U_A^k v||^2 = lambda_n for every n >= 1.
```

The expected decision is false. The named TWIST-J specialization is

```text
d = 4,
A = M_J = [[1,0,-1,1], [0,1,-1,0],
           [1,0, 0,0], [0,1,-1,1]],
spec(M_J) = {1 + zeta_5^(2k): 1 <= k <= 4},
moduli = {phi, phi, phi^-1, phi^-1}.
```

## Proof-first no-go frozen before execution

Assume the displayed realization exists. Its vector spectral measure
`mu_v` is positive, so every displayed norm square gives `lambda_n >= 0`.
Li's criterion then implies RH. On RH, the Cayley map

```text
rho = 1/2 + i gamma,
z_rho = (rho-1)/rho = exp(i theta_gamma)
```

has `|z_rho|=1` and

```text
1/(gamma^2+1/4) = 2(1-cos(theta_gamma)).
```

Taking second differences of the norm ladder forces every Fourier
coefficient of the symmetrized vector measure

```text
sigma = mu_v + iota_* mu_v,  iota(z) = conjugate(z),
```

to equal the corresponding coefficient of `sigma_xi`. Fourier uniqueness
for finite measures therefore gives `sigma = sigma_xi`. Only the
symmetrized measure is forced; no uniqueness of `mu_v` is claimed.

The toral character basis satisfies

```text
e_m(x) = exp(2 pi i <m,x>),
U_A e_m = e_(A^T m).
```

If a nonzero character orbit repeated, `(A^T)^k m=m` for some `k>=1`.
Then `1` would be an eigenvalue of `A^k`, so an eigenvalue of `A` would be
a root of unity, contradicting the carrier hypothesis. Every nonzero orbit
is consequently infinite. Each orbit span is a bilateral shift sector; by
the Fourier transform of `ell^2(Z)`, every vector measure on that sector is
absolutely continuous. Thus the Haar toral Koopman operator has no spectral
atom off the constant eigenvalue `1`.

But `sigma_xi` is purely atomic and has atoms away from `1`. This contradicts
`sigma = sigma_xi`. The no-go is unconditional: RH occurs only as a forced
intermediate consequence of the assumed realization. It is neither assumed
nor proved by the conclusion.

The specialization gate establishes independently that `M_J` lies in the
declared carrier class. The general all-dimensional theorem follows directly
from the no-root-of-unity hypothesis; it is not inferred from a finite loop or
from the `M_J` calculation.

## 2. Code

`verify.py` is the accepted exact audit for this directory. It is a freshly
adapted formal successor of the non-canonical preparation under
`notes/C-LI-TORAL-HAAR-1/`; that preparation and its stdout are not evidence
for this probe and are not retroactively formalized.

The verifier uses only the Python standard library and exact integer or
`Fraction` arithmetic. It reads no external data and writes no file. TH1
through TH9 are the nine theorem-skeleton gates:

```text
TH1  Cayley dictionary at exact rational fixtures.
TH2  exact half-angle algebra.
TH3  forced symmetrized-measure dictionary at a synthetic rational multiset.
TH4  exact M_J characteristic, determinant, trace, and CODEC-TR4 cross-tie.
TH5  exact modulus alternatives in Z[zeta_5] and Z[phi].
TH6  irreducibility and cyclotomic exclusion for charpoly(M_J).
TH7  exterior-square non-escape and the actual character action via M_J^T.
TH8  directed exact bracket for theta at synthetic gamma=1.
TH9  directed exact bracket for the accumulation leading term at eps=1/1000.
```

`X1` is a required finite exact exploratory witness, explicitly not a theorem
gate. It checks finite determinant loops for one cat map and for `M_J`. Its
failure still makes the audit exit nonzero, but its success is never counted
as a tenth theorem gate or as proof of the all-dimensional statement.

The process exits nonzero if any gate or required witness fails. Static
parsing is permitted before the pin; importing or executing the module is not.

## 3. Carrier or data

The proof-first carrier is every `A in GL_d(Z)`, `d>=1`, with no
root-of-unity eigenvalue, acting by the Haar Koopman operator on `T^d`. The
named specialization is exactly `A=M_J` in dimension four. There is no
external dataset and no zero-ordinate list. Synthetic rational zero multisets
and finite integer-matrix loops are audit fixtures only.

## 4. Systematics and declared imports

The following classical inputs are frozen imports rather than verifier
outputs:

- Li's criterion in both directions, with the standard Li normalization;
- convergence of the zero sum defining the finite measure `sigma_xi` on RH;
- Fourier uniqueness for finite measures on the circle;
- the unitary spectral theorem and its atom/eigenspace identity;
- the character basis of `L^2(T^d,Haar)` and the Fourier transform of the
  bilateral shift;
- the Riemann-von Mangoldt count with error `O(log T)` and Stieltjes partial
  summation;
- Gauss's lemma for monic integer polynomials;
- the fact that a root of unity of order `m` has minimal polynomial
  `Phi_m`, of degree `eulerphi(m)`;
- the elementary bound `eulerphi(m) >= sqrt(m/2)`, which confines
  `eulerphi(m)=4` to `m<=32`.

TH6 does not use an arbitrary coefficient search. With no rational root,
Gauss's lemma leaves a product

```text
(x^2+a x+b)(x^2+c x+d),  b d = 1.
```

The only constant cases are `(b,d)=(1,1)` and `(-1,-1)`. Since `a+c=-3`,
their linear coefficients would be `-3` and `3`, never the required `-2`.
The verifier then enumerates exactly the confined cyclotomic orders
`m<=32`, obtaining `{5,8,10,12}`, and compares all four polynomials.

For the accumulation statement, principal arguments are used and
`0<eps<min(1,pi)`. The cutoff is

```text
T_eps = 1/(2 tan(eps/2)) = 1/eps + O(eps).
```

No finite-epsilon interval is treated as proof of the asymptotic. TH8 and TH9
audit deterministic exact interval machinery only.

## 5. Failure threshold

The probe fails if any TH gate or X1 witness fails; if the proof admits a
nonconstant eigenfunction in the declared carrier; if `M_J` has a
root-of-unity eigenvalue; if an exact all-`n` Haar-Koopman realization in the
declared class is exhibited; or if a gap occurs in

```text
realization => Li positivity => RH => forced sigma_xi => toral contradiction.
```

For the asymptotic define

```text
R(eps) = M_xi(eps)
         - (eps/pi)(log(1/(2 pi eps)) + 1).
```

The asymptotic falsifier fires if a proof or exact sequence `eps_j -> 0+`
shows

```text
|R(eps_j)| / (eps_j^2 log(1/eps_j))
```

to be unbounded. A discrepancy at one finite epsilon is not a falsifier of a
big-O statement. Thresholds, imports, carrier scope, and the named
specialization do not move after the pin. Every fired falsifier is retained.

## 6. Action layer

This is an L6 measure/spectral no-go. It contains exactly one named transition
from the public algebraic `M_J`/Pillar-A step to the toral specialization
`T_J[x]=[M_J x]` on `T^4`; TH4 through TH7 gate that transition. No other
algebra-to-measure lift, decoder claim, physical realization, or replacement
carrier is inferred.

## Evidence posture

The proof in this preregistration is the proposed theorem-grade evidence for
the general no-go. The verifier audits the exact finite algebra,
specialization, and directed interval machinery; it is not a numerical proof
of Li's criterion, RH, Fourier uniqueness, or the Riemann-von Mangoldt
theorem. Cross-architecture agreement reproduces the audit and does not
strengthen the frozen mathematical scope.

## Environment and formal execution

```text
cd <repo root>
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-J-LI-TORAL-HAAR-1/verify.py
```

The first formal run occurs only after remote readback of the immutable pin.
It must run in a neutral aarch64 Linux environment. Its exact stdout becomes
`EXPECTED.txt`; `RUN.md` records neutral environment fields, pin and file
hashes, exit code, stderr and stdout byte counts, and stdout SHA-256. A later
GitHub x86_64 check must rerun the identical verifier byte for byte.
`RESULT.md` is added only after formal evidence exists.

## Pre-pin development disclosure

The non-canonical candidate, preregistration draft, verifier v1/v2, and
non-formal outputs in `notes/C-LI-TORAL-HAAR-1/` were used to discover and
break the proposal before this freeze. They carry no public status. This
formal copy fixes the formal identity, failure exit, TH6 proof boundary,
general-theorem wording, nine-gate/X1 split, asymptotic falsifier, and named
action-layer transition. It has not been executed before remote pin readback.

## Out of scope, explicitly

- no proof or numerical test of RH;
- no unconditional existence assertion for `sigma_xi` outside the frozen
  necessary RH-conditional chain;
- no uniqueness of the unsymmetrized vector measure `mu_v`;
- no exclusion of non-Haar, non-Koopman, infinite-dimensional, boundary,
  scattering, or enlarged carriers;
- no construction of a replacement realization;
- no closure of `J-LI-MOMENT-BRIDGE` or any Weil-positivity route;
- no registry, frontier, Canon, fold, release, or tag edit in this probe.

Any wider statement requires a separate ruling, proof, probe, or later sealed
Canon fold.
