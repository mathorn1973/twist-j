# P-J-LI-TORAL-HAAR-1. Preregistration DRAFT

```
STATUS:      DRAFT. BLOCKED-ON-OWNER-CLAIM. NON-CANONICAL.
             Per POLICY.md a formal probe needs the owner to claim the
             named probe in a public issue, a probe/P-J-LI-TORAL-HAAR-1
             branch, and a NEW pin of PREREG.md and verify.py BEFORE any
             formal gate execution. Nothing here is that pin; no formal
             gate was executed on this draft.
SOURCE:      notes/C-LI-TORAL-HAAR-1/ (candidate document and verifier)
```

The six frozen fields, drafted:

## 1. Equation

The Fourier convention is `nu_hat(n) = int_T z^n d nu(z)`. The no-go
chain and forced-target identities are exactly:

```
theta_gamma = 2 arctan(1/(2 gamma));
sigma_xi = sum_{gamma>0} m_gamma/(gamma^2+1/4)
           (delta_{e^{i theta_gamma}} + delta_{e^{-i theta_gamma}});
sigma_xi_hat(n) = t_n;  sigma_xi(T) = 2 lambda_1;
lambda_n = (1/2) int |D_n|^2 d sigma_xi;
M_xi(eps) = (eps/pi)(log(1/(2 pi eps)) + 1) + O(eps^2 log(1/eps));
d >= 1, A in GL_d(Z), and spec(A) contains no root of unity
  => U_A on L^2(T^d,Haar) has no eigenvalue off 1
  => no v can satisfy ||sum_{k<n} U_A^k v||^2 = lambda_n for all n.

Pillar A: A = M_J, spec(M_J) = {1 + zeta_5^(2k): 1 <= k <= 4},
          with moduli {phi, phi, phi^-1, phi^-1}.
```

Exact positive claim under test: there exists v in L^2(T^4,Haar) realizing
the complete Li ladder under U_{M_J}. Expected mathematical result: false.

The proof-first gates are: forced symmetrized-measure dictionary; Fourier
uniqueness and convergence; the root-of-unity-free toral point-spectrum
theorem; exact M_J/Pillar-A specialization; the contradiction; and the
Riemann-von Mangoldt Stieltjes remainder for the accumulation law.

## 2. Code

The formal exact verifier is a freshly pinned successor of
`verify_toral_haar_nogo.py` (this directory; sha256
da3bee431cfe807e62d03156f1d443735cc749d22245c04f3e01ab54658ec406,
5/5 PASS), re-pinned fresh at probe registration per the owner's rule of
no retroactive formalization. Checks TH1-TH5: Cayley dictionary,
half-angle law, forced-measure dictionary on synthetic rational
multisets, character-orbit obstruction det(A^k - I) = 2 - tr(A^k) != 0,
accumulation-law calculus. Stdlib only. A finite cat-map loop is labeled
only as an exploratory witness; the all-k and all-d statement is
proof-first. The successor additionally pins exact M_J characteristic
data and algebraic modulus alternatives phi and phi^-1. Float atan/log
witnesses are excluded from byte-pinned gate stdout or replaced by
deterministic directed intervals. Every asserted gate value is exact.

## 3. Carrier or data

Proof-first carrier class: A in GL_d(Z), d >= 1, with no root-of-unity
eigenvalue, and U_A the Koopman operator on L^2(T^d,Haar). The named
TWIST-J specialization is d = 4, A = M_J, T_J[x] = [M_J x]. No external
dataset and no zero ordinate list is consumed. Synthetic rational zero
multisets and finite integer-matrix instances are audit fixtures only and
do not prove the analytic theorem.

## 4. Systematics

Frozen conventions and imports: lambda_0 = 0 and the standard Li
normalization; nu_hat(n) = int z^n dnu(z); sigma = mu_v + iota_* mu_v
with iota(z) = conjugate(z); N(T) counts positive zero ordinates with
multiplicity; principal argument and 0 < eps < pi in M_xi(eps); Li's
criterion; Fourier uniqueness; the unitary spectral-theorem
atom/eigenspace identity; and the Riemann-von Mangoldt count. The toral
point-spectrum obstruction and M_J specialization are proved inline, not
imported. No countable-Lebesgue decomposition is needed for the no-go.

## 5. Failure threshold

The probe FAILS if any exact pinned assertion fails; the Fourier-orbit
proof admits a nonconstant eigenfunction in the stated class; M_J has a
root-of-unity eigenvalue; an exact all-n Haar-Koopman cocycle for U_{M_J}
is exhibited; a gap is found in realization => Li positivity => RH =>
sigma_sym = sigma_xi; or the normalized accumulation remainder is
unbounded along eps -> 0+. A single finite-eps discrepancy is not a
falsifier of the asymptotic without a separately frozen explicit constant
and range. Thresholds do not move after the pin.

## 6. Action layer

L6 (measure statements about proposed realizations). No lift between
layers is claimed; any future lift needs its own named gate.
