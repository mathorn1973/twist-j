# LI-COCYCLE LANE. Consolidation, 2026-07-16. The single source of truth.

```
PURPOSE:   the lane grew three working lines, several unpushed branches, and
           artifacts scattered over the project, the owner's Library, two
           local clones, and one defective archive. This document is the one
           map. Where it conflicts with memory, this document wins; where it
           conflicts with a repository head, the repository wins.
AUTHORITY: none (project doc). Public authority: mathorn1973/twist-j main,
           STATE ACTIVE, Public Canon v6, tag canon-v6, head 6bb013ba.
REV4:      SUPERSEDED AS THE LANE MAP. The current map is
           notes/j-li-schoenberg-2/LI-COCYCLE-LANE_CONSOLIDATION_2026-07-16.md
           (manifest-pinned). Sections 1-9 below are kept as the historical
           record; the REV4 addendum (section 10) lists the corrections and
           the public branch topology that supersede them. Known errata in
           the body are marked inline with "REV4:".
```

## 1. The consolidated claim ledger (after owner verdicts 1-4)

```
PENTAGON-NORMALIZATION          candidate-T; G0 publicly reproduced
                                (probes/P-PENTAGON-WEIL-1, two architectures,
                                stdout f0423685...97fe; draft PR #42 unmerged
                                by design; fold owner's call)
J-WEIL-EQUIVALENCE              candidate-T conditional on the five frozen
                                Weil conventions (G2 freeze still pending)
J-LI-CND-EQUIVALENCE            T (owner lane; complex two-modulus form fixed)
J-LI-TOEPLITZ-EQUIVALENCE       T (owner lane)
J-LI-COCYCLE-NORMAL-FORM        T as equivalence (owner lane)
J-ARTIN-FROBENIUS-DETERMINANT   T (owner lane)
J-ARTIN-SYMMETRIC-FOCK          T (owner lane)
J-PHI10-SCHOENBERG-EXEMPLAR     T algebraically, D as model of the wall
                                (both lanes; machine pins CO4, CC1)
J-LI-SCHOENBERG-2 (T_1 gate)    closed TWICE independently: owner two-arch
                                run (170cb04a/1dff8214, x86_64 + aarch64) and
                                this lane's EM-2 method (db56b0b1 + 8b0de9b8)
                                with the closed-form margin
                                M_1 = 3 + gamma + gamma^2 + 2 gamma_1
                                      - pi^2/8 - log(4 pi)
                                in [3.7100439e-5, 3.7100844e-5].
                                candidate-T-ready; public T only after a NEW
                                PREREG, NEW pin, registration, and fold.
J-LI-CYCLIC-CARRIER-DIMENSION   candidate-T (owner commit a62b040);
                                INDEPENDENTLY re-derived and instance-pinned
                                in this lane (amend2, pins below). Statement:
                                every finite-spectral pair (U, v) has
                                ||sum_{k<n} U^k v||^2 = a_* n^2 + O(1);
                                a hypothetical Li realization implies RH,
                                then Lagarias (imported, Thm 1.1) gives
                                lambda_n = (n/2) log n + ((gamma - 1 -
                                log 2pi)/2) n + O(sqrt(n) log n), unbounded
                                and o(n^2): finite carriers are excluded,
                                unconditionally (the contradiction kills the
                                assumption on every branch).
J-LI-ATOM-TEST                  new, this lane, T as equivalence (Wiener
                                imported) [REV4: factor corrected, amend4 A4:
                                mu_v({1}) = lim (lambda_{N+1} - lambda_N) /
                                (2N+1), no factor 2; the factor-2 limit is
                                sigma({1})]; no atom at 1 iff the ladder
                                increments are o(N). Under RH the increments
                                are ~ (1/2) log N: a consistency expectation,
                                not a theorem-grade gate (owner verdict 5).
MEASURE REQUIREMENT ROWS        the realization measure mu_v must satisfy,
                                exactly: total mass t_0 = 2 lambda_1 (pinned
                                interval); Fourier moments t_m = lambda_{m+1}
                                + lambda_{m-1} - 2 lambda_m; T_N moment
                                matrices PSD for every N; INFINITE support;
                                1 in supp(mu_v); mu_v({1}) = 0. The circle
                                yes, the finite polygon no.
J-LI-COCYCLE-REALIZATION        O (the uniform target; sharpened as above)
RH                              O
F rows                          RAW-P0-WITHOUT-FILTER-SUBTRACTION;
                                RENAMED-STANDARD-WEIL-AS-NEW-PROOF;
                                PLENUM-RH-AS-RIEMANN-RH;
                                IDEAL-PACKET-BY-ADDITIVE-SECTOR-SUM;
                                COCYCLE-BY-FINITE-FIT, now upgraded from a
                                guard to a theorem-backed row by
                                J-LI-CYCLIC-CARRIER-DIMENSION.
```

## 2. Branch and artifact map (the anti-chaos table)

```
PUBLIC (github.com/mathorn1973/twist-j)
  main                        6bb013ba, canon-v6, ACTIVE, untouched
  probe/P-PENTAGON-WEIL-1     head a7ff0056, prereg pin 6be1231a, issue #41,
                              draft PR #42 (unmerged by design)

OWNER LOCAL (his machine; unpushed, no authenticated gh there yet)
  agent/j-li-schoenberg-2-incubation      913d1ea6
  agent/j-li-cross-branch-staging         a62b0409
      history 6bb013b -> 913d1ea -> 1678d7b -> a62b040
      1678d7b: transfer audit, 1_G vs chi_0^(5) fix (machine-pinned in this
               lane as CC4)
      a62b040: J-LI-CYCLIC-CARRIER-DIMENSION
  handoff artifacts (Library and local, NOT visible to this session):
      thin git bundle sha256 ee06fc0d...ad26a
      tree patch      sha256 762fa643...9cc0
      spectral no-go proof; cross-branch audit
  Library folder TWIST - J/J-LI-SCHOENBERG-2/ (rev3 doc, verifier
      170cb04a...61bb8f, stdout 1dff8214...992e3, SHA256SUMS, git patch)

THIS SESSION (cloud clone /home/claude/twist-j-public)
  agent/c-li-cocycle-1-incubation         aee7a376 (author A. M. Thorn)
      contents: notes/incubation/{C-PENTAGON-WEIL-1, C-WEIL-REALIZATION-1,
      C-LI-COCYCLE-1} with per-folder SHA256SUMS and README
      push BLOCKED: sandbox tokens are 14-byte placeholders, gh absent
  transfer artifacts (delivered to the owner chat; patch also in project):
      incubation-c-li-cocycle-1.bundle    sha256 373fde1e...9169
      incubation-c-li-cocycle-1.patch     sha256 4e3f43c6...efa8
  KNOWN TRANSFER FAULT: the owner's archive 33a55eeb...bbcdd did NOT contain
      the bundle or patch, so aee7a376 is NOT yet merged into his staging.
      The bundle and patch are re-sent with this consolidation. The owner
      correctly refused text reconstruction.

PROJECT (claude/ namespace; permanent record)
  candidates:   C-PENTAGON-WEIL-1.md; C-WEIL-REALIZATION-1.md (rev4) with
                verifiers and amendments; C-LI-COCYCLE-1.md with PREREG and
                verifiers (frozen run with the archived CO6 fire, amend1,
                amend2); O-WEIL-REALIZATION_RECON_2026-07-15.md
  verdicts:     OWNER_VERDICT_{,2,3,4}_C-WEIL-REALIZATION-1 archives with
                sha256 pins
  transfer:     incubation-c-li-cocycle-1.patch
  this file:    LI-COCYCLE-LANE_CONSOLIDATION_2026-07-16.md
```

## 3. The convergence dictionary (both lanes, one language)

```
cocycle          b(n) = sum_{k<n} U^k v  (owner convention; my earlier
                 (U^n - I) xi is the coboundary special case, bounded)
ladder           ||b(n)||^2 = int |D_n(theta)|^2 d mu_v,
                 |D_n|^2 = (1 - cos n theta)/(1 - cos theta)
                 (spectral theorem, imported)
measure          CORRECTED (owner verdict 5, machine-pinned in amend3)
                 [REV4: "sigma = 2 mu_v exactly" is WRONG in general; the
                 correct form is sigma = mu_v + iota_* mu_v, which equals
                 2 mu_v only for conjugation-invariant mu_v, as on the two
                 real finite instances. Machine-pinned in amend4 (A2, A3);
                 the moment identity below stays valid]:
                 t_m = lambda_{m+1} + lambda_{m-1} - 2 lambda_m
                     = 2 * int cos(m theta) d mu_v = sigma_hat(m)
total mass       mu_v(T) = lambda_1, pinned
                 [0.023095708964233559, 0.023095708972138893];
                 sigma(T) = t_0 = 2 lambda_1
moment gates     T_N PSD for all N  <=>  mu_v exists (Herglotz); the T_1
                 gate is the M_1 margin, closed by both lanes; the owner's
                 K carries the 1/2 normalization, so
                 det K_N = 2^-N det T_{N-1} (K_3: det K_3 = det T_2 / 8)
atom test        mu_v({1}) = lim (lambda_{N+1} - lambda_N)/(2N+1)
                 (telescoping exact, CC3; Wiener imported; the owner's
                 normalization)
carrier no-go    finite spectrum => a_* n^2 + O(1) (CC1: a_* = 0 bounded;
                 CC2: a_* = 1, n^2 law); lambda needs unbounded o(n^2)
                 growth => infinite support, 1 in supp, no atom at 1
kill test        CORRECTED RATE DISCIPLINE (owner verdict 5): the
                 theorem-grade necessary condition from the atom test is
                 Delta lambda_n = o(n) only; the rate (1/2) log n holds
                 under RH via Lagarias (imported) and is a consistency
                 expectation, not a theorem-grade gate. Bounded or
                 quadratic ladders still die immediately (carrier no-go).
```

## 4. Blockers and the exact unblocking sequence

```
B1  PUSH AUTH (both sides blocked identically). Single unblocking action:
    one authenticated environment (owner's machine with gh, or any clone
    with a valid token) does:
      git fetch <incubation-c-li-cocycle-1.bundle> \
          agent/c-li-cocycle-1-incubation:agent/c-li-cocycle-1-incubation
      git push -u origin agent/c-li-cocycle-1-incubation
      git push -u origin agent/j-li-cross-branch-staging
    Never rebase or force-push either branch. A merge commit joining
    a62b040 and aee7a376 is the owner's call, after both are public.
B2  CROSS-VERIFICATION WITHOUT TOKENS: attach the owner's thin bundle
    ee06fc0d...ad26a as a file in this chat. This session then imports it
    into the clone, runs git fsck, executes the 170cb04a verifier as a
    third environment against stdout 1dff8214, builds the exact merge with
    aee7a376 locally, and returns ONE consolidated bundle. No credentials
    needed for any of that.
B3  PUBLIC PROBES only after B1 or B2, each with a NEW PREREG and NEW pin
    before its first public run (owner rule; no retroactive
    formalization). Ready candidates: the T_1 gate (two independent
    closures) and the carrier no-go (proof plus machine instances).
```

## 5. Next mathematical gates, in order

```
1. sigma_3 derivation and freeze (gamma_2 and zeta(3) brackets are ready
   extensions of the pinned integer-interval machinery) -> lambda_3 and
   the T_2 gate.
2. The increment kill test as a standing falsifier row for every proposed
   realization (R1 time-driven stream, R2 lambda-adic boundary at p = 5,
   R3 transfer operators): produce lambda_1's interval, M_1's interval,
   and increments ~ (1/2) log N, in that order; first miss kills the
   construction, not RH.
3. After B1/B2: cross-run of both lanes' verifiers in both directions,
   then the public probe assembly.
```

## 6. Amendment 2 pins (this turn's machine work)

```
verifier        C-LI-COCYCLE-1_verifier_amend2.py
file sha256     070e9f3d981fe37cbce8f683ea7a4d5c3f1988db9a88e32918d8b2a401304def
                (6603 bytes, pinned before its single run; 5/5 PASS first run)
stdout sha256   42be432bdf279fe990220e28d56dbf70b0db468f34c683c21d62942bb3772bb9
                (1018 bytes)
checks          CC1 exemplar cycle ladder (0,4,10,14,20,24,...), period 10,
                zeros at 10m, max 24, a_* = 0, exact in Z[zeta_20]
                CC2 C_4 atom instance: g(n) = n^2 + (0,3,4,3), g(4m) = 16m^2,
                a_* = 1, exact in Z[i]
                CC3 telescoping dictionary on two ladders, exact
                CC4 1_G vs chi_0^(5): five_tower * chi_0 = all-ones, n <= 200
                CC5 the dichotomy summary (bounded vs n^2 + O(1))
environment     LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0
                TZ=UTC; Linux x86_64, Python 3.11.15
```

## 7. REV2 addendum (2026-07-16, after owner verdict 5)

```
STAGING HEAD    the owner's lane head is now aa323db4595f9a40dc8f6e8f3fab36
                b9e9d6e35e on agent/j-li-cross-branch-staging (supersedes
                a62b040 as head; history preserved, unpushed).
NEW HANDOFF     thin bundle sha256 f56a4571...02bb, tree patch sha256
                d5f61a6d...ee1 (Library; not yet visible to this session;
                attach as chat files for a third-environment run here).
TRANSFER        the tree of aee7a376 is now CROSS-VERIFIED owner-side: the
                patch 4e3f43c6 applies cleanly and all six verifiers
                reproduce their pinned stdouts. The binary bundle 373fde1e
                failed to arrive twice; remedy shipped this turn: the
                byte-exact base64 text transport
                claude/incubation-c-li-cocycle-1.bundle.base64.md
                (round-trip verified to sha256 373fde1e...). Exact-identity
                merge of aee7a376 unblocks on decode.
SIGMA_3         now DERIVED in this lane (not imported): the xi(1+t)
                expansion with t zeta(1+t) = 1 + gamma t - gamma_1 t^2 +
                (gamma_2/2) t^3 and log Gamma(3/2 + t/2) via psi(3/2) =
                2 - gamma - 2 log 2, psi'(3/2) = pi^2/2 - 4, psi''(3/2) =
                16 - 14 zeta(3) reproduces sigma_1 and sigma_2 exactly
                (route validation) and yields
                sigma_3 = 1 + gamma^3 + 3 gamma gamma_1 + (3/2) gamma_2
                          - (7/8) zeta(3),
                confirming the owner's frozen formula independently.
                Amendment 3 pins: verifier 5d6ab0d0a7442e47fb742b1a3dfddcf4
                cfc9bbdc0827d4b36543f65dea7ae725, stdout dc5eb44a463c3546e5
                2ecc8bfccb049d87c1ec236e5b0ba9229cac03acf945d0, 5/5 PASS
                first run.
LAMBDA_3 / T_2 GATE   owner-side candidate-C, ONE architecture (verifier
                49cdaa57..., 11/11, stdout 678bd1b4...; aarch64 pending).
                This lane's float witnesses agree: lambda_3 float
                0.207638920554 inside the owner interval; det T_2 float
                5.7580329367e-13, and det K_3 = det T_2 / 8 =
                7.19754e-14 inside the owner's [6.9813e-14, 7.3759e-14].
                The escalating-razor phenomenon is real: the measure
                accumulates at 1, so T_N is nearly singular and each gate
                is exponentially thinner (T_1 margin 3.7e-5, det T_2
                5.8e-13). Certification spec for the two-architecture
                re-run: gamma_2 brackets of width about 1e-12 (EM-4
                remainder at N = 1e5, or EM-2 at N = 1e7).
LEDGER DELTA    J-LI-ATOM-TEST normalized (mu_v(T) = lambda_1);
                J-LI-LAMBDA-3/T_2: owner-side candidate-C one-arch, formula
                layer T-derived both lanes; K_2 and K_3 finite gates
                PASSED at their stated grades.
```

## 8. REV3 addendum (2026-07-16, live public state and cross-runs)

```
PUBLIC STATE (verified live against the remote this turn):
  main                        6bb013ba, canon-v6, ACTIVE; NO Weil or Li rows
                              anywhere in CANON, REGISTRY, FRONTIER (the two
                              grep hits are the unrelated ENTROPY lane)
  probe/P-PENTAGON-WEIL-1     a7ff0056, unchanged; still the only formally
                              pinned public artifact of the lane
  agent/j-li-cross-branch-staging   NOW PUBLIC at fc4d6016 ("Publish J-LI
                              cross-branch consolidation", one clean commit;
                              the local heads 913d1ea/1678d7b/a62b040/aa323db4
                              were consolidated into it, not pushed raw).
                              Contents: notes/j-li-schoenberg-2/ with both
                              verifiers, EXPECTED files, SHA256SUMS, the
                              carrier no-go, atom test, FEJER_SCALING (T as
                              necessary implication), LAMBDA3_T2 + aarch64
                              incubation record, and the BLOCKED-PREDEFINITION
                              prereg draft P-J-LI-FEJER-CARRIER-1.
THIRD-ENVIRONMENT CROSS-RUNS (this session, Linux x86_64, Python 3.11.15):
  verify.py            sha256 confirmed 170cb04a33a717e9f637b1948b81f01fba
                       0414b86e0c082a2034bb398061bb8f; run: exit 0, empty
                       stderr, stdout byte-identical to EXPECTED.txt, sha256
                       1dff821424280361ec15ebbb2e405d7e6b4d452d820aeefcd2e8
                       d966cb8992e3. The pin gap that opened this thread is
                       fully closed.
  verify_lambda3_t2.py sha256 confirmed 49cdaa5769104fda39a18d5a3e75dd4f2d
                       a6526e4a2e93201f89345058ebad2a; run: 11/11 PASS,
                       stdout byte-identical, sha256 678bd1b4e88b12f074c5c4
                       6ed06c69f98984570cc3c312a64921a9ac4b0ef60a. With the
                       owner's x86_64 and aarch64 records this gate now has
                       three consistent environments at incubation grade.
CONSOLIDATED HEAD READY TO PUSH:
  branch agent/c-li-cocycle-1-incubation, head 18e7d818f1084a78f2d04d50e923
  c7ddbd76c2e7 = merge of (aee7a376 + 72cc23c consolidation commit) with the
  public fc4d6016. The 72cc23c commit refreshes C-LI-COCYCLE-1 with
  amendments 2 and 3 and adds the public-safe notes/incubation/
  CONSOLIDATION.md. Transport: bundle sha256 a00f124a738b6b5234e22ff83c3285
  63b38219e05bc81302801642b1b8006d7a (prerequisite 6bb013ba), patch sha256
  4ef64ec6..., base64 transport doc df93d614.... One authenticated push of
  this branch puts the ENTIRE lane, both lines and their merge point,
  on the public repository.
```

## 9. Non-claims

The carrier no-go narrows the realization space; it does not enter it. The
T_1 gate and every finite prefix remain necessary-condition calibrations.
Nothing here touches G5. J-LI-COCYCLE-REALIZATION [O]. RH [O]. No public
registration, no push, no normative change was made by this session.

## 10. REV4 addendum (2026-07-16, supersession and public topology)

```
STATUS         this document is SUPERSEDED as the lane map by
               notes/j-li-schoenberg-2/LI-COCYCLE-LANE_CONSOLIDATION_
               2026-07-16.md. It stays as the historical record of the
               lane's consolidation day; nothing below rewrites the pinned
               artifacts it references.
MEASURE        the section-3 row "sigma = 2 mu_v exactly" and the section-1
               atom-test factor 2 are corrected: sigma = mu_v + iota_* mu_v,
               mu_v(T) = lambda_1, sigma(T) = 2 lambda_1, sigma_hat(m) = t_m,
               mu_v({1}) = lim Delta lambda_N / (2N+1), sigma({1}) = twice
               that. Fourier data determines sigma only; the non-symmetric
               mu_v is not determined. Machine pins: amend4 (A2, A3, A4),
               verifier 351f3dae41df9dabf2230466b792d27e9045e81dfef4dbab373
               26cfda954e8e4, stdout 37c01ea5f79a52f7b5dcfcec2c7bd99b3a61d4
               18af31b76f73b478b83259b876.
DET SCALE      the REV2 lambda_3/T_2 row already used the correct
               det K_3 = det T_2 / 8; the amend3 S4 stdout line did not and
               printed "contains float: False" at a mis-scale of 2^3. The
               corrected witness (amend4 A1, A5) reads True:
               det K_3 = 7.1975411709e-14 inside the owner's interval.
PUBLIC         the blockers B1/B2 (section 4) and the section-8 head
TOPOLOGY       18e7d818 are OBSOLETE. Live public state:
                 main                              6bb013ba (canon-v6, ACTIVE)
                 agent/j-li-cross-branch-staging   fc4d6016 (public)
                 c-li-cocycle-1-incubation         ac62cac + debt-fix commits
               The public incubation branch is a CONTENT consolidation: the
               local commit aee7a376 and its exact parentage were not
               preserved, by design (owner's call). Neither incubation
               branch has a PR or GitHub checks; the only open PR is the
               draft #42 (P-PENTAGON-WEIL-1, unmerged by design).
EVIDENCE MAP   confirmed shift for the draft-PR lane: V05 belongs to G02,
               V06 to G05, and G06 is proof-only.
MANIFESTS      notes/C-LI-COCYCLE-1/SHA256SUMS and
               notes/C-PENTAGON-WEIL-1/SHA256SUMS added; the two components
               were the only ones without manifests.
```
