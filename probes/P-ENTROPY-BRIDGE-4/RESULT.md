# P-ENTROPY-BRIDGE-4 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS

## Scientific decision at the recorded leg

```text
RESULT 8/8 ALL PASS, exit 0, stderr empty.
```

All eight preregistered gates passed on the first formal execution of the
pinned verifier. The immutable preregistration pin is
`3ad1e240da540840a4dd898a57ba48fa9716047e`, public lock issue 33, initial
base `da5c3423891390a7960522232a73c1a6fad17db3`. The formal evidence commit
`7b0e04819d513d3eddf50727ccb49e6377c020b9` adds only `EXPECTED.txt` and
`RUN.md`; it does not alter `PREREG.md` or `verify.py`.

Recorded aarch64 leg:

```text
platform:       Ubuntu 24.04.4 LTS
architecture:   aarch64
python:         3.12.3
stdout sha256:  6c93f74845471f46470fd504344780d58306dbd099f6384ead4156ce74a282c4
stdout bytes:   1916
stdout lines:   39
stderr bytes:   0
result:         8/8 ALL PASS
```

Two-architecture record:

```text
aarch64 leg    Ubuntu 24.04.4 LTS, CPython 3.12.3, neutral environment;
               first formal execution; RUN.md in this directory.
x86_64 leg     GitHub check on pull request 34, head
               fc55c4a87122c36b553a68ae4eeea3f744ca9485;
               run 29366414776, job 87199009061, conclusion success;
               Ubuntu 24.04 runner, CPython 3.12.13; verifier
               byte-identical (4d3ad9eb...), stdout byte-identical
               (6c93f748..., 1916 bytes); log carries
               VERIFY PASS P-ENTROPY-BRIDGE-4.
gate:          PASS. The aarch64 and GitHub x86_64 outputs are byte-identical.
```

## Recorded finite outcomes

```text
G01 CORE
    The public census reconstructs a recurrent core of 6250 states on 313
    components: 312 of size 20 and one of size 10. The two living halves are
    disjoint and have 3125 states each.

G02 ARITHMETIC
    J^10 + 1 lies in lambda^6 O but not lambda^7 O. J^2 + 1 lies in lambda O
    but not lambda^2 O. These are exact regular-representation membership
    decisions modulo 25 at the preregistered depths.

G03 FRAME
    Each recurrent component is invariant under both branch letters. For
    k = 0..10, both block labels, and both source halves, Phi^(k)_eps maps
    bijectively onto H_((eps+k) mod 2).

G04 PENTAGONS
    The level-0 vertex groups are trivial. On every component and half, the
    level-k vertex groups for k = 1..10 are cyclic of order five and have one
    constant orbit partition into five-cells. Every size-20 component half
    has two cells and each singlet half one, giving 625 = 5^4 pentagons per
    full living half.

G05 EQUIVARIANCE
    Both one-tick branch maps carry every canonical pentagon cell onto one
    canonical pentagon cell. The pentagon partition is a finite dynamical
    quotient on the declared carrier.

G06 QUOTIENT
    The induced vertex holonomy on the pentagon-class quotient is trivial for
    k = 1..8.

G07 AFFINE
    In the preregistered coherent level-2 gauge, every level-k cell map for
    k = 0..10 is affine over F_5. All 313 components have the same frozen
    (a,b) spectra, and the rows repeat with period four for k = 1..10. This is
    a gauge-specific finite statement; no gauge-independent identification
    with the lambda-digit action is earned.

G08 BOUNDED-NOGO
    The component-local cylinder system has zero solutions in all 900 frozen
    cases: the singlet and canonical size-20 component at L = 4..16, three
    cursor positions, and clocks 1,2,4,5,8,10,16,20,32,40,80, plus the
    singlet at clock 4 through L = 30. This does not quantify over every
    component, clock, or window.
```

No preregistered falsifier fired on the recorded leg.

## Scope and non-conclusions

The earned statement is finite and computation-grade only: the
pentagon quotient, equivariance, frozen quotient holonomy, frozen affine
cocycle table, and the exactly enumerated bounded no-go cases. In particular:

- the literal depth-five bijection is not declared formally dead;
- no ergodic-atom or spectral theorem is claimed;
- no all-scale persistence, measurable cohomology decision, or inverse-limit
  factor is established;
- no regularity, measure transport, L2 lift, or physical reading follows;
- `ENTROPY-LAYER-BRIDGE` remains open.

Folding a reproduced outcome into the registry, frontier, or Canon is a
separate sealed step. This probe changes only
`probes/P-ENTROPY-BRIDGE-4/`.
