# Conditional obstruction for every finite even-timed contact word

PUBLIC / NON-CANONICAL / L1. A. M. Thorn, 2026-10-18.
SPDX-License-Identifier: Apache-2.0.

This proof is frozen before evaluating condition R3. The finite condition
is not assumed to have passed. The only computed proposition in this
probe is the exact rank in section 4. Its all-word consequence follows
from the written argument, not from a finite search over histories.

## 1. Literal source and complete amplitude state

Use the supplied rational apparatus at public main
dc162f03ba9e0b09ce950a76f0bf4939a31a8d8d, file
probes/P-TWO-USE-TYPED-READOUT-CLOSURE-1/apparatus.py.
SOURCES.tsv pins its bytes and its finite domain. This is the existing
declared extension, not an admitted contact of the original native U.

The amplitude tuple is z=(u,v,A0,A1,B0,B1), with u,v in Q^705 and
four tapes in Q^4, hence dimension 1426. The separate pointer k toggles;
it does not select a different amplitude matrix. Let P inject the four
ports, P^t P=I, J0=I-PP^t and K=I-PP^t/2. The literal free update is

    u'=v,
    v'=-J0 u+K H_w v+2P A0,
    A0'=A1, A1'=B1,
    B0'=P^t u/2-P^t H_w v/4,
    B1'=B0.

H_w has diagonal 10/9 and off-diagonal weight/324 for squared
displacement norms 2,4,8,10,16 and weights 6,1,15,1,1 respectively.
Only endpoints inside the frozen finite domain are retained.

The inverse follows by substitution:

    v=u',
    u=-J0 v'+K H_w u'+2P B0',
    A0=P^t v'/2-P^t H_w u'/4,
    A1=A0', B0=B1', B1=A1'.

In particular F is invertible. Set T=F^2 and

    H_pair=ker(T-I)=ker(F-I) direct_sum ker(F+I).

The last equality requires no diagonalizability assumption: for Tz=z,
(z+Fz)/2 and (z-Fz)/2 are respectively the +1 and -1 components.
Calling H_pair the pure pair refers only to these free amplitude modes.

The five source sites, in SOURCE order, are

    Y=((0,0,0),(1,1,0),(1,0,1),(0,1,1),(2,0,0)).

Only the first four are ports. S_source sends eta in Q^4 to the field
whose values are eta_j-sum(eta)/5 at those four sites and
-sum(eta)/5 at the fifth site; it vanishes elsewhere. Define

    D_v=S_source[e1,e2]/2,
    D_src alpha=(0,D_v alpha,0,0,0,0).

The finite domain is exactly Y+B_zero+B_zero, where B_zero consists
of zero and all 60 even-parity stencil displacements. Its lexicographic
TSV has 705 points; it is included unchanged and byte-pinned.

## 2. Every actual history belongs to the tested word class

The actual eight-phase schedule contacts A at c=1 and B at c=4.
Rows c=2,3 and c=5,6 apply F. Other rows do not change amplitudes.
Thus consecutive contact OPPORTUNITIES are separated by exactly two
free steps, including across the cycle boundary. Buffer capture precedes
A; B uses the retained buffer. Both source labels remain in F5^2.

With ell=(0,1,2,-2,-1), an accepted contact has effective coordinate

    alpha=sigma*(ell(q),ell(r)+1),   sigma in {+1,-1}.

A refused contact has alpha=0. Accepted zero impulses can still change
a control sign, but their effective amplitude is zero. Every actual
effective coordinate is in the larger rectangle

    A={alpha in Z^2: |alpha_1|<=2, |alpha_2|<=3}.

No claim that every word in A is a native-source history is needed.
We prove an obstruction for ALL finite words in A at the same timing.
Every guarded actual history is then covered as a subset, including
arbitrary native heads, buffers, retained signs, banks and refusals.

Starting with zero amplitudes, a cut immediately after the Nth opportunity
has the exact amplitude

    w_N=sum_(i=0)^(N-1) T^(N-1-i) D_src alpha_i.

At other cuts the contact contribution is F^r w_N for some r>=0.
More generally a history starting at z_in has endpoint

    z_out=F^M z_in+F^r w_N.

Here M counts free steps and r is the common free padding after the
last listed opportunity. Zero entries retain the opportunity spacing.
A "nonzero word" below means at least one nonzero EFFECTIVE accepted
impulse, not merely a nonzero proposal that was refused.

## 3. Exact leading reduction at the prime 3

Let Z_(3) be the rational numbers with denominator prime to 3, and reduce
3-integral coefficients to F3. For a rational vector let v3 be the
minimum coordinate valuation, with v3(0)=+infinity.

Define

    Abar = 81 H_w mod3,
    Kbar = I+PP^t mod3,
    Bbar = Kbar Abar.

Indeed 81*(10/9)=90 is zero mod3, and
81*(weight/324)=weight/4. Thus Abar is precisely adjacency for
squared displacement norms 4,10,16, all with coefficient 1, on the
literal finite domain. The other two shells vanish. Kbar multiplies
the four PORT ROWS by 2 and all other rows by 1.

The matrix 81F has entries in Z_(3). Its reduction has only two nonzero
output blocks:

    v_out=Bbar v_in,
    (B0)_out=-P^t Abar v_in.

Every other block vanishes. Repeated multiplication therefore has
v-block Bbar^n on an input supported in v. In particular the leading
v-block of 3^8 T is Bbar^2. No infinite-lattice or translation-invariant
spectral substitution is made.

Dbar_v has the following five nonzero rows in the Y order above:

    (1,2), (2,1), (2,2), (2,2), (2,2).

These rows are inserted by coordinate, not at the first five TSV
indices. The fifth site has no port factor. The first and third
rows have determinant 1 mod3, so the source image has rank two.

## 4. The sole finite condition R3

The exact prospective test is

    R3: rank_F3(Bbar^705 Dbar_v)=2.

For a linear map on a 705-dimensional space, its ascending kernel
chain stabilizes by exponent 705:

    ker(Bbar^705)=ker(Bbar^(705+j))   for all j>=0.

Otherwise each strict inclusion would increase dimension beyond 705;
once two consecutive kernels agree, all later kernels agree.

Consequently R3 is equivalent to

    im(Dbar_v) intersect ker(Bbar^705)={0}.

If R3 holds, then for EVERY n>=0 and beta in F3^2\{0},

    Bbar^n Dbar_v beta != 0.

For n<=705 this follows by multiplication to exponent 705. For later
n it follows from kernel stabilization. This is why one finite test
can imply a statement about all word lengths.

A rank smaller than two refutes R3 only. It does not supply a finite
contact word with pure-pair endpoint, a bank, or a native preparation.

## 5. Exact valuation of one impulse

For a nonzero alpha in A set

    nu=min(v3(alpha_1),v3(alpha_2)).

The amplitude bounds give nu in {0,1}. The value 1 is possible only
for alpha=(0,+3) or (0,-3). Let beta be the nonzero reduction of
alpha/3^nu. For every j>=0,

    3^(8j-nu) T^j D_src alpha
      =(81F)^(2j) D_src(alpha/3^nu).

The right side is 3-integral. Its v-block reduces exactly to

    Bbar^(2j) Dbar_v beta.

Under R3 this is nonzero. Therefore

    v3(T^j D_src alpha)
      =v3(v(T^j D_src alpha))
      =nu-8j.

The first equality follows because all blocks are 3-integral after
the displayed normalization, while the v-block has a nonzero
reduction. This is equality of valuations, not only a bound.

## 6. The oldest effective impulse cannot cancel

Take any finite word with at least one nonzero alpha_i. Its oldest
nonzero term has the unique largest age j and valuation nu_old-8j,
at most 1-8j. Every younger nonzero term has age at most j-1 and
valuation at least

    -8(j-1)=8-8j.

The gap is at least seven. Hence the unique lowest 3-adic layer of
the oldest term survives the sum:

    v3(v(w_N))=nu_old-8j,   in particular w_N!=0.

The same argument after one further T gives

    v3(v(Tw_N))=v3(v(w_N))-8.

Thus Tw_N!=w_N and

    w_N not in H_pair.

This proof imposes no bound on N, no bound on the native counter and
no assumption that an energy shell is finite.

## 7. Stronger no-return statement from every initial pure pair

The previous result concerns the contact contribution, independently of
the initial state or the bank that selects the effective word. Suppose

    z_in in H_pair.

At an arbitrary finite later cut,

    (T-I)z_out
      =(T-I)(F^M z_in+F^r w_N)
      =F^r(T-I)w_N.

F is invertible and commutes with T. Under R3 the last vector is
nonzero whenever the history contains a nonzero effective impulse.
Therefore

    z_out not in H_pair.

CONDITIONAL THEOREM: if R3 holds, every finite actual scheduled history
starting anywhere in ker(F^2-I), with at least one nonzero accepted
effective impulse, ends outside ker(F^2-I). It also cannot return
to zero. Histories containing only zero effective impulses retain
the ordinary free evolution.

This includes an initial pure pair with occupied tapes. It does not
include an arbitrary occupied initial amplitude outside H_pair, whose
other modes can affect cancellation. No funding-from-blank claim is
needed for this stronger conclusion: the algebra covers all rectangle
words, including whichever word the occupied-state guards select.

## 8. Relation to energy and the native-contact programme

The source's positive quadratic account is

    E_cl(z)=(||u||^2+||v||^2-u^t H_w v)/2
            +2*(||A0||^2+||A1||^2+||B0||^2+||B1||^2).

F preserves it. Positivity follows from 0<H_w<2I. The lower bound
H_w>=(2/9)I follows from the off-diagonal row sum <=8/9. For the
upper bound, extend a vector by zero outside the domain and write

    u^t(2I-H_w)u=(1/2) sum_(x,d) w_d*(u_x-u_(x-d))^2.

Here w_d=weight(d)/324 and x runs over the full even-parity lattice;
the zero extension makes every displayed sum finite.
Equality would force invariance under the positive-weight shift (4,0,0);
finite support then forces u=0. The pure-pair space and its
E_cl-orthogonal complement consequently split the energy additively.

R3 would prove that after a nonzero effective history from a pure pair
the complementary energy is strictly positive at every finite later
cut. For its fixed pure-pair projection, the algebraic minimum obtained
by dropping that complement is not attained by such a history. This does NOT provide
a positive uniform gap, an approximation-rate bound or an asymptotic
lower bound.

The actual funded contact subtracts its exact E_cl increment from the
bank b and adds that increment to recorded work W. Free rows preserve
both accounts. Thus, for an initial pure pair of energy E_in,

    E_pair,out + E_perp,out + b_out = E_in + b_in,
    W_out-W_in = E_pair,out-E_in + E_perp,out,
    b_in-b_out = E_pair,out-E_in + E_perp,out.

Under R3 a nonzero effective history has E_perp,out>0. This does not
force the NET bank withdrawal to be positive: the pair energy can fall.
Nor does it identify any term with a Dirac-energy denomination. For a
candidate endpoint energy E_star and capacity B, the guard requires
E_in+b_in-B <= E_star <= E_in+b_in. The simpler funding-from-blank
inequalities must not be extended to occupied initial pairs.

The source impulse, its chosen E_cl and funded bank are still a
declared rational extension. This probe does not select a physical
energy reading, realize the Dirac onsite projector, or fill the
common native carrier required by #1596. The isolated channel
(0,pi)->(pi/2,pi/2) and the denomination 2*sqrt(1+m^2)-2m retain their
separate typing and accounting obligations. The exact ratio
m/atan(m)>1 is untouched.

The earlier four-dimensional Hilbert closure, compressed-channel value
3/20 and seven-dimensional energy closure are not computational
claims of this R3 verifier. The present formal test neither validates
nor changes those separate analytical statements.
