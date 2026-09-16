# K1: one finite TM source-to-doublet map

**NON-CANONICAL / PROPOSED DEFINITION / ANALYTIC DERIVATION / NO FORMAL RUN.**
Date: 2026-09-08. Basis: Public Canon v81,
`82d536a71025032d6dd4093db61ecb9f31990250`.
Owner: `TT-VECTOR-STATE-NORMALIZATION [O]`, unchanged.

This is one fully specified candidate, with a ten-element source, five
Fourier slots and two overlapping native window positions. Its source law,
doublet amplitude and consumed first/fourth-order contractions are given
below. It is a mathematical reading proposal, not a physical state law,
action normalization, tensor spectrum or numerical `r_T(k)`. No second
candidate is introduced or compared. No numerical or formal scientific
execution supplies any statement in this note.

## 1. The map, in one formula

Let `z=exp(2*pi*i/5)` in the principal complex embedding. The source is a
four-bit Thue-Morse factor `w=(b_0,b_1,b_2,b_3)` with the exact law in
section 2. For `x in Z/5` and `t in {0,1}`, define

```text
u_t(w) = b_(t+2) - b_t in {-1,0,1},
B_x = (1+z^x)/sqrt(10),
v(w,x,t) = B_x z^(x u_t(w)),
V(w,x,t) = (Re v(w,x,t), Im v(w,x,t)) in R^2.
```

This total function is **K1 in this note**. Powers use residue classes mod 5;
`sqrt(10)` is the positive real root. The exact value field is contained in
`Q(z,i,sqrt(10))`, with real components selected by complex conjugation.
There are no adjustable coefficients, randomized updates or undefined
branches in this map.

The choice `u_t=omega(b_t,b_(t+1),b_(t+2))` uses the exact orientation function
`omega(a,b,c)=c-a` already frozen by `DEF-TM-SYM2-ORIENTATION-SOURCE`.
**Using that orientation as the monomial translation label is a new proposed
dictionary choice.** The public one-dimensional anti-invariant sector
motivates this choice but does not uniquely derive this map or its physical
meaning. No `C_sel -> Q_word` map, selector representative or enlarged gauge
is introduced. The formula consumes only the word projection; other typed
source records, if supplied, remain context and are not identified with it.

Here `x` is a character/Fourier-slot label on the finite coefficient group.
It is not a spatial position, SI distance or cosmological wave number.
Here `t=0,1` selects the first or second length-three window in one source
word; it is not a physical duration, an independently resampled preparation
or an arbitrary later time. In a native occurrence beginning at counter `n`,
these are the windows beginning at `n` and `n+1`. No continuation past this
two-position domain is defined by this finite candidate.

## 2. One complete native finite source law

Use the mathematical stationary factor frequencies of the native
`theta_n=s_2(n) mod 2` stream. The public L5 input is the uniform law on

```text
W3 = {001,010,011,100,101,110},       f_3(w)=1/6.
```

This is the stationary **word** law imported by
`TM-SYM2-PROJECTIVE-FOURFOLD [T]` and used explicitly in
[the Born-halving preregistration, sections 2.1 and 3](../probes/P-TM-SYM2-BORN-HALVING-1/PREREG.md).
It is not imported as the L6 six-line measure `mu_B` and is not assumed to
be a physical preparation ensemble for TT.

The required two-window source law follows from this input and the native
substitution identities

```text
theta_(2n)=theta_n,       theta_(2n+1)=1-theta_n.
```

Marginalizing `f_3` gives the pair probabilities
`f_2(00)=f_2(11)=1/6` and `f_2(01)=f_2(10)=1/3`.
At an even starting index a length-four factor is
`(a,1-a,b,1-b)`; at an odd starting index it is `(1-a,b,1-b,c)`.
The two index classes each have asymptotic weight `1/2`. Applying the pair
law in the first case and the triple law in the second gives exactly:

| Source word `w` | Probability `nu(w)` | `(u_0,u_1)` |
| --- | --- | --- |
| `0010` | `1/12` | `(1,0)` |
| `0011` | `1/12` | `(1,1)` |
| `0100` | `1/12` | `(0,-1)` |
| `0101` | `1/12` | `(0,0)` |
| `0110` | `1/6` | `(1,-1)` |
| `1001` | `1/6` | `(-1,1)` |
| `1010` | `1/12` | `(0,0)` |
| `1011` | `1/12` | `(0,1)` |
| `1100` | `1/12` | `(-1,-1)` |
| `1101` | `1/12` | `(-1,0)` |

For completeness, the even-index images are `0101,0110,1001,1010`, with
weights `1/12,1/6,1/6,1/12`. The six odd-index images are
`1011,1100,1101,0010,0011,0100`, each with weight `1/12`. They are disjoint
and sum to one, so the table gives the full length-four source law rather
than a selection from an inspected outcome set. Both length-three window
marginals equal `f_3`.

Equivalently, in row and column order `(-1,0,1)`, the law actually consumed
by the map is

```text
Law(u_0,u_1) = (1/12) [[1,1,2],
                           [1,2,1],
                           [2,1,1]].
```

Each marginal is uniform on three values; the pair is not independent.
For example, `Pr(u_0=-1,u_1=1)=1/6`, not the marginal product `1/9`.
This joint law comes from overlapping native windows. It is not an iid
extension of `f_3`, a newly chosen Markov chain or a temporal law inferred
from a one-time Born distribution.

## 3. Amplitude provenance: an explicit normalization convention

To avoid confusing the monomial coefficient vector with the doublet, denote
the former by

```text
a_u = delta_u + delta_(u+1) in R^(Z/5),
norm(a_u)^2 = 2,
F(a)_x = sum_r a_r z^(rx),       F_unitary = F/sqrt(5).
```

K1 first gives the coefficient vector unit Euclidean norm and then applies
the unitary finite Fourier transform:

```text
v(w,x,t) = [F_unitary(a_(u_t)/sqrt(2))]_x.
```

This is exactly the formula in section 1. The two factors in `sqrt(10)`
are therefore **two nonzero coefficient entries** and **five Fourier
characters**. Normalized coefficient squares are `(1/2,1/2)` by direct
calculation; they are not extra source probabilities assigned to `w`.
Finite Fourier orthogonality gives, for every source and both times,

```text
sum_x |v(w,x,t)|^2 = 1,
|v(w,x,t)|^2 = (2+z^x+z^(-x))/10.
```

All five slots are retained. The `x=0` slot is `2/sqrt(10)`, separately
from the four Galois slots. For `x!=0`, the numerator `1+z^x` equals
`sigma_(3x)(J)`, using the registered monomial-lift identity. No slot is
dropped, reweighted or chosen to improve a tensor prediction.

Unit coefficient norm followed by unitary Fourier is the **proposed K1
dimensionless normalization**, not a theorem deriving the physical action
or identifying its unit with a scalar perturbation unit. The public
TM-SYM2 dictionary fixes its own monomial-lift reading; it does not already
adopt this normalization for TT. Thus the numerical scale of this finite
map is completely specified, while its physical use still needs a justified
identification. In particular this convention cannot justify a cancellation
of an unknown physical amplitude against the scalar sector.

## 4. Closed analytic formulas for the consumed moments

All expectations in this section use the ten-point law `nu`. Define

```text
f(m) = (z^(-m)+1+z^m)/3,

g(m,n) = (1/12) [z^(-m-n) + z^(-m) + 2 z^(-m+n)
                         + z^(-n) + 2 + z^n
                         + 2 z^(m-n) + z^m + z^(m+n)],

D_ts(m,n) = f(m+n)     if t=s,
            g(m,n)     if t!=s,       t,s in {0,1}.
```

The joint table immediately gives
`E[z^(m u_t+n u_s)]=D_ts(m,n)` and `E[z^(m u_t)]=f(m)`.
For `t=1,s=0`, the same formula applies because the joint table is symmetric.
Both `f` and `g` are real; their arguments are residues mod 5.
These finite polynomials, rather than an unspecified expectation operator,
determine every moment used below.

For the original complex doublet,

```text
E[v(x,t)] = B_x f(x),
E[v(x,t) conjugate(v(y,s))] = B_x conjugate(B_y) D_ts(x,-y),
E[v(x,t) v(y,s)] = B_x B_y D_ts(x,y).
```

Consequently its connected covariance and pseudo-covariance are obtained
by subtracting `B_x conjugate(B_y) f(x)f(y)` and
`B_x B_y f(x)f(y)`, respectively. This candidate does not assume zero mean,
`C=delta` or `P=0`.

Now use the registered square and put

```text
h(x,t) = v(x,t)^2 = A_x z^(2x u_t),       A_x = B_x^2,
q_+ = Re h,                              q_cross = Im h,
mu_h(x,t) = A_x f(2x),
mu_+(x,t) = Re(A_x) f(2x),
mu_cross(x,t) = Im(A_x) f(2x).
```

The exact **connected fourth-order contractions of the doublet** are

```text
K((x,t),(y,s)) = E[(h(x,t)-mu_h(x,t))
                        conjugate(h(y,s)-mu_h(y,s))]
 = A_x conjugate(A_y) [D_ts(2x,-2y) - f(2x) f(2y)],

L((x,t),(y,s)) = E[(h(x,t)-mu_h(x,t))(h(y,s)-mu_h(y,s))]
 = A_x A_y [D_ts(2x,2y) - f(2x) f(2y)].
```

There is no Wick substitution: these expressions follow by squaring the
explicit map and summing its explicitly supplied law. They determine the
full real covariance consumed by the plus/cross readout:

```text
Gamma_++       = (Re K + Re L)/2,
Gamma_crosscross = (Re K - Re L)/2,
Gamma_+cross   = (Im L - Im K)/2,
Gamma_cross+   = (Im L + Im K)/2.
```

Each equality follows by expanding `h=q_+ + i*q_cross` in `K` and `L`.
Together with the displayed `mu`, these formulas evaluate the contraction
from [the closure-input note](V81-TT-NORMALIZATION-CLOSURE-INPUT-1.md) for
every one of the candidate's point pairs. They cover both equal-time and
two-time readouts without a full four-independent-time tensor.

At equal time `D_tt(2x,-2y)=f(2x-2y)`. At the two distinct times it is
`g(2x,-2y)`. Thus the temporal coupling is explicit and is not silently
replaced by the product of one-time moments. At `x=0`, `h=2/5` is a coherent
constant and every covariance with that slot vanishes. At each nonzero
slot, `K((x,t),(x,t))=|A_x|^2[1-f(2x)^2]>0`: the three distinct phases have
an average of modulus less than one. The construction therefore has
nonconstant quadratic readout, even after subtracting the coherent mean.

This also proves realizability and positive semidefiniteness directly:
for every finite real coefficient family `c_(a,x,t)`, its covariance
quadratic form is
`E[(sum_(a,x,t) c_(a,x,t)(q_a(x,t)-mu_a(x,t)))^2]>=0`
under the positive ten-point law. No arbitrary moment tensor has been
declared independently of an underlying state.

## 5. Exact TT scope and the remaining physical decision

The map is compatible with the registered **algebraic** TT identities:

- `h=(v_1+i*v_2)^2` holds by definition, with
  `h_+=v_1^2-v_2^2` and `h_cross=2*v_1*v_2`.
- On nonzero ambient doublets the square has fibres `{v,-v}`. The candidate
  uses that same map; its probability support need not contain both points
  of every fibre. No sign-symmetry or rotational isotropy of the source law
  is claimed.
- For `H=[[h_+,h_cross],[h_cross,-h_+]]`,
  `det(I+H)=1-|h|^2=1-|v|^4` identically.
- Input-frame rotation doubles the output angle, and input conjugation
  fixes plus and reverses cross, as in `POL-READ`. In this candidate
  `v(-x,t)=conjugate(v(x,t))` also holds literally.

The registered label `c=1-s^2` gives `-3` for the square's spin `s=2`.
K1 changes neither that coefficient nor the registered propagation
dictionary. It does **not** identify its two window positions with physical
propagation time or assert that the resulting samples solve a cosmological
or Schwarzschild evolution equation. Algebraic compatibility is therefore
established at the displayed scope; admission as a full physical TT
normalization is not established.

The fixed-modulus non-Gaussian boundary remains intact. This map has fixed
slot modulus, but does not lie in the theorem's frozen zero-mean,
`C=delta,P=0` comparison class. Its fourth moments have been supplied
directly, so neither the six-law theorem nor a Gaussian shortcut is used to
select them. No claim is made that this one proposal exhausts admissible
normalizations.

The concrete decision now available is whether to retain **this** orientation
label, unit coefficient norm and unitary Fourier map as the K1 mathematical
candidate for a later typed physical bridge. Its finite source law and
`(mu,Gamma)` are already fixed and require no further selection. Physical
closure would have to connect this slot/time domain and dimensionless norm
to a physical action/readout and a scalar comparison in that same
convention. The existing homogeneous `CONFORMAL-PREFACTOR` and explicit
Stage B `Z_L2=1/2` do not perform that identification. If a later bridge
rescales the doublet by `a`, the supplied `mu_h` scales by `a^2` and `K,L`
by `a^4`; cancellation in `P_T/P_S` must come from that same bridge, not
from setting an unproved scalar scale equal to it.

No physical denominator, physical wave-number map or numerical tensor ratio
is manufactured here. The completed output is one explicit finite K1 map
and its entire consumed moment law. Its derivation remains in notes and
earns no new registered status; formal validation requires its own public
preregistration and verifier pin before execution.

## Sources and provenance of choices

- [Canon section 2](../canon/CANON.md): native Thue-Morse identity
  `(theta_(2m),theta_(2m+1))=(theta_m,1-theta_m)`.
- [TM-SYM2 Born-halving preregistration](../probes/P-TM-SYM2-BORN-HALVING-1/PREREG.md),
  sections 2.1, 3, 5 and 6: mathematical W3 source law, orientation function,
  and monomial coefficient lift. The finite W4 table here is derived from
  those word frequencies and substitution; no experimental data are used.
- [Canon sections 13 and 14](../canon/CANON.md): bounds of
  `TM-SYM2-PHYSICAL-MEASURE`, `TT-SQUARING-DECODER`, `POL-READ`,
  `TT-QUADRATIC-GERM` and `TT-VECTOR-MOMENT-UNDERDETERMINATION`.
- New proposed choices, explicitly confined to this note: translate the
  monomial by `omega`; give its coefficient vector unit Euclidean norm;
  take its unitary Fourier coefficients as the real TT doublet; retain all
  five slots at the two overlapping positions. The moment values follow
  from these choices; physical necessity of the choices does not.
