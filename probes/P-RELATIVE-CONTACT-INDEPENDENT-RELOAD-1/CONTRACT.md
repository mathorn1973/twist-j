# Two independent loads through one finite contact read core

**NON-CANONICAL / L1 / candidate-C finite audit.**
Probe: `P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1`.
Public reservation: [issue #1870](https://github.com/mathorn1973/twist-j/issues/1870).

This contract supplies two independently variable, initially prepared input
cartridges to one shared read core. The second cartridge enters that core
after the first experiment has completed. The first records remain present
while the same read construction acts on the second input and fresh funded
memory. Every operation and every changing resource belongs to the declared
finite carrier. No execution result is asserted in this document.

The source is the result-exposed ten-input construction in
[PR #1857](https://github.com/mathorn1973/twist-j/pull/1857), exact head
`377a99ae11b885e27e863e2323c9a2f6e7d68510`, under
`probes/P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1/`. Its fixed word is reused
without modifying that owned probe. This is a new composition and reload
audit, not a claim of blind discovery or independent acceptance of its
source. The new verifier must execute the complete new trajectories; source
results are not substituted for those executions.

## 1. Carrier, accounts and supplied operations

Let

\[
 O=\mathbb Z[j],\qquad 1+j+j^2+j^3+j^4=0,\qquad
 \rho=j^2,\quad u=1-\rho,\quad w=1+\rho,\quad b=1+\rho^2.
\]

Coordinates use the marked basis \((1,j,j^2,j^3)\). For
\(a=\sum_{i=0}^3 a_i j^i\), define

\[
 Q(a)=\frac{5\sum_i a_i^2-(\sum_i a_i)^2}{2},\qquad
 \epsilon(a)=\sum_i a_i\pmod5.
\]

The complete state carrier is \(O^{56}\). The total account and ring sum
are \(E(z)=\sum_i Q(z_i)\) and \(\Sigma(z)=\sum_i z_i\).
The supplied total contact is

\[
 C(a,b)=
 \begin{cases}
 (a,b),&a-b\notin2O,\\
 ((a+b+\rho(a-b))/2,(a+b-\rho(a-b))/2),&a-b\in2O.
 \end{cases}
\]

It has \(C^5=\mathrm{id}\), so its inverse is four actual applications
of the same contact. Each contact preserves the pair sum, Hermitian account,
positive half-trace account and both labelled residues modulo \(1-j\).

The alphabet also contains a supplied whole-slot transposition
\(\operatorname{SWAP}_{i,j}\), exchanging two complete ring coordinates.
These transpositions preserve complete sums and accounts and are their own
inverses. They are **additional operations**, not an asserted contact-only
implementation or a native-U gate. A transposition generally permutes
labelled residues; the five specified transpositions below exchange equal
residues on this input family.

All addresses below are zero based. Products are chronological, from left
to right. No operation is selected by an observed input, intermediate answer,
record or acceptance pattern. The primitive contact's own admission rule
is the only data-dependent branch in this fixed mixed word.

## 2. Inputs, common preparation and complete allocation

Put

\[
 F=C_{0,1}C_{1,2},\qquad Y_a=F^a(0,2,0),\qquad
 X_k=(\rho^k w,-\rho^k w).
\]

The source subscript is reduced modulo nine and the clock subscript modulo
five. Let \(M_\emptyset\) be the ten-slot fresh memory
\((-b,b)^5\). For \(p\in\mathbb Z/5\), let \(M[p]\) be the same
five labelled pairs except that pair \(p\) is
\((-\rho b,\rho b)\). Thus \(M[0]\ne M_\emptyset\): record zero
is a present record, not absence.

The input domain is exactly

\[
 I=\{0,1\}\times\mathbb Z/5,\qquad
 I\times I=\{(n,k,m,\ell):n,m\in\{0,1\},\ k,\ell\in\mathbb Z/5\}.
\]

It contains 100 ordered input pairs. Independence means this full Cartesian
domain, not a probability assumption. The complete loading map is

\[
 L(n,k,m,\ell)=
 (Y_n,X_k,0,u,0,0,w,0,
  M_\emptyset,M_\emptyset,M_\emptyset,M_\emptyset,Y_m,X_\ell).
\]

| Slots | Role | Initial contents | Account |
| --- | --- | --- | ---: |
| 0..2 | Current source | \(Y_n\) | 8 |
| 3..4 | Current receiver clock | \(X_k\) | 6 |
| 5 | Marker \(g\) | 0 | 0 |
| 6..8 | Selector A, B, skip | \((u,0,0)\) | 5 |
| 9 | Helper \(h\) | \(w\) | 3 |
| 10 | Sampling gate \(t\) | 0 | 0 |
| 11..20 | First experiment, archive A | \(M_\emptyset\) | 30 |
| 21..30 | First experiment, archive B | \(M_\emptyset\) | 30 |
| 31..40 | Second experiment, archive A | \(M_\emptyset\) | 30 |
| 41..50 | Second experiment, archive B | \(M_\emptyset\) | 30 |
| 51..53 | Queued independent source | \(Y_m\) | 8 |
| 54..55 | Queued independent clock | \(X_\ell\) | 6 |

Only the ten input-system slots \(0..4,51..55\) vary. The other **46
auxiliary slots have one common initial state**, of account **128**. Every
complete preparation has account **156** and ring sum **6**.
The initial labelled residue vector, common to all 100 preparations, is

\[
 (0,2,0,2,3,0,0,0,0,2,0,(3,2)^{20},0,2,0,2,3).
\]

Both inputs and all four fresh memory sets are supplied before execution.
The loader is the displayed initial-state interface. There is no claim that
these states are prepared from one raw scalar, a thermal state or an
unspecified reservoir by the contact word. The second input is independent
of the first answer, but is not chosen externally after execution starts.

## 3. The unchanged read word and its two address embeddings

The source `WORD535.txt` uses one-based addresses and has SHA-256
`ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b`.
Its complete zero-based expansion is fixed by the following blocks. A power
means literal repetition, never substitution of an expected endpoint.

\[
 O=C_{1,5},\quad A_0=C_{5,9},\quad B_c=C_{c,9},\quad
 O_2=C_{9,10},\quad T=C_{3,4},
\]
\[
 E_c=A_0B_cA_0^4B_c^4,\qquad E_c^{-1}=B_cA_0B_c^4A_0^4.
\]

For memory base \(q=11\) or 21 and \(p=0,\ldots,4\), put
\(a_p=q+2p\), \(b_p=q+2p+1\), and define

\[
 K_p=C_{3,a_p}^4C_{a_p,b_p}^4C_{3,a_p}C_{a_p,b_p},\qquad
 \operatorname{SCAN}_q=\prod_{p=0}^4(C_{3,10}K_pC_{3,10}^4T).
\]

The product order is increasing \(p\). Define

\[
 W_A=E_6O_2\operatorname{SCAN}_{11}O_2^4E_6^{-1},\qquad
 W_B=E_7O_2\operatorname{SCAN}_{21}O_2^4E_7^{-1},
\]
\[
 D(c,d)=C_{9,c}^3C_{9,d}^3C_{9,c}C_{9,d}C_{9,c},\qquad
 V(c,d)=A_0D(c,d)A_0^4D(c,d),
\]
\[
 R=OW_AW_BV(7,8)V(6,7)O^4,\qquad
 S=RF^{-1}RFFT,\qquad F^{-1}=C_{1,2}^4C_{0,1}^4.
\]

The lengths are \(|W_A|=|W_B|=105\), \(|R|=261\), and \(|S|=535\).
The new audit must compare the expanded oriented contacts with the exact
source word, not merely its unordered edge set.

Let \(S_A\) embed this word at its original addresses \(0..30\).
Let \(S_B\) apply the fixed address map

\[
 \phi(i)=i\quad(0\le i\le10),\qquad
 \phi(i)=i+20\quad(11\le i\le30)
\]

to every edge of \(S\). Both embeddings therefore share precisely the
eleven-slot source/clock/read core. Their twenty-slot memory sets are
disjoint. This address change is a fixed program definition, not a physical
permutation or a choice made during execution.

## 4. One mixed word and the exact reload interface

The five supplied transpositions are

\[
 \Pi=\operatorname{SWAP}_{0,51}\operatorname{SWAP}_{1,52}
      \operatorname{SWAP}_{2,53}\operatorname{SWAP}_{3,54}
      \operatorname{SWAP}_{4,55}.
\]

For every member of the input family apply exactly the same word

\[
 \boxed{P=S_A^{10}\,\Pi\,S_B^{10}.}
\]

There are **10,700 primitive contacts and five supplied transpositions**,
or 10,705 operations when each transposition counts as one operation.
There is no later external injection, erasure, relabelling of the state,
answer lookup or free resource reset.

Define \(\Delta_0=1\), \(\Delta_1=8\), and, modulo five,

\[
 a=-k,\quad b_1=-(k+\Delta_n),\qquad
 c=-\ell,\quad d=-(\ell+\Delta_m).
\]

After \(S_A^{10}\) the complete predicted state is

\[
 (Y_{n+10},X_k,0,u,0,0,w,0,
  M[a],M[b_1],M_\emptyset,M_\emptyset,Y_m,X_\ell).
\]

Immediately after \(\Pi\) it is

\[
 (Y_m,X_\ell,0,u,0,0,w,0,
  M[a],M[b_1],M_\emptyset,M_\emptyset,Y_{n+10},X_k).
\]

This is the full reload checkpoint. The second experiment receives the same
ready read controls and fresh selected memories as the first. The old source
and clock remain as literal occupied values in slots \(51..55\), and both
first archives stay at their original addresses. The five swaps do not
touch any control or archive slot.

The complete final prediction is

\[
 \boxed{P L(n,k,m,\ell)=
 (Y_{m+10},X_\ell,0,u,0,0,w,0,
  M[a],M[b_1],M[c],M[d],Y_{n+10},X_k).}
\]

No coordinate is suppressed from either endpoint or from the inverse test.

## 5. Current-state records, retention and funded reuse

The reader inspects only the four actual ten-slot banks at \(11..50\).
It first requires each to equal one and only one of the five valid states
\(M[p]\). A fresh bank, an invalid pair, or multiple changed pairs is
not accepted as a record. It then reads their four labels \((a,b_1,c,d)\).
For each ordered label pair \((x,y)\), use

\[
 \operatorname{decode}(x,y)=
 \begin{cases}
 (0,-x\bmod5),&x-y\equiv1\pmod5,\\
 (1,-x\bmod5),&x-y\equiv3\pmod5,\\
 \text{invalid},&\text{otherwise}.
 \end{cases}
\]

The output is \((\operatorname{decode}(a,b_1),
\operatorname{decode}(c,d))\). The reader receives neither the original
input tuple nor saved input copies, event counters, source leftovers or
expected outputs. The audit may compare the independently decoded answer
with the enumerated input afterwards. Exactly 100 four-bank code tuples
are predicted, one for each input pair.

Within each ten-step experiment, retention is required at every complete
\(R\) and \(S\) boundary after acquisition, through that experiment's
end. It is not required after every primitive contact within a read.
After the first ten-step experiment finishes, its twenty archive slots are
untouched by \(\Pi\) and every primitive operation of \(S_B^{10}\).
Their retention is therefore literal throughout the entire remaining word.
The queued cartridge and second memories likewise remain untouched during
the first experiment; the parked old input remains untouched during the
second experiment.

The shared core is reused, but fresh memory is consumed. Across the whole
word, the number of fresh ten-slot sets falls \(4\to3\to2\to1\to0\).
Each retains its account 30 when occupied. The complete account remains
156; freshness is not a dissipated-energy account. The end has four retained
records and no remaining fresh memory in the declared stock. No third
experiment or repeated application of \(P\) on that occupied endpoint is
covered by this contract.

## 6. Events and timing conventions

In each stage number local step starts by \(r=0,\ldots,9\). For source
input \(s=0\), the event steps are \((0,1,9)\); for \(s=1\), they are
\((0,8,9)\). The first two events write A then B, and the third uses the
skip selector. The selector returns to A, while both memories remain used.

An onset is the designated first contact of an active read, at local
\(S\)-contact offset 1 or 270, changing \(g=0\) to \(u\).
Completions are offsets 261 or 530. Other internal changes of \(g\) are
not additional events; the marker alone is not an invariant binary gate
throughout an active read. The reload is a scheduled loading boundary, not
an additional onset under this definition.

| Stage-local source input | First two onset ordinals | First two completion ordinals | Gap |
| --- | --- | --- | ---: |
| 0 | 1, 805 | 261, 1065 | 804 |
| 1 | 270, 4281 | 530, 4541 | 4011 |

For the second stage add **5350** when counting only contact applications,
or **5355** when counting all contacts and transpositions as elementary
operations. The five transpositions occupy elementary-operation ordinals
5351 through 5355. The gaps within either stage remain 804 or 4011 under
both conventions. No physical duration or elapsed-time calibration is
assigned to either operation count.

## 7. Required new finite audit and scope boundary

The new verifier must execute all 100 complete trajectories and their exact
primitive inverses. It must check the word embedding, common preparation,
complete 56-slot read/step states, full reload checkpoint, current-state
decoder, archive retention, accounts, residues and event/timing predictions.
The frozen trajectory counts are:

| Quantity | Required total over 100 cases |
| --- | ---: |
| Complete \(S\) boundaries | 2000 |
| Complete \(R\) boundaries | 4000 |
| Complete reload checkpoints | 100 |
| Designated events | 600 |
| Complete inverse restorations | 100 |
| Contact applications, forward and inverse | 5,350,000 |
| Supplied transpositions, forward and inverse | 1000 |

Per case the inverse has **42,800 contacts and five transpositions**: reverse
the full mixed word, replace each contact by four contacts, and retain each
swap as its own inverse. Any local source-orbit setup or standalone local
arithmetic checks are counted separately from these trajectory totals.

Tolerance is zero. An incorrect full checkpoint, invalid or colliding record,
changed retained archive, wrong schedule/count, invariant violation, wrong
word or failed inverse falsifies the relevant frozen prediction. The source
probe's reported success cannot discharge a failed new composition audit.

This is a supplied finite mixed-alphabet apparatus. It asserts no minimum
slot count, account or word length; no contact-only implementation of the
loader; no arbitrary external post-start inputs; no universal initialization,
thermal preparation, autonomous renewal, indefinitely reusable bank, native-U
compilation, physical energy identification, occurrence law or cross-layer
transfer. It neither closes `RELATIVE-CONTACT-COMMON-APPARATUS-OPEN` nor changes
any Canon status. Its evidence remains the actual new finite execution and
the separately stated analytical arguments and review.
