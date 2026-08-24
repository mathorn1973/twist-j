# POST-RESULT CORRECTION C-RH-CAPACITY-CONTRACTION-1-N

```text
STATUS:        NON-CANONICAL POST-RESULT CORRECTION
AUTHORITY:     none
ISSUE:         #357
PR:            #359
ERROR FOUND AT: 08726a5c0173978cb4696372d21819468c664c7c
HISTORY READ THROUGH: 094c62c71e2ae7503b19969cadf1211eea685073
PUBLIC STATUS: no change
RH STATUS:     O (unchanged)
```

This correction preserves the preregistration and commit history while
withdrawing conclusions that depended on one wrong factorization of the pole
term. It does not alter `PREREG.md` or the frozen breaker.

## 1. Source-level error

Suzuki uses

```text
Q_W(v)=W(v*tilde(v)),
tilde(v)(x)=conj(v(-x)).
```

For

```text
M_+(v)=integral_R v(x)e^(x/2) dx,
M_-(v)=integral_R v(x)e^(-x/2) dx,
```

the two pole integrals are

```text
integral_R (v*tilde(v))(t)e^(t/2) dt
  = M_+(v) conj(M_-(v)),

integral_R (v*tilde(v))(t)e^(-t/2) dt
  = M_-(v) conj(M_+(v)).
```

Their sum is therefore

```text
2 Re[M_+(v) conj(M_-(v))],
```

not `|M_+(v)|^2+|M_-(v)|^2`. The exact signed diagonalization is

```text
2 Re[M_+ conj(M_-)]
 = (1/2)|M_++M_-|^2-(1/2)|M_+-M_-|^2.
```

The pole contribution is a rank-two indefinite form.

## 2. Corrected capacity formula

With the definitions frozen in `PREREG.md`, the direct source-side formula is

```text
q_A,a(v)
 = 2 Re[M_+(v) conj(M_-(v))]
 + integral_0^infinity K(t)||E_av-U_tE_av||^2 dt
 + (1/2) sum_(L_n<2a) w_n||E_av-U_(L_n)E_av||^2
 - kappa||v||^2,

K(t)=e^(-t/2)/(1-e^(-2t)),
kappa=log(pi)-psi_dig(1/4).
```

Thus G3 is the signed coercivity problem

```text
(1/2)|M_++M_-|^2
 + continuous jump energy
 + discrete jump energy
 >= (1/2)|M_+-M_-|^2+kappa||v||^2.
```

It is not a positive energy minus one scalar mass.

## 3. Withdrawn conclusions

The following statements at reviewed head `08726a5` are not established:

1. the pole term is a positive rank-two form;
2. every term in `q_A,a` except `-kappa||v||^2` is nonnegative;
3. G3 is a single positive-energy spectral gap;
4. `q_A,a(v)>0` for all nonzero `v` and all `a>=log 41`;
5. the unresolved G3 region has been reduced to `0<a<log 41`;
6. the displayed `R_+` and `R_-` maps in the reviewed result are correct.

The large-cutoff theorem is **not refuted** here. Its supplied proof is stopped,
and the statement returns to `UNDECIDED`.

## 4. Results that survive

The following are unaffected by the pole correction:

1. the exact finite-prime signed factorization and local inertia obstruction;
2. the archimedean jump-energy formula apart from its separate pole term;
3. the translation-chain lower bound;
4. the Chebyshev prime-power shell estimate and strict-endpoint correction;
5. the exact cutoff restriction law;
6. the local Euler/Blaschke, phase-derivative, colligation, and square-root
   identities, subject to the scope boundaries recorded in their files.

The corrected signed source maps use

```text
R_+^pole(v)=(M_+(v)+M_-(v))/sqrt(2),
R_-^pole(v)=(M_+(v)-M_-(v))/sqrt(2).
```

With these components, the exact identity

```text
Q_W^a(v)=||R_+(v)||^2-||R_-(v)||^2
```

survives. Its contractive and coherent realization remains open.

## 5. Large-cutoff salvage boundary

The prime shell computation still proves

```text
q_A,a(v)/||v||^2
 >= 2 Re[M_+conj(M_-)]/||v||^2
    +(9/20)x-3/5-(log x)/x-kappa,
x=e^a>=41.
```

The omitted pole term has lowest rank-two eigenvalue

```text
2a-2sinh(a),
```

so bounding it independently is too costly to recover the claimed ray from
this shell estimate. Any repair must prove a joint inequality coupling the
negative pole direction to the archimedean and/or prime jump energies.

## 6. Cutoff-lock variance

The public issue body froze `L_n<=2a`, while the committed `PREREG.md` uses
`L_n<2a`. The equality-delay correlation vanishes, so either convention gives
the same signed Weil prime form. It does **not** give the same auxiliary
capacity at a threshold `2a=log n`: the inclusive convention adds

```text
w_n||v||^2
```

to each delayed Hilbert leg, whereas the strict convention omits both legs.
All formulas in this result package use the committed strict convention. The
issue lock remains preserved as provenance; this variance must be frozen
explicitly before any later public claim. Positivity for the strict candidate
would imply positivity for the inclusive candidate, but the converse need not
hold at threshold cutoffs.

## 7. Process consequence

G3 is again `UNDECIDED` for the full frozen domain. Under the preregistered
breaker order, G4 and G6 remain blocked. The proposed semilocal intertwiner is
a precise follow-up comparison target, but it is not an opened G6 gate unless
G3-G5 first close or a separate lock explicitly authorizes the comparison as
an independent falsification study.

No Canon, Registry, frontier, evidence-ledger, or RH status movement follows.
