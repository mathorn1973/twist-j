# Reconciliation of the post-PR-243 intermediate review

NON-CANONICAL. This note records how the supplied public review is
applied after PR #243 was merged. It does not amend the sealed
incubation bundles, claim a probe, or move any public status.

The review inspected the correct PR head but described PR #243 as open.
It is now merged at `a2198c477898963a815a09c34b8bb45c40d4a7b9`.
Its scientific corrections remain useful and are applied here on a new
notes-only surface.

## Accepted corrections

1. **N9 separates theorem from reading.** The exact facts are
   `nu^4 = -I`, `(1-J)^5 = -1`, and
   `tau(phi^-1) = -phi < 0`. The last formula uses `tau|F`; the CM
   involution `sigma = tau^2` fixes `F`, so the former spelling
   `sigma(phi^-1) = -phi` was false. Reading these typed witnesses as
   one ontological bit is `[D]`, not a theorem gate, and is omitted from
   the future verifier.
2. **N11 must require one multiplier.** The old gate checked two
   totally positive block multipliers without checking their equality.
   For the explicit normalization `C0` and `d = phi`, exact arithmetic
   gives `kappa = N(d) = phi^2`. The hardened target is therefore the
   stronger single identity

   ```text
   B0^dagger H_pair B0 = phi^2 tau(H_pair).
   ```

3. **The unused tuple entries are removed.** `A_J` and decoder `Q` do
   not enter E1-E4. The narrow L4 probe freezes neither and fills no
   `QUADRATIC-DECODER-DATA` slot.
4. **The Schur form must be complete inside the verifier.** The unified
   candidate audits both scalar centralizers, both zero Hom blocks, the
   one sigma-intertwiner line, the scalar lower off-diagonal block, and
   the combined pair kernel.
5. **The square is typed narrowly.** `nu^2` is block-diagonal and
   sigma-semilinear. Its linear coefficient is not the identity, so it
   is not called bare coordinate conjugation.

## Additional corrections required by the cocycle

- `{1,sigma}` is the stabilizer of the marked twist-isomorphism class,
  not a descent subgroup. Although `rho^sigma ~= rho`, the cocycle
  class `[-1]` prevents normalizing its semilinear intertwiner to an
  involution and therefore obstructs an `F`-form through that datum.
- A Q-valued character of `rho (+) rho^tau` does not alone construct a
  Q-form or coherent `C4` descent datum. The pair's Galois-stable
  `K`-isomorphism class is instead certified by explicit intertwiners
  for `tau`, `sigma`, and `tau^3`. They are not claimed to satisfy a
  descent cocycle. The order-eight central lift is the obstruction made
  explicit, not an ordinary `C4` action.
- Equality of trace multisets does not construct an outer automorphism.
  The narrow statement records exchange of the two golden trace values
  but identifies no conjugacy classes and asserts no outer descent until
  an automorphism and intertwiner are frozen.
- The existing first incubation verifier's prose says `sigma(G)=G`
  setwise while its Q2 gate checks `sigma(G) != G`; the future verifier
  retains only the exact checked intersection/twist facts.

## Resulting scope

The healthy theorem target is the fixed-representative L4 statement:
marked twist stabilizer, Galois-stable pair isomorphism class, complete
tau-semilinear block classification, norm obstruction, minimal
attainable order eight, single-branch invariant Gram line, and balanced
pair similitude. The cross-lane phrase "the same bit" remains optional
`[D]` interpretation outside the theorem and verifier.
