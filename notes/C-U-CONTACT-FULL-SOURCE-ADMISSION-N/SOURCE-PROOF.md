# Complete-source preservation in a conditional coherent contact lift

**PUBLIC, NON-CANONICAL. Unexecuted analytical quantum comparison; L1 only.**
Incubation reservation: [issue #1442][reservation].
Branch: `codex/v101-contact-full-source`.
Source base: `a18e65d3e43acc6cb1896296b8bd0fdecdad35a7`.
Original text: Apache-2.0. Draft date: 2026-10-10.

The Hilbert spaces, quantum channels and coherent lift below are additional
comparison assumptions. They are not derived from native U, J, or the classical
contact theorem. This note supplies neither physical admission nor a formal
execution record. Its argument was derived before reading another new author's
contact derivation. No scientific program was run or imported for this proof.

No-broadcasting and nondisturbing-information constraints are existing quantum
information mathematics: see Barnum, Caves, Fuchs, Jozsa and Schumacher,
*Noncommuting mixed states cannot be broadcast*, and Koashi and Imoto,
*What is Possible Without Disturbing Partially Known Quantum States?*
[Barnum et al.][barnum] [Koashi-Imoto][koashi]
The full-state no-imprinting statement needed here is proved directly in
section 7. No broader Koashi-Imoto decomposition theorem is asserted or used.

## 1. Three different source contracts

Let S be the new five-valued source and E the complete receiver. Distinguish:

1. **Classical nondemolition:** every basis state |s><s|, or every diagonal
   mixture in this basis, has its source marginal preserved.
2. **Complete-state preservation at a fixed preparation:** for one fixed
   receiver state rho_E, initially independent of S, the source output equals
   sigma_S for every density matrix sigma_S, including its coherences.
3. **All-input operator conservation:** the interaction preserves every source
   observable A tensor I as an operator on the entire joint carrier. This
   controls arbitrary receiver states and initial correlations as well.

Contract 1 does not imply 2 or 3. The receiver preparation in contract 2 is
the same for every unknown source input. A source-dependent ready state may
already contain the sought information and does not satisfy that contract.
When preservation is relative to a fixed known free source unitary Q, apply
Q dagger to the output before comparing. The no-imprinting conclusion below
is unchanged. Arbitrary input-dependent corrections are not admitted.

## 2. Exact classical contact and its phase-free coherent lift

The existing contact proof fixes v=(p1,p4,p1p,p4p,q,r) in F5^6 and

```text
x=p1-1, y=p1p-4, c=x+y, h=y-x,
C_s^f(v)=(p1,p4-f(x,y)s,p1p,p4p+f(x,y)s,q,r).
```

It leaves x,y and s unchanged, so C_s C_t=C_(s+t) and C_0=I. For the
normalized representative f=2h, every basis checkpoint with h!=0 has an
orbit of length five. More generally the exact criterion is f(x,y)!=0.
One must not replace it by h!=0 for every nonlinear member of the larger
family: those members may vanish off the supported SUM orbit. Every unit
member is nonzero on the occupied-SUM orbit c=+/-1,h=+/-2. [Contact proof][contact]

Adopt H_S=C^5 and H_E=ell^2(F5^6), with their indicated orthonormal bases.
Let V|v>=|C_1(v)> and define the phase-free comparison unitary

```text
V^5=I,
U = sum_(s=0)^4 |s><s| tensor V^s,
U dagger = sum_(s=0)^4 |s><s| tensor V^(-s).            (1)
```

This is a globally unitary contact. It is not a unitary realization of the
whole selected native evolution W_N, whose global injectivity fails in the
classical theorem. A quantum dilation of that full evolution is a separate
carrier and interface problem. Classical global invertibility of C_s alone
also gives no marginal-preservation theorem for a coherent source.

## 3. The source channel at one independent receiver preparation

Take an arbitrary source matrix sigma and one fixed receiver density matrix
rho, initially in the product sigma tensor rho. Direct multiplication gives

```text
U(sigma tensor rho)U dagger
 = sum_(s,t) sigma_st |s><t| tensor V^s rho V^(-t),
[Phi_rho(sigma)]_st = sigma_st gamma_(s-t),
gamma_k = Tr(rho V^k),                  indices modulo 5.       (2)
```

In particular gamma_0=1: all source populations survive. Off-diagonal
entries generally do not. The environment outputs conditional on classical
s are rho_s=V^s rho V^(-s).

Write omega=exp(2 pi i/5), V=sum_j omega^j Pi_j, and
w_j=Tr(rho Pi_j). The w_j are nonnegative and sum to one. With
Z|s>=omega^s|s>, equation (2) becomes

```text
gamma_k=sum_j w_j omega^(jk),
Phi_rho(sigma)=sum_j w_j Z^j sigma Z^(-j).               (3)
```

**Exact preservation criterion.** Phi_rho is the identity channel if and
only if supp(rho) is contained in ker(V-I). Necessity follows from
gamma_1=1: a convex combination of the five distinct unit roots equals 1
only if w_0=1. Positivity then places the whole support of rho in Pi_0.
Conversely that support condition makes every gamma_k equal to one.
In this case every rho_s=rho, so the receiver gets no information about s.

More generally Phi_rho is a reversible unitary source channel exactly when
rho is supported in one V-eigenspace Pi_j. It is then conjugation by Z^j
and a known Z^(-j) corrects it. If two different w_j are positive, then
|gamma_1|<1; the input (|0>+|1>)/sqrt(2) becomes mixed, so no unitary
correction can restore every source state. Again, the single-eigenspace
case has rho_s=rho and no informative receiver output.

For this order-five comparison, unless supp(rho) is contained in Pi_0,
the exact fixed source matrices are precisely the diagonal ones: for any
nonzero k, gamma_k=1 would already force w_0=1. This is a statement about
this channel, not a classification of all nondisturbing mixed-state families.

## 4. The complete receiver basis witness and the occupied readout

Fix one basis checkpoint v with f(x,y)!=0. For s!=t,
the second coordinate of C_s(v)-C_t(v) is -f(x,y)(s-t)!=0.
Consequently the five kets |C_s(v)> are orthogonal. In particular this
holds for every fixed h!=0 with f=2h, and for every occupied-SUM checkpoint
with any of the declared unit-gain contacts.

For rho=|v><v| one obtains

```text
gamma_k=0 for k!=0,
Phi_rho(sigma)=sum_s sigma_ss |s><s|.                    (4)
```

Thus the exact contact completely dephases a general source in its label
basis at these preparations. For |+>=5^(-1/2)sum_s |s>, the joint output is
5^(-1/2)sum_s |s>|C_s(v)>, while the source marginal is I_5/5.
The joint state remains pure: coherence is present in correlations, not
destroyed from the globally unitary system. It is absent from the reduced
source state that contract 2 promises to preserve.

The full checkpoint is not needed to distinguish the five classical outputs
on the supported SUM orbit. Its existing fixed reader obeys
R(C_s(v))=R(v)+s in F5. In the comparison Hilbert space the projectors onto
the computational-basis level sets of R are orthogonal and already give
perfect classical records. Calling them physical measurement outcomes would
require additional admission; their mathematical distinguishability suffices
for the argument in section 6.

## 5. Weyl witness and the conserved observable algebra

Use the explicit convention X|s>=|s+1 mod 5> and Z|s>=omega^s|s>.
For every source matrix unit, equation (1) gives

```text
U dagger (|s><t| tensor I) U = |s><t| tensor V^(t-s),
U dagger (Z tensor I) U = Z tensor I,
U dagger (X tensor I) U = X tensor V^(-1).               (5)
```

The minus sign in the X identity follows because its matrix units are
|s+1><s|; the wraparound uses V^5=I. At the basis preparation in section 4,
the source expectation of X changes from 1 to 0 on input |+>.

The complete receiver contains a five-cycle, so V has order exactly five.
For s!=t, V^(t-s)!=I. Linear independence of the source matrix units then
shows that the source operators conserved pointwise on the entire joint
space are exactly the diagonal algebra in the |s> basis. Preserving this
commutative algebra is not preserving the full matrix algebra M_5.
In general, a joint unitary conserving all A tensor I must lie in its
commutant, hence be I_S tensor W_E; such a unitary cannot imprint S on E.

For this contact V acts as identity on q,r and does not use them as controls.
Their full quantum observable algebra is therefore conserved, not only their
classical values. The total source s,q,r nevertheless need not be preserved:
s coherences, including correlations with q,r, can change. Statements about
these q,r operators apply to the contact, not to their whole native evolution.

## 6. Arbitrary phases and environments with exact classical records

The basis witness is not an artifact of choosing all permutation phases zero.
Every monomial lift with the same classical action has the form

```text
U_phi |s,v> = exp(i phi(s,v)) |s,C_s(v)>.
```

For fixed v with f(x,y)!=0 its distinct receiver kets remain orthogonal;
the source channel is still exactly (4), for arbitrary phi. Likewise,
source-independent receiver unitaries A and B replacing V^s by A V^s B
give gamma_k=Tr(B rho B dagger V^k): A cancels. If B is a diagonal phase
and rho is a basis checkpoint, rho is unchanged. Fixed source phases only
rotate surviving coherences and cannot restore their lost magnitudes.

There is a wider channel statement. Let a deterministic completely positive
trace-preserving process act on S and an arbitrary fixed, independent ready
environment. Suppose each basis source |s><s| is retained and a declared
archive distinguishes s perfectly. Purify the ready state and dilate the
process to an isometry, retaining every otherwise discarded environment.
Its action on the basis must be

```text
|s> -> |s> tensor |eta_s>.
```

The pure source marginal forces this factorization. Orthogonal archive
record supports force <eta_t|eta_s>=0 for s!=t, even if other environment
degrees of freedom are hidden or correlated with that archive. Expansion
of an arbitrary sigma therefore gives the dephasing channel (4) again.
Arbitrary phases, auxiliary systems, mixed ready states and implementation
details cannot change this conclusion while these two exact promises hold.

## 7. Full-state no-imprinting and restoration with an archive

**Theorem.** Let Lambda be any deterministic quantum channel from S to S A,
with all auxiliary inputs fixed independently of the unknown source. If
Tr_A Lambda(sigma)=sigma for every source density matrix, then there is a
single state tau_A such that Lambda(sigma)=sigma tensor tau_A for all sigma.

**Proof.** Dilate Lambda to an isometry W:S->S A F. Since a pure source
input |psi><psi| has the same pure source output, W|psi>=|psi>|eta_psi>.
Choose an orthonormal basis |i>. For its superposition (|i>+|j>)/sqrt(2),
linearity gives the two environment vectors eta_i and eta_j. Its unchanged
source off-diagonal entry requires <eta_j|eta_i>=1. These normalized vectors
are equal. Thus all basis vectors have one common eta and W=I tensor |eta>.
Tracing F gives the asserted constant tau_A. QED.

This proves the full-state case directly. It does not assert that every
restricted noncommuting mixed-state family has no readable classical sector.
Such broader structure questions belong to the cited established literature.

A deterministic restoration after writing, with any accessible auxiliaries,
is another channel of this form. If it restores every unknown source state,
all retained external records together must be source-independent. Therefore
it cannot both restore the source and keep an informative archive. Applying
U dagger restores the original joint preparation by uncomputing the write;
it does not keep its record. Copying the label into another archive first
does not help: after undoing U, the archive still distinguishes the source
basis components and their reduced source coherence remains absent.

This excludes neither restoration for a known state nor conditional,
postselected protocols outside the deterministic all-input promise. It also
does not say that joint information was destroyed. It identifies which
two simultaneous output guarantees are incompatible under the stated channel
and independent-preparation assumptions.

## 8. References, initial correlations and valid exceptions

For any initially entangled source-reference state tau_SR independent of rho_E,
the induced operation is Phi_rho tensor id_R. Identity on all source matrices
is consequently identity on every such SR state. Section 7 also factors the
whole output as tau_SR tensor tau_A. Basis preservation alone gives neither
claim: dephasing half of a maximally entangled SR pair changes it.

If the receiver is already correlated with S or R, its marginal alone does
not specify a channel on S. Write the full input as
Omega_SRE=sum_(s,t)|s><t| tensor Omega_st^(RE). For the contact (1), exact
preservation of this particular SR marginal is equivalent to

```text
Tr_E[Omega_st^(RE) (I_R tensor (V^(s-t)-I))]=0
for every s,t.                                         (6)
```

This follows by the same block expansion and the cyclicity of partial trace
for receiver-only factors. For universal preservation at a fixed receiver
marginal rho, the support criterion in section 3 is still necessary because
products are included, and sufficient because positivity restricts every
joint state to S R tensor supp(rho). Correlated inputs cannot be treated as
an unspecified resource for a claim about an independent ready receiver.

The legitimate exceptions and limits are precise:

- Every diagonal source state is preserved for arbitrary rho. More generally
  a joint state block-diagonal in s retains its SR marginal, even with initial
  receiver correlations. This is the commuting classical information case.
- At f(x,y)=0 a basis receiver is fixed by every C_s; the phase-free lift
  preserves all source states there but performs no write. In particular h=0
  has this property for every covariant coefficient in the declared class.
- An eigen-receiver in ker(V-I), including coherent superpositions along a
  nontrivial orbit, preserves the full source and supplies no source record.
  A different single eigenphase supplies only the correctable phase of
  section 3. These preparations are not the sharp occupied basis checkpoint.
- Merely [rho,V]=0 is insufficient. The uniform mixture on one five-cycle
  obeys rho_s=rho for all s but still has gamma_k=0 for k!=0. Its source is
  dephased although the receiver marginal alone carries no label information.
- For a general mixed receiver, (2)-(3) give the exact answer; a blanket
  claim of complete dephasing outside the specified basis/record case is false.

## 9. Earned conditional boundary

The occupied basis preparation admits an exact five-valued classical source
write and source-label retention. Under a quantum extension that allows every
source density matrix with the same independent preparation, its coherent
lift cannot additionally preserve the complete source. This remains true for
any deterministic implementation retaining exact distinguishable classical
records, and for a proposed restoration that keeps an informative archive.

This is a conditional quantum comparison, not a theorem that the declared
TWIST-J source physically admits coherent superpositions, this tensor factor,
this unitary interaction, or a quantum instrument. No Hamiltonian, energy
account, physical clock, source preparation, actual event or Born-law bridge
is supplied here. A choice to admit only the commuting source family is a
different explicit physical contract, not a hidden proof of full-state
preservation. No native theorem, owner status or cross-layer gate is changed.

[reservation]: https://github.com/mathorn1973/twist-j/issues/1442
[contact]: https://github.com/mathorn1973/twist-j/blob/a18e65d3e43acc6cb1896296b8bd0fdecdad35a7/probes/P-U-OCCUPIED-SUM-COVARIANT-CONTACT-1/PROOF.md#L135
[barnum]: https://arxiv.org/abs/quant-ph/9511010
[koashi]: https://arxiv.org/abs/quant-ph/0101144
