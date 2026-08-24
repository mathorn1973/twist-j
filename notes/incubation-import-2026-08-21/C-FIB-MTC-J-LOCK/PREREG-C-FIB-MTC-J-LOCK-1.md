# PREREG C-FIB-MTC-J-LOCK-1

    candidate id   C-FIB-MTC-J-LOCK-1
    target line    public, mathorn1973/twist-j main
    authority      none. This is a candidate. It promotes nothing.
    layer          L1 (state). No lift to L2-L6 is claimed.
    basis          Public Canon v25, TAG canon-v25,
                   CONTENT_COMMIT b914755b422bf79a8be637993b2edaa12a4333f8,
                   CANON_SHA256 53fa5acc9f2d910b26293d5152d93deac6596abd012997c7ff195397d9e476bb,
                   CANON_BYTES 136831, canon/SHA256SUMS 5 of 5 OK.
    role           INDEPENDENT AUDIT of a forwarded third-party observation.
                   Not a rerun of the forwarded code path.

## 0. What is being audited

A forwarded session note asserts, at status H, that J is visible in the
Fibonacci modular tensor category through two channels: quantum dimension
d_tau = phi (modulus) and topological spin theta_tau = zeta_5^2 (argument),
with J = 1 + theta_tau, |sigma_1(J)| = 1/d_tau, and the weighted Gauss sum
1 + phi^2 theta_tau = D exp(2 pi i c / 8) at c = 14/5. It proposes the
Fibonacci category as the first target of a calibration lane.

This preregistration does not accept that framing. It tests whether the
relation is an observation (as claimed) or a derivation, and it tests whether
the relation distinguishes the golden fusion ring at all.

## 1. Equation

Work in Z[zeta_20], zeta_5 = zeta_20^4, zeta_10 = zeta_20^2, exact.
Write phi = -zeta_5^2 - zeta_5^3, J = 1 + zeta_5^2.

Imported, not derived here, and named as imports:

    I1  (Vafa)      topological spins in a modular tensor category are roots
                    of unity.
    I2  (Turaev;    p^+ p^- = D^2, where p^± = sum_a d_a^2 theta_a^{±1} and
        Bakalov-    D^2 = sum_a d_a^2.
        Kirillov)
    I3  (anomaly)   p^+ = D exp(2 pi i c / 8), c the topological central charge
                    mod 8.

Claims to be tested, each exactly:

    E1  fusion       the fusion matrix N_tau = [[0,1],[1,1]] has Perron-
                     Frobenius eigenvalue phi, and phi^2 = phi + 1 in Z[zeta_5].
    E2  forcing      for a UNITARY rank-2 modular category on the golden ring,
                     I2 forces 2 Re(theta_tau) = 1 - d_tau^2. With d_tau = phi
                     and I1 this admits exactly two solutions,
                     theta_tau in {zeta_5^2, zeta_5^3}, hence 1 + theta_tau
                     in {J, conj(J)}. The relation is DERIVED, not observed.
    E3  modulus      J conj(J) = 2 - phi = phi^-2, hence
                     (J conj(J)) d_tau^2 = 1 exactly.
    E4  ribbon       with R^{tau tau}_1 = zeta_5^3 and R^{tau tau}_tau
                     = -zeta_5^4, the ribbon sum
                     theta_tau = d_tau^-1 (R_1 + d_tau R_tau) equals zeta_5^2.
    E5  Gauss sum    p^+ = zeta_5^2 - zeta_5^4 exactly, and
                     p^+ = D zeta_20^7 with D = zeta_20 + zeta_20^-1
                     = 2 cos(pi/10), which is I3 at c = 14/5 mod 8.
                     No square root and no decimal enters the assertion.
    E6  shadow       the Galois-conjugate (non-unitary, Lee-Yang) solution
                     d = -phi^-1 gives theta in {zeta_5, zeta_5^4}; the four
                     modular categories on the golden ring therefore carry
                     spins {zeta_5^a : a = 1,2,3,4} and
                     {1 + theta} = the full Galois orbit of J, with
                     prod (1 + theta) = N(J) = 1.
    E7  axiom link   theta_tau = J - 1, hence theta_tau^3 = (J - 1)^3 = zeta_5.

## 2. Code

`verify_fib_mtc_j_lock.py` and `break_fib_mtc_j_lock.py`. Python standard
library only. Integer and Fraction arithmetic in Z[zeta_N] represented as
coefficient vectors modulo Phi_N. No float in any assertion. Run from the
working directory with
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.
Independent code path: the verifier is written from the fusion ring and the
imported MTC identities, not from the forwarded note's numeric witnesses.

## 3. Carrier or data

No experimental data. The carrier is the classification of modular tensor
categories on the fusion ring tau tensor tau = 1 + tau, and the SU(2)_k
(Temperley-Lieb-Jones) family for the counterexample scan.

## 4. Systematics

    S1  the imports I1-I3 are theorems about modular categories taken from the
        literature. They are NOT derived inside TWIST-J. Any claim resting on
        them inherits an external dependency and may not be labelled T-LOCK.
    S2  Fibonacci is the even part of SU(2)_3, not SU(2)_3 itself. The scan
        must record which family it covers and must not claim coverage of all
        modular categories.
    S3  the public registry already carries PHIBIT-NOT-TAU [F], fired:
        the physical reading of the phibit as the Fibonacci tau anyon is
        falsified, and only a named gate may reopen the physical reading.
        Nothing in this candidate may reopen it by implication. This candidate
        is confined to modular data. It asserts no physical identification.
    S4  the internal Canon v184 snapshot already carries norm(J)^2 = 2 - phi
        = phi^-2 at T inside T-VERB-TRANSPORT. The modulus half of the
        forwarded "two locks" is therefore not new evidence. Only the joint
        forcing is new.

## 5. Failure threshold

    F1  E2 fails if 2 Re(theta_tau) = 1 - d_tau^2 does not follow from I2 on
        the golden ring, or if the solution set for theta_tau is not exactly
        {zeta_5^2, zeta_5^3} under I1 and d_tau = phi.
    F2  E3, E4, E5, E6, E7 fail on any exact inequality in Z[zeta_20].
    F3  THE PRIMARY FALSIFIER. The condition
            |1 + theta_a|^2 = d_a^-2
        is claimed to be a discriminator. It is falsified as a discriminator
        if any modular category outside the golden fusion ring has a simple
        object a with d_a > 1 satisfying it. The scan covers SU(2)_k for
        n = k + 2 in 3..202, every simple object, exactly. A single hit with
        d_a > 1 outside (k, m) = (3, 3) fires F3 and the discriminator claim
        dies. Degenerate hits at d_a = 1 are reported, not hidden, and are
        counted as a REAL WEAKENING of the unqualified condition.
    F4  the rank-2 uniqueness sub-claim fails if the fusion ring
        tau^2 = 1 + m tau admits a solution of |1 + theta|^2 = d^-2 for any
        integer m other than m = 1.
    F5  scope failure. If the result is written anywhere as a physical
        identification of a TWIST-J object with the tau anyon, the candidate
        is void by collision with PHIBIT-NOT-TAU [F].

No threshold may move after this file is frozen. A fired falsifier is
archived, not deleted.

## 6. Action layer

    L1 only. On success the candidate proposes a mathematics-grade row about
    modular data over Q(zeta_5). It proposes NO physical row, NO dictionary
    row, and NO change to the two-forces reading. The p = 5 selection question
    is recorded as an open obligation, not answered.

## 7. Declared outcome classes

    upgrade    E2 holds: the forwarded H becomes a derivation, candidate-T for
               the implication, with I1-I3 named as external imports.
    deflate    the "two independent locks" reading is withdrawn: modulus and
               argument are one modular constraint with two faces, not two
               independent confirmations.
    F3 fires   the discriminator claim dies and the calibration-lane proposal
               loses its stated justification.
