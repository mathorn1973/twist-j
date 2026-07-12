# Cutover audit (working document, GENESIS)

Review material, not part of the normative Canon. This file may name
internal artifacts once; the public series never inherits their
numbering. Session synthesis-canon-v1-s1, 2026-07-12.

## Frozen synthesis basis

```
internal version   v184 (sealed)
source HEAD        f51955d7 (mathorn1973/twistj-jam, main)
lock               2e2c399e83effd2f24051da01ea1608ba80cf903
Canon file         TWIST_J_Canon_v184_ALL_IN_ONE.md
SHA-256            cd92b8bba54658e154e8fc05eb562749f04c70b134dcc728c7236ed10378ef80
byte count         230406
```

Reading surface: the sealed internal consolidation at v1/ of the
internal repository (canon pin 7c41d949, gate commit f51955d7), byte
equal to v184 content with the dated fold parts retired. If the
internal basis moves during synthesis, stop and re-freeze.

## Claim mapping (grows with the registry)

Rule: every public claim maps to an internal claim of equal or
stronger status and at least the same scope. Missing support lowers or
omits; nothing is invented. Public statuses here are deliberately
conservative pending public probe machinery.

```
public claim id                internal source (status)             public
J-UNIT                         Part I unit facts (T)                T
J-PROJECTIONS                  Part I two projections (T)           T
PI-FROM-J                      Part I, Li_1(J) = i pi/5 (T)         T
J-GOLDEN-BRIDGE                kernel facts, glossary (T)           T
J-STEP                         step map, M_J columns (T)            T
J-MODULUS-CHORD                J Jbar = 2 - phi (T)                 T
J-TENTH-ROOT                   T-J-SHADOW rung 7 (T)                T
J-RAMIFIED-CHORD               T-PLENUM-RAMIFIED-CHORD (T)          T
PLENUM-POINT                   T-PLENUM-J-FORM, -BACKBONE-VALUE,
                               -INTEGER-SKELETON (T, LOCK cand)     T
ALPHA-SEED                     the alpha exact lemma (T-LOCK)       T
BORN-FACE-WEIGHTS              D-KCM-MAGNETIC-EMERGENCE weights;
                               the eight exact identities (T)       T
CENSUS-313                     SS85.12 census; hosting corollary (T)
                               conservative public grade            C
CENSUS-Z5-SHEET                D-CENSUS-Z5-SHEET (D)                C
CENSUS-PAIRING                 D-PAIR-MAP (D)                       C
CENSUS-HOSTING                 T-HOSTING (T)                        C
BORN-HALF-ANGLE                T-BORN-HALF-ANGLE (T-LOCK); the norm
                               gate now publicly evidenced          T
BORN-RESIDUAL-SPLIT            T-BORN-RESIDUAL-SPLIT (T-LOCK)       T
SPIN-BISECTOR                  T-SPIN-BISECTOR (T-LOCK); finite
                               shadow scope, no positivity          T
BORN-ORDER-STAIRCASE           T-BORN-ORDER-STAIRCASE (T-LOCK)      T
METRO-ADMISSIBILITY            O-METRO-ADMISSIBILITY residual       O
METRO-EDGE-SCALE               O-METRO-EDGE-SCALE + SI clause       O
LORENTZ-A2A3                   O-LORENTZ-A2A3                       O
QUANT-SUBSTRATE                O-QUANT-SUBSTRATE                    O
COLOR-MEASURE-SELECTION        O-A18-COLOR-MEASURE-SELECTION        O
TT-GAUGE-PULLBACK              O-TT-GAUGE-PULLBACK (Stage B)        O
TT-SOURCE                      O-TT-SOURCE                          O
QNM-LEAVER-MU                  O-QNM-LEAVER-MU                      O
POL-READ                       O-POL-READ                           O
TT-VECTOR-STATE-NORMALIZATION  O-TT-VECTOR-STATE-NORMALIZATION      O
FRW-INHOM                      O-FRW-INHOM                          O
DRESS-CROSSCOUNT               O-DRESS-CROSSCOUNT                   O
NS-TILT                        O-NS-TILT (H, falsifier live)        H
DE-CONFORMAL-WEIGHT            O-DE-CONFORMAL-WEIGHT                O
ALPHA-S-RUNNING                O-ALPHA-S-RUNNING                    O
SCHEME-DICTIONARY              O-SCHEME-DICTIONARY                  O
FIBER-THRESHOLD                O-FIBER-THRESHOLD                    O
GENERATIONS-L3                 generations at the E_SM L3 frontier  O
ETA-ALTERNATOR-BRIDGE          CB4 + O-ETA-ALTERNATOR-BRIDGE        O
SPIN-LIFT-FORCED               O-SPIN-LIFT-FORCED                   O
KC3-PLENUM-READOUT             H-KC3-PLENUM-READOUT                 H
QUADRATIC-ENVELOPE-DECODER     H-QUADRATIC-ENVELOPE-DECODER         H
TM-SYM2-MEASURE                H-TM-SYM2-MEASURE                    H
QUADRATIC-DECODER-DATA         O-QUADRATIC-DECODER-DATA residual    O
NEUTRON-DELTA-EM               O-NEUTRON-DELTA-EM                   O
PROTON-RESIDUAL-IS-QCD         O-PROTON-RESIDUAL-IS-QCD             O
SQRT-PHI-TIME-GRAVITY          O-SQRT-PHI-TIME-GRAVITY              O
OBSERVER-WRITE-PORT            AX-CW at H; the write port test      H
PHOTON-RADIATIVE-INDEPENDENCE  O-PHOTON-RADIATIVE-INDEPENDENCE      O
```

## Intentional omissions so far (to be resolved before the PR)

Internal claims stated in the Canon text with their labels but not yet
registered, pending public evidence (reproduction or inline
derivation): the hyperplane and codec claims;
the Dirac ladder theorem layer; the color ladder
rungs; the gravity chain (capacity, FRW coefficients, bridge law); the
mass ladder values; Weinberg; the Maxwell closure; the alpha value
comparison; the cosmology register (w, Omega_b, dark matter ratio,
gyron density); the coupling and metrology arc theorems. Explicitly omitted
from the public frontier, with reasons: SIGMA3-PRIMITIVE (author
decision: an optional enrichment, not a gap; stays internal);
W1-INTERFACE-PRINCIPLE, KERNEL-BRAID, and TIMEQUANTUM-POTENTIAL
(deferred: no faithful public decision condition is stated yet; each
returns only with a concrete falsifier or decision condition). The
internal O17 residual stays deferred on the same ground. No claim is silently dropped. Each candidate is registered,
conservatively lowered, rewritten as non-claim material, or
explicitly omitted with a reason. The queue is
notes/synthesis-canon-v1.md.
