# Preregistration: two-trace residue inversion

PUBLIC, NON-CANONICAL incubation. No authority. Action layer: L1 only.
Owner: A. M. Thorn / thorn-jtrace-20260929. Issue: #1281.
Date: 29 September 2026. License: Apache-2.0.

## Basis and prior knowledge

Public main and tag canon-v93: d708d887f3dbf92ae02115d92ecf12d581db72b5.
Content commit: 138eb9af93ca94d5f95531e46301ed23718fc07d.
Canon SHA-256: 9002c1c0f299f0226fa5ebc05747b0f0be1a11465279f35ee6e43a79f6ccaa21.
Canon bytes: 807444. All five normative hashes, ancestry, repository activation
validator, downloaded release manifest and required publication checks passed.

Public inputs: J-PROJECTIONS, J-STEP, J-UNIT-STRIP-NORMAL-FORM,
J-SCALAR-CODE-CAPACITY-3125, U-COUNTER-REACHABLE-AMPLITUDE-CLASS.
QDD-GALOIS-SUM-RATIO supplies context, not a physical measurement mechanism.
The relevant proof/evidence is in P-ZETA5-RESIDUE-STRIP-DECODER-2 and
P-U-COUNTER-AMPLITUDE-CLASS-1. These completed probes are not resumed or edited.

The preceding conversation already proposed the identities and injectivity
proof below. Its assertion of 1000 unpinned prototype tests has no recovered
code or transcript in this session and is not evidence. This pin governs a new
prospective audit, not a retrospective registration of that assertion.

## Equation and carrier

O=Z[zeta], Phi_5(zeta)=0, J=1+zeta^2, phi=-zeta^2-zeta^3.
Equality is exact equality of four coefficients in (1,zeta,zeta^2,zeta^3).
For alpha != 0 let A=|sigma_1(alpha)|^2, B=|sigma_2(alpha)|^2,
S0=A+B=Tr(alpha*bar(alpha))/2, S1=S(J alpha), N=AB.
The primary domain is {alpha in O: 1<=N(alpha)<=941}.
The primary reader is (S0,S1,alpha mod25 O). Its two traces refer to a PURE J
step; an affine source insertion is outside that observation model.

## Frozen tasks

A. Derive S0=2u+v, S1=3u-v, u=(S0+S1)/5, v=(3S0-2S1)/5,
N=(3S0S1-S0^2-S1^2)/5, and S(n+2)=3S(n+1)-S(n).
B. Prove injectivity of (S0,S1,alpha mod m O) when m^4>16X and N<=X.
C. Give a total-on-image, terminating exact inverse at X=941,m=25,
including integer strip normalization and a proved coefficient box [-8,8]^4.
D. Audit all coefficients in [-8,8]^4; retain the entire oriented B_941,
check the public counts B_940=3110, B_941=3150, and decode every J^k beta
with beta in B_941 and k=-16,...,16. Stress fixed strip indices
0,1,2,3,4,5,6,7,8,9 with exponents -1024,-257,257,1024.
E. Preserve the known mod5 collision (5,5*zeta), strip endpoints, invalid
input rejection, and a pure-versus-affine-step control. A valid record
corrupted into another valid record need not be detected: no error-correction
claim is made.
F. Census distinct (S0,S1,residue) keys for m=5 and m=25 on the complete
B_941. Determine the first collision norm for m=5 within this domain and
whether its keys can encode 3125 labels globally over pure J orbits. The
answer is NOT preregistered as success or failure. No search beyond N=941 and
no smallest-modulus claim is included.
G. A separately implemented same-author adversarial audit uses cyclic
five-coordinate polynomial convolution, conjugation, norm, and a complete
[-9,9]^4 box. It imports neither decoder.py nor verify.py. Compare the two
complete strip digests and census records only after both codes are frozen.
This is method separation, not blind two-agent independence.

## Code and deterministic execution

Freeze this file, PROOF.md, decoder.py, verify.py, break.py and README.md
in Git, push, and publicly read back the commit before first audit execution.
Only compilation/static inspection may precede the pin.
Python standard library, exact Python integers, no floating point or random
sampling, PYTHONHASHSEED=0, LC_ALL=C, TZ=UTC, PYTHONDONTWRITEBYTECODE=1.
Commands from repository root:

    python3 notes/C-J-TWO-TRACE-RESIDUE-DECODER-N/verify.py
    python3 notes/C-J-TWO-TRACE-RESIDUE-DECODER-N/break.py

Budget: 120 seconds per script. Any exceeded budget or nonzero exit is recorded
without a mathematical conclusion for that failed execution. Codes and scope
are not changed to conceal a failure. Scientific stdout and empty stderr are
recorded separately, with SHA-256 and byte counts, after execution.

## Failure threshold and systematics

Exact equality, zero tolerance. Any false identity, admitted collision of the
m=25 reader, failed round trip, false strip/coefficient bound, public-count
mismatch, or invalid accepted output is a failure, preserved before any
successor is considered. Unknown census answers are boundary information,
not a moved threshold. Check signs of the J exponent, the half-open strip,
nonzero support, the ramified quotient O/25O (not a finite field), and the
unbounded integer information carried by the traces.

## Ceiling and exclusions

Written proofs: candidate-T pending independent review. Finite census and
execution: candidate-C. This is not a formal public probe and a notes PR's
repository checks do not execute these scripts as a two-architecture
scientific gate. A later formal probe must have its own accepted immutable pin.
No Canon, Registry, GATES, workflow, original probe or apparatus-note edits.
No physical clock, source mechanism, native language completeness, Born law,
occurrence, apparatus completeness, SI scale, photon/RH closure, or layer lift.
