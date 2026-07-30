# PREREG. P-SQRT-PHI-DIGIT-1

Public lock: issue #87. Base: Public Canon v11, activation commit
`3d8c6307f20d01ad50fc90ae1c5777926b884881`, Canon content commit
`3dc0d4255ae47f0512e5dd656d92ceb308ab026a`.

```text
LAYER:  L1 state and readout arithmetic. No lift to L2-L6 is claimed.
TARGET: audit the proof-first SQRT-PHI-DIGIT-LIFT theorem candidate while
        leaving SQRT-PHI-TIME-GRAVITY [O] open.
```

No scientific status is earned by this preregistration. Any eventual Canon,
registry, dependency, or frontier disposition is separate reviewed work.

## Frozen field, quotient, and inherited lift

Work in the exact pair model

```text
K = F_25 = F_5[tau]/(tau^2 - 2),
(a,b) = a + b tau,
(a,b)(c,d) = (ac + 2bd, ad + bc) mod 5.
```

Freeze

```text
J = 2,  phi = 3 = J^-1,  eta = tau^3,
N(x) = x^6 : K^* -> F_5^*.
```

Let

```text
q : F_5^* -> F_5^*/{+-1} ~= F_2,
q(+-1) = 0,  q(+-2) = 1.
```

For `n in N_0`, let `s2(n)` be the finite binary digit sum,
`theta_n = s2(n) mod 2`, and inherit the registered theorem

```text
Theta_n = J^s2(n) in F_5^*.                              (A)
```

Here `J` is the ramified image `J_lambda=2`, not the integral cyclotomic
element before reduction.

## Frozen statement

The field element `eta` obeys

```text
eta^2 = phi,  eta^4 = -1,  ord(eta) = 8,  N(eta) = J.    (B)
```

The equation `r^2=phi` has exactly the two roots

```text
r_+ = eta,  r_- = -eta.                                  (C)
```

Both roots have order eight and norm `J`. Restricted to `<eta>`, the norm
gives the exact sequence

```text
1 -> {+-1} -> <eta> ~= C8 --N--> <J> ~= C4 -> 1,         (D)
```

and this sequence is nonsplit. The claim concerns only the restricted
`C8 -> C4` norm, not the full norm map `K^* -> F_5^*`.

For each `epsilon in {+1,-1}`, put `r_epsilon=epsilon eta` and freeze the
digit recursion

```text
Y_0^epsilon      = 1,
Y_(2n)^epsilon   = Y_n^epsilon,
Y_(2n+1)^epsilon = r_epsilon Y_n^epsilon.                 (E)
```

The unique solution for every `n in N_0` is

```text
Y_n^epsilon = r_epsilon^s2(n).                            (F)
```

For both branches and every `n in N_0`, the projection identities are

```text
N(Y_n^epsilon)  = Theta_n,
q(N(Y_n^epsilon)) = theta_n,
(Y_n^epsilon)^2 = Theta_n^-1,
(Y_n^epsilon)^4 = (-1)^theta_n,
Y_n^-            = (-1)^theta_n Y_n^+.                   (G)
```

Thus the exact algebraic tower is

```text
C8  --norm-->  C4  --sign quotient-->  C2
Y_n            Theta_n                 theta_n.
```

For `c_n=nu_2(n+1)`, the chronological successor law is

```text
Y_(n+1)^epsilon = Y_n^epsilon r_epsilon^(1-c_n).          (H)
```

The exponent in (H) is an integer group exponent in `K^*`; negative values
use the inverse. Because `r_epsilon` has order eight, the verifier may reduce
that exponent modulo eight. The successor multiplier is not constant:

```text
n=0 gives multiplier r_epsilon,
n=1 gives multiplier 1.                                  (I)
```

Therefore the digit-one multiplier `+-sqrt(phi)` is not the declared
chronological tick multiplier.

## Frozen all-n proof

1. The scalar squares in `F_5` are `{0,1,4}`, so `X^2-2` is irreducible.
   Hence the displayed pair model is a field of 25 elements. Its Frobenius
   sends `tau` to `tau^5=-tau`, so `N(a+b tau)=a^2-2b^2`.
2. Direct exact powers give `eta=tau^3=2 tau`, `eta^2=3=phi`,
   `eta^4=-1`, and `eta^8=1` with `eta^4!=1`; hence `eta` has order eight.
   Also `N(eta)=eta^6=(-1)phi=2=J`, proving (B).
3. Solving `(a+b tau)^2=3` forces `2ab=0`. The case `b=0` would require a
   scalar square equal to three, which is impossible. Thus `a=0` and
   `2b^2=3`, so `b=+-2`. These are exactly `+-eta`, proving (C).
4. On `<eta>`, multiplicativity gives `N(eta^k)=J^k`. The image is `<J>`,
   the kernel is `{1,-1}`, and the two preimages of the generator `J` are
   `eta` and `-eta`, both of order eight. A section from `C4` would have to
   send its generator to an element whose order divides four, so none exists.
   This proves exactness and nonsplitting in (D).
5. Each application of (E) removes the final binary digit. Induction on
   binary length therefore gives the unique formula (F) for every
   nonnegative integer.
6. Multiplicativity of `N`, `N(r_epsilon)=J`, `r_epsilon^2=phi=J^-1`,
   `r_epsilon^4=-1`, and `(-eta)^k=(-1)^k eta^k` prove all identities in
   (G), using the inherited formulas in (A).
7. Incrementing `n` clears exactly `c_n` trailing one-bits and creates one
   new one. Thus `s2(n+1)-s2(n)=1-c_n`, which proves (H) from (F). The two
   exact cases in (I) disprove a constant chronological multiplier.

The proof, not the finite audit prefix, is the proposed basis for theorem
status at the frozen L1 scope.

## The six frozen fields

```text
EQUATION     Statements (A)-(I) exactly as written above. The novel content
             is the two-branch C8 digit lift, its restricted nonsplit norm
             sequence, the exact C8 -> C4 -> C2 projection tower, and the
             nonconstant chronological carry law. Inherited RAMIFIED-TM-LIFT
             remains a premise, not a newly earned result.

CODE         verify.py, SHA-256
             ad94fdff5cf0b7c8674d36b675f058f347287702c90428c19aa6b76e8e4a1cab
             (7004 bytes). Python standard library only; exact integer pairs;
             deterministic; no floats, files, network, or subprocesses. Run
             from the repository root with LC_ALL=C LANG=C
             PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

CARRIER      theorem: all 25 elements of K for the field and root facts, the
             restricted subgroup <eta>, both roots r_epsilon, and every
             n in N_0. Audit: all 25 field elements, every nonzero pair
             product and inverse, every root candidate, all 64 products in
             the restricted C8, both digit branches for 0<=n<=2^18, and the
             chronological law for 0<=n<2^18 including carry lengths 0..18.
             There is no external dataset.

SYSTEMATICS  exact proof has no numerical approximation. Audit limitations
             are its frozen finite prefix and implementation correctness;
             they do not enlarge or establish the all-n scope. Issue #87 and
             any prior informal calculation are source material only, not
             formal evidence. A defect found in PREREG.md or verify.py after
             the pin invalidates this named probe: execution stops, neither
             frozen file is amended, and a new named probe and pin are
             required. Only result-record corrections may be later commits.

THRESHOLD    KILL the theorem candidate on any incorrect field, root, norm,
             order, kernel, image, or nonsplitting statement; any third or
             missing root of X^2-phi; any counterexample to (E)-(H); a
             constant chronological multiplier; a proof gap or dependency
             conflict; or any unreconciled FAIL in gates 01-06. A formal leg
             passes only with exit 0, empty stderr, all six PASS lines, the
             RESULT 6/6 ALL PASS line, and byte-identical stdout on the
             recorded aarch64 and GitHub x86_64 runs.

LAYER        L1 only. No state-to-manifold, boundary, support, stream,
             measure, clock dictionary, or force lift is asserted.
```

## Dependencies and scope firewall

Frozen theorem premises:

```text
DEF-ARCHITECTURE         the declared public type boundary
DEF-ODOMETER-ORBIT       the forward N_0 carrier and finite digit sum
PENTIT-ROOT-FACTS [T]    J=2, phi=3, and the exact tau root block in F_25
QUBIT-FROM-F5 [T]        the C4 -> C2 sign quotient
RAMIFIED-TM-LIFT [T]     Theta_n=J^s2(n) and q(Theta_n)=theta_n
```

`SILVER-RING-FACTS [C]`, `PENTIT-ROOT-READING [D]`,
`TIME-QUANTUM-TOWER [C]`, and `METRO-TICK [T]` are not premises.

This probe does not assert that `n -> n+1` is multiplication by
`sqrt(phi)`, that digit insertion is a physical tick, or that either sign
branch is uniquely or physically selected. It does not identify `Y_n` with
a checkpoint, decoder output, or full `U` state. It adds no physical time,
time arrow, gravity dynamics, coupling, SI scale, force, parity on all of
`Z_2`, or lift to L2-L6.

The live `SQRT-PHI-TIME-GRAVITY [O]` obligation remains open. A later fold
may make it depend on `SQRT-PHI-DIGIT-LIFT`, but it still requires a typed
bridge into the declared chronological clock and gravity channel.

Before the first formal execution, this file and `verify.py` must be committed
and pushed together. After that public pin they are immutable for this probe.
