# READBACK C-RH-CAPACITY-CONTRACTION-1-N

```text
STATUS:        NON-CANONICAL INCUBATION READBACK
AUTHORITY:     none
ISSUE:         #357
PR:            #359
LANE HEAD:     1dd2ef2a4d844d3a915738369898c41ff0ebc93d
PUBLIC BASIS:  Public Canon v46, main 6545c1d0
PUBLIC STATUS: no change
RH STATUS:     O (unchanged)
```

This readback supersedes the consolidation survey made before #359. The
frozen `PREREG.md`, the corrected finite `break.py`, and their history remain
preserved. The later result package must be read with `CORRECTION.md`.

## Current gate state

```text
G1  DELAYED-KREIN-FACTOR          candidate-T exact algebra retained
G2  PURE-ARCHIMEDEAN-SCHUR-NOGO  candidate-T exact sign law retained
G3  CAPACITY-POSITIVITY           UNDECIDED on the full domain a>0
G4  CAPACITY-CLOSURE              BLOCKED on G3
G5  CUTOFF-COHERENCE              candidate-T restriction law retained
G6  NESTED-CONTRACTION            BLOCKED by the frozen G3-G5 order
```

The exact finite breaker still checks only the displayed witnesses or
discrete analogues that it prints. The general G2 Schur sign law and G5
disjoint-support identity are separate elementary proofs; the script is an
audit witness, not a universal proof by sampling. Its terminal state remains

```text
G3 UNIVERSAL POSITIVITY UNDECIDED.
```

## Source-level correction

For Suzuki's involution

```text
tilde(v)(x)=conj(v(-x)),
```

the two pole integrals sum to

```text
2 Re[M_+(v)conj(M_-(v))]
 =(1/2)|M_+(v)+M_-(v)|^2
  -(1/2)|M_+(v)-M_-(v)|^2,
```

not `|M_+|^2+|M_-|^2`. The corrected strict-cutoff capacity is therefore

```text
q_A,a(v)
 =2 Re[M_+(v)conj(M_-(v))]
  +integral_0^infinity K(t)||E_a v-U_tE_a v||^2 dt
  +(1/2)sum_(log n<2a) w_n||E_a v-U_(log n)E_a v||^2
  -kappa||v||^2.
```

It is a signed coercivity problem. The proof supplied earlier for
`q_A,a(v)>0` on `a>=log 41` discarded the indefinite pole term and is
withdrawn. The theorem is not refuted, but the supplied proof is stopped; the
large ray and the full G3 domain are both `UNDECIDED`.

The exact signed feature maps survive with pole coordinates

```text
R_+^pole(v)=[M_+(v)+M_-(v)]/sqrt(2),
R_-^pole(v)=[M_+(v)-M_-(v)]/sqrt(2).
```

Together with the continuous jump, mass, and delayed prime channels they give

```text
Q_W^a(v)=||R_+(v)||^2-||R_-(v)||^2.
```

No contractive or coherent extension of the algebraic graph map has been
proved.

## Exact content retained

1. The finite prime-power delayed factorization and one-block inertia no-go.
2. The gamma jump-energy formula with its separate signed pole and mass terms.
3. The translation-chain lower bound and the strict prime-power shell
   estimate. The shell estimate alone does not control the negative pole
   direction.
4. The G5 restriction law: each newly admitted disjoint delay adds exactly
   `w_n||v||^2` to both delayed legs, so the signed difference is unchanged.
5. At scalar Fourier-symbol level, the Euler-normalized balanced
   stabilization yields exact local Euler/Blaschke quadratures, scattering
   phase derivatives, and local square-root-cover identities.
6. Connes--Consani Proposition 3.7 identifies the lifted local Blaschke factor
   and Hardy kernel; Theorem 5.3 supplies multiplier comparison maps when
   places are added.
7. The gamma ratio has an exact Weierstrass boundary factorization into
   first-order rational all-pass cells plus pure boundary phases.
8. On a stated smooth form core, the semilocal phase derivative gives the
   exact signed identity

   ```text
   Q_W^a
    =(R_+^pole)^*R_+^pole-(R_-^pole)^*R_-^pole
      -i W_a^*W_a'.
   ```

   Here `W_a` is an isometric cutoff-output column and the last term is its
   Wigner--Smith/logarithmic velocity. This is a form identity for `Q_W^a`,
   not the frozen G3 capacity; `q_A,a=Q_W^a+||V_a^+v||^2` still uses the
   strict truncated feature map.
9. In the exact Connes--Consani archimedean source convention,
   `u_inf=rho_inf`, and its logarithmic derivative is the same gamma Weil
   multiplier. The source prolate pair is the escape square

   ```text
   B^*B=P1 P1_hat P1,
   delta(1)=||B||_HS^2.
   ```

   `P1` is already the two-sided time cutoff in the even real model, not a
   Hardy half-space. The map from this source cutoff carrier to Suzuki's
   additive support carrier is not proved.
10. A post-prereg shortcut is exactly excluded: multiplying one Gauss
    archimedean half-factor by `rho_p` cannot be inner in the stated
    half-plane, because the pole at `s=0` survives (or its order increases).
    This is a NON-CANONICAL candidate-T no-go for that named shortcut, not a
    public `F` claim and not an opened G6 gate.
11. Suzuki's unconditional screw-line carrier is prior art: the vector exists
    in `L2` without RH, while the ordinary Gram/metric identification remains
    RH-equivalent. The global boundary phase has the exact Cayley form

    ```text
    Theta_xi=(1-xi'/xi)/(1+xi'/xi).
    ```

    Boundary unimodularity is unconditional; Hardy innerness/zero escape is
    the classical RH-equivalent wall, not a local-passivity conclusion.
12. With Suzuki's Fourier convention and
    `A_0=(2 pi)^(-1/2) sharp o F`, there is an exact unconditional identity

    ```text
    A_0[V(0)] = S_diag(Theta_xi)
              ~= ker T_(conjugate Theta_xi),
    S_diag(u)=ker(Q M_u Q |_(QH)).
    ```

    `S_diag` is deliberately neutral: Connes--Consani's named Sonin space
    additionally assumes quasi-innerness, which is not proved for
    `Theta_xi`. The semilocal-to-global Wiener--Hopf transport is unproved and
    deferred to a separately locked comparison.
13. The raw prime-ordered Euler impedance diverges already on every real
    `1/2<sigma<1`. This is a candidate-T no-go only for that raw shortcut.
    The source comparison also excludes a literal generator-/spectrum-
    preserving identification of the named CCM and Suzuki de Branges spaces;
    it does not exclude a nontrivial intertwiner, quotient, compression, or
    renormalized defect limit.

Items 5-7 do not construct a linear map from the delayed Euler tower to a
Hardy/Sonin carrier. Boundary unimodularity is not by itself a causal passive
realization, and the finite-prime ratio `rho_p=z/b_r` is not the Schur transfer
function realized by the displayed colligation in that disk orientation.
Items 8-13 add no positivity: full Euler completion is only a balanced
stabilization of the signed Weil value, the pole pair is indefinite, and the
Connes/Suzuki cutoff-carrier and semilocal/global intertwiners are deferred.

## Stopped and bounded follow-up claims

- The positive-pole shortcut and the supplied large-cutoff G3 proof are
  stopped by the source correction.
- Direct identification of both corrected feature legs with the exact Sonin
  isometry would force equal norms and is a no-go only for that direct
  isometric candidate.
- The local `D_p,N_p,b_r` multiplier identity is exact, but the actual
  semilocal graph update retains `u_F`; an outer reweighting and a linear
  carrier map remain missing.
- The model-space projection difference is an exact rank-two analogue, not a
  new proof of the delayed-tower Sylvester no-go without a carrier map.
- The literal coefficient-preserving three-sector match to the semilocal
  off-diagonal pole expansion fails at the mixed collision jet. This does not
  exclude a prime-dependent basis change or larger mixed defect carrier.
- `TRACE-REMAINDER-DOMINATION-NOGO.md` is `STOP` as a #357 result because it
  reused the wrong positive pole sum. Its auxiliary `delta(1)` comparison does
  not decide G3 or G6.
- Every proposed compressed-delay, Sonin, model-space, or cutoff-defect
  construction is only a possible separately locked comparison/no-go study.
  None opens or executes G6 while G3 is undecided.
- The first Hardy-half-space reading of the Connes prolate projection and the
  later speculative gauge reading were both withdrawn in branch history. The
  corrected source convention is the two-sided prolate pair with superscript
  `g` meaning geometric representation, not an extra phase gauge.
- `ONE-CRITICAL-ZERO -> V(0) NONZERO` is `STOP` as an unsupported inference:
  the source construction of the corresponding `V(0)` vector is
  RH-dependent. No theorem says every possible zero-based construction fails.
- The local prime sign and raw cumulative Euler divergence are one nested
  obstruction family, not independent confirmations. Likewise, the bounded
  source de Branges mismatch overlaps the earlier direct-isometry boundary.

## Cutoff provenance variance

The public issue body froze `log n<=2a`, while committed `PREREG.md` uses
`log n<2a`. At equality the correlation vanishes, so both conventions give
the same signed Weil prime form. They do not give the same auxiliary capacity:
the inclusive convention adds matched mass `w_n||v||^2` to both Hilbert legs.
The result package uses the committed strict convention. A later public claim
must freeze one convention explicitly.

## Source and lane boundaries

This lane imports Suzuki arXiv:2606.09096 for the Weil functional and localized
form. It remains source-distinct from #355 and #358, which use arXiv:2206.03682.
The theorem-scope correction in #355 must not leak into this preregistration.

Three capacity-looking objects remain inequivalent until a typed bridge is
proved:

- `q_A,a(v)` here, a signed quadratic-form candidate;
- `X_(+,a)` in #355, a positive feature carrier;
- scalar `A(t)` in #358, attacked by ramp, filtration, and screw falsifiers.

The complete finite-prime-sector no-go constrains the fixed source-side split
in #355: a contraction for that split cannot be finite-prime-only. It does not
prove G3, identify `q_A` with `X_+`, or force every future architecture to use
the same cross-place block.

## Ordered boundary

The immediate #357 task is a joint source-side coercivity analysis for the
corrected signed G3 formula. In parallel, one outcome-blind G0 classification
must type `q_A` and `X_+` before either is selected as a capacity carrier.

The post-correction Sonin/Toeplitz documents retained in this history are
exposed preparation only: they are neither G6 evidence nor inherited
candidate results of #357. Fresh issue #360 and branch
`notes/c-rh-global-sonin-wiener-hopf-1-n` own any re-derivation of that
semilocal/global comparison. The #360 scientific package is not integrated in
this consolidation; this readback records only the routing boundary added at
`1dd2ef2`.

No Canon, Registry, frontier, evidence-ledger, or RH status movement follows.
