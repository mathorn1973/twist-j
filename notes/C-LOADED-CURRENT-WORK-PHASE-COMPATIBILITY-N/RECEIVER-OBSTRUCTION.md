# Fixed receivers and the unresolved character choice

**NON-CANONICAL / L1. Conditional candidate-T. Hand proofs; no scientific execution or independent acceptance.**

This additive analysis uses [FULL-FIELD-PHASE.md](FULL-FIELD-PHASE.md) at `49b2ffd7b04978bc35a2efb22b74feb6b01cf715`. Earlier sources and run records remain unchanged. Put `a_t=1+5t`, `t in Z/5`, and `zeta^5=j`. The alternative readings are `chi_t(r)=zeta^(a_t r)`, but the actual pointer law `r'=r+Gamma modulo25` is independent of `t`.

## 1. No receiver distinguishes a mere change of dictionary

**Proposition.** If preparation, complete joint dynamics and observation rules are identical for all `t`, every receiver history is identical. This includes adaptive controls and autonomous reciprocal coupling.

**Proof.** Include source, field, pointer, receiver, ancillas, retained history and controller in one state `z_n`. Equal states produce equal observations and equal next states under the fixed joint transition. Induction starts from the common preparation. Adaptivity uses the same retained history; reciprocal backreaction is already part of the joint transition. QED.

With identical initial distributions and transition kernels the same induction gives identical stochastic output laws, including stopping rules. Different hidden references, controllers or preparations fall outside the hypothesis. The result is about identical actual states, not a limitation on the ingenuity of a receiver.

At the free witness the old pointer is `r=13` and its digits are `(3,2)` for every `t`. Computing the five exponents `13,3,18,8,23` evaluates five dictionaries on that one record. It does not identify an operationally present `t`.

Actual re-encoding would instead give `r_t=a_t r` and increments `a_t Gamma`. Its high digits `2,0,3,1,4` are distinguishable by a fixed reader, but `t` has now entered the state or law. Conversely, a simultaneous coordinate change `E_t:r->a_t r`, conjugation of dynamics, transformation of preparation, and replacement of reader `D` by `D composed with E_t^-1` preserves every observation. A comparison must freeze the receiver frame independently.

## 2. An exact linear spectral obstruction over Q(j)

Set `K=Q(j)` and `L=Q(zeta)`. Cyclotomic irreducibility gives `[L:Q]=20`, `[K:Q]=4`, hence `[L:K]=5` and

    minpoly_K(zeta)=X^5-j.

For the prime-power degrees, `Phi_25(X+1)` and `Phi_5(X+1)` satisfy Eisenstein at five. See [Conrad's cyclotomic-field notes](https://math.stanford.edu/~conrad/210BPage/handouts/cyclotomic.pdf). Therefore a `K`-linear operator with a faithful twenty-fifth-root eigenvalue needs at least five coordinates. This is a linear representation bound, not a physical dimension or pointer-cost bound.

It is attained on `K^5` by

    V e_k=e_(k+1) for k<4,       V e_4=j e_0.

Here `V^5=j I`; the five complex eigenvalues are `alpha_t=zeta*j^t`. The operator contains all five, selecting none. Its commutant is the field `K[V]`: `e_0,V e_0,...,V^4 e_0` is a basis and the minimal polynomial is irreducible. Thus every nonzero commuting `K`-linear filter is invertible, and the only such projectors are `0` and `I`.

Every nonzero `K^5` vector also has nonzero projection onto all five complex eigenmodes. Write it as `P(V)e_0`, `deg P<5`. Every projection of `e_0` is nonzero, while `P(alpha_t)=0` would contradict irreducibility. In particular no nonzero exact pure-eigenmode preparation belongs to `K^5`.

This excludes exact commuting linear filters and pure-mode preparations in that carrier. It does not exclude approximation, limits, nonlinear controllers, added references or extended coefficient fields. Mere use of coefficients in `K` does not imply that every observation is Galois-invariant.

## 3. A positive spectral energy is additional selection data

At the marked complex embedding consider

    H_m=(I-j^m V)^*(I-j^m V),       m in Z/5.

All are positive. Their mode-`t` eigenvalues are `|1-zeta*j^(t+m)|^2`. Under an additional normalized ground-state requirement the unique minimum selects `t=-m`: exponent `1` is strictly closest to `1` among the roots with exponents `1,6,11,16,21`. Thus `H_0` selects the principal mode under that requirement, but positivity and `V^5=j I` do not select `H_0`.

These alternatives have an essential gauge relation. For `D_m=diag(1,j^m,j^(2m),j^(3m),j^(4m))`,

    D_m V D_m^-1=j^m V,       H_m=D_m H_0 D_m^-1.

Transforming preparation and receiver frame together preserves observations. The family demonstrates freedom of a marked mode label under the stated conditions; physical inequivalence additionally requires an independently fixed receiver frame.

The native account `sum_k Q(v_k)` is conserved by `V` and `j^m V`. A normalized principal-embedding Rayleigh minimum of `H_m` is not that account and has not been selected by its conservation. An unconstrained positive quadratic energy has its minimum at the zero state; imposing nonzero normalization or occupancy is additional data. Its exact normalized complex ground eigenvector is not a nonzero `K^5` state.

Finally, reversible unitary evolution preserves eigenmode weights. It does not cool into the selected ground mode. Preparation, relaxation, measurement or a limiting procedure must be supplied, with the required carrier and resources.

The next experiment must therefore identify where character hypotheses produce different actual states or dynamics, then attach one independently fixed receiver. Reading a record can discriminate such operational alternatives; it cannot create a missing parameter inside the unchanged law. No physical character, action unit or electromagnetic coupling has yet been selected.