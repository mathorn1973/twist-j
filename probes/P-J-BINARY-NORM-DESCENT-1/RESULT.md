# P-J-BINARY-NORM-DESCENT-1 result

Date: 2026-08-21

```text
DECISION:   J-BINARY-NORM-DESCENT-CONFIRMED
CHECKS:     20 of 20 PASS, exit 0, empty stderr
PIN:        846f116b817284c688235bbea729cd9a9cd1f20f
CLAIM LOCK: issue 499
LAYER:      L1 integral / finite-field algebra only
BASIS:      Public Canon v59, tag canon-v59, content 5da6b883,
            CANON_SHA256 7fdea700...87f641, CANON_BYTES 314310
```

No threshold moved after the pin. No mathematical falsifier fired. This result
changes no Canon, Registry, Frontier, Evidence or Gate row. A fold is a
separate later act. The public two-architecture workflow is still required
before this probe can be merged as computation-backed public evidence.

## 1. The result

The characteristic-zero affine form from `P-AFFINE-QUADRATIC-READING-1`
has an exact binary residue presentation:

```text
O = Z[zeta_5],
O/(2) ~= F16,
O_(K+)/(2) ~= F4,
q_2(y) = q_+(y) mod 2
       = Tr_(F4/F2)(N_(F16/F4)(y)).
```

The polar form of `q_2` is nondegenerate and

```text
q_2(y)=0 for y != 0
iff N_(F16/F4)(y)=1
iff y in mu_5.
```

Hence the complete nonzero singular locus of the binary reduction is the five
cyclotomic points themselves.

The integral A4 bridge is exact:

```text
P(A4)=(zeta_5-1)O,
P mod 2 : A4/2A4 -> O/2O is an F2-linear isomorphism,
q_+(P x) = (5/2) sum_r x_r^2,
q_+(P x) mod 2 = q_A(x mod 2).
```

Thus the already registered `CARRY-PENTAD [T]` form and the binary residue of
the unique affine `q_+` are the same quadratic carrier under `P mod 2`.
`CARRY-PENTAD` already owns the Arf-1 and `O^-(4,2) ~= S_5` consequences; this
probe claims no new S5 theorem.

## 2. The type correction survives the formal gate

The probe deliberately armed the distinction between the multiplication motor and Frobenius. It passed:

```text
bar(D_J)(y) = alpha^2 y,
Frob_2(y)   = y^2,
bar(D_J) != Frob_2.
```

On `mu_5=<alpha>` they act on exponent labels as

```text
bar(D_J): k -> k+2,
Frob_2:   k -> 2k.
```

They are the translation and dilation generators of the same sharply
two-transitive `AGL_1(F_5)` action of order 20. Frobenius is the reduction of
the Galois generator `u`, not of the multiplication motor `D_J`.

This also blocks the earlier overstatement that the exponent action selects
rational prime 2: every prime `p == 2 mod 5` has the same Frobenius exponent on
fifth roots. Characteristic two is not selected by that fact alone.

## 3. Field integrity, with nonselective controls

The binary shadow is one field because `Phi_5` is irreducible over F2:

```text
Z[zeta_5]/(2) ~= F16.
```

The controls behave differently:

```text
Z[i]/(2)       nonreduced,
Z[zeta_7]/(2)  ~= F8 x F8,
Z[zeta_3]/(2)  ~= F4.
```

The last control matters. Being a field modulo two is not unique to the
fifth-cycotomic case and is not a selector for J.

## 4. Status and scope

The written proofs in `PREREG.md` carry the universal statements; the finite
verifier is an exact audit of all sixteen residue elements and the integral
bridge. The target later row is therefore theorem-grade at L1 if review and
the required public workflow accept the proof chain:

```text
J-BINARY-NORM-DESCENT [T]
```

At the current branch state this is a probe result, not a Canon promotion.
One local x86_64 formal leg has passed. The repository workflow must still
reproduce `EXPECTED.txt` byte for byte on public x86_64 and aarch64 and pass
the aggregate `check` before merge.

## 5. Firewall

```text
MAY
  the field-integrity theorem, the Galois/Frobenius descent, the required
  motor/Frobenius inequality, the norm-trace formula, the mu5 singular locus,
  the A4 ideal/isometry bridge, and the final comparison to CARRY-PENTAD.

MAY NOT
  uniqueness of J, p=5, order five or characteristic two; any J-specific
  significance for F2, XOR, AND or Boolean completeness; a derivation of
  Thue-Morse; a claim that quadratic degree alone selects characteristic two;
  a new Arf or S5 theorem; Born probability; effect, apparatus, instrument,
  event stream, sampling, measure, decoder completion, spacetime, force, SI
  value, or any L2-L6 lift.
```

`READING-SPLIT [D]`, `QUADRATIC-DECODER-DATA [O]` and every QDD apparatus row
remain unchanged.

```text
SAMPLING NOT PROVIDED.
```

## 6. Exposure

RESULT-EXPOSED, as preregistered. Discovery work existed before the pin and is
not evidence. The accepted verifier was newly authored, committed together
with the preregistration, read back by Git-object identity before execution,
and then executed exactly once for the recorded local leg.
