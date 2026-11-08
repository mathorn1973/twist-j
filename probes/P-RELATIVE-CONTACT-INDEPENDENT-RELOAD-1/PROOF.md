# Composition and resource proof for two independent finite loads

**NON-CANONICAL / L1.** Companion to the candidate-C finite audit
`P-RELATIVE-CONTACT-INDEPENDENT-RELOAD-1`.

`CONTRACT.md` fixes the complete carrier, loading map, mixed word and output
equality. This text proves the arithmetic invariants and composition
implications. It explicitly identifies the finite read facts that the new
verifier must discharge on the actual new trajectories. It asserts no
execution result, independent review, Canon theorem or closure of an open
obligation.

The unchanged read construction is from PR #1857 at
`377a99ae11b885e27e863e2323c9a2f6e7d68510`, with its source word SHA-256
`ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b`.
The new composition retains that exposed source and its restrictions.
No earlier verifier result substitutes for executing the new 56-slot word.

## 1. Exact operations and invariants

Write \(O=\mathbb Z[j]\), \(\rho=j^2\), \(u=1-\rho\),
\(w=1+\rho\), and \(b=1+\rho^2\), as in the contract.
On an admitted pair put \(s=(a+b)/2\) and \(d=(a-b)/2\).
Both are integral because coefficientwise evenness of \(a-b\) also makes
\(a+b\) even. The contact sends \((s+d,s-d)\) to
\((s+\rho d,s-\rho d)\). Its output difference is \(2\rho d\),
so repeated contacts remain admitted and rotate the relative coordinate.
As \(\rho^5=1\), their fifth power is the identity. Refused pairs are
identities throughout. Thus \(C^{-1}=C^4\) on the whole pair carrier.

The sum remains \(2s\). With conjugation \(\bar j=j^{-1}\),
\(\rho\bar\rho=1\), and the parallelogram identity gives

\[
 (s+\rho d)\overline{(s+\rho d)}+
 (s-\rho d)\overline{(s-\rho d)}
 =2s\bar s+2d\bar d.
\]

This preserves the full Hermitian account and its half-trace \(Q\).
The four-coefficient formula in the contract follows from cyclotomic
traces. It is integral since \(\sum a_i^2\equiv(\sum a_i)^2\pmod2\),
and positive definite since \((\sum a_i)^2\le4\sum a_i^2\).
Each labelled slot changes by a multiple of \(\rho-1\), so its residue
under \(\epsilon:O\to\mathbb F_5\), \(j\mapsto1\), is unchanged.

A whole-slot transposition is separately an involution and preserves each
complete sum and account. Consequently the full mixed word \(P\) is a
bijection on \(O^{56}\), with the literal inverse stated in the contract.
This conclusion does not compile a transposition into contacts.

## 2. The source orbit and prepared resources

For \(e=1,2,3,4\), the nine source states have the explicit forms

\[
 Y_0=(0,2,0),\qquad
 Y_e=(1-\rho^e,1+\rho^e,0),\qquad
 Y_{4+e}=(0,1+\rho^e,1-\rho^e).
\]

The two contacts of \(F\) carry these successively around their nine-cycle.
Within the first group \(C_{0,1}\) increments the exponent and
\(C_{1,2}\) refuses; at its end \((0,2,0)\) is intermediate and
the second contact enters the second group. Within the second group the
first contact refuses and the second increments the exponent, returning to
\(Y_0\) at its end. For refusal, each \(1+\rho^e\) is nonzero
modulo \(2O\): over \(\mathbb F_2\) the cyclotomic polynomial
\(X^4+X^3+X^2+X+1\) is irreducible, and its root has order five.
The displayed nine states are distinct.

The contact on \(X_k=(\rho^kw,-\rho^kw)\) has zero center and
increments \(k\) modulo five. These five states are distinct. Directly,

\[
 Q(Y_a)=8,\quad \Sigma(Y_a)=2,\qquad
 Q(X_k)=6,\quad\Sigma(X_k)=0,
\]
\[
 Q(u)=5,\qquad Q(w)=Q(b)=3.
\]

Multiplication by \(\rho\) preserves account, so every fresh or valid
recorded ten-slot memory has account 30 and sum zero. The six shared control
slots have account 8 and sum \(u+w=2\). There are two five-slot input
systems and four ten-slot memory sets. Hence

\[
 E_{\rm auxiliary}=8+4\cdot30=128,\qquad
 E_{\rm complete}=14+14+128=156,\qquad
 \Sigma_{\rm complete}=2+2+2=6.
\]

Exactly the ten input-system coordinates vary with \((n,k,m,\ell)\).
The displayed loader therefore gives 46 identical auxiliary coordinates
for every input pair, without preparing an answer-dependent memory bank.

Every source state has labelled residue vector \((0,2,0)\), and each
clock state has residues \((2,3)\). The queued and current input slots
therefore have equal corresponding residues even after the first source
and clock have evolved. Each of the five reload swaps exchanges equal
residues. Contacts preserve the other labelled residues, establishing the
single complete residue vector stated in the contract throughout the word.

## 3. Finite read facts and exact stage composition

On its reachable ready configurations, the 261-contact read \(R\) must
satisfy the following full-state facts:

1. It restores the source presented to that read, receiver clock, zero
   marker and sampling gate, and helper \(w\).
2. At a source phase other than zero it preserves the selector and both
   memory sets, including any occupied memory.
3. At source phase zero with selection A or B and that selected set fresh,
   it changes exactly the pair numbered minus the current clock phase from
   memory phase zero to phase one. The other set is preserved, including
   when occupied.
4. At source phase zero with skip selection, both occupied sets are
   preserved.
5. At source phase zero the selector cycles A to B to skip to A; otherwise
   it stays unchanged.

These are finite obligations on reached states, not an unrestricted theorem
about arbitrary controller or occupied-bank preparations. The new verifier
must check their resulting complete 56-slot states at all 4000 read
boundaries, together with the 2000 complete macrostep boundaries. It must
also verify the oriented source-word expansion and its two actual address
embeddings. It must not replace a read with this abstract transition rule.

To see the stage implications, let a macrostep begin at source/clock phase
\((a,q)\). Its first read sees \(a\); its second, following
\(F^{-1}\), sees \(a-1\). The following \(F\) restores the source
phase, and the final \(FT\) advances source and clock. Under the read facts,
the complete boundary phases are therefore \((a+1,q+1)\).

For an initial source \(s\in\{0,1\}\) and clock phase \(r\), the
phases at step start \(t\) are \((s+t\bmod9,r+t\bmod5)\).
The first read is active at source phase zero and the second at source
phase one. During ten complete steps, the event times are \((0,1,9)\)
for \(s=0\), and \((0,8,9)\) for \(s=1\). These select A, B and
skip in that order. Thus the two codes are
\((-r,-(r+\Delta_s))\), the source ends at \(Y_{s+10}\), the clock
returns to \(X_r\), and all six read controls return to their original
ready state. There is no fourth event in the declared stage.

The finite read facts entail retention at all later read and macrostep
boundaries within that stage: an inactive read preserves occupied sets,
the second acquisition preserves the first set, and the final active read
bypasses both. The source/clock updates touch neither memory. This argument
does not claim constancy of every archive coordinate inside a read.

## 4. Shared-core reload and complete final state

The two embeddings use address maps fixed before any input is selected.
For either embedding, projecting onto its eleven core slots and twenty
memory slots commutes with every contact in that embedded word. Its
complement is untouched. This is an exact consequence of the edge list,
independent of the values in the complement.

Apply the preceding stage implication first to \(S_A^{10}\). The queued
input and both second-stage memories have not changed. The first twenty
memory slots contain their two records, and the shared controls are ready.
This gives the first complete intermediate formula in `CONTRACT.md`.

The fixed \(\Pi\) then exchanges only the two five-slot input systems.
It neither computes the second input nor consults the first record. It
places the independently supplied \((Y_m,X_\ell)\) at the shared input
ports and parks the actual old \((Y_{n+10},X_k)\) in the former cartridge.
All controls and all forty memory slots are unchanged. The full reload
checkpoint therefore has exactly the prescribed formula.

The projection onto the \(S_B\) addresses is now the same common-ready
31-slot preparation as in a first experiment, with input \((m,\ell)\).
The first archives and parked old input are its untouched complement.
Apply the stage implication again. This gives the complete 56-slot endpoint

\[
 (Y_{m+10},X_\ell,0,u,0,0,w,0,
 M[-k],M[-k-\Delta_n],M[-\ell],M[-\ell-\Delta_m],Y_{n+10},X_k).
\]

In particular the first archives are untouched at every primitive contact
of the second stage, not merely restored at its boundaries. The exact new
replay must verify this complement and both complete stage states rather
than simulating two disconnected 31-slot arrays. This is what tests the
actual shared address layout and the physical slot exchanges specified by
the model.

The final disposition keeps both old and new input-system states, all four
records and every control. The second experiment spends fresh stock that
was present initially. It does not reset a used memory or restore every
resource while retaining its records. A return of the selector to A is not
a fresh-memory certificate.

## 5. Decoding only the present four-bank state

For one stage the five present-record states \(M[p]\) are distinct: their
changed labelled pairs occupy different positions, and
\(\rho b\ne b\). They are also distinct from \(M_\emptyset\).
Checking the full coordinates therefore recovers a unique label from any
valid present record, without a separate presence flag or historical input.

For the two labels \((x,y)=(-r,-(r+\Delta_s))\), their difference is
\(\Delta_s\) modulo five. It is one for \(s=0\) and three for
\(s=1\); these are distinct. Thus the current-state reader obtains
\(s\) from the difference and \(r=-x\pmod5\) from the first label.
Applied independently to the two actual bank pairs, it recovers exactly
\(((n,k),(m,\ell))\). The four-bank output map is injective on all
100 inputs. No use of the parked source, original enumeration index,
execution counter or saved input is necessary or permitted by this reader.

This inverse interpretation is confined to the two declared gap values one
and eight. A general clock interval is not recovered from its residue
modulo five. Nor is a probability measure or entropy interpretation part
of this finite injectivity statement.

## 6. Primitive timing, operation counts and inverse

Each \(S\) has read onsets at contact offsets 1 and 270 and completions
at 261 and 530. Adding \(535t\) for the appropriate event step gives
onsets \((1,805)\) or \((270,4281)\), and completions \((261,1065)\)
or \((530,4541)\). Each completion is 260 contacts after its onset;
the two within-stage gaps are therefore 804 and 4011 under either convention.

The second stage begins after 5350 contacts and five transpositions. Thus
its contact-only ordinals receive offset 5350, whereas its complete
elementary-operation ordinals receive offset 5355. Adding a constant to
both endpoints leaves every within-stage gap unchanged. Neither count is
a physical time calibration. The designated onset definition does not
assert that \(g\) remains a binary flag at all internal contacts.

There are twenty 535-contact macrosteps and five swaps per case. Each
macrostep contains two read boundaries, and each ten-step stage has three
events. Across 100 cases this gives 2000 macrostep boundaries, 4000 read
boundaries, 100 reload checkpoints and 600 events.

Reversing \(P\), replacing every \(C\) by \(C^4\), and reversing
the five self-inverse swaps yields 42,800 contacts and five swaps per inverse.
The exact full inverse exists on every state by section 1; the finite audit
must additionally execute it and compare all 56 recovered coordinates with
the complete preparation in each case. Forward plus inverse trajectories
therefore use

\[
 100(10\,700+42\,800)=5\,350\,000
\]

contact applications and \(100(5+5)=1000\) supplied transpositions.
Source-orbit setup and any separately performed local arithmetic checks are
not included in these trajectory counters.

## 7. Evidential and physical limits

The new finite execution must discharge the reached-state read facts in
both embedded stages, check the complete reload and endpoint formulas,
validate a decoder acting only on current archive coordinates, and preserve
any failed prediction. Proof by copying source results or by assigning
expected intermediate states is not an execution of this composition.

The fixed word supplies finite reuse of a shared read core with independently
prepared delayed input and fresh memory stock. It does not prepare those
inputs from raw or thermal data, accept an arbitrary external input stream,
compile its five swaps into contacts, regenerate used memory, prove a minimum,
or provide unbounded reuse. Native U, physical realization, measured energy,
occurrence and cross-layer transfer remain outside scope. The analytical
arguments and any eventual candidate-C evidence do not themselves close the
common-apparatus Canon obligation.
