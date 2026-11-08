# Complete lower-bound reconstruction

Status: PASS / NON-CANONICAL / L1 / candidate-C on local x86_64;
conditional candidate-T after two-architecture replay and mathematical review.
No public registry or Canon status is changed by this file.

The first public-pinned execution completed on Python3.12.14, x86_64,
with exit0 and empty stderr. Custody is in RUN.md. No falsifier fired,
no UNKNOWN remained, and the pin and thresholds were not changed.

| Auxiliary q | Initial banks | Final banks | Account-compatible pairs | Parity exclusions | Closed target exclusions | Closed source exclusions | Unknown |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 12 | 715 | 1830 | 0 | 0 | 0 | 0 | 0 |
| 17 | 5500 | 18880 | 1692 | 1584 | 108 | 0 | 0 |
| 22 | 31075 | 114985 | 70664 | 62988 | 7564 | 112 | 0 |

All values are literal multiset counts, without a Galois quotient. They
must not be equated to the earlier Galois-representative counts. The new
enumeration reconstructs its entire domain from the proved coefficient
bound; it does not trust an imported representative list.

At account22 the closed target sizes are1,5,13,25,33,57, with respectively
2908,3592,700,100,132,132 endpoint pairs. The112 remaining pairs have
closed source components of size5. No exploration stopped at the cap is
used as evidence of exclusion. All26 coordinates and permitted pair
contacts are included in every closure. EXPECTED.txt binds exact counts
and hashes of the regenerated complete banks and exclusion certificates.

The positive sixteen-contact witness passes with auxiliary account27,
and the signed fourteen-power-contact witness passes with account12.
Both full final multisets and labelled inverse paths pass. The pair-law
audit covers26244 power cases, besides every inverse/order check.

Consequently the new complete computation, with the finite-reduction proof,
supports sharp minimum27 for the stated four-slot positive preparation.
The signed minimum12 follows from its residue lower bound and witness.
The separate historical130 and294-word inventories remain unreproduced:
they are unnecessary for this minimum claim and are not silently adopted.

The account is conserved. These are initial prepared resources, not energy
spent or heat. Retained-output renewal and multi-input restrictions keep
their explicit scopes in PROOF.md and #1847. No measured quantity, native
implementation, physical instrument, occurrence law or layer lift follows.

Required next acceptance evidence: byte-identical x86_64 and aarch64
repository replay on one PR head, and an independent mathematical review
of the finite reduction, quotient, enumeration, certificates and fixtures.
The latter is not replaced by running this same script twice. Only a
separate reviewed fold can add the earned scoped result to Public Canon.
