# Preparing a thermal environment and nearly clean registers

**NON-CANONICAL, L1, conditional analytical candidate-T.**
Independent mathematical acceptance is pending. Public reservation:
[#1759](https://github.com/mathorn1973/twist-j/issues/1759).

A finite common-temperature donor bank can prepare the environment and known
basis-ready registers required by [#1758 at 24337945][prior]. Reversible
compression concentrates purity; funded SWAPs create the nominated thermal
marginals; every displaced value, donor and work correlation is retained.
One explicit time-independent local Hamiltonian performs preparation and
the inherited accepted endpoint experiment.

The actual input uses no exactly clean compiler scratch. Fresh rows and
routing ladders contain counted thermal junk. The work ladder and master
cursor have full-rank polarized distributions. Their charge, low entropy
and joint nonstationarity are supplied bootstrap resources, not outputs of
the prefix they control. The result is approximate readiness with an
explicit error, not exact purification of a finite full-rank closed input.

## 1. A common finite bath and reversible preparation

Let beta_0 epsilon=log2. Ordinary donor qubits of gap epsilon have excited
population 1/3. A gap-2epsilon donor at the same temperature has population
1/5. These are one common-temperature product input, not the desired pair
of already-prepared hot/cold Gibbs states.

For m nominated ready bits, use disjoint ternary trees. The reversible
three-bit compressor swaps 100 and 011 and fixes the other six words.
It writes the majority into its first bit while keeping the other bits.
For independent child outputs,

\[
 p_0=\frac13,\qquad p_{r+1}=3p_r^2-2p_r^3.
\]

Put b=ceil(log_2 m)+80, k=3+ceil(log_2 b), and N=3^k. Each target gets one
retained output from N donor bits. The exact recurrence gives

\[
 \xi=1-(1-p_k)^m\leq mp_k<2^{-80}.
\]

Complement the retained outputs whose nominated ready value is one, then
SWAP them into the old target registers. Matching-gap SWAPs transfer the
former target information, including reference correlations, into retained
sink wires. No reset or discarded branch is used.

For the old environment, fund a SWAP from a gap-epsilon donor into the
gap-3epsilon hot target, and a SWAP from a gap-2epsilon donor into the
gap-epsilon cold target. On the buffered work component, the resulting
reduced environment is exactly the old population pair (1/3,1/5).
The two swaps cost 26epsilon/45 in mean work for the specified initial
common-temperature target states.

These are exact reduced statements on the good reference component.
The actual full-rank work/controller preparation adds the errors below.
[RESOURCES.md](RESOURCES.md) specifies the bath, compression, retained
entropy and work accounting.

## 2. Funded local operations and one full Hamiltonian

Let Q be the finite maximum payload energy in units epsilon. Use a physical
work ladder with levels 0 through 2R, R=2Q, and energy epsilon times its
level. Local gates are extended unitarily inside each complete local
energy sector and as identity on incomplete local sectors.

Starting at the central work level, every prefix remains buffered and the
energy shifts telescope:

\[
 n_{\rm work,final}=R+E_{\rm payload,in}/\epsilon
                         -E_{\rm payload,out}/\epsilon.
\]

This proves the required action even while the work store becomes correlated
with the thermal payload. In bad edge sectors, the actual local extensions
remain in the state; their product is not falsely declared the identity
completion of the entire word.

A moving ladder is routed to each local gate and back by equal-spectrum
SWAPs, restoring other ladder cells exactly. Whole-row transfers likewise
move the original payload forward while retaining the earlier row contents.
Neither mechanism needs clean routing or row scratch.

[HAMILTONIAN.md](HAMILTONIAN.md) gives the spatial construction and
H=H_0+H_prop, with both terms positive and [H_0,H_prop]=0. The gates act on
finitely many nearby sites; the physical ladder's growing onsite dimension
2R+1 is explicitly counted. It is not an undeclared qubit-code purity
resource or a preservation of the preceding all-qubit local dimension.

The master path has K=8B edges, with B at least 8192 and large enough for
the actual compiled preparation and experiment blocks. Preparation finishes
by B; identity histories from B to 3B hold its output on a fixed row.
The experiment finishes by 4B; the remaining histories form an output tail.
The old endpoint map is retained on its promised family. Its former
continuous-time Hamiltonian is not claimed unchanged.

## 3. Actual readiness and the admitted bootstrap

The actual work seed is full rank:

\[
 \Pr(n=R)=1-\eta_B,\qquad
 \Pr(n\ne R)=\frac{\eta_B}{2R}\ \text{per level},\qquad
 \eta_B=\frac{2^{-80}}{Q+1}.
\]

Every physical cursor qubit is also full rank. The entry favors occupation
1-r, all others favor r, with r=2^{-80}/(K+1). Its total bad-pattern weight
is at most eta_C=2^-80. Multi-cursor and invalid input sectors are included
in the raw Hamiltonian, not projected out.

For the preparation window sin^2(theta) in [3/16,1/4], where
theta=gt/[hbar(K+1)], the wrong master-history weight obeys

\[
 \delta_{\rm pre}<2(31/32)^B<2^{-255}.
\]

The reduced old apparatus and its logical reference are therefore within
xi+eta_B+eta_C+delta_pre of the nominated ready/environment input.
This does not assert a product with the retained bath/work trash or an
already implemented readiness instrument.

The finite full-rank obstruction explains why exact blank registers are
not claimed. For a target dimension d_T and retained-rest dimension d_R,
the maximum pure-target weight under any unitary is at most the sum of the
largest d_R eigenvalues of the complete input. It is strictly below one
for a full-rank input and d_T>1. Arbitrary logical code states require the
scope qualifications in [PREPARATION.md](PREPARATION.md).

## 4. Work, total energy and where the entropy goes

The ideal buffered preparation has exact mean payload work cost

\[
 W_{\rm prep}=\epsilon\left[mC_{\rm tree}
                   +m_1(1-2p_k)+\frac{26}{45}\right],
\]
\[
 C_{\rm tree}=\sum_{r=0}^{k-1}
       3^{k-r-1}p_r(1-p_r)(1-2p_r).
\]

Here m_1 counts nominated one bits. The work ladder loses this energy on
the buffered component. RESOURCES.md also keeps the finite bad-seed
contribution; no small-probability energy term is dropped merely because
the apparatus is large.

The complete initial energy includes every data row, donor, head ladder,
work seed and master cursor. Its propagation contribution is g times the
initial mean cursor number. The exact total energy and variance are given
in HAMILTONIAN.md; the preparation-work expression alone is not that total.

With all donors/work/controller retained, initial product preparation gives

\[
 \Delta S_{\rm rest}
 =S_{\rm target,in}-S_{\rm target,out}+I({\rm target}:{\rm rest})_{\rm out}.
\]

Thus entropy is transferred and correlations remain. The purified bits,
finite bath and work source are not restored for reuse. The old source
reaction is ultimately funded by this work-assisted preparation, not by
an inexhaustible single-temperature bath.

## 5. Output accuracy and residual physical boundary

The actual accepted output is approximate. The cooling, bad work and bad
clock terms are bounded before conditioning, and the acceptance denominator
is included afterwards. PREPARATION.md derives retention of the whole-input
threshold >1/75000 and unwanted fraction <1/10^6 using the inherited strict
margins. The occupied-memory/reference SWAP and correct receiver statement
have the stated small trace-distance error; they are no longer claimed
exact for the actual noisy readiness.

Although [H_0,rho_in]=0, the polarized entry next to the fixed first
propagation edge gives

\[
 \|[H,\rho_{\rm in}]\|_1\geq2a_0(1-2r)>0.
\]

This initial nonstationarity, the work distribution and controller
polarization remain supplied. A Gibbs state of the full H would not run.
[NATIVE.md](NATIVE.md) distinguishes this added law from unchanged U_rec,
and identifies the unprepared resources, finite-error scope and lack of
a material implementation, occurrence law or useful reset.

[VALIDATION.md](VALIDATION.md) records fixed inputs, proof-file custody and
the actual checks. No new scientific executable or simulation was run.

[prior]: https://github.com/mathorn1973/twist-j/tree/243379459e3c7493368473cbae1a17eb99ee8316/notes/C-ENVIRONMENT-SOURCE-PREPARATION-N
