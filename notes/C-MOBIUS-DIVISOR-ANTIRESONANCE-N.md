# C-MOBIUS-DIVISOR-ANTIRESONANCE-N

**Title:** Möbius divisor antiresonance: prime-power first response and the zeta-ratio bridge  
**Author:** A. M. Thorn  
**Date:** 27 September 2026  
**Status:** NON-CANONICAL RESEARCH NOTE. No public scientific status is created by this file.  
**Object lock:** issue #1193  
**Public baseline:** Public Canon v92  
**Scope:** arithmetic and analytic number theory only. No L1 to L6 physical lift.

## 0. Purpose

This note makes one narrow use of the word **antiresonance** precise.

For each positive integer (n), define the Möbius divisor response

[
A_n(w)
:=
sum_{dmid n}mu(d)d^{-w}.
]

Because only squarefree divisors survive, the response factorizes as

[
oxed{
A_n(w)=prod_{pmid n}left(1-p^{-w}ight).
}
	ag{1}
]

For (n>1), every factor vanishes at (w=0). The response therefore has an exact zero there. The order of this zero is not arbitrary: it is exactly the number of distinct prime divisors of (n).

This gives a sharp arithmetic statement:

> **Prime powers are the unique simple-zero class of the Möbius divisor antiresonance.**

Equivalently, all (n>1) cancel at zero response, but prime powers are the only integers whose cancellation is broken already by the first derivative.

The note then connects the local filter to the global zeta function through the exact two-variable identity

[
oxed{
sum_{nge1}rac{A_n(w)}{n^s}
=
rac{zeta(s)}{zeta(s+w)}.
}
	ag{2}
]

Differentiating at (w=0) recovers the von Mangoldt series

[
oxed{
sum_{nge1}rac{Lambda(n)}{n^s}
=
-rac{zeta'(s)}{zeta(s)}.
}
	ag{3}
]

These identities are standard arithmetic consequences of Möbius inversion and Euler products, reorganized here as one exact cancellation picture. No novelty or priority is claimed for the underlying number-theoretic identities.

Local labels in this note are descriptive only:

```text
[T, elementary]   proved directly in this note
[KNOWN]           standard established mathematics
[H]               proposed follow-up question
[F]               explicitly excluded interpretation
```

None changes `canon/REGISTRY.tsv`.

---

## 1. The finite interference form

Let

[
operatorname{rad}(n)=prod_{pmid n}p,
qquad
omega(n)=|{p:pmid n}|.
]

Only squarefree divisors contribute to (A_n), so

[
A_n(w)=A_{operatorname{rad}(n)}(w).
	ag{4}
]

If the distinct prime divisors are (p_1,ldots,p_r), then every squarefree divisor corresponds to a subset
(Ssubseteq{1,ldots,r}). Hence

[
oxed{
A_n(w)
=
sum_{Ssubseteq{1,ldots,r}}
(-1)^{|S|}
exp!left(
-wsum_{jin S}log p_j
ight).
}
	ag{5}
]

On the imaginary axis (w=it),

[
A_n(it)
=
sum_S
(-1)^{|S|}
e^{-itlog d_S},
qquad
d_S:=prod_{jin S}p_j.
	ag{6}
]

Thus (A_n(it)) is literally a finite signed sum of unit-modulus phases.

At (t=0), every phase equals one and

[
A_n(0)
=
sum_S(-1)^{|S|}
=
(1-1)^r.
	ag{7}
]

Therefore

[
oxed{
A_n(0)=0
qquad
(n>1).
}
	ag{8}
]

**[T, elementary.]** The zero is exact finite inclusion-exclusion. No limiting argument and no analytic continuation are involved.

This is the entire sense in which the word **antiresonance** is used here: nonzero channels are present in the finite sum, while the signed response vanishes exactly.

No physical energy is defined by (5) or (6).

---

## 2. Order of the antiresonance

For one prime (p),

[
1-p^{-w}
=
1-e^{-wlog p}
=
wlog p+O(w^2).
	ag{9}
]

Let (r=omega(n)). Multiplying the (r) factors in (1),

[
A_n(w)
=
w^rprod_{pmid n}log p
+
O(w^{r+1}).
	ag{10}
]

Therefore:

### Theorem 2.1

**[T, elementary.]** For every (n>1),

[
oxed{
operatorname{ord}_{w=0}A_n(w)=omega(n).
}
	ag{11}
]

Equivalently,

[
A_n^{(k)}(0)=0
qquad
(0le k<omega(n)),
	ag{12}
]

and the first nonzero derivative is

[
oxed{
A_n^{(omega(n))}(0)
=
omega(n)!
prod_{pmid n}log p.
}
	ag{13}
]

So the number of distinct prime divisors is exactly the order of the local cancellation.

This gives a clean stratification:

[
egin{array}{c|c}
omega(n) & 	ext{response at }w=0\
hline
1 & 	ext{simple zero}\
2 & 	ext{double zero}\
3 & 	ext{triple zero}\
dots & dots
end{array}
]

Prime powers are precisely the integers with (omega(n)=1).

---

## 3. The first response is the von Mangoldt function

Differentiate the divisor sum directly:

[
A_n'(0)
=
-sum_{dmid n}mu(d)log d.
	ag{14}
]

The standard Möbius identity for the von Mangoldt function is

[
Lambda(n)
=
-sum_{dmid n}mu(d)log d,
	ag{15}
]

with (Lambda(1)=0). Hence:

### Theorem 3.1

**[T, elementary.]**

[
oxed{
A_n'(0)=Lambda(n).
}
	ag{16}
]

Therefore

[
A_n'(0)
=
egin{cases}
log p,&n=p^k, kge1,\
0,&	ext{otherwise}.
end{cases}
	ag{17}
]

This is the exact first-response statement.

Every (n>1) is at antiresonance at (w=0), but the response leaves zero to first order if and only if (n) is a prime power.

The distinction is important:

[
oxed{
	ext{prime powers are not exceptions to cancellation;}
quad
	ext{they are the lowest-order cancellation class.}
}
	ag{18}
]

---

## 4. Positive response intensity

Define the nonnegative scalar

[
I_n(t):=|A_n(it)|^2.
	ag{19}
]

By (1),

[
|1-e^{-itlog p}|^2
=
4sin^2!left(rac{tlog p}{2}ight),
]

so

[
oxed{
I_n(t)
=
prod_{pmid n}
4sin^2!left(rac{tlog p}{2}ight).
}
	ag{20}
]

Since

[
4sin^2(x/2)=x^2+O(x^4),
]

we obtain

[
oxed{
I_n(t)
=
t^{2omega(n)}
prod_{pmid n}(log p)^2
+
O!left(t^{2omega(n)+2}ight).
}
	ag{21}
]

Thus

[
oxed{
lim_{t	o0}
rac{I_n(t)}{t^{2omega(n)}}
=
prod_{pmid n}(log p)^2
qquad
(n>1).
}
	ag{22}
]

In particular:

### Corollary 4.1

**[T, elementary.]** For every (n>1),

[
oxed{
lim_{t	o0}rac{|A_n(it)|^2}{t^2}
=
Lambda(n)^2.
}
	ag{23}
]

For a prime power the limit is ((log p)^2). For an integer with at least two distinct prime divisors the limit is zero.

This is a positive version of the same first-response selector. It is still an arithmetic scalar, not a physical energy.

---

## 5. Examples

### (n=8)

Only the prime (2) occurs:

[
A_8(w)=1-2^{-w}.
]

Hence

[
A_8(0)=0,
qquad
A_8'(0)=log2,
]

and

[
I_8(t)=4sin^2!left(rac{tlog2}{2}ight)
=t^2log^22+O(t^4).
]

### (n=12)

The distinct primes are (2) and (3):

[
A_{12}(w)
=
(1-2^{-w})(1-3^{-w})
=
1-2^{-w}-3^{-w}+6^{-w}.
]

Thus

[
A_{12}(0)=0
]

and

[
A_{12}'(0)
=
log2+log3-log6
=
0.
]

The first nonzero term is quadratic:

[
A_{12}(w)
=
w^2log2log3+O(w^3).
]

### (n=30)

The distinct primes are (2,3,5), so

[
A_{30}(w)
=
(1-2^{-w})(1-3^{-w})(1-5^{-w})
]

has a zero of order three:

[
A_{30}(w)
=
w^3log2log3log5+O(w^4).
]

The hierarchy is exact.

---

## 6. The global zeta-ratio bridge

Define

[
mathcal F(s,w)
:=
sum_{nge1}rac{A_n(w)}{n^s}.
	ag{24}
]

Take

[
Re s>1,
qquad
Re(s+w)>1.
	ag{25}
]

The function (A_n(w)) is multiplicative in (n), and for every (kge1),

[
A_{p^k}(w)=1-p^{-w}.
	ag{26}
]

Therefore the local Euler factor is

[
egin{aligned}
sum_{kge0}A_{p^k}(w)p^{-ks}
&=
1+(1-p^{-w})sum_{kge1}p^{-ks}\
&=
1+(1-p^{-w})rac{p^{-s}}{1-p^{-s}}\
&=
rac{1-p^{-(s+w)}}{1-p^{-s}}.
end{aligned}
	ag{27}
]

Multiplying over primes gives:

### Theorem 6.1

**[T, elementary Euler product.]** In the absolute-convergence domain (25),

[
oxed{
mathcal F(s,w)
=
sum_{nge1}rac{A_n(w)}{n^s}
=
rac{zeta(s)}{zeta(s+w)}.
}
	ag{28}
]

At (w=0),

[
mathcal F(s,0)=1.
	ag{29}
]

This is the global form of the local cancellation: all (n>1) disappear at (w=0), leaving only (n=1).

Differentiation at (w=0) is valid locally in the absolute-convergence domain and gives

[
sum_{nge1}rac{A_n'(0)}{n^s}
=
-rac{zeta'(s)}{zeta(s)}.
	ag{30}
]

Using Theorem 3.1:

### Corollary 6.2

**[KNOWN, recovered directly here.]**

[
oxed{
sum_{nge1}rac{Lambda(n)}{n^s}
=
-rac{zeta'(s)}{zeta(s)},
qquad
Re s>1.
}
	ag{31}
]

So the prime-power source in the logarithmic derivative of (zeta) is exactly the first variation of a divisor filter whose zeroth-order response cancels every (n>1).

That is the strongest exact statement in this note.

---

## 7. What the word antiresonance does and does not buy

The terminology is useful only if its scope is kept narrow.

For fixed (n), equation (6) is a finite signed phase sum. At (t=0), every individual phase has modulus one while the signed total is zero. That is structurally analogous to destructive interference.

But the mathematics established here is only

[
	ext{finite phase sum}
longrightarrow
	ext{exact zero}
longrightarrow
	ext{order of zero}
longrightarrow
Lambda(n)
longrightarrow
-zeta'/zeta.
]

It does **not** establish

[
	ext{arithmetic cancellation}
longrightarrow
	ext{physical vacuum or plenum energy cancellation}.
]

Those are different statements.

A physical antiresonance requires a specified physical amplitude, dynamics, observable and coupling. None is supplied here.

---

## 8. Hard boundaries

### 8.1 The Möbius function is already in the construction

The filter begins with

[
A_n(w)=sum_{dmid n}mu(d)d^{-w}.
]

Therefore the squarefree prime-divisor structure is already encoded in the coefficients.

**[F]** This note does not derive the existence of primes from a prime-free substrate.

It reorganizes known arithmetic information into a useful exact response hierarchy.

### 8.2 Prime powers, not primes alone

Because

[
A_n(w)=A_{operatorname{rad}(n)}(w),
]

the filter does not see prime exponents.

Thus

[
A_p(w)=A_{p^2}(w)=A_{p^3}(w)=cdots.
]

**[F]** The first-response theorem is not a primality test. It is a prime-power selector.

### 8.3 The parameter is not physical time

The variables (w) and (t) are analytic parameters introduced by definition.

**[F]** No identification with physical time, energy, frequency, action or a TWIST-J clock is made.

### 8.4 No physical vacuum claim

TWIST-J uses **plenum**, not vacuum, for its structured substrate.

This note constructs no Hamiltonian, no quantum field theory, no stress-energy tensor and no gravitational coupling.

**[F]** It does not address the cosmological constant problem.

### 8.5 No Connes or Hilbert-Pólya realization

The zeta-ratio identity is an Euler-product identity in the absolute-convergence half-plane.

**[F]** No spectral operator with Riemann zeros as eigenvalues or missing states is constructed.

### 8.6 No RH implication

Equation (28) may of course be meromorphically continued through the known continuation of (zeta), but no continuation argument is used here to infer zero locations.

**[F]** No RH result, Mertens estimate, zero-free region or zero-multiplicity theorem follows from this note.

---

## 9. Relation to adjacent TWIST-J work

This object is intentionally separate from two existing non-canonical branches.

### Digit antiresonance

Issue #965 / PR #966, `C-TM-MOBIUS-DIGIT-ANTIRESONANCE-N`, studies:

- Thue-Morse character uniqueness;
- exact digital cancellation;
- digit leakage;
- filtration alignment;
- a possible Möbius-Walsh transfer.

The present note uses no Thue-Morse input. Its cancellation is divisor inclusion-exclusion on the Boolean lattice of distinct prime factors.

### RH Möbius mean channel

Issue #978, branch `notes/c-rh-mobius-mean-channel-n`, studies a specific RH approximation and common-sign Möbius mean-channel obstruction.

The present note supplies no estimate for that channel and does not alter its open endpoint.

The public rows `TRIVIAL-RAPIDITY-EVALUATION-BRIDGE [O]` and
`LAMBDA-COCYCLE-ANGLES [H]` remain unchanged.

---

## 10. Falsifier-first checklist

The written theorem package fails if any one of the following exact statements is false:

1. for some (n), the divisor sum does not equal the prime product (1);
2. for some (n>1), the zero order is not (omega(n));
3. for some (n), (A_n'(0)
eLambda(n));
4. the positive identity (20) fails;
5. the limit (23) fails for some (n>1);
6. one Euler factor in (27) is incorrect;
7. the global identity (28) fails in its declared absolute-convergence domain;
8. the note is interpreted as deriving primes independently of (mu), distinguishing primes from prime powers, proving RH, or supplying a physical vacuum/plenum mechanism.

Items 1 through 7 are mathematical falsifiers. Item 8 is a scope falsifier.

No numerical verifier is needed for these finite algebraic derivations. Any future computational promotion is a separate public object.

---

## 11. The next honest questions

The present note suggests several follow-ups, none of which is claimed here.

### H1. Prime-free reconstruction

Can one construct an independent arithmetic operator, not defined with (mu), whose first variation is forced to equal (Lambda)?

That would be materially stronger than the current filter because the prime support would no longer be inserted through Möbius coefficients.

### H2. Higher-response hierarchy

The complete derivative hierarchy

[
A_n^{(k)}(0)
]

contains more information than the first derivative. The first nonzero level is exactly (omega(n)). A natural question is whether the higher derivatives admit a useful global organization with a transparent arithmetic meaning beyond formal derivatives of

[
rac{zeta(s)}{zeta(s+w)}.
]

### H3. Joined response versus summatory cancellation

The local zero is exact for every (n>1). It does not imply cancellation of

[
sum_{nle x}mu(n)
]

or any RH-strength summatory estimate.

Any useful bridge from the local divisor response to a summatory theorem must preserve the relevant joined arithmetic structure rather than replace it by the slogan "destructive interference".

---

## 12. Compact statement

The result can be compressed to four lines.

For

[
A_n(w)=sum_{dmid n}mu(d)d^{-w},
]

one has

[
oxed{
A_n(w)=prod_{pmid n}(1-p^{-w}),
qquad
operatorname{ord}_{0}A_n=omega(n),
}
]

[
oxed{
A_n'(0)=Lambda(n),
qquad
lim_{t	o0}rac{|A_n(it)|^2}{t^2}=Lambda(n)^2
quad(n>1),
}
]

and

[
oxed{
sum_{nge1}rac{A_n(w)}{n^s}
=
rac{zeta(s)}{zeta(s+w)}
quad
(Re s>1, Re(s+w)>1).
}
]

So the exact arithmetic content of the antiresonance picture is:

> **All nontrivial divisor patterns cancel at zeroth order. Prime powers are precisely the patterns whose cancellation has only first order, and their surviving first response is the von Mangoldt weight.**

Nothing physical is added by that sentence. The mathematics is already enough.

---

**Repository boundary:** NON-CANONICAL note only. Public Canon v92, Registry, Frontier, gates, evidence and releases are unchanged.
