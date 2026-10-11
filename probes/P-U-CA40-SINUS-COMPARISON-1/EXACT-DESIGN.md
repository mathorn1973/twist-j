# Exact audit and interpretation contract

PUBLIC NON-CANONICAL. Conditional L1 mathematics. Original text Apache-2.0.
Reserved probe P-U-CA40-SINUS-COMPARISON-1:
https://github.com/mathorn1973/twist-j/issues/1456.

This design was prepared without running or importing scientific source.
The exact verifier checks finite rational identities. It is not an oracle
for the nonlinear numerical result, a trajectory convergence test or a
physical-admission certificate. PREREG.md governs the final execution contract.

## 1. Fixed numerical scope

Keep both predecessor envelopes and the three active branches `(4,3)`,
`(4,4)`, `(1,1)`. All seven harmonic modes remain present. The protected
electronic responses are zero. The independent initial bus has nbar=1/20
in each mode. The moving full-linear frame is computed from the same
absolute-time pulse history; no waveform, phase or duration is refitted.

The deterministic initial thermal set is total occupation K=3, comprising
120 orthonormal Fock inputs. The four configurations, in frozen order, are

```text
dynamic total cutoff L=4, 128 RK4 steps per original segment;
dynamic total cutoff L=6, 128 RK4 steps per original segment;
dynamic total cutoff L=6, 256 RK4 steps per original segment;
dynamic total cutoff L=6, 512 RK4 steps per original segment.
```

An original segment is 6.25 microseconds; there are 80. No step crosses an
original segment or ideal-carrier boundary. The basis dimension is
binom(L+7,7): 330 at L=4 and 1716 at L=6. The initial thermal rank and the
dynamic basis dimension are distinct quantities. No K=4 or L=8 numerical
extension belongs to this pin. The coordinator has a frozen 1800-second
budget for kernel launches and execution, measured from setup start, and
retains partial output on timeout without retry. Final validation,
endpoint comparisons and archival may extend the total reported wall time.

The fixed panels diagnose cutoff and step sensitivity. Their agreement is
not a rigorous bound on either error. The six branch evolutions do not
constitute a complete 25-branch channel audit.

## 2. Thermal weights and exact omitted mass

For r=nbar/(1+nbar)=1/21 and n=(n_1,...,n_7), preserve the original weights

```text
p_n=(1-r)^7 r^(sum n_i),
T_K={n:sum n_i<=K},
dim(T_K)=binom(K+7,7),
w_K=(1-r)^7 sum_(j=0..K) binom(j+6,6)r^j,
p_tail=1-w_K.
```

The verifier compares explicit occupation enumeration with the grouped
stars-and-bars formula at K=0,1,2,3. At K=3 it checks exactly that
`0<p_tail<9/10000`. There are 120 retained vectors, with unequal weights;
they are not a uniform ensemble and not a random thermal sample.

The normalized conditioned bus differs from the full thermal state by
trace distance p_tail. A generic comparison of two output channels with
that conditioned input therefore has a 2p_tail conditioning allowance.
This is a statement about INITIAL thermal truncation. It says nothing
about a finite Hamiltonian or later population at a dynamic cutoff.

For the overlaps used here, keep unnormalized sums instead. If |g_n|<=1,

```text
G_ret=sum_(n in T_K) p_n g_n,
G_full=G_ret+G_tail,             |G_tail|<=p_tail.       (1)
```

The omitted contribution is a complex disc, not a guessed value zero.
The verifier tests this disc with rational unit-modulus tail values and
exposes omission of the retained mass. With an identity evolution,
G_ret=w_K while G_full=1; treating G_ret as the complete overlap falsely
creates apparent decoherence. Conversely, normalizing G_ret but then
forgetting the factor w_K also changes the defined observable.

## 3. Exact projected displacement

The dynamic projector P_L retains total occupation <=L. Use

```text
D(beta)=exp(-||beta||^2/2) exp(beta.a^dagger) exp(-beta*.a),
P_L D(beta) P_L
 = exp(-||beta||^2/2)
   exp(P_L beta.a^dagger P_L) exp(-P_L beta*.a P_L).      (2)
```

Equation (2) is valid because annihilation occurs first and only lowers
total occupation; subsequent creation only raises it. A path which goes
above L cannot return during the creation factor. Both projected
exponentials are finite nilpotent polynomials. This argument does not
permit exponentiating the projected quadrature:
`P_L exp(iX) P_L != exp(i P_L X P_L)` in general.

To keep fixtures rational, use the unnormalized basis
`|n>_u=product (a_m^dagger)^n_m |0>`, whose metric is product n_m!.
Here creation has coefficient 1, annihilation coefficient n_m. The
universal Gaussian scalar is kept formal and canceled from identities;
no transcendental displacement amplitude is evaluated by the verifier.

An independent coefficient formula for the normal-ordered part is

```text
A_(m,n)(beta)=sum_(0<=j_i<=min(m_i,n_i))
 product_i [binom(n_i,j_i)(-conj(beta_i))^(n_i-j_i)
            beta_i^(m_i-j_i)/(m_i-j_i)!].               (3)
```

The verifier compares sparse ladder exponentials against (3), and against
restriction from a larger ambient cutoff, on one-, two- and three-mode
rational fixtures. It also checks the weighted adjoint identity
`metric(m) A_mn(beta)=metric(n) conjugate(A_nm(-beta))`.
The fixtures have 35 columns and 525 matrix entries. They audit the
dimension-independent algebra used by seven modes; they do not enumerate
the seven-mode numerical trajectory or verify its floating arithmetic.

The projected-quadrature negative control uses L=0. Its exponential is
the identity, but the true vacuum displacement has a nonzero quadratic
coefficient `-||beta||^2/2`. Thus apparent exact unitarity within a tiny
projected quadrature space can hide real leakage of the full operator.

## 4. Moving-frame overlap restoration

Let `U_S,z=U_L,z W_z` for each branch z. The nonlinear physical bus overlap
for branches a,b is

```text
G_S,ab = Tr[rho_th W_b^dagger U_L,b^dagger U_L,a W_a].  (4)
```

The factor between the W states is essential. For
`U_L,z=exp(iPhi_z)D(alpha_z)`, it equals

```text
U_L,b^dagger U_L,a
 = exp(i[Phi_a-Phi_b+Im(conj(alpha_b).alpha_a)])
   D(alpha_a-alpha_b).                                (5)
```

For two finite projected W vectors, the matrix element of (5) is obtained
with the true P_L D P_L action (2), including its Gaussian prefactor.
This is the exact physical-frame matrix element between those approximate
vectors; no additional assumption that the displacement preserves P_L
is needed. It does not remove errors in those vectors themselves.

The finite exact audit uses rational 2x2 unitaries to check
`(U_L,b W_b)^dagger(U_L,a W_a)
 = W_b^dagger U_L,b^dagger U_L,a W_a` and branch-frame rephasing invariance.
It exposes a raw-W-overlap mistake even when W_a=W_b=I: the actual S and
L evolutions are identical, but dropping their different frames invents
a discrepancy. This is not a numerical simulation of a physical qubit.

For a balanced coherent input of a,b, optionally correlated with orthogonal
reference labels, the reduced electronic/reference output difference is

```text
D_ab=|G_S,ab-G_L,ab|/2.                                (6)
```

Use the full analytic thermal G_L and the retained nonlinear G_S,ret.
Before dynamic/integration errors, the exact thermal allowance gives

```text
max(0,(|G_S,ret-G_L|-p_tail)/2) <= D_ab
 <= min(1,(|G_S,ret-G_L|+p_tail)/2).                    (7)
```

There are three pairs among the chosen three branches, per target sign.
Equation (7) is a thermal-tail envelope conditional on accurate propagated
vectors and analytic comparison data. It is not by itself a total error
bar for the ordinary floating finite-cutoff simulation.

Also retain `C_z,ret=sum p_n <n|W_z|n>`. Its full value is the overlap
of two specified purifications of the bus, with tail disc (1). It is not
the Uhlmann fidelity of the reduced mixed bus states, a measured source
coherence, or the optimal electronic channel distance. State this scope
when reporting echo amplitudes or distances derived from them.

## 5. Projection and integration error remain separate

For an exact projected trajectory psi_L(t) embedded into the full space,
Duhamel supplies

```text
||psi_full(T)-psi_L(T)|| <= integral ||Q_L H(t)P_L psi_L(t)|| dt/hbar. (8)
```

An approximate time integrator needs its residual in addition. For two
unit-normalized branch vectors with certified norm errors e_a,n,e_b,n,
the retained coherence error is at most
`sum_(retained n) p_n(e_a,n+e_b,n)`. Half of this enters (7). This does not
require an extra factor 120, but it requires actual error bounds.

The exact checker audits two relevant finite identities. For a highest
shell vector psi_L and A=sum conj(beta_m) a_m,

```text
||A^dagger psi_L||^2
 = ||beta||^2 ||psi_L||^2 + ||A psi_L||^2.               (9)
```

Only that shell contributes to Q_L X P_L. Omitting the lowering term in
(9) is a named negative control. A separate rational-unitary fixture
checks `||Q D psi||^2=||psi||^2-||P D psi||^2` for an exact unitary D.
In floating displacement calculations this subtraction can lose accuracy;
silently clipping a negative answer is not a residual certificate.

Sampled shell populations, sampled displacement leakages, and fixed-step
quadrature of residual norms are diagnostics. Without between-sample
enclosures and floating error control they do not certify (8). Boundary
mass alone is also insufficient: its coupling coefficient and accumulated
duration matter. The present exact output explicitly reports no dynamic
cutoff certificate and no time-integration certificate.

Norm preservation is a useful integrator check but does not establish
correct dynamics. A unitary evolution with the wrong generator can have
zero norm drift. Agreement of L=4 and L=6, or of two RK4 steps, likewise
does not prove convergence to the infinite-dimensional answer.

## 6. Source scope and acceptance semantics

In every declared branch Hamiltonian the protected electronic labels do
not occur. Ideal adjoint shelving return therefore gives
`I_P tensor U_(active,bus)` at the endpoint. The protected/source-reference
marginal is preserved for arbitrary correlations under this assumption.
The exact verifier checks commutation with a complete ququint Weyl algebra
in a small IP tensor V fixture. It does not test actual spectator darkness
or restore a complete unknown source after an informative full contact C.

Keep four distinct result types:

- EXACT_AUDIT_PASS or failure concerns only the finite rational identities
  and required negative controls. It does not certify the numerical run.
- Numerical integrity/consistency reports whether all frozen inputs, process
  records, dimensions and internal checks completed. Preserve any failure.
- Fixed-panel convergence reports L4/128 versus L6/128, and L6 at
  128/256/512, using complex amplitudes and restored coherences, not merely
  their magnitudes. Its threshold and norm-drift checks are frozen in PREREG.
- The nonlinear comparison reports specific branch/pair observables with
  exact thermal-tail allowances and separately labeled dynamic/time
  diagnostics. Without controlled latter errors it earns no rigorous
  threshold-crossing theorem or uniform channel certificate.

If the last panel times out or the convergence checks do not resolve the
question, report INCOMPLETE or numerically unresolved as appropriate; do
not select a favorable earlier panel or change the cutoff/step grid. A
large difference is a modeled numerical witness only at its stated error
status. Norm checks, plots or a small initial thermal tail cannot upgrade it.

The exact CLI accepts no arguments, imports only standard-library exact
arithmetic/support modules, reads no files and writes one deterministic
ASCII JSON line with explicit LF. All sources, data and declarations must
be publicly pinned and read back before execution. No expected output is
invented before the first completed formal run. This source preparation
authorizes no scientific execution.
