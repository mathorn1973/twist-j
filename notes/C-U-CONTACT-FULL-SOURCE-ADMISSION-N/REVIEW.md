# Independent source-preservation review

**NON-CANONICAL. Conditional mathematical review; no physical admission.**
A. M. Thorn; original text Apache-2.0.

Reservation: [issue #1442](https://github.com/mathorn1973/twist-j/issues/1442).
Public base: `a18e65d3e43acc6cb1896296b8bd0fdecdad35a7`.

## 1. Provenance and scope

This review was derived from the shared question and the existing
[occupied-contact proof](../../probes/P-U-OCCUPIED-SUM-COVARIANT-CONTACT-1/PROOF.md),
before reading this lane's SOURCE-PROOF.md or another agent's source
derivation. It is an independently derived argument within the same
assistant team, not an external review or a blind discovery.

The concrete contact and its classical results were already exposed.
All witnesses and identities below were checked symbolically. No scientific
program, enumeration, numerical experiment, verifier, or new reproduction
was run for this review. Cardinalities and formulas are not execution results.

After this source argument was delivered, the coordinator supplied a proposed
positive circuit outline: extend local SU(5) and pair-SUM operations to seven
systems and use `F_uw^dagger diag(omega^(2s(y-x)(m_w-m_u))) F_uw`, with a
seven-term cubic polarization and `6=1` in F5, without a clean ancillary
register. That outline was not an independent construction of this reviewer.
It is recorded as disclosed input. The later scoped cross-review in Section 9
must be distinguished from the independent source argument below.

The conclusion has two distinct premises: the classical contact already
defined by the probe, and an additional standard quantum interpretation.
Neither the latter nor a physical implementation follows from a permutation
of the declared classical carrier. No Canon status is changed here.

## 2. The classical statement and the additional quantum premise

Write `v=(p1,p4,p1p,p4p,q,r) in F5^6`, `x=p1-1`, `y=p1p-4`.
The representative contact and complete joint contact are

    C_s(v)=(p1,p4-f(x,y)s,p1p,p4p+f(x,y)s,q,r),
    f(x,y)=2(y-x),
    J(v,s)=(C_s(v),s).

The existing proof gives `C_s C_a=C_(s+a)` and `C_s^(-1)=C_(-s)` on the
whole classical receiver carrier. Thus J is a permutation of F5^7.
It leaves s, q, and r unchanged during contact. The receiver is occupied;
its preparation is not silently replaced by a blank state.

The quantum premise used here is `H_S=C^5` with orthonormal basis `|s>`,
and `H_B=C^(5^6)` with orthonormal checkpoint basis `|v>`.
The phase-free permutation lift is a unitary V satisfying

    V(|s> tensor |v>)=|s> tensor |C_s(v)>.

A more general monomial lift may multiply this output by
`exp(i phi(s,v))`. These phases do not affect the orthogonal-record argument.
The basis labels, superpositions, tensor decomposition, and operational
reading of R are additional assumptions, not established physical objects.

Only the contact is lifted globally here. The original W_N is explicitly
noninjective on its complete classical carrier; this review does not declare
W_N to be a global unitary. The selected native continuation on a fixed
reached time sheet consists of known bijections, which is sufficient below.

## 3. Exact occupied witness at N=4

Use the probe's preparation with `t=1`, `s1=0`, and arbitrary second source s.
The actual native first write gives, in F5,

    v3=(0,4,1,4,1,1),
    v4=b(v3)=(4,1,0,1,4,4).

At v4, `(x,y)=(3,1)`, hence `f=2(1-3)=1`. The fixed readout is

    S=p1+p4+p1p+p4p,
    L=p1+p4p,
    M=2((p1-1)(p4-3)+(p1p-4)(p4p-2)),
    R=(1-S^2)L+S^2 M.

Here `S=1`, `M=R=1`, and `z=4`. In particular the receiver is not blank.
The two contact outputs are

    C_0(v4)=(4,1,0,1,4,4),  R=1,
    C_1(v4)=(4,0,0,2,4,4),  R=2.

At native time 4, `theta_4=1`, so the selected next generator is b for
both outputs. The complete following checkpoints are respectively

    (0,4,1,4,1,1),  R=1,
    (0,3,1,0,1,1),  R=2.

Thus this witness uses the permitted N=4 contact and its actual next native
step. It is not a substituted externally chosen native word.

For input source `(|0>+|1>)/sqrt(2)`, the lifted contact produces two
orthogonal receiver branches. The source marginal becomes
`(|0><0|+|1><1|)/2`, although every classical branch retains its source label.
Arbitrary branch phases cannot change that marginal.

## 4. General source channel on the prepared occupied family

Fix t, s1, and a permitted contact time N independently of the unknown second
source. Let v be the corresponding free occupied checkpoint and
`r0=R(v)=t+s1`. On the prepared centered orbit the existing proof establishes

    R(C_s(v))=r0+s.

Distinct s therefore have distinct exact receiver records. In the quantum
lift, the states `|e_s>=exp(i phi(s,v))|C_s(v)>` are orthonormal.
For an arbitrary source density operator rho, the joint output is

    sum_(s,a) rho_(s,a) |s><a| tensor |e_s><e_a|,

and its source marginal is exactly

    Delta(rho)=sum_s rho_(s,s)|s><s|.

In particular a uniform coherent source becomes `I_5/5`; it is not preserved
as a pure state. No phase convention rescues off-diagonal entries, because
their multipliers are the zero inner products `<e_a|e_s>` for `a!=s`.
The same argument applies to perfect quantum records in disjoint record
subspaces, even when those records are not individual checkpoint vectors.

For a general fixed receiver density operator sigma and controlled unitaries
V_s, the source matrix element instead acquires the multiplier

    gamma_(s,a)=Tr(V_s sigma V_a^dagger).

Hence dephasing is not asserted for every receiver preparation. The exact
vanishing here follows from the distinguishable occupied-record outputs.
A common subsequent receiver unitary cannot change their overlaps.

The composite output is still a pure coherent state when the input was pure
and the operation was unitary. Its relative phases survive in correlations.
They have not been destroyed globally by the contact; the source alone no
longer has its original state. Joint invertibility is not local identity.

## 5. Source marginal versus source-reference preservation

Let A be an untouched reference and prepare

    |Phi>_(AS)=1/sqrt(5) sum_s |s>_A |s>_S.

With the same fixed occupied receiver, contact gives, with phases absorbed
in the definition of e_s,

    1/sqrt(5) sum_s |s>_A |s>_S |e_s>_B.

The source marginal is `I_5/5` before and after. Nevertheless, after tracing
out B the source-reference state has changed from `|Phi><Phi|` to

    1/5 sum_s |ss><ss|.

Thus checking the source marginal on this one mixed input would miss the
loss of its original reference correlations. Checking classical values of s
alone is weaker still. Exact identity of a source channel on all density
operators also preserves arbitrary source-reference states; preservation of
selected density operators does not imply that channel identity.

The probe declares one added F5 source coordinate. It supplies no dictionary
identifying that coordinate with all physical degrees of freedom of an
external source. Its classical source-coordinate result remains correct;
the stronger physical identification remains an additional obligation.

## 6. Exact restoration while retaining information

Consider any deterministic quantum protocol containing contact, recovery,
feedback, and auxiliary systems, with a fixed initial apparatus independent
of the unknown source. Purify the apparatus and include every discarded
system in an environment. The complete process then has an isometric
dilation W from the source to the source and a complementary system K.

If every pure source state is restored exactly, purity of its final marginal
requires the factorization

    W|psi>=|psi> tensor |eta_psi>.

An overall phase may be absorbed into eta_psi. Isometry gives

    <psi|varphi>=<psi|varphi><eta_psi|eta_varphi>.

For nonzero source overlap, the complementary overlap must be exactly one.
The normalized complementary vectors are therefore identical. On the whole
source Hilbert space all vectors are connected through nonorthogonal pairs,
so the complementary state is independent of the input.

Equivalently, preservation of each basis vector gives `W|s>=|s>|eta_s>`.
Preservation of every `( |s>+|a> )/sqrt(2)` forces `<eta_a|eta_s>=1`.
Linearity then gives `W=identity_S tensor |eta>` on the input space.
Tracing out part of K yields `rho -> rho tensor sigma_K` for the retained
outputs, with sigma_K independent of rho. The argument includes arbitrary
measurement and recovery implementations through their dilation.

Consequently an exact identity source channel cannot leave a new nonconstant
record of the source in the receiver, an archive, a measurement outcome, or
an unobserved environment. This is a statement about the net protocol, not
a prohibition on intermediate correlations or an assertion about energy.

Applying V^dagger restores both the source and the original occupied receiver.
If a distinguishable record is first copied to an archive, that inversion
instead leaves a state of the form

    sum_s alpha_s |s>_S |v>_B |record_s>_K.

The archive still dephases the source marginal. Moving the record elsewhere
does not restore the source while retaining that information.

## 7. Exceptions that a correct conclusion must preserve

**Orthogonal or classical source family.** The contact preserves every
`|s><s|` while recording s. It also preserves the marginal of every diagonal
mixture `sum_s p_s|s><s|`. It may change correlations with a purification, as
Section 5 shows. A universal ban on preserving a source and writing a record
would incorrectly exclude this permitted classical case.

**Classical blocks with quantum content.** Split the source space into
orthogonal blocks, for example `span{|0>,|1>}` and `span{|2>,|3>,|4>}`.
A different controlled interaction can record the block while preserving
arbitrary states inside each block. No superpositions across blocks are then
promised preservation. Even a noncommuting allowed family can contain a
readable classical part. For pure-state families the overlap-graph argument
forbids information within each connected component, not between orthogonal
components. This exception does not make the present unit-gain contact
coherence-preserving: that contact distinguishes all five source labels.

**Invariant receiver preparation.** For the phase-free lift, put
`|chi>=1/sqrt(5) sum_a |C_a(v)>`. The group law makes `C_s|chi>=|chi>` for
every s. All source states are then unchanged, but the receiver obtains no
information about s and has no single definite old value of R. This is not
the fixed occupied checkpoint preparation used in Sections 3 and 4.

**Quantum erasure and recovery.** Define `omega=exp(2 pi i/5)` and measure
the occupied five-dimensional receiver output subspace in the basis
`|f_k>=1/sqrt(5) sum_s omega^(ks)|e_s>`. Complete this measurement arbitrarily
on its unused orthogonal complement.
Outcome k leaves the unnormalized source
`1/sqrt(5) sum_s alpha_s omega^(-ks)|s>`. Its probability is 1/5 for every
input. Applying the diagonal correction `|s> -> omega^(ks)|s>` restores the
source. The retained outcome k is independent of the input and is not the
former s record. This provides an explicit recovery, with information erased.

**Prior side information and restricted promises.** A pre-existing classical
label of preparation can be copied without obtaining new information from
the source. An input-dependent apparatus therefore falls outside the fixed
apparatus premise. Preservation of a single known state, approximate
preservation, or a postselected success branch also differs from the exact
deterministic identity-channel requirement proved here.

## 8. Admission conclusion and primary references

The classical permutation and its exact inverse survive this review. Under
the additional standard quantum model, the informative occupied contact
preserves source basis labels but not arbitrary source coherence. Exact
universal restoration and a remaining informative record are incompatible
under the stated fixed-apparatus quantum assumptions. This is not an
unconditional physical no-go for TWIST-J or a refutation of its classical
source-coordinate statement.

A physical admission must separately identify the complete source, allowed
input family, equality criterion including any reference correlations,
receiver preparation, available interaction and controls, and record meaning.
An abstract circuit decomposition alone would not establish these premises.
No empirical result, physical coupling, Canon promotion, or global unitary
extension of W_N is claimed here.

The proofs above are self-contained applications of familiar quantum
information boundaries, not a claim to new general no-disturbance results.
Primary background sources are [Fuchs, Information Gain vs. State Disturbance
in Quantum Theory (1996)](https://arxiv.org/abs/quant-ph/9605014), and
[Koashi and Imoto, What is Possible Without Disturbing Partially Known Quantum
States? (2002 revision)](https://arxiv.org/abs/quant-ph/0101144).
The latter is particularly relevant to preserving the classical-block
exception instead of overextending a universal-state argument.

## 9. Subsequent cross-review of the control and admission text

After completing Sections 1-8, this reviewer read CONTRACT.md,
CONTROL-PROOF.md, README.md, and this REVIEW.md together. The cited Canon
QDD-AFFINE-CONTROL-REALIZATION and QDD-CLEAN-ENERGY-OBSTRUCTION passages
were also checked. SOURCE-PROOF.md had not yet been read at this stage;
this section does not certify its contents. The circuit was already disclosed
by the coordinator, so this is a cross-review, not an independent invention.
No scientific program or new verifier was executed.

The Fourier signs are correct for the declared positive-exponent F. The two
character sums have coefficients `u-u'-2hs` and `w-w'+2hs`, hence give
exactly `u'=u-2hs` and `w'=w+2hs`, each with amplitude one. Centering requires
`K^-1 C K`, and the Fourier-side changes `y<-y-x`, `m_w<-m_w-m_u` require
`L^-1 D_abc L`. Both orders in CONTROL-PROOF are correct.

The cubic polarization has coefficient 6, which is 1 in F5; the seven signed
coefficients therefore produce exactly 2abc. For each completed
`B_T^-1 Q_pivot(k) B_T`, the occupied pivot first contains the sum of its
original value and the other selected coordinates, acquires the intended
phase, and returns to its original label. No zero initialization is needed.
Only the completed diagonal gadgets commute; the text correctly requires
each compute/phase/uncompute sequence to finish before the next one.
The two original q,r registers are untouched on their full amplitude spaces.

The determinant and phase account is also correct: `sum_(j=0)^4 j^3=100`
gives `det Q(k)=omega^(100k)=1`. The four displayed two-level relative phases
put `omega^(k j^3)` on each nonzero level and exactly one on zero. This uses
the full admitted local SU(5) option, not affine controls alone. A scalar
phase of an implemented F cancels against its actual inverse in each
sandwich. An uncancelled scalar phase of a whole coherently controlled
circuit would become relative; the proof explicitly preserves that boundary.

For the clean additive-energy lemma, conservation and a common final
environment give one input-independent energy gap. The finite full-space
permutation forces that gap to zero. Setting `h=1,s=3` attains displacement
one while leaving u,w arbitrary. Thus `E_u(u-1)-E_u(u)` and the negative
of `E_w(w+1)-E_w(w)` are one real constant; summing around the five-cycle
makes it zero. Both profiles must be flat. This is a necessary condition
under the declared clean, global, additive-energy premises, not a physical
energy assignment or a sufficient resource construction.

The formal lift distinction in CONTRACT is valid. For `i_X Omega=dH`,
`H=-s h^2` gives the stated u,w shifts and kappa increment h^2.
For `H*=-s h^2+s h^10`, the x,y derivatives of the added term vanish in
characteristic five, whereas its s derivative changes the kappa increment
to `h^2-h^10`, zero on F5 points. Adding 4s to the quadratic lift instead
makes that increment `h^2-4`, zero on the prepared orbit only. These are
explicitly different chosen polynomial lifts. A zero point function need
not have zero formal polynomial derivatives. The eight-coordinate formal
symplectic construction is kept distinct from the seven-system complex
quantum comparison and from real physical energy.

No mathematical blocker was found in this cross-reviewed control/admission
scope. The seven-system extension, pair access, coherent local controls,
timing, physical source identification, independent contact selection and
record interpretation remain additional obligations. The README and contract
retain these qualifications and do not promote the circuit to a native law.
Their explicit endpoint qualification was also checked: restored labels at
completed gadget boundaries do not prove unchanged states during pulses.
Preservation at every physical instant needs the actual Hamiltonians and
their complete prefix evolution, beyond the endpoint identity audited here.

## 10. Later cross-review of SOURCE-PROOF.md

After the source author completed all nine sections, this reviewer read
SOURCE-PROOF.md against the already written independent argument above.
This is a subsequent same-team comparison, not a claim that either text was
produced without the shared question or previously exposed classical result.
No scientific execution was added.

The controlled-unitary convention gives `gamma_(s-t)=Tr(rho V^(s-t))`.
With `V=sum_j omega^j Pi_j`, its source channel is indeed the mixture of
conjugations by `Z^j` with weights `Tr(rho Pi_j)`. The Heisenberg identity
has the opposite increment: `U^dagger(X tensor I)U=X tensor V^(-1)` for
`X|s>=|s+1>`. Both signs in the source proof agree with direct expansion.

Its fixed-preparation identity criterion is exact: `gamma_1=1` forces all
spectral weight into Pi_0, and positivity forces the support there. A single
other eigenspace gives a known correctable phase but no source record.
Two positive distinct spectral weights reduce the adjacent coherence modulus.
The stronger fixed-matrix conclusion uses the prime order five correctly:
for every nonzero k, the only root with `omega^(jk)=1` is j=0.
All-input observable conservation is separately distinguished from these
fixed-preparation statements; the full commutant argument is valid.

For an initially correlated source/reference/receiver input, cyclicity of
the receiver partial trace gives precisely the condition in equation (6),
with `V^(s-t)-I` on the receiver. Products make the fixed-receiver support
condition necessary for universal preservation. Positivity confines every
joint state with that receiver marginal to its support, making the same
condition sufficient. The explicit `[rho,V]=0` counterexample correctly
rejects an insufficient weaker criterion.

The exact-record dephasing extension and deterministic restoration theorem
agree with Sections 4-7 above. They preserve the distinction between a
classical diagonal family, one unchanged marginal, universal channel identity,
reference correlations and reversible joint information. The receiver
pre/post matrices A,B in Section 6 are explicitly fixed unitaries, matching
the scope of the displayed single-matrix sandwich and cancellation formula.
No mathematical blocker was found under these stated assumptions.
