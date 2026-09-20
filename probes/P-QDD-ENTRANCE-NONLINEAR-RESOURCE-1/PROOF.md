# Entrance obstruction and the missing source-sensitive resource

**PUBLIC; candidate-T, L1, NON-CANONICAL.** This is a written mathematical
proof for `P-QDD-ENTRANCE-NONLINEAR-RESOURCE-1`, owned by
[#1087](https://github.com/mathorn1973/twist-j/issues/1087). It claims no
physical implementation, new native primitive, scientific execution, or
change to Public Canon v90. Execution and acceptance are recorded separately.

The comparison target is the complete coherent entrance specified in
[ENTRANCE-CONTRACT.md](../P-QDD-UNINTERRUPTED-RECORD-1/ENTRANCE-CONTRACT.md).
The accepted [uninterrupted-record proof](../P-QDD-UNINTERRUPTED-RECORD-1/PROOF.md)
supplies its code, native waiting law and reference port. Here we decide
two explicitly bounded mathematical realization classes, identify a
constant-shift positive control, and reduce the source dependence of the
target to the existing two port coordinates. The separately admitted
construction in [CONSTRUCTION.md](CONSTRUCTION.md) addresses an enlarged
resource class. Its added interactions are not consequences of the
negative theorems below.

## 1. Native maps, the prepared code and the entrance target

All checkpoint coordinates in this proof lie in `F5`. Write

\[
x=(a,b,c,d,q,r)=(p;q,r),\qquad
s(p)=a+b+c+d,\qquad z=s(p)+q+r.
\tag{1}
\]

The symbols `a,b,c,d` in `p` denote coordinates; the subscripts of the
following `g` denote generator names. The native generators are

\[
\begin{aligned}
g_a x&=(b,a,d,c,q,r),\\
g_b x&=(-c,-d,-a,-b,-q,-r),\\
g_c x&=(2-c,1-d+r,2-a,1-b-r,1-q,-r),\\
g_d x&=(2-a,1-b,3-c,4-d,1-q,1-r),\\
g_e x&=(2-a,1-b,3-c,4-d,2-q,1-r).
\end{aligned}
\tag{2}
\]

Index these maps by `0,1,2,3,4`, respectively. At driver bit `t`,

\[
F_t(x)=g_{(z(x)+2t)\bmod5}(x).
\tag{3}
\]

The actual update uses `t=theta_n`. A common binary word may be substituted
when proving a stronger algebraic statement. `N_(n,d)` denotes the actual
composition of `d` native steps beginning at counter `n`. It is not an
inverse evolution or a newly selectable physical control.

At counter three, the four endpoint basis points are

\[
Y_h=(h,0,0,0,1-h,0),\qquad h\in\{1,2,3,4\}.
\tag{4}
\]

They have common `z=1,r=0`. Their freely evolved points and code are

\[
Y_h(n)=N_{3,n-3}Y_h,\qquad
\mathcal K_n=\operatorname{span}_{\mathbb C}\{|Y_h(n)\rangle:h\ne0\},
\qquad n\ge3.
\tag{5}
\]

The ordering `(1,2,4,3)` used by the amplitude matrix in the accepted proof
does not change the point formulas here. Its invertibility means that
arbitrary source amplitudes span all of `K_n`, so each endpoint basis input
is a necessary test of the complete coherent target.

For paired displacement and the transported label, write

\[
T_\delta(p;q,r)=(p;q-\delta,r+\delta),\qquad
h_n(p)=(-1)^{n-3}s(p).
\tag{6}
\]

The admitted coarse function and entrance are

\[
f(0)=0,\quad f(1)=1,\quad f(2)=f(3)=f(4)=2,
\qquad C_nx=T_{f(h_n(p))}x.
\tag{7}
\]

With `d` native ticks elapsed, the target on the code is

\[
V_{n,d}|Y_h(n)\rangle
=|N_{n,d}C_nY_h(n)\rangle
=|T_{\varepsilon f(h)}Y_h(n+d)\rangle,
\qquad \varepsilon=(-1)^d.
\tag{8}
\]

The last equality is the accepted stable-region transport theorem. If
`r^0_(n+d)` is the common freely evolved ready port, its target `r` value is

\[
R_{n,d}(h)=r^0_{n+d}+\varepsilon f(h).
\tag{9}
\]

Equation (8) has a fixed phase convention and is required on every code
amplitude, with all retained auxiliaries accounted for. The obstructions
below already follow from the necessary point-basis requirement (9).
They therefore cannot be repaired by matching just the four populations
or by assigning endpoint-dependent phases.

## 2. A smaller autonomous native factor

Define

\[
\pi(x)=(z(x),r).
\tag{10}
\]

Summing (2) and retaining its last coordinate gives

\[
\begin{array}{c|cc}
 & z' & r'\\\hline
g_a & z & r\\
g_b & -z & -r\\
g_c & 2-z & -r\\
g_d & 2-z & 1-r\\
g_e & 3-z & 1-r
\end{array}
\tag{11}
\]

Thus every generator descends to a map `bar g_i` of `F5^2`:

\[
\pi g_i=\bar g_i\pi.
\tag{12}
\]

The selector in (3) depends only on the first coordinate of `pi`.
Consequently it too descends:

\[
\pi F_t=\bar F_t\pi,
\quad
\bar F_t(z,r)=\bar g_{(z+2t)\bmod5}(z,r).
\tag{13}
\]

These are global identities, including states outside `z in {1,4}`. The
larger autonomous quotient `(z,q,r)` is already proved in
[the native point-port proof, section 1](../P-QDD-NATIVE-POINT-PORT-CAPACITY-1/PROOF.md).
Equations (10)--(13) project that inherited quotient further; they do not
claim a new independent derivation of the native laws.

**Theorem 1: no entrance from unchanged native evolution.** For every
`n>=3`, every common driver word and every finite waiting length, all four
code inputs have the same output `(z,r)`. In particular no actual native
waiting interval realizes (8).

**Proof.** The inputs at counter three have equal `pi`. Equation (13),
applied inductively, preserves equality of `pi`, giving it also at any
launch counter `n`. Another induction covers any subsequent common word.
The required values (9) differ between `h=1` and `h=2`, since
`epsilon` is nonzero in `F5`. Equal actual `r` values cannot be both.
QED.

This obstruction is to producing the first source-dependent port
displacement. It is compatible with the accepted theorem that native
evolution preserves and transports a displacement which has already been
inserted.

## 3. Arbitrary feedback through this factor still cannot insert the mark

The following complete class is larger than unchanged native waiting.
It consists of classical deterministic or stochastic point transitions,
not coherent superpositions and interference of control programs.
Fix a launch `n`, a source-independent context and an arbitrary auxiliary
state space `A`. A controller may retain the entire past, use arbitrary
functions of that past, and have arbitrary independent seeds. Its only
source-sensitive observations are functions of the sequence of `pi`
values. At each decision it may choose any of the five generators in (2),
or choose a driver bit and apply (3), update its auxiliary state, wait, and
decide whether to stop. The common counter may also be an input. Choosing
generators directly is a relaxation of native commandability, not a
physical assertion that such controls exist.

More generally, any admitted joint primitive may be used if its projected
update obeys

\[
(\pi(x'),a')=H(\pi(x),a,\xi,n)
\tag{14}
\]

for a fixed function `H`. Its action on the other native coordinates need
not be specified to prove this theorem. All observations, decision times
and stopping decisions must have the same factor property. A fresh seed
or an entire independent process may be included in `xi`; an arbitrary
history may be included in `a`. Initial auxiliary states and seeds have
the same law for every endpoint input and may be coupled to equal values
for comparing those inputs. No hidden endpoint-dependent preparation,
clock phase or stopping input is admitted.

This is a restriction on the available **actuators as well as
observations**. Restricting observations alone would be insufficient: a
fixed command to an already supplied `C_n` would insert the mark without
any controller measurement. Such an actuator violates (14) and is not in
the declared class.

**Theorem 2: complete factor-feedback obstruction.** No member of this
class supplies the exact entrance (8) on all four endpoint inputs at its
declared completion time, with a source-independent context and ready
preparation. This remains true with arbitrary memory, independent native
ancillas, and almost-sure finite stopping.

**Proof.** First fix the entire auxiliary input and seed. The initial
projected joint state `(pi,a)` is equal on all four inputs. By (14), the
next projected state is equal, all observations are equal, and the next
decision is equal. Induction therefore gives equal projected states and
transcripts throughout the execution. Its stopping time, if finite, is
also common. At that time the four actual `r` values agree. Equation (9)
requires two different values even when the common completion duration
depends on the fixed seed. This is a contradiction.

For a probabilistic auxiliary input, couple the four executions with the
same seed and initial auxiliary value. If a total exact witness succeeded
almost surely for each of the four endpoint inputs, the intersection of
their four success events would still have probability one. The pathwise
contradiction applies on that intersection. An execution which never
completes on a supported input is not a total entrance witness. Independent
native ancillas can be included in the seed and auxiliary state: their
evolution adds no source-sensitive observation. QED.

This is completeness for the declared factor-feedback class, not a claim
about every physical apparatus. In particular:

- `q` observation is excluded. Initially `q=1-h`, so allowing it gives
  information not contained in `pi`.
- Observation of source coordinates, a source-dependent phase or clock,
  a prepared source-correlated auxiliary, or a primitive whose projected
  update fails (14) changes the class.
- The whole pair `(q,r)` must not be confused with the restricted observed
  pair `(z,r)`. The theorem is not a prohibition of all two-port readers.
- A quantum interaction outside the declared factor description is not
  automatically covered. Its full state law and comparison require their
  own proof.

The previously registered fixed-reader permanent-no-write theorem has a
different scope. Here an entrance is excluded because its required new
source dependence cannot pass through the admitted observation/control
factor, even for a finite write. No new permanence or recurrence premise
is needed.

## 4. The freely transported code stays on one affine line

On `z in {1,4}`, the selector table is

\[
\begin{array}{c|c|c|c}
z&t&\text{generator}&z'\\\hline
1&0&b&4\\
1&1&d&1\\
4&0&e&4\\
4&1&b&1
\end{array}
\tag{15}
\]

All code points therefore select the same affine generator at each step
and remain on a common stable sheet. Every selected generator is an
invertible affine map of the full checkpoint. Beginning with (4), which
is the restriction of an affine line to four parameters, we obtain

\[
Y_h(n)=u_n+h v_n,\qquad h\in\mathbb F_5^*,\qquad v_n\ne0.
\tag{16}
\]

This follows by applying the same affine composition to the full initial
line `Y_h`, including its unused `h=0` point. Invertibility of that
composition gives `v_n != 0`. Its `r` coordinate and its trace coordinate
are constant along the line. On the stable sheet the source sum reverses
sign at each step, so

\[
s(p_h(n))=(-1)^{n-3}h,\qquad h_n(p_h(n))=h.
\tag{17}
\]

The equal-selector assertion is essential. A general composition of
piecewise-affine selected maps on an arbitrary line need not remain
affine on that line.

## 5. The exact minimum polynomial degree on the code

Here degree means degree of a polynomial in finite-field checkpoint
coordinates, not degree of an amplitude map or of a physical interaction
Hamiltonian. A function on `F5` has a unique representing polynomial of
degree at most four; polynomial expressions of higher degree are compared
as functions modulo `h^5-h`.

**Lemma 3.** On `h in {1,2,3,4}`, the unique polynomial of degree at most
three with values `(1,2,2,2)` is

\[
g(h)=h^3+h^2+h+3.
\tag{18}
\]

No polynomial of degree at most two has those values. Every extension to
all of `F5` with value `t` at zero has the unique reduced polynomial

\[
f_t(h)=t+h+h^2+h^3+(3-t)h^4.
\tag{19}
\]

**Proof.** Direct substitution gives the four required values in (18).
The difference between two polynomials of degree at most three with four
distinct roots is zero, proving uniqueness. The third forward difference
of the required values is

\[
f(4)-3f(3)+3f(2)-f(1)=2-6+6-1=1\quad\text{in }\mathbb F_5.
\tag{20}
\]

It vanishes for every polynomial of degree at most two, proving the lower
bound. Finally `1-h^4` is one at zero and zero at every nonzero element.
Adding `(t-3)(1-h^4)` to (18) yields (19), whose uniqueness follows from
five-point interpolation in degree at most four. QED.

The accepted global function in (7) is the case `t=0`:

\[
f(h)=3h^4+h^3+h^2+h.
\tag{21}
\]

The cubic extension has `t=3`, not zero. Thus the minimum degree on the
four-point code is three, whereas the minimum reduced degree for the
declared all-five-label function is four. These are distinct domains;
choosing the cubic extension cannot silently redefine the admitted
off-code entrance.

**Theorem 4: endpoint polynomial obstruction.** Fix `n>=3` and `d>=0`.
There is no deterministic point map whose output `r` coordinate is a
polynomial of total degree at most two in the native input coordinates and
which agrees with the entrance target on all four code points. In
particular, no affine point map agrees with that target, even if it is
chosen from a class much larger than the native generator group.

**Proof.** Substitute (16) into its output `r` polynomial. The resulting
polynomial in `h` has degree at most two. If the map met (9), subtracting
the common reference and multiplying by the nonzero `epsilon` would give
a degree-at-most-two polynomial with values `(1,2,2,2)`. This contradicts
Lemma 3. QED.

The hypothesis concerns the **complete endpoint map**, not each primitive
separately. Composing quadratic primitives can increase the endpoint
degree. Likewise, a selector can introduce nonlinear dependence after an
additional routing operation makes its input source-sensitive. Neither
possibility is ruled out by Theorem 4. The actual free code fails to use
such a selector resource because its common trace makes all branches equal.

## 6. Independent coherent ancillas do not repair a quadratic endpoint

The previous theorem has a robust extension which does not assume that an
auxiliary is in a single classical state.

Let `A` be any nonempty finite auxiliary point set and let `rho` be any
density operator on `C^A`, independent of the code input. This includes
arbitrary coherent pure states, mixtures, and purifications when all
purifying coordinates are included. Consider a global monomial unitary

\[
\mathsf M|x,a\rangle
=e^{i\chi(x,a)}|X(x,a),B(x,a)\rangle,
\tag{22}
\]

where the joint map `(x,a) -> (X(x,a),B(x,a))` is a permutation of the
complete joint point basis. The output retains all coordinates; no
noninjective point pushforward is presumed to be a physical quantum
channel. Phases in (22) may be arbitrary.

The polynomial hypothesis is only this: for each fixed `a`, the output
native `r` coordinate

\[
R_a(x)=r(X(x,a))
\tag{23}
\]

has a polynomial representation of degree at most two in the six native
input coordinates. The other output coordinates may be arbitrary.
Any globally affine permutation on native and auxiliary finite-field
coordinates has this property; a complete globally quadratic permutation
does as well. No bound on auxiliary dimension or coherence is imposed.

**Theorem 5: auxiliary-independent quadratic obstruction.** No map (22)
under hypothesis (23), with any independent `rho`, has the exact native
entrance output (8) for every endpoint basis input. Consequently it cannot
satisfy the full clean coherent entrance contract, even if arbitrary
source-dependent residual auxiliary states were allowed instead of the
clean common one.

**Proof.** Fix an endpoint input `x_h=Y_h(n)`. Let `P_bad(h)` be the
diagonal projector onto all joint output basis points whose native `r`
coordinate differs from (9). A monomial unitary takes a diagonal projector
to a diagonal projector under conjugation: phases cancel, and the
permutation simply relabels its selected basis points. Therefore

\[
\begin{aligned}
&\operatorname{Tr}\!\left[
 P_{\rm bad}(h)\mathsf M
 (|x_h\rangle\langle x_h|\otimes\rho)
 \mathsf M^\dagger\right]\\
&\hspace{1cm}=
\sum_{a\in A}\rho_{aa}\cdot
\mathbf1_{\{R_a(x_h)\ne R_{n,d}(h)\}}.
\end{aligned}
\tag{24}
\]

In particular off-diagonal auxiliary coherences cannot cancel a wrong
`r` output in this class. Exact realization makes (24) zero for each of
the four values of `h`. Every summand is nonnegative. Since
`sum_a rho_aa=1`, choose one `a_0` with `rho_(a_0 a_0)>0`. For that same
auxiliary point and every `h`, it follows that

\[
R_{a_0}(Y_h(n))=r^0_{n+d}+\varepsilon f(h).
\tag{25}
\]

Hypothesis (23) and (16) make the left side a polynomial of degree at
most two in `h`, contradicting Theorem 4. QED.

The theorem is unchanged by arbitrary source-independent classical
mixtures of such maps. The wrong-output probabilities remain
nonnegative, and exactness on the four basis inputs selects a common
full-measure set of successful classical branches; any one such branch
would contradict the theorem. A claim of almost-sure exact realization
cannot replace a failed branch with a source-dependent one.

The stronger clean requirement of a common residual auxiliary and a
common phase is not needed for this impossibility. Conversely, the
theorem does not classify arbitrary nonmonomial quantum channels,
interfering sums of different point maps, postselected measurements with
source-sensitive controls, or noninjective linear extensions of point
maps. Adding those resources changes the class and needs its own complete
state accounting. A composition of monomial gates is monomial, but its
endpoint degree must still satisfy (23) for this theorem to apply.

## 7. Constant paired shifts already occur in the commanded word algebra

It would be incorrect to infer that the affine generator group cannot
produce a nonzero paired displacement at all. Composition is written
right to left. From (2), `g_d^2=I` and

\[
Q=g_e g_d:
  (p;q,r)\longmapsto(p;q+1,r).
\tag{26}
\]

Also

\[
g_dg_b(p;q,r)
=((c+2,d+1,a+3,b+4);q+1,r+1).
\tag{27}
\]

Applying this map twice adds `(2,1,3,4)+(3,4,2,1)=0` to the source and
adds two to each port coordinate. Thus

\[
D=(g_dg_b)^2:
 (p;q,r)\longmapsto(p;q+2,r+2).
\tag{28}
\]

Combining (26)--(28), and cancelling the adjacent `g_d^2`, gives

\[
\boxed{T_2=QD=g_e g_b g_d g_b.}
\tag{29}
\]

The actual application order of this commanded word is `b,d,b,e`. Since
two generates the additive group of `F5`, its powers give every constant
paired displacement:

\[
T_\delta=(T_2)^{\,3\delta\bmod5}.
\tag{30}
\]

This is an all-state affine identity and a positive control for the
obstructions. No enumeration of finite word lengths is needed. It shows
that individual constant displacements are available in the commanded
generator algebra. A common word still produces a common displacement on
the code; it cannot supply the required dependence on `h`.

In particular (29) is not a claim that the actual selector follows
`b,d,b,e` from every prepared source at the relevant clock phase. Nor does
it prove physical commandability of the five generators. Selecting a
different power in (30) according to `h` would assume the source-sensitive
control resource whose origin is being investigated.

## 8. The needed source label is already encoded in the port pair

The missing control must not be confused with missing information. From
the definition of `z`, identically on every native point,

\[
s(p)=z-q-r,
\qquad h_n(p)=(-1)^{n-3}(z-q-r).
\tag{31}
\]

On a selected stable sheet with known common `z_n`, this gives the exact
two-port expression

\[
h_n=(-1)^{n-3}(z_n-q-r).
\tag{32}
\]

Both `q+r` and `z` are preserved by every paired shift `T_delta`.
Therefore a controlled paired translation using (32) does not change its
own control label. With `b_0=q+r`, the intended entrance has the reduced
form

\[
(b_0,r)\longmapsto
\left(b_0, r+f\bigl((-1)^{n-3}(z_n-b_0)\bigr)\right),
\tag{33}
\]

and the original `q` is recovered as `b_0-r`. This is a reversible shear
on the two-port coordinates at fixed `z_n`; its inverse subtracts the same
function because `b_0` is unchanged. The conservation of `q+r` asserted
here is under the entrance shear, not under arbitrary native waiting.
The reference `z_n` and the sign are declared context/counter inputs.

For the code, (17) and (31) show that (33) applies exactly the LOW/HIGH
function in (7). Thus information sufficient to control the mark is
already present in `q,r` together with the common trace and counter. No
new independent value of `h` must be loaded. At counter three the
simpler relation is `h=1-q`, since `r=0`.

Equation (33) is a target reduction, not its implementation. To treat it
as a physical entrance one must justify an interaction which actually
uses that information to change `r` with the stated coarse dependence,
while preserving all required coherent amplitudes and owning every
auxiliary output. Writing the shear as a new elementary gate would merely
restate the target. Theorems 2 and 5 show exactly why the two bounded
resource classes above do not supply it.

## 9. The conserved pair and translation covariance do not select a write

For a target-independent mathematical comparison, consider the complete
class of permutations `V` of the two-port space `F5^2` satisfying only

\[
q'+r'=q+r,\qquad VT_\delta=T_\delta V
\quad\text{for every }\delta\in\mathbb F_5.
\tag{34}
\]

These conditions are stated without reference to LOW, HIGH or the target
function `f`. They do not assert that every such permutation is a
physically admitted operation. We classify this mathematical class to
test what those two structural conditions alone imply.

**Theorem 6: complete shear class and nonselection.** Every permutation
in (34), and only those permutations, has the form

\[
V_k(b_0,r)=(b_0,r+k(b_0)),\qquad b_0=q+r,
\tag{35}
\]

where `k:F5->F5` is arbitrary. There are exactly `5^5=3125` such maps.

**Proof.** Conservation of `b_0` makes the map on its fibre
`(b_0,r) -> (b_0,v_(b_0)(r))`. Paired translation becomes
`(b_0,r) -> (b_0,r+delta)`. Commutation is therefore the identity

\[
v_{b_0}(r+\delta)=v_{b_0}(r)+\delta.
\tag{36}
\]

Set `r=0` and define `k(b_0)=v_(b_0)(0)`. This gives (35) at every `r`.
Conversely each map (35) is a permutation, with inverse obtained by
subtracting `k`, and plainly satisfies both conditions in (34). The five
values of `k` are independent and each has five choices. QED.

Identity (`k=0`), constant shifts, fine label-dependent shifts and coarse
shifts all belong to this class. The target at fixed context `n,z_n`
corresponds to

\[
k_{n,z_n}(b_0)=f\bigl((-1)^{n-3}(z_n-b_0)\bigr).
\tag{37}
\]

Thus conservation and translation covariance do not force the desired
coarse interaction. They admit it alongside 3124 other maps. The
four-point code fixes four values of `k`; by itself it leaves five
possible values on the remaining fibre. The separately declared
`f(0)=0` fixes that fifth value for the accepted global extension. Neither
the structural conditions nor agreement on the code derives that choice.

This is an exact mathematical nonselection statement about (34). It is
not a classification of all physically admissible apparatuses or a
replacement for their independently justified primitive family.

## 10. Meaning and limits of the result

The mathematical conclusions concern the complete declared classes:

1. An arbitrary controller which accesses the source only through the
   native factor `(z,r)` cannot create the entrance mark, even with
   arbitrary independent memory, seeds and stopping.
2. A complete endpoint map with output `r` of degree at most two cannot
   realize the entrance on the four-point code. Global monomial
   implementations retain this obstruction with arbitrary independent
   coherent or mixed auxiliaries.
3. The code target has minimum polynomial degree three; its accepted
   all-five-label extension has degree four. Constant shifts themselves
   occur in the commanded native word algebra, and the required control
   label is recoverable from the full port pair and common context.
4. Conservation of the port sum and covariance under paired translations
   admit exactly 3125 two-port permutations and do not select the desired
   coarse write.

There is no contradiction between these statements and a construction
using additional routing, nonlinear control or nonmonomial interference.
In particular a composition of low-degree primitives may acquire the
required higher endpoint degree. The separate construction must say which
new primitive breaks which negative hypothesis, retain its auxiliaries,
and keep its mathematical resource assumption distinct from physical
admission.

No theorem here establishes that a proposed physical carrier realizes the
native checkpoint coordinates, that its controls are independently
available, that the entrance completes during a specified physical time,
or that the apparatus ceases to couple afterward. Nor does it supply the
archive exchange, archive persistence, a realized single event, an
occurrence law, preparation/reset, or a complete physical apparatus
family. These remain under `QDD-INSTRUMENT-APPARATUS [O]` and the explicit
entrance contract. No general physical impossibility or L1-to-L5 closure
is asserted.

The universal conclusions in this file follow from quotient induction,
polynomial interpolation and positivity, not from a finite trajectory
cutoff or a finite search through candidate controls. A prospective exact
verifier can audit the displayed finite identities without replacing
those arguments or expanding their scope.
