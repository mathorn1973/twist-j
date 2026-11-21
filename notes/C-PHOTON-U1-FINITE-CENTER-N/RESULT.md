# Audit A result: exact finite-center bridge and bounded reader

**PUBLIC-source, NON-CANONICAL; no authority.**
Candidate C-PHOTON-U1-FINITE-CENTER-N, owner issue #1715.
Author: A. M. Thorn. Date: 2026-10-23. Apache-2.0.

**Finite audit: PASS, candidate-C on local x86_64.**
**Sampler exercise: PASS_OPERATIONS_ONLY, phase decision weight zero.**
**Written universal proof: candidate-T, separate from the finite audit.**

The preregistration is pinned at
`b7be3d00495330e4ac00441b865f9009e54a6299`; complete scientific sources
were publicly pinned and read back at
`9a74d03fb8f2c8086eff0f326446352f0f628082` before execution. All three
first runs exited zero with empty stderr inside their separate 180-second
budgets. No falsifier fired, no scientific run failed and no threshold,
executable source or first-run transcript was replaced. `RUN.md` records complete
custody and the original streams remain under `runs/audit-a/`.

## Mathematical result and its exact scope

The written character argument establishes the proposed sufficient bound

```text
N > max_e(sum_p |B_ep| + |J_e|)
    implies Z_ZN[a,J] = Z_U1[a,J]
```

for every real plaquette source `a`, on the stated finite cell complex,
with identical orientations and normalized Haar measures on all edges.
It retains all integer cycles, including nontrivial torus winding.
For the selected four-dimensional cubical action this gives N>=7 for
partition/source functions without a link insertion, and N>=8 for the
whole class of integer currents with maximum absolute coefficient one.
This is a candidate-T finite-action theorem, not a phase statement or an
equivalence of arbitrary link observables or primal configurations.

The N=2,...,6 parity constructions show the threshold seven is globally
sharp on the admitted even four-tori. Their nonzero `Bn=N j` has positive
character weight. For the full admitted current class, the N=6 construction
with inserted `J=j` gives `Bn+J=7j`, separating the Z7 and U1 numerators.
This insertion is a product of winding-loop characters; no sharpness
claim is made for one simple contractible Wilson loop.

The source argument gives exact stack/uniform agreement and
`F''(0)=Var(W)` in the complete integer-closed surface ensemble, hence
also for the matching Z7 source functions. The untwisted Z7 source-Hessian
reader lies in Q(x), where `x=2*cos(2*pi/7)`, and is bounded at each finite
volume. Its per-configuration values need not be positive. The finite
positive winding variance supplies no uniform positive thermodynamic
lower bound. None of these source equalities extends automatically to Z5.

## Exact finite audit outcomes

Both independently authored programs passed frozen tests 1--6. They used
different exact field representations: rational triples modulo
`x^3+x^2-2*x-1` in the primary, and a separately implemented cyclotomic
representation in the breaker. Neither comparison is a second hardware
architecture or independent external acceptance.

The local incidence census contains 1093 ternary words of lengths zero
through six. For N=7,8,13 it found exactly the same zero selection over
the integers and modulo N. The modulo-five controls contain two nonzero
aliases at degree five and twelve at degree six; modulo six contains
two at degree six. These are finite word counts, not lattice defect
probabilities.

The actual oriented four-torus witnesses have the following support
counts. Every edge equation and current conservation check passed.

| N | Triple `(a1,a2,a3)` | Support at L=4 | Support at L=6 |
|---:|---|---:|---:|
| 2 | `(0,0,2)` | 256 | 1296 |
| 3 | `(0,1,2)` | 384 | 1944 |
| 4 | `(0,2,2)` | 512 | 2592 |
| 5 | `(1,2,2)` | 640 | 3240 |
| 6 | `(2,2,2)` | 768 | 3888 |

The current support is 256 at L=4 and 1296 at L=6. The inserted-current
N7 witness passed at both sizes. At L=4, all six fundamental wrapping
sheets had support 16 and winding one in their own orientation. All stack
positions and uniform pairings agreed, while all 1024 elementary cube
boundaries had zero winding.

The seven algebraic weights and score identities passed exact checks.
All 924 weak compositions of six staples gave seven strictly positive
conditional masses and exact normalized probability sums. The independently
generated 6468-line coefficient stream has the same SHA-256 in both runs:

```text
04ef99ab864b0240d3d8b0039e538eaf18d79d999aeadf89a8cb624ae84a4e5b
```

The two-dimensional enumerations retained every constrained plaquette
assignment and all wrapping sectors. Their exact controls agree:

| Torus | Assignments | Z(0) | Mean uniform H | Mean stack H | Z(2*pi/7 stack) |
|---|---:|---:|---|---|---|
| 2x2 | 343 | 18 | 1/9 | 1/9 | 16+x |
| 3x2 | 16807 | 66 | 1/33 | 1/33 | 64+x |

The corresponding source ratios are `(16+x)/18` and `(64+x)/66`.
Removing winding sectors would give the incorrect partitions 16 and 64
and zero response; the controls distinguish this error. On a single
three-cube boundary, exactly three of 729 ternary fields survived integer
closure and the partition was 66. On the single plaquette disk the sole
survivor was zero and the partition was 2.

## What the sampler exercise establishes

The four pinned starts at L=2 and L=3 completed two full sweeps each:
1552 edge updates in all, of which 797 changed the edge residue. The
categorical updates requested 49664 PRNG bits, excluding hot-start
initialization. Cached curls, recomputed curls, Bianchi identities,
principal-plane divisibility and exact reader serialization agreed after
every sweep. The full individual records are preserved without converting
the Hessians to decimal phase indicators.

This confirms operation of the exercised code paths. It is not an
equilibrium estimate, thermalization test, sector-frequency test, mixing
bound, mass estimate or phase measurement. The mathematical categorical
law assumes ideal independent fair bits; the seeded PRNG supplies only
the declared reproducible engineering trajectory.

## Coverage and next obligation

`MEASUREMENT.md` describes a broader qualification program as well as the
frozen audit. Its section 4 received an explicitly marked post-audit
documentation clarification; the frozen source commit and manifest retain
the pre-execution text. Audit A does not claim completion of every
additional test listed there. In particular, separate scripted-bit categorical boundary
tests, intentional cache-corruption tests and a dedicated comprehensive
direct-plaquette-replacement qualification are not reported as executed
tests in this first-run record. The complete conditional-mass census and
the eight consistent exercised sweeps retain exactly their stated scope.
Any further execution must receive its own declared contract and record;
the source manifest and first outputs of Audit A remain unchanged.

A production finite-size experiment still requires a separate public pin
with sizes, fresh seeds, starts, warmup, sampling budget, an independent
state reader, uncertainty treatment, practical mixing diagnostics and
explicit STOP/UNRESOLVED conditions. No such experiment ran here.

The present result makes a finite Z7 model an exact computational carrier
for the selected U1 plaquette-source question. It does not decide whether
that action is Coulomb or confined, reduce the Z5 thermodynamic question
without a further defect-control theorem, select the action from native U,
or close the public PHOTON-MASSLESS-PHASE obligation. Local computation
remains candidate-C; written proof remains candidate-T pending acceptance.
Notes CI is not the public two-architecture scientific computation gate.
