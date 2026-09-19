# Draft preregistration: Galois-channel optimum and minimal auxiliary

**NON-CANONICAL / DRAFT / NO PUBLIC PIN / NOT EXECUTED.**

Proposed identifier: `P-U-GALOIS-CHANNEL-OPTIMUM-1`, unreserved.
Proposed owner: one named owner to be recorded in a public issue before
formal commitment. This draft reserves neither an identifier nor claims.
Working basis: Public Canon v88 at public main
`e57d4506d5b28bf8cb4979c4e29db6b10b2441f2`.
Action layer: **L1**, mathematical comparison on declared finite complex
state spaces. No cross-layer or physical-adoption gate is proposed.

The issue packages #1037 and #1038 and their prior reported results are
result-exposed incubation inputs. Their issue freezes and outputs are not
formal public pins or executions of this draft. The accompanying proof and
verifier are review candidates; formal acceptance remains pending.

## 1. Equation and complete class

Index k,a in {0,1,2,3} in the inherited mark order (1,2,4,3).
Use orthonormal input coordinates e_(k,a) in C^16 and output e_k in C^4:

    H=((1,1,1,1),(1,-1,1,-1),(1,1,-1,-1),(1,-1,-1,1)),
    F=H/2,
    C e_a=(1/2) sum_k H_ka e_(k,a),
    Pi=CC*, Q=I16-Pi, D=FC*, q_ka=Qe_(k,a).

The four source-basis columns of the public Galois code extend over C
through an invertible coordinate map with Gram I4-ones4/5. Thus this is
the unchanged code expressed in normalized coordinates; it admits every
complex alpha. Its free native pushforward is N e_(k,a)=e_k, NC=F.

Comparison class: **all** complex CPTP maps Phi:M16(C)->M4(C) such that

    Phi(C rho C*)=F rho F*

for every complex source operator rho (equivalently every density
operator). CPTP is an external mathematical framework, not a native law.
The full four-dimensional output and exact full-code transfer are fixed.

Coordinate agreement and the error metric are

    f_ka(Phi)=<k|Phi(|k,a><k,a|)|k>,
    delta(Phi)=max_(k,a)(1-f_ka(Phi)).

Each 1-f_ka is coordinate-distribution total variation against native
endpoint k. It is not full quantum trace distance or a QDD weight error.

Proposed conditional mathematical conclusions, without earned public status:

1. Every admitted channel has Phi(X)=DXD*+Psi(QXQ), where Psi is CPTP
   on the twelve-dimensional complement. The maximum minimum agreement
   and maximum mean agreement both equal 5/8; min delta=3/8.
2. Every mean optimizer, and hence every worst-coordinate optimizer, has
   complement effects A_k=Psi*(|k><k|)=sum_a|q_ka><q_ka|, each of rank four.
   Every optimizer therefore requires purified auxiliary dimension at
   least five; the displayed five-Kraus construction attains five.
   This is uniqueness of coordinate effects, not uniqueness of the channel.

## 2. Carrier and exact controls

Seventeen-Kraus optimizer Phi17:

    K0=D, K_(k,a)=|k><q_ka|.

Five-Kraus optimizer Phi5:

    J0=D, J_(a+1)=sum_k|k><q_ka|.

Both give raw coordinate weights 5/8 at k=j and 1/8 elsewhere on input
e_(j,b). Their full output densities differ: raw e_(0,0) has entry(0,1)
+1/16 for Phi17 and -1/8 for Phi5.

The point-exact control Lambda uses L_a e_(k,b)=delta_ab e_k.
Every point-exact CPTP map has fixed diagonal native-fibre effects; its
coded output coordinate law is uniform. The fixed alpha=(1,1,1,1)/2
requires F alpha=e0, while Lambda gives I4/4. This control tests exact
simultaneous compatibility; its 3/4 error is separate from the optimum 3/8.

A second control transfers the code with a four-dimensional pure
auxiliary, but has uniform raw output populations 1/4. In register order
(output l, auxiliary mu), its isometry is

    V4[(l,mu),(k,a)]=F_la F_mu,k H_ka.

This shows why auxiliary minimum five requires optimal raw agreement.
Mixed initial auxiliaries are counted after purification.

The constructive full orthogonal extension, retaining every output, is

    U20=((Q,C),(FC*,0)).

Input is the direct sum of sixteen signal and four additional coordinates;
output is residual sixteen then central four. Relabel residual(k,a) as
(k,mu=a+1), central k as(k,mu=0) to obtain Phi5 by tracing mu.

Let B apply F to k separately at fixed a, Z=diag(H_ka), L=ZB, and
E0 e_a=e_(0,a). Let S swap e_(0,a) with additional port a. Freeze

    LE0=C,
    U20=(I16 direct-sum F)(L direct-sum I4)S(L* direct-sum I4).

The matched loader cancels its inverse on designated inputs. Matrix
factorization is a certificate, not an independently derived native
coupling or a physical calibration.

## 3. Code and audit coverage

`verify.py` is a fresh combined standard-library Fraction verifier draft
adapted, with attribution, from the hash-verified issue auditors. It reads
no external files, invokes no other program, uses no floating-point
arithmetic, writes no files, and prints deterministic JSON.

Planned finite checks: C,F,Pi,Q,D identities; five- and seventeen-Kraus
completeness and exact code transfer on all sixteen matrix units;
128 code/complement cross terms for each channel; all sixteen raw full
densities and coordinate laws; positive slack scaled-projection identities;
effect ranks and completeness; invertible outer-product minor; five-Kraus
Gram; point-exact and four-auxiliary controls; full U20 orthogonality and
independently formed factorization; all twenty scattering columns, four
code inputs and twelve complement inputs; loader cancellation; fixed phase
flip and coarse/fine HIGH comparison controls.

All coefficients are rational. Identities on every source matrix unit
establish equality on complex operators by complex linearity. The
complete-class bound and equality classification require the written
proof; checking selected channels does not prove the universal theorem.

The bounded native antecedent and N identities remain inherited from
`P-U-GALOIS-FIBER-CODE-1`; this draft does not register them again. Source
#1037's old native-address transcript is retained only in source custody.

## 4. Systematics and exclusions

No postselection, discarded residual ports, post-freeze or source-state-
dependent alteration of the declared code/loader to repair target agreement,
changed source labels, output-space enlargement, or approximate code
recovery is admitted. Arbitrary complex input operators and arbitrary
complex CPTP channels are admitted; rational examples do not restrict the
comparison class. The full-output-rank condition is indispensable to
code/complement cross-term removal.

The sixteen raw coordinates have not been established to be separately
preparable orthogonal physical states. No physical preparation, actual
apparatus coupling, exclusive event, Born occurrence, persistent record,
reset, family completeness or physical layer bridge follows. U, the free
pushforward N, Phi17/Phi5 and U20 remain distinct objects. The optical
REALIZATION source remains noncanonical engineering material and is not
promoted by this intake. General-m Hadamard claims and measured
calibration/tolerance claims are outside the proposed two-claim fold.

## 5. Failure thresholds and disposition

Every finite identity is exact: any unequal rational entry, nonzero
required residual, wrong rank/determinant, failed assertion, nonzero exit,
nonempty stderr, or stdout mismatch in required replay is a failed audit.
No numerical tolerance or data-dependent threshold is available.

Any valid full-class counterexample to the 5/8 bound, decomposition,
optimal-effect equality or purified minimum five defeats the corresponding
proposed theorem. Failure of an explicit construction defeats its attaining
certificate. A physical mismatch outside the mathematical comparison
hypotheses is not a counterexample at this scope.

A failure is retained under the applicable public probe procedure; there
is no post-pin source repair, threshold change, or relabeling an executed
failure as an unexecuted abandoned pin. No wider physical owner receives
an F verdict from this bounded comparison.

## 6. Remaining formal sequence

Before any formal execution: complete current-main authority and collision
preflight; appoint one public owner and confirm the unreserved identifier;
independently review this exact statement; accept the proof and verifier;
place them on their own formal probe branch and path; commit and push the
preregistration and verifier; record the immutable commit and file SHA-256.

Only afterward use the current POLICY/AGENTS and repository runner/checker
contract for the Linux-compatible local execution and required clean
x86_64/aarch64 Python 3.12 replays. Record actual EXPECTED.txt, RUN.md and
RESULT.md from that execution. No such records are present in this draft.
A separate reviewed public fold may then consider the two proposed claims
for T at their precise mathematical scopes. v89 is provisional.
