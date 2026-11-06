# Independent derivation and countercheck

**C-TWIST-RELATIONAL-PHYSICS-1-N — NON-CANONICAL, conditional L1.**

Author: A. M. Thorn. License: Apache-2.0.

## Independence and execution boundary

This review and `break_check.py` were written from the frozen `PREREG.md`
and the following permitted source contracts:

- Public Canon v106, `ACTIVE-ISOSPECTRAL-RECORD` and
  `COMPACT-ACTIVE-RECORD-APPARATUS`, at their stated conditional scopes;
- `notes/C-COMPACT-ENERGY-RECORD-N/COMPACT_MODEL.md`, Git blob
  `381f32303b8233203bec0a64521cc29e389a0776`;
- `notes/C-ORIGINAL-PORT-SOURCE-PREPARATION-N/SOURCE_CIRCUIT.md`, Git blob
  `fea890cd90c5f1d6c14e477c51509e08da2e8ffa`.

The builder's `PROOF.md`, `verify.py` and execution outputs were not read.
The new countercheck has not been executed during authoring. First execution
requires the coordinator to confirm immutable public pin and readback. A
later execution record must state its actual result; this pre-execution
review is not a PASS record.

The source notes retain historical candidate headers. The premises used
here are the named v106 claims at the pinned public commit in `PREREG.md`,
not a scientific promotion conferred by the note headers or this review.

The independent arithmetic route uses rational isolation of sqrt(5),
gcd-orbit Fourier cancellation in composite dimension 561, direct integer
binomial sums, and exact rational small-matrix counterexamples. It does not
reconstruct the original contact/source circuit or enumerate a dense
206794356912000-dimensional matrix.

## 1. State space, isometry and the complete energy shell

Let A denote the complete inherited apparatus: its 561-level program
cursor and eleven data registers. The eleven data dimensions are

    15, 15, 15, 4, 3, 26, 26, 3, 2, 2, 2.

Their product is 657072000. Thus dim(A)=368617392000, and adjoining the
new 561-level reference clock gives total dimension 206794356912000.
These are dimensions, not counts of physical sites or qubits. There are
thirteen declared registers. An arbitrary passive reference is tensorially
retained and is not assigned a fictitious finite dimension.

The inherited source expansion gives 12 complete spatial calls, each with
eight factors, 17 other source gates, two setting gates, three further
eight-factor spatial steps, and one pointer gate:

    12*8 + 17 + 2 + 3*8 + 1 = 140.

The additional 420 program gates are identities. The source theorem and
the exact full actions of these gates are premises, not consequences of
the present arithmetic check.

Write d=561, K=560 and g=E_ctl>0. The apparatus spectral resolution is

    H_A = sum_s g(2s+1)/d * P_s,       s=0,...,K,
    P_s P_t = delta_(s,t) P_s,         sum_s P_s = I_A.

Each P_s has the complete data multiplicity. The new clock has eigenvalues
2gq/d, q=0,...,K. Its ground energy is zero; the apparatus spectrum is
strictly positive, between g/d and (2K+1)g/d.

Define V:A -> C tensor A by

    V = sum_s |K-s> tensor P_s.

Orthogonality gives V*V=I_A and

    Q_star = VV* = sum_s |K-s><K-s| tensor P_s.

The total energy on a general (q,s) spectral block is
g(2q+2s+1)/d. Equality to E_star=(2K+1)g/d holds if and only if q+s=K.
Consequently Q_star is the entire E_star eigenspace, not a selected proper
part of it. All 561 paired blocks and all 314160 outside blocks are kept
in the code's exact census.

It follows that

    (H_total-E_star)V = 0,
    H_total Q_star = Q_star H_total = E_star Q_star.

For any normalized apparatus/reference density rho_0,

    R = (V tensor I_ref) rho_0 (V* tensor I_ref)

is normalized, positive and stationary. All statements hold for mixed
states and arbitrary passive references by tensoring the identities with
I_ref. No purification with an assumed finite reference size is needed.

## 2. Composite Fourier clock and forward conditional dynamics

Put zeta=exp(2pi i/d) and

    |t_j> = d^(-1/2) sum_q zeta^(-qj) |q>.

This is an orthonormal clock basis although d=3*11*17 is composite.
For any nonzero residue difference h, let a=gcd(h,d) and r=d/a. The
residues qh mod d visit every multiple of a exactly a times. Their sum
is a times a complete r-cycle. The identity

    (1-x^a) sum_(u=0)^(r-1) x^(au) = 1-x^d

evaluated at the primitive d-th root proves cancellation: a<d ensures
1-zeta^a is nonzero. The checker covers every h, including all seven
possible gcd classes. It never assumes primality of d.

Let F_j=exp(-i H_A tau_j/hbar), with tau_j=pi*hbar*j/g. The clock bra
has the positive phase, so

    K_j := (<t_j| tensor I_A)V
         = d^(-1/2) sum_s exp[2pi i(K-s)j/d] P_s
         = d^(-1/2) exp[i pi(2K+1)j/d] F_j.

The underlying integer exponent identity is

    2(K-s)j - (-(2s+1)j) = (2K+1)j.

The countercheck checks it for every one of the 561^2 pairs (j,s),
before any reduction modulo a phase period. Thus K_j* K_j=I_A/d and
the clock probability is exactly 1/d for every normalized input.
The local-clock conditional apparatus/reference density is exactly

    (F_j tensor I_ref) rho_0 (F_j* tensor I_ref).

Changing the sign in the ket definition while continuing to call the
conditional evolution forward is not harmless: the relative defect
between s=0 and s=1 at j=1 is 4 in units pi/d. It cannot be absorbed
into one common phase. The checker detects that negative control.

The tau_j are a declared physical calibration of a finite relational
clock. Uniform clock sampling and these conditional densities do not
describe a sequence of invasive measurements, a first-passage process,
an unbounded time variable, or a comparison of proper times on paths.

## 3. Complete energy-commuting effects, including E_out

Let Pi_0 and Pi_1 be the two complete pointer projectors on A. They
need not commute with H_A. Define

    E_jy = Q_star (|t_j><t_j| tensor Pi_y) Q_star,
    E_out = I - Q_star.

Pulling back by the isometry gives the exact expression

    V* E_jy V = (1/d) F_j* Pi_y F_j,
    E_jy = (1/d) V F_j* Pi_y F_j V*.

This proves positivity on the full carrier: the right side is a positive
operator embedded by an isometry. Equivalently it is a Gram form, with
no commutation assumption between an apparatus energy block and Pi_y.

For each fixed j, completeness of the pointer yields

    sum_y E_jy = Q_star/d.

Summing over all d clock outcomes yields Q_star. The remaining full-carrier
sector is E_out, so

    sum_(j,y) E_jy + E_out = I.

All these effects commute with H_total. The compressed effects act only
within the single energy shell, where the Hamiltonian is a scalar, and
E_out is a spectral projector. No locality of these measurement operations
has been inferred from this commutator.

There is a useful stronger diagnostic:

    E_jy^2 = E_jy/d.

Every nonzero E_jy is therefore a scaled projector and is not itself a
projector because d>1. A two-energy rational pointer block and a third
outside-energy block explicitly verify positivity, commutation,
completeness, the scaled-projector identity and the necessity of E_out.
The general result comes from the displayed orthogonal-block proof; the
small witness is a counterexample to stronger incorrect claims, not a
replacement for the general proof.

For ideal R supported by Q_star,

    tr(R E_jy) = tr[R (|t_j><t_j| tensor Pi_y)],
    tr(R E_out) = 0.

This is equality of probabilities. It is not equality of the instruments'
post-measurement states. For example, a local clock projection on an
energy basis state |K-s,s> produces |t_j,s>, whose weight outside Q_star
is 1-1/d. A shell-supported implementation of the compressed effects can
retain the shell. The local-clock conditional-state formula in Section 2
must not be advertised as the post-state of every compressed-effect
instrument.

## 4. Exact clock energy moments

The inherited apparatus assigns the masses

    w_s = binom(K,s)/2^K

to its energies, independently of the admitted data/reference input.
The integer identities

    sum_s binom(K,s) = 2^K,
    sum_s s binom(K,s) = K 2^(K-1),
    sum_s s^2 binom(K,s) = K(K+1) 2^(K-2)

give

    <H_A>/g = 1,                 Var(H_A)/g^2 = K/d^2,
    <H_C>/g = K/d,               Var(H_C)/g^2 = K/d^2,
    Cov(H_A,H_C)/g^2 = -K/d^2.

Thus <H_total>/g=(2K+1)/d and Var(H_total)=0. This exact cancellation
depends on the anticorrelated pairing q=K-s. Using q=s instead fails the
energy-shell equation on 560 of the 561 blocks; only the midpoint remains.

The new stationary preparation has not been obtained by erasing the
apparatus's energy coherence. It correlates that coherence with the new
clock. Dephasing those correlations removes conditional off-diagonal
terms. In a normalized two-energy coherent block, the j=0 density has every
entry 1/2, while dephasing changes it to diag(1/2,1/2). A plus-state
projector then changes its probability from 1 to 1/2.

This witness also occurs within an admitted pure ready input, without
assuming a new two-energy preparation. The extreme spectral masses obey
w_0=w_K=2^(-K). Write phi_s=P_s|ready>/sqrt(w_s) for s=0,K. The actual
two-energy block is 2^(1-K) times the normalized coherent block above.
The effect projecting onto (phi_0+phi_K)/sqrt(2), with zero action on all
other energies, has probability 2^(1-K) before dephasing and 2^(-K) after
dephasing. The strictly positive difference is exactly 2^(-K). This is a
full probability comparison, not conditioning on a rare accepted block.
The code verifies these rational values. Thus an incoherent energy mixture
cannot replace the same admitted relational state.

## 5. Cursor distribution, window and joint-event lower bound

The inherited complete apparatus Hamiltonian is unitarily equivalent to

    g I - (2g/d) S_x

on spin K/2, tensored with the complete data identity. Starting from the
program endpoint zero gives a binomial cursor position m with parameter

    p(t) = sin^2(g t/(d hbar)).

The symmetric-power derivation uses K two-state rotations as a mathematical
representation. It does not add K hidden physical clock registers and
does not assert independent repeated detection trials.

At the conditional times tau_j, p_j=sin^2(pi*j/d). The frozen window
J={187,...,374} has 188 elements and a complement of 373. Its angle
range is exactly [pi/3,2pi/3]. Monotonicity of sine on the first half
and reflection about pi/2 give p_j>=3/4.

The source/pointer contract says that no gate before gate 140 acts on the
initially zero pointer. For cursor m<140 its pointer-one probability is
zero. For all m>=140 the complete payload is the same endpoint, because
the remaining gates are identities. The pointer effect is diagonal in the
cursor register, so orthogonal cursor branches do not create extra cross
terms in its probability.

For X~Bin(K,p), Markov's inequality gives

    Pr(X<L) <= 3^(L-1) E[3^(-X)]
             = 3^(L-1) (1-2p/3)^K
             <= 3^(L-1)/2^K
             = epsilon/3 < epsilon,

where epsilon=(3/16)^140 and K=4L=560. Since 3<4,

    epsilon < (1/4)^140 = 2^(-280) < 1/2.

The checker independently evaluates the endpoint binomial tail exactly at
p=3/4 using common denominator 4^K. It also checks the binomial coefficient
identities that telescope to

    d/dp Pr[Bin(K,p)<L]
      = -K binom(K-1,L-1) p^(L-1) (1-p)^(K-L) <= 0.

Thus the endpoint bound controls the entire window without numerically
evaluating any sine.

For the inherited phase settings the endpoint pointer contrast is Delta.
Both cursor distributions are the same, and the unfinished-pointer weight
is zero for both. The complete probability contrast of the joint event
"j in J and pointer one" is therefore exactly

    delta_joint = (Delta/d) sum_(j in J) B_j.

The factor 1/d is essential; no clock-window postselection is discarded.
All other clock and pointer outcomes, and E_out, remain in the full law.

To certify the inherited scalar contrast independently, isolate the positive
square root by

    559/250 < sqrt(5) < 22361/10000.

The checker certifies both inequalities by integer squares. For

    f(x)=65536(48533-10985x)/[5^9(39521+154x)],

the denominator is positive on that interval, the numerator remains
positive, and f is strictly decreasing because
10985*39521+48533*154>0. Hence

    Delta > f(22361/10000) > 1/50.

No decimal or floating-point approximation enters this certificate.
Consequently

    delta_joint > (188/561)(1-epsilon)Delta
                > (188/561)(1/2)(1/50)
                = 47/14025.

The checker also compares the stronger rational-isolation bound directly
with the frozen threshold. It does not optimize the window or alter the
threshold after execution.

## 6. Robustness of the one joint event

Use trace distance T(rho,sigma)=||rho-sigma||_1/2. If the actual normalized
joint preparations obey T(Rtilde_+,R_+)<=epsilon_+ and the corresponding
minus bound, and the valid implemented event effect differs from the
ideal one by operator norm at most eta, then

    |ptilde_+-p_+| <= epsilon_+ + eta,
    |ptilde_--p_-| <= epsilon_- + eta.

The contrast can therefore decrease by at most
epsilon_++epsilon_-+2eta. With each tolerance equal to 1/10000, this loss
is 1/2500 and

    47/14025 - 1/2500 > 1/400.

These errors refer to the new complete stationary preparation and new
compressed joint-event measurement. The inherited compact-device tolerance
does not certify either operation. The probabilities are per trial and
are not renormalized on acceptance, so no rare-outcome amplification of a
conditional-state error is being suppressed.

## 7. Fixed review boundaries

The new construction is mathematically finite apart from the optional
passive reference. Its local-clock conditionals reproduce the already
declared finite source/contact/memory apparatus. The physical choice of
the stationary preparation, energy scale, clock readout and complete
effect implementation remains an explicit postulate.

In particular, the following stronger claims are not established:

- Native six-pentit U generates this entire apparatus or the new reference
  clock. The original n is not identified with j or with proper time.
- The preparation is free, arises thermally, or is generated by the new
  closed Hamiltonian from an independently supplied uncorrelated ready state.
- Every compressed effect is local, a projector, or has the local-clock
  conditional density as its implemented post-state.
- A single joint distribution specifies repeated interrogation, permanent
  records, apparatus renewal or indefinite clock operation.
- Register locality is simulated spatial locality, or this finite model
  supplies Lorentz symmetry, a gravitational metric or a physical species.
- The inherited active-source contrast is independently rederived here.
  Its formula and admitted memory/reference scope remain canonical inputs.

Within those boundaries, the independent analytical derivation supports the
fixed candidate contract. The exact arithmetic and counterexample checks
remain unexecuted until public pin/readback, and their result must be
recorded separately without modifying this contract to fit the output.
