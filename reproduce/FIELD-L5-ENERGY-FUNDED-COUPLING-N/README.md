# Exact local L5 coupling audit

PUBLIC / NON-CANONICAL, L1. Candidate C-FIELD-L5-ENERGY-FUNDED-COUPLING-N,
claimed in issue #1305. No Canon status is assigned by this reproduction.

The self-contained law, proof, preregistration and two independent exact
implementations are in `notes/C-FIELD-L5-ENERGY-FUNDED-COUPLING-N/`.
The preregistration was frozen at
`f3993f87f537cfaa991bef3875ba5d74bfc82855` before implementation execution.

This bridge checks the literal SHA-256 of the preregistration and each source,
then executes the primary and challenger in order. They share no scientific
helper and use only the Python standard library. The primary verifies its
public source context; the challenger reconstructs from frozen definitions.
Both audit the stated matrix identities, full-state funded involution,
pointwise Gauss defect, exact inverse, admission and rejection boundaries,
all frozen finite fixtures and the two period-ten witnesses. The proof,
rather than the finite test set, supports the universal statements.

The five ASCII/LF lines in EXPECTED.txt are the prospective success target
specified before execution. They become an observed result only when the
unchanged runner confirms equality, as recorded in the candidate RUN.md.

From the committed repository root, use the current repository runner:

```text
python3 tools/check_reproduce.py --base b8ba1a07ad776cdd8d878fe0a407e07312c0e263
```

The runner owns timeout, environment, exit/stderr and exact-output policy.
The ordinary PR workflow runs this same reproduction on x86_64 and aarch64.
There is no runtime network, private archive or external package dependency.
The selected closed cell has Ucell^10=I; passing this audit does not establish
directed decay, transport, permanent recording or a multicell automaton.
