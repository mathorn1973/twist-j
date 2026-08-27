# P-O5-FIRST-SHELL-BILINEAR-SQUARE-1 result

Status: **CANDIDATE-T / PROOF-FIRST / LOCAL FORMAL LEG PASS / PUBLIC TWO-ARCHITECTURE REPLAY PENDING / CANON UNCHANGED**

## Verdict

The frozen written proof survives the accepted exact audit.

Let `nu(n)=mu(n)` on squarefree integers supported only on split rational
primes strictly greater than `11`, and zero otherwise. Let

```text
b(n)=(-2)^omega(n)
```

on the same squarefree support. Then for every `n>=1`,

```text
b(n)=sum_(ab=n,(a,b)=1)nu(a)nu(b).
```

Therefore the first-shell carrier of the merged dilation probe is exactly the
coprime bilinear annulus

```text
W_11(N)=sum_(N/11<ab<=N,(a,b)=1)nu(a)nu(b).
```

Define the ordinary convolution square

```text
c=nu*nu,
C(N)=sum_(ab<=N)nu(a)nu(b),
Q_11(N)=C(N)-C(floor(N/11)).
```

The coprime carrier and ordinary square differ by the exact local dressing

```text
R_p(T)=(1-2T)/(1-T)^2,
R_p(T)-1=-T^2/(1-T)^2,
R_p(T)^-1-1=T^2/(1-2T).
```

The deviations start at degree two. Since the first tail split prime is `19`,
the global dressing and its inverse have absolutely convergent Dirichlet
coefficient series at every real `theta>1/2`. Writing their coefficients as
`r(d)` and `q(d)` gives the exact annular transfers

```text
W_11(N)=sum_(d<=N)r(d)Q_11(floor(N/d)),
Q_11(N)=sum_(d<=N)q(d)W_11(floor(N/d)).
```

Consequently, for every fixed real `theta>1/2`,

```text
W_11(N)=O(N^theta)
iff
Q_11(N)=O(N^theta).
```

In particular the all-epsilon square-root target is equivalent on the
first-shell carrier and the ordinary bilinear annulus.

The ordinary annulus has the exact hyperbola form

```text
U(X)=sum_(n<=X)nu(n),
H(X)=sum_(ab<=X)nu(a)nu(b),
R=floor(sqrt(X)),

H(X)=2 sum_(a<=R)nu(a)U(floor(X/a))-U(R)^2,
Q_11(N)=H(N)-H(floor(N/11)).
```

Equivalently,

```text
Q_11(N)=sum_(a>=1)nu(a)
  [U(floor(N/a))-U(floor(N/(11a)))].
```

This is a transfer theorem, not a new cancellation estimate.

## Exact route boundary

For one fixed squarefree allowed support `S`, every ordered partition
`S=A disjoint-union B` has

```text
nu(product A)nu(product B)=(-1)^|S|.
```

Thus every support-preserving recoloring is sign-preserving, not
sign-reversing. The bilinearization itself cannot generate cancellation inside
one fixed product. A successful next mechanism must couple different products
or supports, or use a genuinely nontrivial signed kernel with separately
controlled reconstruction.

## Accepted exact audit

```text
pin_commit:       7af861ebd5e2f06a8f75624a2e4bc80e19f01883
verifier_sha256:  857dba6fa4a152ac5a57749875d9bdc3c293e8fd3028ce86377356178179bd5a
stdout_sha256:    fa0db49ae054064f0fd6071cb8c773932a6e029bd5982fbc2f2d170696315488
stdout_bytes:     362
stdout_lines:     9
exit_code:        0
stderr_bytes:     0
readout:          VERIFY RESULT 8/8 ALL PASS
```

Frozen breakers fired at their preregistered witnesses:

```text
B1 uncoprime coefficient claim:       n=361
B2 deleted overlap dressing:          degree two
B3 false inverse degree-one term:     degree one
B4 included split prime 11 in tail:   n=11
B5 support recoloring sign reversal:  support {19}
```

## Scientific boundary

The coprime bilinearization, overlap dressing, half-plane coefficient-unit
transfer, ordinary hyperbola identity and support-preserving recoloring no-go
are `candidate-T`.

No RH or GRH result, new summatory estimate, zero-free region, meromorphic
continuation of the square-root carrier, Hecke or automorphic object, selected
split orientation, physical dictionary, probability statement, SI statement
or L1-L6 lift is claimed. The theorem does not say that `Q_11` is small.

Public Canon v67, Registry, Frontier, dependencies, gates, evidence, Notes and
all existing public rows remain unchanged.
