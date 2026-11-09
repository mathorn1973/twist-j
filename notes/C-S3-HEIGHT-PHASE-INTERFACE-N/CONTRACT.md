# S3 interface and conditional assembly contract

NON-CANONICAL / L1. Definitions and exposed analytical targets, 2026-11-08.
Base: a8482d068156c8f42a390a81e817566b1c5abeda, active Public Canon v109.
This is a new interface contract, not an amendment to a sealed predecessor.

## 1. Arithmetic and law

O=Z[j], Phi_5(j)=0, rho=j^2, u=1-j, B=1-rho,
J=1+rho, X=1+j-2j^3, phi=-j^2-j^3 (phi^2=phi+1).
Here u is the pole-height coordinate; the old stopwatch's u is our B.
Write h(z)=z conjugate(z) and
Q(z)=(5 sum(z_i^2)-(sum z_i)^2)/2 in the basis 1,j,j^2,j^3.
For h(z)=a+b phi, Q(z)=2a+b.

C(a,b) refuses as identity if a-b is not in 2O; otherwise it sends
(a,b) to (s+rho d,s-rho d), s=(a+b)/2,d=(a-b)/2.
C^5=id and C^-1=C^4. Whole-slot SWAP is a separately supplied involution.
A word is fixed in advance and acts chronologically left to right.
Only the contact's parity guard depends on data. No externally chosen edge,
input-conditioned word, postselection, reassignment or reset is admitted.

Every primitive preserves the full-state sum, summed h, and summed Q. Contacts preserve each
labelled residue epsilon(z)=sum z_i modulo5. SWAP transports these residues
by its fixed permutation; it never creates a new residue.

## 2. First finite compiler class

Five heights t=-2,-1,0,1,2 have already prepared six-slot states
G_t=(u+tB,u-tB,0,0,X,2).
The old 322-contact loader is an unchanged possible upstream preparation,
not a word reexecuted or revalidated here.

A acts on eight ZERO-BASED slots:
0,1 height pair; 2,3 zero helpers; 4,5 old helpers X,2;
6,7 a single common clock seed J,-J.
Every slot other than0,1 has one common preparation for all five t.
The target is EXACTLY
A(G_t,J,-J)=(R_t,rho^(t+2)J,-rho^(t+2)J),
where R_t consists of six explicitly retained ring coordinates.
No condition forces R_t=G_t. A successful certificate must print all R_t,
admission traces and the same literal word for all five inputs.

Input account is39+10t^2; clock output account is6, hence the complete
remainder must carry33+10t^2. Its sum is2u+X+2.
Residues initially are(0,0,0,0,0,2,2,3).
The target clock is already on ports with the required residues.
No five-phase bank of preencoded target answers is provided.

The broad analytical interface permits a fixed finite common stock Z on h
additional slots, with its exact coordinates declared before a search.
The FIRST search fixes h=0 and contacts only. SWAP, more stock, extra gates
or enlarged caps require a separately identified successor experiment.
The source phase n is NOT inferred from t. It is independently supplied as
Y_n=F^n(0,2,0), F=C01 C12, n in{0,1}; A does not touch it.
The full input family is the Cartesian product of these two source states
and the five heights. Its size is10, with no probability claim.

## 3. Immutable downstream interface

The existing 31-slot stopwatch takes (Y_n,X_r,aux), where
X_r=(rho^r J,-rho^r J).
Its26 auxiliaries are common, Q=68; the total is82, sum4.
Use exactly the existing WORD535.txt, SHA256
ca6bdd7a9b43e329cbc3630f26e32125b1d16a9872b9563e57733f5c408c916b.
Its5350-contact run W writes two working records.
The registered workbank-reuse construction U_i=W K_A K_B W^-1 uses26870
contacts, copies both records to two fresh ten-slot archive banks and returns
the entire31-slot work core, including Y_n and X_r, to its preparation.
The archive labels are p_A=-r, p_B=-(r+Delta_n), Delta_0=1,Delta_1=8.
They decode r and n on this exact input family. No arbitrary interval is read.

A typed compiler certificate must literally reach this preparation; similarity
of scalar accounts or renamed phase labels is insufficient.

## 4. Conditional finite-k assembly

For every k>=1 fixed before construction and every sequence(n_i,t_i) from the
ten-input family, use one common fixed program built from
A U_i A^-1, i=1,...,k, with five fixed swaps between stages.
A and its inverse never touch the source, old controls, working banks or
permanent archives. The swaps exchange the three Y slots and two height
slots with the next raw five-slot cartridge. The four G-tail slots, clock
seed and optional translator stock are shared and restored at every cycle end.
Spent inputs are parked intact in the vacated cartridges.

A complete address layout is:
0..30 old apparatus, including source0..2, clock3..4, oldaux5..30;
31..36 G_t, with variable height31,32 and commontail33..36;
37..36+h optional commonstock;
37+h..36+h+20k permanent archives in stage order;
37+h+20k..N-1 queued five-slot cartridges, k-1 of them.
A's eight local ports map to(31,32,33,34,35,36,3,4).
Additional local ports map in order to37..36+h.
Between stage i and i+1 swap(0,1,2,31,32) with the five addresses of
cartridge i, always in the displayed order. The addresses never depend on data.

N=32+h+25k, with32+h+20k common auxiliary slots and5k input slots.
Let E_Z=sum Q(Z_l), H_Z=sum h(Z_l), Sigma_Z=sum Z_l. Then
E_total=97+E_Z+78k+10 sum_i t_i^2,
H_total=37+23phi+H_Z+k(30+18phi)+(4+2phi)sum_i t_i^2,
Sigma_total=X+4+Sigma_Z+k(2+2u).
The common auxiliary account is97+E_Z+60k.
Fresh archives retain their account60 per stage; consumed freshness is
not a disappearing energy charge.

If A contains c contacts and s swaps, the forward program contains
k(26870+5c) contacts and2ks+5(k-1) swaps.
Its unreduced literal inverse has four times the forward contact count
and the same number of swaps. It removes the archives.
All earlier archives are untouched after their stage completes.

This is an implication CONDITIONAL ON A, not an existence theorem for A,
and not a single finite machine retaining unlimited history.

## 5. Failure and scope

Any wrong clock coefficient, changed downstream word, missing remainder,
non-common stock, incorrect inverse, unpaid account or undeclared operation
invalidates a claimed compiler. Complete assembly additionally requires all
per-cut invariants and the actual archive/core endpoints.
A bounded search finding nothing is inconclusive outside its exact explored
prefix. It must not be called a proof that S3 is impossible.
S0-S1, physical preparation, autonomous timing, K1/K4/K6 identification,
native-U and a physical event law remain outside this S2-S8 construction.
