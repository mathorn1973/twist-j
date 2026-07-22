# PREREG. P-C8-BILINEAR-SHADOW-2

Public lock: issue [#124](https://github.com/mathorn1973/twist-j/issues/124),
created `2026-07-22T17:25:05Z` before this branch, path, or commit. The issue
claims exactly this probe, branch, path, owner, and L1 scope. Its collision
audit found no competing `-2` issue, branch, probe, PR, registry row, or note.
Its frozen scope was type-corrected during public pre-pin review, still before
any `-2` commit or execution; the correction is recorded in the issue history
and comment `issuecomment-5049378272`.

Base: Public Canon v15, tag `canon-v15`, activation commit
`8f4e176c5d76f519d3493e56e438aba7856e1f01`, Canon content commit
`a850753348583e611bf7ccd5aa074030dc7e12f5`, Canon SHA-256
`53237ec25b3782e833367c998c049d19459189a21c2a36638dd9e1600335976b`,
89288 bytes, branch parent `8445b59c3555f15e167d6769edb3c85b8ba6404e`.

```text
LAYER:  L1 state and readout arithmetic only. No lift to L2-L6.
TARGET: the exact C8 axes, Galois-conjugate registered digit branches, the
        branch-invariant record with its parity boundary, and its strict
        mod-8 refinement of the norm channel.
```

No scientific status is earned by this preregistration. Any Canon, registry,
dependency, frontier, or dictionary disposition is separate reviewed work.

## Protocol-repair and known-result disclosure

`P-C8-BILINEAR-SHADOW-1` is sealed and protocol-invalid, not scientifically
falsified. Its pin `c5c6db7bbba3daac1c831528acae632b1925e0bf`, records
`55eec9f7fdbcfc3120c0e0e04aaa70d2c04462e3`, verifier SHA-256
`542823134665618e8f1211aeabafafd22aa104654144bec8ac52ea72f56546d6`,
and known stdout SHA-256
`cc194c8da06d4873d6b279bbc658d2aade71be70dfa877dbdb0ab892d15c3a62`
(1100 bytes, `6/6 ALL PASS`) remain public audit history. PR #123 merged it as
`8445b59c3555f15e167d6769edb3c85b8ba6404e`.

It is not evidence for this name: it had no public issue claim before the
pin, its `RUN.md` incorrectly asserted an attached issue, PR #123 had an
empty body and no recorded review/security attestation, and its frozen axes
and gauge glosses were not type-exact. Neither frozen predecessor file is
amended.

The predecessor result is known. This `-2` probe is a transparent protocol
repair and fresh reproduction, not blind discovery. As of this pre-pin
review no `-2` verifier execution has occurred; none may occur until this
file and `verify.py` are committed, publicly pushed, and read back. The old
EXPECTED, RUN, and RESULT files are not copied. Any new difference or failure
is preserved.

## Frozen model and inherited objects

Work in the exact pair model

```text
K = F_25 = F_5[tau]/(tau^2 - 2),
(a,b) = a + b tau,
(a,b)(c,d) = (ac + 2bd, ad + bc) mod 5,
J = 2, phi = 3 = J^-1, eta = tau^3,
N(x) = x^6, Frob(x) = x^5.
```

Inherit the registered theorems `RAMIFIED-TM-LIFT`
(`Theta_n = J^s2(n)`, `theta_n = s2(n) mod 2`) and
`SQRT-PHI-DIGIT-LIFT`

```text
Y_n^+ = eta^s2(n),
Y_n^- = (-eta)^s2(n),
N(Y_n^epsilon) = Theta_n,
Y_n^- = (-1)^theta_n Y_n^+,
Y_(n+1)^epsilon = Y_n^epsilon r_epsilon^(1-nu_2(n+1)),
r_+ = eta, r_- = -eta.
```

## Frozen statement

```text
(A) AXES      <tau> = F_5^* union tau F_5^*. The even powers are the
              nonzero base-field axis F_5^*; the odd powers are
              tau F_5^*. The order-eight elements are exactly
              {+-tau,+-eta}, squaring into {J,phi}.
(B) GALOIS    Frob(a+b tau)=a-b tau. It fixes F_5 pointwise, negates
              tau F_5, and N(x)=N(-x).
(C) SWAP      Frob(Y_n^+)=Y_n^- for every n. The two registered branches
              are Galois-conjugate. No broader physical or gauge
              equivalence is claimed.
(D) RECORD    V^epsilon=(Theta_n for all n; Y_n^epsilon at indices with
              even s2(n); Y_n^epsilon Y_m^epsilon when both digit sums
              are odd) is F_5-valued, and V^+=V^-=:V. The branches differ
              exactly at indices with odd s2(n); mixed-parity products are
              off the base-field axis and branch-dependent.
(E) REFINE    The norm channel reads s2 mod 4. V reads s2 mod 8 on even
              digit-sum classes and s2(n)+s2(m) mod 8 on odd-pair classes.
              Witnesses are n=15 versus 255 and pairs (1,1) versus (1,31).
              On even classes (Y_n^epsilon)^2=Theta_n^-1.
```

The statement is restricted to this exact algebra and record. It selects no
branch and makes no L2-L6, clock, gravity, SI, force, uniqueness, or physical
gauge claim. `SQRT-PHI-TIME-GRAVITY [O]` remains open.

## Frozen all-n proof

1. The scalar squares in F_5 are `{0,1,4}`, so `x^2-2` is irreducible and
   K is a field. `Frob(tau)=tau^5=-tau`, hence Frobenius is conjugation and
   `N(a+b tau)=a^2-2b^2`.
2. `tau^(2k)=J^k` runs over `F_5^*`; `tau^(2k+1)` runs over its disjoint
   tau-multiple. These eight powers are distinct roots of `x^8-1`, so they
   exhaust its roots. Separately, `F_5^*` supplies all four roots of
   `x^4-1`; thus no order-four element lies off the base-field axis. The
   elements of exact order eight are consequently `+-tau,+-eta`.
3. Conjugation fixes the base field, negates its tau-axis, preserves norm,
   and sends `eta` to `-eta`. Raising this identity to `s2(n)` proves (B)
   and (C) for every n.
4. `(-eta)^s=(-1)^s eta^s`. For even s, both branches equal
   `phi^(s/2)` in F_5. For odd s,t, their product is
   `phi^((s+t)/2)` and both signs cancel. A mixed-parity product is a
   nonzero tau-axis element and its single branch sign does not cancel.
5. `ord(2)=ord(phi)=4`. Therefore `2^s` reads exactly s mod 4, while
   `phi^(s/2)` is injective on even classes mod 8; the same calculation
   applies to odd-pair sums. The displayed witnesses are direct evaluations,
   and `Y^2=phi^s=(2^s)^-1=Theta^-1` on even classes.
6. The successor law follows for every n from
   `s2(n+1)-s2(n)=1-nu_2(n+1)` and the two closed branch forms.

The proof, not the finite trajectory prefix, is the proposed basis for
theorem status. The verifier audits the proof's finite field and residue
claims and checks the inherited recurrence on a frozen prefix.

## The six frozen fields

```text
EQUATION     Statements (A)-(E) exactly as written above. Inherited
             RAMIFIED-TM-LIFT and SQRT-PHI-DIGIT-LIFT remain premises.

CODE         verify.py, SHA-256
             3c293b6571c1cf29702d28d531a789bddde11c695ce079f6ba7fe1a2b4c270ce
             (6541 bytes). Python standard library only; exact integer
             pairs; deterministic; binary LF stdout; no floats, network,
             filesystem reads or writes, or subprocesses; writes only the
             declared transcript to stdout.

CARRIER      all 25 elements of K; all fourth and eighth roots; the full
             <tau>; both registered branches; every exponent class mod 8;
             and 0<=n<2^16 as an audit of the proven all-n recurrence. No
             external dataset.

SYSTEMATICS  exact arithmetic throughout. The predecessor and its known
             output are disclosed above but are not evidence. Relative to
             its verifier, this verifier makes the identifier fresh,
             renders stdout host-independent, audits all fourth/eighth
             roots explicitly, and directly checks odd-pair injectivity.
             It has not been executed as of this pre-pin review. A defect found in
             PREREG.md or verify.py after the pin invalidates this named
             probe: execution stops, neither frozen file is amended, and
             a new named probe and pin are required.

THRESHOLD    KILL the theorem candidate on any incorrect field, axes,
             root census, Galois, branch, record, boundary, or refinement
             statement; any counterexample in the declared carriers; a
             proof gap or dependency conflict; or any unreconciled FAIL in
             gates 01-06. A formal leg passes only with exit 0, empty
             stderr, six PASS lines, `RESULT 6/6 ALL PASS`, and exact stdout.
             The formal local aarch64 record and required GitHub x86_64
             check must use the pinned verifier hash and byte-identical
             stdout. Independent proof, not architecture count, is the
             proposed basis for T.

LAYER        L1 only. No state-to-manifold, boundary, support, stream,
             measure, clock, gravity, SI, force, or physical-gauge lift.
```

## Dependencies and scope firewall

Frozen premises:

```text
PENTIT-ROOT-FACTS [T]       exact F_25 pair model and tau/eta identities
RAMIFIED-TM-LIFT [T]        Theta_n and theta_n digit recursion
SQRT-PHI-DIGIT-LIFT [T]     both Y branches, projections, successor law
```

`QUBIT-FROM-F5 [T]` is only a consistency comparison for the registered sign
quotient, not a premise. No curvature, selector, Born, clock, metrology, or
gravity row is used.

Before the first formal execution, this file and `verify.py` must be
committed and publicly pushed together. Their public hashes and bytes must be
read back and recorded on issue #124. They are immutable after that pin.
