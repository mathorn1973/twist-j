# Informal audit record

NON-CANONICAL. Issue #2102 posted before the numerical run. The accepted
public-probe pin, runners and architecture gate were not invoked.

First audit: Linux aarch64, Python 3.11.2, exit 0.
Command: python3 verify.py > EXPECTED.txt
verify.py SHA-256: 460367464555443f226364d2c99f2dc64002bd548aa9a1ee1a07ad669a33edb7
EXPECTED.txt SHA-256: f676e55cee675bfd15b60036d12b2a7e8d66ef7c06759ed797ac60e461afd642

Second audit: Linux x86_64, separate combination-basis creation matrices,
SymPy Smith normal form, direct polynomial quotient and explicit reader
matrix. Exit 0; matching two-cut Smith lists and all reader/covariance tests.
The archived break.py is a cleaned, equivalent copy of that executed
source (unused imports and comments removed); it is result-exposed and
has not been represented as a blind second-agent review. The second audit
does not give byte-identical formal two-architecture evidence.

No new scientific status in the public registry. No external preprint
Lean build was executed. No licensed external code was incorporated.
