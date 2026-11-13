<!-- SPDX-License-Identifier: Apache-2.0 -->

# Co-located loaded writer: frozen exact audit

NON-CANONICAL / L1 / incubation. No authority. Candidate-T for written
conditional proofs; candidate-C for finite local computations. Owner:
A. M. Thorn / ChatGPT-colocated-loaded-writer-20261108. Reservation #1954.

PUBLIC-source basis: main d4d363722f052141a4ce65e9da39f11a74b43b95,
ACTIVE Public Canon v109. This successor does not alter #1953 or #1947.
Its carrier differs explicitly from the previous uncharged-archive apparatus.
Freeze this file and both checker sources in local Git before execution.
This is not a formal public probe or a two-architecture gate.

## 1. Equation

O=Z[j], 1+j+j^2+j^3+j^4=0; rho=j^2, J=1+rho,
phi=-j^2-j^3. Use the four integral coefficients in (1,j,j^2,j^3).
For v with coefficients a_k,

    Q(v) = (5 sum a_k^2 - (sum a_k)^2)/2,
    h(v) = v conjugate(v).

Ordinary C(a,b) refuses if a-b is not in 2O. Otherwise t=(a-b)/2,
c=(a+b)/2 and (a',b')=(c+rho*t,c-rho*t). Refusal is identity.
All contacts have inverse C^4, including refused and diagonal cases.

There are two vertices A,B and one oriented edge with divergence (-F,F).
Slot 0, denoted x, is charged at A; every other actual slot v is charged at B.
Each B slot has its own fixed uncharged reference e_v=0. There is no other
charged background. Initial total slot sum is zero and F=-x=sum_B v.
The complete declared account and its Hermitian version are

    E = Q(x) + sum_B [Q(v)+Q(e_v)+Q(v-e_v)] + Q(F),
    H = h(x) + sum_B [h(v)+h(e_v)+h(v-e_v)] + h(F).

For a contact involving slot0 and v, use the original loaded rule

    d=(2v-x-e_v+F)/4; refuse iff d is not integral;
    i=(rho-1)d; x'=x-i; v'=v+i; F'=F+i.

For two B slots use ordinary C and leave F fixed. This is an explicitly
supplied co-located interaction inventory. It is not derived uniquely from J.
On F=-x and e_v=0 the first rule equals ordinary C(x,v), and E=2 sum Q.
The field must be advanced by the actual current, not reset from x afterwards.

## 2. Code and prospective execution

verify.py implements the actual loaded rule, ordinary rule, exact accounts,
Gauss checks, residue checks and the words below. break.py is written in a
separate agent from this document without reading verify.py. It must be frozen
before execution or output comparison. Code may be statically checked first.
Both use Python standard library only, no floating point or imported predecessor
verifier. Record first commands, exit codes, empty/nonempty stderr, exact stdout,
source hashes, environment and Git pin. Do not replace a failed first run.
Independent code construction is not a second architecture.

## 3. Carrier, inputs and fixed words

### A. Two-contact record

Use five actual slots (x,y,h,z,k), four zero references and one field.
Initial state (-d,d,-3-rho,0,3+rho), F=d. Word: C(0,2), C(0,3).
Primary inputs d=J and d=phi. Also audit d=J*rho^r for all r=0,...,4:
this same-residue refinement was derived analytically before computation.
Do not count duplicate d=J twice. Full account predicted80 for all six inputs.

For d=J predict endpoint (-J,J,-2J,rho-1,3+rho), F=J, two admissions.
For the other five inputs predict unchanged endpoint, zero admissions.
The whole source pair and field return in every case. The archive triple
has common neutral initial state and ends neutral. Its record slot z has
Q=5 for J and Q=0 otherwise. Inverse is four C(0,3), then four C(0,2).

### B. Root-pair record

Use six actual slots, five zero references and one field. Pair i occupies
(2i,2i+1)=(j^u,-j^u) with i=0,1,2. Set F=-slot0.
For P_ij define chronological A=C(2i,2i+1),
K=C(2i,2j+1) C(2i+1,2j), and

    P_ij = A K A K^2 A K^3 A K^4 A.

This is the credited 25-attempt word of #1930 JOINT-CONSTRUCTION.md at
f975ee0056d85583623bfc27cb41a18dda18907f, with the donor slot order reversed
by edge naming only. No physical slot swap or phase-conditioned schedule.
It has phase action (u,v)->(v,2v-u) modulo5.

    W = P_01 P_01 P_02 P_02 P_12 P_12.

W has150 elementary attempts. On arbitrary phase triples (r,s,t), predict

    (r',s',t') = (r+3s+2t, r+4s+t, 2s+4t) modulo5.

Audit all125 triples and their literal inverses (reverse each contact and
repeat it four times,600 attempts). In particular all25 (r,s,s) inputs must
give (r,r,s). Thus source pair, reference pair and field return, while the
memory pair takes the original source phase. Full account24 for every input.
The common-reference family is the positive writer claim; arbitrary occupied
triples are matrix/inverse controls, not a claim of source restoration.

For each fixed s, all five initial memory/reference preparations are identical
as r varies. The output r=s coincides with blank and supplies no completion
flag. A prepared source phase is being recorded, not a path determinant.

## 4. Systematics and controls

At every elementary attempt, forward and inverse, check exact Gauss at BOTH
vertices, complete E and H, all slot residues modulo1-j (sum coefficients
modulo5), integrality, and total charge. Compare the loaded implementation
against a direct ordinary-contact shadow with its own field-current update.
Count accepted diagonal attempts separately from state-changing attempts.
Record first bad cut on any failure. Report field changes and return without
calling them source work or physical propagation.

Primary checker audits all256 choices x,v,e,F with each coordinate in
{0,1,j,rho} for the general loaded rule, checking its complete three-slot
account, inverse, integrality and Gauss residual preservation, including
refusals. This finite algebra audit is not a universal proof.

Read the archive using its current coordinates and Q for the two-contact
case, or current root phase for the pair case. Do not claim a paid receiver
has been appended. The two-contact archive redistributes account; the root
family keeps every individual actual-slot Q constant. The prepared references,
zero references, potential terms, field and fixed calendar are all declared.

## 5. Failure thresholds

Zero tolerance. Any failure of a predicted primary endpoint, inverse,
admission table, account, residue, shadow equality, source/reference/field
return on the stated writer family, or any nonzero Gauss residual at any cut
falsifies that construction as stated. Preserve the exact failing input and
cut. A valid first result is not retroactively rewritten under this pin.
The full125 family is only required to obey its displayed matrix, not the
writer restoration identities outside t=s. Checker disagreement is STOP.

## 6. Action layer and limits

L1 only, explicitly NON-CANONICAL. Proof at most candidate-T, finite audit
candidate-C, one x86_64 lane. This is a new two-vertex co-located carrier with
the stated existing contact formula and local contacts. It does not embed
the full27-site apparatus, preserve the earlier one-charge-per-vertex premise,
derive this topology from J, or establish autonomous/native-U scheduling.
No P27/P35 determinant/history acquisition, energy-to-phase law, physical
occurrence, Born law, alpha, action quantum, minimal account or physical
arbitrary-state copying follows. The inverse erases the new records.

No Canon, Registry, Frontier, gate, workflow, release or predecessor file edits.
