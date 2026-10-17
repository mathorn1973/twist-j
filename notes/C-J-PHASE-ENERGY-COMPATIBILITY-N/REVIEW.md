# Independent review of the frozen author files

PUBLIC / NON-CANONICAL / L1. Candidate C-J-PHASE-ENERGY-COMPATIBILITY-N.
Author identity for repository custody: A. M. Thorn.
SPDX-License-Identifier: Apache-2.0.

Review target: e690cda29eda557ddde8b3f7f486a42cd15858e4.

| File | SHA-256 |
|---|---|
| PROOF.md | ec900e0e56f40ab6a2da0cece37b96a478b0c6be90735bc315e489680afcbe54 |
| audit.py | 5964f71f6a5d835cfe8093e545893bc66fc96afb82b82199d3a1337169b66df6 |

The attack contract was committed at
f398cbe9e72b9dae2744feaeff0832100a30bd00. The independent analytical
derivation was then committed at
e3e7a58c8b98ce3982886aec93b2bd0348302923 before the author files above
were opened. DERIVATION.md records the complete exposure boundary,
including a coordinator summary and an auxiliary analytical model check.
This is separate model-context review in one assistant system, not
external peer review. The source verifier was not read or imported.

## Verdict

No mathematical counterexample or blocking proof defect was found at the
frozen, explicitly conditional scope. Part A and part B agree with the
independent derivation. The executable received static source review only;
no scientific program has run, and no finite-inventory execution result
is certified by this review.

## Analytical checks

The cycle criterion is both necessary and sufficient. Its construction
correctly handles cycle lengths divisible by five without division. The
funded gates are bijective on complete states: reversing the requested
sign gives the inverse accepted/rejected rule, and the controller phase
must be decremented first. Fixed-energy shells are finite. On every
actual branch the scalar area is exactly Delta u=Delta v over the
integers, so the two energy-zero/one length-four cycles force the unique
universal pair (0,0). The weighted-permutation conjugacy has the stated
sign: G P G^-1 contributes j^(u(Ts)-u(s)). Complete-state return is
correctly distinguished from a base q,p return.

The independent cold-preparation hand calculation gives B=0 period four,
energy two, and B=4 period 124, energy six. Both have area sum zero;
the resulting two F5 constraints independently force (0,0). The author's
whole-carrier proof does not depend on this longer trace, and its claim
that the separately planned cold audit remains a finite check is sound.

For B, unitarity, trace, determinant and branch range imply the specified
spectral equation. Direct differentiation gives omega''(0)=1/m. The
chain rule yields M_curv=B^2 m/A and the strict ratio m/atan(m)>1 under
the same declared positive linear calibration. The m=2 remark about
adding integer multiples of 2 pi is valid at that fixed rung; it is not
stated as an all-m theorem. The nonlinear shell and drift equality are
exact. The local chart restriction and global phase ambiguity are both
explicit. The integral proof of the signed weak-step rest bound is valid
for all epsilon,M>0 and claims only the rest limit.

## Nonblocking wording precision

In B2, the sentence that a universal energy zero is fixed by the massless
branch should be read together with the frozen literal E_phase=A omega
convention. The massless SPEED alone fixes A/B and does not fix an
additive energy offset. Equivalently, one can explicitly require the
massless zero-momentum energy to vanish. This precision changes no
preregistered formula or conclusion: an additive offset is already outside
the declared literal reading.

The nonlinear shell has only |phat|<=1 on this real-k carrier. Its scalar
identity and matching drift therefore do not supply unrestricted Lorentz
boost invariance, canonical equivalence, a physical inertia experiment,
or a global replacement for temporal eigenphase. The author's explicit
local and physical-scope restrictions are sufficient to prevent these
extensions. No further physical conclusion is certified here.

## Static executable review and outstanding execution

The inventory construction includes every complete E<=6 state: each
integer coordinate has absolute value at most two, and range(7-H) gives
exactly all admissible banks. Both signs and every controller value are
included. The forward and inverse implementations match the exposed
rules; rejection preserves integers and bank while flipping sigma.
The audit checks energy closure, both inverse compositions, integer
coboundaries, a disjoint complete-cycle partition, integer zero cycle
sums, all 25 coefficient pairs, and the four declared witnesses. The two
cold cycles receive their own coefficient-pair check. Counts and witness
periods are printed rather than used as fitted thresholds. All arithmetic
is integer arithmetic, and the only import is standard-library itertools.
It neither imports the source verifier nor reads runtime data.

The program's PASS/FAIL flags and zero exit for a scientific failure
match PREREG.md. An exception, timeout or stderr remains an execution
failure under that contract. Static inspection is not execution evidence.
Public source readback is still required before the first scientific
runtime. No RUN.md, exact stdout, architecture agreement, policy-CI
scientific reproduction, public pin, Canon promotion or native/physical
admission is implied by this review.
