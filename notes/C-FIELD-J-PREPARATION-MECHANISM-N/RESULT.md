# Counted local preparation of the coherent pointer supply

**PUBLIC, NON-CANONICAL. Accepted conditional L1 candidate-T: finite
approximate pointer-bank preparation and its complete Stage-C error bound.
Exact finite readiness, native physical realization and actual occurrence
remain open.**

Owner: A. M. Thorn. Original work, Apache-2.0. Recorded 2 October 2026
(Europe/Prague; first executions and CI dated 1 October UTC).
Issue [#1331](https://github.com/mathorn1973/twist-j/issues/1331), draft
PR [#1332](https://github.com/mathorn1973/twist-j/pull/1332).

## What has changed

The previous interface supplied an independent coherent E state for every
active and reserve pointer. This candidate replaces that black-box loading
operation, **to any specified positive error**, with a fully specified
finite sequence of local pointer/bath collisions. It counts every fresh
bath bit, retains every output and bounds the complete joint handoff error,
including pointer/source/environment correlations. It does not merely
rename a Fourier preparation or move an E state from another cell.

This is a conditional effective quantum model. The phase-sensitive local
interaction, its pulse area, pure bath inputs and external sequencing are
new explicit premises. Their availability has not been derived from
native U. Thus the exact E-bank premise of #1330 is not literally removed;
its operational role admits a controlled approximate replacement under
these additional hypotheses. The fixed Stage-C instrument is unchanged.

The [author proof](PROOF.md), independent
[proof](../C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/PROOF.md) and
[per-claim review](../C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/REVIEW.md)
establish F1-F7 within that scope. The review accepts all seven groups.

## Complete mechanism and finite resources

Set L=613, m=K+1. Even pointer mode j denotes the existing coordinate
p=2j. The newly declared internal graph is the cycle j to j+1 modulo L;
this is not a claim of spatial locality on the inherited B chain.
Let Z contain the source, its references and all other inherited fields.
The admitted initial state is any even-supported, possibly mixed and
correlated Omega on the m pointers and Z, together with B independent
bath qubits in the basis state zero. A concrete clean input is
|0><0| to the m-th tensor power times the supplied source/reference state.
It contains no coherent E pointer. Ready geometry and zero archive flags
are still supplied; source-code loading is still supplied.

For each edge use

\[
d_j=(|j\rangle-|j+1\rangle)/\sqrt2,\quad
s_j=(|j\rangle+|j+1\rangle)/\sqrt2,\quad
P_j=|d_j\rangle\langle d_j|,\quad Q_j=I-P_j,\quad
J_j=|s_j\rangle\langle d_j|.
\]

One fresh bath bit participates in the total reflection

\[
\nu_j=(d_j|0\rangle-s_j|1\rangle)/\sqrt2,\qquad
U_j=I-2|\nu_j\rangle\langle\nu_j|.
\]

The supplied Hamiltonian pulse is
H_j(t)=hbar g(t)|nu_j><nu_j| with integral g(t)dt=pi. It exchanges d_j|0>
and s_j|1> and fixes the orthogonal complement, including odd pointers.
It is self-inverse on every input, not only prepared ones. The zero-bath
reduction is Phi_j(rho)=Q_j rho Q_j+J_j rho J_j^*. Each pointer i receives
n_i complete ordered sweeps. The required number of distinct pure bits is

\[
B=L\sum_{i=1}^{m}n_i;
\qquad B=mLn\quad\hbox{for equal sweep counts}.
\]

For the prescribed ordered product W of the actual U operations, the
complete output is exactly

\[
\Omega_{\rm out}=W(\Omega\otimes|0^B\rangle\langle0^B|)W^\dagger
=\sum_{u,v}(K_u\otimes I_Z)\Omega(K_v^\dagger\otimes I_Z)
 \otimes|u\rangle\langle v|.
\]

All bath coherences and correlations survive in this expression. Reverse
operation order recovers the full input. There is no postselection,
measurement-based stopping or discarded bath refresh. Dirty baths have a
defined unitary evolution but do not satisfy the fresh-bath convergence
guarantee. Odd pointers and dirty archive flags are not repaired.

The extended bare ledger assigns equal energy to the bath levels and
adds B to the inherited ledger; every U commutes with it. This is not
thermal cooling or a calculation of physical drive work. Purity, storage,
phase alignment, pulse accuracy, clock and addressing remain resources.

## Uniform preparation and history error

Write P_E=|E><E|, E=L^(-1/2) sum_j |j>. On the even sector, one edge raises
F=Tr(P_E rho) by (2/L)Tr(P_j rho). The all-L proof combines the cycle gap
with the sequential no-jump loss to give

\[
1-F_n\le r_L^n(1-F_0),\qquad r_L=1-4/L^3,\quad L\ge3.
\]

P_E is the unique even-sector stationary density of a complete sweep.
The proof is analytic and uniform; finite small-matrix audits are not
extrapolated to L=613. This conservative rate makes no efficiency claim.

For arbitrary admitted correlations, put

\[
\delta=\min\{1,\sum_i r_L^{n_i}(1-F_{i,0})\},\qquad
\epsilon=\min\{1,\sqrt\delta+\delta/2\}.
\]

With D denoting half the trace norm and Z' including all retained baths,

\[
D(\Omega_{\rm out},P_E^{\otimes m}\otimes\Omega_{Z',\rm out})
\le\epsilon.
\]

The comparison uses the **actual remaining output marginal**, not an
invented independent fresh environment. The original Z marginal is
unchanged. For basis-blank pointers F_i,0=1/L. For any requested
0<epsilon_target<=1 it suffices to choose finite sweep counts with
sum_i r_L^(n_i)(1-F_i,0)<=4 epsilon_target^2/9. The registered audit checks
finite descriptors and exact rational certificates, not a full execution
of such a potentially enormous L=613 preparation budget.

One common admissible finite Stage-C CPTP protocol with at most K uses,
keeping preparation baths untouched, preserves the same joint epsilon
bound. Complete formal record distributions have total-variation error
at most epsilon, and each formal prefix weight differs by at most epsilon.
There is no horizon multiplier for the once-loaded bank. When both
p_actual and p_ideal are positive, the normalized branch states have distance at most
min(1,2 epsilon/min(p_actual,p_ideal)); a zero ideal branch can acquire
weight at most epsilon. Exact ideal zero weights and exact repeatability
are therefore not asserted for the approximate preparation.

These are formal state/trace comparisons. They neither produce an actual
outcome nor define an independently justified occurrence measure.

## Controls that distinguish preparation from an assumed target

E and the diagonal even mixture have identical populations. E has zero
edge bath-mark expectation; the mixture initially has expectation 1/L,
and its first collision creates neighbouring off-diagonal entries 1/L
while preserving the uniform populations. Translation invariance of a
density operator is not support on the invariant vector line.

The exact diagnostic is sum of bath-mark expectations
=(L/2)(F_final-F_initial). From a basis pointer its asymptotic supremum
is (L-1)/2=306 for L=613. This is an expectation in the joint state, not
a realized count or emitted-energy law.

For the declared zero-phase operations, all matrices are dyadic rational.
Finite unconditional evolution of a dyadic pointer input with basis baths
therefore has a dyadic reduced pointer matrix. P_E has entry 1/613.
**Exact E preparation from the basis-blank pointer is impossible in any
finite sequence of this class.** The obstruction still holds with an
arbitrary untouched source/reference state, but is not a no-go theorem for
other interactions, initial non-dyadic pointers or other preparation models.

Edge phases give a common dark line only when their product around the
cycle is one, and consistent nonconstant phases can select a different
line. The positive bound assumes zero edge phases. A dirty bath in state
one reduces E fidelity to (1-2/L)^2 in one collision. These controls expose
the supplied phase and purity resources rather than concealing them.

## Immutable evidence and actual runs

The inherited C reference is
`024936502544c2ec45acc8890a052c7b3aca26be`.
The specification was publicly frozen/read back at
`7809098069d4c4ff9f362048cf92c3e8b4714493`.
Complete author sources were frozen/read back at
`4bbd66ba7b979660fe2ec3b8eb855cef8a5063c1`.
Complete fresh independent sources were frozen/read back at
`4e5d56faac8fcd8bbbde7bed6d5b3783383f15eb`.
The final independent review was published/read back at
`02d96ba6911e8de4e7276c2697a9db8cad6b71a6`.

The reviewer knew the public specification, proposed model/constants and
admitted C sources; no target blindness is claimed. It froze its own proof
and program and completed its first run before seeing the successor author
proof/code/output. Author-side proof assistance and coordinator design
assistance are disclosed and are not counted as independent review.

| First pinned local run | Runtime | Result | Actual stdout |
|---|---:|---|---:|
| Independent, executed first | 4.732 s | exit 0, empty stderr | 455 bytes |
| Author, executed second | 3.632 s | exit 0, empty stderr | 526 bytes |

Both used Ubuntu 22.04.5 LTS, x86_64, Python 3.10.12 and the registered
120-second deterministic envelope. Complete source hashes, environment
and actual output custody are in the author
[RUN](../../reproduce/C-FIELD-J-PREPARATION-MECHANISM-N/RUN.md) and
independent [RUN](../../reproduce/C-FIELD-J-PREPARATION-MECHANISM-REVIEW-N/RUN.md).
There was no failed scientific run, source repair after freeze or local
rerun. EXPECTED files are captured outputs, not predictions.

The existing unchanged workflow then actually replayed both programs at
PR head `373071a864cebfe98c8ed7501d4ac0089ee738da`, run
[36941514569](https://github.com/mathorn1973/twist-j/actions/runs/36941514569).
The coordinator fetched and inspected both decoded job logs:

| CI job | Actual environment | Both reproduction entries |
|---|---|---|
| [architecture-x86_64](https://github.com/mathorn1973/twist-j/actions/runs/36941514569/job/110633855117) | Ubuntu 24.04, CPython 3.12.14 x64 | PASS |
| [architecture-aarch64](https://github.com/mathorn1973/twist-j/actions/runs/36941514569/job/110633855306) | Ubuntu 24.04 arm, CPython 3.12.14 arm64 | PASS |

Each log's two REPRODUCE PASS entries identify exactly these SHA-256 pairs:

| Program | verify.py | Actual stdout / EXPECTED.txt |
|---|---|---|
| Author | `9036378f0d5babae9d3c33f754bab5b28a03f449b309e32cda859df7fbe549fd` | `02a11e0babc33f06cdb1d5d13d2c8df54e1bbd5c1514cc78f1881ba47ef301d3` |
| Independent | `660ec02ce86b0b84346c7aded071b8c37e3a650f56ec6f9021128f07cc485702` | `c08168efaf82b2ffa50d8717f6963acc431935871d593a26323eb88b810671a0` |

The workflow aggregate check also passed. Its publication job was skipped
for this PR; that is not a release. Local policy, Canon, ledger and gate
contract checks passed. The review's statement that CI was pending is a
correct earlier observation; the above actual later logs supply that
gate. This record cites the tested head explicitly and does not claim
that a later documentation commit had already been tested.

## Receiving boundary and remaining work

[INTERFACE.md](INTERFACE.md) exports the actual joint state, epsilon,
finite capacity and untouched-bath contract. It states the obligations for
a successor's actual-state representation, controller, invocation/context
fields, WRITE completion, unused-cell selection, epochs and exhaustion.
WRITE, archive occupancy and an actual LOW/HIGH outcome remain distinct.
Restoring a working pointer does not prepare a new independent source.

No actual-state controller or occurrence law is supplied here. R still
requires such a mechanism on this same preparation interface; D requires
an independently justified initial measure or frequency theorem for its
actual recorded histories. The right-hand Stage-C trace formula cannot
be used as the definition of that left-hand measure. No generic weighted
sampler was built. Native physics, source/context preparation, the phase
and clock origin and all three QDD physical obligations remain open.

The authority remains Public Canon v96: live main/tag
`44423153eee6259c7277eec5f5adbed9679f9146`, admitted content base
`d63de7e7345cf5fa5ab344654aafb7238d6d8bca`. All five canonical file hashes
were checked against Git bytes before this work. Only the two preparation
notes and reproduction lanes are added relative to the fixed C base.
No Canon, registry, policy, workflow, gate, main, tag or release is changed.
PR #1332 remains a draft, unmerged research proposal.
