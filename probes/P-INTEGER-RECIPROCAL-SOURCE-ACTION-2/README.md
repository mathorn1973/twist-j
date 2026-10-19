# Reciprocal integer source-metric action and coupling-selection model

NON-CANONICAL, L1. Ownership issue:
https://github.com/mathorn1973/twist-j/issues/1642.

This probe extends P-INTEGER-PRIMITIVE-SOURCE-METRIC-1 (Draft PR #1641) by
addressing the first two open obligations identified there:

1. **Coupling selection (Theorem B1):** Proves and audits that the source
   functional chi(H,R)=coeff_j((H-R)_01), the marked dipole ell=(1,-1,0,0,0)
   (up to sign), the factor 2, and the step-covariant attenuation 324^(-n) are
   the unique coupling quadruplet satisfying four explicit representation,
   support/zero-sum, primitive-parity, and step-covariance conditions (CS1-CS4).
2. **Reciprocal backreaction and joint action (Theorems B2-B5):** Couples the
   primitive field numerator P back into the Hermitian source during phase 6 via
   the unimodular shear S^(beta(P)) with beta(P)=((P_0 mod 2)-(P_1 mod 2)) +
   ((P_2 mod 3)-(P_4 mod 3)), preserving exact 38-coordinate core invertibility,
   the total funded bijection F^-1 = Rev F Rev with conserved E+b, the exact
   all-counter primitive denominator d_n=2*324^(n-1), the all-counter Lorentzian
   signature bound (-299/500 < h_n(r) < 499/500) across all ten canonical words
   and source seeds a in {-1,0,+1}, and simultaneous Euler-Lagrange stationarity
   of a single joint quadratic action A_joint with respect to all metric,
   lapse, shift, and source variables.

## Read and reproduce

- PREREG.md freezes the carrier, structural conditions, exact fixtures,
  falsifiers, and certificate grammar.
- PROOF.md gives the coupling-uniqueness, reciprocal-reversibility,
  all-counter primitive denominator, Lorentz-signature, and joint-action proofs.
- SOURCE.md identifies the actual Public Canon v103 bytes, non-canonical
  companions, consumed predecessor pin, and every new modeling choice.
- verify.py uses 8-coordinate integer Hermitian gates and explicit operator
  matrices.
- breaker.py independently uses polynomial-ring 2x2 Hermitian matrices,
  stencil evaluation, and Gaussian-elimination Green solvers.
- FROZEN.sha256 commits the five prospective source files.
- EXPECTED.txt is the exact first formal stdout.
- RUN.md and RESULT.md describe execution custody and the scope earned.
- REVIEW.md records the pre-pin analytical and static audit and predecessor
  disposition.

From the repository root, using Python 3.12 and the standard library:

    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
      python3 probes/P-INTEGER-RECIPROCAL-SOURCE-ACTION-2/verify.py

Expected successful output ends with:

    CERTIFICATE_RESULT=PASS
    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

The complete output must match EXPECTED.txt byte for byte. The unchanged
repository PR workflow performs this replay on both x86_64 and aarch64.

## Limits

The coupling-uniqueness theorem is conditional on the explicit axioms CS1-CS4.
The field-to-source backreaction functional beta(P) is a declared coarse-grained
parity-dipole link, and the joint action uses an adjoint multiplier p_n to
variation-encode the first-order source recurrence. Passing from the linear TT
sector to full nonlinear general relativity, native-U realization, and a
continuum limit remain separate obligations.
