# C-LI-S2-RELATIVE-DETERMINANT-1. S2 rigidity, Fredholm polarization, and the next positive target

```text
CANDIDATE ID:   C-LI-S2-RELATIVE-DETERMINANT-1
DATE:           2026-07-16
TARGET ROWS:    J-LI-S2-NORMAL-FORM
                J-LI-S2-SPECTRAL-RIGIDITY
                J-LI-S2-COCYCLE-REDUCTION
                J-LI-SCHATTEN-BOUNDARY
                J-LI-POSITIVE-FREDHOLM-EQUIVALENCE
                J-LI-S2-FREDHOLM-POLARIZATION
                J-XI-STIELTJES-HANKEL-EQUIVALENCE
                J-LI-CAYLEY-COUNTING-GATE
                J-LI-TORAL-HAAR-DIRECT-NOGO
                J-LI-IDEAL-FOCK-DIRECT-NOGO
                J-LI-S2-RELATIVE-DETERMINANT-REALIZATION
PARENTS:        PENTAGON-NORMALIZATION; C-LI-COCYCLE-1 through amendment 4;
                notes/j-li-schoenberg-2; C-LI-TORAL-HAAR-1
LAYER:          L6 measure/operator ideal
AUTHORITY:      none. NON-CANONICAL candidate document under POLICY.md.
PUBLIC STATUS:  no registry row, no Canon promotion, no formal probe.
RH:             O.
```

## 0. Result and non-result

This candidate fixes the exact operator class of an all-n positive Li
realization and removes a remaining spectral ambiguity.  It gives two
equivalent positive normal forms and a second sequence of finite kill tests:

```text
real form       an orthogonal O with I-O in S2;
complex form    a positive trace-class A with a polarized Fredholm determinant;
finite tests    shifted Hankel matrices of the logarithmic-derivative moments.
```

It does **not** construct the required object from J.  It does not prove RH.
The word `relative` in the candidate ID names the intended future
architecture.  No pair of parent operators and no perturbation determinant is
yet defined, so the current proved statements use the ordinary Fredholm
determinant `det_1`.

## 1. Falsifiers first

A proposed J-native realization fails if any one of the following occurs.

1. `A_J` is not positive, not trace class, or has finite rank.
2. `sqrt(A_J)` is trace class while the proposal claims the exact Li Schatten
   boundary.
3. A real rotation realization is assigned the unsquared Xi determinant
   without a positive-frequency polarization (or an explicitly equivalent
   Pfaffian construction).
4. The determinant is not `det_1`, or its normalization at zero is not one.
5. The trivial C4 sector uses raw `P_0` rather than `Z_J=P_0/f_5`, or omits
   the ramified local block at 5.
6. G4 imports the global identity reserved for G8.
7. A direct-carrier no-go is presented as excluding a relative determinant,
   scattering construction, transfer operator, or an arbitrary cocycle.
8. Zeta, Xi, a zero list, a prime table, Li coefficients, or the standard Weil
   form enters the construction as an undeclared input.
9. Any exactly derived shifted Hankel matrix below has a negative direction.

Failure of a proposed construction before its equality with Xi is proved
kills that construction, not RH.

## 2. Imported classical inputs

The analytic proofs below import, and do not reprove:

- Li's criterion: RH iff all Li coefficients are nonnegative;
- the functional equation, reality, and Hadamard product of Riemann's xi;
- Fourier uniqueness for finite measures on the circle;
- the spectral theorem for normal compact perturbations of the identity;
- the Riemann-von Mangoldt zero count;
- the Stieltjes moment theorem.

The included verifier checks only finite exact dictionaries.  It does not
promote these imported theorems into TWIST-J results.

## 3. Hilbert-Schmidt normal form

Let

```text
Xi(t) = xi(1/2 + i t),       Xi(0) != 0,
```

and let `lambda_n` be the standard Li coefficients.  Then

```text
RH
<=> there are a separable real Hilbert space H_R and an orthogonal O such that
    I-O is Hilbert-Schmidt and
    lambda_n = (1/2) ||I-O^n||_S2^2 for every n >= 1.
```

Under RH, write the zeros as `1/2 +- i gamma`, `gamma>0`, with multiplicity
`m_gamma`, and define

```text
O_xi = direct_sum_(gamma>0) R(theta_gamma)^(m_gamma),
exp(i theta_gamma) = (gamma+i/2)/(gamma-i/2).
```

For one real rotation block,

```text
||I-R(theta_gamma)||_S2^2 = 2/(gamma^2+1/4),
(1/2)||I-R(n theta_gamma)||_S2^2 = 2(1-cos(n theta_gamma)).
```

The zero count makes the first sum finite.  Summing the second identity gives
the Li coefficient.  Conversely, the displayed norm is nonnegative for every
`n`; Li's criterion gives RH.

The operator is not unique: any identity summand is invisible.  The next
section proves that this is the only freedom.

## 4. Spectral rigidity

Complexify `O`.  Because `I-O` is compact and `O` is normal, its spectrum off
`1` is pure point with finite multiplicities.  Let `nu_O` be the corresponding
counting measure on the unit circle minus `{1}`, including multiplicity, and
define the finite conjugation-invariant measure

```text
d sigma_O(z) = |1-z|^2 d nu_O(z).
```

The norm identity gives

```text
sigma_O(T) = 2 lambda_1.
```

For `lambda_0=0`, `lambda_-n=lambda_n`, and

```text
t_n = lambda_(n+1) + lambda_(n-1) - 2 lambda_n,
```

a block calculation gives

```text
t_n = integral_T z^n d sigma_O(z).
```

All Fourier coefficients of the finite measure are therefore fixed by the Li
ladder.  Fourier uniqueness fixes `sigma_O`, and off `1` one recovers

```text
d nu_O(z) = |1-z|^(-2) d sigma_O(z).
```

Thus every exact S2 witness has the same nonidentity eigenangles and
multiplicities as `O_xi`.  Two minimal witnesses are orthogonally equivalent;
the only unobservable freedom is the dimension of `ker(I-O)`.

This closes the all-witness version of the Schatten boundary rather than only
the zero-built example.

## 5. Schatten boundary and counting gate

The nonzero singular values of `I-O` are

```text
s_gamma = 1/sqrt(gamma^2+1/4),
```

twice per positive zero ordinate, with multiplicity.  With one fixed boundary
convention for the counting functions,

```text
N_(I-O)(epsilon)
  = 2 N(sqrt(epsilon^(-2)-1/4))
  = (1/(pi epsilon))(log(1/(2 pi epsilon))-1)
    + O(log(1/epsilon)).
```

Consequently

```text
I-O is in S_p  <=>  p>1,
s_k ~ (log k)/(pi k).
```

The precise wording is: `O` is a compact perturbation of the identity.  The
orthogonal operator itself is not compact on the infinite-dimensional target.

More generally, for a positive discrete Hamiltonian `H e_j=h_j e_j` and its
Cayley operator

```text
Q_H=(H+i/2)(H-i/2)^(-1),
```

one has

```text
s_j(I-Q_H)=1/sqrt(h_j^2+1/4),
N_(I-Q_H)(epsilon)=N_H(sqrt(epsilon^(-2)-1/4)).
```

A direct Li identification therefore forces the Riemann-von Mangoldt counting
law for `H`, with the factor two restored on realification.

## 6. Canonical cocycle relative to O

On `K=S2(H_R)` define

```text
U(X)=O X,                  v=(I-O)/sqrt(2).
```

Each difference below is Hilbert-Schmidt, and telescoping in the bounded
operators gives

```text
sum_(k=0)^(n-1) U^k v = (I-O^n)/sqrt(2),
lambda_n = ||sum_(k=0)^(n-1) U^k v||_K^2.
```

The vector is forced relative to the selected `O`.  This does not assert that
an arbitrary earlier cocycle witness is automatically of this S2 form.

## 7. Positive Fredholm normal form

There is a second exact equivalence:

```text
RH
<=> there is a complex Hilbert space and A=A*>=0, A in S1, such that
    Xi(t)/Xi(0) = det_1(I-t^2 A) as an identity of entire functions.
```

Under RH, take one positive-frequency copy of each zero pair and set

```text
A e_(gamma,r) = gamma^(-2) e_(gamma,r),  1 <= r <= m_gamma.
```

The zero count gives `A in S1`.  Pairing opposite zeros makes the product
absolutely convergent:

```text
Xi(t)/Xi(0) = product_(gamma>0) (1-t^2/gamma^2)^(m_gamma).
```

Any residual Hadamard factor is `exp(a+b t)`; evenness gives `b=0` and the
normalization at zero gives `exp(a)=1`.  Conversely, the zeros of the
determinant of a positive operator are real and occur at `+-a_j^(-1/2)`, so
the entire-function identity implies RH.

The determinant does not see a kernel.  The minimal positive operator is
unique up to unitary equivalence on its nonzero spectral subspace.

Define

```text
B_A=(I-A/4)(I+A/4)^(-1).
```

Then `B_A` is a self-adjoint contraction, `I-B_A` is trace class, and

```text
lambda_n = 2 Tr[I-T_n(B_A)].
```

The bracket is trace class.  It must not be split into the two generally
undefined traces `Tr I - Tr T_n(B_A)`.

## 8. Exact A-to-O map and mandatory polarization

Given `A>=0`, define on its complex Hilbert space

```text
Z_A=(I+(i/2)sqrt(A))(I-(i/2)sqrt(A))^(-1).
```

Its realification is orthogonal.  On an eigenvalue `a`,

```text
exp(i theta(a)) = (1+i sqrt(a)/2)/(1-i sqrt(a)/2),
cos(theta(a))   = (1-a/4)/(1+a/4),
|1-exp(i theta(a))|^2 = a/(1+a/4).
```

Therefore `A in S1` implies `I-O_A in S2`.  The exact non-trace-class
boundary additionally requires `sqrt(A) not in S1`.

Conversely, if `-1` is absent from the nonidentity spectrum of `O`, put

```text
D_O     = (I-O)*(I-O),
A_R     = D_O (I-D_O/4)^(-1).
```

Equivalently, with `C_O=2(I-O)(I+O)^(-1)`, `A_R=-C_O^2`.  A rotation block
has the eigenvalue `gamma^(-2)` twice.  Thus the real determinant is

```text
det_R(I-t^2 A_R) = (Xi(t)/Xi(0))^2.
```

To obtain one copy, complexify and restrict to the positive-frequency
spectral subspace `H_+=E_O({Im z>0})H_C`.  The polarized restriction `A_+`
then has

```text
det_C(I-t^2 A_+) = Xi(t)/Xi(0).
```

Any unsquared real determinant without this polarization has the wrong
multiplicity.

## 9. Stieltjes-Hankel normal form

The Fredholm target yields a second all-order positivity ladder.  Because Xi
is even, define the entire function

```text
G(x)=Xi(sqrt(x))/Xi(0),       G(0)=1,
-G'(x)/G(x)=sum_(n>=0) q_n x^n near x=0.
```

Then

```text
RH
<=> H_N^(0)=(q_(i+j))_(i,j=0..N) >= 0 and
    H_N^(1)=(q_(i+j+1))_(i,j=0..N) >= 0 for every N.
```

Under RH, `q_n=Tr(A_xi^(n+1))`.  Hence for every polynomial `p`,

```text
c* H_N^(0) c = Tr[A_xi |p(A_xi)|^2] >= 0,
c* H_N^(1) c = Tr[A_xi^2 |p(A_xi)|^2] >= 0.
```

The inequalities are strict for nonzero `c` because the target spectrum has
infinite support.

Conversely, the two Hankel families give a Stieltjes moment measure `eta` on
`[0,infinity)`.  Cauchy bounds for the analytic germ supply an exponential
bound on `q_n`; moment positivity then forces `eta` to have compact support.
Its Stieltjes transform

```text
S(x)=integral d eta(a)/(1-a x)
```

has the same germ as `-G'/G`.  Analytic continuation on the slit plane shows
that `G` can have no zero off the positive real axis: such a zero would give a
pole of `-G'/G` where `S` is analytic.  Hence all zeros of Xi are real and RH
follows.  At a positive zero `x_j=1/a_j`, residue comparison gives

```text
eta({a_j})=m_j a_j.
```

Because `G` has order `1/2<1`, no nonconstant exponential factor remains.
The compact moment problem is determinate, so there is no additional
continuous component or atom at zero.  Thus the positive trace-class
Fredholm spectrum and its integer multiplicities are recovered.  This is a
proof-first equivalence; a finite positive Hankel prefix is only a calibration.

If `G(x)=1+sum_(k>=1) g_k x^k`, the moments are generated without a formal
logarithm by

```text
q_n=-(n+1)g_(n+1)-sum_(k=1)^n g_k q_(n-k).
```

This creates a second finite falsifier ladder beside the Li-Schoenberg
matrices.  A negative exact Hankel minor kills the claimed global positive
realization.  A mismatch in a proposed J-derived `q_n` kills that construction,
not RH.

## 10. Direct-carrier no-go results: exact scope

### 10.1 Toral Haar-Koopman

On any infinite character orbit of the Pillar A Koopman operator, take the
orthonormal sequence `e_k`.  Then

```text
||(I-K_J)e_k||=sqrt(2),       e_k -> 0 weakly.
```

Thus `I-K_J` is not compact and is not Hilbert-Schmidt.  This excludes only
the direct identification `O_J=K_J`.  It does not replace the stronger
atomic-versus-absolutely-continuous no-go in `C-LI-TORAL-HAAR-1`, which is
still required to exclude every cocycle vector for the fixed Koopman carrier.

### 10.2 Native ideal/Fock occupation spectrum

For `H_B e_n=(log n)e_n` and

```text
Q_B=(H_B+i/2)(H_B-i/2)^(-1),
```

the exact defect is

```text
||I-Q_B||_S2^2
  = 4 + sum_(n>=2) 1/((log n)^2+1/4)
  = infinity.
```

In fact `I-Q_B` is compact but belongs to no finite Schatten class.  Dyadic
blocks already give an exponentially growing lower bound.  The full ideal
Hamiltonian fails by the principal-ideal subsequence `(m)`, `N((m))=m^4`.

This falsifies only the direct native occupation/Cayley identification.  It
does not falsify Pillar B, a relative determinant, scattering, or a transfer
operator.

## 11. Gates for the surviving construction

```text
G0  Freeze the J-only dependency graph for A_J.

G1  Freeze the complex Hilbert space, adjunction, multiplicities, and the
    positive-frequency polarization.

G2  Prove A_J=A_J*>=0, A_J in S1, rank(A_J)=infinity; for the exact boundary,
    also sqrt(A_J) not in S1.

G3  Use det_1 and D_J(0)=1.  The trivial C4 sector is built from
    Z_J=P_0/f_5, not raw P_0, including the local block at 5.

G4  Check only frozen local/coefficient accounting: declared Taylor or
    log-derivative coefficients, Gamma terms, von Mangoldt terms, and filter
    subtraction on a named test domain.  G4 is not a global identity of
    meromorphic functions.

G5  Produce lambda_1, lambda_2, lambda_3, K_2, K_3, and the first declared
    Hankel moments as outputs, never inputs.

G6  Apply the explicit polarized A-to-O map; prove I-O_J in S2 and
    sqrt(A_J) not in S1.  Prevent determinant doubling.

G7  Audit that zeta, Xi, zeros, primes, Li coefficients, and the standard
    Weil form are not hidden construction inputs.

G8  Prove det_1(I-t^2 A_J)=Xi_J(t)/Xi_J(0) as an identity of entire functions.
```

If G4 were strengthened to equality of the full logarithmic derivatives on
an open connected region, together with normalization at zero it would
already imply G8.  G4 and G8 must not duplicate one another.  G8 is proof
only; no finite verifier can certify it.

If a future proposal truly uses a relative determinant, it must additionally
freeze the parent operator pair, common domain, resolvent-comparability or
trace-class perturbation, determinant quotient, and normalization.  Until
then `relative` remains a program label, not a proved construction.

## 12. Exact machine audit

`verify_s2_relative_determinant.py` is a stdlib-only exact dictionary audit.
It checks:

```text
S1  Cayley rotation and one-block Hilbert-Schmidt factors;
S2  block Li formula and the canonical cocycle telescope;
S3  weighted spectral moments and Li second differences;
S4  A-to-O map, B_A, and the Chebyshev trace dictionary;
S5  the real-versus-complex determinant square;
S6  Fredholm logarithmic-derivative coefficients p_m=Tr(A^m);
S7  two shifted Hankel families on an exact finite model;
S8  direct-Cayley carrier obstruction skeletons with restricted scope.
```

All asserted values use integers or `fractions.Fraction`.  The analytic
theorems remain proof-first imports.  The run is a non-formal prep audit, not a
public reproduction and not a probe execution.

```text
verifier sha256  c6158ce8f3321fb6247ac96e5d419af742e3ca29d4081ab2edb2e86735db5ca3
verifier bytes   8947
stdout sha256    cf1bb46883313154ae067b369403f7d46c63c9d801a15a0642c50c27d225f6aa
stdout bytes     808
result           8 PASS, 0 FAIL, exit 0, empty stderr; first run
environment      LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
                 PYTHONHASHSEED=0 TZ=UTC; Linux x86_64; Python 3.12.13
scope            non-formal one-environment dictionary audit
```

## 13. Proposed non-public ledger

| Candidate row | Mathematical classification | Public state |
|---|---:|---:|
| `J-LI-S2-NORMAL-FORM` | T as equivalence | unregistered |
| `J-LI-S2-SPECTRAL-RIGIDITY` | T | unregistered |
| `J-LI-S2-COCYCLE-REDUCTION` | T relative to O | unregistered |
| `J-LI-SCHATTEN-BOUNDARY` | T | unregistered |
| `J-LI-POSITIVE-FREDHOLM-EQUIVALENCE` | T as equivalence | unregistered |
| `J-LI-S2-FREDHOLM-POLARIZATION` | T | unregistered |
| `J-XI-STIELTJES-HANKEL-EQUIVALENCE` | T as equivalence | unregistered |
| `J-LI-CAYLEY-COUNTING-GATE` | T, direct scope | unregistered |
| `J-LI-TORAL-HAAR-DIRECT-NOGO` | T, direct scope | unregistered |
| `J-LI-IDEAL-FOCK-DIRECT-NOGO` | T, direct scope | unregistered |
| `J-LI-S2-RELATIVE-DETERMINANT-REALIZATION` | O | unregistered |
| RH | O | unregistered |

The next constructive object is not another finite Li prefix.  It is a
J-derived positive moment functional whose Stieltjes transform passes G0-G7
and whose determinant can face the proof-only G8 wall.
