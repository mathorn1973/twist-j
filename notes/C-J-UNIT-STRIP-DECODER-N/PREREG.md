# C-J-UNIT-STRIP-DECODER-N preregistration

```text
STATUS:             NON-CANONICAL INCUBATION, RESULT-EXPOSED
SCIENTIFIC CEILING: candidate-T proof statements; candidate-C finite counts
ACTION LAYER:       L1 only
PUBLIC LOCK:        issue #1269
BASE:               b648e2dfb8ea8f1519e8e0a6e139c0bb49676ade
FORMAL PROBE:       NONE
CANON/REGISTRY:     UNCHANGED
```

This file freezes the incubation contract before the fresh public-branch rerun.
The mathematical result and an earlier local prototype were already exposed,
so no prospective or blind-discovery claim is available.

## Frozen targets

Let `K=Q(zeta_5)`, `O_K=Z[zeta_5]`, `J=1+zeta_5^2`, and for nonzero alpha

```text
c(alpha) = (log |sigma_2(alpha)| - log |sigma_1(alpha)|)/(2 log phi).
```

The targets are exactly:

1. **STRIP.** `alpha = J^n beta`, uniquely, with `n=floor(c(alpha))` and
   `0 <= c(beta) < 1`; multiplication by `J^k` changes only `n` by `k`.
2. **INTEGER TEST.** For `alpha*bar(alpha)=u+v phi`, reduced means exactly
   `v <= 0` and `u+2v > 0`; `u,v` are the displayed integral quadratic forms
   in PROOF.md and `N(alpha)=u^2+u v-v^2`.
3. **CARRY.** Two reduced representatives multiply with one carry
   `e in {0,1}` and the carry obeys the associativity cocycle. The ramified
   witness is `(1-zeta_5)^2 = -sqrt(5) J`.
4. **COUNT.** The coefficient box in PROOF.md is complete. At every norm
   `1..1000`, lattice enumeration equals ten times the independent ideal-count
   Euler recurrence. In particular `|B_940|=3110`, `|B_941|=3150`,
   `|B_1000|=3410`.
5. **SELECTED NATIVE CODE.** On the already public reachable chart, freeze
   `b:F_5^5 -> B_941` by sorting representatives by `(norm, coefficient tuple)`
   and taking the base-five label index. Then `R(n,x)=J^n b(ell_n(x))` obeys
   `R(U omega)=J R(omega)` and is invertible on the union of reachable sheets
   `n>=3`, with norm at most 941.
6. **CAPACITY.** In the frozen class of nonzero integral scalar readers that
   are U-to-J equivariant, globally injective across all reachable sheets
   `n>=3`, and uniformly norm-bounded by X, the least possible X is 941.
   This is a coding threshold, not a physical constant.

## Imported public inputs

The note may use only the exact public rows named in PROOF.md. In particular,
`U-COUNTER-REACHABLE-AMPLITUDE-CLASS [T]` already owns the general reachable
reader classification. This incubation may specialize it but may not present
that classification as new.

## Code and data

`verify.py` and `break.py` are standard-library only. No external data,
floating point, random sampling, tolerance, network input, or generated codebook
file is used. The codebook is reconstructed exactly from the finite box.

Formal incubation rerun command after the frozen source commit and public readback:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
python3 notes/C-J-UNIT-STRIP-DECODER-N/verify.py
```

The same environment is used for `break.py`.

## Falsifiers

- one nonzero alpha with no unique strip representative;
- an incorrect integer-strip equivalence or norm formula;
- carry outside `{0,1}` or a cocycle failure;
- a reduced norm<=1000 element outside the certified box;
- any normwise mismatch between the two exact count methods;
- a reachable point violating the frozen scalar-code equivariance or inverse;
- a globally injective frozen-class reader with bound <=940, or failure of the
  explicit 941 construction.

A source, custody, branch, or execution defect is STOP and is not converted into
a mathematical falsifier.

## Firewalls

No Canon status move, no registry row, no physical clock, no selection of J,
no preferred codebook, no Hodge amplitude, Born law, apparatus, event, measure,
SI scale, or L2-L6 bridge. `2 log phi`, the scalar J exponent and the `4 log phi`
coaxial rapidity spacing remain distinct.
