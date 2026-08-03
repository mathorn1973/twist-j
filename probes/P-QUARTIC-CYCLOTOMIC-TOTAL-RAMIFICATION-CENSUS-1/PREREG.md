# PREREG. P-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS-1

```text
PREREGISTERED CANDIDATE / RESULT-EXPOSED / PROOF-FIRST /
FIRST FORMAL RUN PENDING REMOTE PIN READBACK
```

Public lock: issue
[#256](https://github.com/mathorn1973/twist-j/issues/256), created
`2026-08-03T08:01:05Z` before this branch, path, prospective pin,
verifier execution, or formal data. The issue claims exactly this probe,
branch, path, target, owner, and L1 scope.

Base: Public Canon v32 ACTIVE, tag `canon-v32`, activation commit and branch
parent `f8c4cc64ba4fc21723fc3e715b5a40036ef7b404`, Canon content commit
`b007a9df39e672a7ad30afc6e6c88e13551ab280`, Canon SHA-256
`b303c9690c91125f79748fd9ba890dd21ac1acb49d7125f42aa56970e85b43e5`,
164705 bytes. The tag equals the branch parent, the content commit is its
ancestor, and the x86_64, aarch64, and aggregate jobs passed in public
[workflow run 30760083580](https://github.com/mathorn1973/twist-j/actions/runs/30760083580).

```text
LAYER:  L1 exact arithmetic only. No lift to L2-L6.
TARGET: QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS, proposed T,
        proof-first: classify total ramification in the frozen class of
        full quartic cyclotomic fields and audit the residue-unit groups
        at the totally ramified rational primes.
```

This preregistration earns no scientific status. The target is absent from
the Public Canon v32 registry. Any Canon, registry, dependency, dictionary,
or release disposition is separate reviewed work.

## 0. Chronology, exposure, and independence

The mathematical outcome and its proposed proof skeleton were public before
this branch. The current Codex/GPT seat is therefore a result-exposed builder,
not a blind discoverer or independent breaker. This is a confirmatory
proof-first probe. No execution output from this `verify.py` has been
produced or observed because the file has not been executed, imported, or
used to open any scientific carrier.
`EXPECTED.txt`, `RUN.md`, and `RESULT.md` do not exist at preregistration.

The intended breaker is a fresh independent Claude seat. After this
`PREREG.md` is frozen, that seat receives only this file, Public Canon v32,
and the dependencies declared below. It receives no builder `verify.py`, no
`EXPECTED.txt`, no builder stdout, and no private expected-value handoff. It
must independently author and hash `break.py` before any comparison with the
builder verifier. Model identity alone supplies no independence; the frozen
information firewall does. Current GPT seats must not author `break.py` and
their reviews remain builder-side review only.

The breaker and the required two-architecture replay are distinct controls.
Running the builder verifier on another machine is reproduction, not an
independent construction. Neither control by itself promotes a computation
above the status allowed by policy. Proposed T rests on the complete written
proof below and still requires explicit owner acceptance of its final frozen
scope.

## 1. Equation

### 1.1 Frozen input class

Fix compatible roots of unity in one algebraic closure of `Q`. For every
positive integer `n`, let

```text
K_n   = Q(zeta_n),
Phi_n = the nth cyclotomic polynomial,
O_n   = O_(K_n) = Z[zeta_n].
```

The input class consists only of full cyclotomic fields `K_n` satisfying
`[K_n:Q]=phi(n)=4`, quotiented by equality of fields. Here **full
cyclotomic** means the whole field `Q(zeta_n)`, not an arbitrary quartic
subfield of a higher-degree cyclotomic field. No claim selects degree four or
proves that full cyclotomic fields exhaust another admissible class.

### 1.2 Declared classical theorem inputs

The proof uses exactly these standard algebraic-number-theory theorems:

1. the cyclotomic integral-basis theorem
   `O_(Q(zeta_n))=Z[zeta_n]`;
2. the cyclotomic discriminant formula displayed in section 7.2;
3. Dedekind factorization for a monogenic integral basis, including the
   ramification multiplicities and residue degrees of section 7.3;
4. a rational prime ramifies in a number field if and only if it divides the
   field discriminant;
5. the multiplicative group of a finite field is cyclic.

These are proof inputs, not claims earned by a finite verifier. The verifier
audits their exact small certificates where possible.

### 1.3 Frozen theorem statement

The candidate theorem comprises Q1-Q4 exactly.

**Q1. Index census.**

```text
phi(n)=4 if and only if n is in {5,8,10,12}.
```

**Q2. Field quotient and distinctness.**

```text
Q(zeta_10)=Q(zeta_5),

K_5  = Q(zeta_5),
K_8  = Q(zeta_8),
K_12 = Q(zeta_12)
```

are the three distinct fields in the frozen class, with

```text
disc(K_5)  = 5^3,
disc(K_8)  = 2^8,
disc(K_12) = 2^4 3^2.
```

The equality is explicit: inside `K_5`,

```text
zeta_10 = -zeta_5^3,     zeta_10^2=zeta_5,
zeta_10^5=-1,            zeta_10^10=1.
```

**Q3. Ramification census.** The exact reductions are

```text
Phi_5  mod 5 = (x-1)^4,
Phi_8  mod 2 = (x+1)^4,
Phi_12 mod 2 = (x^2+x+1)^2,
Phi_12 mod 3 = (x^2+1)^2.
```

The quadratic factors are irreducible over `F_2` and `F_3`, respectively.
Define the four Dedekind primes

```text
p_(5,5)  =(5,zeta_5-1),
p_(8,2)  =(2,zeta_8+1)=(2,zeta_8-1),
P_(12,2) =(2,zeta_12^2+zeta_12+1),
P_(12,3) =(3,zeta_12^2+1).
```

Dedekind factorization and the norm argument below therefore give

```text
5 O_5 = p_(5,5)^4,   p_(5,5)=(1-zeta_5),   (e,f,g)=(4,1,1),
2 O_8 = p_(8,2)^4,   p_(8,2)=(1-zeta_8),   (e,f,g)=(4,1,1),

2 O_12 = P_(12,2)^2,               (e,f,g)=(2,2,1),
3 O_12 = P_(12,3)^2,               (e,f,g)=(2,2,1),
```

All other rational primes are unramified in these fields because the three
displayed discriminants have no other prime support. Thus

```text
{(K,p): K is a full quartic cyclotomic field and p is totally ramified in K}
    = {(K_5,5),(K_8,2)}.
```

Here total ramification means `e=[K:Q]=4`, equivalently in these Galois
degree-four fields `(e,f,g)=(4,1,1)`. A unique prime above `p` (`g=1`) is not
enough: the two `K_12` profiles have `e=f=2` and are not total.

The principal identifications use

```text
N(1-zeta_5)=Phi_5(1)=5,
N(1-zeta_8)=Phi_8(1)=2.
```

**Q4. Residue-unit output at the total primes.**

Define residue fields at prime ideals, not the nonreduced quotients by
`p O_K`:

```text
k_(5,5)  =O_5/p_(5,5)   =F_5,     k_(5,5)^x=C_4,
k_(8,2)  =O_8/p_(8,2)   =F_2,     k_(8,2)^x=C_1.
```

For the inherited public axiom element `J=1+zeta_5^2`,

```text
J mod p_(5,5) = 2,
ord_(F_5^x)(2)=4,
k_(5,5)^x=<J mod p_(5,5)>.
```

The two ramified but non-total `K_12` controls are retained explicitly:

```text
k_(12,2)=O_12/P_(12,2)=F_2[t]/(t^2+t+1)=F_4,   k_(12,2)^x=C_3,
k_(12,3)=O_12/P_(12,3)=F_3[u]/(u^2+1)=F_9,     k_(12,3)^x=C_8.
```

They prevent the two selected outputs from being misstated as the complete
ramified-residue census. The theorem classifies total ramification and the
residues at the total primes.

## 2. Code

The accepted verifier is
`probes/P-QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS-1/verify.py`,
SHA-256 `60fd58dc3eeab0e40bf0b2ab04e05690b4a1cc088cade4ce500007ce930c1539`
(18225 bytes).
It is a self-contained Python 3 standard-library program using exact integer
and finite-field arithmetic. It has no floating point, tolerance, randomness,
argv or environment input, filesystem read or write, network access,
subprocess, dynamic code, or dependency on a prior transcript.

Its nine frozen gates are:

1. `TOTIENT`: a finite certificate derived from the prime-factor formula for
   `phi`, not an arbitrary bounded scan;
2. `FIELDS`: reconstruction of `Phi_5`, `Phi_8`, `Phi_10`, and `Phi_12` and
   the explicit `zeta_10=-zeta_5^3` field equality;
3. `DISCRIMINANT`: comparison of the cyclotomic discriminant formula with an
   independent exact resultant calculation;
4. `REDUCTIONS`: the four displayed modular identities and the two quadratic
   irreducibility checks;
5. `PROFILES`: independent exhaustive monic factorization over the relevant
   finite fields and the four `(e,f,g)` profiles;
6. `CENSUS`: discriminant support combined with the profiles to select
   exactly `(K_5,5)` and `(K_8,2)`;
7. `NORMS`: the two exact norm evaluations and unique linear total factors;
   the written proof combines them to identify the principal ideals;
8. `RESIDUES`: complete enumeration of the four residue fields and their
   multiplicative-group orders and generators;
9. `INHERITED-J`: direct audit that the inherited reduction is `2` and
   generates `F_5^x`; a mismatch is repository STOP.

After the nine gates the verifier writes the frozen non-gate scope line

```text
SCOPE L1 TOTAL RAMIFICATION IN FULL QUARTIC CYCLOTOMIC FIELDS ONLY; K12 RESIDUES ARE NON-TOTAL CONTROLS; NO TWO-PLACE-PHYSICS OR L2-L6 CLAIM
```

The verifier is an audit of the written theorem. In particular, the all-`n`
claim in Q1 and the use of Dedekind factorization rest on the proof, not on a
runtime search.

## 3. Carrier and data

The theorem carrier is the complete class of positive integers `n` with
`phi(n)=4`, the three resulting full fields (not quartic subfields of larger
cyclotomic fields), all rational primes, and the residue fields at every
ramified prime of those fields. The proof reduces the infinite integer and
prime scopes to exact finite classifications; the verifier does not impose an
empirical search cutoff.

The audit carrier is:

- every theoretically possible prime factor and exponent allowed by the
  factorization formula when `phi(n)=4`;
- the exact four cyclotomic polynomials for `n=5,8,10,12`;
- both exact discriminant routes for those polynomials;
- every monic factor needed for exhaustive degree-four factorization over
  `F_2`, `F_3`, and `F_5`;
- every element of `F_2`, `F_4`, `F_5`, and `F_9`, including every nonzero
  element for the unit-order census;
- the explicit `zeta_10` element in the power basis of `Q(zeta_5)` and the
  residue of `J` at `p_(5,5)`.

There is no external dataset, physical carrier, measured input, random seed,
machine-specific input, or hidden file.

## 4. Systematics

- The proof of Q1 starts from the prime-factor formula for `phi`; a finite
  prefix scan is neither evidence nor a completeness step.
- The equality `K_10=K_5` is imposed only after both inclusions are exhibited
  by `zeta_10=-zeta_5^3` and `zeta_5=zeta_10^2`.
- Distinctness of `K_5`, `K_8`, and `K_12` uses unequal field
  discriminants, not unequal chosen indices.
- The integral-basis theorem `O_(Q(zeta_n))=Z[zeta_n]` is stated explicitly;
  therefore the modular factorization has no hidden index obstruction.
- Repeated factors encode ramification indices only through that Dedekind
  step. The verifier separately checks factor degrees, multiplicities, and
  discriminants.
- `K_12` contributes two ramified residue fields and is never described as
  unramified. It is excluded only from the **total** ramification locus.
- Finite-field cyclicity is audited by complete enumeration on the four
  residue fields, while the written proof supplies the general theorem used
  to name the cyclic groups.
- The public mathematical result was exposed before the pin. Builder reviews
  are confirmatory and cannot satisfy the blind-breaker condition.
- A defect in `PREREG.md` or `verify.py` after the public pin invalidates this
  probe name. The frozen files remain preserved; execution stops and a fresh
  named issue, branch, and pin are required. Thresholds and scope never move.

## 5. Failure threshold

`THEOREM-CERTIFIED` is available only if the complete written proof is
accepted at its exact scope and every pinned audit gate passes. A formal
verifier leg passes only with exit 0, empty stderr, nine `PASS` lines, the
exact frozen `SCOPE` line, `RESULT 9/9 ALL PASS`, and stdout byte-identical to
the single committed `EXPECTED.txt` in both required GitHub architectures.

`NEGATIVE` fires on an exact witness to any of the following:

1. the complete solution set of `phi(n)=4` differs from `{5,8,10,12}`;
2. the quotient to three distinct fields is incomplete or identifies two of
   `K_5`, `K_8`, and `K_12` incorrectly;
3. the complete totally ramified pair set differs from
   `{(K_5,5),(K_8,2)}`, including any additional total prime in `K_5` or
   `K_8`, any total prime in `K_12`, or either displayed pair being absent;
4. either norm/ideal identity identifying `p_(5,5)` or `p_(8,2)` is false;
5. a frozen cyclotomic polynomial, field equality, discriminant,
   factorization, irreducibility result, ramification index, residue degree,
   residue field, or residue-unit group is false.

`STOP` applies to unclear authority, a collision, an incomplete proof, a
dependency used above its public scope, a mismatch in the inherited
`J mod p_(5,5)=2` premise, a broken blind-breaker firewall, a pin/hash/byte
failure, an invalid verifier, nonempty stderr, nonzero exit without an exact
scientific witness, or any attempted post-pin movement of the carrier,
equation, systematics, threshold, or layer. Failure of the inherited J premise
requires correction of existing Public Canon and is not an ordinary negative
result of this probe.

Every fired scientific falsifier is retained. No failure is hidden and no
threshold is repaired after the pin.

## 6. Action layer

L1 exact arithmetic only: cyclotomic fields, their integer rings, rational
prime decomposition, residue fields, finite unit groups, and the inherited
ramified reduction of `J`. No decoder, Born measure, physical bit, clock,
force, observable, support, stream, measure, SI quantity, or L2-L6 object is
defined or inferred.

## 7. Frozen proof

### 7.1 Complete solution of `phi(n)=4`

Write

```text
n=2^a product_i p_i^(a_i)
```

with distinct odd primes `p_i`. Then

```text
phi(n)=2^max(a-1,0) product_i p_i^(a_i-1)(p_i-1)=4.
```

For every odd `p_i`, the factor `p_i-1` divides 4, hence
`p_i in {3,5}`. Also `p_i^(a_i-1)` divides 4; because `p_i` is odd,
`a_i=1`. The primes 3 and 5 cannot both occur, since
`(3-1)(5-1)=8`.

If the odd part is 1, `phi(2^a)=4` gives `a=3` and `n=8`. If the odd
part is 3, its totient contributes 2, so `phi(2^a)=2`, giving `a=2` and
`n=12`. If the odd part is 5, its totient contributes 4, so
`phi(2^a)=1`, giving `a=0` or `a=1`, hence `n=5` or `n=10`. These cases
are exhaustive and each displayed integer has totient four. This proves Q1
without a search bound.

### 7.2 Field quotient and discriminants

For odd `m`, `Q(zeta_(2m))=Q(zeta_m)` because

```text
zeta_m=zeta_(2m)^2,
zeta_(2m)=-zeta_m^((m+1)/2).
```

At `m=5` this is the explicit Q2 identity. Thus the four indices give at
most the three displayed fields.

For a full cyclotomic field,

```text
disc(Q(zeta_n))
  = (-1)^(phi(n)/2) n^phi(n)
    / product_(p divides n) p^(phi(n)/(p-1)).
```

At `n=5,8,10,12` this gives `5^3,2^8,5^3,2^4 3^2`. Equal number fields
have equal discriminants, so `K_5`, `K_8`, and `K_12` are pairwise distinct.
This proves Q2.

### 7.3 Dedekind factorization

The standard integral-basis theorem for full cyclotomic fields gives
`O_n=Z[zeta_n]`; equivalently, the power basis has index one. Therefore
Dedekind's factorization theorem applies at the ramified primes without an
index exception: if

```text
Phi_n mod p = product_i f_i^e_i
```

with distinct monic irreducible `f_i`, then

```text
p O_n = product_i (p,f_i(zeta_n))^e_i,
```

and the residue degree is `deg(f_i)`.

Binomial expansion gives the first two reductions:

```text
(x-1)^4 = x^4+x^3+x^2+x+1 mod 5,
(x+1)^4 = x^4+1 mod 2.
```

Direct squaring gives the two `Phi_12` reductions. The polynomial
`x^2+x+1` has no root in `F_2`, and `x^2+1` has no root in `F_3`; each is
therefore irreducible. The four `(e,f,g)` profiles in Q3 follow.

### 7.4 Principal total primes

For a cyclotomic polynomial,

```text
N_(K_n/Q)(1-zeta_n)=Phi_n(1).
```

Thus the two norms are 5 and 2. The elements `1-zeta_5` and `1-zeta_8`
lie in the unique primes `p_(5,5)` and `p_(8,2)` supplied by the linear
factors `x-1` and `x+1` (the signs agree in characteristic two). Each
principal ideal has the same norm as that prime, so the ideals are equal.
Hence

```text
5 O_5=p_(5,5)^4=(1-zeta_5)^4,
2 O_8=p_(8,2)^4=(1-zeta_8)^4.
```

The degree is four, so these are total. In `K_12`, both ramified profiles
have `e=2`, `f=2`, and `g=1`; neither prime is total. The discriminant support
excludes every other rational prime from ramification, and an unramified prime
cannot be totally ramified. This completes Q3.

### 7.5 Residue-unit census and J

The factor degrees give residue fields `F_5`, `F_2`, `F_4`, and `F_9` in
the order stated in Q4. The multiplicative group of a finite field `F_q` is
cyclic of order `q-1`. More explicitly, 2 has order 4 in `F_5^x`,
`F_2^x={1}`, the class `t` has order 3 in
`F_2[t]/(t^2+t+1)`, and `1+u` has order 8 in
`F_3[u]/(u^2+1)` because

```text
(1+u)^2=-u,     (1+u)^4=-1,     (1+u)^8=1.
```

Hence the groups are `C_4`, `C_1`, `C_3`, and `C_8`, not merely groups of
those cardinalities.

Modulo `p_(5,5)=(1-zeta_5)`, one has `zeta_5=1`, so

```text
J=1+zeta_5^2=2 mod p_(5,5).
```

In `F_5^x`, `2^2=4=-1` and `2^4=1`; therefore 2 has exact order four and
generates the full residue-unit group. This proves Q4 while retaining the
two `K_12` residues as non-total controls.

## 8. Dependencies and scope firewall

Q1-Q3 and the residue-field census are self-contained classical arithmetic
and have no TWIST-J logical dependency. The final J compatibility corollary
has these inherited public supports at their registered scopes:

```text
C20-TEICHMULLER-SPLIT [T]
    O=Z[zeta_5], lambda=1-zeta_5, (5)=(lambda)^4 as ideals,
    residue F_5, Sylow C_4, and the reduced action of J.

RAMIFIED-TM-LIFT [T]
    J_lambda=[J] mod (1-zeta_5)=2 in F_5^x, only at L1.
```

The proof reconstructs the finite quartic census rather than inferring it
from these rows. Their J statements are inherited regression checks, not new
conclusions or evidence for the field census. `BORN-RESIDUAL-SPLIT [T]`
concerns `Z[i]/5` and
`Z[zeta_8]/5`, not `O_8/(1-zeta_8)`, and is not a premise.
`CARRY-J-CHECKPOINT [T]`, `Z2-PLACES-SPLIT [T]`, and
`TWO-PLACE-PHYSICS [D]` are not premises and do not move.

NO CLAIM:

- that degree four is selected;
- that full cyclotomic fields are the complete admissible class;
- that the two selected total primes are the only ramified places among all
  number fields, or even all ramified residue entries in the frozen class;
- any general conductor or prime-power classification beyond Q1-Q4;
- that either residue is a decoder, Born measure, physical bit, clock, force,
  observable, or physical place;
- that `TWO-PLACE-PHYSICS` is unique or has theorem status;
- any lift from L1 to L2-L6;
- any uniqueness statement beyond the frozen class and equality relation.

## 9. Prospective pin and formal-execution boundary

Before the first formal scientific execution:

1. statically review exactly this `PREREG.md` and `verify.py` without opening
   the claim carrier through the verifier;
2. commit and push only these two files on the named branch;
3. publish and read back the full pin commit, SHA-256 hashes, byte counts, and
   Git blobs on issue #256;
4. keep both frozen files immutable after that pin;
5. give the blind breaker only the frozen inputs listed in section 0 and
   freeze its independent `break.py` and hash before cross-comparison;
6. only then authorize a formal clean run of the pinned verifier;
7. preserve stdout, empty-stderr evidence, every fired falsifier, and the
   neutral run metadata in later `EXPECTED.txt`, `RUN.md`, and `RESULT.md`.

Compilation, AST parsing, content linting, and security review that do not
execute the verifier or inspect a scientific carrier are allowed before the
pin. No formal stdout is generated during builder preparation.
