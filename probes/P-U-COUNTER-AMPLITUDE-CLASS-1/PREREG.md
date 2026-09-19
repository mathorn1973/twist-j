# P-U-COUNTER-AMPLITUDE-CLASS-1

Status: preregistered candidate, NON-CANONICAL. Action layer: L1 only.
Owner: A. M. Thorn / counter-amplitude classification session 2026-09-19.
Public lock: #1077. Branch: probe/P-U-COUNTER-AMPLITUDE-CLASS-1.
Source: public main 16e6bd3579527f522ca7e8c85411107f6873eea8,
Public Canon v89 ACTIVE. This is one new formal probe.

## Exposure and scope

The thirteen-component census, sign-quotient conjecture, and selector
obstructions were exposed before this pin. The structural formula and proof
were validated in merged note #1075. The 3125 retained labels and explicit
all-clock chart are already canonical U-NATIVE-CHART-AND-QDD-READBACK.
This probe formally audits their joint reader classification and exact
common-factor boundary. It is neither blind discovery nor a new claim that
the native dynamics retain 3125 labels. PROOF.md discloses its dependencies.

The separate P-U-J-HODGE-SEPARABLE-COUNTER-READ-1, lock #1069, retains its
owner and public pin 51672be0f697ce3d977fde20e93572382d9cf7ab. Its verifier
is not read, executed, changed or disposed of here. No ownership or result
is inferred for that probe.

## 1. Equation

Use exactly the five native affine maps a,b,c,d,e, phase z, two controls
f_t(x)=g_(z(x)+2t)(x), and theta_n=s_2(n) mod 2 in PROOF.md section 1.
All checkpoint arithmetic is modulo five. Let d_n=f_(theta_n),
E_0=id and E_(n+1)=d_n E_n.

For any set Y and stipulated bijection L:Y->Y require

    R(n+1,d_n(x))=L(R(n,x)).

Frozen targets, all with exact equality:

G1. The explicit kappa of PROOF.md section 2 changes by common sign
on every selected edge. Its 25 oriented fibres each have 625 heads,
125 per phase sheet. Q=[kappa] has precisely thirteen weak graph
components, sizes 625 once and 1250 twelve times. The H/G transient
excursions generate the full two-dimensional sum kernel, proving
connectivity rather than inferring it from a count.

G2. Whole-Omega separable readers R(n,x)=L^n F(x) are exactly
L^n g(Q(x)), with arbitrary g. On the origin-zero reachable domain
D={(n,x):x in E_n(F5^6)}, all counter-dependent readers are exactly

    R(n,x)=L^n G(ell_n(x)),  G:F5^5->Y arbitrary,

with ell_n the extended canonical chart in PROOF.md section 3.
Every ell_n is onto; ell_0 has 3125 fibres, each five heads, one of
each initial phase. No general whole-Omega nonseparable classification
is asserted. No preferred L or G follows from intertwining.

G3. Q=qbar ell_n on D, where

    qbar(alpha,beta,gamma,delta,epsilon)
        =[alpha+beta,gamma+delta].

The qbar fibres have sizes 125 once and 250 twelve times. Whole-Omega
separable readers restrict exactly to G=g qbar. This is a strict
subclass for targets with at least two points. Spanning a six-space
by finitely many assigned values is not surjectivity onto that space.

G4. Current phase or selector-index readers, with any counter dependence,
admit only constant source amplitudes for bijective target evolution,
because z_3=i_3=1 for every head. Complete histories distinguish exactly
five initial-phase classes. The map x->(ell_0(x),z(x)) is a bijection
F5^6 -> F5^5 x F5. Hence a source amplitude both recoverable from a
current full-checkpoint reader and from the selector history is constant.
No probability distribution or physical independence is claimed.

G5. An additional requirement that G be additive from (F5^5,+) to a
characteristic-zero vector space forces G=0. This is a conditional
torsion obstruction, not a no-go for arbitrary nonlinear amplitudes,
free function-space linearization, or a declared integer lift.

G6. The auxiliary static audit from #1075 is retained: [(u,v)] maps
injectively to (u^2,uv,v^2), giving 13 matrices, twelve nonzero over six
projective directions. It is not the entire determinant-zero cone.
The actual selected basis vector C^(2t)e_z differs from
(I+C^2)e_z, also modulo constants, over Z and F5. The latter static
operator on A4 is not a native update. No six-direction/Hodge-axis
identification or unique source torsor is asserted.

## 2. Code

Freeze PREREG.md, PROOF.md, verify.py and break.py in one public commit
before any execution. verify.py is a self-contained exact standard-library
audit. It contains the already disclosed structural audit and the new
chart/classification checks. break.py is written independently from the
proof and canonical affine formulas, without opening verify.py or the
incubation builder/breaker. Its graph traversal and chart audits supply
an implementation-independent falsification attempt, not blind discovery.
Both hashes are frozen before execution or output comparison.

Formal command, from repository root:

    python3 probes/P-U-COUNTER-AMPLITUDE-CLASS-1/verify.py

Independent command:

    python3 probes/P-U-COUNTER-AMPLITUDE-CLASS-1/break.py

## 3. Carrier and data

The complete declared finite source is F5^6: all 15625 checkpoints,
both selector controls, all five generator identities, all F5^5 chart
labels, all 25 oriented two-coordinate values and 625 terminal labels.
There is no external dataset, floating point, random sampling or tolerance.
The target theorem quantifies over stipulated sets and bijections; code
does not purport to enumerate all targets or prove that universal theorem.

## 4. Systematics

The builder checks the structural identities on the complete finite
carrier. It audits the extended chart along every head at ticks 0..31
inclusive, chart inverses at ticks 3..31, the five-head fibres and
the exact Cartesian head map, qbar projection and fibre counts. It checks
the clock recurrence for ticks 3..4095. The breaker independently traverses
the full undirected two-control graph, compares component memberships
with Q, and checks head fibres and chart conservation at ticks 3..15.
All-clock claims rest on the canonical proof and PROOF.md, never on finite
prefix extrapolation. Arbitrary-target classification, common-factor
constancy and additive zero are proved by cancellation and finite torsion.

Run after public readback in LC_ALL=C, LANG=C, PYTHONDONTWRITEBYTECODE=1,
PYTHONHASHSEED=0, TZ=UTC. Record exact stdout, stderr, exit, source hashes,
neutral platform, architecture and Python version. EXPECTED.txt is actual
first-run stdout. Required public replay is the unchanged repository
workflow on x86_64 and aarch64 plus aggregate check. Independent breaker
output is separately labelled and is not silently counted as a second
architecture.

## 5. Failure threshold

One exact failed identity, wrong fibre membership, missing head, wrong
count, or counterexample rejects its corresponding target. Any code or
custody defect is STOP. Preserve a failed first run; do not edit a pinned
verifier, proof, threshold or scope to recover the same identifier. An
incomplete failed gate is disposed of as ABANDONED under POLICY.md, with
the identifier consumed; a completed result is recorded at its earned
scope. No post-result redefinition of reader domain is permitted.

## 6. Action layer and deliverable

L1 only. Independently proved statements may earn candidate-T, remaining
NON-CANONICAL until a separate reviewed fold. Exact computation without
proof is at most candidate-C until the required reproduction gate passes.
Deliver proof, deterministic verifier and independent breaker, immutable
pin, exact outputs, neutral run records and a bounded RESULT.md. Record
public acceptance separately from local execution. No physical time,
physical superselection, occurrence, Born rule, SI or L2-L6 identification.
