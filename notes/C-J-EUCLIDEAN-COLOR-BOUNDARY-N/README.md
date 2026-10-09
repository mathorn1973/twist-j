# C-J-EUCLIDEAN-COLOR-BOUNDARY-N

Status: NON-CANONICAL. No authority. L1 scalar arithmetic only.
Owner: A. M. Thorn / session J-COLOR-20261009. Issue: #1433.
Public basis: Canon v100, main c164b79ce134152ac7cd600421791df74113f29f.

## Result

For both Z[zeta_5] and Q(zeta_5) in their specified complex scalar embedding,
the exact unit-distance graph is three-colorable with chromatic number three.
Allowing both lengths 1 and phi already forces five colors, and the union of
all phi-power lengths still has chromatic number exactly five. Each exponent
parity separately has chromatic number three.

The complete chosen nonzero additive scalar-chart class with one constant
response to J consists of the four Galois embeddings times a nonzero complex
constant. The complete chosen nonzero additive F5-reader class with one
constant response to J consists of the four nonzero multiples of reduction
modulo 1-zeta_5. Normalizing the value at one selects that residue reader.
These are chosen mathematical classes, not all physical decoders.

The residue reader has no positive uniform Euclidean distance margin:
0 and 1-phi^(-4n) have equal residue and a distance tending to one. All five
residue fibers are dense in the single complex image. A joint position and
residue read has product closure C x F5 and update (z,r)->(Jz,2r), using an
explicit product topology rather than the scalar Euclidean topology alone.

Separately, any finite chromatic obstruction in the full plane transfers to
every positive-width distance band on a dense carrier. The annular lower
bound six is explicitly CONDITIONAL on the external E6 theorem. That Lean
build is not reproduced by this note or by its Python audits.

## Evidence and reading order

1. PROOF.md: self-contained arguments and complete scope boundaries.
2. RESULT.md: status and decisions, including the failed robustness property.
3. PREREG.md: scope frozen and pushed before either script ran.
4. verify.py and break.py: two exact representations, frozen together.
5. EXPECTED.txt and RUN.md: byte-identical finite audit output and run record.
6. REVIEW.md: same-session adversarial review, not independent-agent review.
7. SOURCES.md: immutable source pointers and external-dependency boundary.
8. PROMO-C-J-EUCLIDEAN-COLOR-BOUNDARY-N.md: later-review proposal only.

Written arguments are candidate-T. Finite audits are candidate-C, with one
x86_64 execution architecture. Neither a second representation nor the
ordinary notes-only CI creates a two-architecture science gate.

From the repository root:

```sh
python3 notes/C-J-EUCLIDEAN-COLOR-BOUNDARY-N/verify.py
python3 notes/C-J-EUCLIDEAN-COLOR-BOUNDARY-N/break.py
```

Both commands produce the committed EXPECTED.txt bytes. The repository
reproduction runner can also audit this layout without registering it as a
minimal reproduction:

```sh
python3 -c 'from pathlib import Path; from tools.check_reproduce import reproduce; reproduce(Path("notes/C-J-EUCLIDEAN-COLOR-BOUNDARY-N").resolve())'
```

No claim is made about a native Omega-to-scalar map, physical distance,
phase acquisition, energy, force, event measure, topology or proton.
No Canon, registry, frontier, gate or workflow is changed.
