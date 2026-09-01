# Promotion handoff: `C-C40-RECIPROCAL-RAMIFIED-SEAM-N`

This is a **NON-CANONICAL handoff**, not a promotion request and not a Canon
patch. The strongest present status is `candidate-T / L1`.

## Candidate statement for a later public fold

For \(K_{40}=\mathbf Q(\zeta_{40})\):

- \(\Phi_{40}=x^{16}-x^{12}+x^8-x^4+1\);
- at `2`, \(\Phi_{40}\bmod2=\Phi_5^4\) and `(e,f,g)=(4,4,1)`;
- at `5`, \(\Phi_{40}\bmod5=\Phi_8^4=(x^2-2)^4(x^2-3)^4\) and
  `(e,f,g)=(4,2,2)`;
- for `p` not dividing `40`, the modulo-`40` classes give exactly the atlas
  and densities recorded in `README.md`;
- the Galois group is `C4 x C2 x C2`, has exponent `4`, and admits no
  unramified inert rational prime;
- `Phi_40 mod p` is nevertheless reducible for every rational prime `p`, by
  the two ramified identities plus the complete unramified order argument.

The local rider is mandatory: `Phi_40` is irreducible over `Q_2`, while over
`Q_5` it has two degree-`8` factors. Repeated modular factors are nonreduced
ramified reductions, not etale products and not a field merger. “Reciprocal”
means complementary primary roles, not a symmetry exchanging `2` and `5`.

## Registered imports that a fold must preserve

- `DQRC-MAXIMAL-SECTOR-FIELD-BOUNDARY [T]` owns the compositum,
  intersection, and degree;
- `QUARTIC-CYCLOTOMIC-TOTAL-RAMIFICATION-CENSUS [T]` owns the underlying
  quartic total-ramification inputs;
- `J-BINARY-NORM-INDEX [T]` owns the inert `2` / `F_16` input in `K_5`;
- `BORN-RESIDUAL-SPLIT [T]` owns the `Phi_8 mod 5` two-quadratic split and
  conjugation action.

No later fold may present these dependencies as new output or use this packet
to promote `I-BILOCATED` or any other registered row.

## Evidence available to a later fold

- scope and decisive falsifiers frozen at commit
  `aa44cfe32bf461c217d6046ff3c835d3bd12eca7` before execution;
- public hash/readback record in issue #750;
- exact standard-library principal verifier with captured stdout;
- separately authored blind breaker with captured stdout;
- exact proof in `README.md`, including the Dirichlet density input;
- content manifest in `SHA256SUMS`.

Finite prime scans are audits only and must never replace the universal group
argument.

## Requirements before any promotion

A future owner must re-bootstrap the then-current public authority, rescan
Canon and all live work for collision, reproduce both frozen programs, review
the proof independently, and use a distinct policy-compliant public fold.
This packet itself moves nothing.

## Permanent exclusions

No RH claim, physical bridge, causal mechanism, field merger, selector,
orientation choice, evidence credit, or autonomous status movement follows
from this incubation.

