# P-ENTROPY-BRIDGE-2 preregistration

Status: PRE-PIN DRAFT

This document freezes the complete decision surface for the second probe of
the ENTROPY-BRIDGE program: the exact decision of the finite-cylindrical
ansatz for the bridge cut, and the scale behavior of the renormalized block
maps. It contains no gate output and earns no scientific status. Formal
execution is forbidden until this document and the accepted verifier are
committed and pushed as one immutable preregistration pin and that remote
pin is read back.

## Public identity and action layer

```text
program:          ENTROPY-BRIDGE
probe:            P-ENTROPY-BRIDGE-2
public lock:      issue 27
owner:            entropy-bridge session
branch:           probe/P-ENTROPY-BRIDGE-2
path:             probes/P-ENTROPY-BRIDGE-2/
initial base:     dfb8bc43f9f1c9df25aaa334fa9780f460e75f51
action layer:     L5 stream (driver and kernel combinatorics); no L2 lift
                  and no L6 measure claim is made by this probe
scientific state: decides the cylinder ansatz inside ENTROPY-LAYER-BRIDGE
                  [O]; records one F at tested depths and one C law
```

This probe is based on Public Canon 2, tag `canon-v2`, activation commit
`5abb22319007fd3172f7123f4b3a71b547fb94af`, content commit
`7cfe2a62a456d0f84b1f60b4945dcdfe896e99db`, Canon SHA-256
`abd0e026ccc2be00cdb0d9d13d634e0a71602b1565e6d53ac23a99b506281021`, and
follows P-ENTROPY-BRIDGE-1 (merged to main in pull request 26; its pinned
facts, in particular branch indegree {0: 3125, 2: 3125} on the recurrent
core, are inputs by reference).

## The frozen question

The ENTROPY-BRIDGE program (owner ruling R4, pinned in the
P-ENTROPY-BRIDGE-1 preregistration) seeks a cut P_5(kappa, y) with

    P_5(S_K kappa, J y) = F_{theta(kappa)}(P_5(kappa, y)),
    F_eps(psi) = g_{z(psi) + 2 eps mod 5}(psi),

kappa in the two-sided Thue-Morse subshift, y in O_{K,lambda}, target the
public carrier F_5^6. This probe decides the EXACT FINITE-CYLINDRICAL
ansatz: P_5 depending only on a driver window of length L (current position
c inside the window) and the residue y mod lambda^m, at the frozen depths
below. It further measures the renormalized block maps whose behavior
governs every deeper reading.

Reduction, part of the freeze (proofs one line each, in this document):

1. Contexts (window w, residue u) evolve by (w, u) -> (tail(w a), J u) for
   every admissible extension a, with the constraint P(next) =
   F_{theta}(P(prev)), theta the current letter of w. Feasibility of the
   ansatz at depth (L, c, m) equals solvability of this finite constraint
   system over all admissible windows and residues.
2. ISOMORPHISM LEMMA. The residue enters only through its J-orbit index:
   contexts over a J-orbit of length ell form a constraint system
   isomorphic to (windows) x Z_ell. One decision per orbit length occurring
   in the spectrum therefore decides the whole depth. The spectra are
   themselves gates (G01, G02).
3. KILLING LEMMA. J 0 = 0, and the residue class y = 0 mod lambda^m has
   positive Haar measure at every finite depth m. Any cylinder cut
   therefore restricts on it to a solution of the PURE-WORD system (ell =
   1, no residue data). Pure-word infeasibility at window length L blocks
   window length L at EVERY lambda-depth. (Machine part gate G06; the
   measure statement is this frozen text.)

## The six frozen fields

```text
equation:     the constraint system above at the frozen depths; the
              frozen expected values: solution count 0 at every tested
              depth (G05, G07, G08); factor counts of the driver word
              pinned per L (G05); orbit spectra {1: 1, 4: 1, 20: 31} mod 5
              and {1: 1, 4: 1, 20: 781, 100: 3750} mod 25 (G01, G02); no
              common fixed point of F_0, F_1 (G03); core 6250 on 313
              (G04); the one-bit-per-scale law |image Phi^(k)_eps on the
              core| = 3125 exactly for k = 0..10, both letters, where
              Phi^(k)_eps composes F along the level-k substitution block
              of eps (G09); the odometer collision pins: on the seed-0
              orbit, first (n mod 2^k, theta_{n >> k}) collision exactly
              at 4096 + 2^(k+1) for k = 1..10 (G10).
code:         verify.py in this directory, Python 3 standard library only,
              exact integer arithmetic, no float anywhere, single process,
              no filesystem writes, runtime well under 120 seconds
              (component timings measured in recon: seconds).
carrier:      the public F_5^6 kernel constants (as pinned by the Canon
              reproduction and P-ENTROPY-BRIDGE-1); the Thue-Morse drive;
              M_J for the residue action. No external data.
systematics:  driver factors taken from the prefix 2^16 (complete for the
              tested lengths); recon-lane exploration disclosed below; the
              trajectory pins use seed 0 with warmup offset 4096.
failure
threshold:    any gate FAIL. All gates are exact equalities of integers or
              finite dictionaries. No tolerances.
action layer: L5. The corollary "no exact finite-cylindrical cut with
              driver window <= 16 exists at any lambda-depth" is licensed
              by G05 plus the killing lemma at the stated scope. No claim
              is made about measurable non-cylinder cuts; that is the
              successor construction.
```

## Gates (all exact; the frozen decision surface)

```text
G01 SPECTRUM-5     J-orbit spectrum mod 5 equals {1: 1, 4: 1, 20: 31}.
G02 SPECTRUM-25    J-orbit spectrum mod 25 equals {1: 1, 4: 1, 20: 781,
                   100: 3750}.
G03 NO-CONSTANT    F_0 and F_1 share no fixed point (no constant cut).
G04 CORE           recurrent core 6250 states on 313 attractors (census
                   protocol of the public reproduction).
G05 PURE-WORD-NOGO the pure-word constraint system has ZERO solutions for
                   every window length L = 4..16; driver factor counts
                   pinned: (words, edges) = (10,12), (12,16), (16,20),
                   (20,22), (22,24), (24,28), (28,32), (32,36), (36,40),
                   (40,42), (42,44), (44,46), (46,48).
G06 KILLING-ZERO   M_J 0 = 0: the zero residue class is J-invariant, so
                   the pure-word system embeds at every lambda-depth; with
                   G05 this blocks every cylinder cut with window <= 16 at
                   every depth.
G07 M4-TABLE       zero solutions at lambda-depth 4 for every (L, c) with
                   L in {4, 5, 6}, every current position, every orbit
                   length in {1, 4, 20}.
G08 M8-TABLE       zero solutions at lambda-depth 8 for L = 4 and every
                   orbit length in {1, 4, 20, 100}.
G09 BLOCK-HALVING  the renormalized block maps are exactly 2:1 on the
                   core at every dyadic scale: |image Phi^(k)_eps| = 3125
                   for k = 0..10 and both letters. One bit lost per
                   scale, never more, never less.
G10 COLLISION-PIN  the odometer-cylinder reading with one block label
                   fails with the exact seed-independent pattern: first
                   collision at 4096 + 2^(k+1), k = 1..10 (pinned on the
                   seed-0 orbit).
```

Falsifier map: a NONZERO count in G05, G07, or G08 refutes the no-go and
EXHIBITS a finite-cylindrical cut, a first-class positive that would
redirect the program; a break of G09 at some level refutes the scale law;
a mismatch in G10 refutes the collision structure. A fired gate is merged,
not hidden.

## Reading (frozen, carried at its stated grade)

The cylinder ansatz for the bridge cut FAILS at every tested depth, and by
the killing lemma the failure at windows <= 16 extends over all
lambda-depths: the obstruction is the driver-word holonomy alone, and the
residue tower cannot repair it. The one-bit-per-scale law names the
mechanism at C grade: each dyadic block map hides exactly one unresolved
bit at every scale, so any locally constant reading misses infinitely many
bits. Consequence for the program, recorded as the narrowed obligation: a
solution of the bridge equation, if it exists, is measurable and not
locally constant in the driver coordinate; it must read unboundedly many
letters (the carry structure), with the lambda-digit tower of
O_{K,lambda} as the natural per-scale carrier. The constructive attack is
the successor probe.

## Environment and execution

```text
cd <repo root>
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-ENTROPY-BRIDGE-2/verify.py
```

Exit 0; exact stdout as EXPECTED.txt on the first formal run (aarch64);
RUN.md with neutral descriptors; a preliminary RESULT.md is added BEFORE
the pull request (workflow requirement learned in P-ENTROPY-BRIDGE-1);
the pull request check reruns on GitHub x86_64; byte identity closes the
two-architecture computation gate.

## Disclosure

Recon-lane exploration (incubation lane, session records of 2026-07-14,
project doc P-ENTROPY-BRIDGE-2_RECON) computed every value frozen above
before this pin, on x86_64, outside this repository, with unpinned recon
scripts, including component timings. That exploration carries no public
status. The formal status of every gate derives only from the post-pin
two-architecture runs of the pinned verifier.

## Out of scope, explicitly

Measurable non-cylinder cuts (the successor construction); window lengths
above 16; lambda-depths above 8 in the tables; the L2 -> L5 entropy
transport; any physical reading; any claim that the public architecture is
derived from J or M_J. Nothing in this probe modifies canon/, the
registry, or the frontier; folding any outcome is a separate sealed step.
