# Round 2 proof: exactly fifteen persistent states

NON-CANONICAL. No authority. All new conclusions candidate-D, L1.
Paper continuation of C-J-TWO-PLACE-FROBENIUS-N, issue #2080.

## 1. Declared observer class

Fix one origin-zero native seed and a finite offset window \(W_n\) of
the decorated observations \(Y=(\psi,\Theta)\) defined in
[PROOF.md](PROOF.md). The extra observer has a finite state set \(H\),
one actual state \(h_n\in H\) at each tick, and fixed deterministic maps

\[
h_{n+1}=A(h_n,W_n),\qquad b_n=B(h_n,W_n).
\tag{1.1}
\]

The actual state can depend on the entire prior run; we do not reset it
at the copied windows. Correctness is required after a fixed warmup at
every time \(n\) coprime to thirty. Updates occur at **every chronological
native tick**, including times at which no output is required. There
is no absolute-time input, external calendar, unit-only visitation
schedule, feedback into the native system, or undeclared context state.
The maps and initial state may be designed for this fixed seed.

The target is the inert-defect flag

\[
b_n=\mathbf1_{\Delta(n)=0\bmod2\mathcal O}
=\mathbf1_{\chi_3(n)\chi_5(n)=+1}
\quad\text{when }\gcd(n,30)=1.
\tag{1.2}
\]

Only \(|H_{\rm reachable}|\), the number of reachable extra persistent
states, is counted below. A fixed observation window is an allowed input
resource; its own physical storage cost is additional. A one-time
externally supplied answer bit is not the chronological observer (1.1).

## 2. Every nonzero phase difference can be separated

**Lemma 2.1 [candidate-D].** For each nonzero \(d\in\mathbb Z/15\mathbb Z\)
there is \(x\) such that \(x\) and \(x+d\) are units modulo fifteen and

\[
(\chi_3\chi_5)(x+d)=-(\chi_3\chi_5)(x).
\tag{2.1}
\]

Write \(d_3,d_5\) for its residues modulo three and five. If \(d_3=0\),
then \(d_5\ne0\). Choose \(x=1\pmod3\) and \(x=d_5\pmod5\). The
three-character is unchanged, while the five-character changes sign
because \(x+d=2x\pmod5\) and \(\chi_5(2)=-1\).

If \(d_3\ne0\), choose \(x=d_3\pmod3\). Then \(x+d=-x\pmod3\), so
the three-character changes sign. If \(d_5=0\), choose any nonzero
\(x\pmod5\). Otherwise choose \(x=2d_5\pmod5\), giving
\(x+d=3d_5=-x\pmod5\). Since \(\chi_5(-1)=+1\), the five-character
is unchanged. The Chinese remainder theorem combines the choices.

For two start times whose difference is \(d\pmod{15}\) and whose
parities agree, a common shift \(0\le e\le29\) can therefore make
both times odd units with opposite target flags: prescribe the first
shifted residue to be \(x\pmod{15}\), and its parity to be odd.

## 3. The sharp lower bound

**Theorem 3.1 [candidate-D].** Every observer in Section 1 that is
correct on all required unit times has at least fifteen reachable
persistent states.

**Proof.** Choose one sufficiently late native observation block
containing every input window \(W_{r+e}\), \(0\le e\le29\). By the
copy theorem in PROOF.md, this complete block has fifteen copies on
the same fixed-seed trajectory, at starts \(N_0,\ldots,N_{14}\) with
all fifteen residues modulo fifteen and the same parity. All copies
can lie after warmup.

If there were at most fourteen reachable states, two of the actual
states at these starts would agree: \(h_{N_i}=h_{N_j}\), \(i\ne j\).
Their inputs \(W_{N_i+e},W_{N_j+e}\) agree for every \(0\le e\le29\).
Induction in (1.1) then gives equal extra states and outputs at the
corresponding times throughout that common future.

The two start residues have a nonzero difference modulo fifteen.
Lemma 2.1 supplies a common shift of at most twenty-nine making both
times admissible and the required outputs opposite. This contradicts
their equality. The actual states at the copies were never assumed
to have a shared initialization; their equality follows only from
the count of reachable states. QED.

This proves the bound even for the single binary flag, not just for
reconstruction of the full residue modulo fifteen. It also explains
why counting only the eight unit residue classes would be insufficient:
the state must evolve correctly through all intervening ticks.

## 4. An attaining register from J

**Theorem 4.1 [candidate-D, using the registered order of J modulo two].**
Fifteen extra persistent states suffice, with no dependence on the
native seed or input window.

Let \(g=J\bmod2\) in \(\mathcal O/2\mathcal O=\mathbb F_{16}\).
The registered result J-BINARY-NORM-INDEX gives \(\operatorname{ord}(g)=15\).
No proper subfield of \(\mathbb F_{16}\) contains an element of that
order, so \(1,g,g^2,g^3\) is a basis over \(\mathbb F_2\).
Its polynomial identity is

\[
g^4+g^3+1=0.
\tag{4.1}
\]

For example, this follows by reducing the minimal polynomial
\(X^4-3X^3+4X^2-2X+1\) of \(J\) modulo two. Direct use of
\(g=1+j^2\) and \(1+j+j^2+j^3+j^4=0\) gives

\[
g^3=j^3,\qquad g^6=j,\qquad g^{12}=j^2=g+1.
\tag{4.2}
\]

Initialize \(c_0=1\) and set \(c_{n+1}=gc_n\). Then \(c_n=g^n\),
and in characteristic two

\[
\Delta(n)\bmod2\mathcal O
=g^n+1+j^{2n}=c_n+1+c_n^{12}.
\tag{4.3}
\]

Testing the right side for zero supplies the required flag at every
index, not merely at unit indices. The fifteen nonzero field elements
are exactly the states visited by this register.

Write \(c=z_0+z_1g+z_2g^2+z_3g^3\). Equation (4.1) gives the explicit
binary update

\[
(z_0,z_1,z_2,z_3)\mapsto(z_3,z_0,z_1,z_2+z_3).
\tag{4.4}
\]

The start is \((1,0,0,0)\); addition in (4.4) is modulo two. Four bits
provide sixteen possible encodings, of which exactly fifteen are
used. Initialization at an arbitrary later time \(T\) needs the correct
\(c_T=g^T\). This is explicit supplied phase information, not a phase
learned from a finite synchronized window.

Combining Theorems 3.1 and 4.1 establishes the exact minimum fifteen
for the declared persistent-observer class. It does not establish a
physical memory device or an invariant subsystem of the native U.

## 5. Coupling the odd phase to the registered dyadic history

**Inherited T.** U-FINITE-HISTORY-CLOCK-PHASE reads \(n\bmod2^k\) from
a finite synchronized native history, for every fixed \(k\ge1\).
Its sufficient drive-bit window length is \(5\cdot2^{k-1}\). Native
checkpoint traces provide \(\theta_{n-1}\), hence the corresponding
one-step correction in the endpoint phase.

**Candidate-D.** For \(k\ge2\), that reading together with \(c_n\)
determines \(n\bmod(15\cdot2^k)\). The map \(n\bmod15\mapsto g^n\)
is bijective, and the Chinese remainder theorem combines its inverse
with the dyadic phase.

By [first-round PROOF.md, Section 4](../PROOF.md), the latter residue
is exactly the information carried by

\[
\Delta(n)\bmod(5\cdot2^{k+1})\mathcal O.
\tag{5.1}
\]

The restriction \(k\ge2\) matters: at modulus twenty the arithmetic
period is sixty, so a phase modulo thirty would not suffice. The
general arithmetic period is \(15\cdot2^{\max(2,k)}\).

For every fixed precision this constructs a fully specified L1
observer extension. Its stated sufficient retained dyadic history
length grows with precision. The fifteen-state result counts only the
additional persistent odd phase; it is not a total apparatus-memory
bound. A native carrier for both retained resources remains an open
and separately scoped task.
