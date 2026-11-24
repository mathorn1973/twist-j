# Intake of the parallel unit-arity note

**NON-CANONICAL. No authority. Paper review: candidate-D, L1.**

## Source and exposure

At the user's request, today's related conversations were searched. The initial
conversation summaries reported `C-J-UNIT-RELATION-DEPTH-1` and
`C-J-UNIT-ARITY-BOUND-1`. The full native file
`PROMO-C-J-UNIT-ARITY-BOUND-1.md` was then located and read, including all eight
sections. Its source metadata gives 10512 bytes and creation on 2026-11-24.
The companion archive was located but its programs were not run or audited here.
No unseen conversation or missing certificate is assumed to have been reviewed.

This is a user-supplied parallel reference, not public Canon authority. Its own
header classifies paper deductions as candidate-D and finite checks as candidate-C,
and disclaims independent blind confirmation or a two-architecture scientific gate.
Its exact enumerations remain at that source status and are not promoted by this
intake. The following projection argument is checked directly on paper.

## Integral phase projection

Let $A=\mathbb Z[\phi]$ and $t=\phi-1=\phi^{-1}$. The identity
$j+j^{-1}=t$ gives

| Phase | Coordinate in $A$ | Coordinate multiplying $j$ |
| --- | --- | --- |
| $1$ | $1$ | $0$ |
| $j$ | $0$ | $1$ |
| $j^2$ | $-1$ | $t$ |
| $j^3$ | $-t$ | $-t$ |
| $j^4$ | $t$ | $-1$ |

For example, $j^2=tj-1$ and $t^2=1-t$ give the remaining rows.
They span $\mathcal O$ over $A$. Independence over $\mathbb Q(\phi)$
follows because $j$ is not real. Thus

$$
\mathcal O=A\oplus jA
$$

as an integral module, and this decomposition remains exact modulo every
rational integer. Each coordinate of a signed unit $\pm j^a\phi^e$ is
zero or a signed real unit. Projecting a sum of at most $k$ quartic units
therefore gives two real-unit sums of at most $k$ terms each.

If the original sum vanishes modulo $p\mathcal O$ but not modulo
$q\mathcal O$, both coordinates vanish modulo $pA$ and at least one
does not vanish modulo $qA$. That coordinate is a real separator of
no larger weight. The reverse inequality follows by including real units
in $\mathcal O$. Consequently

$$
d_{\mathcal O}(p,q)=d_A(p,q)
$$

for the minimum number of signed unit summands in this precise reader.
This argument belongs to the parallel note. We use it as a checked paper
reduction and do not claim it as a new result of #2086. Norm observations,
chosen prime ideals, arbitrary coefficient polynomials and physical measurements
are outside its stated scope.

## Reported finite obstructions

The source defines $d(p,q)$ by whole-ideal vanishing with repeated terms allowed.
It reports the following complete finite checks:

| First Fibonacci rank | Prime pair | Reported minimum weight |
| --- | --- | ---: |
| 64 | $1087,4481$ | 6 |
| 73 | $9375829,86020717$ | 8 |

For rank 64 it gives the relation

$$
\phi^3+\phi^{25}+\phi^{29}=1+\phi^{11}+\phi^{121}
$$

modulo the first prime and not the second. For rank 73 it gives

$$
\phi^{10}+\phi^{16}+\phi^{51}+\phi^{95}
=1+\phi^{61}+\phi^{105}+\phi^{286}.
$$

The lower bounds require exhaustive equality tables. This lane does not
independently re-establish those tables, the large integer coefficient
certificates, their primality checks, or their checksums. They are reported
finite evidence, not premises of any theorem in this package. The positive
relations and metadata are retained here solely as source descriptions.

The rank-73 source reports $\operatorname{ord}(\phi)=292$, hence
$h=146$ and $b=74$ for our trace criterion. Since $74^3<2\cdot9375829$,
neither member satisfies the sufficient prime-level 769-unit condition.
The example thus lies in the remaining sparse-order regime; it is not
an instance to which the trace theorem promises a separator. There is no
conflict with the six-unit theorem for the special order-$5^{k+1}$ blocks.

## Relation between the upper bounds

The parallel paper proves, for primes of common Fibonacci rank $r$,

$$
d(p,q)\le2\left\lfloor\frac{\lceil r/2\rceil}{2}\right\rfloor
$$

by a nonconsecutive greedy Fibonacci expansion of the smaller prime.
The present nearest signed Lucas construction instead gives the bound

$$
d(p,q)\le\left\lfloor\frac{2\lceil r/2\rceil+4}{3}\right\rfloor,
$$

where the stated small-domain conditions in `BASELINE_AND_HEIGHT.md` apply.
Either bound may be retained by taking their minimum. This improves the
asymptotic coefficient from one half to one third by an elementary signed
digit argument. It is not a constant bound and does not improve the cost of
trial division. The earlier result retains its separate authorship and scope.

The source also explains the algorithmic implication of a hypothetical
universal constant weight: finite common unit labels allow complete bounded-weight
enumeration in a polynomial of the return index. This is why a universal
constant would be substantially stronger than finite separation for each pair.
Our two trace criteria and the six-unit block theorem give stated subfamilies;
they leave that universal question unresolved.
