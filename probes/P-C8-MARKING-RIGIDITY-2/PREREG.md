# P-C8-MARKING-RIGIDITY-2 preregistration

Status: **PREREGISTERED / UNRUN / NON-CANONICAL**

Issue lock: #731

## Authority pin

At preregistration review:

- authority: Public Canon v72, `mathorn1973/twist-j main`
- public main base: `43cfd9e4ca570a51f9aa548a8b0e61dad45f5b7f`
- Canon content commit: `aac8a3a4aff027beb2b08edbde1ae8e59224914c`
- Canon SHA-256: `39ca6e5c49d3ec2b78464045312af75618c4601f87dfa178dfd689d8a4942c70`
- predecessor: `P-C8-MARKING-RIGIDITY-1`, issue #729, merged PR #730, pin `3ccb245b565b77fdd05636c1b91dcd6e99629457`

The predecessor completed a formal run but its frozen evidence package has two post-merge integrity defects: its bounded primality audit used `int(n ** 0.5)` despite a no-floating-point method declaration, and its `RUN.md` recorded a machine nickname. The predecessor bytes and history remain immutable. They are provenance only for this successor and are not evidence for it.

This probe is a result-exposed protocol repair. It re-audits the same six scientific statements with a newly authored exact verifier. It does not strengthen the predecessor scope.

## Frozen question

Given the marked datum, is the C8 level forced once the marking is supplied, and can the remaining target orientation be separated by a Hermitian observable with rational matrix entries?

## Frozen scope

Six gates. Universal mathematical statements are carried by the written arguments below. Finite computation is an audit.

### G1, marked datum

In

```text
F_25 = F_5[tau]/(tau^2 - 2),
```

verify exactly

```text
tau^2 = 2,
tau^4 = -1,
ord(tau) = 8,
ord_5(2) = 4,
F_5 nonsquares = {2,3}.
```

### G2, rigidity of the residue prime

Let `p` be an odd prime and suppose `tau in F_(p^2)` satisfies `tau^2=2` and `ord(tau)=8`. Then `ord(tau^2)=4`, hence `ord_p(2)=4`. Therefore

```text
p | 2^4 - 1 = 15,
p does not divide 2^2 - 1 = 3.
```

The only prime divisor of 15 surviving the second condition is `p=5`. Characteristic two is excluded because every finite multiplicative group in characteristic two has odd order.

The verifier also scans primes below 20000 as a bounded audit of this proof. The scan is not the source of the universal conclusion.

### G3, converse over F_5

For each `m in F_5^*`, enumerate both square roots of `m` in `F_25`. Each nonsquare marking `m in {2,3}` must have roots of exact order 8. No square marking `m in {1,4}` may have a root of order 8.

### G4, source orientation

Verify exactly

```text
2^-1 = 3 mod 5,
(tau^3)^2 = (tau^7)^2 = 3,
(tau^5)^2 = 2.
```

Thus the orientation-reversing source automorphisms move the marked multiplier from `2` to its inverse `3`, while the sign branch preserves the marking.

### G5, (Z/8)^* arithmetic

On the four faithful C8 characters indexed by `{1,3,5,7}`, Frobenius acts by exponent `5` and complex conjugation by exponent `7`. Verify that they are distinct commuting involutions, generate all of `(Z/8)^*`, and act freely and transitively on the four indices.

### G6, rational-observable orientation no-go

Use the same external standard-QM two-use comparison as the predecessor. Prepare

```text
|Phi> = (|00> + |11>)/sqrt(2)
```

and apply `T^k` to both qubits for `k=1` and `k=7`, where `T=diag(1,zeta_8)`. The resulting states must be entrywise complex conjugates.

Audit all sixteen two-qubit Pauli products. The ten products whose matrices have rational entries span the Hermitian rational-entry matrices. None may separate the two states. `X tensor Y` and `Y tensor X` must separate them with expectation `+1` at `k=1` and `-1` at `k=7`. By rational linearity, every Hermitian observable with rational matrix entries is orientation-blind on this pair.

This is a relative no-go. It does not exclude a target observable which already carries an orientation through `i`.

## Integrity repair

The accepted verifier is newly authored for this successor. It uses only the Python standard library and exact arithmetic:

- integers and modular arithmetic for `F_5`, `F_25` and orders;
- `math.isqrt` for the exact primality bound;
- `fractions.Fraction` in `Q(zeta_8)=Q[z]/(z^4+1)`;
- no float or complex builtin values anywhere;
- no NumPy, SymPy, mpmath, random, network, file input, subprocess, dynamic import, `eval` or `exec`.

The finite prime scan must call the integer `isqrt` helper. Any floating-point operation in a decision path is integrity `STOP`.

A later `RUN.md` must record only neutral public platform, architecture and Python metadata. No machine nickname, internal fleet label, private hostname or address is permitted.

## Firewalls

The probe MUST NOT claim:

- that TWIST-J derives quantum mechanics;
- that any TWIST-J carrier is a physical qubit, state, phase, gate or apparatus;
- a Born rule, measurement law, state preparation or Born-norm transport;
- quantum advantage, universality or speedup;
- that the marking `J_lambda=2` is derived;
- that the prime five is derived without the marked datum;
- a unique C8 generator orientation;
- that the orientation debt is physically empty or cannot be paid by transport from an independently oriented object.

## Falsifiers and decision

`REPAIRED-PASS` requires the written proofs, exact first execution from the immutable pin, no fired scientific falsifier, and the required byte-identical x86_64/aarch64 workflow.

`SCIENTIFIC-FIRED` records an exact counterexample to any frozen G1-G6 statement.

`STOP` applies to authority drift, collision, pre-pin execution or import, post-pin mutation, hidden floating point, incomplete exact carrier, security or metadata failure, nondeterminism, nonzero exit, nonempty stderr, transcript mismatch or architecture mismatch.

A repair pass changes no Canon status. Public claim registration, if ever desired, is a separate fold.

## Formal order

1. Commit and push this `PREREG.md` and the accepted `verify.py` together before the accepted verifier is imported or executed.
2. Read both public remote blobs back. Record the pin commit, SHA-256, byte counts, line endings and final LF.
3. Only after that readback execute the pinned verifier formally.
4. Add only `EXPECTED.txt`, `RUN.md`, and `RESULT.md` after a completed run.
5. Open one probe-only pull request and require x86_64, aarch64 and aggregate `check` PASS plus manual security review.
6. Never amend, rebase, squash, force-push, rename, resume or reuse the probe after the pin.
