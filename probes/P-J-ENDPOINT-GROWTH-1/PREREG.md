# P-J-ENDPOINT-GROWTH-1

Status: preregistered public probe candidate, RESULT-EXPOSED, proof-first.
Owner: A. M. Thorn / ChatGPT endpoint-growth-20260929.
Public lock: #1278.
Branch: probe/P-J-ENDPOINT-GROWTH-1.
Source: public main c1cfe0751c65ce9ffb680aa7decd99d83600409f.
Authority: Public Canon v92 ACTIVE.
Action layer: L1 mathematical carrier only.

## 1. Frozen equation and target

Let O=Z[zeta_5], J=1+zeta_5^2, phi=(1+sqrt(5))/2 and
D={u+v*zeta_5: u,v in {-2,-1,0,1,2}}. A_0={0} and
A_n=sum_(k=0)^(n-1) J^k D, with exact equality in O. Every source word in D^n
is admitted, independently at every position. A fixed initial carrier only
translates A_n by J^n alpha_0.

Prove for every integer n>=0:

    phi^(2n) <= |A_n| <= C*phi^(2n), C=93890+41760*sqrt(5),
    lim_(n->infinity) log|A_n|/n = 2 log(phi).

The note-local O-J-ENDPOINT-GROWTH-LOWER-BOUND from
notes/C-J-SOURCE-PHASE-READOUT-MEMORY-N is the motivating question, not a
normative Frontier row. No public H/O row is closed by this probe.

## 2. Frozen code

The accepted standard-library verify.py is committed with this preregistration
and PROOF.md. Record commit and SHA-256 values publicly and read the bytes
back before formal execution. No import, execution or formal replay of this
probe precedes that pin. Static AST and hash checks are allowed.

The source uses exact integers and Fraction arithmetic in Z[zeta_5] and
Q(sqrt(5)), including exact order comparisons by rational squares. It has
no random input, floating-point scientific assertion, external data or
third-party implementation.

## 3. Frozen carrier, proof certificate and finite inputs

In the expanding embedding eta=zeta_5^2 and beta=1+eta^2=-phi*eta,
use P={a+b*eta: |a|,|b|<=1/2}. In the real basis (1,eta), multiplication by
beta has matrix B=((0,phi),(-phi,phi^2)), determinant phi^2 and absolute row
sums phi and 2+sqrt(5), both below five. The exact union of the 25 digit
translates of P is 5P. Thus beta*P is contained in sigma(D)+P; iteration
and area prove the lower bound. PROOF.md also supplies the upper bound by
four-dimensional norm packing, with all constants written explicitly.

The finite audit checks:
- integer carrier matrix and cyclotomic identities for eta,beta and phi;
- determinant and exact covering row inequalities;
- nine half-integer sample points in P (18 coordinate checks) and the exact
  five-interval partition; the all-point covering is proved analytically;
- the exact algebraic upper constant;
- complete endpoint census for n=0..4: 1,25,625,5449,27233;
- both exact cardinality inequalities at each of those five n.

No finite census alone establishes the all-n theorem.

## 4. Systematics and exposure

The all-n proof, constant-one target and finite census were already exposed
in NON-CANONICAL incubation. One incubation code attempt raised a Python
TypeError from missing reflected scalar comparisons. Its narrowly repaired
successor and an independently implemented exact audit passed. That was not
a failed mathematical inequality or a public probe. Its failed-run transcript
is not imported. This source derives from the repaired implementation.
Publication is not retroactive preregistration or blind confirmation.

An independent mathematical review checked both bounds, the exact constant,
the distinction between positive real phi and sigma(phi), and the scope.
A separate code review will inspect the public frozen source. Public
architecture reruns are reproductions, not independent proof discovery.

## 5. Frozen falsifiers and execution conditions

A scientific falsifier is an exact admitted n, digit word/set, or proof
counterexample that contradicts a stated bound or an indispensable identity.
A false finite count, false exact covering prerequisite or false algebraic
constant rejects its frozen check. Preserve failures; do not move thresholds.
Authority, ownership, source/pin/hash, runtime, environment or evidence
integrity defects are STOP and are not a mathematical negative decision.

Follow POLICY.md, AGENTS.md and the current repository check_verifier.py
procedure. The first local formal command is

    python3 probes/P-J-ENDPOINT-GROWTH-1/verify.py

Use the repository deterministic environment and its unchanged verifier
budget. Record actual stdout, stderr, platform, architecture, Python, exit
status and hashes. The required clean x86_64 and aarch64 jobs must reproduce
the same EXPECTED.txt byte for byte. The pin is immutable after publication.

## 6. Status and scope

The written result remains candidate-T until a separate Canon fold. The
local finite audit is candidate-C before the required public architecture
replay. A successful probe changes no Canon or physical claim by itself.

No distribution on endpoints is supplied. In particular no Shannon entropy
lower bound or equality follows from endpoint cardinality. No completeness
of native U input words, physical decoder, event, occurrence, apparatus,
memory/reset implementation, physical entropy or L1-to-L6 lift is claimed.
The existing negative ENTROPY-LAYER-BRIDGE remains untouched.
