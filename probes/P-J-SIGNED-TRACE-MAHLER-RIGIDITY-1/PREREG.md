# P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1 preregistration

Date: 2026-08-25

Author of record: A. M. Thorn

Status: preregistered protocol only. Formal execution count zero. No
scientific result is earned by this file. The accepted `verify.py` may be
read, parsed, compiled, and inspected statically before the pin, but it has
not been imported or executed. This file and `verify.py` must be committed
together, pushed, and read back byte for byte from the public remote before
the first formal scientific execution.

Public claim lock: issue 562, opened before this file was committed.

```text
branch:  probe/P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1
path:    probes/P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1/
owner:   A. M. Thorn
mode:    RESULT-EXPOSED, proof-first; the verifier is an exact audit
```

## Authority

```text
STATE:          ACTIVE
CANON:          Public Canon v63
AUTHORITY:      mathorn1973/twist-j main
TAG:            canon-v63
TAG_TARGET:     0b7182b865a5abb8d114d0361f8e2f8c9f9a0d9c
CONTENT_COMMIT: 253f026c56d04dddc5a7a1936fbd7c70bb0f1de7
CANON_SHA256:   3696bbb17f0a961d545cdfd7e589de7a8c6ae269fec1847142b20581260f19d9
CANON_BYTES:    334109
BASE_COMMIT:    0b7182b865a5abb8d114d0361f8e2f8c9f9a0d9c
ACTION_LAYER:   L1 exact characteristic-polynomial algebra only
```

Immediately before issue lock and branch creation, public `main`, the complete
remote-ref set, open and closed issues and pull requests, `STATUS.md`,
`POLICY.md`, `AGENTS.md`, `canon/SHA256SUMS`, the registry, frontier,
dependencies, evidence, gates, and public probes were read from a clean v63
checkout. The tag target and content commit are ancestors of `main`; the
recomputed Canon hash and byte count match `STATUS.md`; policy, Canon, ledger,
gate-contract, unit, and Linux reproduction checks pass.

This probe changes exactly its own directory. It changes no Canon, registry,
frontier, dependency, evidence, gate, release, or workflow file.

## Collision search and adjacent ownership

No issue, pull request, remote branch, public probe path, registry row, object
lock, or claim lock named `P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1` or
`J-SIGNED-TRACE-MAHLER-RIGIDITY` existed at lock time. Searches also covered
`SIGNED-TRACE`, `SINGER-MAHLER`, and `MAHLER-RIGIDITY` aliases.

Adjacent public objects retain their existing ownership:

```text
J-MAHLER-MEASURE [T]
  owns the characteristic polynomial of J, its exact Mahler value phi^2,
  and the target root-modulus split. Those facts are target controls here;
  the new object is global minimality inside a frozen signed-trace class.

J-BINARY-NORM-DESCENT [T]
  owns the binary norm-trace structure and its explicit no-selector guard.

J-BINARY-NORM-INDEX [T]
  owns the inert-prime norm-one index and order-15 attainment.

CARRY-PENTAD [T]
  owns its fixed order-five/binary-width statement and no-selection guards.

J-ODD-MOTOR-MEDIATED-BRIDGE [T]
  owns its native sector and mediated-block theorem on M_J.
```

The last four objects provide no Mahler-minimality premise and acquire no
reverse dependency. The negative broad-Singer controls below reinforce, and
do not weaken, their no-selector boundaries.

## Result exposure

`RESULT-EXPOSED`, not blind. The four tier decisions, coefficient counts,
candidate witnesses, proof, and several exact implementations were already
derived and executed on the noncanonical branch
`notes/C-J-SINGER-MAHLER-LIFT-1-N`, incubation pin
`49ce4081e021171bc4c8c79a3fc7ffe4a496ea1a`, result head
`8f5a36f3d3e7d838ee61e2b2b30600752e133a34`. Those files, hashes, transcripts,
breaker history, and promotion proposal are discovery context only. They are
not evidence for this probe, and no blindness claim is made here.

The accepted public `verify.py` is newly authored for this identifier, uses a
different exact root-count route, and has never been imported or executed at
pin time. Its exposed constants are preregistered thresholds, not discoveries.
The public theorem rests on the self-contained written proof below; the
verifier audits its finite counterexample surface and exact controls.

## Field 1: equation, classes, and theorem

For integers `a,b,c`, put

```text
f_(a,b,c)(X) = X^4 + a X^3 + b X^2 + c X + 1,
f_J(X)       = X^4 - 3 X^3 + 4 X^2 - 2 X + 1
             = Phi_5(X - 1),
tau          = phi^2 = (3 + sqrt(5))/2.
```

For roots `alpha_1,...,alpha_4`, define

```text
M(f) = product_i max(1, |alpha_i|).
```

Call `f` admissible exactly when it has no root on the unit circle and has
exactly two roots, counted with multiplicity, in `|z|>1` and two in `|z|<1`.

Over `F_2`, freeze the two primitive monic quartics

```text
p_L = X^4 + X + 1,
p_R = X^4 + X^3 + 1.
```

Freeze the nested classes before execution:

```text
A0 SINGER:
   f is admissible and f mod 2 is p_L or p_R.

A1 ORIENTED:
   f is admissible and f mod 2 is p_R.

A2 SIGNED TRACE:
   f is in A1 and a = -3, equivalently Tr(C_f) = 3.

A3 DISPLACEMENT UNIT:
   f is in A2 and f(1) = 1, equivalently det(I-C_f) = 1.
```

The nesting `A3 subset A2 subset A1 subset A0` is immutable. No extra
condition may be added after the pin.

For each tier define

```text
J_MIN(A_r):  every f in A_r has M(f) >= tau,
             with equality if and only if f = f_J.
```

The exposed candidate decisions, now frozen as thresholds rather than assumed
as public results, are

```text
A0  FALSE by an exact F-LOWER and non-target F-TIE;
A1  FALSE by an exact F-LOWER and non-target F-TIE;
A2  TRUE globally, with f_J the unique equality case;
A3  TRUE as a corollary, with the same unique equality case.
```

The frozen negative controls are

```text
h(X)=X^4-X^3+1  in A1, with M(h) <= sqrt(3) < tau;
f_J(-X)          a distinct A1 equality witness;
X^4 f_J(1/X)     a distinct p_L equality witness in A0.
```

The maximum later theorem is

```text
J-SIGNED-TRACE-MAHLER-RIGIDITY [T], L1
```

with the statement: if

```text
f(X)=X^4-3X^3+bX^2+cX+1 in Z[X],  b,c even,
```

is admissible, then `M(f)>=phi^2`, with equality exactly for
`f=Phi_5(X-1)`. The broader primitive binary Singer class, including its
`p_R`-oriented subclass, does not satisfy this lower bound or uniqueness.
Signed trace is therefore the first sufficient condition only in the frozen
A0-A3 ladder; reduction modulo two alone is not a selector. A3 earns no
second claim because `f(1)=1` is unnecessary for the A2 theorem.

### Written proof: the two negative tiers

Take `h(X)=X^4-X^3+1`. Modulo two it is `p_R`, hence lies in A1 whenever it
is admissible. If `|z|=1` and `h(z)=0`, then `z^3(z-1)=-1`, so `|z-1|=1`.
Together with `|z|=1`, this gives `z+z^-1=1`, hence `z^3=-1`; substitution
then forces `z=2`, impossible. Thus `h` has no unit-circle root.

For real `x<=0`, `h(x)>0`. For `x>=0`, its only nonzero critical point is
`x=3/4`, where `h(3/4)=229/256>0`; hence it has no real root. Its roots form
two conjugate pairs, their modulus product is one, and none has modulus one,
so exactly one pair lies outside and one inside. Jensen, quadratic mean, and
Parseval give the exact Landau bound

```text
M(h) <= sqrt(1^2+(-1)^2+1^2) = sqrt(3) < 2 < tau.
```

This is F-LOWER for A1 and A0. Independently, `f_J(-X)` is distinct from
`f_J`, remains in A1, and has the same root moduli; it is F-TIE for A1 and A0.
The reciprocal `X^4 f_J(1/X)` is a second equality control in the `p_L`
branch of A0.

### Written proof: preliminary A2 facts

In A2, `a=-3` and `b,c` are even, so `f mod 2=p_R`. The polynomial `p_R` has
no root in `F_2`, and at a root of the only irreducible quadratic
`X^2+X+1` it has nonzero value `X`. Thus `p_R` is irreducible; every A2
polynomial is irreducible over `Q` and separable.

For both `p_L` and `p_R`, the residue class of `X` also satisfies the exact
finite-field certificate

```text
X^15 = 1,  X^5 != 1,  X^3 != 1  (mod p_L or p_R),
```

so its order is exactly fifteen. The verifier checks both reductions rather
than inferring primitivity from irreducibility alone.

Set

```text
E=f(1)=b+c-1,
A=f(-1)=b-c+5.
```

Both are nonzero odd integers. If `N_+` counts real roots greater than one
and `N_-` real roots less than minus one, factorization at `1` and `-1` gives
`sign(E)=(-1)^N_+` and `sign(A)=(-1)^N_-`. Nonreal outside roots occur in
conjugate pairs, while exactly two roots are outside, so `N_+` and `N_-` have
the same parity. Therefore `E,A` have the same sign, leaving only the two
cases below.

### Written proof: exterior resolvent

For roots `r_1,...,r_4`, direct expansion in the elementary symmetric
functions gives

```text
G(Y) = product_(i<j) (Y-r_i r_j)
     = Y^6-bY^5+(ac-1)Y^4-(a^2+c^2-2b)Y^3
       +(ac-1)Y^2-bY+1
     = Y^3 H(Y+Y^-1),

H(Z) = Z^3-bZ^2+(ac-4)Z+(4b-a^2-c^2).
```

The three roots of `H` correspond to the three complementary pairings of the
four roots.

### Written proof: positive-sign branch

Assume `E,A>0`. If the outside roots are nonreal, they are conjugate and
their product is positive. If real, the sign conditions put them both above
one or both below minus one. The latter is impossible: their sum is below
`-2`, the real sum of the two inside roots has absolute value below `2`, but
the total root sum is `3`. Hence the outside product is always
`M=M(f)>1`, and its `H` root is `X_0=M+M^-1>2`.

For either cross product `q=alpha_i beta_j`, where `alpha` is outside and
`beta` inside,

```text
M^-1 < |q| < M.
```

If `X=q+q^-1` is real, then either `|q|=1`, giving `X in [-2,2]`, or `q` is
real. Negative `q` gives `X<=-2`; positive `q`, under `M<=tau`, gives
`X<M+M^-1<=3`. If the two cross values are nonreal they are conjugates.
Consequently, whenever `M<=tau`,

```text
C=(3-X_1)(3-X_2)>0,
H(3)=(3-M-M^-1) C.
```

Since `t+t^-1` is strictly increasing for `t>1`, this proves the precisely
scoped implication

```text
M<=tau  implies  H(3)>=0,
```

with equality exactly at `M=tau` within that scope.

At `a=-3`,

```text
D=H(3)=6-5b-9c-c^2.
```

If `M<=tau`, then `D>=0`; and `E>0` gives `b>1-c`. Hence

```text
5(1-c) < 5b <= 6-9c-c^2,
```

so `(c+2)^2<5`. Even `c` leaves only `-4,-2,0`. The cases `c=-4` and `c=0`
contradict `D>=0` and the least allowed even `b`; the case `c=-2` forces
`b>=4` from `E>0` and `b<=4` from `D>=0`. Thus `b=4,c=-2` and `f=f_J`.

### Written proof: negative-sign branch

Assume `E,A<0`. Since `f(0)=1` and a monic quartic tends to positive infinity
at both ends, there is one root in each of

```text
(-infinity,-1), (-1,0), (0,1), (1,infinity).
```

Write them `-Y,-v,u,X`, with `X,Y>1` and `0<u,v<1`. Then

```text
M=XY,  uv=M^-1,  3=X-Y+u-v.
```

Because `Y>1`, `X=M/Y<M` and `X-Y<M-1`. Because `u<1` and
`uv=M^-1`, `v>M^-1` and `u-v<1-M^-1`. Therefore

```text
3 < M-M^-1,
M > (3+sqrt(13))/2 > (3+sqrt(5))/2 = tau.
```

This branch cannot contain a counterexample or equality.

### Written proof: completion and A3

The sign cases exhaust A2. The positive branch forces `f_J` whenever
`M<=tau`, and the negative branch has a strict larger lower bound. Finally,
`f_J=Phi_5(X-1)` has roots `1+zeta_5^k` with moduli
`phi,phi,phi^-1,phi^-1`, so it is admissible and `M(f_J)=tau`.

A3 is a subclass. Directly, `f(1)=1` gives `b+c=2`, and therefore

```text
H(3)=-(c+2)^2.
```

Under `M<=tau`, the positive comparison requires `H(3)>=0`, forcing
`c=-2,b=4`. This is only a fingerprint for the same theorem, not a new
selector.

## Field 2: accepted code

Accepted file:

```text
probes/P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1/verify.py
```

Python 3.12 standard library only. It uses integers, `Fraction`, polynomial
Euclidean arithmetic, Sturm sequences, a Cayley transform, a Bezoutian
half-plane count, and exact symmetric-form inertia. It contains no float,
tolerance, NumPy, SymPy, randomness, network, subprocess, filesystem read or
write, environment-dependent output, timing, hostname, or path field.

The verifier has zero arguments, deterministic compact stdout, empty stderr
on a completed result, and a 120-second local runtime ceiling. It uses
explicit fail gates, not decision-bearing `assert`. Internal algebra or
integrity failure exits nonzero and is `STOP`; a completed mathematical
falsifier prints the fired decision and exits zero.

For root counting, define

```text
Q_f(W)=(W-1)^4 f((W+1)/(W-1)).
```

The map `W=(z+1)/(z-1)` sends `|z|>1` to the right half-plane, `|z|<1` to
the left half-plane, and the unit circle to the imaginary axis. Writing
`Q_f(iT)=R(T)+iI(T)`, the signature of the exact Bezoutian

```text
(R(X)I(Y)-R(Y)I(X))/(X-Y)
```

is the right-minus-left root count; its positive and negative inertia give
the outside and inside counts, while nullity detects a unit-circle root in
the frozen parity classes. This is the Hermite-Bezout inertia theorem, with
algebraic multiplicities. Here `f(1)` and `f(-1)` are odd and nonzero, while
the Cayley cubic coefficient is `2(a-c)` and is nonzero by the frozen parity.
If `R,I` shared a nonreal root, `Q_f` would contain an opposite pair `W,-W`,
which corresponds to a reciprocal pair `z,z^-1`. For a real constant-one
quartic without unit roots that forces full reciprocity and hence `a=c`,
again excluded by parity. Thus a null Bezoutian direction on this carrier is
exactly an imaginary-axis, hence unit-circle, root rather than an unobserved
reciprocal-pair degeneracy. The code calibrates the orientation on fixed
linear and nonsymmetric quadratic controls before using it.

For admissible 2/2 polynomials, the outside pair product has modulus `M`, and
every cross product lies in the strict annulus `(M^-1,M)`. Hence a real root
of `H` strictly outside `[-3,3]` is equivalent to `M>tau`; endpoint roots are
retained. Sturm sequences count those strict roots exactly. This route is
distinct from the incubation verifier.

## Field 3: carrier

```text
coefficient carrier:
  (a,b,c) in Z^3, monic degree-four constant-one polynomials

matrix convention:
  det(XI-C_f)=f(X), Tr(C_f)=-a, det(I-C_f)=f(1)

binary carrier:
  F_2[X]/(p_L) or F_2[X]/(p_R); the root has exact order 15

comparison carrier:
  exact Cayley/Bezout root counts, exact Sturm counts for H,
  and tau in Q(sqrt(5)) with no numerical embedding
```

This carrier is not an integral conjugacy class, ideal class, marked lift,
matrix basis, or canonical realization.

## Field 4: systematics and complete window

For any monic quartic with `M(f)<=tau`, the elementary-symmetric bound

```text
|coefficient_k| <= binom(4,k) M(f)
```

and the exact inequalities

```text
4 tau = 6+2sqrt(5) < 11,
6 tau = 9+3sqrt(5) < 16
```

give the complete integer window

```text
-10 <= a,c <= 10,
-15 <= b   <= 15.
```

The frozen pre-admissibility coefficient-candidate counts in this window are

```text
A0 surface  3300
A1 surface  1650
A2 surface   165
A3 surface    11
```

These are parity/trace/displacement surfaces before the exact admissibility
test, not cardinalities of the already-admissible classes. A0/A1 use these
counts as coverage controls and are decided negatively by the frozen exact
witnesses. The positive A2/A3 surfaces receive the rowwise root/resolvent
admissibility audit below, without silently dropping a candidate row.

The exposed exact audit thresholds are

```text
A2:
  127 rows have an H root strictly outside [-3,3];
   38 residual rows remain;
   their outside-root counts are 29 with 3, 8 with 1, 1 with 2;
   the unique admissible residual is (b,c)=(4,-2).

A3:
  10 rows have an H root strictly outside [-3,3];
   1 residual row remains, (b,c)=(4,-2), with a 2/2 split.
```

The Cayley/Bezout outside-root profiles count algebraic multiplicity. The
Sturm test counts distinct strict `H` roots, but only its exact zero/nonzero
existence decision is used; `H_outside` is a count of candidate rows, not a
sum of root multiplicities. Roots at `H(3)=0` or `H(-3)=0` are not strictly
outside. Unit-circle roots, null Bezoutians, polynomial-remainder defects, or
asymmetric forms cannot be silently classified. Numerical roots and finite
scans carry no universal quantifier; the written proof does.

## Field 5: failure threshold and decision

Thresholds never move after this pin.

```text
J-SIGNED-TRACE-MAHLER-RIGIDITY-CONFIRMED
  all binary, target, witness, exact-window, A2, and A3 checks pass; A0 and A1
  are false by the frozen exact controls; A2 and A3 have f_J as their unique
  at-or-below-tau admissible polynomial; the written global proof is intact.

J-SIGNED-TRACE-MAHLER-RIGIDITY-FIRED
  a completed exact calculation fires any scientific falsifier below. The
  exact outcome is preserved and merged; no class, threshold, or wording is
  changed to rescue the route.

STOP
  authority, collision, pin, readback, exactness, internal-algebra,
  deterministic-output, stderr, mutation, security, runtime, or architecture
  integrity fails. A verifier defect preventing a completed formal run spends
  this identifier and requires an ABANDONED record under POLICY.md.
```

Frozen falsifiers:

```text
F1  f_J fails any coefficient, parity, binary, admissibility, root-split,
    Phi_5 shift, H factor, or M(f_J)=tau control;
F2  h is not an admissible A1 strict-lower witness, or either displayed tie
    is not in its frozen class with the target Mahler measure;
F3  an admissible A2 polynomial has M(f)<tau;
F4  an admissible A2 polynomial other than f_J has M(f)=tau;
F5  the exterior resolvent, sign split, H(3) implication, negative-sign gap,
    or A3 square fingerprint fails exactly;
F6  the frozen coefficient-candidate surfaces have a different cardinality,
    omit an eligible candidate row, contradict the theorem, or the exact root
    routes are inconsistent;
F7  A3 contains an admissible polynomial at or below tau other than f_J.
```

The verifier audits F1, F2, F6, F7 and the complete at-or-below-threshold
surface relevant to F3/F4. The self-contained proof carries F3-F5 globally.

## Field 6: action layer and scope firewall

`L1` exact characteristic-polynomial algebra only.

This probe does not classify integral matrix conjugacy classes, ideal classes,
marked lifts, bases, or integral realizations. It does not derive or select the
signed trace from `J`, claim that the condition is necessary outside A0-A3,
or select a binary orientation, axiom exponent, rational prime,
characteristic-two place, or order-five cycle.

It makes no decoder, event, apparatus, probability, Born-law, dynamics,
entropy, spacetime, force, SI-value, physical-generation, or L2-L6 statement.
In particular, the integer `3` in the trace is not a reading of
`GENERATIONS-L3`.

```text
SAMPLING NOT PROVIDED.
```

## Formal order

1. Commit only this `PREREG.md` and the never-executed accepted `verify.py`
   together; push the full pin commit.
2. In a separate clean checkout, read both files back from that immutable
   public commit and record SHA-256, bytes, lines, LF, and final LF.
3. Only then run, from the repository root, exactly
   `python3 probes/P-J-SIGNED-TRACE-MAHLER-RIGIDITY-1/verify.py` in a neutral
   Linux environment with empty stderr.
4. Commit only `EXPECTED.txt`, `RUN.md`, and `RESULT.md` afterward. Never alter
   either pinned file.
5. Open one probe-only pull request. Require byte-identical Python 3.12 output
   on GitHub x86_64 and aarch64 plus aggregate `check`.
6. Merge with a merge commit only. Never amend, rebase, squash, force-push,
   rename, resume, or reuse this identifier after the pin.
7. Any registry or Canon treatment is a separately locked later fold.
