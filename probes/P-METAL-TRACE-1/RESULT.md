# P-METAL-TRACE-1 result

Status: SCIENTIFIC RESULT; TWO-ARCHITECTURE COMPUTATION GATE PASS

## Scientific decision

```text
DECISION POSITIVE
```

All 19 preregistered exact assertions hold on the pinned verifier. No
falsifier fired and no threshold moved after the pin. The frozen cascade
stands at its declared scope:

```text
metal law     phi^2 = phi + 1 (t = 1)      delta^2 = 2 delta + 1 (t = 2)
units         N(phi) = -1                  N(delta) = -1
trace         Tr(phi) = 1                  Tr(delta) = 2
disc          t^2 + 4 = 5                  t^2 + 4 = 8
ramified      5 | 5 -> Q(sqrt5)            2 | 8 -> Q(sqrt2)
growth        phi^n = F_n phi + F_(n-1)    delta^n = P_n delta + P_(n-1)
pure form     N(J = 1 + zeta_5^2) = 1      1 + i = sqrt2 m_8 = sqrt(2i),
                                           (1 + i)^2 = 2i,
                                           N_{Q(zeta_8)}(1 + i) = 4
```

## Scope

The claim is scoped to the two simplest metals t in {1, 2}: the
trace-to-field map is not injective for general t (t = 4 also lands in
Q(sqrt5); the non-formal break path pinned this boundary). Norm degrees are
stated per field: N(1 + i) = 2 over Q(i) and 4 over Q(zeta_8); assertion
(c) uses the degree-4 norm. The growth identities are verified at n <= 11
as witness, not as scope. The run/record physical reading (combine vs
copy, reversible run vs irreversible write) is H material outside this
probe and earns nothing here.

## Legs

```text
leg          architecture   python   result             stdout sha256
-----------  ------------   ------   ----------------   ----------------------------------------
local        x86_64         3.11.15  ALL OK, 19 checks  8f1567fd0d9f2ac766d8242821ec8bff6277a3c40fcd467a284662dd9de54d12
                                                        (1101 bytes, 20 lines, empty stderr, exit 0)
CI           x86_64         -        VERIFY PASS        policy workflow run 29682530733
                                                        (job 88181118811) on commit ca4cd46,
                                                        required check green
local        aarch64        3.12.3   ALL OK, 19 checks  8f1567fd0d9f2ac766d8242821ec8bff6277a3c40fcd467a284662dd9de54d12
                                                        (1101 bytes, 20 lines, empty stderr, exit 0)
```

The aarch64 leg ran on Ubuntu 24.04 LTS from a clean shallow clone of
`probe/P-METAL-TRACE-1` at commit
`46b9f5d3b4d280ea967c503082349bd202b01c18`, with the pinned verifier
hash confirmed equal to
`57501a2975ff71a43a1e5f98e7f976e35d27dd6252143fb5d20ce715375fff2a`
before execution, under
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`,
run from the repository root. Its stdout was compared byte for byte
(`cmp`) against the committed `EXPECTED.txt` and is identical.

Provenance (informational, not a leg): the incubation candidate session,
whose artifacts are recorded by hash in issue 70, reported the same stdout
sha256 (Python 3.12.3) for its pre-probe run of the byte-identical
verifier. That record is non-public and earns nothing here.

## Gate

Two-architecture computation gate: PASS. The aarch64 local leg and the
x86_64 legs (the formal local leg of RUN.md and the GitHub required
check) reproduce
`8f1567fd0d9f2ac766d8242821ec8bff6277a3c40fcd467a284662dd9de54d12` byte
for byte from the byte-identical pinned verifier. The pin was published
before any execution and the decision surface was not weakened after the
pin. No falsifier fired: a single differing stdout byte would have fired
the preregistered failure threshold. The identities appear to admit
short self-contained classical proofs; an independent theorem-grade
write-up remains available to the owner, with this verifier as its
audit. Status motion (any registry row and its status) is the owner's
fold decision, outside this probe.

## Fold

Any registry row (METAL-TRACE-CASCADE), Canon section 4 text, or
reproduce/ bundle is a separate sealed fold under POLICY.md and is NOT
part of this probe pull request. The candidate fold proposal is staged
outside this probe directory (notes lane). The public lock is issue 70.
