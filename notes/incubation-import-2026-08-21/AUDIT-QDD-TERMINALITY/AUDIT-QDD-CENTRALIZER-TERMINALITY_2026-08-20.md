# AUDIT: the terminality bifurcation of P-QDD-J-CENTRALIZER-TERMINALITY-1

```text
Status     NON-CANONICAL independent audit of the owner-forwarded bifurcation
           report. No authority, no repo edit, no registry motion, no fold.
           O2 stays open, O1 untouched, SAMPLING NOT PROVIDED.
Session    AUDIT-QDD-CENTRALIZER-TERMINALITY, 2026-08-20.
Basis      Public Canon v56 ACTIVE. Probe merged to main by PR #462, merge
           commit 4ed6cb72; origin/main has since advanced to d525da09 by an
           unrelated probe merge; the probe directory and canon/ are
           byte-identical between the two commits (checked).
Prereg     PREREG-AUDIT-QDD-TERMINALITY-1.md, sha256 d479d89927fa3b42cb48b6f
           009158bda5469bb6064bf666f46950f001b9a21d0, frozen 17:35:41Z before
           the run.
Layer      L4 apparatus/support only, matching the probe.
Verdict    the handed report is faithful to the sealed record; the whole
           chain re-verifies by fresh code, 32/32; the sealed verifier
           reproduces byte-identically; zero findings; one added reduction
           sharpens the O2 target to a single class-level equation.
```

## 1. Report against the sealed record

Every checkable claim of the forwarded report matches the sealed probe:
decision BIFURCATION-PASS with 14/14 exact gates; one formal execution, exit
zero, empty stderr, stdout byte-identical to EXPECTED.txt; two public
architecture legs green; merge into main by merge commit 4ed6cb72; canon,
registry, frontier, and STATUS untouched by the branch (the merge adds only
the six probe files). The report's labeling [candidate-T] is correct in the
registry sense: the probe is sealed public evidence, but the three proposed
rows (APPARATUS-CLASS, NONSELECTION, TERMINALITY-SELECTION) exist only as a
later-fold ceiling; nothing is registered yet.

## 2. Independent verification (fresh code, no import from the probe)

Own Fraction matrix kernel; M_J rebuilt from the axiom step
(a,b,c,d) -> (a-c+d, b-c, a, b-c+d); target effects compared LAST.
All of the following re-verified exactly, 32/32 PASS:

```text
QA1 [candidate-T]  D = M_J - I, D^5 = I, D^T G D = G; simplex sum zero, Gram
    4/5 and -1/5, u_2 = -one; all twenty affine maps, group law on all four
    hundred pairs, G-orthogonality, rho(1,1) = D; stabilizer averages P_k
    rank 1 with image Q u_k, Q_k rank 3; g_k of order four with trace
    certificates (0, 0, 0, 4) pinning the characteristic polynomial
    x^4 - 1 = (x-1)(x+1)(x^2+1); the full R, C, J multiplication table at
    every token, J^2 = -C, J^sharp = -J; the centralizer as a 48-equation
    rational system has nullity exactly three at every token with {R, C, J}
    a basis; affine transport across tokens for all twenty maps.
QA2 [candidate-T]  effect equation exact on the rational circle; pairwise
    physical distinctness T(t) != +-T(u) on nine sampled t; Kraus
    completeness and zero cross term; ordinary repeatability Q T = T for
    every member; the four self-adjoint involutive members each satisfy
    T^2 = Q and reduce to exactly two physical classes [Q] and [R - C].
QA3 [candidate-T]  the mixed-line witness w_R + w_C is moved by every
    sampled non +-Q member and fixed as a line by +-Q; strict idempotence
    T^2 = T holds in the class exactly at T = Q.
QA4 [candidate-T]  target comparison last: P_2 = E_low = (1/4) one one^T and
    Q_2 = E_high; every sampled member realizes the frozen effects at k = 2.
QA5 [reproduction]  all four sealed files match the RUN.md pin hashes and
    the sealed verifier reproduces byte-identically on this platform
    (x86_64, same architecture class as the sealed local leg).
```

The written quantifier steps of the sealed prereg (primary decomposition,
scalar lemma for line-preserving maps, completeness of the rational circle)
were read and re-derived; they are sound. The scalar lemma is certified here
by exact witnesses on every sampled member rather than re-quantified.

## 3. Added reduction: the O2 gap is one equation

```text
Q6 [candidate-T, machine-checked]  Inside the frozen class,
    T^2 = +T or T^2 = -T   holds exactly for T in {+Q, -Q}.
```

In centralizer coordinates: T^2 has coordinates (e^2, z^2) with z = r + s i
on the rational circle; e^2 = 1 always; the plus case forces e = 1, z = 1;
the minus case forces e = -1, z = -1; both land in the single physical class
[Q]. Under the registered post-state equivalence K ~ L iff K = +-L, this is:

```text
T^2 ~_post T   if and only if   [T] = [Q]  (the Lueder class).
```

Consequences, stated carefully:

```text
1  The premise needed for Lueder selection at the physical-class level is
   strictly weaker than both sealed positive-route conditions. Ray
   terminality quantifies over every vector line; strict idempotence demands
   the exact algebraic identity T^2 = T. The class-level equation
   T^2 ~_post T quantifies over nothing: it is one equation between two
   instruments, the single write and the double write.
2  The negative-route survivor [R - C] is precisely a non-terminal
   involution: (R - C)^2 = Q, and Q is not +-(R - C). Repetition brings it
   back to the projection after TWO writes, never after one. This locates
   exactly where the repeatability intuition fails: at the sign and
   composition bookkeeping, not at outcomes.
3  The probe's closing question ("why must repeated reading be terminal and
   not merely repeatable") can therefore be narrowed further, to:

       why is the double write the same post-state event as the single
       write, that is, why does T^2 ~_post T hold physically?

   A write-once record register makes the two events carry identical
   records; what remains to be derived from the architecture (decoder
   one-wayness, record memory, no-feedback) is that identical records force
   post-state equivalence of the instruments. That derivation is O2 and it
   remains open. This audit adopts nothing and opens no lane; the reduction
   only shrinks the bridge that a future typed public gate must build.
```

## 4. Findings

None. QF1 to QF4 all silent. One boundary note, not a defect: the finite-t
rational-circle parametrization misses the member (e, r, s) = (1, -1, 0),
which corresponds to t at infinity; the sealed prereg states its injection
for finite t and is correct as written.

## 5. Run record

```text
order        prereg frozen 2026-08-20T17:35:41Z; static compile only before;
             one formal run; no threshold moved; stdout captured whole.
environment  LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
             TZ=UTC; Linux x86_64; CPython 3.11.15. Single platform,
             candidate labels only.
prereg       PREREG-AUDIT-QDD-TERMINALITY-1.md
             sha256 d479d89927fa3b42cb48b6f009158bda5469bb6064bf666f46950f001b9a21d0  (5884 B)
program      audit_qdd_centralizer_1.py
             sha256 cdeb1ee739dd4ae962cb75c23e39b596240147656a3655eba252e274646794aa  (15013 B)
stdout       audit_qdd_centralizer_1.stdout.txt, 32/32 PASS, exit 0,
             stderr empty
             sha256 f997225df4a73c29bd3ee4209792089da2ec3064f8571c4833970588834e34cc  (2181 B, 33 lines)
sealed pins  PREREG 3274806f.., verify.py 992f1bcc.., exact_matrix.py
             12b87e67.., EXPECTED.txt fc40a456..: all matched in the clone;
             sealed verifier rerun byte-identical, exit 0.
```

## 6. Scope firewall

L4 only; candidate grades only; single platform. Nothing here closes O2,
touches O1, produces events or sampling, or exceeds the sealed probe's frozen
class. The reduction in section 3 is a statement about the frozen class and a
proposal about how to phrase the missing premise; it is not a claim that the
public architecture implies terminality.
