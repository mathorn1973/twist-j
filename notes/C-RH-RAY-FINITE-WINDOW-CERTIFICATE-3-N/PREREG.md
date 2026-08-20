# PREREG-C-RH-RAY-FINITE-WINDOW-CERTIFICATE-3-N

```text
STATUS:          NON-CANONICAL / RESULT-EXPOSED / INTEGRITY-RETRY
AUTHORITY:       none
ISSUE:           #469
BRANCH:          notes/c-rh-ray-finite-window-certificate-3-n
PATH:            notes/C-RH-RAY-FINITE-WINDOW-CERTIFICATE-3-N/
BASIS:           Public Canon v57 ACTIVE
MAIN AND TAG:    4ef54f0c34f80897af0121a2d93b710e70a8377c
CONTENT COMMIT:  8e8b04abe4d3359942449533854ef1d142be70df
CANON SHA256:    c96a2ef52c78d68ef8f04b582e4a17328e6a863b49664f29b1bd324171d802a8
CANON BYTES:     295013
LAYER:           analytic and operator-theoretic only
FORMAL PROBE:    none
CANON WRITE:     forbidden
ACTUAL ZEROS:    forbidden in assertions
```

This is the fresh retry required after #468's pinned wrapper failed before
science. The failure was an importlib/dataclasses integrity defect. No
mathematical threshold or result changes here.

## Result exposure

Known before this pin from #466 and #468:

```text
q_W=3/5,
direct sufficient-tail transition r=14,
N=17,
inertia=(4,2,11),
first nonpositive leading minor=5,
uniform-bound transition r=19,
breaker findings=0/10,
matrix engine=10/10 PASS.
```

This lane is not blind discovery and not independent confirmation.

## Frozen theorem

Use the Ray-Pick objects of #374:

```text
X(z)=xi(1/2+z),
alpha=rho-1/2,
tau alpha=-conj(alpha),
M(a)=X'(a)/X(a),
K_ray(a,b)=(M(a)+M(b))/(a+b),       a,b>1/2.
```

For fixed `c>1/2`, put

```text
t_beta=(c-conj(beta))^-1,
w_k(beta)=sqrt(m_beta)t_beta^k.
```

Let `W` be a finite tau-invariant zero window and let
`O={alpha,tau alpha}` be one nontrivial orbit of multiplicity `m_O`. Let the
exact interpolation polynomial `P_r` vanish on `W\O` and take the values
`+1,-1` on the target pair. Define

```text
tau_0=min(|t_alpha|,|t_(tau alpha)|),
q_W=sup_(beta notin W)|t_beta|/tau_0.
```

The theorem to audit is exactly:

```text
Tail_r<=A_W(c)q_W^(2(r-r_0)),
Tail_r<2m_O => a finite one-point Ray-Pick derivative matrix is indefinite,
r_*=min{r>=r_0:A_W(c)q_W^(2(r-r_0))<2m_O},
N_*=r_*+|W|-1.
```

The complete-height sufficient condition is

```text
T>sqrt(y^2+(c+|x|)^2)
```

for `alpha=x+iy` and a window complete through height `T`.

The written proof must retain:

1. the exact mixed-derivative/J_ref Gram identity;
2. injectivity and exact interpolation;
3. the tau-invariant split `-2m_O+E_r`, `|E_r|<=Tail_r`;
4. the finite-matrix and leading-minor consequence;
5. the r-independent constant

   ```text
   A_W(c)=B_W^2C_W^2M(c)/((c-1/2)tau_0^2);
   ```

6. the ordinary Cauchy bound

   ```text
   sum_beta m_beta|t_beta|^2<=M(c)/(c-1/2);
   ```

7. the complete-height bound on `q_W`.

## Frozen synthetic carrier

```text
c=7/5,
alpha=2/5+12i/5,
tau alpha=-2/5+12i/5,
W={alpha,tau alpha,conj(alpha),conj(tau alpha)},
outside={24i/5,-24i/5},
multiplicity 1 on W,
multiplicity 10^6 outside,
r_0=1.
```

It is a theorem control, not a zero set.

## Falsifiers

Any exact failure of the derivative signs, interpolation, invariant split,
ordinary norm bound, exponential bound, threshold, height inequality, direct
versus coefficient form, inertia, or leading-minor result is F. Any authority,
ordering, hash, wrapper, import, or scope failure is STOP. A tau-fixed target
must be rejected. A window with `q_W>=1` must be rejected from the exponential
gate.

## Breaker and accepted verifier

The v57 breaker is pinned before the accepted verifier and run once. It may be
byte-identical to #468's clean breaker because all result exposure is declared.

The exact matrix engine may be carried byte-identically from the successful
v56 audit and is pinned under this fresh path. The accepted wrapper is new and
must use this exact order:

```python
spec = importlib.util.spec_from_file_location(NAME, ENGINE)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
raise SystemExit(module.main())
```

The explicit `sys.modules` registration is the only integrity delta from the
failed #468 wrapper. It is frozen before execution. The wrapper hash-checks the
engine and accepts no arguments.

## Order

1. Pin and read back this file.
2. Pin and read back `break.py`; run it once.
3. Pin and read back `PROOF.md`, `engine.py`, and `verify.py`.
4. Run `verify.py` once under the deterministic environment.
5. Record exact stdout, stderr, hashes, RUN, RESULT, and issue closeout.

No file is repaired after its first execution.

## Decision ceiling

```text
CERTIFICATE  candidate-T conditional theorem + candidate-C synthetic replay
F            exact mathematical falsifier
STOP         any integrity or protocol failure
```

## Firewall

No actual zero, no zero table in assertions, no RH proof or evidence, no
Euler-side positivity theorem, no Canon, Registry, Frontier, public probe,
release, physical, decoder, Born, SI, or L1-L6 claim.