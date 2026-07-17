# P-J-LI-TORAL-HAAR-1: Owner Ruling (NON-CANONICAL)

```text
Program:          J-LI
Probe:            P-J-LI-TORAL-HAAR-1
Claim candidate:  J-LI-TORAL-HAAR-NOGO [T]
Track:            L6 measure/spectral no-go
Owner:            A. M. Thorn
Date:             2026-07-17
Basis:            Public Canon v7, tag canon-v7
Current main:     f5679fd9bdce98d6501e38fafe4bf312023804ea
Probe merge:      0c351e7690586710b67e22a8e2390d6f599c5613
Status:           RULING CANDIDATE BEFORE MERGE; NON-CANONICAL
Authority:        none until reviewed merge and public byte readback
Computation:      none authorized or required by this ruling
```

## 0. Owner decision

The completed public probe is accepted as sufficient evidence for a later
sealed Canon fold of exactly one claim candidate:

```text
J-LI-TORAL-HAAR-NOGO [T]
```

The earned scope is the all-`n` no-go theorem in section 2.  The separate
candidate identifiers `J-LI-SPECTRAL-TARGET` and
`J-LI-BY-STANDARD-TORAL-HAAR` are deliberately not registered by this
ruling.  The first remains a necessary conditional step inside the proof;
the second would only duplicate the no-go as a falsified positive alias.

The `[T]` recommendation rests on the proof frozen before execution.  The
byte-identical aarch64 and x86_64 runs audit its exact algebraic and interval
gates; they are not a computational proof of the imported global analytic
theorems.

## 1. Public evidence and immutable pins

```text
public lock issue              50
initial public base            7fe66e7ee8d02068c9717314988500c6022e73d6
preregistration pin            47b738ac90c7e76063696b62ef88685ca507d973
PREREG.md SHA-256              91efae35540d16f0714bf199d69f31d44f4ca1fef6863cc253e36680315c4383
verify.py SHA-256              3f309c3244a5ca8c911d9d2da0dfe7f48ade08f09c5ba8ada2cc379235fd219d
formal aarch64 run commit      376add6c14e6d2bc37dbcf4a7478b0d8af493982
EXPECTED.txt SHA-256           8e17b45e07b977fbbfe74f31cb64e2a78bc950cd5bedb70b9b163bcd77fbefc8
RUN.md SHA-256                 5393587ec61c769f4bf1b328fe6ece651faccc1de655bcec8764c86c9e3284e3
final probe head               2c6413c2700d016ff44f835fc726153a6f40c9f3
probe merge                    0c351e7690586710b67e22a8e2390d6f599c5613
GitHub x86_64 witness          run 29578010224, job 87876817139, PASS
probe bundle SHA-256           f313f2f064cd4031865f5b871ac73dd68367802e80a9e6235f591b5774be8a0e
```

The formal aarch64 execution used Ubuntu 24.04.4 LTS and CPython 3.12.3.
The GitHub x86_64 execution used Ubuntu 24.04.4 and CPython 3.12.13.  Both
produced the exact 2717-byte, 16-line stdout with SHA-256
`8e17b45e07b977fbbfe74f31cb64e2a78bc950cd5bedb70b9b163bcd77fbefc8`,
exit zero, and empty stderr.  The aarch64 leg was repeated three times with
byte-identical output.  The formal result records 9/9 theorem-skeleton gates
passing; X1 is an exploratory finite witness and is not a theorem gate.

## 2. Exact earned scope

For every integer `d >= 1` and every `A in GL_d(Z)` with no root-of-unity
eigenvalue, let `U_A f = f o T_A` be the Haar Koopman operator on
`L^2(T^d, Haar)`.  There is no vector `v` satisfying

```text
|| sum_(k=0)^(n-1) U_A^k v ||^2 = lambda_n
```

for every `n >= 1`, where `lambda_n` is the standard Li sequence.

Indeed, an exact realization first forces `lambda_n >= 0` for all `n`, hence
RH by Li's criterion.  Under that forced consequence, the standard Li
zero-sum formula and Fourier uniqueness force only the symmetrized vector
spectral measure

```text
mu_v + iota_* mu_v = sigma_xi,       iota(z) = conjugate(z),
```

where `sigma_xi` is the declared purely atomic zero measure.  A
root-of-unity-free toral character orbit is either constant or bilateral;
therefore its Haar Koopman spectral measure has no atoms away from `1`.
The forced atomic measure has atoms away from `1`, giving a contradiction.

The contradiction is unconditional for the assumed realization.  RH is a
forced intermediate consequence inside the contradiction and is neither an
assumption nor a conclusion of the public claim.

For the named TWIST-J specialization, `d = 4` and `A = M_J`.  Its exact
characteristic polynomial and eigenvalue moduli `phi, phi, phi^-1, phi^-1`
place it in the declared root-of-unity-free carrier class.  This
specialization uses the public `J-STEP`; the general theorem does not.

## 3. Named imports and proof boundary

The later Canon text must name, rather than silently absorb, these classical
imports:

- the standard Li coefficients, their zero-sum normalization, and Li's
  criterion in both directions;
- convergence of the fixed-`n` zero sum under RH;
- uniqueness of finite measures from their Fourier coefficients;
- the spectral theorem for a unitary operator, including the atom/eigenspace
  correspondence;
- the character basis of `L^2(T^d, Haar)` and the bilateral-shift
  decomposition of root-of-unity-free toral character orbits;
- the Riemann-von Mangoldt counting law and Stieltjes partial summation where
  the probe discusses the conditional accumulation asymptotic; and
- Gauss's lemma and the standard cyclotomic minimal-polynomial facts used to
  audit the `M_J` specialization.

The public theorem is proof-first.  TH1--TH9 audit exact finite consequences
and the named specialization.  X1 and the frozen TH8/TH9 intervals do not
prove the all-dimensional theorem or the imported asymptotic.

## 4. Binding non-claims

This ruling does not earn or register:

```text
J-LI-SPECTRAL-TARGET
J-LI-BY-STANDARD-TORAL-HAAR
J-LI-MOMENT-BRIDGE
J-LI-COCYCLE-REALIZATION
J-WEIL-POSITIVE-REALIZATION
RH
```

In particular:

- no existence of `sigma_xi` is asserted outside the forced RH branch of the
  contradiction;
- only `mu_v + iota_* mu_v` is forced; the unsymmetrized `mu_v` is not
  claimed unique;
- matrices with root-of-unity eigenvalues are outside the theorem;
- no non-Haar, non-Koopman, infinite-dimensional, boundary, scattering, or
  enlarged carrier is excluded;
- no replacement carrier, moment bridge, cocycle realization, Weil-positive
  form, decoder, or physical lift is constructed;
- no finite prefix or finite fit is excluded: the hypothesis and conclusion
  concern one exact realization for every `n >= 1`; and
- Pillar A's algebraic and periodic content is not falsified.

RH remains open.

## 5. Promotion posture

After reviewed merge and public byte readback, this file is an owner ruling,
not a normative claim.  A separate sealed Canon fold may add exactly
`J-LI-TORAL-HAAR-NOGO [T]`, at L6, with evidence
`probes/P-J-LI-TORAL-HAAR-1` and the scope in section 2.  The fold may add the
single dependency on `J-STEP` needed for the named `M_J` specialization.

The fold must leave `J-LI-SPECTRAL-TARGET`, the positive-route alias, every
replacement realization, Weil positivity, and RH unregistered and open.
It must not promote the conditional accumulation asymptotic as a separate
claim.

No Canon, registry, frontier, status, release, or tag file changes occur on
this ruling branch.
