# Round 2: fixed-seed readout and the missing persistent phase

NON-CANONICAL. No authority. No Canon status changes.

All new mathematical conclusions: candidate-D, L1, paper derivations.
Owner: A. M. Thorn, ChatGPT-Astra-Sol-20261124-Two-Place.
Date: 2026-11-24. Claim: [#2080](https://github.com/mathorn1973/twist-j/issues/2080).
Publication basis: 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed, Public Canon v117.
Initial source basis: 26bd3b935272ac6ff35591f50be616473a54ef7a.
First-round draft head: 17b58fe36fc70f3af5140be2840803176b1e4741.

## 1. What has been resolved

The first-round [DECODER.md](../DECODER.md) left open whether its
finite-history obstruction still holds on one separately prescribed
origin-zero native trajectory. It does. The stronger statement is:

**Candidate-D.** Every finite fully synchronized observation window of a
fixed seed, including the four-phase decoration, has arbitrarily late
exact copies on that same trajectory in every residue class modulo any
odd integer. The copies can preserve any prescribed finite dyadic phase
of the original endpoint.

Consequently, for any period \(2^a q\), with \(q\) odd, a function of time
with that period is readable by some fixed finite native observation
window exactly when it depends only on time modulo \(2^a\), on the
admitted residue classes. This classification holds for each individual
fixed seed, even when the reader knows that seed. For period sixty the
readable part is exactly time modulo four.

The proof uses the registered conserved native chart, not a model of a
different trajectory or a change of initial state. It also rules out an
adaptive counter-free reader that stops after finitely many synchronized
relative queries at each evaluation. A marked origin, the available
history length, an external time label or retained observer state is a
different input contract.

## 2. A concrete long collision

**Candidate-D.** Put \(M=16^k\), \(k\ge1\). On every fixed seed the final
\(2M-5\) decorated observations at the two endpoints

\[
n=4M-5,\qquad n'=6M-5
\]

agree exactly. Yet the endpoints are respectively 29 and 1 modulo 30,
so they have opposite values of \(\chi_3\chi_5\), and therefore opposite
inert-defect flags.

The first instance consists of **27 identical consecutive observations
ending at times 59 and 91**. This is an instance of a symbolic family,
not a numerical search or a primality test.

At horizon \(N_k=6\cdot16^k-5\), a uniform causal fixed-width reader of
this flag, valid on all eligible times after its window has synchronized,
needs width at least \(2\cdot16^k-4\). This lower bound concerns a window
without an externally supplied endpoint index.

## 3. The exact added-state cost

**Candidate-D.** Consider an observer whose extra finite state is updated
at every native tick by a time-independent deterministic rule. It may
also read any fixed finite decorated window of the unchanged native
trajectory. It receives no absolute time or external visitation schedule.
To output

\[
b_n=\mathbf1_{\Delta(n)=0\bmod2\mathcal O}
\]

correctly at every time coprime to 30 after any fixed warmup, the observer needs at least **15
reachable persistent states**. Fifteen suffice. The lower bound holds
on a single prescribed seed and allows the observer state to depend on
the entire actual past.

The attaining construction is especially direct. Let
\(g=J\bmod2\) in \(\mathbb F_{16}\), and initialize \(c_0=1\). Use

\[
c_{n+1}=gc_n,\qquad
b_n=\mathbf1_{c_n+1+c_n^{12}=0}.
\]

The registered order of \(g\) is 15. In the basis \(1,g,g^2,g^3\), the
four-bit state has the update

\[
(z_0,z_1,z_2,z_3)\longmapsto
(z_3,z_0,z_1,z_2+z_3),\qquad z_i\in\mathbb F_2.
\]

All fifteen nonzero states occur. The zero state is unused. Initialization
at a later time \(T\) requires the correct phase \(c_T=g^T\); an arbitrary
reset does not supply that information.

This is a sharp resource theorem for an explicitly extended observer.
It does not locate these fifteen persistent states inside the original
six-coordinate checkpoint. The retained input window, if physically
stored, has its own cost and is not counted among these fifteen states.

## 4. Relation to the refined arithmetic decoder

**Inherited T.** The registered finite-history reader recovers every
fixed dyadic phase \(n\bmod2^k\); a sufficient drive-bit window has
length \(5\cdot2^{k-1}\). Native traces expose the preceding drive bit,
with the corresponding one-step phase correction.

**Candidate-D.** For \(k\ge2\), that dyadic reading together with the
fifteen-state register recovers

\[
n\bmod(15\cdot2^k),
\]

which is exactly the information in
\(\Delta(n)\bmod(5\cdot2^{k+1})\mathcal O\) by the first-round arithmetic
theorem. Thus a declared observer extension realizes the arithmetic
reader at every fixed precision. The stated sufficient dyadic window
grows with the precision; no one fixed finite window and fixed finite
register can supply unbounded precision. No sharp window minimum at
each precision is claimed.

## 5. Remaining question and evidence boundary

**O.** Give a permitted native memory carrier, preparation and update law
that realizes the persistent odd phase and the retained dyadic history.
The current proof specifies what the observer must retain and provides
an exact arithmetic construction. It does not establish that an unchanged
native checkpoint supplies that carrier, or that such an apparatus has
been physically realized.

The source basis and ownership are in [SOURCE_REVIEW.md](SOURCE_REVIEW.md).
Full proofs are in [PROOF.md](PROOF.md) and [OBSERVER.md](OBSERVER.md).
The first-round scientific files are retained as written; this round
explicitly resolves their stated fixed-seed open case.

No new scientific executable, mathematical census or formal proof checker
was run. Internal Astra development, Astra opposition and Sol source
review do not constitute external or blind confirmation. Repository
acceptance checks, if green, do not promote these paper claims. No RH
bound, prime recognizer, physical readout or L2-L6 lift is asserted.
