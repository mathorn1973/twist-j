# A common contact apparatus with two informative timestamps

**NON-CANONICAL / L1 / candidate-C.** Public confirmation contract, 2026-11-02.
Probe: `P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1`.
The construction and its ten-input result were exposed during incubation.
This document does not claim a blind preregistration or change a Canon status.

The proposed positive result concerns the existence clause of
`RELATIVE-CONTACT-COMMON-APPARATUS-OPEN`. Its finite domain is exactly the ten
preparations below and their declared occupied continuations. The proof
obligations, exact replay and outcome are distinguished in `PROOF.md`,
`PREREG.md` and the eventual result record.

## 1. Complete carrier and primitive law

Let \(\mathcal O=\mathbb Z[j]\), where \(1+j+j^2+j^3+j^4=0\), and set
\(\rho=j^2\), \(u=1-\rho\), \(w=1+\rho\), \(b=1+\rho^2\).
Use the four-coefficient basis \(1,j,j^2,j^3\). The integral account is

\[
Q(a)=\frac{5\sum_{i=0}^3 a_i^2-(\sum_{i=0}^3 a_i)^2}{2}.
\]

The complete carrier is \(\mathcal O^{31}\). A primitive ordered contact is

\[
C(a,b)=
\begin{cases}
(a,b),&a-b\notin2\mathcal O,\\
((a+b+\rho(a-b))/2,(a+b-\rho(a-b))/2),&a-b\in2\mathcal O.
\end{cases}
\]

Every accepted output is integral. A contact preserves the pair sum, pair
account and each labelled residue modulo \(1-j\); \(C^5=\mathrm{id}\).
All words act chronologically from left to right. No register or operation
that changes during the experiment is omitted from this carrier and word.

## 2. Input family, loading and common resources

Addresses in this document are zero based. Let
\(F=C_{0,1}C_{1,2}\), \(Y_n=F^n(0,2,0)\), with \(n\) modulo nine, and
\(X_k=(\rho^kw,-\rho^kw)\), with \(k\) modulo five.
The declared input system consists of the three source slots and the two
receiver-clock slots. The input family and loading map are exactly

\[
I=\{0,1\}\times\mathbb Z/5,\qquad
L(n,k)=(Y_n,X_k,0,u,0,0,w,0,(-b,b)^5,(-b,b)^5).
\]

All **26 auxiliary slots have one common initial state** for every input.
The five input slots vary only through this map. At a fixed \(k\), changing
\(n\) changes only the three source slots, so the other 28 slots are then
identical. The two independently admitted phases mean a Cartesian product
of preparations; no probability or statistical-independence assumption is
made. Loading is initial preparation. There is no later external injection.

| Slots | Role | Initial state | Total account |
|---|---|---|---:|
| 0–2 | Arrival source | \(Y_n\) | 8 |
| 3–4 | Receiver clock | \(X_k\) | 6 |
| 5 | Marker \(g\) | 0 | 0 |
| 6–8 | Selector A, B, S | \((u,0,0)\) | 5 |
| 9 | Helper \(h\) | \(w\) | 3 |
| 10 | Sampling gate \(t\) | 0 | 0 |
| 11–20 | Memory set A, five pairs | \((-b,b)^5\) | 30 |
| 21–30 | Memory set B, five pairs | \((-b,b)^5\) | 30 |
| All 31 | Complete preparation | \(L(n,k)\) | **82** |

The total sum is 4. Account is an arithmetic invariant, without an
identification with measured physical energy. No input-dependent controller,
memory preparation or operation word is allowed.

## 3. Complete fixed word

`WORD535.txt` is the normative primitive sequence, including orientation.
Its lines use **one-based** addresses. Its SHA-256 is

`ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b`.

The following zero-based block specification must expand to exactly the
same ordered, oriented contacts after conversion to one-based addresses.
A power means literal repetition. Define

\[
O=C_{1,5},\quad A_0=C_{5,9},\quad B_c=C_{c,9},\quad O_2=C_{9,10},\quad T=C_{3,4},
\]
\[
E_c=A_0B_cA_0^4B_c^4,\qquad E_c^{-1}=B_cA_0B_c^4A_0^4.
\]

For memory base \(m=11\) or 21, and \(p=0,\ldots,4\), put
\(a_p=m+2p\), \(b_p=m+2p+1\), and

\[
K_p=C_{3,a_p}^4 C_{a_p,b_p}^4 C_{3,a_p}C_{a_p,b_p},\qquad
\mathrm{SCAN}_m=\prod_{p=0}^4(C_{3,10}K_pC_{3,10}^4T).
\]

The product order is increasing \(p\). Define the 105-contact wrappers

\[
W_A=E_6O_2\mathrm{SCAN}_{11}O_2^4E_6^{-1},\qquad
W_B=E_7O_2\mathrm{SCAN}_{21}O_2^4E_7^{-1}.
\]

Finally,

\[
D(c,d)=C_{9,c}^3C_{9,d}^3C_{9,c}C_{9,d}C_{9,c},\qquad
V(c,d)=A_0D(c,d)A_0^4D(c,d),
\]
\[
R=O W_A W_B V(7,8)V(6,7)O^4,\qquad |R|=261,
\]
\[
S=R F^{-1}R F F T,\qquad F^{-1}=C_{1,2}^4C_{0,1}^4,\qquad |S|=535.
\]

The macrostep is named \(S\), not the Canon's native \(U\). The same literal
word is applied for every input and step, including occupied continuations.
The state dependence belongs to the primitive acceptance rule. The supplied
word is the common law; no compiler into a simpler native update is claimed.

## 4. Event schedule and common horizon

Run exactly \(S^{10}\), or 5350 primitive contacts, from every \(L(n,k)\).
Number starting step times \(t=0,\ldots,9\). The first read in \(S\) tests
source phase zero; \(F^{-1}RF\) tests phase one. At each complete step boundary
the source and clock advance by one on their respective orbits.

| Source input | Event steps | First-to-second clock increments |
|---|---|---:|
| \(n=0\) | 0, 1, 9 | 1 |
| \(n=1\) | 0, 8, 9 | 8 |

For both inputs the first event writes A, the second writes B, and the third
uses selector S and writes neither. The selector advances A to B to S to A.
There is no fourth event in this positive contract. S is a selector label
as well as the macrostep's chosen notation; the selector's role is always
explicit. It supplies one bypass, not permanent shutdown.

## 5. Record equality, absence and information

A memory pair in phase \(r\) is exactly \((-\rho^rb,\rho^rb)\).
A fresh set has all five pair phases zero. A present record labelled
\(p\in\mathbb Z/5\) has phase one in pair \(p\) and zero in the other four.
Thus a present record labelled zero is distinct from an absent record.
Record equality is exact equality of all ten labelled ring coordinates;
no phase, permutation or other quotient is applied to the output.

Let \(\Delta_0=1\) and \(\Delta_1=8\). The final record labels are

\[
p_A=-k\pmod5,\qquad p_B=-(k+\Delta_n)\pmod5.
\]

The **ordered pair** of records distinguishes all ten inputs. Neither
individual five-valued record does so. Decode

\[
d=p_A-p_B\pmod5,\quad
d=1\Rightarrow(n,\Delta)=(0,1),\quad
d=3\Rightarrow(n,\Delta)=(1,8),\quad k=-p_A\pmod5.
\]

Each first record has exactly two possible second records. For example,
\(k=0\) gives \((0,4)\) and \((0,2)\). The source distinction is absent
from the first record and present in the second. Each acquisition records
the clock phase at that acquisition; the two records together identify the
declared initial input.

The clock reads increments modulo five. The inverse interpretation of
\(d\) is exact only on the declared interval set \(\{1,8\}\). Intervals
1 and 6 would alias. No arbitrary integer interval measurement, old
\(K=9p\pmod{45}\) interpretation, or probabilistic information measure is
asserted.

## 6. Primitive timing

An onset is the designated first \(O=C_{1,5}\) contact of an active read
that changes \(g=0\) to \(u\). Its performed-contact offset in \(S\) is
1 or 270. Acquisition completes at the end of that active \(R\), at offset
261 or 530. An arbitrary internal change of \(g\), or acceptance of a
zero/zero contact, is not an additional onset. The gate is carried by the
joint control state; \(g\) alone is not assumed to remain a binary flag
throughout a read.

| Source input | First two onset ordinals | First two completion ordinals | Elapsed contacts |
|---|---|---|---:|
| 0 | 1, 805 | 261, 1065 | 804 |
| 1 | 270, 4281 | 530, 4541 | 4011 |

Every completion is 260 contacts after its onset, so the two interval
conventions agree here. The clock's one or eight free increments do not
mean 535 or 4280 primitive contacts. The active read windows have different
offsets. A pair's internal write contact can also depend on the captured
phase and is not silently identified with onset or completion.

## 7. Retention, funded reuse and capacity boundary

Retention is required at every later completed \(R\) and \(S\) boundary
after a record's acquisition, through the common end. At those checkpoints
A and then B must be exactly unchanged. Individual archive coordinates may
rotate inside \(R\); constancy after every primitive contact is not claimed.

After event one, the read core has its zero guards and helper \(w\) restored,
and selector B points to the already funded fresh second set. This is the
renewed ready configuration for the next admissible acquisition while A
remains an archive. The next arrival is supplied by the prepared deterministic
source. No arbitrary later reload is part of the contract.

Ready sets change in number \(2\to1\to0\), while retained sets change
\(0\to1\to2\). Each ten-slot set retains account 30. The spent resource is
its fresh condition, not a loss of conserved account. Both sets, source,
clock and controller remain in the full final state. No changing resource
is discarded or reset for free.

All ten initial states have the same labelled residue vector modulo \(1-j\),
and all ten final states have that same vector:

\[
(0,2,0,2,3,0,0,0,0,2,0,(3,2)^{10}).
\]

Here entries are in \(\mathbb Z/5\) and the last pair is repeated ten times.
Records are stored in **phases within a fixed residue fibre**. No residue
change or residue-capacity increase is claimed. The admitted record code
has five present values per set and ten reachable ordered pairs under this
contract. The prepared stock supports two retained acquisitions and one
subsequent bypass within the declared horizon; no larger capacity or
indefinite renewal is asserted.

## 8. Complete final disposition

After exactly ten steps the full state must be

\[
(Y_{n+10\bmod9},X_k,0,u,0,0,w,0,A[p_A],B[p_B]).
\]

The source has advanced ten times, the clock returns to phase \(k\), the
selector returns to A, both gates are zero, and the helper is \(w\). Both
formerly fresh sets are archives. Total account remains 82 and total sum 4.

Reverse all primitive contacts and replace each by its fourth power to
obtain the exact inverse. It must return every final state to its complete
preparation. This inverse removes the records and is not claimed as renewal
with records retained. A run beyond the declared end has no retention or
readiness guarantee here.

## 9. Scope of the proposed row-O witness

The carrier, initial input interface, common auxiliary resources, complete
law, exact output equality, finite retention checkpoints, funded second use
and disposition of every changing register are fixed together. All ten
inputs and their occupied continuations must pass the same exact checks.
This is a finite L1 candidate for the common-apparatus existence clause.

The public replay and independent review determine its evidential status.
This contract does not itself close the registry row, promote a theorem,
change the Canon, establish physical realization, identify physical energy,
compile to native \(U\), or transfer a result to another layer.
