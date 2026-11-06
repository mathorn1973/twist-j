# Immutable sources and attribution

**NON-CANONICAL. C-HODGE-INFINITE-CARRIER-N.**

## Public authority

The publishing session's authority gate uses `mathorn1973/twist-j` main,
Public Canon v104, with main/peeled activation tag
`e6240e2689bb22aab5f02bad90b75d3692bb96d9` and content commit
`4a50e527d20018839f006ed312454b710e6486b4`. These identify the basis of this
note, not a new authority. The user's historical uploaded compilations
are not inputs to any proof below.

## 1. Complete homogeneous capture and receiver source

[homogeneous_source.md](https://github.com/mathorn1973/twistj-handoff/blob/0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8/homogeneous-capture-2026-10-22/proofs/homogeneous_source.md),
`mathorn1973/twistj-handoff`, commit
`0b9bf39b3a5866fdb34c6f37711462dc8dd08ab8`, path
`homogeneous-capture-2026-10-22/proofs/homogeneous_source.md`.

Sections 1--3 define the object coin, Fourier/streaming convention, pulse
coin and edge, token/pulse arrangements, label allocation, and capture
rotation. Section 9 defines the receiver and its old-label swap.
PROOF sections 2--3 re-express this already specified law. In particular,
the local recurrence is not a new derivation of those construction choices
from J.

## 2. Complete physical cut and native encoded current

[PROOF_CURRENT.md](https://github.com/mathorn1973/twist-j/blob/d221e10747e009cb1315295a258f1d48e8b75bce/notes/C-HODGE-SPATIAL-CUT-N/PROOF_CURRENT.md),
`mathorn1973/twist-j`, commit
`d221e10747e009cb1315295a258f1d48e8b75bce`, path
`notes/C-HODGE-SPATIAL-CUT-N/PROOF_CURRENT.md`.

Equations (C1)--(C4) define the entire encoded sector, physical charge
weights (2,2,4,2), and layer order. Equations (C6)--(C17) derive the current,
receiver-edge cross term, and exact bilinear continuity. PROOF section 3
restates these identities in the explicit recurrence notation. The
infinite +/-2 eigenspace construction and the full-domain finite-factor
obstruction in section 6 are new consequences of that unchanged current.

The source's larger native occupied-state extension is not replaced by
the fixed encoded charges; no additional claim about that extension is
made here.

## 3. Open-channel reduction and normalization

At commit `b4696efa4fcb56cef8883fb593d2ab571bdcd047` of
`mathorn1973/twist-j`:

- [PROOF_REDUCTION.md](https://github.com/mathorn1973/twist-j/blob/b4696efa4fcb56cef8883fb593d2ab571bdcd047/notes/C-HODGE-OPEN-CHANNEL-N/PROOF_REDUCTION.md)
  defines the actual block system, complete incoming token state, causal
  reconstruction, and valid cyclic preparation sector.
- [PROOF_PORT.md](https://github.com/mathorn1973/twist-j/blob/b4696efa4fcb56cef8883fb593d2ab571bdcd047/notes/C-HODGE-OPEN-CHANNEL-N/PROOF_PORT.md)
  equations (P1)--(P7) define T, the normalized contact vector, F and
  s=(4-F)/(4+F). The present note rederives that last identity. Its
  nonrationality proof does **not** use the candidate positive-density
  result (P24).
- [PROOF_CURRENT.md](https://github.com/mathorn1973/twist-j/blob/b4696efa4fcb56cef8883fb593d2ab571bdcd047/notes/C-HODGE-OPEN-CHANNEL-N/PROOF_CURRENT.md)
  equations (DN2)--(DN6) define the normalized dark-state example.
  PROOF section 7 explains why its normalized 2 sqrt(2)/5 and an
  unnormalized 8/5 pairing are consistent, and why that example does not
  invalidate a prior restriction of allowed initial states.

The scientific verifier and breaker of this predecessor were neither read
nor executed in the analytical authoring or review tasks.

## 4. Canonical complete-operator spectral gap

[CANON.md, CONTACT-W-SPECTRAL-READING](https://github.com/mathorn1973/twist-j/blob/4a50e527d20018839f006ed312454b710e6486b4/canon/CANON.md),
Public Canon v104 content commit
`4a50e527d20018839f006ed312454b710e6486b4`.

This registered [T] theorem concerns exactly
W=exp[-i(2pi/5)P0] S ((I+2iX) tensor (I+2iX))/5 with the same streaming
convention. It proves two open gaps of width at least
acos(7/25)-2pi/5>0 for the full operator, not only a selected momentum
fiber. Multiplication by exp(-i beta) rotates the gaps. This is the only
spectral-support input to PROOF section 5 beyond the spectral
representation of a unitary operator.

## New and restated content

The lattice recurrence, local charge and current are explicit restatements
of the above source. The extreme-coordinate theorem, the gap-plus-infinite-
cyclic-span nonrationality proof, and infinite full-current-index theorem
are the new analytical content. The elementary gap lemma includes its
Poisson-measure argument in full. No external theorem is invoked to infer
a physical continuum, a Hodge action, or an occurrence law.
