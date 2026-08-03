# Kappa attack: checkerboard phase, slab revival, and a first witness

**STATUS: NON-CANONICAL WORK NOTE. NO PROBE RUN. NO CANON CHANGE.**
Falsification attack on the kappa route of `PHOTON-WINDOW-PROOF [O]`,
on the candidate surface frozen by owner disposition R0A-R5B in
`notes/canon/P-PHOTON-KAPPA-LEMMA-1-PREDEFINITION.md` (section 9).
Authority at the time of writing: **Public Canon v34**
(tag `canon-v34`, content commit `b15bde93...`, SHA-256 `1a26e805...`,
172167 bytes). Nothing here changes any public claim; every labeled
status below is a candidate label in the sense of the reconciliation
vocabulary, not a registered status. Scripts and the witness artifact
are archived in `notes/kappa-witness-2026-08-03/`; cubical conventions
are exactly those of `reproduce/photon-electron/verify.py`.

The candidate surface and certificate form:

```text
j in C_1^c(Z^4; {0,+1,-1}), j != 0, partial j = 0,
n in C_2^c(Z^4; {0,+1,-1}), partial n = 5j,
L = |supp j|, F = |supp n|,
falsifier certificate: connected edge-simple (j, n) with
partial n = 5j and 2^F <= 7^L.
```

Certificate scope, stated explicitly (owner-audit wording):

```text
edge coefficients: {-1,0,+1}
repeated edges: forbidden
repeated vertices: allowed
vertex degree: even, not necessarily 2
connectivity: support graph connected
```

The support is a connected Eulerian graph; a closed walk traversing
every support edge exactly once (Hierholzer certificate) realizes the
current as one closed edge-simple worldline with repeated vertices.
This subclass is what disposition R3A names as the first falsifier
subclass; it is not claimed to be a degree-2 simple polygon.

## 0. Headline result

**[reported candidate-C; exact feasibility, one machine]**

An explicit pair `(j, n)` at shape `(P,m,C,D) = (6,3,6,6)`:

```text
L = 3240        F = 7993        F/L = 2.46697...
B(3240) = max{m : 2^m <= 7^3240} = 9095;  F = 7993 <= 9095
2^F <= 7^L rechecked as exact integers (2407 vs 2739 digits)
```

Verification is split per the owner audit:

- **exact feasible witness after an independent integer recheck**:
  `verify_witness.py` re-verifies from the JSON alone: j ternary,
  closed, nonzero, support connected, explicit Eulerian walk of 3240
  steps; n ternary; `partial n = 5j` coefficientwise on every edge of
  `Z^4`; the threshold inequality as exact big integers. All PASS.
- **solver-reported optimum within the frozen rings-8 shell**: the
  archived run log (`run_6366_r8.log`, invocation in `runjob.sh`)
  records `ILP: 309808 variable faces` and `ILP status: Optimal`;
  that remains solver output, not a theorem, and the certificate does
  not need it. Caveat for auditors: `repair_witness.py` accepts any
  non-Infeasible incumbent and falls back to CBC when HiGHS is
  absent, so the exact integer recheck, not the solver status, is the
  gate.

Candidate consequence, in the predefinition's own frame: for this
admitted worldline `F_occ(j) <= 7993`, so every universal coefficient
claim `F_occ >= kappa L` forces `kappa <= 7993/3240 < log2 7`, and
`2^(4 kappa) > 2401` fails. The pair is therefore a **candidate
refutation** of the kappa route of `PHOTON-WINDOW-PROOF` on the
R0A-R5B candidate surface; the registered outcome vocabulary
(CANDIDATE-REFUTED) is reachable only through the formal probe
protocol (issue #200 definition lock, `S_kappa` freeze,
preregistration, two-architecture record). A public one-machine
finite result remains at most `C` by policy.

## 1. Five-of-six rigidity

**[candidate-T]** On a charged edge the six incident ternary
contributions sum to +-5, so they are five equal signs and one zero:
every occupied face incident to a charged edge serves it with the
forced sign, each charged edge carries exactly one missing-coface
slot, and with `N_r` the count of occupied faces having `r` charged
boundary edges,

```text
sum_r r N_r = 5L,      F >= 5L/4.
```

**Correction adopted from the owner audit:** an `r = 1` face has
three uncharged boundary incidences, not one distinguished one. On an
uncharged edge the nonzero incident contributions balance in equal
`+/-` counts (an even number), and the balancing face need not be an
`r = 0` face; other `r >= 1` faces may absorb part of the syndrome.
Any "no third-party absorption" step is a separate geometric lemma
that must be proved per carrier, and it is exactly the unproved step
in the slab accounting below.

## 2. The checkerboard identity and the exact bulk optimum

**[candidate-T, frozen bulk current]** With
`h(x) = (-1)^(x0+x1+x2+x3)` and a 0/1 projector
`g(x) + g(x - e_3) = 1`:

```text
j_0 = h,  j_1 = -h,
n_01 = h,  n_02 = h,  n_12 = -h,  n_03 = g h,  n_13 = -g h
```

satisfies, under the public orientation
`partial f_mn(x) = e_m(x) + e_n(x+e_m) - e_m(x+e_n) - e_n(x)`,

```text
(partial n)_0 = 2h + 2h + h = 5h = 5 j_0,
(partial n)_1 = -5h = 5 j_1,
(partial n)_2 = 0,   (partial n)_3 = 0,   partial j = 0.
```

This is a local chain identity (window-verified exhaustively in
`local_identity.py`), the service factorization `5 = 2 + 2 + 1`. On a
periodic bulk cell of V sites: `L = 2V`, `N_4 = V` (full `f_01`),
`N_2 = 3V` (full `f_02`, `f_12`, half-density `f_03`, `f_13`),
`F = 4V = 2L`, service `4V + 6V = 10V = 5L`, no `r <= 1` faces, zero
syndrome on every uncharged edge.

**Scoped optimality [candidate-T]:** for this current only `f_01`
slots can be `r = 4` and there are `L/2` of them; every other slot has
`r <= 2`; hence `5L <= 2F + 2a <= 2F + L`, so `F >= 2L`, achieved:
`Phi(j) = 2L` on the frozen periodic checkerboard current.

**Three-direction no-go [candidate-T, scoped to the separable
coherent sign ansatz]:** full pairwise coherence in three directions
needs `eps_0 eps_1 = eps_0 eps_2 = eps_1 eps_2 = -1`, whose product
gives `1 = -1`. This is the impossibility of two-coloring a triangle,
for this ansatz only; it is not a universal no-go for irregular
three-direction currents.

## 3. Slab family: corrected arithmetic, branch revived

**[correction of an earlier claim in this note's first version]**
The earlier statement "the slab family costs at least 3 per edge for
every n" was wrong; it read the n = 8 value as a bound. The literal
accounting gives per slice

```text
A = n^2 + 4n(n-1) pair faces, 4n singles per layer,
F_slice = 5L_slice - A + 4n = 5n^2 + 8n,
F_slice / L_slice = 5/2 + 4/n.
```

The exact min-cost-flow slice optimum confirms the formula on every
tested even n. Scope caveat: the flow is solved on a pad-4 padded
window; enlarging the window can only lower the optimum, so the "no"
rows are certified only within the truncation. The costs are
unchanged at pad 6 (archived check), which supports but does not
prove window-independence:

```text
n     c2(flow)  = 2n^2+4n   F_slice   dL     2^dF < 7^dL
8     160       160         384       128    no
10    240       240         580       200    no
12    336       336         816       288    no
14    448       448         1092      392    yes
16    576       576         1408      512    yes
```

**The first slice on the falsifier side is n = 14**; n = 16 gives
the cleanest exact margin, since `dF/dL = 11/4` there and the already
frozen inequality `2^11 = 2048 < 2401 = 7^4` decides it directly.
**The slab branch is not dead**; it is a second
candidate falsifier family, potentially simpler than the
checkerboard, provided its explicit slice filling and finite caps are
exhibited. Caveats: `F_slice = 5n^2 + 8n` is the optimum inside the
flow ansatz (dir-1 pattern fixed, dirs 2/3 as unit-capacity flow, no
third-party absorption); a universal slab lower bound is open in both
directions.

## 4. Ternary closure is capacitated relative homology, not homology

**[correction adopted from the owner audit]** With
`d = 5j - partial n_bulk` one has `partial d = 0`, and trivial
compactly supported H_1 of Z^4 yields an unrestricted integer m with
`partial m = d`. It does not yield `m_f` in the residual capacity
sets `A_f = {a : n_bulk(f) + a in {-1,0,1}}`, nor bounded shells or
costs. The honest statement: null-homology removes the unrestricted
integer obstruction; existence and cost of a ternary bounded-shell
extension is a capacitated problem that must be solved case by case.
The experiment record illustrates this: with the original
fixed-formula bridge placement, the rings-6 shell was solver-reported
infeasible (archived log `run_6366_r6.log`); a rings-8 run with the
same placement was likewise solver-reported infeasible, but that log
was overwritten and is not archived. The obstruction itself is
reproducible exactly, independent of any solver: the archived
`legacy_bridges_demo.py` replays the original placement and the
five-of-six diagnosis prints 17 locally unfillable charged edges at
`(6,3,6,6)` (two blocked slots leave only four servers) and 0 at
`(4,2,4,4)`, which is why the smallest instance succeeded by anchor
luck.

## 5. Bridges: two separate lemmata

**Current splice [candidate-T]:** the reroute is `j' = j +- partial f`
at a square where the neighbor layer carries the opposite pattern
sign; it cancels two old edges, adds two new ones, preserves
`partial j = 0`, ternarity, and L, and joins the two plane supports.
Anchors are searched under the local five-of-six check until clean
(`_local_ok`); all shapes tested pass with zero locally unfillable
edges.

**Filling splice [open in general]:** a compatible ternary change
`n -> n'` with `partial n' = 5j'` and controlled cost is exactly the
capacitated closure problem of section 4. It is established here only
instance-wise (the MIP found it, the integer recheck confirmed it).

## 6. Dichotomy and the pump target

**[candidate-D]** Writing `F = 2L + T` for a finite checkerboard
droplet, the certificate condition is `2^T <= (7/4)^L`. Either the
closure tax is `o(L)` and large droplets certifiably cross (which the
L = 3240 witness now instantiates at T = 1513 <= 2615), or a positive
universal kappa needs a linear confining tax. On the candidate
reading of the witness, no such tax is available on this surface, and
the local combinatorics alone would then not rescue a universal
coefficient above `log2 7`; both statements inherit the witness's
candidate-C standing and become firm only through the formal probe.

**Pump lemma [next target, candidate-T when built]:** an open block
with equal left/right boundary syndrome and increments
`2^dF < 7^dL`, plus two finite caps, yields for k copies
`L_k = L_c + k dL`, `F_k = F_c + k dF`, and `2^(F_k) <= 7^(L_k)` for
every sufficiently large k: an exact counterexample *family* rather
than one instance, with the crossing k explicit. Both branches
qualify: checkerboard slices (`dF = 2 dL`, `2^2 < 7`) and slab n = 16
slices (`dF/dL = 11/4`, `2^11 < 7^4`). This, not a larger closed 4D
MIP, is the right next construction; the witness caps themselves are
candidate cap material.

## 7. Artifacts

```text
notes/kappa-witness-2026-08-03/
  witness_6_3_6_6.json    the pair (j, n): L = 3240, F = 7993
  verify_witness.py       standalone exact recheck (PASS); its
                          consequence line is candidate-labeled
  kappa_lib.py            face/coface conventions as the public
                          verifier; edge_d is the induced 1-boundary
  checker_witness.py      current + bulk builder
  repair_witness.py       bridges (searched anchors) + shell MIP
  build_witness.py        slab machinery + exact 2D flow
  flow_scan.py            the slab slice table above
  local_identity.py       exhaustive window check of section 2
  diagnose_local.py       five-of-six local feasibility audit
  legacy_bridges_demo.py  replays the pre-fix bridge placement and
                          its 17-edge local obstruction
  cluster_repair.py       clustered repair variant
  runjob.sh               the archived solver invocation
  run_6366_r6.log         rings-6 legacy-bridge infeasible record
  run_6366_r8.log         the successful rings-8 run record
  adversarial_check_fresh.py  independent re-implementation used by
                          the adversarial verification pass (PASS)
```

Independent replay: `python3 verify_witness.py witness_6_3_6_6.json`
from that directory (Python standard library only). An adversarial
verification pass (four independent auditors: fresh verifier
re-implementation, convention and scope audit against the public
verifier and the predefinition, exact big-integer arithmetic audit,
and a hostile read of this note) returned CONFIRMED on all four
tracks; its corrections are incorporated in this revision.

## 8. Status matrix

```text
five-of-six rigidity                      candidate-T
even balance on uncharged edges           candidate-T
checkerboard identity partial n = 5j      candidate-T
periodic bulk F/L = 2                     candidate-T
F >= 2L for frozen checkerboard current   candidate-T (scoped)
three-direction no-go                     candidate-T (scoped to ansatz)
slab F_slice = 5n^2 + 8n (ansatz)         candidate-C (flow-verified 8..16)
slab >= 3 for every n                     WITHDRAWN (false; 5/2 + 4/n)
witness L = 3240, F = 7993                exact feasibility after
                                          independent recheck; public
                                          value at most C, one machine
HiGHS optimality inside rings-8 shell     solver-reported only
ternary closure from homology             WITHDRAWN (capacitated
                                          relative homology instead)
boundary-order tax in general             open; instantiated once
public Canon / frontier change            none
```

## 9. Route to the public record

Per the predefinition checklist (section 11): freeze `S_kappa` with
the certificate scope block above, resolve issue #200 review, then
`P-PHOTON-KAPPA-LEMMA-1` preregisters the witness-checking verifier
and the committed witness JSON and runs the two-architecture gate. If
and only if every gate passes, the kappa route of
`PHOTON-WINDOW-PROOF` would close negatively as CANDIDATE-REFUTED for
every coefficient satisfying (K2); no outcome is asserted here. The
roughening-certificate route of the parent is untouched either way.

Suggested admissibility sentence for the future preregistration
(removes the only residual scope ambiguity): "A certificate current j
is admissible iff j is in C_1^c(Z^4; {0,+1,-1}), partial j = 0, and
supp(j) is connected; repeated vertices (support degrees 4 or 6) are
admissible, and vertex-simplicity / degree-2 support is not
required."
