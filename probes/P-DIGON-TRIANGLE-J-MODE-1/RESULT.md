# P-DIGON-TRIANGLE-J-MODE-1 result

Status: FORMAL PROBE RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS; PUBLIC CLAIM UNREGISTERED

## Recorded decision

```text
verdict: RESULT PASS checks=26 fails=0
exit:    0
stderr:  empty
```

No preregistered falsifier fired. All seven clauses T1 to T7 of PREREG.md
hold exactly in Q(zeta_5):

```text
T1  charpoly(T) = (x-1)^2 Phi_5(x), T^5 = I, T != I
T2  modes mu = zeta_5^k with face amplitudes (digon, triangle) = (1, r_k),
    r_k = 2 - |1 - mu|^2 = mu + 1/mu, T v = mu v
T3  r_k mu = 1 + mu^2 = sigma_k(J); k = 1: r = 1/phi = |J|, r mu = J
T4  lambda_k + 1/r_k^2 = 4; k = 1: (3 - phi) + phi^2 = 4, legs |1 - zeta_5| and phi, hypotenuse 2
T5  the form 1 + mu^2 iff the reference face is a digon; a triangle gives 1 + mu + mu^2
T6  census of two-face single-shared-edge Gram cells in the window: (1,1) degenerate,
    (1,2) order 10, (1,3) order 8, (2,2) orders 3 and 6, (2,3) order 5, (3,3) wall;
    (2,3) is the only one with modes of order 5; (1,2) reads as the conjugates of J
    at angles 36 and 108 degrees
T7  reversed shared edge: r_k mu = -sigma_k(J)
```

The proof-first conclusion at the declared scope: the polar form of
J = 1 + zeta_5^2 is realised by the digon + triangle cell, with the modulus
1/phi as the amplitude ratio triangle/digon and the argument 2 pi/5 as the
mode frequency; the right triangle with legs |1 - zeta_5| and phi and
hypotenuse 2 is the k = 1 mode; the digon row is what produces the form
1 + mu^2.

## Gate record

```text
preregistration pin:  86eaa9f622227e723859865ce9ca918e30ceb548
public lock:          issue 1732

local platform:       Ubuntu 24.04.5 LTS
local architecture:   x86_64
local Python:         CPython 3.13.17
local executions:     3, byte-identical
local exit/stderr:    0 / 0 bytes

verifier SHA-256:     d8ce54f6b125220efa4bb2999fd6a6007925a16d2edc596e2346dbbd9915a778
stdout SHA-256:       cdfb2fc3207476ce3cc1010ea4692fd4f4a2a98714e743ce2b2ae2ccb6a2e4ff
stdout bytes:         1960
stdout lines:         27

formal evidence head: 535429e6f5510d4363953d9f6cb7aa1c38069032
pull request:         1733
workflow run:         39994845185 (policy), conclusion success

x86_64 job:           120555577015, GitHub-hosted ubuntu-latest, architecture-x86_64,
                      step "Reproduce changed public probes" success
aarch64 job:          120555577562, GitHub-hosted ubuntu-24.04-arm, architecture-aarch64,
                      step "Reproduce changed public probes" success
GitHub Python:        CPython 3.12 per the workflow's setup-python pin; the exact
                      patch level was not read back from the job logs here
check job:            120556120373, TWO-ARCHITECTURE CHECK PASS

byte identity:        PASS on both GitHub architectures; tools/check_verifier.py fails
                      the job unless the replay reproduces EXPECTED.txt byte for byte
                      and the pinned verifier hash matches
computation gate:     PASS (x86_64 local, x86_64 GitHub, aarch64 GitHub)
```

The GitHub policy workflow succeeded on the formal-evidence head and enforced
verifier integrity against the pin commit, exit zero, empty stderr, and
byte-identical `EXPECTED.txt` on two architectures. `RUN.md` remains the
neutral local x86_64 record. This close-gate update changes only `RESULT.md`.

## Scope, credit and status

`verify.py` audits the identities; the theorem rests on the one-line proof
frozen in PREREG.md section 3 (G M = |1 - mu|^2 M and the first row of G).
The orders of the five unweighted cells are already registered in
FIELD-FIVE-CELL-SHEAR-COMPARISON [T] and are inherited, not re-claimed. The
identification of this cell's active lattice with Z[zeta_5] and of I + A^2
with J in the unmerged notes C-FIELD-CYCLOTOMIC-WINDOW-N and
C-FIELD-CYCLOTOMIC-WINDOW-AUDIT-N (issue 1301, pull request 1304) is
credited; this probe adds the per-mode amplitude-ratio form and the
hypotenuse-2 identity and uses neither note as a dependency.

The incubation lane of the author ran the same checks before the public pin
(verifier SHA-256 ebfa53264d519d673ba11829a9151efb38b7fbe6d0ae5f4b4c08f53f58431518,
same stdout SHA-256 as above; independent F_p breaker SHA-256
9be2a01438938671d734f10f5a92ee635a740587651c63011eb2b99fbae90847, PASS).
The public pin is the first execution in this repository.

This probe changes no normative Canon file. No physical or native selection
of the cell is claimed. Registration, if any, is a separate sealed fold with
proposed row DIGON-TRIANGLE-J-MODE in section 1 of the Canon.
