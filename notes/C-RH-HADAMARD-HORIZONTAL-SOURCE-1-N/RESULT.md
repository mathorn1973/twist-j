# C-RH-HADAMARD-HORIZONTAL-SOURCE-1-N result

```text
STATUS:       NON-CANONICAL
ISSUE LOCK:   #373
PUBLIC BASIS: Public Canon v46
DECISION:     PARTIAL SOURCE
RH STATUS:    unchanged
```

## 1. G1. The unconditional prime-side source exists

The corrected source is Baluyot-Goldston-Suriajaya-Turnage-Butterbaugh, arXiv:2501.14545v2, together with their earlier Acta Arithmetica construction arXiv:2306.04799.

At the frozen scope they define

```text
Fcal(x,T)
 = sum_(T<gamma,gamma'<=2T) x^(rho-rho') W(rho-rho'),
W(u)=4/(4-u^2).
```

The corrected v2 paper records all three source facts needed here:

1. `Fcal(x,T)>=0` without RH.
2. It has the exact L2 zero-side representation

```text
Fcal(x,T)
 = (2/pi) integral_R
     | sum_(T<gamma<=2T)
         x^(rho-1/2)/(1-(rho-(1/2+it))^2) |^2 dt.
```

3. The unconditional Montgomery evaluation is reached through

```text
R(x,T)=integral_0^T |A1+A2+A3|^2 dt,
A2(x,t)
 = - sum_(n>=1) Lambda(n) n^(-1/2-it) min(n/x,x/n),
```

with the corrected v2 error term. Thus the load-bearing source is genuinely prime-side through the von Mangoldt coefficients and is not a zero-only restatement.

This is an external theorem source, not a TWIST-J theorem.

## 2. G2. The symmetric diagonal is exactly a Hadamard radial channel

For

```text
rho  = beta+i gamma,
rho* = 1-conjugate(rho),
delta= beta-1/2,
u    = alpha log T,
```

the v2 Tsang-kernel treatment gives the symmetric diagonal factor

```text
cosh((2 beta-1)u).
```

Let

```text
v=(exp(delta u),exp(-delta u)).
```

The normalized H2 antisymmetric component is

```text
a=(exp(delta u)-exp(-delta u))/sqrt(2),
|a|^2
 = (exp(delta u)-exp(-delta u))^2/2
 = cosh(2 delta u)-1.
```

Since `2 delta=2 beta-1`, exactly

```text
cosh((2 beta-1)u)=1+|a|^2.
```

[NON-CANONICAL candidate-T]

So the modern unconditional Montgomery/Tsang source already carries a true radial Hadamard channel. It vanishes precisely on the critical line. Hadamard is only the character decomposition; the source of the radial information is the functional symmetric diagonal in the pair-correlation form.

## 3. G3. Global Cayley-energy identity

Use every upper-half-plane zero with multiplicity and the involution

```text
rho -> rho*=1-conjugate(rho).
```

Define

```text
E_C(rho)
 = (1/2)|1/rho-1/rho*|^2,
S2
 = sum_(gamma>0) 1/|rho|^2.
```

The involution permutes the upper zero multiset. Expanding the square,

```text
sum E_C(rho)
 = S2 - Re sum_(gamma>0) 1/(rho(1-rho)).
```

But

```text
1/(rho(1-rho))=1/rho+1/(1-rho).
```

After taking real parts, the second summand is the first summand reindexed by `rho -> rho*`. Therefore

```text
Re sum_(gamma>0) 1/(rho(1-rho))
 = 2 sum_(gamma>0) Re(1/rho)
 = lambda_1.
```

Hence

```text
boxed:  sum_(gamma>0) E_C(rho) = S2-lambda_1.
```

Every off-line functional pair occurs twice in the upper-half-plane sum. If one instead counts each functional pair once, then

```text
boxed:  E_pair_total = (S2-lambda_1)/2.
```

### Convergence

`N(T)=O(T log T)` and `0<beta<1`. On a dyadic ordinate block `[Y,2Y]`,

```text
sum 1/|rho|^2 = O(log Y / Y).
```

The dyadic series converges. The same bound applies to the real parts of `1/rho`, to `1/(rho(1-rho))`, and to `E_C`. All rearrangements above are therefore absolute at the stated real/quadratic level.

Since every `E_C(rho)>=0` and

```text
E_C(rho)=0 iff Re(rho)=1/2,
```

we obtain

```text
boxed:  S2 >= lambda_1,
boxed:  S2 = lambda_1 iff RH.
```

[NON-CANONICAL candidate-T]

This is a global two-zero/conjugate-norm RH criterion. It is not a proof of RH because no prime-side evaluation of `S2` is supplied.

## 4. Why the corrected Montgomery source does not yet give exact Cayley E

For the symmetric functional pair,

```text
rho-rho* = 2 beta-1.
```

Therefore every kernel depending only on the pair difference `rho-rho*` sees `beta` but loses the absolute height `gamma`.

By contrast,

```text
E_C(rho)
 = (2 beta-1)^2
   / (2 (beta^2+gamma^2) ((1-beta)^2+gamma^2)).
```

Two hypothetical pairs with the same `beta` and different `gamma` have the same difference-kernel data but different `E_C`. Consequently:

```text
[NON-CANONICAL candidate-T]
No source whose zero-side pair kernel is a function of rho-rho* alone can
recover the exact Cayley defect E_C pointwise.
```

This is the exact boundary of the present `Fcal`/Tsang source. It supplies a radial horizontal defect, not the Cayley normalization by `|rho rho*|^2`.

## 5. The prime-error route contains the missing 1/rho weights, but isolation is not closed

The classical explicit formula for the prime-counting error has zero terms of the shape

```text
-x^rho/rho.
```

The primary short-interval literature packages the corresponding difference as

```text
c(rho,theta)=((1+theta)^rho-1)/rho.
```

Thus the missing `1/rho` weight is not foreign to the prime side. A quadratic second moment of such an explicit-formula field naturally produces `1/(rho conjugate(rho'))` weights.

However, there is a second obstruction. The 2026 Goldston-Lee-Schettler-Suriajaya horizontal-multiplicity formulation makes explicit that a same-height quadratic statistic contains every pair of zeros on the horizontal line. If more than two zeros share one ordinate, there are nonsymmetric horizontal terms in addition to the functional pair.

The current source search has not produced a prime-defined projector that selects exactly

```text
rho' = 1-conjugate(rho)
```

and simultaneously retains the `1/rho` weights, without using zero-side pair labels or an additional hypothesis.

Therefore G4/G5 stop at:

```text
horizontal radial source:       YES, exact and prime-side
1/rho source ingredient:        YES, classical explicit formula
exact Cayley pair isolation:    NOT CLOSED
```

## 6. G6. This is outside the #363 finite-profile no-go

The surviving source is a genuine two-zero quadratic object. It is not a finite list of single-variable Li moments and does not obtain its content from strict finite Toeplitz positivity. Issue #363 therefore does not kill the source itself.

It does still forbid replacing the missing global isolation by a fixed finite strict moment profile on the dense lambda grid.

## 7. Breaker verdict

The independently frozen breaker found:

```text
B1 PASS   H2 factor is cosh(2 delta u)-1
B2 PASS   E_C expansion and zero set
B3 PASS   pair-count factor: sum_upper E_C = S2-lambda_1
B4 PASS   absolute convergence from dyadic N(T)=O(T log T)
B5 PASS   unconditional Fcal has a genuine von-Mangoldt source side
B6 FIRES  same-height / difference-kernel data do not isolate exact E_C
B7 PASS   no E_C-dependent kernel inserted
B8 PASS   surviving source is quadratic two-zero data, not #363 finite profile
```

## 8. Decision

```text
G1  PASS
G2  PASS
G3  PASS
G4  PARTIAL
G5  NOT CLOSED
G6  PASS
G7  PASS with B6 boundary

DECISION: PARTIAL SOURCE
```

The source search succeeds in the important sense that the radial Hadamard channel is already present in a known unconditional prime-side pair-correlation construction. It fails the stronger preregistered bar of exact access to the Cayley-normalized energy `E_C`.

## 9. The next exact target

Do not search for another basis transform. The missing object is now sharply typed:

```text
WEIGHTED FUNCTIONAL HORIZONTAL CORRELATION

input weight:       1/rho from the explicit formula
pair involution:    rho -> 1-conjugate(rho)
quadratic channel:  (1/2)|1/rho-1/rho*|^2
aggregate:          (S2-lambda_1)/2
source requirement: prime-defined, no zero-side pair selector
```

A successful construction would give exact prime-side access to the nonnegative quantity whose vanishing is RH. It would still not prove the vanishing.

A particularly promising structural comparison is between two quadratic pairings:

```text
ordinary/conjugate norm pairing  -> S2,
functional-reflection pairing    -> lambda_1,
Hadamard difference              -> S2-lambda_1.
```

The functional-reflection side is the natural territory of the Weil explicit-formula involution. The ordinary norm side is the territory of pair correlation / second moments. Their exact junction is the next source attack.

No public status moves.
