# P-PENTAGON-WEIL-1: Owner Ruling (NON-CANONICAL)

```text
Program:          PENTAGON-WEIL
Probe:            P-PENTAGON-WEIL-1
Claim candidate:  PENTAGON-NORMALIZATION [T]
Track:            exact analytic normalization
Owner:            A. M. Thorn, public lock issue 41
Date:             2026-07-17
Basis:            Public Canon v6, tag canon-v6
Current main:     e9a358a50f24fe1df3441516b9681a379bb4269e
Probe merge:      07b7f77531ec7920f5686084c6168077cff4acb0
Status:           RULING CANDIDATE BEFORE MERGE; NON-CANONICAL
Authority:        none until reviewed merge and public byte readback
Computation:      none authorized or required by this ruling
```

## 0. Owner decision

The completed public probe is accepted as sufficient evidence for a later
sealed Canon fold of exactly one claim candidate:

```text
PENTAGON-NORMALIZATION [T]
```

The earned scope is the pentagon root-filter normalization stated in section
2 below.  This ruling does not promote the broader Weil equivalence, define a
Weil test space, construct a positive realization, or make progress on RH.

The `[T]` recommendation rests on two distinct parts:

1. self-contained exact algebra and the inline divisor argument in the frozen
   preregistration; and
2. byte-identical execution of the exact finite audit on formal aarch64 and
   GitHub x86_64.

The classical analytic-continuation, functional-equation, Euler-product, and
completion theorems remain named imports.  The public claim must state that
boundary explicitly and must not present the verifier as a computational
proof of those imported theorems.

## 1. Public evidence and immutable pins

```text
public lock issue              41
initial public base            6bb013bafb2d1c06fcb295fdbfce0f86198fd685
preregistration pin            6be1231a4366dbcc04f7251afe7adb44df555250
PREREG.md SHA-256              f7e3b3ea14be504e73a26f49c29b7b87bc67655f6ccd215d6de3eadc5bd12774
verify.py SHA-256              5655888c9c8eac7fe49b2734235d9a65d318fac8b57b7d2a90b67a1f450f614c
formal aarch64 run commit      5a2771232335a173318ecb3d7b37a5e62d4111dd
EXPECTED.txt SHA-256           f042368571e4f3d302a6cfbe47c6d344bcdf8411d9dd4dca3a21aa9f216797fe
RUN.md SHA-256                 ee2aa4612b7e9073c910468ff604e1c38724a3a1bea37f2a01a8dfef114e9ad1
final probe head               b3a768ceceb28e861e6f0e5cfe3c0e2a39132ace
probe merge                    07b7f77531ec7920f5686084c6168077cff4acb0
current-main GitHub check      run 29575382018, job 87868541118, PASS
```

The formal aarch64 execution used Ubuntu 24.04.4 LTS and CPython 3.12.3.
The original GitHub x86_64 witness was run 29451572197, job 87475031267.
Both produced the exact 711-byte stdout with SHA-256
`f042368571e4f3d302a6cfbe47c6d344bcdf8411d9dd4dca3a21aa9f216797fe`,
exit zero, and empty stderr.  The later current-main check passed after a
merge of public `main` that left all five probe files byte-identical.

## 2. Exact earned scope

Let `j = zeta_5`, use the real branch of `log 5`, and define

```text
c(n)   = sum_(a=1)^4 j^(a n) = 5 [5 divides n] - 1,
P_0(s) = sum_(n>=1) c(n) n^(-s),
f_5(s) = 5^(1-s) - 1.
```

Then, on `Re(s)>1`,

```text
P_0(s) = f_5(s) zeta(s).
```

After the explicitly named classical meromorphic continuation and standard
completion are applied,

```text
Z_J(s)  = MerCont(P_0(s) / f_5(s)) = zeta(s),
xi_J(s) = (1/2) s(s-1) pi^(-s/2) Gamma(s/2) Z_J(s) = xi(s).
```

The quotient removes the filter zeros

```text
s_k = 1 - 2 pi i k / log 5,
```

with the pole and trivial zeros handled by the standard zeta completion.  The
natural series value at one is `P_0(1) = -log 5`.  The signed logarithmic
derivative contains the exact correction

```text
coeff(-P_0'/P_0)(n)
  = Lambda(n) - (log 5) n [n = 5^m],
```

so the artificial `5^m log 5` tower is subtracted rather than reinterpreted
as prime data.

The exact machine audit closes all six frozen computational rows.  The
preregistered RH equivalence in the open critical strip is proof-only and is
not one of the six machine rows.

## 3. Named imports and proof boundary

The later Canon text must name the following classical imports rather than
silently absorbing them into the computation:

- meromorphic continuation and the functional equation of `zeta`;
- the standard completed function `xi` and its divisor;
- the Euler product in its ordinary domain;
- Dirichlet convergence for the periodic coefficient sequence where used;
- the standard treatment of the pole and trivial zeros in the completion.

The verifier proves the exact finite root-filter algebra, cutoff identities,
value-at-one certificate, raw-symmetry falsifier, and sign accounting.  It
does not reprove the imported global analytic theorems.

## 4. Binding non-claims

This ruling does not earn or register any of the following:

```text
J-WEIL-EQUIVALENCE
J-WEIL-POSITIVE-REALIZATION
RH
```

In particular:

- no admissible Weil test space, Fourier convention, involution, closure, or
  quadratic-form normalization is frozen;
- no Hilbert space, positive operator, Fredholm determinant, or J-native
  carrier is constructed;
- the raw carrier `P_0` is not an uncorrected Weil-form carrier;
- the raw completion fails the standard constant unit-root-number symmetry
  by the exact factor `f_5(2)/f_5(-1) = -1/30`;
- equality `xi_J = xi` is a normalization identity, not a new proof of any
  property of `xi`;
- no L5-to-L6 lift is created by the word "Weil".

The five conventions required for a public `J-WEIL-EQUIVALENCE` statement
remain unfrozen.  Therefore no broad `P-PENTAGON-WEIL-2` follows from this
ruling.

## 5. Promotion posture

After reviewed merge and public byte readback, this file is an owner ruling,
not a normative claim.  A separate sealed Canon fold may add exactly
`PENTAGON-NORMALIZATION [T]` with evidence
`probes/P-PENTAGON-WEIL-1` and the scope in section 2.  That fold must choose
the Canon placement, registry wording, dependency edges, changelog entry, and
release version under the ordinary Public Canon policy.

The fold must leave the Weil positive-realization problem and RH open.  It
must not infer the unregistered Weil equivalence merely from the name of the
probe or from `xi_J = xi`.

No Canon, registry, frontier, status, release, or tag file changes on this
ruling branch.

