<!-- SPDX-License-Identifier: Apache-2.0 -->

# A balanced contact record acquired during the two source paths

**NON-CANONICAL / L1 / conditional candidate-T. No Canon authority.**

This is the proof for experiment B of the frozen PREREG.md, reservation
#1955. It does not assert a computation result. The paid root-pair reader
in experiment A is a separate apparatus and is not silently appended here.

## 1. Premises and exact account conventions

Work in O=Z[j], with rho=j^2, J=1+rho, Jinv=-j-j^2 and
phi=-j^2-j^3. Put h(v)=v conjugate(v) and Q(v)=Tr_(K/Q)(h(v))/2.
The original source word, source closure and path identities are credited
to [#1923 CONTACT.md](https://github.com/mathorn1973/twist-j/blob/d4d363722f052141a4ce65e9da39f11a74b43b95/notes/C-COMMON-COUNTER-PATH-PHASE-N/CONTACT.md).
The loaded contact is inherited from
[#1930 PROOF.md](https://github.com/mathorn1973/twist-j/blob/f975ee0056d85583623bfc27cb41a18dda18907f/notes/C-LOADED-CURRENT-WORK-PHASE-COMPATIBILITY-N/PROOF.md).
The co-located realization is the explicitly supplied carrier of
[candidate #1954](https://github.com/mathorn1973/twist-j/issues/1954),
not the earlier separate-edge continuity construction.

For each admitted ordinary contact define t=(a-b)/2 and charge its path
ledger by h(t); charge zero on refusal. H_path denotes the sum over ALL
source and recorder contacts. It is distinct from the conserved state
account H_account and its trace account E.

For H_path=A+Bphi, its trace account is 2A+B. Thus the preregistration's
shorthand `trace(H_path)=150` means Tr_(K/Q)(H_path)/2=150, equivalently
Tr_(Q(phi)/Q)(H_path)=150. The literal full K-trace is300. This explicit
normalization preserves the frozen numerical trace-account prediction.
If reporting 2H_path, it is the separately labelled doubled ledger from
the preregistration, not a derived physical action normalization.

## 2. Every-cut loaded realization

The actual source slots are

    I1=(B,-B,u,u,X,2),
    B=1-rho, u=1-j, X=1+j-2j^3,
    S=sum I1=5-j-2j^3.

Append the untouched actual coordinate -S and the two neutral recorder
triples specified below. There are13 actual charged coordinates. Slot0=x
is at vertex A and the remaining12 are at vertex B, each with its own
fixed zero reference e_v. One oriented edge has divergence(-F,F).
Initially the actual sum is zero and F=-x=sum_B v.

The loaded x-v contact has

    d=(2v-x-e_v+F)/4=(v-x)/2,
    i=(rho-1)d,
    (x',v',F')=(x-i,v+i,F+i).

It therefore has exactly the ordinary-contact guard and source action.
The actual current update gives F'=-x' and sum_B v'=F'. An ordinary
B-B contact preserves the B charge sum and leaves F unchanged. Hence
both Gauss residuals remain zero after every elementary attempt.

The complete accounts on this invariant slice are

    H_account=h(x)+h(F)+sum_B[h(v)+h(0)+h(v-0)]
             =2 sum_actual h(v),
    E=2 sum_actual Q(v).

An admitted ordinary contact preserves its pair sum and h-sum because
its relative coordinate t is replaced by rho*t and h(rho)=1. Refusals
are identities. Consequently both complete accounts are preserved by
every primitive in the source words and the recorder. Every increment
is divisible by1-j, so all actual-slot and field residues are preserved.
Admission persists along powers of one contact, giving C^5=I and the
literal inverse C^4, including refused and diagonal states. The same
Gauss and account argument applies to every inverse cut.

## 3. The common four-contact port

Set

    a0=B, a1=B*rho^4,
    c_k=a_k/J, m_k=a_k+2c_k,
    recorder triple_k=(m_k,0,-m_k).

The helper m_k is the coordinate named h_k in PREREG.md. The two triples
occupy slots(7,8,9) and(10,11,12). Their initial states are identical in
both path experiments. Execute the same fixed word

    T=C(0,7) C(0,8) C(0,10) C(0,11).

For one matching block put x=a, c=a/J, m=a+2c, z=0. Its first ordinary
half difference is -c. Since Jc=a and (1-rho)c=2c-a, the two steps are

    (x,m,z,F)=(a,a+2c,0,-a)
       -> (2c,2a,0,-2c)
       -> (a,2a,(1-rho)c,-a).

The second half difference is c. Both are integral, so both contacts
admit. The source coordinate and field return after the block, while
the record becomes delta=(1-rho)c. The companion -m is untouched.
The final triple remains neutral because 2a+delta=m.

Modulo2O, B is congruent to the unit J. The element rho has order five
there: rho^5=1, rho is not1, and five is prime. Thus a0 and a1 are
distinct nonzero unit classes. Also m_k=a_k modulo2O. On the other
source phase the first contact refuses, and the contact against zero
refuses too. Accordingly exactly one block acts on either frozen input.
No externally evaluated phase test or path label enters T.

The exact norms are

    c0=(-1,-2,-2,0), m0=(-1,-4,-5,0),
    h(c0)=3+4phi,
    h(m0)=18+19phi, Q(m0)=55,
    h(delta0)=10+15phi, Q(delta0)=35,
    delta1=rho^4*delta0.

Multiplication by rho^4 preserves each norm. In the active block the
helper's Q changes55->20 and the record's Q changes0->35. The companion
keeps55; each recorder triple therefore keeps total ordinary account110.
The actual source and field each pass through Q=5->40->5. Their transient
increase is paid by the helper and then released into the record under
the doubled complete account. No uncounted funding is introduced.

## 4. Insertion at source cut five

The first four attempts of both source words are C12. On the initially
balanced pair(B,-B), each multiplies its first coordinate by rho. P27's
fifth attempt is C35 and leaves that pair untouched; P35's fifth is C12
and closes it. Therefore the actual source at the common insertion cut is

    x=B*rho^4=a1 for P27,
    x=B=a0 for P35.

The recorder restores every original source coordinate and the field
before the next source attempt. Induction through the unchanged source
suffix then proves equality with the uninstrumented source at EVERY
source-attempt boundary. The source may change inside an active recorder
block; its actual field current maintains Gauss there. No enlarged cut
is used to conceal an intermediate violation.

The remaining source attempts never address the archive slots, so the
new record persists. The credited original source closure gives the
complete final source I1 and F=-B in both cases. Slot6=-S and both archive
companions stay unchanged. The final reading from current coordinates is

    (Q(slot8),Q(slot11))=(0,35) for P27,
    (Q(slot8),Q(slot11))=(35,0) for P35.

This differs from the common blank(0,0). Completion is distinguishable
within this frozen two-path family only. A different prefix phase could
leave both selectors refused; no unrestricted arrival detector is claimed.

## 5. Complete budgets, area, determinant and inverse

Direct cyclotomic identities give

    h(I1 summed by slots)=19+5phi, Q(I1)=43,
    h(S)=35+3phi, Q(S)=73.

Source plus neutralizing companion contributes54+8phi to the ordinary
h-sum. The two neutral recorder triples contribute4h(m0)=72+76phi.
Thus the complete Hermitian account is252+168phi and E=672 in both runs.
All13 actual slots,12 zero references and the field are included.

Both original padded source words have35 attempts, source area55+20phi,
and respectively27 and35 admissions, with no admitted diagonal contacts.
Exactly one recorder block contributes two nonzero half differences
with h(c_k)=3+4phi; the other two attempts refuse. Hence

    H_port=6+8phi,
    H_path=H_source+H_port=61+28phi

in BOTH complete39-attempt programs. The trace account is150, and the
separately defined doubled ledger is122+56phi. This equality includes
every recorder contribution; it is not inferred from conserved E.

The recorder adds two admissions. Original source determinants are
rho^27=j^4 and rho^35=1, while combined-word determinants are
rho^29=j^3 and rho^37=j^4. Their ratio remainsj^4. The norm records must
not be renamed as either pair of phase determinants.

Reversing all39 primitive attempts and replacing each by C^4 gives156
attempts. It restores every initial coordinate and removes the records,
with the every-cut invariants from section2. No permanent copy survives
complete reversal.

## 6. Frozen causal controls and boundary of the claim

With T omitted, the same full carrier has untouched blank archives and
the two source/field endpoints coincide. Its source area is55+20phi.
If T is instead delayed until after all35 source attempts, both sources
already equal I1. The same a0 selector then acts in both experiments,
yielding(35,0) for both. Its area contribution is again6+8phi, so the
delayed total remains61+28phi. Both controls have the same complete672
account, and their literal inverses obey the same primitive conservation.
These are all six preregistered path/timing cases.

More generally, any identical deterministic postprocessor given only the
common returned source/field and common fresh auxiliaries has identical
input in the two runs and must have identical output. The successful T
avoids that endpoint obstruction by coupling to an actually different
source coordinate while the paths are in progress.

The WHOLE source calendars differ; only their initial full state, recorder
preparation, inserted word and chosen source-counter cut are common. Cut5
and its two helpers were selected from known paths before this candidate's
computation. This is a retained selected-prefix history record at equal
complete account and equal declared path area, not a universal determinant
accumulator or a derivation of the proposed root-pair phases j^4 versus1.
The output coordinates and funding are real parts of the declared contact
apparatus, but no separate #1930 reader or physical calorimeter is installed
here. No native-U scheduling, autonomous selection, full27-site embedding,
physical action normalization, Born law, Planck scale or alpha follows.
