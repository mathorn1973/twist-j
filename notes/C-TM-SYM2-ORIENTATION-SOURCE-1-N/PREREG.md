# PREREG C-TM-SYM2-ORIENTATION-SOURCE-1-N

```text
STATUS:       NON-CANONICAL INCUBATION
ISSUE LOCK:   #375
PUBLIC BASIS: Public Canon v46
LAYER:        L5 source/orientation only
```

## Frozen source problem

The public TM-SYM2 lane already has the orientation character

```text
epsilon_read = chi_Q chi_F,
```

but the currently common selector outputs carry zero epsilon mode. Find a selector-free L5 stream in the same character without choosing any one of the 48 selectors.

## Frozen carrier

```text
W3={001,010,011,100,101,110},
N(a,b,c)=(1-a,1-b,1-c),
R(a,b,c)=(c,b,a),
q(n)=(theta_(n-1),theta_n,theta_(n+1)).
```

The quotient class order is

```text
(++),(+-),(-+),(--),
v_epsilon=(1,-1,-1,1)^T.
```

Candidate source:

```text
omega(a,b,c)=c-a,
omega_n=theta_(n+1)-theta_(n-1),
J_n=omega_n v_epsilon.
```

## Frozen gates

S1 through S8 are exactly those in issue #375 and are incorporated here without amendment.

The only admissible outcomes are SOURCE, PARTIAL, F, STOP.

## Exposure

The candidate `omega=c-a`, its expected N/R sign behavior, and the possible one-dimensional character-space argument were seen before this pin. They are exposed preparation, not evidence.

## Evidence discipline

Written exact proof is load-bearing. A finite standard-library verifier, if added later, is an audit only. No floating point and no statistical fitting are admissible.

## Firewall

No L6 measure, Born probability, physical reading, selector adoption, gauge enlargement, Canon/Registry/frontier edit, or public status movement.
