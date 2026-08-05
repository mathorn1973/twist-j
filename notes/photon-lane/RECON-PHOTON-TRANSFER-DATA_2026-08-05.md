# RECON: the photon transfer data (lane A, the R3 feeder)

```text
STATUS   RECON, NON-CANONICAL. Exact arithmetic, single architecture
         (x86_64, Python 3.11.15), recon grade: no candidate id, no
         probe, no authority, no status. Findings are labeled
         [computed, recon]; citations carry their public labels.
BASIS    Public Canon v36 (fresh local clone; the architecture display
         of CANON.md section 3: five involutive generators with
         s_c = (2,1,2,1), u_c = (0,1,0,-1), c_d = (2,1,3,4,1,1),
         v_e = (0,0,0,0,1,0); selector firing {b,d,e};
         FIRED-COMMUTATOR-NOGO [T]; KERNEL-CONNECT-ALL-K [T];
         KERNEL-CELL-DICTIONARY [D]; MEASURE-BORN-VERB [D];
         FORCE-WEYL-HOLONOMY [T]). Frozen cone (-4, +32, -72) on
         shells (2, 4, 6) from the C-PHOTON-POINT-GROUP-1 record.
PINS     recon_photon_transfer_data.py
         sha256 2ef93c9c26c56a57da588b89d9f07c53ecca6043bf41a34925b24f2f8e244042
         (16594 B; a dead assignment line was removed after the first
         run; stdout unchanged byte for byte)
         stdout sha256 a2d7bb7b0542e15c506954f78d3b55899ee5736ce85609dc0a25eae04a5fbdc1
         18 of 18 checks PASS, exit 0, stderr empty, reproduced
         byte-identically on aarch64 (Ubuntu 24.04, Python 3.12.3).
GATE     transcription cross-checks X1 to X4 all PASS (involutivity,
         (bc)^5 = id, the three displayed fired fiber commutators
         reproduced exactly, Klein group of linear parts). A failure
         there would void this census, not the canon.
```

## Question

Before R3 freezes transfer data (weights, phases) for the photon
operator: does ANY registered principle select them? Three branches:
uniform families, Born class weights, and the machine's own registered
translation alphabet; plus the phase sector.

## Findings

**F1 [computed, recon].** Uniform weight families miss the cone:
shell-1 only gives -4, shells 1+2 give 28, shells 1+2+3 give -44.

**F2 [computed, recon].** No nonzero assignment of the Born verb
weights {4, phi^2, phi^-2} (MEASURE-BORN-VERB [D],
PHOTON-WINDOW-COORDINATES [T]) nor of the dual weights {10, 5, 0} to
the three shells lies on the cone (54 exact checks in Q(sqrt5); the
only hit is the degenerate all-zero triple). Class weights are not
shell weights; this closes a tempting numerological shortcut.

**F3 [computed, recon, from the public display].** The registered
translation seeds of the kernel (the extracted pure translations of
KERNEL-CONNECT-ALL-K [T]) are

```text
v_c = (2,1,2,1,1,0)   piston (2,1,2,1), Tr4 = 1: OFF the spatial
                      kernel; the c-deposit carries the trace (scale)
                      direction
v_d = (2,1,3,4,1,1)   piston (2,1,3,4), Tr4 = 0: spatial
v_e = (2,1,3,4,2,1)   the SAME spatial class as v_d
```

**F4 [computed, recon].** The unique seed spatial class (2,1,3,4) is
NULL in the reduced form (q = 30 = 0 mod 5) and lifts minimally to
norm 10, witness (2,1,-2,-1). It is not a root class. Caveat carried
from the photon-Fermat audit: every nondegenerate ternary form over
F_5 has exactly 25 null points (Chevalley-Warning), so nullity alone
is cheap; what is possibly meaningful is only that the dynamics
deposits exactly one such class, and that reading is OPEN, not
claimed.

**F5 [computed, recon].** The Gamma-module closure of the seeds
(Gamma = <M_a, M_c, M_d, M_e> as in the public row) reaches dimension
6 in one step (dims 3 then 6), cross-checking KERNEL-CONNECT-ALL-K
[T]. The orbit has 44 vectors and deposits 20 distinct nonzero spatial
classes with shell census

```text
norm-2 roots: 4 of 12    norm-4: 2 of 6    norm-8: 4 of 12
norm-10: 8 of 24         norm-16: 2 of 6   (8 classes null mod 5)
```

For reference, the minimal-lift norm census of all 124 nonzero kernel
classes is (2:12, 4:6, 6:24, 8:12, 10:24, 12:8, 14:24, 16:6, 18:8).

**F6 [computed, recon; conditional on the coordinate-identity reading
of GATE-LIFT-KERNEL-Z].** The deposited 20-class alphabet is NOT
closed under the carrier point group (the 48 signed permutations of
the piston coordinates). The machine's spatial alphabet breaks
octahedral symmetry. Consequence for the photon program: either the
measure or decoder RESTORES isotropy downstream, or the carrier's
octahedral symmetry is physically broken by the dynamics. Deciding
which is first-order R1/R3 material, and the point-group result now
acts as the referee: a derived characteristic that is
octahedral-symmetric would prove restoration; one that is not would
make the anisotropy physics with a falsifier.

**F7 [computed, recon].** The phase sector on the carrier: 24
triangles per vertex, each edge in exactly 4, falling into 4 direction
classes that form ONE orbit under the 48-group. A fully symmetric flux
ansatz on the carrier is therefore a SINGLE Z_5 number. The flat
sector has zero holonomy on every triangle (pure gauge cancels
exactly), so for flat connections the phase-free cone stands
unchanged. At cell level the fluxes are already registered as the
fired fiber commutators (0,0,0,0,3,0), (0,0,0,0,3,3), (0,0,0,0,1,3)
[T]; their carrier-level assignment is unregistered and needs the same
lift as the weights.

## Verdict map (A3)

```text
FORCED     NO. Nothing registered selects a point on the cone, and the
           registered alphabet is not even shell-symmetric.
NONUNIQUE  not established either; no admissible class of transports
           is frozen to classify.
EMPTY      YES for public derivation, with two named missing maps:
           (i) the cell-to-carrier lift (the R1 object), and
           (ii) a class-to-shell (or class-to-alphabet) weight
           transport. R3 must freeze them, or a derivation must
           produce them; nothing registered does either today.
```

The R3 decision space is now concrete instead of open-ended: transfer
data = a weight system over the machine's 20-class deposited alphabet
(or a declared symmetric completion of it, which is itself a choice to
be named), plus one Z_5 flux number in the symmetric ansatz, plus the
lift identification. Three named objects. That is what "the photon's
remaining input" actually is.

## Falsifier of this recon

Any transcription cross-check X1 to X4 failing on re-run; any quoted
display differing from CANON.md at v36; any census number failing an
exact recomputation; a public row registering a weight or flux
selection this recon declares missing. Single-architecture recon
grade: nothing here carries candidate or probe weight.
