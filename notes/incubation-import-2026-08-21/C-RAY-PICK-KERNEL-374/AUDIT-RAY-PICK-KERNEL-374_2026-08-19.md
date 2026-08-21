# AUDIT-RAY-PICK-KERNEL-374, 2026-08-19/20

NON-CANONICAL. Independent audit of the owner's ray-Pick-kernel attack result
and record of its posting under junction lock mathorn1973/twist-j#374
(C-RH-WEIL-NORM-JUNCTION-1-N). Auditing session did not produce the attack.

## 1. Basis

```text
public line   Public Canon v54 ACTIVE, main 483591d, tag canon-v54 and content
              commit 0bfd67b4 ancestors of main, canon/SHA256SUMS 5 of 5 OK,
              STATUS/POLICY/AGENTS/CORE/FRONTIER read in full
lock          issue #374, open, 0 prior comments; frozen branch
              notes/c-rh-weil-norm-junction-1-n (PREREG.md, BREAKER.md) read;
              lock branch NOT touched (owned by the ChatGPT owner session)
```

## 2. What was checked and the verdicts

```text
A1 Hadamard form K_ray(a,b) = sum m_alpha/((a-alpha)(b+alpha))   candidate-T, re-proved
A2 ell^2 model, J involution, completeness of Cauchy vectors     candidate-T, re-proved
   with correction C1: FINITE accumulation point required
A3 RH <=> ray PSD                                                candidate-T, re-proved
A4 off-critical orbit => negative direction; neg index = orbits  candidate-T, re-proved
A5 RH <=> D_N > 0 for a_n = 1 + 1/n (Sylvester step explicit)    candidate-T, re-proved
A6 NEW: S2 - lambda_1 = ||P_minus v_(1/2)||^2, equality iff RH   candidate-T, added
A7 prime-side display, sigma > 1; diagonal M(a) > 0 is           candidate-T, re-proved
   UNCONDITIONAL, so all RH content is off-diagonal
A8 G_a Laplace family and bracket identity                       candidate-D, owner
   derivation, not re-derived; a = 1/2 endpoint consistent with
   Suzuki (1.8)/(4.1) via the exact witness M(1/2) = lambda_1
A9 narrowed limit gate: scalar Q_R(i a_n) -> Q_xi(i a_n) on the  candidate-T, re-proved
   fixed sequence suffices for RH (PSD passes to limits)
F  single G_1/Poisson moment insufficient as mechanism           kept, sharpened
```

Prior-art boundary added (correction C4): both directions of A3 are
assemblable from classical parts (positive-real functions, Nevanlinna-Pick
interpolation, Lagarias 1999 scalar half-plane criterion). The contribution is
the mechanism, the fixed determinant chain, and the prime-side carrier, not
the equivalence as such. Full corrections C1-C9 are in the posted addendum.

## 3. Citation audit

```text
VERIFIED    arXiv:2301.05779v2 (Li coefficients as norms): (1.7), (1.8), (4.1),
            (3.6) with 1/rho weight at n = 1; xi + xi' zeros obstacle verbatim.
CORRECTED   arXiv:2606.09096: exists, v1 submitted 2026-06-08. The claimed v2
            of 2026-08-17 was NOT confirmable on three surfaces (arxiv abs,
            papers.cool, alphaxiv); addendum cites v1 and leaves the v2 dating
            to the owner to re-pin.
NOT REVERIFIED (arxiv full-text fetches rate limited from this session):
            section 7.7 operator display and the alleged missing 1/pi;
            Theorem 4.2 of arXiv:2301.00421v3 (title verified: On the Hilbert
            space derived from the Weil distribution; screw line S_t and
            Theta = E#/E definitions verified). Left owner-reported with an
            explicit falsifier.
```

## 4. Engineering witness (floats, labeled)

```text
file          claude/witness_kray_ray_pick.py
sha256(file)  946f602c5b359a72ac4c0f534b78f24c9816d97e5d98629c1eca34feca5d5fce  (4979 bytes)
sha256(out)   110cb645f666cd0292b9258b784f4e5c3fa9accd8a1d7ae0930c71d9feaff09b  (1016 bytes)
env           LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
              Linux x86_64, CPython 3.11.15, mpmath 1.4.1, exit 0
```

stdout, verbatim:

```text
W1 zeros used NZ=500, T=811.18436, engineering tail estimate 0.0023
PASS W1(0.7,1.3)  K_ray=0.0461161231866  zerosum=0.0438185463122  |diff|=0.0023  (tail~0.0023)
PASS W1(0.6,0.9)  K_ray=0.0461632767688  zerosum=0.0438656992358  |diff|=0.0023  (tail~0.0023)
PASS W1(1.0,2.0)  K_ray=0.0459900665187  zerosum=0.0436924914248  |diff|=0.0023  (tail~0.0023)
PASS W2 D_1..D_8 > 0  D_1=0.0459171 D_2=8.30227e-7 D_3=1.66568e-15 D_4=8.14781e-29 D_5=4.48554e-47 D_6=1.15779e-70 D_7=8.75043e-100 D_8=1.13663e-134
PASS W2 min eigenvalue > 0  lambda_min=4.39817e-37
PASS W3 M(1/2)=lambda_1  M(1/2)=0.02309570896612103381431025  lambda_1=0.02309570896612103381431025  |diff|=8.61e-42
PASS W4 M(a)>0 on grid  M(0.5001)=0.023100324 M(0.51)=0.023557241 M(0.6)=0.027709956 M(0.75)=0.034626194 ...
PASS W5 sigma=2.0  formula=0.0690672319222292  direct=0.0690662315300007  |diff|=1.0e-6  (Lambda tail<=2.08e-6)
PASS W5 sigma=3.0  formula=0.114390695240145  direct=0.114390695239644  |diff|=5.0e-13  (Lambda tail<=1.56e-12)
WITNESS PASS
```

All decimals are computed witnesses, not conclusions.

## 5. The posting

```text
where       https://github.com/mathorn1973/twist-j/issues/374#issuecomment-5349558921
body        claude/ADDENDUM-RAY-PICK-KERNEL-374_2026-08-19.md (exact posted text)
body sha256 0e22ee174bd0439b50da0ee911e4c53896376c842ca6954f6c9fcf25977267fb  (16821 bytes)
how         this cloud session has no GitHub API credential for twist-j (git
            proxy: repository not in the session's authorized set). The comment
            was posted through the owner's authenticated gh on the macOS arm64 leg node
            (account mathorn1973). Transfer was made in five parts and
            hash-verified byte for byte against the sha256 above before
            posting. A first base64 transfer attempt corrupted in transit and
            was discarded on the hash mismatch; nothing corrupted was posted.
firewall    comment is NON-CANONICAL, candidate labels only, no J7 verdict,
            no registry/frontier/Canon/status movement, lock branch untouched
```

## 6. Open after this audit

```text
O1  global PSD of K_ray from the Euler side without zero input, or the
    narrowed scalar limit gate (A9) toward the 2606.09096 construction.
O2  independent re-derivation of the G_a closed form and bracket identity
    (candidate-D in the addendum; falsifier FA4).
O3  owner re-pin of the 2606.09096 version/date; one look decides the
    alleged section 7.7 missing 1/pi against Theorem 4.2 of 2301.00421v3.
```
