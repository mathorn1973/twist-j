# READBACK C-SUZUKI-LOCAL-CAPACITY-NOGO-1

```text
STATUS:        NON-CANONICAL POST-FREEZE READBACK
AUTHORITY:     none
ISSUE:         #358
PUBLIC BASIS:  Public Canon v46, main 6545c1d0
PUBLIC STATUS: no change
RH STATUS:     O (unchanged)
```

This file records transport, collision, reproduction, and evidence boundaries.
It does not amend the frozen `PREREG.md`, promote a claim, or turn the notes
lane into public evidence.

## 1. Bundle provenance and transport map

The imported Git bundle had SHA-256

```text
005f64d95250970e25cb4586ac8c9a7dfc658c270413897b0f9b62d90b30be8b
```

and contained one linear branch based on `6545c1d0`:

| Object | Bundle identity | Public transport identity | Tree |
|---|---|---|---|
| frozen preregistration | `29cbc9c028c30af30f6e13c927a45283c5b61ef6` | `09368fdc74e39be973f343933a1bf7f0ea05ce04` | `c2e067b944f4b0d6a8b0c62de3cdbcf67c3e19b0` |
| verifier, breaker, result | `abd0e32ec0ec6723af3f45f07248514bc969fd21` | `f0f2a8c024dfe4d0b6c75c2002a44d352f9cb932` | `80b72597be8e32c11e77e1f0e69a7eb835524a20` |

The public transport preserves the exact two trees, file modes, file contents,
linear two-step topology, and commit order. The GitHub write surface could not
preserve the bundle's original commit object IDs, parent identities, or SSH
signature blocks. Issue #358 records the original bundle identities; the full
original-to-transport map is retained here.

Each original commit contains an SSH signature block. A cryptographic
self-consistency check succeeds when the recovered public key is supplied,
but that key is not bound to the author by a public GitHub signing-key record
or a trusted `allowedSigners` map. The signatures therefore support object
integrity only; they do not establish a publicly verified signer identity.

Frozen content hashes:

| Actual path | SHA-256 |
|---|---|
| `PREREG.md` | `37cc1a43238a4b076578a59b70009628d61b31f9da126b7e02662cdaad1d8218` |
| `verify.py` | `c68381aff92bd6b01d2170e40d1d82da909f7ec11c3f597516da8c1c1e128ddb` |
| `break.py` | `f624e530b53c94c2f40d355dd26d0a038518e2d2162f81c6a9ac1abc77f65e55` |
| `RESULT.md` | `df464b36a69d2710b5d329bad2d098daf3852f96e66df84d1b36ff45e32c0f26` |

## 2. Frozen-name readback

The frozen prose names long-form artifacts, while the bundle stores short
paths. The content hashes, rather than the prose filenames, identify the
objects:

| Name in frozen prose | Actual path |
|---|---|
| `PREREG-C-SUZUKI-LOCAL-CAPACITY-NOGO-1.md` | `PREREG.md` |
| `verify_suzuki_local_capacity_nogo_1.py` | `verify.py` |
| `breaker_suzuki_local_capacity_nogo_1.py` | `break.py` |

This mismatch is documented, not repaired in the frozen files.

## 3. Collision readback and scope firewall

The frozen collision paragraph did not include the required remote issue,
branch, and lock scan. Before the bundle's commits, the public repository
already contained related lanes #354, #355, and #357. Therefore the broad
frozen statement that the collision scan was clean is superseded as a process
claim by this readback.

There is no path collision, but there is both scientific adjacency and one
claim overlap:

- #355 studies the signed half-angle/Krein factorization of Suzuki's scalar
  screw kernel;
- #357 studies the functional candidate `q_A,a(v)` for the localized Weil
  form;
- #358 studies scalar functions `A(t)` and `P(t)` and rules out specified
  ramp, filtration, domination, and screw realizations.

The prime-kernel half of #358 N5 is the same theorem as the complete-prime-
sector no-go in #355, up to the sign convention relating `K_P` and `G_P`.
They must not be counted as independent claims. The analytic two-point witness
`t=+/-(1/4)log 6` in #355 is a short exact proof; V5 at `(3,6)` is a secondary
one-architecture computational witness for the same prime-kernel no-go. The
`K_A` half of N5 is a different scalar-capacity statement and remains governed
by its own evidence.

In particular, the scalar `A(t)` no-go in this lane does **not** decide
`q_A,a(v)>=0`, G3, or any of G4-G6 in #357. Conversely, an eventual result on
`q_A,a` would not silently repair a failed scalar ramp model here.

## 4. Reproduction record

On Linux x86_64 with Python 3, the frozen `verify.py` rerun produced exit 0,
empty stderr, `12/12` PASS, 1054 stdout bytes, and

```text
sha256(stdout) = ad99e73f827fbc075342d93fbc8e840c05cba8764c99b5c26bedf37b46050a84.
```

With `mpmath==1.3.0`, the frozen `break.py` rerun produced exit 0, empty
stderr, and

```text
sha256(stdout) = 9819e011f74b12b3f78ef88c96b77f14fd18a738cd0b0675ce5eb03943bb8a6e.
```

These are exact same-script reproductions, not independent confirmation. The
breaker is a distinct implementation path for its stated finite checks, but
both recorded runs are on one architecture. No `EXPECTED.txt` or `RUN.md` is
present; that is acceptable for a notes incubation but insufficient for a
future public probe package.

V5's event guards are wider than integer-floor guards but are sufficient for
the prime-power event stream: there is no prime power strictly between 20 and
23, nor strictly between 401 and 409. Thus the next events after the frozen
lists are 23 and 409. This exact finite fact should be checked explicitly by
any promoted verifier instead of being left implicit in prose.

## 5. Evidence and status ceiling

The frozen labels are read as follows without modifying their preregistered
text:

- N1 is supported by the written elementary identity; its verifier run is an
  audit of that identity.
- R2 is an attributed reproduction and carries no novelty claim.
- N3's all-variable emptiness theorem follows from the written proof that the
  frozen ramp class is convex while `A''<0` on a nonempty interval. The V3
  triple is an audit witness. The phrase `the class carries candidate-F` in
  `RESULT.md` is not a public status and is read only as failure of the frozen
  positive-ramp route, not as an additional registered claim.
- N4 uses machine-decided certified sign gates. Its computational evidence
  remains `candidate-C` until a second architecture or an independent written
  sign proof closes the relevant inequalities, irrespective of the stronger
  label printed in `RESULT.md`.
- N5 is a conjunction. Its prime-kernel half now has the independent exact
  two-point proof cross-recorded in #355; its scalar-capacity `K_A` half remains
  a one-architecture certified sign result. The combined N5 statement therefore
  retains the lower evidence ceiling until that second half is independently
  closed.
- R6 and R7 remain `candidate-C`, as the result itself records. The
  preregistered R6 `candidate-T` target was not earned. V6 proves `A>0` on
  `[1/128,45/64]`, but this is a prime-free statement about `Psi=A` only on
  `[1/128,log 2]`; the short tail beyond `log 2` must not be called prime-free.
- N8 applies only to one global diagonal model satisfying
  `||Z_t||^2=A(t)` and `T Z_t=Y_t` for all relevant `t`. If
  `||T||<=1-delta`, then
  `Psi>=delta(2-delta)A ~ 4 delta(2-delta)e^(t/2)`. The frozen result's
  asymptotic display `~4 delta e^(t/2)` omits the factor `(2-delta)`; the
  exact preceding inequality is the governing statement. This argument does
  not apply automatically to unrelated windowed contractions `T_a` or to
  every Gram realization. The required `Psi=o(e^(t/2))` is available directly
  from Suzuki arXiv:2206.03682 Theorem 1.1(3), so a future proof need not leave
  a partial-summation step implicit. The conclusion is only that a contractive
  global `T`, if it exists, has norm one and admits the displayed vectors with
  norm ratio tending to one. It does not prove that `T` is an isometry on its
  whole space. With no machine gate, this remains a NON-CANONICAL candidate and
  earns no public status here.

The parent chain establishes only that the preregistration commit is the
parent of the result commit. It does not independently date the authoring or
first execution of either file. The shared timestamps do not establish elapsed
time, and the three pre-run defects mentioned in `RESULT.md` have no archived
defective objects. This limits provenance claims but does not alter the frozen
tree.

## 6. Consolidation consequence

This lane contributes one bounded conclusion: the frozen nonnegative-ramp,
Stieltjes-filtration with increment domination, and separate scalar screw-
kernel models fail. N8 additionally constrains the one stated global diagonal
model. These no-gos do not exhaust all Gram realizations. The lane supplies no
positive capacity, no global contraction, no RH evidence, and no Canon,
Registry, frontier, or evidence-ledger movement.
