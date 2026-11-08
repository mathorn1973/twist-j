# Primitive integer source-to-metric model

NON-CANONICAL, L1. Ownership issue:
https://github.com/mathorn1973/twist-j/issues/1640.

This probe adds an actual Hermitian-source term to a primitive integer K1
field transition. With m=324 and ell=(1,-1,0,0,0),

    P_next=C P-a(k) Q+2 chi(H,R) ell,
    Q_next=P, k_next=k+1,
    a(1)=324, a(k)=104976 for k>=2,
    h_k=P/(2*324^(k-1)),
    g_k(r)=diag(-1,1+h_k(r),1-h_k(r),1).

The source coefficient is read after the six Hermitian source phases.
A seventh phase advances the field. The full core has 38 integer
coordinates; bank and direction give 40. The exact image congruence and
positive account make domain-and-bank reflection a total bijection.

At the same word, common sufficient budget, and reached counter k=2,
opposite source signs produce a field difference ell/162. This response
disappears when the coupling is disabled. The first local formal run
passed, with raw-byte agreement of two separately written implementations.

## Read and reproduce

- PREREG.md freezes the carrier, choices, exact fixtures, falsifiers, and
  raw certificate grammar.
- PROOF.md gives the all-counter denominator, reversibility, signature,
  sharp-budget and prescribed-source action proofs.
- SOURCE.md identifies the actual Public Canon v103 bytes, non-canonical
  companions, and every new modeling choice.
- verify.py uses polynomial ring and matrix arithmetic.
- breaker.py independently uses direct integer-coordinate Hermitian gates
  and explicit field matrices; the primary launches it in a subprocess.
- FROZEN.sha256 commits the five prospective source files.
- EXPECTED.txt is the exact first formal stdout.
- RUN.md and RESULT.md describe execution custody and the scope earned.
- REVIEW.md records the actual scope of the team's pre-pin analytical and
  static implementation reviews.

From the repository root, using Python 3.12 and the standard library:

    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
      python3 probes/P-INTEGER-PRIMITIVE-SOURCE-METRIC-1/verify.py

Expected successful output ends with:

    CERTIFICATE_RESULT=PASS
    BREAKER_RAW_BYTES=IDENTICAL
    RESULT=PASS

The complete output must match EXPECTED.txt byte for byte. The unchanged
repository PR workflow performs this replay on both x86_64 and aarch64.

## Limits

The metric is proved Lorentzian for the twenty declared ready source/word
histories and their reversibly retraced prefixes. The unrestricted integer
carrier also contains degenerate metric readouts. The source functional,
dipole, strength, account and attenuation are explicit choices.

The quadratic action varies the metric, lapse and shift while holding
the source history fixed. A joint matter action, reciprocal backreaction,
native-U realization, physical clock or energy, full nonlinear general
relativity and a continuum limit remain separate obligations.
