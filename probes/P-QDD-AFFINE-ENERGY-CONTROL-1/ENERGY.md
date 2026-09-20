# Conserved-energy boundary for the entrance and affine routing

**PUBLIC; candidate-T, L1, NON-CANONICAL.** This is a conditional theorem
about an explicitly specified quantum implementation class. It does not
assign physical energy levels to native coordinates, identify their
mathematical amplitudes with physical preparations, or assert that the
class contains every physical apparatus. No physical law is added to the
Canon by this note.

There are two different comparison domains:

1. The entrance conclusion in Section 3 requires agreement only on the
   four-dimensional prepared code. It applies to any implementation of
   that code target in the declared conserved-energy class, regardless of
   its decomposition into intermediate operations.
2. The conclusion for `B` in Section 4 requires implementation of its
   entire six-coordinate permutation, on all `5^6` basis states with a
   common clean environment. It allows more general local spectra but
   requires agreement on a larger target domain. The entrance
   contract does **not** demand this global implementation of `B`.

## 1. The independently stated comparison class

Let `H_S` be a finite-dimensional system Hamiltonian. Let `H_E` be an
arbitrary self-adjoint environment Hamiltonian; the environment Hilbert
space may be infinite-dimensional and `H_E` may be unbounded. The
environment includes all controllers, work stores, clocks and other
resources whose states participate in the proposed operation. At the
comparison boundaries the specified conserved observable is

```math
H_0=H_S\otimes I_E+I_S\otimes H_E.
```

An admitted complete operation is a unitary `V` which conserves this
observable in the strong, domain-independent form

```math
V e^{itH_0}=e^{itH_0}V\qquad(t\in\mathbb R).                 \tag{E1}
```

Here `t` is the real parameter of the characteristic function of energy,
not an assertion about the physical duration of the operation. Writing
the bounded exponential identity avoids an undefined commutator on an
unbounded-operator domain.

The initial environment is one fixed normalized state, independent of
the unknown code input. A *clean coherent implementation* of an isometry
`T` on a code `K` means, initially for pure environments,

```math
V(\psi\otimes\eta_{\rm in})
   =T\psi\otimes\eta_{\rm out}\qquad(\psi\in K),             \tag{E2}
```

with one normalized output environment independent of `psi`. A common
overall phase can be absorbed in `eta_out`. The output environment need
not equal the input environment: a fixed resource may be consumed. The
condition also holds after tensoring with an arbitrary untouched
reference. Equality of the four classical output populations alone is
not (E2).

For a mixed initial environment, use a fixed density operator of trace
one and include its purification in the comparison, as justified in
Section 2. No finite mean energy, finite variance, finite spectrum or
energy eigenstate preparation is required.

This defines a complete conditional class of additive-energy-conserving
operations. It can describe a closed autonomous implementation when its
actual complete dynamics satisfies (E1), but autonomy alone is not enough:
a time-independent Hamiltonian conserves its own total Hamiltonian,
which need not be the stipulated additive `H_0`. An unaccounted change in
interaction energy does not satisfy this definition merely because the
microscopic dynamics is autonomous. Any such energy and its carrier must
be specified in a different or enlarged comparison.

An externally prescribed pulse on the checkpoint is not, by itself, an
implementation in this class. Its source can provide work and phase
control. To compare a pulse implementation with (E1)--(E2), include that
source and every residual output, and establish the stated conservation
and cleanliness for the enlarged system. The note does not infer these
conditions from the existence of a finite pulse formula.

## 2. Common-environment energy-gap lemma

**Lemma.** Let `|x_i>` and `|y_i>` be orthonormal eigenvectors of `H_S`,
with real energies `E_i` and `E'_i`, respectively. Suppose (E1)--(E2)
hold with `T|x_i>=|y_i>`. Then

```math
E'_i-E_i=\kappa                                             \tag{E3}
```

is one constant independent of `i`.

The same conclusion holds if specified phases multiply the individual
`|y_i>`; those phases disappear from the energy characteristic functions.
To implement a specified coherent target the phases must, in addition,
agree with that target.

**Proof.** Define

```math
\chi_{\rm in}(t)
   =\langle\eta_{\rm in},e^{itH_E}\eta_{\rm in}\rangle,
\qquad
\chi_{\rm out}(t)
   =\langle\eta_{\rm out},e^{itH_E}\eta_{\rm out}\rangle.
```

These functions are continuous and equal one at zero. This follows from
strong continuity of the unitary group and normalization; their
derivatives and energy moments need not exist. Conservation and the
product input/output in (E2) give, for every real `t`,

```math
e^{itE_i}\chi_{\rm in}(t)
   =e^{itE'_i}\chi_{\rm out}(t).                            \tag{E4}
```

Continuity supplies an open interval about zero on which
`chi_out(t)` is nonzero. For two labels `i,j`, dividing (E4) on this
interval gives

```math
e^{it(E'_i-E_i)}=e^{it(E'_j-E_j)}.
```

An exponential of a real nonzero linear function of `t` cannot equal
one on an interval. Hence (E3) follows. This argument applies even when
neither environment state has finite expected energy. In particular,
allowing a normalizable infinite-dimensional work store does not by
itself evade the lemma. An improper, nonnormalizable state is not an
admitted preparation. QED.

### Mixed preparations and coherent equality

Let the initial environment be a normalized density operator `rho_E`.
Choose a purification `|eta_in>` on `E tensor R`, give the reference `R`
the zero Hamiltonian, and let the operation on it be the identity. The
enlarged operation `V tensor I_R` conserves

```math
H_S\otimes I_{ER}+I_S\otimes H_E\otimes I_R.
```

Suppose that, with this fixed preparation, the reduced system channel is
exactly `rho -> T rho T^dagger` on every code operator. For each basis
vector its purified output must factor as

```math
|y_i\rangle\otimes|\eta_i\rangle,
```

because its reduced system state is pure. Preservation of the off-diagonal
matrix unit `|x_i><x_j|` then requires

```math
\langle\eta_j|\eta_i\rangle=1.
```

The normalized vectors `eta_i` are therefore identical. This proves (E2)
on the whole code for the enlarged environment, so the lemma applies.
The argument is not available if only the basis populations are correct
or if fine source information may remain in a discarded environment.
Pre-existing source-dependent correlations are also outside the fixed
independent-preparation premise.

The lemma permits a common nonzero energy transfer to or from a resource.
It excludes different transfers for different code labels when the
complete resource output is required to be common. It does not claim
that a common transfer is sufficient for the desired physical process.

## 3. Entrance obstruction already on the four-point code

Use the mathematical checkpoint carrier

```math
\mathcal H_S=(\mathbb C^5)^{\otimes6},\qquad
x=(a,b,c,d,q,r)\in\mathbb F_5^6.
```

For this conditional energy encoding, the basis representative of a field
element is the ordinary integer in `{0,1,2,3,4}`. Define the number
operator `N|j>=j|j>`. A field sum is still reduced modulo five, while an
energy sum below is an ordinary real sum. The distinction matters at a
wrap from level zero to level four.

The accepted code and entrance target are

```math
Y_h=(h,0,0,0,1-h,0),\qquad h=1,2,3,4,
```

```math
C_3Y_h=(h,0,0,0,1-h-f(h),f(h)),\qquad
f(1)=1,\quad f(2)=f(3)=f(4)=2.                              \tag{E5}
```

All coordinates in (E5) are reduced modulo five. The public two-tick
construction has free comparison `N_(3,2)=I` on these inputs and their
displaced outputs, so its completed target is exactly (E5). The LOW label
is `h=1`; the other three basis states span HIGH. The discussion concerns
all their coherent superpositions, not four independent classical tests.

Give each coordinate the same equally spaced energy with gap `Delta>0`:

```math
H_S=\Delta(N_a+N_b+N_c+N_d+N_q+N_r).                       \tag{E6}
```

The exact port energy accounting is

| `h` | Input `(q,r)` | Output `(q,r)` | Total checkpoint energy change |
| --- | --- | --- | --- |
| 1 | `(0,0)` | `(4,1)` | `5 Delta` |
| 2 | `(4,0)` | `(2,2)` | `0` |
| 3 | `(3,0)` | `(1,2)` | `0` |
| 4 | `(2,0)` | `(0,2)` | `0` |

The source coordinates are restored, so they contribute zero to these
differences. The energy-gap lemma therefore gives

```math
\boxed{\text{No operation satisfying (E1)--(E2) realizes (E5)
under the encoding (E6).}}                                \tag{E7}
```

This excludes the **whole** declared energy-conserving clean class for
this encoding, including arbitrary admissible intermediate interactions,
arbitrary duration and arbitrary normalizable controller or environment.
It does not merely exclude the displayed affine decomposition.

This conclusion uses coherence between LOW and HIGH as required by the
entrance target, not only coherence among the three HIGH vectors. Their
three energy changes already agree. An operation allowed to leave a
LOW/HIGH-distinguishing environment is a different target and is not
excluded by this particular common-environment argument.

It does not assign (E6) to TWIST-J. In particular, the native preservation
of `q+r` modulo five does not imply preservation of the real energy in
(E6). There is no canonical identification of these field labels with an
equally spaced material energy spectrum.

### Unequal gaps: a necessary-condition escape

Keep the source energies arbitrary and diagonal, and give only the port
coordinates equally spaced spectra with independently chosen gaps:

```math
H_S=H_{abcd}+\Delta_q N_q+\Delta_r N_r.
```

Because the source point is unchanged, the four differences are

```math
\Delta E_1=4\Delta_q+\Delta_r,\qquad
\Delta E_2=\Delta E_3=\Delta E_4=-2\Delta_q+2\Delta_r.
```

They are common exactly when

```math
\boxed{\Delta_r=6\Delta_q},\qquad
\kappa=10\Delta_q.                                       \tag{E8}
```

Thus the equal-gap contradiction is not independent of energy encoding.
For positive unequal gaps satisfying (E8), this particular necessary
condition no longer excludes the code target. A common resource energy
loss of `10 Delta_q` would still have to be accounted for. Equation (E8)
does **not** construct an admissible interaction, prove a resource with
the needed spectrum exists, establish its preparation, or supply native
timing or the physical dictionary. It is not a positive realization and
does not select those gaps physically.

## 4. Global `B` excludes every nontrivial additive diagonal energy

This section concerns the exact permutation `B` on the entire checkpoint
basis, not merely its four inputs in the accepted entrance protocol.
Write `B(x)=Mx+b` over `F5`, where

```math
M=\begin{pmatrix}
1&1&3&0&0&1\\
3&0&3&0&0&3\\
4&0&0&0&0&2\\
4&0&2&1&0&1\\
0&0&4&0&1&0\\
3&0&3&0&0&4
\end{pmatrix},\qquad
b=(3,0,3,0,0,3)^T.                                      \tag{E9}
```

For completeness, its output `(A0,B0,C0,D0,Q0,R0)` has the unique
preimage, with all operations in `F5`,

```text
r = R0-B0-3,
a = 4(C0-3-2r),
c = 2B0-a-r,
b = A0-3-a-3c-r,
d = D0-4a-2c-r,
q = Q0-4c.
```

The coordinate named `b` in this inverse is distinct from the translation
vector in (E9). These equations prove invertibility directly.

Consider **arbitrary** real local energy profiles, without an
equally-spaced assumption:

```math
E(x)=\sum_{i=1}^{6}e_i(x_i),\qquad
H_S=\sum_{x\in\mathbb F_5^6} E(x)|x\rangle\langle x|.       \tag{E10}
```

Suppose (E1)--(E2) implements `|x> -> |Bx>` for every `x`, using the same
initial and common final environment. By the lemma,

```math
E(Bx)-E(x)=\kappa\qquad\text{for every }x.                  \tag{E11}
```

Since `B` permutes a finite set, summing (E11) over that set gives
`5^6 kappa=0` as a real equality. Hence `kappa=0` and `E composed with B=E`.

Let `zeta=exp(2 pi i/5)`. Expand each function on `F5` in its finite
Fourier series:

```math
e_i(u)=\sum_{k\in\mathbb F_5}c_{i,k}\zeta^{ku}.
```

The nonconstant frequencies of `E(x)` lie on the six coordinate axes

```math
\{k e_i:1\le i\le6,\ k\in\mathbb F_5^\times\}
   \subset\mathbb F_5^6.                                 \tag{E12}
```

If `m_i` denotes row `i` of `M`, then

```math
E(Bx)=\sum_{i,k}c_{i,k}\zeta^{k b_i}\zeta^{k m_i\cdot x}.
```

Its corresponding nonconstant frequencies are `k m_i`. Every displayed
row in (E9) has at least two nonzero coordinates, so none of these
frequencies lies on a coordinate axis. Also, two different rows cannot
be proportional: that would contradict invertibility of `M`. Therefore
the 24 frequencies `k m_i` are distinct, and none lies in (E12).

Finite Fourier characters are linearly independent. In `E(Bx)=E(x)`,
the coefficient of each such non-axis frequency must therefore vanish:

```math
c_{i,k}\zeta^{k b_i}=0\qquad(k\ne0).
```

The phase factor is nonzero, so every `c_(i,k)` with `k!=0` vanishes.
Each local energy profile `e_i` is constant. We have proved

```math
\boxed{\text{A globally clean conserved-energy implementation of }B
\text{ with (E10) requires all six local spectra to be flat.}} \tag{E13}
```

This conclusion is independent of the spacings, ordering, signs or
degeneracies of the real local levels. Flat local spectra remove this
energy obstruction; they do not supply the coupling or control.

An interacting, nonadditive checkpoint Hamiltonian is outside (E10).
A code-only realization is also outside the global hypothesis of this
section. In particular, the unequal-gap escape in (E8) is consistent with
(E13): the former concerns four code vectors, whereas the latter demands
all `5^6` transitions of `B`. A physical entrance may agree with the
four-point target without implementing `B` elsewhere or even using `B` as
an intermediate operation.

## 5. What this decides and what it leaves open

| Question | Exact result and scope |
| --- | --- |
| Clean entrance on the four-point code, equal positive local gaps, complete additive-energy conservation | Impossible in the entire class (E1)--(E2), by the unequal four energy changes. |
| The same code with independent equally spaced port gaps | A necessary condition is `Delta_r=6 Delta_q`; it is not a realization. |
| Global clean permutation `B`, arbitrary additive diagonal local energies | Impossible unless all local spectra are flat. |
| Externally prescribed finite pulses for affine maps | Their mathematical existence is not contradicted; their work and control sources must be included before applying the closed-class theorem. |
| Physical origin of affine routing in native TWIST-J | Not established by these results; the carrier, energy assignment, independently available coupling and time law remain physical obligations. |

The conclusions do not identify an empty family of every physical
apparatus, adopt a new energy encoding, or close
`QDD-INSTRUMENT-APPARATUS`. They separate an actual resource constraint
from the formal fact that a point permutation has a unitary matrix.

## 6. Source and authority boundary

The four-point entrance target, `B`, its inverse and the two-native-tick
comparison are taken from the accepted
[native routing proof](../P-QDD-ENTRANCE-NONLINEAR-RESOURCE-1/NATIVE-ROUTING.md).
The requirement to compare every code amplitude, retain all resources
and distinguish code agreement from physical admission is the existing
[entrance contract](../P-QDD-UNINTERRUPTED-RECORD-1/ENTRANCE-CONTRACT.md).
The conserved observable and energy encodings in this note are explicit
conditional comparison premises. They are not entries silently added to
the physical dictionary or the Canon.
