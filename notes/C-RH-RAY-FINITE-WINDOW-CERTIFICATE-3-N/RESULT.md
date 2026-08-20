# Result. C-RH-RAY-FINITE-WINDOW-CERTIFICATE-3-N

```text
DECISION:      CERTIFICATE
THEOREM:       candidate-T, conditional and NON-CANONICAL
COMPUTATION:   candidate-C, exact bounded synthetic replay
BREAKER:       0/10 findings
VERIFIER:      10/10 PASS
AUTHORITY:     none
PUBLIC STATUS: none
RH:            unchanged and open
```

## 1. Result

**[candidate-T, NON-CANONICAL]** The qualitative Ray-Pick converse from issue
#374 has an explicit finite-window version.

Fix `c>1/2`. Suppose a complete finite tau-invariant window `W` of distinct
zeta-zero locations contains one nontrivial orbit

```text
O={alpha,tau alpha},       tau alpha=-conj(alpha),
```

with common multiplicity `m_O`. Define

```text
t_beta=(c-conj(beta))^-1,
tau_0=min(|t_alpha|,|t_(tau alpha)|),
q_W=sup_(beta notin W)|t_beta|/tau_0.
```

There is an explicit polynomial `P_r` with no constant term which is zero on
all of `W\O` and has values `+1,-1` on the target pair. Its Ray form splits
exactly as

```text
<J_ref f_r,f_r>=-2m_O+E_r,
|E_r|<=Tail_r,
Tail_r=sum_(beta notin W)m_beta|P_r(t_beta)|^2.
```

The finite window removes every other known orbit exactly. Tau invariance
removes every window-to-tail cross term. Only the positive norm of the unknown
outside tail remains.

If `q_W<1`, the tail has the explicit bound

```text
Tail_r<=A_W(c)q_W^(2(r-r_0)),
A_W(c)=B_W^2C_W^2M(c)/((c-1/2)tau_0^2),
```

where `B_W` and `C_W` are the finite interpolation constants frozen in the
preregistration. The constant is independent of `r`. Therefore

```text
r_*=min{r>=r_0:A_W(c)q_W^(2(r-r_0))<2m_O}
```

exists, and the one-point mixed-derivative Ray-Pick matrix through order

```text
N_*=r_*+|W|-1
```

is indefinite. At least one leading principal minor through that order is
nonpositive.

This is the new mathematical content: one hypothetical off-critical orbit plus
a complete sufficiently tall zero window forces a finite explicit positivity
failure. The earlier result only guaranteed that some finite failure exists.

## 2. Prime-side part of the bound

The ordinary Cauchy norm needed in the tail estimate obeys

```text
sum_beta m_beta/|c-beta|^2<=M(c)/(c-1/2),
M(c)=X'(c)/X(c).
```

For `c>1/2`, `M(c)` has the absolutely convergent prime-side display already
recorded in the Ray-Pick incubation under #374. Thus the infinite ordinary-norm
constant does not require a second zero-side sum once `c` is fixed.

This does not make the certificate Euler-side. The target orbit, the complete
window, and the ratio `q_W` are still zero-side inputs.

## 3. Height criterion

If `alpha=x+iy` and `W` contains every zero location through height `T`, then

```text
q_W<=sqrt(y^2+(c+|x|)^2)/T.
```

Hence

```text
T>sqrt(y^2+(c+|x|)^2)
```

is a simple sufficient condition for exponential tail separation.

An arithmetic use still requires a proof that the zero window is complete with
multiplicities without assuming RH, exact isolation of a nontrivial tau orbit,
and certified finite constants. None is supplied here.

## 4. Exact synthetic replay

**[candidate-C, NON-CANONICAL]** On the frozen rational carrier

```text
c=7/5,
target={2/5+12i/5,-2/5+12i/5},
W=target plus its conjugate orbit,
outside={24i/5,-24i/5},
outside multiplicity=10^6,
q_W=3/5,
```

both code paths give exactly:

```text
r=1:                                 sufficient tail test fails
first direct tail certificate:       r=14
finite derivative order:             N=17
exact inertia at N=17:               (positive,negative,zero)=(4,2,11)
first nonpositive leading minor:      order 5
conservative uniform-bound threshold:r=19
breaker:                             0/10 findings
accepted verifier:                   10/10 PASS
```

The difference between `r=14` and `r=19` is not a disagreement. `r=14` uses
the exact finite outside tail. `r=19` is the sufficient threshold obtained from
the general uniform majorant without using cancellation.

## 5. Integrity history

The record preserves two predecessor boundaries:

1. #466 completed the synthetic discovery before Public Canon v57 activated,
   then stopped as a stale-basis surface.
2. #468 repinned the theorem on v57. Its breaker passed, but its first pinned
   wrapper failed during import before the engine ran because the dynamic
   module was not inserted into `sys.modules`. The wrapper was not repaired.
3. This fresh #469 lane pinned the explicit registration before execution:

   ```python
   sys.modules[spec.name]=module
   spec.loader.exec_module(module)
   ```

   The carried engine bytes and every scientific threshold remained unchanged.

## 6. Scientific weight

This is a genuine quantitative sharpening of the Ray-Pick carrier, but it does
not move RH.

What is now closed conditionally:

```text
one off-critical tau orbit
+ one complete sufficiently tall zero window
=> one explicitly bounded finite derivative positivity failure.
```

What remains the wall:

```text
construct the same positivity or its failure from the Euler side without
feeding in the zero window.
```

Equivalently, the result improves falsity detectability after an off-critical
orbit is known. It does not help prove that no such orbit exists. The
Stieltjes/Hausdorff source bar from #374 remains unchanged.

## 7. Nonclaims

No actual zeta ordinate. No zero table in an assertion. No RH proof, evidence,
or probability update. No public T or C row. No Canon, Registry, Frontier,
probe, release, physical, decoder, Born, SI, or L1-L6 statement. No claim of
novelty relative to the general theory of Cauchy interpolation beyond this
specific Ray-Pick packaging and explicit threshold.