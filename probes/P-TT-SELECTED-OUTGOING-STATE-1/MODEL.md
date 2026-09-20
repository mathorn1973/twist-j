# ETH-TT-1: a complete selected outgoing vector state

PUBLIC; NON-CANONICAL; conditional mathematics at L1. Public Canon v90,
base `1d3e70433f850d03aa210374d8cda16dd97a0c10`; lock
[#1097](https://github.com/mathorn1973/twist-j/issues/1097).
The author selects this bounded effective theory under the
[selected-theory program](../../notes/canon/SELECTED-THEORY-PROGRAM-2026-09-20.md).
Selection is an input. Its consequences are the mathematical claims.

## 1. Unchanged source and primary dynamics

Retain DEF-K1-ISOLATED-TT-EMISSION, including its marked plus frame, unit
source amplitude, isolated onset and complete radiative-channel transfer.
These are already selected inputs, not new deductions from J. The source is
one word w in

    W={0010,0011,0100,0101,0110,1001,1010,1011,1100,1101}.

Its law is nu(0110)=nu(1001)=1/6, and nu=1/12 on the other eight words.
This is the established native four-word frequency law used here as a
selected single-packet ensemble. No independent sequence of preparations
or physical occurrence mechanism is inferred from that arithmetic theorem.

For t=0,1 and r in Z/5 set

    u_t=w_(t+2)-w_t,
    b_src,t(r)=[delta_(r,u_t)+delta_(r,u_t+1)]/sqrt(2),
    H_t=b_src,t^2,  Phi=H_1-H_0,
    L=[188I-29(S+S^-1)-65(S^2+S^-2)]/324,  Sf(r)=f(r+1),
    h_0=h_1=0,
    h_(m+1)=(2I-L)h_m-h_(m-1)+delta_(m,1)Phi,  m>=1.

The outgoing h is real in this frame; its cross component is zero.
The source amplitude b_src is not identified with an outgoing vector.
The primary recurrence for h is retained at zero as well as nonzero field.
Every h_m is rational. Define A_0=A_1=0, A_2=I and
A_(m+1)=(2I-L)A_m-A_(m-1) for m>=2, so h_m=A_m Phi.

The six active sources are +/-d1, +/-d2, +/-(d1+d2), where

    d1=(e0-e2)/2,  d2=(e4-e1)/2.

Each of +/-d1 and +/-d2 has mass 1/12, each of +/-(d1+d2) mass 1/6.
The remaining four words give the zero history, total mass 1/3. Retain
these zero preparations; do not condition on emission.

## 2. New full-law selection

Draw epsilon_+,epsilon_- independently and uniformly from {+1,-1}, once
per isolated packet, independently of w. Reuse these same two signs at
every site and counter. With

    a_m(r)=sqrt(max(h_m(r),0)),
    b_m(r)=sqrt(max(-h_m(r),0)),
    v_m(r)=epsilon_+ a_m(r)+i epsilon_- b_m(r),
    V_m(r)=(Re v_m(r),Im v_m(r)),

both square roots mean the nonnegative real root. If h=0 then v=0.
There is no branch division, fresh sign at a later counter, or hidden
independent draw at another site. Values belong to real algebraic radical
extensions (and their complexification); membership in Q(zeta_5) is not
asserted for v. At every point,

    v^2=h,  |v|^2=|h|,
    det(I2+[[Re h,Im h],[Im h,-Re h]])=1-|h|^2=1-|v|^4.

The full state is the pushforward of the 40 labelled atoms
(w,epsilon_+,epsilon_-) with weight nu(w)/4 to the ENTIRE infinite
counter sequence. Equivalently every finite prefix is its literal
restriction. The law has 25 distinct histories: one zero atom of mass
1/3, sixteen atoms of mass 1/48, and eight atoms of mass 1/24. These
same support counts hold at every single slice m>=2. Counters 0 and 1
are entirely zero, not normalized nonzero emission states.

The word and sign labels are mathematical preparation data. The selected
law does not provide a native sign generator, physical randomness, an
apparatus, a clock or a repeated-source law.

## 3. Why this sign choice, and its exact uniqueness class

The declared lift class is sign coherent: one sign for every positive h
entry and one sign for every negative h entry in the entire history.
Reflection v->conjugate(v) flips epsilon_-; rotation by pi sends v->-v
and flips both signs. For any active packet the first emitted slice is
nonzero with zero mean, hence contains both signs. The two operations act
freely and transitively on its four lifts. Conditional invariance therefore
forces the uniform law on these four histories. Four is the minimum
conditional support under this symmetry. Sign coherence is an adopted
restriction; symmetry alone does not force it among all square-root laws.

This choice retains reflection and double-cover symmetry with just two
persistent binary labels instead of an independent sign field over time.
It is a reason for the selection, not a global physical uniqueness theorem.
Within this class no continuous coefficient or sign bias remains.

Frame transport is explicit. For a common polarization line described by
h^(alpha)=exp(2i alpha)h, set v^(alpha)=exp(i alpha)v. Rotation transports
alpha, and reflection conjugates both fields. Redescribing the same tensor
line by (alpha,h)->(alpha+pi/2,-h) permutes the four signs and leaves the
conditional vector law unchanged. Thus this common-line FAMILY is O(2)
covariant. The marked plus-frame ensemble is not an isotropic ensemble
of polarization axes and is not spatially translation invariant. No
single-valued globally equivariant square-root section is claimed.

## 4. Complete moments, including all time pairs

Write p=(r,m), q=(s,n); a_p,b_p are the nonnegative functions above. For
every finite point list the law is one finite sum, with the SAME w and
sign pair used in all factors. This determines every joint moment, not
only equal-time marginal laws. In particular,

    E[v_p]=0,
    C_v(p,q)=E[v_p conjugate(v_q)]
            =sum_w nu(w)(a_p a_q+b_p b_q),
    P_v(p,q)=E[v_p v_q]=0.

The last equality uses source-pair reversal h->-h with equal mass, not
independence between p and q. A general product of v and conjugate(v)
is evaluated by expansion: retain exactly those terms having an even
number of a factors and an even number of b factors, multiply each b
factor by i for v or -i for conjugate(v), then average over w. This is
the complete non-Gaussian moment rule, including fourth moments.

Let C_Phi=E[Phi Phi^T]. Then

    C_Phi=(d1 d1^T+d2 d2^T)/6+(d1+d2)(d1+d2)^T/3,
    E[h_m]=0,
    C_h(m,n)=A_m C_Phi A_n^T.

C_Phi has nonzero eigenvalues 5/12 and 1/12. The full outgoing tensor
history has covariance rank two on every finite prefix containing m=2;
its single-slice covariance has rank two at each m>=2. The fourth-order
contractions of v consumed by the registered square are precisely

    E[v_p^2 conjugate(v_q^2)]=E[v_p^2 v_q^2]=C_h(p,q).

The finite atomic state supplies the missing fourth moments directly.
It does not invoke Gaussian or Wick closure. Fourier-space covariance
and pseudo-covariance are the full transforms F C_v F^dagger and
F P_v F^T; off-diagonal Fourier entries are retained. Diagonal powers
alone would not specify this nonstationary, nonhomogeneous state.

## 5. Action and normalization

Retain the full constrained quadratic tensor action and its source from
Canon section 14, with lambda=216*pi. On the TT representative its free
part is

    S_T=(1/(4 lambda)) sum_m
        [||Delta h_m||^2-<h_m,L h_m>].

For two real tensor components sum both copies. The canonical tensor
coordinate is q_T=h/sqrt(2 lambda), giving coefficient 1/2 in its
quadratic free action. The matching square-root coordinate would be
v_can=v/(2 lambda)^(1/4), so v_can^2=q_T. These are explicit inherited
normalization conventions, not an SI calibration.

The vector is a selected readout of the primary h solution. Variation
of S_T[v^2] alone is NOT its evolution law: the Jacobian of v->v^2
vanishes at v=0 and loses the h field equation there. In particular the
silent zero vector can be stationary for the pulled-back action even
when the primary equation has a nonzero impulse. This probe neither
repairs that singular variational theory nor uses it to claim emission.
The complete selected dynamics is the h recurrence plus the persistent
root prescription, with the initial atom specified.

## 6. A selected finite comparison, fully separated from cosmological r_T

Define the composite intensity

    s_m(r)=|v_m(r)|^2=|h_m(r)|,
    q_I=s/sqrt(2 lambda),
    F_kr=zeta_5^(kr)/sqrt(5).

The coefficient one is an additional comparison choice. Applying the same
canonical vector scaling gives v_can^2=q_T and |v_can|^2=q_I, so their
common power factor follows within that chosen square/norm comparison.
s is an O(2)-invariant quadratic scalar of v. It is
not the cosmological curvature perturbation zeta, the trace of the TT
metric, or an independently evolved breathing field. No scalar action
or c(0)=+1 propagation is inferred for this composite intensity.

At a declared integer m, take ensemble-connected powers in ALL five
Fourier slots, without spatial or time averaging:

    T_k(m)=E[|(Fh_m)_k-E(Fh_m)_k|^2],
    I_k(m)=E[|(Fs_m)_k-E(Fs_m)_k|^2],
    P_T^fin=T_k/(2 lambda),  P_I^fin=I_k/(2 lambda),
    R_TI(k,m)=T_k(m)/I_k(m) when I_k(m)>0.

At every m>=2 all I_k are strictly positive, T_0=0, and all nonzero-mode
T_k are strictly positive. Thus R_TI is defined in every slot for every
such counter. At m=0,1 both powers vanish; the ratio is UNDEFINED, not
zero. Every later value is exactly computable in Q(sqrt(5)) from the
unchanged rational recurrence and the ten-word sum. These are finite
character labels and counters, not cosmological wave numbers and epochs.

At the first emitted slice the analytically determined values are:

| k | T_k(2) | I_k(2) | R_TI(k,2) |
|---|---|---|---|
| 0 | 0 | 2/15 | 0 |
| 1,4 | (3+sqrt(5))/24 | (7-2sqrt(5))/240 | 10(31+13sqrt(5))/29 |
| 2,3 | (3-sqrt(5))/24 | (7+2sqrt(5))/240 | 10(31-13sqrt(5))/29 |

The sums are sum_k T_k=1/2 and sum_k I_k=1/4. Although s^2=|h|^2
pointwise equates TOTAL RAW powers, the coherent mean of s is nonzero;
subtracting that mean changes the connected comparison. No coefficient
is adjusted to reduce or match these derived ratios.

## 7. Choice ledger and remaining owner

| Input | Selection and reason | Boundary |
|---|---|---|
| Inherited K1 data | Unit two-site source, ten-word law, plus frame, isolated impulse, planar L and complete transfer | Retains all earlier adopted assumptions; no new derivation from J |
| CH-TT-ROOT-COHERENCE | One root sign shared on each sign sector for the whole packet | A restricted economical lift class, not all admissible vector states |
| CH-TT-DECK-LAW | Reflection/halfturn-invariant conditional law, independent of w | Uniform four-state law follows within that class; no physical generator supplied |
| CH-TT-INTENSITY-COMPARISON | s=|v|^2, coefficient one and common canonical scale | Fully declared finite composite comparison; not a primordial scalar law |

The mathematical state is complete: source, all-counter evolution, root
law, all joint moments, action convention, Fourier comparison and zero
cases are supplied. This closes the outgoing-state construction task
within the selected theory. It does not close
TT-VECTOR-STATE-NORMALIZATION's full physical decision by relabelling
R_TI as r_T. That owner retains the scalar physical carrier/action,
tensor-to-scalar unit relation, physical coordinate/epoch/mode matching
and the required typed physical reading gates. No new open registry row
is needed for work already owned there.

Any later physical adoption must assess separately a proposed
GATE-L1-L4-SELECTED-TT-STATE (carrier and support),
GATE-L4-L5-SELECTED-TT-READOUT (clock, context and readout), and
GATE-L5-L6-SELECTED-TT-COMPARISON (ensemble and physical power law).
All are PROPOSED and UNPASSED, not registry additions. This probe stays
at L1. It changes no Canon file and supplies no experiment, apparatus,
nonlinear geometry, energy scale or repeated-source occurrence law.
