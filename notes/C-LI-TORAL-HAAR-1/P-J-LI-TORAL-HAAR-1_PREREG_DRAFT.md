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

The no-go chain and the forced-target identities, exactly as frozen in
C-LI-TORAL-HAAR-1.md sections 2-4:

```
theta_gamma = 2 arctan(1/(2 gamma));
sigma_xi = sum_{gamma>0} m_gamma/(gamma^2+1/4)
           (delta_{e^{i theta_gamma}} + delta_{e^{-i theta_gamma}});
sigma_xi_hat(n) = t_n;  sigma_xi(T) = 2 lambda_1;
lambda_n = (1/2) int |D_n|^2 d sigma_xi;
M_xi(eps) = (eps/pi)(log(1/(2 pi eps)) + 1) + O(eps^2 log(1/eps));
exact Haar cocycle on hyperbolic toral automorphism => lambda_n >= 0
  => RH => symmetrized spectral measure = sigma_xi (atomic, atoms off 1)
  => contradiction with countable Lebesgue spectrum off constants.
```

Claim under test: the standard toral Haar-Koopman realization of the Li
ladder is excluded, unconditionally as falsification of that realization.

## 2. Code

The accepted exact verifier for the probe is a successor of
`verify_toral_haar_nogo.py` (this directory; sha256
da3bee431cfe807e62d03156f1d443735cc749d22245c04f3e01ab54658ec406,
5/5 PASS), re-pinned fresh at probe registration per the owner's rule of
no retroactive formalization. Checks TH1-TH5: Cayley dictionary,
half-angle law, forced-measure dictionary on synthetic rational
multisets, character-orbit obstruction det(A^k - I) = 2 - tr(A^k) != 0,
accumulation-law calculus. Stdlib only; every assertion exact; floats
only as printed witnesses.

## 3. Carrier or data

None. Proof-first probe: the carrier class is the mathematical object
(hyperbolic A in SL_2(Z), Koopman on L^2(T^2, Haar)); all machine
instances are synthetic rational multisets and exact integer matrices.
No external dataset; no zero ordinates are consumed. An OPTIONAL
exploratory finite test to n = 32 (finite character truncations) is a
sanity check only and is NOT a gate.

## 4. Systematics

The imported classical inputs, named and held fixed: Li's criterion
(positivity => RH direction); Fourier uniqueness of finite positive
measures on T; the countable-Lebesgue decomposition of hyperbolic toral
Koopman operators; the Riemann-von Mangoldt count for the accumulation
remainder. The symmetrization discipline (sigma = mu_v + iota_* mu_v,
never "sigma = 2 mu_v" in general) per C-LI-COCYCLE-1 amendment 4.

## 5. Failure threshold

The probe FAILS if any TH assertion fails on the pinned re-run on either
architecture, or if a reviewer exhibits a gap in steps (a)-(e) of the
proof, or if an explicit exact Haar cocycle satisfying the premises is
produced. Thresholds do not move after the pin.

## 6. Action layer

L6 (measure statements about proposed realizations). No lift between
layers is claimed; any future lift needs its own named gate.
