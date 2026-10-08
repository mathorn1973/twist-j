# Source transitions, energy selection and a hidden contact context

**NON-CANONICAL / NO AUTHORITY. Conditional candidate-T, L1.**
This analytical continuation of the synthesis starts from the author's
source-transition test. It adds a complete one-parameter consistency
criterion and an explicit same-output ambiguity between the two completed
contacts. No scientific program was run. Ordinary affine-equation and
factorization arguments are not claimed as newly discovered mathematics.

The underlying notes were first published at
`7ea9b35e725368f616d2f1cd82cdb251b26f2187`. Their fixed carrier and
energies remain premises. In particular the reference label H1 below
does not assume that c=1 is the physical answer.

## 1. A complete test for an independently specified transition family

Fix a complete carrier X, a nonempty allowed parameter domain C subset R,
two already specified functions H1, Pi on X, and a set Q subset X times X
of admitted transitions. The complete apparatus and helpers belong to X.
The relation Q may include multiple prepared contexts or branches; it
need not be the graph of a single bijection. It must be fixed independently
of the subsequent conservation test, including refused and occupied-input
branches and every claimed preparation restriction.
Neither Q nor its preparation domain may vary with c in this theorem.

For q=(x,y) put

```text
a_q = H1(y)-H1(x),    b_q = Pi(y)-Pi(x),
Hc = H1+(c-1)Pi,
C_adm = {c in C : a_q+(c-1)b_q=0 for every q in Q}.          (S1)
```

Here Pi is the total number of odd stocks when applying the reserve
family of READOUT R5. Auxiliary costs and any interaction energy must be
included in H1. If they have a different c-dependence, S1 is not the
complete proposed family and must be replaced before testing it.

There are exactly the following possibilities.

1. If all b_q=0, then C_adm=C when all a_q=0, and C_adm is empty
   otherwise. This includes the vacuous empty transition family.
2. Otherwise choose any q0 with b_0 != 0. Set

```text
c_star = 1-a_0/b_0.
```

   Then C_adm={c_star} exactly when c_star belongs to C and

```text
a_q b_0 - a_0 b_q = 0 for every q in Q.                    (S2)
```

   If either condition fails, C_adm is empty. In particular b_q=0 in
   S2 forces a_q=0; zero-parity changes cannot be silently omitted.

**Proof.** A zero coefficient gives the constant equation a_q=0. Every
nonzero coefficient gives a unique root. Substituting the root from q0
into all other equations and multiplying by b_0 gives S2. Thus a single
nonzero-parity transition proposes one value, while the whole admitted
family decides whether that value survives. For the current nonnegative
reserve family C is [0,infinity), or the nonnegative integers if integral
reserve energies are also required. Those restrictions are separate from
the linear conservation equations.

An empty admissible set has a finite certificate using at most two
transitions: one has b=0,a!=0; one nonzero-b transition proposes a root
outside C; or two nonzero-b transitions propose different roots. In the
last case their determinant a_1 b_2-a_2 b_1 is nonzero. This is an
existence bound on a falsifying certificate, not a terminating search
algorithm for an unspecified infinite Q. Passing a finite sample does
not prove the positive universal statement S2.

The result is independent of the chosen reference member. For any c0,
write Hc=Hc0+(c-c0)Pi and a_q^(c0)=a_q+(c0-1)b_q. The inferred value
c0-a_0^(c0)/b_0 equals 1-a_0/b_0, and the determinants in S2 are
unchanged. Choosing H1 as coordinates therefore does not impose its
conservation on the source law.

In contrast, defining a source stock decrement from a previously chosen
H1 price makes a_q=0 by construction. Such a construction can restrict
the remaining profiles to c=1 when b_q!=0, but it is not independent
evidence for the construction's selected energy or for that source law.

## 2. Full accounts and time resolution cannot be discarded

For an additive system/helper account without an omitted interaction term,

```text
a_total=a_system+a_helper,    b_total=b_system+b_helper.
```

S1 tests these total quantities. For example a system parity change can
be cancelled by the helper's opposite parity change. Dropping that helper
would create a false parameter selection. If the helper returns to the
same complete state, both of its differences vanish. The weaker condition
of equal initial and final helper Pi cancels only b_helper, not its
reference-energy contribution. A changing shared interaction term must
still be included even if the helper's own coordinates return.

For a composed trajectory x0,...,xm, both a and b telescope. A complete
cycle xm=x0 consequently gives sum a=sum b=0 for every family member,
whether or not any individual transition conserves energy. Its net
balance alone cannot select c. Likewise conservation at macrostep
boundaries need not imply conservation at every proposed internal step:
nonzero defects may cancel. The test must use the transitions at the time
resolution actually asserted by the physical conservation claim.

This does not weaken the old-layer result in READOUT R5. There every
pre/post layer separately preserves each tested Hc, so those particular
layers cannot compensate the defect of an inserted new contact.

## 3. Reading a family of laws requires a joint fibre condition

Let Tk:X->X be known bijections labelled by a contact context k in K.
Suppose that the final recorded interface is R(y), omitting k. To read
the last change of the fixed receiver energy E1 define

```text
W(y,k)=E1(y)-E1(Tk^(-1)y).
```

A common exact reader w with w(R(y))=W(y,k) exists if and only if

```text
R(y)=R(z)  implies  W(y,k)=W(z,l)
for every admitted pair (y,k),(z,l).                       (S3)
```

This is READOUT R1 applied to the joint carrier of output and context.
Necessity follows from equality of the argument of w. Sufficiency defines
w on each actually occupied interface fibre by its common W value.
If the preparation restricts the possible pairs, S3 is tested only on
that declared joint domain. A separate correct decoder for every k does
not prove the cross-context equalities in S3.

## 4. One identical final cell state, two different last energy transfers

An explicit counterexample to S3 uses the existing completed contacts,
without constructing a new motion law or changing the energy.
Let T be the old two-cell bijection of READOUT R3, and let

```text
Td = (Wd on the receiver) T,
Ta = (Wa on the receiver) T.
```

Both are complete bijections preserving Hhat_1. Fix the receiver c_star
to be the common input of CONTACT section 8:

```text
m=R, b=(5v,0,-5v), v=(1,0,0,0),
E=(2,2,1,-4), M=(0,0), r=81, E1(c_star)=424.
```

Fix ONE final two-cell state y_star: receiver c_star, source with zero
matter triple ZM and all other source coordinates zero, eta=0, p=0.
Its full old-carrier energy including the pointer is Hhat_1=425.
All these are allowed product-carrier coordinates.

Since Wd and Wa are involutions, their inverse images of c_star are
exactly the two already proved outputs in CONTACT section 8. Their
stocks are respectively 76 and 1. For j=d,a set xj=Tj^(-1)y_star.
These are allowed full inputs; no successful-only branch, empty-memory
replacement or extra preparation is assumed. READOUT R6 gives

```text
Delta E1 along xd -> y_star = r(Wd c_star)-0 = 76,
Delta E1 along xa -> y_star = r(Wa c_star)-0 = 1.           (S4)
```

The complete balance can also be read directly. In T^(-1), source G and F
fix the zero nonstock coordinates. Undoing the stock swaps leaves the
source stock 76 or 1 and the input link zero. Receiver energy is then
fixed by its conserved total through G and F:

| Quantity | History using Td | History using Ta |
|---|---:|---:|
| Initial source energy | 76 | 1 |
| Initial receiver energy | 348 | 423 |
| Initial link energy | 0 | 0 |
| Pointer energy | 1 | 1 |
| Initial total Hhat_1 | 425 | 425 |
| Final receiver energy | 424 | 424 |
| Last receiver change | 76 | 1 |

In fact both predecessor receivers have matter AM and charged registers
(0,5v,-5v). Their (E,M,r) tuples are respectively
(-1,0,1,-4;0,0;10) and (-4,2,2,-3;0,0;70). Their active field energies
are 3 and 18, so the AM funding guards are exactly
10+2-4*3=0 and 70+2-4*18=0. Forward G changes AM to R and leaves stock
zero. Thus e=0 and the input pointer is p=0 in both histories; there
is no hidden restriction from the recorded reaction or a refused branch.
These tuples are obtained by the same exact F and G inverses used in R6.

Thus even the ENTIRE final old two-cell state, and knowledge of its
total energy, cannot provide one law-independent exact last-transfer
reader on the union of these two histories. Receiver plus link is of
course insufficient on that union too. For a real-valued common estimate
v, max(|v-76|,|v-1|)>=75/2; exact recovery is impossible. This does not
contradict the known-law readout theorem, which fixes the contact first.

The histories have different initial cell states. Nor is y_star being
called the same complete physical apparatus state under both contexts.
If the choice of contact is stored in an additional context register,
the complete final states include that distinction.

Indeed, with a specified unchanged register k in {d,a}, define the single
controlled bijection

```text
T_controlled(x,k)=(Tk x,k).
```

Its inverse uses Tk^(-1). Taking the register's energy to be a fixed
constant preserves the selected account, and reading k with the old
receiver/link interface restores the corresponding exact decoder for
every state. At least two supplementary distinguishable values are
necessary for the ambiguous pair S4; this explicit context bit is
sufficient for the two-law family as an abstract code. Its physical
preparation, control implementation, readable record and energy cost
are additional premises. No global uniqueness of all contacts is required.

## 5. What the audited accepted sources actually supply

This audit uses Public Canon v100 at
`7d7f588c42422c2cf37b04d76ebc13ca55eb96dc`, whose authority tuple is in
SOURCES.md. It concerns the named sources below, not an exhaustive
impossibility claim about future laws or all integer encodings.

| Accepted source | Supplied law | Boundary for the present test |
|---|---|---|
| [Complete field-chain layers](../../canon/CANON.md#shared-proof-5-four-layers-occupied-contacts-cuts-and-full-projection) | G changes stocks by even integers; A,B swap whole occupied stocks; F changes no stock | Each primitive preserves Hhat_1, total Pi and each actual node charge. Thus a=b=0, and no member of this family is selected |
| [INTEGER-ENERGY-FUNDED-INVOLUTION](../../canon/CANON.md#integer-energy-funded-involution-t) | Given T and H0, set the resource change to minus H0(Ts)-H0(s), with full refusal branches | Energy and the unfunded law are premises; this is not an independently supplied stock change |
| [FIELD-GAUSS-CONTACT-MEMORY](../../canon/CANON.md#field-gauss-contact-memory-t) | Given actual charge transport and its current, update E by a closed flow minus that current | It supplies Gauss continuity and stored contact coordinates, not the matter law or energetic stock account |
| [CONTACT-RECORD](../../canon/CANON.md#contact-record-t), [RESIDUAL-STEP-RECORD](../../canon/CANON.md#residual-step-record-t) | Complete specified finite permutations and occupied-record continuation | Their F5 records and two-state bit are a different carrier. No map to this cell's nonnegative stocks or Hc account is supplied |

The field-chain conclusion also covers finite adaptive procedures built
only from its invariant-preserving primitives. On every branch each
operation preserves the same functions, so induction preserves them
regardless of data-dependent gate choices or the finite stopping time.
Extra control updates are allowed in this argument only when they also
preserve those functions on the declared complete carrier. A new coupling
that changes a node charge is outside the alphabet, not a counterexample
to this closure argument. The same applies to discarded helpers or
changed readout definitions.

Consequently this audited alphabet supplies neither an informative total
parity change nor the new contacts' actual charge motion. The other named
sources do not fill that carrier-and-law gap. This is a precise absence
of a supplied bridge within these sources, not a theorem that no broader
physical source transition can exist.

## 6. The next source claim is now falsifiable without preselecting c

A prospective source contribution must first give its complete carrier,
prepared context, full transition relation, state equality and accessible
readout. It must provide all field and stock changes from that law,
including helper and interaction accounts. S1 and S2 then decide which
members of the already declared family are conserved. A universal positive
claim needs a proof over the admitted domain; one or two actual transitions
can provide the finite negative certificates above.

Independence from the target energy is a source/provenance and physical
admission obligation, not a consequence of satisfying S1 or of publishing
a formula before evaluating it. In particular the canonical form
R(n,x)=L^n G0(ell_n(x)) permits a stipulated target L to be inserted into
an intertwining reader. Equality RU=LR alone does not select that L.
Likewise the abstract context register above does not derive a native
apparatus. The original native-U and phase boundaries in READOUT remain.

The present continuation proves the test and the cross-context obstruction.
It does not supply the missing independently admitted source transition.
