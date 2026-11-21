<!-- SPDX-License-Identifier: Apache-2.0 -->

# An exact writer on a co-located charged carrier

**NON-CANONICAL / L1 / conditional candidate-T. No Canon authority.**

Candidate C-COLOCATED-LOADED-WRITER-1, reservation #1954. This proof uses
the carrier and fixed words in the frozen PREREG.md. It asserts neither a
run result nor independent acceptance. All rings and accounts are exact.

## 1. Credited premises and the changed carrier

Let O=Z[j], rho=j^2, J=1+rho, phi=-j^2-j^3, and h(a)=a conjugate(a).
Write Q(a)=Tr(h(a))/2. The ordinary contact, loaded contact, and the
25-attempt phase word P are inherited from #1930 at public commit
`f975ee0056d85583623bfc27cb41a18dda18907f`, respectively PROOF.md and
[JOINT-CONSTRUCTION.md](https://github.com/mathorn1973/twist-j/blob/f975ee0056d85583623bfc27cb41a18dda18907f/notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N/JOINT-CONSTRUCTION.md).
The phase-word construction is credited, not claimed as new here.

There are two vertices and one oriented field edge with divergence (-F,F).
Exactly one actual slot x is charged at A. Every other actual slot v is
charged at B, including every archive and reference-pair slot. Each v has
a separate fixed uncharged reference e_v=0. Initially the actual-slot sum
is zero and F=-x=sum_B v. Thus both Gauss residuals are zero.

This explicitly changes the topology of #1953: its fixed-field argument
does not cover several active charged slots at the same vertex. The
present contact inventory and topology are supplied choices. The one-edge
account below is declared directly; no full 27-site field embedding or
free-field propagation is inferred from it.

## 2. Whole-alphabet lift and every-cut conservation

For an admitted ordinary contact let c=(a+b)/2 and t=(a-b)/2. Its outputs
are c+rho*t and c-rho*t. Since h(rho)=1,

    h(c+rho*t)+h(c-rho*t)=2h(c)+2h(t)=h(a)+h(b).

The sum a+b is unchanged. Admission persists because the new half
difference is rho*t. Therefore C^5=I and C^-1=C^4, also on refused
and diagonal inputs. Each coordinate increment is divisible by 1-j.

For an x-v contact the original loaded rule uses

    d=(2v-x-e_v+F)/4,  i=(rho-1)d,
    (x',v',F')=(x-i,v+i,F+i),  e_v'=e_v.

It refuses when d is not integral. On e_v=0 and F=-x, d=(v-x)/2,
so its admission and outputs are exactly those of ordinary C(x,v).
The actual current update gives F'=-(x-i)=-x'; this is not a field reset.
Also sum_B v'=sum_B v+i=F+i=F'. Both Gauss residuals stay zero.
For a B-B contact use ordinary C and leave F fixed. It preserves the
total charge at B, so again preserves both residuals.

For completeness, the inherited loaded account is conserved before
restricting to this slice. Put B(a,b)=a conjugate(b)+b conjugate(a).
The change of h(x)+h(v)+h(e_v)+h(v-e_v)+h(F) is

    4h(i)+B(-x+2v-e_v+F,i)
      =4[h(i)+B(d,i)]=4[h(d+i)-h(d)]=0,

because d+i=rho*d. Its new numerator is 4(d+i), so admission persists
and four further loaded contacts give the inverse. A refusal is identity.

The complete declared Hermitian account is

    H=h(x)+sum_B[h(v)+h(e_v)+h(v-e_v)]+h(F).

On the invariant slice it equals 2 sum_all h(v), and its trace account
E equals 2 sum_all Q(v). Thus every contact in the entire ordinary alphabet
has an exact loaded realization preserving H, E, total charge, all slot
residues and Gauss. The same proof applies at every primitive inverse cut.
Zero references stay explicit and fixed. There is no uncounted work bank.

## 3. A two-contact retained record

Use actual slots (x,y,h,z,k)=(-d,d,-3-rho,0,3+rho), with F=d.
Here h is a slot name, distinct from the quadratic function h(a).
The fixed chronological word is C(0,2), C(0,3).

For d=J, the first contact has half difference 1 and gives

    x=-2, h=-2J, F=2.

The second has half difference -1 and gives x=-J, z=rho-1, F=J.
Hence the endpoint is (-J,J,-2J,rho-1,3+rho). The whole source pair
and field return; the initially common neutral archive remains neutral.
Its current record coordinate has Q(rho-1)=5.

For d=phi or J*rho^r with r=1,2,3,4, the first contact refuses. Its
admission condition is d=J modulo 2O. The five J*rho^r classes are
distinct: J is a unit and rho has order five modulo 2O. Moreover
phi-J=-1-2rho-j^3 is nonzero modulo 2O. The second contact then also
refuses, since d is a unit and therefore is not divisible by 2. These
five inputs remain unchanged and have record z=0.

For all six distinct inputs Q(d)=3 and Q(3+rho)=17. Thus the initial
actual-slot account is 2*3+2*17=40 and E=80. For the written endpoint,
the archive accounts are 12,5,17, still summing to 34. The record is a
redistribution of already counted account. Four C(0,3), then four C(0,2)
restore the complete state by the whole-alphabet inverse proved above.

## 4. A source-preserving five-phase record

Each of three actual pairs has canonical order (j^u,-j^u). In P_ij the
source pair i has this order and the donor pair j is addressed in reverse
order by the edge names; no physical swap is performed. With

    A=C(2i,2i+1), K=C(2i,2j+1) C(2i+1,2j),
    P_ij=A K A K^2 A K^3 A K^4 A,

the credited phase action is (u,v)->(v,2v-u) modulo five. Its proof uses
the actual contact guard: K admits exactly when the two phases agree;
A increases the source phase by two. No external phase test selects a word.
Consequently P_ij^2 maps (u,v) to (-u+2v,-2u+3v).

Compose W=P_01^2 P_02^2 P_12^2 chronologically. Direct substitution gives

    (r,s,t) -> (r+3s+2t, r+4s+t, 2s+4t) modulo five.

This matrix has determinant one. On the prepared writer family t=s,

    (r,s,s) -> (r,r,s).

The whole source pair and reference pair return, and the memory pair
now carries the original source phase. For fixed s its initial memory
and reference are identical for all five source inputs. Since slot0
returns, its actual current-driven field F returns too. Every actual slot
remains a root unit during the word, so E=2*(6*2)=24 at every cut.
W has 150 attempts. Its literal inverse reverses their order and replaces
each by four contacts, giving 600 attempts and erasing the new record.
The displayed matrix applies to all 125 triples; source restoration is
asserted only on t=s. No arbitrary-state copying claim is made.

## 5. Exact boundary of the result

The output r=s is identical to the blank; the writer has no separate
completion flag. A prepared source state is recorded, not its preceding
history or the P27/P35 determinant. Admission histories may differ across
inputs; this piecewise contact map is not a global linear quantum copier.
Reading means inspecting the retained coordinates in this proof. No paid
receiver, native-U calendar, physical occurrence, action scale or alpha
has been derived. Finite audits and their first-run outcomes are separate
candidate-C evidence and cannot enlarge these conditional claims.
