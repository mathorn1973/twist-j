# AUDIT C-FIB-MTC-J-LOCK-1

Independent audit of a forwarded observation that J is visible in the
Fibonacci modular tensor category. NON-CANONICAL. Candidate. Promotes nothing.

    date            2026-07-27
    candidate id    C-FIB-MTC-J-LOCK-1
    target line     public, mathorn1973/twist-j main
    layer           L1. No lift to L2 through L6 is claimed.
    role            independent audit and break attempt, not a rerun

## Currency gate

    STATE            ACTIVE
    CANON            Public Canon v25
    AUTHORITY        mathorn1973/twist-j main
    TAG              canon-v25            ancestor of main: yes
    CONTENT_COMMIT   b914755b422bf79a8be637993b2edaa12a4333f8   ancestor: yes
    CANON_SHA256     53fa5acc9f2d910b26293d5152d93deac6596abd012997c7ff195397d9e476bb
    CANON_BYTES      136831               measured: 136831, match
    canon/SHA256SUMS 5 of 5 OK
    clone head       ef1d2d917486dfb15cba3a81bd2309183c57f572

Internal line not reached this session. The v184 snapshot pin is quoted from
the project contract and is NOT independently confirmed here.

## Pins

    PREREG-C-FIB-MTC-J-LOCK-1.md        b536d7a154ee28e89152767060ce28b4790b428927d5f904c74052acfabd8a74
    verify_fib_mtc_j_lock.py            42210ae778a3be037404b57727c72190f154d0fa4d12f0e7eb484c9b2e81e4d9
      stdout                            dff7ccd2420f4de0ab9967d59fb69ae811f71b37f21460adfa19f2735acbaa77
    break_fib_mtc_j_lock.py             1dbe1c1c20ebb621293fb86a453af7fef0effe61a0bf3061669fd5caa21a0e49
      stdout                            b06de3b155e4274d1fc3cf9058b5d9f6861958bb81082ca5f858aac7b921f815
    amend1_break_p11_counterexample.py  a2768271e9019b9516b3060daa5ac37b990a93fcbd085c2ca3dce1dbfd5448ab
      stdout                            7df9e08341631cc933fe4c36d21761cb359cad70229451f51c03706551492efe

    platform  Linux x86_64, CPython 3.11.15, stdlib only, exact arithmetic.
    Single architecture. Not two-platform. Nothing here is computation-grade T.

## VERDICT, falsification first

    FIRED     F3, the primary falsifier. The double lock does NOT select p = 5.
              A second solution exists at p = 11 and is confirmed by two
              independent algebraic routes.
    UPGRADED  the forwarded H is not an observation. It is a DERIVATION.
              candidate-T for the implication, conditional on named imports.
    DEFLATED  "two independent locks" is withdrawn. There is one modular
              constraint with two faces.
    BLOCKED   any physical reading collides with PHIBIT-NOT-TAU [F], already
              fired in the public registry. This candidate asserts none.

## 1. What was upgraded

The forwarded note reports, at H, that J = 1 + theta_tau with theta_tau the
topological spin of the Fibonacci tau anyon, and that the modulus of J is the
inverse quantum dimension. Both are true. Neither is an observation.

Rank 2, simples {1, tau}, d_1 = 1, theta_1 = 1. Write p^± = sum_a d_a^2
theta_a^{±1} and D^2 = sum_a d_a^2. The imported modular identity
p^+ p^- = D^2 reads

    (1 + d^2 theta)(1 + d^2 theta^-1) = 1 + d^2

and, cancelling d^2, becomes

    theta + theta^-1 = 1 - d^2.

The fusion rule tau tensor tau = 1 + tau gives d^2 = d + 1, so the right side
is -d. In the unitary branch d = phi, so theta is a root of

    x^2 + phi x + 1 = (x - zeta_5^2)(x - zeta_5^3).

A monic quadratic has exactly two roots. Therefore

    theta_tau in {zeta_5^2, zeta_5^3}   and   1 + theta_tau in {J, conj J}.

The axiom is forced by one integer fusion rule plus modularity. No choice of
the author enters, and Vafa's theorem is not even needed: the quadratic does
the work. This is the real content, and it is stronger than what was claimed.

Consequences, all verified exactly in Z[zeta_20], 24 of 24 assertions passing,
no float in any assertion:

    theta_tau = J - 1,  and  (J - 1)^3 = zeta_5, the axiom-block identity
    J conj(J) = 2 - phi = phi^-2,  hence  |J|^2 d_tau^2 = 1 exactly
    1 - J = -zeta_5^2 is a primitive tenth root of unity
    D = zeta_20 + zeta_20^-1 = 2 cos(pi/10) is an algebraic integer of Z[zeta_20]
    p^+ = zeta_5^2 - zeta_5^4 = D zeta_20^7, which IS the anomaly statement
      p^+ = D exp(2 pi i c / 8) at c = 14/5, with no square root and no
      decimal anywhere in the assertion
    the entire central-charge claim collapses to  1 + phi zeta_5^2 = -zeta_5^4

The Galois shadow is exact and complete. The second root of d^2 = d + 1 is
-phi^-1, the non-unitary Lee-Yang branch, and the same forcing gives
theta in {zeta_5, zeta_5^4}. The four modular categories on the golden fusion
ring therefore carry spins exactly {zeta_5^a : a = 1, 2, 3, 4}, so

    {1 + theta} over the four categories = the full Galois orbit of J,

and the product over the orbit is N(J) = 1. The unit axiom N(J) = 1 is the
closure of the spin data of the complete classification. That reading is new
here and is the most useful thing this audit produced on the positive side.

## 2. What was deflated

Three framings in the forwarded note do not survive.

The "two independent locks" reading is wrong. Modulus and argument are not two
independent confirmations. Given the fusion rule, modularity fixes
theta + theta^-1, which fixes the argument, and the modulus follows from the
same equation. One constraint, two faces. Calling it two locks double counts
the evidence. The correct statement is stronger anyway: it is a derivation.

The "unweighted Gauss sum" framing adds nothing. In a rank-2 category
sum_a theta_a is trivially 1 + theta_tau because the unit has spin 1. It is an
invariant, but it carries no theorem. The weighted sum p^+ is the object with
content, and its identity is E5 above.

The modulus half is not new evidence. The internal Canon v184 snapshot already
carries norm(J)^2 = 2 - phi = phi^-2 at T inside T-VERB-TRANSPORT. Only the
joint forcing with the spin is new.

## 3. What was falsified

The forwarded note proposes the Fibonacci category as the discriminator for J
over phi and as the best first target of a calibration lane. The implied
discriminator is

    LOCK(a):   |1 + theta_a|^2 d_a^2 = 1.

Three attacks were run against it.

B1, exhaustive and symbolic over ALL rank-2 fusion rings tau^2 = 1 + m tau.
Working in Z[m][d] modulo d^2 - m d - 1:

    d^4 - 3 d^2 + 1 = (m^2 - 1) d^2   identically.

So LOCK holds if and only if m^2 = 1, that is m = 1, the golden ring. Within
rank 2 the golden ring is unique. This part survives and is exact.

B2, the abelian counterexample. At d = 1 the condition reads
theta + theta^-1 = -1, so theta is a primitive cube root of unity. The Z_3
anyon model (SU(3)_1) realises it: three simples of dimension 1, spins
{1, zeta_3, zeta_3}, p^+ p^- = 3 = D^2, a genuine modular category, and
LOCK holds. The UNQUALIFIED condition is therefore not a discriminator and is
falsified as stated. It must carry the non-degeneracy clause d_a > 1.

B3, the exhaustive scan that fired the primary falsifier. The SU(2)_k
(Temperley-Lieb-Jones) family, n = k + 2 from 3 to 202, every simple object,
20300 pairs, each decided exactly. Each pair is first certified nonzero by a
ring homomorphism Z[zeta_{8n}] to F_p with p = 1 mod 8n, and every apparent
zero is re-decided by exact reduction modulo Phi_{8n}. Two nontrivial hits:

    k = 3   n = 5    m = 3   (j = 1)   h = 2/5    the Fibonacci object
    k = 9   n = 11   m = 5   (j = 2)   h = 6/11   THE COUNTEREXAMPLE

The second hit was confirmed by an independent second algebraic route
(product-to-sum, linear in the roots of unity, not the squared-binomial
identity the scan used). Both routes agree. The solution branch has the closed
form 4n = m^2 + 4m - 1 with 4m - m^2 + 1 = ±4, which admits exactly m = 3 at
n = 5 and m = 5 at n = 11.

The counterexample is structurally identical to the p = 5 case:

    the object      j = 2 in SU(2)_9, quantum dimension sin(5 pi/11)/sin(pi/11)
    its spin        theta = zeta_11^6
    the analogue    J_11 = 1 + zeta_11^6
    the unit        N(1 + zeta_11^a) = Phi_11(-1) = 1, a unit of norm 1
    the lock        |J_11|^2 d^2 = 1, exactly

Two further defences were tried and both failed.

The unit property does not select 5. Phi_p(-1) = 1 for every odd prime p, so
1 + zeta_p^a is a norm-1 unit for every p. Checked for p in
{5, 7, 11, 13, 17, 19, 23}.

Orbit completeness does not select 5 either. At p = 5 all four Galois
conjugates of J satisfy LOCK against a golden-ring quantum dimension, 4 of 4.
That looked like a residual distinction. It is not: at p = 11 all ten Galois
conjugates of 1 + zeta_11^6 are realised as inverse quantum dimensions in the
Galois family of SU(2)_9, 10 of 10.

    What survives is MINIMALITY and nothing else. p = 5 is the smaller of
    exactly two solutions in the scanned family. It is not the only one.

Scope, stated so it cannot be overread. The scan covers SU(2)_k for n up to
202 and all rank-2 fusion rings. It does not cover higher-rank non-TLJ modular
categories. It therefore cannot claim, and does not claim, that p = 5 is
forced, and it equally cannot claim that p = 11 is the only rival. There may
be more.

## 4. Collision, and the scope fence

The public registry carries, at row PHIBIT-NOT-TAU [F]:

    fired: the phibit fusion ring is the group ring of Z_5 with five
    invertible simples of dimension 1, while the Fibonacci ring has two
    simples with tau tau = 1 + tau and dimension phi; the dead branch is
    archived and only a named gate could reopen the physical reading.

Nothing in this audit reopens it. Everything above is a statement about
modular data over Q(zeta_5), not about any TWIST-J object being a tau anyon.
The distinction matters and is easy to lose: the audit confirms that the two
channels of J are jointly forced by an integer rule, and it confirms nothing
at all about the physical dictionary. The Fibonacci category assigns the
modulus to a quantum dimension and the argument to a topological spin. Neither
is gravity and neither is electromagnetism. A calibration against this
category therefore tests the ALGEBRA of the two-projection claim and leaves
the PHYSICAL half of that claim entirely untouched.

## 5. Effect on the calibration lane proposal

The proposal in claude/NADHLED-PREKLAD-DO-J_2026-07-27.md names the Fibonacci
modular tensor category as "the discriminator for J over phi" and "the single
highest-value target in the demonstration set". That justification is now
falsified as written and must be re-scoped.

    keep     Fibonacci as a calibration target for the ALGEBRA. The forcing in
             section 1 is exact, it is a derivation, and it does discriminate
             J over phi in the narrow sense that phi fixes only the modulus
             while theta_tau fixes the whole of J.
    drop     the claim that it discriminates p = 5, or that it supports the
             two-forces reading. It does neither.
    add      SU(2)_9 at j = 2 as a required companion target. Any calibration
             lane that presents p = 5 as forced must say why p = 11 with
             J_11 = 1 + zeta_11^6 is not an equally good universe. That is now
             a concrete, named, checkable obligation rather than a vague one.

## 6. Registry action: NONE PROPOSED

Superseded 2026-07-27 by owner directive: close live rows, open no new
branches at this phase. An earlier draft of this section proposed two rows,
FIB-MTC-J-FORCING [H] and PENTIC-SELECTION [O]. Both are withdrawn. The
reasoning for the withdrawal is stronger than the directive alone, and is
recorded here so it is not relitigated.

Nothing in this audit discharges a live row. The public registry carries 3 H
rows (NS-TILT, OBSERVER-WRITE-PORT, LAMBDA-COCYCLE-ANGLES) and 23 O rows.
This work touches none of them.

Nothing in this audit is new to the canon either. Section 1, "The axiom and
the two projections", already carries

    J-PROJECTIONS [T]   in the principal archimedean embedding,
                        J = 1 + zeta_5^2 has modulus 1/phi and principal
                        argument 2 pi/5

which is exactly what the modulus and argument results of this audit
reproduce. J-PROJECTIONS is already at T, and the public series carries no
T-LOCK by convention, so there is no grade above it to move to. The forcing
derivation of section 1 improves the PROVENANCE of a row that is already at
the top of the public ladder. Provenance is not a status, and the registry has
no field for it. There is therefore no registry move available, and inventing
one would be a new row purchased with no gain.

The physical fence is already correct without help from this audit.
AXIOM-PROJECTION-DICTIONARY is [D] and states "with no uniqueness claim". The
scoping warning of section 4 is a warning the public canon already honours.

PENTIC-SELECTION is withdrawn as a registry row and kept as a hazard recorded
in this note only. Registering it would add a 24th open obligation, that is, a
public commitment to discharge it, during a phase whose purpose is to shrink
that inventory. A known weakness recorded in a NON-CANONICAL note blocks
nobody and commits nobody. The p = 11 rival is stated in section 3 and that is
where it stays until the program is opening branches again.

The single canon-surface defect this audit did find is hygiene, not science,
and is recorded in section 8.

## 7. What was tried and did not break it

Recorded for the honest-attempt requirement. The forcing in section 1
withstood: an attempt to find a third root of x^2 + phi x + 1 (a monic
quadratic has two, the attempt is void by construction); an attempt to break
the ribbon route by using the R-symbols rather than modularity, which gives
the same theta_tau = zeta_5^2 through a different identity; an attempt to
break the anomaly claim by branch ambiguity in the square root, defeated by
writing D = zeta_20 + zeta_20^-1 so that no square root ever appears; and an
attempt to find a rank-2 fusion ring other than the golden one satisfying
LOCK, closed exhaustively and symbolically in B1.

The discriminator claim did not withstand B2 and B3 and is falsified.

## 8. The one canon-surface defect found

canon/CANON.md, section 11, carries the sentence

    The Fibonacci category with central charge c = 14/5 is mathematical
    background; its physical reading fired: ...

The clause before the semicolon carries NO status label and has no backing row
in canon/REGISTRY.tsv. Public conventions require that every claim carries a
label, and it sits inside a hashed normative file in a section that is
otherwise labelled throughout (PHIBIT-NOT-TAU [F], PENTIT-ROOT-FACTS [T],
PENTIT-ROOT-READING [D], MAGIC-PRIME-GATE [T], QUBIT-FROM-F5 [T],
BELL-MAGIC-BOUNDARY [T]).

The fired row it introduces does not need it. The PHIBIT-NOT-TAU proof is a
finite counting argument about invertible simples and is complete without any
statement about the central charge.

    recommended   delete the clause. Deleting removes an unlabelled claim and
                  adds nothing, which is the correct direction in a closing
                  phase.
    alternative   label it and back it with the exact identity of section 1,
                  p^+ = zeta_5^2 - zeta_5^4 = D zeta_20^7 with
                  D = zeta_20 + zeta_20^-1. This is the integer form of
                  c = 14/5 and removes the only decimal in the sentence. It
                  costs a new registry row, so it is the worse option now.
    cost          any change to CANON.md is a sealed integer-versioned fold
                  with new hashes. Do NOT spend a fold on this alone. Carry it
                  as a rider on the next fold that happens for another reason.
