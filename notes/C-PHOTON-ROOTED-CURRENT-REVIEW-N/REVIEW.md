# Independent review of the frozen rooted-current candidate

**PUBLIC, NON-CANONICAL. Scoped verdict: ACCEPT G1-G6.**

Reviewer session: photon_breaker. Date: 2026-10-01.
Candidate: C-PHOTON-ROOTED-CURRENT-TAIL-N, issue
[#1324](https://github.com/mathorn1973/twist-j/issues/1324).
This accepts the written analytical statements at candidate-T scope, with
the displayed antecedents and source-status boundaries intact. It is not
an upper-tail theorem, a computational gate or a Canon promotion.

## 1. Freeze, custody and exposure

The candidate is frozen at
`82b16f69418df669d0674d878afbf96eadfb3f4e`. The independent preregistration
and derivation were committed and publicly read back at
`8bf269cd0245b925db109264188a84841661e4ce` before the reviewer opened
the author's CONTRACT.md. The coordinator's public readbacks matched
PREREG blob `1c72a8561163183ddb4b499cc2be4f1d2fb6705a` and DERIVATION blob
`0d0ec1cd976bc4764ed55e3a0b2d2cd688acbffc`.

Direct byte hashing and readback give:

| Artifact | SHA-256 | Bytes |
|---|---|---:|
| Independent PREREG.md at the review freeze | `25e578d928c778ada6301af6e5f97750003d202113fe2471837a37961410688c` | 7467 |
| Independent DERIVATION.md at the review freeze | `b6cd5b6b6f3fcb1207de4627c8630ea7ae4e396ca340ec01de632977ddc5dfa4` | 16988 |
| Author CONTRACT.md at the candidate freeze | `72250ffaefe50e075994ba9b4ba1fe7eb88e45afc714c3171f93900424b5748d` | 18442 |

The frozen review files remain byte-identical to their public pin. CONTRACT.md
was read by `git show` at the candidate pin only after the coordinator
confirmed the independent public freeze and authorized comparison. No
author file has been changed.

The full pre-comparison exposure declaration is retained in
[PREREG.md](PREREG.md). This was known-target work: all G1-G6 constants were
visible in the frozen specification. It was not result-blind, an independent
implementation, or an independent review of the whole historical source
corpus. A read displayed incidental later sections of the two permitted
source notes; those sections were not used as premises. No author construction,
builder code, verifier output, other review or complete taskpack was read
before the independent derivation freeze. The post-freeze exposure is the
author CONTRACT.md alone. Its additional source names and author exposure
declarations have not been imported as new scientific premises.

All accepted statements use the same three admitted snapshots at public
main `44423153eee6259c7277eec5f5adbed9679f9146`, whose exact hashes and
byte counts are recorded in PREREG.md. The canonical variance-floor theorem
keeps its T scope; the augmentation and whole-current reduction notes remain
NON-CANONICAL dependencies. The current Canon remains Public Canon v96.

## 2. Claim-by-claim comparison

| Frozen claim | Verdict | Proof and comparison |
|---|---|---|
| G1: every canonical root has p_(L,e)>=2^-41 | **ACCEPT** | Independent DERIVATION sections 1-2 and author section 5 agree. Global reversal gives zero mean, unit current gives Var(j_e)=p_e, and the one-patch linear-observable variance lemma gives 2^(1-42). The exterior average is complete. |
| G2: every nonzero component current has M_K in {4,6,...,N}; R3>=2^-35 | **ACCEPT** | Independent section 3 and author sections 4-5 use conserved unit flow on the simple bipartite torus graph. Edge-disjoint directed cycles are even and have length at least four, including winding cycles. The N=4V root average yields 64*2^-41. |
| G3: the specified C/16 and 25rho certificates have deficit D(C)>=3575rho | **ACCEPT, conditional on the stated future uniform bound** | Independent section 4 and author section 5 give C>=2^-35, C/16>=144rho and 25*(144-1)rho=3575rho. This is the signed difference of the specified certificates, with no assertion about the sign of actual b-25chi. |
| G4: exact finite tail identity; exponential majorant and remainder | **ACCEPT, with the upper bound conditional on its tail premise** | Independent section 5 and author section 3 have identical d_r, F_N, rational infinite sum and q^N remainder. The Aq^r convention contributes exactly one extra factor q. |
| G5: polynomial finite/infinite majorants and remainder | **ACCEPT, conditional on its polynomial-tail premise** | Independent section 6 and author section 3 agree on all three harmonic/zeta coefficients. Keeping the r=1 term exact and integrating the remaining bound proves C0(1+3/epsilon); integration beyond N proves 3C0*N^(-epsilon)/epsilon for every epsilon>0. |
| G6: even-size contraction implication, G_K and exact remainder | **ACCEPT, conditional on (H) and p_e<=p_*** | Independent section 7 and author section 4 agree on Kmax=2V-2, a_k=24k^2+72k+56, the rational G_infinity and its remainder. The independent proof explicitly covers theta=0 and zero denominator events. |

The accepted exponential and contraction series formulas are identities for
all real parameters in their frozen ranges, proved from the geometric
series and its first two moment sums. They are not numerical extrapolations.
The polynomial estimates hold for every real epsilon>0 by absolute
convergence and integral comparison. The finite cutoffs and their exact
remainders are retained; no asymptotic expression replaces a finite formula.

## 3. Adversarial checks and classifications

**Sign symmetry and insertion variance.** Reversal of the whole signed
state preserves the full weight and all admissible sectors. The argument
does not reverse only an interior while freezing a nonzero exterior. For a
fixed exterior, the zero filling may be forbidden. Then its p_0 is zero and
the local variance inequality is trivial. When zero is permitted, the two
21-face fillings have probabilities 2^-21*p_0 and linear-observable offsets
of magnitude one. Averaging their nonnegative variance contribution gives
2^-20*P(n|S=0), and the unconditional empty-set estimate gives 2^-41.
The proposed counterattack of demanding a uniform empty probability in each
fixed exterior therefore does not refute G1: that stronger assertion is not
used. No proof gap remains in this conditioning step.

**Normalization and completeness.** A signed field has exactly product_e r_e!
compatible matchings, canceled by their reciprocal weights; a consistent
unsigned structure has exactly 2^k equal-weight signings. This proves the
same Z_L and the correct signed marginal. Neutral-only components, degree-four
and degree-six pairings, arbitrary neutral joins and winding structures are
all retained. Selecting one matching or flipping individual current loops
would change the argument and can be invalid; neither construction does so.
Component signs are independent only for the prescribed paired face graph.

**Graph size and root factors.** Even L makes parity well-defined through
the periodic seam; L>=4 prevents the degenerate parallel-edge graph at L=2.
Conservation and unit capacity give an edge-disjoint cycle decomposition,
without requiring it to be unique. Minimum cycle size four holds for winding
and nonwinding cycles alike. M_K counts all current edges in the component,
not neutral area, diameter or one selected loop. The pointwise rooting
identity sums to sum_K M_K^4, so the lower bound and inherited 1/16 have the
advertised normalization. Odd volumes or L=2 are outside-scope examples,
not admitted counterexamples.

**Certificate direction and limit boundary.** The lower bound on R3 forces
a lower bound on the numerical value of any valid C. It does not force
actual chi to equal C/16. The resulting negative certificate difference
does not constrain the sign of the true infrared difference. The canonical
finite floor and error terms are retained, and the thermodynamic limit is
taken first at fixed nonzero limiting momentum, then the infrared limit.
Profile existence, uniqueness, local-to-Fourier identification and limit
exchange have not been assumed proved. The original nonempty jointly
admitted profile family is unchanged.

**Series endpoints and zero events.** The exact shifted polynomials in the
two geometric remainders match the frozen formulas. At theta=0, G_K and
G_infinity are both 64 and the remainder is zero. If a denominator tail
event has zero probability, its nested successor is also zero; the undivided
inequality covers it. A conditional-probability quotient is used only for
positive denominators. The polynomial remainder is nonnegative, strictly
positive for C0>0, and zero for C0=0. The term “positive tail” denotes the
sum of positive-series terms and does not create a strict-positivity claim
at zero prefactor. In any event G1 rules out C0=0 (or A=0) as an actual
full-measure upper-tail premise. No q=1, theta=1 or epsilon=0 extension is
asserted.

**Author notation and retained draft metadata.** Author section 4 says
theta<1; the controlling frozen specification explicitly states
0<=theta<1, which is the reviewed range. Moreover G1 makes the first
conditioning event positive, so a negative theta could not satisfy (H).
The author's exponential convention exp(-a*r) is the frozen Aq^r
convention with q=exp(-a), within 0<q<1. Neither is a changed target.
The unchanged author header's “no ... candidate pin” is retained
pre-freeze draft metadata, not the current custody statement. The actual
candidate and review pins above control this comparison. It is not a
scientific defect or a reason to rewrite the frozen author document.

No admitted exact counterexample was found, and the independent proofs
above supply the reasoning required for acceptance rather than treating
the absence of a counterexample as proof. No frozen constant or carrier
was adjusted. There is no REJECT or BLOCKED verdict among G1-G6.

## 4. Explicitly unclosed work

Neither the author nor this review proves an exponential tail, a polynomial
tail with exponent above three, or the contraction (H) for the actual
complete measure. The choice p_*=1 is unconditional but does not supply
(H). Failure of one proposed theta, or failure of one sufficient upper-tail
route, would not prove R3 unbounded.

Uniform R3 boundedness remains unresolved. The larger #1122/#1143 owners,
P1, PHOTON-MASSLESS-PHASE and the physical photon bridge retain their
existing status. Acceptance is limited to G1-G6 with their exact
hypotheses, known source dependencies and mathematical carrier. No Canon,
registry, gate, workflow, policy or release change follows.

The review performed no scientific execution and makes no verifier,
finite-audit, two-architecture or numerical evidence claim. Custody hashes,
Git readback and static text checks are procedural only. A later optional
finite audit would need its own prospective authorization and frozen scope.
