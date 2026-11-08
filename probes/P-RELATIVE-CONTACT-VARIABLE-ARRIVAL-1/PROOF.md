# Composition proof and finite proof obligations

**NON-CANONICAL / L1.** Algebraic deductions below are candidate-T; the
complete ten-input execution is candidate-C. This public text is
result-exposed. It is a new presentation of a known construction, not an
unread prediction. `CONTRACT.md` fixes the full domain and normative word.
Probe: `P-RELATIVE-CONTACT-VARIABLE-ARRIVAL-1`.

## 1. The primitive preserves the declared carrier

For an accepted pair put \(s=(a+b)/2\) and \(d=(a-b)/2\).
Its output is \((s+\rho d,s-\rho d)\), which is integral. Its difference
is \(2\rho d\), so it stays in the accepted parity class. Repeating the
contact multiplies \(d\) by \(\rho\), and \(\rho^5=1\). Rejected pairs
are fixed. Therefore the total contact has fifth power identity.

The pair sum is \(2s\). The quadratic form is invariant under multiplication
by \(j\), as follows by substitution of
\((a_0,a_1,a_2,a_3)\mapsto(-a_3,a_0-a_3,a_1-a_3,a_2-a_3)\).
The parallelogram identity then gives

\[
Q(s+\rho d)+Q(s-\rho d)=2Q(s)+2Q(d)=Q(a)+Q(b).
\]

Acceptance makes both \(s\) and \(d\) integral, since coefficientwise
evenness of \(a-b\) also makes \(a+b\) even.
Each labelled coordinate changes by a multiple of \(\rho-1\), since
\(a'=a+(\rho-1)d\) and \(b'=b-(\rho-1)d\).
As \(\rho-1\) is divisible by \(1-j\), the labelled residue vector is
fixed. In four-coefficient form the residue is \(\sum a_i\pmod5\).

Thus every word in the declared contact alphabet is a bijection preserving
the complete account, sum and labelled residue vector. The reverse word
with every contact repeated four times is its inverse.

## 2. What is required of the 261-contact read

The block construction in `CONTRACT.md` gives an exact primitive definition
of \(R\). The composition argument needs these boundary facts only on the
read states reached by the ten admitted runs:

1. \(R\) restores the presented source, receiver clock, both zero guards
   and helper \(w\).
2. If the presented source is not \(Y_0\), \(R\) preserves both sets and
   the selector, including occupied sets.
3. At \(Y_0\), selection A or B with that set fresh records the receiver
   phase \(b\) in pair \(p=-b\pmod5\), changing precisely that pair's
   phase from zero to one. The other set is preserved even when occupied.
4. At \(Y_0\) with selection S, both occupied sets are preserved.
5. At \(Y_0\) the selector advances A to B to S to A; otherwise it stays.

The public exact replay must establish the complete state at all 200 read
boundaries, as well as all 100 macrostep boundaries. This finite statement
does not assume a universal read theorem on arbitrary controller or bank
states. In particular, a fresh-only test would not discharge occupied
continuation. The finite proof obligation includes the second read's
temporarily shifted source phase, not just the free macrostep phase.

The helper commutator explains the selection mechanism. With controls
\(g,c\in\{0,u\}\) and helper \(w\),
\(E_c=A_0B_cA_0^4B_c^4\) fixes the three inactive preparations, while
\((g,c,h)=(u,u,w)\) maps to \((u,0,2)\).
The following contact with the zero sampling gate opens it in this last
case. The enclosing inverses restore the controls after the scan. Likewise
the declared controlled swaps give the selector cycle. These identities
describe finite prepared states, not a Boolean value assigned to \(g\)
at every internal contact. The public claim remains tied to the complete
primitive replay and exact boundary states.

## 3. Source evolution and event positions

The source orbit has \(F(Y_a)=Y_{a+1}\), with nine distinct states, and
\(T(X_b)=X_{b+1}\), with five distinct phases. The finite orbit assertions
are included in the exact replay. At a step starting in phases \((a,b)\),
the first read sees \(a\), and the second, after \(F^{-1}\), sees \(a-1\).
Each restores what it is presented. The next \(F\) restores \(a\), and
the final \(FT\) advances the two phases. Therefore

\[
(a,b)\longmapsto(a+1\bmod9,b+1\bmod5)
\]

at macrostep boundaries. The two read events are respectively \(a=0\)
and \(a=1\); they are disjoint. The positive inverse implementation costs
eight contacts, giving

\[
|S|=261+8+261+2+2+1=535.
\]

For initial \((n,k)\), the phases at step \(t\) are
\((n+t\bmod9,k+t\bmod5)\). On \(t=0,\ldots,9\), the events are
\((0,1,9)\) for \(n=0\), and \((0,8,9)\) for \(n=1\).
There are exactly three events. They select A, B and S in that order.

## 4. Retention and funded continuation

At the first event A is fresh and B remains fresh. All intervening inactive
reads preserve occupied A. At the second event B is fresh and A is
preserved. Subsequent inactive reads preserve both sets; the third active
read uses S and preserves both. No fourth active read occurs before the
common end. The interposed \(F,F^{-1},T\) touch neither archive.

Induction over these read boundaries proves retention at every declared
checkpoint, subject to the finite local facts in section 2. It also proves
readiness for the second acquisition: the read core is restored, B is
fresh, and the selector points to B while A remains stored. No bank is
erased or discarded. This is finite stock-funded reuse.

After ten steps the source is \(Y_{n+10\bmod9}\), the receiver clock is
\(X_k\), the selector has cycled back to A, the guards are zero and the
helper is \(w\). The two exact record states supply the remaining twenty
coordinates. This proves the complete final-state formula, contingent on
the explicitly discharged finite read facts, rather than an unspecified
environmental disposal.

## 5. The ordered records separate all ten inputs

Both first events occur at \(t=0\), hence \(p_A=-k\pmod5\). The second
event occurs at \(\Delta_n\), equal to 1 or 8, hence
\(p_B=-(k+\Delta_n)\pmod5\). Their difference is 1 or 3 modulo five.
Those residues distinguish \(n\), and \(k=-p_A\) then distinguishes
the remaining phase. Thus the ordered output is injective on the full
Cartesian family of ten inputs.

For each of the five first-record labels, the possible second labels are
\(p_A-1\) and \(p_A-3\). They are distinct. This proves ten joint
outputs and two alternatives per first output without a probability
measure. Neither individual five-valued record is injective on ten inputs.
The claim about information added by the second record is this explicit
finite distinction, not a measure-dependent entropy statement.

Every input and output has the same labelled residue vector, by section 1
and the preparation formula. Because \(\rho\equiv1\pmod{1-j}\), changing
a recorded pair's phase cannot change that vector. This locates all record
distinctions inside a single fixed residue fibre and respects the declared
capacity boundary.

## 6. Primitive timing

The first read's initial contact is 1 and its completion is 261; the
second's are 270 and 530. Add \(535t\) to obtain global performed-contact
ordinals. Therefore the first two onsets are \((1,805)\) and
\((270,4281)\), and their completion pairs are \((261,1065)\) and
\((530,4541)\). The differences are respectively 804 and 4011.

In general the completion difference is
\(535\Delta+\epsilon_2-\epsilon_1\), where \(\epsilon_i\) is 261 or
530. The clock counts its free phase increments modulo five; it does not
count every primitive contact. Changing the timing convention from onset
to completion adds 260 to both endpoints and therefore leaves these two
elapsed counts unchanged.

The onset predicate is restricted to the designated first contact of each
read. Later internal transitions of \(g\) do not create additional
events. This restriction is part of the original timing definition, not
a post-result selection of convenient transitions.

## 7. Exact finite closure and limits

The public replay must enumerate every member of \(I\), apply the same
literal word ten times, check the complete boundary states, event schedule,
two records, invariants, normative word and full inverse. A single exact
mismatch falsifies this contract; there is no tolerance or excluded input.
Passing it discharges the finite reachable-state obligations used above.
The eventual result record must identify the pinned code, output and
architecture evidence.

This establishes a candidate for one finite common-apparatus contract.
It does not prove unrestricted read behavior, arbitrary arrival streams,
unbounded reuse, a physical implementation, or a Canon status transition.
The source and clock are included deterministic input registers. Their
separate preparation is not an unmodelled external resource.
