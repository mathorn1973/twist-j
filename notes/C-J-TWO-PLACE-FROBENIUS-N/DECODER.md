# Native observation fibres and carry history

NON-CANONICAL. All new deductions: candidate-D, L1.
Registered T premises keep their exact scopes.

## 1. The actual state is not the arithmetic power orbit

The canonical autonomous state retains an index together with a checkpoint.
Write

\[
X=\mathbb F_5^6,\quad
\theta_n=s_2(n)\bmod2,\quad
\Theta_n=2^{s_2(n)}\bmod5,\quad
E_n(x)=\operatorname{pr}_{\psi}U^n(0,x).
\]

The registered update is

\[
\psi_{n+1}=F_{\theta_n}(\psi_n),\qquad
F_e(x)=G_{z_6(x)+2e}(x),
\]

where the generator subscript is reduced modulo five.
The maps \(F_0,F_1\) are fixed maps on the finite set \(X\).
They are not the arithmetic binary-index maps in PROOF.md.

For \(z\in\mathbb F_5\), put \(X_z=\{x:z_6(x)=z\}\).
KERNEL-Z6-SYNCHRONIZATION [T], clause S1, gives

\[
E_n|_{X_z}:X_z\longrightarrow X_{q_n}
\quad\hbox{bijectively},\qquad
q_n=4+2\theta_{n-1},\quad n\ge3.                           \tag{1.1}
\]

Thus the synchronized sheet reads the preceding driver bit. The whole
checkpoint contains additional coordinates, but every point of the same
target sheet is attainable from every chosen initial sheet.

The registered COMPLETE-STATE-OBSERVATION-CONTRACT says that an output
factors through an observation exactly when it is constant on that
observation's fibres. Retaining the complete state, including \(n\), is
a different observation from retaining only \(\psi_n\).

## 2. Exact checkpoint failures, with the domains kept separate

### The full carrier, same seed

CARRY-J-CHECKPOINT [T] proves
\(\psi_4=\psi_6\) for every origin-zero initial checkpoint.
At two, with \(g=J\bmod2\),

\[
\Delta(4)=0,\qquad \Delta(6)=g^6-g\ne0.
\]

The first equality is Frobenius; the second uses \(j^{12}=j^2\) and
the order fifteen of \(g\).
Even the binary zero flag cannot be a function of the bare checkpoint on
the full time carrier. This example alone says nothing about a
restriction to unit indices modulo thirty.

### The unit-index carrier, all seeds

For any time-only output \(B(n)\), (1.1) proves the following equivalence:
there is one map \(h:X\to\mathcal Y\) with
\(h(E_n(x))=B(n)\) for all seeds \(x\) and all admitted \(n\ge3\)
if and only if \(B\) is constant on each class of admitted times with
equal \(\theta_{n-1}\).
For necessity take a common point in the same reachable sheet.
For sufficiency read \(\theta_{n-1}\) from that sheet.

The unit times \(7,13,19\) have

\[
\theta_6=\theta_{12}=\theta_{18}=0,\qquad
\Theta_7=\Theta_{13}=\Theta_{19}=3.
\]

Choose any common point of \(X_4\), for example
\((4,0,0,0,0,0)\). Equation (1.1) supplies initial seeds realizing that
point at the three times, even if one prescribes the same initial sheet.
Yet

\[
\begin{array}{c|ccc}
n&7&13&19\\ \hline
\Delta(n)=0\bmod2&\text{false}&\text{false}&\text{true}\\
\Delta(n)=0\bmod\lambda&\text{false}&\text{true}&\text{false}.
\end{array}
\]

Consequently neither flag factors through \((\psi_n,\Theta_n)\) on the
all-seed unit-index carrier. The constructed seeds may differ. This is
not a same-seed unit-index result.

There is also no substitution of the arithmetic residue reading for
the four-phase digit-count reading. The indices \(11,71\) agree modulo
sixty, whereas their binary digit sums are three and four. Hence their
complete defect residues modulo ten agree, but their \(\Theta\) values
are three and one. Conversely \(7,13\) have the same \(\Theta\) and
different ramified flags.

## 3. A bounded history recovers the ramified flag

The registered U-FINITE-HISTORY-CLOCK-PHASE [T] already supplies a
sufficient ten-bit driver window for phase modulo four. On synchronized
checkpoints the recovered endpoint is one step behind and must be
advanced by one modulo four. This existing theorem already proves
finite-history recovery of
\(\Delta(n)=0\bmod\lambda\).

Here is a shorter paper bound, without a minimality claim.

### Proposition 3.1

Seven consecutive checkpoints
\(\psi_{n-6},\ldots,\psi_n\), for \(n\ge9\), determine \(n\bmod4\).
They therefore determine the ramified flag, uniformly over all seeds.

Every legal four-bit Thue-Morse word determines the parity of its
starting index. An equal adjacent pair can start only at an odd index,
because
\(\theta_{2m+1}=1-\theta_{2m}\).
The local position of an equal pair therefore determines the parity.
If the four-bit word alternates, its start must be even: an alternating
word beginning at \(2m+1\) would force
\(\theta_m=\theta_{m+1}=\theta_{m+2}\).
Such three equal bits are impossible because every three consecutive
indices contain an aligned complementary pair.

This parity rule depends only on equality patterns, so it is unchanged
by complementing all bits.
In a seven-bit word starting at \(t=2m+e\), the first four bits determine
\(e\). The bits at offsets \(0,2,4,6\) are the four consecutive parent
bits starting at \(m\), complemented if \(e=1\).
Applying the same parity rule determines \(m\bmod2\), hence \(t\bmod4\).

By (1.1), seven checkpoints starting at \(n-6\ge3\) give the seven driver
bits starting at \(t=n-7\). Add seven modulo four to recover \(n\bmod4\).
This observer uses an explicit retained window. It is not a proof that
the checkpoint itself stores that window physically.

## 4. No fixed decorated history recovers the inert flag uniformly

### Proposition 4.1

Fix any finite set of time offsets. No single function of the checkpoint
and four-phase observations at those offsets recovers

\[
\mathbf1_{\Delta(n)=0\bmod2}
\]

for every origin-zero seed and every sufficiently large unit index
\(n\bmod30\).
The obstruction remains if both seeds are required to belong to the
same prescribed initial sheet.

### Proof

Enlarge the offsets to an interval \([A,B]\) containing zero. Choose
an integer \(r\equiv21\bmod30\) large enough that \(r+A-1\ge0\).
Choose \(M=16^k\), \(k\ge1\), so large that \(r+B<M\) and
\(M+r+A\ge3\).
Set

\[
n=M+r,\qquad n'=2M+r.
\]

For every \(i\in[A-1,B]\), the low binary block \(r+i\) lies in
\([0,M)\). The high blocks of \(n+i\) and \(n'+i\) are respectively
one and two, each with digit sum one. Therefore

\[
s_2(n+i)=1+s_2(r+i)=s_2(n'+i).
\]

All corresponding \(\theta\) and \(\Theta\) values agree, including the
predecessor of the first observed checkpoint.
The reachable target sheets at the start of the windows are consequently
equal. Choose one common checkpoint on that sheet.
Equation (1.1) supplies an initial seed for each window, within any one
prescribed initial sheet. Identical subsequent driver bits and the fixed
maps \(F_0,F_1\) give identical checkpoint windows.

But \(M=16\bmod30\), so \(n=7\bmod30\) and \(n'=23\bmod30\).
These are unit indices. The characters \(\chi_3\chi_5\) are \(-1\)
and \(+1\), respectively. By PROOF.md (2.1), their inert flags differ.
This contradicts the proposed factorization.

The observer was not given the absolute counter or an extra persistent
state. The theorem does not cover one specially fixed initial seed,
an unbounded or adaptively growing history, or the full autonomous state.

The positive ramified result and this negative inert result concern the
same native history class. They are a concrete distinction between the
two places, rather than an analogy based on their names.

### Corollary 4.2: complete periodic classification at sixty

Let \(B(n)=b(n\bmod60)\), on all times or just the unit-index domain.
There exists some fixed finite decorated window and one reader valid
uniformly for all seeds, after warmup, if and only if \(b\) factors
through \(n\bmod4\) on that domain.
The statement remains true when all allowed initial seeds lie in any
one prescribed initial sheet.

Sufficiency is Proposition 3.1, or the registered finite-history phase
theorem. For necessity, fix any two admitted classes \(a_0,a_1\bmod60\)
with \(a_0=a_1\bmod4\), and fix a proposed observation window \([P,Q]\).
Choose a common low block \(r=a_0\bmod4\) sufficiently large to protect
the lower endpoint \(r+P-1\ge0\). Choose a sufficiently large multiple
\(K\) of four so that \(r+Q<2^K\) and the first observed times exceed
two.

A binary integer with fourteen set bits, of which \(t\) are in distinct
positions \(1\bmod4\) and the remaining \(14-t\) in distinct positions
\(0\bmod4\), has residue

\[
14+t\bmod15,\qquad 0\le t\le14.
\]

All fifteen residues occur, with the same exact digit sum fourteen.
Choose two such positive integers \(v_0,v_1\) with residues
\(a_0-r,a_1-r\bmod15\). Since \(2^K=1\bmod15\), the times

\[
n_0=2^K v_0+r,\qquad n_1=2^K v_1+r
\]

have the desired classes modulo sixty. Throughout the protected
window, including its predecessor, corresponding indices have digit
sum \(14+s_2(r+i)\). Align the first checkpoint using (1.1), and
propagate as in Proposition 4.1. The decorated windows coincide.
Thus \(b(a_0)=b(a_1)\), proving the necessity.

This is a classification of which periodic outputs admit some finite
window, not a claim that every fixed short window already reads all
of them. On the sixteen unit classes only the two modulo-four classes
survive this uniform history observation.

## 5. Finite additional memory still cannot certify infinitely many primes

The following abstract closure fact is classical; we include a direct
specialization to the actual native update. It is not claimed as a new
automata theorem.

Let \(X\) be any finite set with fixed maps \(F_0,F_1\), a fixed initial
state, and chronological drive \(\theta_n\).
Let \(M\) be the finite transformation monoid generated by the two maps.
For \(a,b\in M\), define

\[
P_{a,b}(n)=c_{\theta_{n-1}}\circ\cdots\circ c_{\theta_0},
\qquad c_0=a,\quad c_1=b,\quad P_{a,b}(0)=\mathrm{id}.
\]

The identities \(\theta_{2k}=\theta_k\) and
\(\theta_{2k+1}=1-\theta_k\) give

\[
\begin{aligned}
P_{a,b}(2n)&=P_{b\circ a,a\circ b}(n),\\
P_{a,b}(2n+1)&=c_{\theta_n}\circ P_{b\circ a,a\circ b}(n).
\end{aligned}                                             \tag{5.1}
\]

Retaining the finite vector of all \(P_{a,b}(n)\) and \(\theta_n\)
gives a deterministic finite update when a binary digit is appended to
the index. Its output at the original pair and the fixed initial state
is exactly the chronological checkpoint.
Leading zero digits leave the initial vector unchanged.
Thus the state sequence and every fixed finite output from it are
2-automatic.

This applies to fixed finite observer memory as well: put the memory
into the finite state set and use its declared fixed update.
To include \(\Theta_n\) as an input to that update, not merely as a
terminal output, put \(u_n=s_2(n)\bmod4\). For each quadruple
\(C=(c_0,c_1,c_2,c_3)\) of transformations of the enlarged finite state,
let \(P_C\) denote the prefix product driven by \(u_n\), and set
\(T(C)_i=c_{i+1\bmod4}\circ c_i\). Then

\[
P_C(2n)=P_{T(C)}(n),\qquad
P_C(2n+1)=c_{u_n}\circ P_{T(C)}(n).
\]

Retaining all these products and \(u_n\) gives the same finite
index-reading construction, since \(u_{2n}=u_n\) and
\(u_{2n+1}=u_n+1\bmod4\).
The inputs \(\theta_n,\Theta_n\) are functions of \(u_n\).
Any fixed periodic residue channel can be maintained by a finite
chronological counter included in the enlarged state. Thus the claim
covers fixed finite memory fed by the checkpoint, the four-phase
reading and fixed periodic residue channels.

No infinite regular set of canonical binary words consists entirely of
primes. For completeness, suppose a finite automaton accepts an
infinite subset of primes. Choose an accepted odd prime \(p\) whose
word is long enough to have a pumpable nonempty block \(v\), writing
the word \(uvw\). Appending \(v\) to a prefix value modulo \(p\)
acts as the affine permutation

\[
y\longmapsto 2^{|v|}y+[v]_2
\]

of \(\mathbb F_p\). Let \(L\ge1\) be its finite permutation order.
The accepted pumped word \(uv^{1+L}w\) has the same value modulo \(p\),
but is a strictly larger positive integer. It is a composite accepted
as prime, a contradiction.

Consequently a sound prime flag in the stated fixed finite-state class
can mark only finitely many primes. If it is only claimed sound on unit
indices, intersect with the finite residue test modulo thirty first.
Any finite warmup exclusion is harmless to this argument.

This statement does not ban primality algorithms with growing memory,
varying modulus, arithmetic access to the counter, variable output
interpretation, or a different state carrier.

## 6. What a further native construction must specify

The arithmetic digit lift in PROOF.md is already explicit and exact.
Its native realization is a separate open obligation:

- which state or retained history carries its growing precision;
- how that data is written and updated under the declared native law;
- which exact observation map recovers it, on which initial states;
- whether any extra counter, phase or persistent context is supplied.

The single-checkpoint and bounded-history obstructions above constrain
these choices. They do not select a physical apparatus or a cross-layer
interpretation.
