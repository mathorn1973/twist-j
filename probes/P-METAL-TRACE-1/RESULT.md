# P-METAL-TRACE-1 result

Status: SCIENTIFIC RESULT; ONE ARCHITECTURE CLASS (x86_64); AARCH64 LEG
PENDING

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
CI           x86_64         -        pending            required check at pull-request time
aarch64      -              -        PENDING            the open two-architecture obligation;
                                                        appended here as a neutral leg record
```

Provenance (informational, not a leg): the incubation candidate session,
whose artifacts are recorded by hash in issue 70, reported the same stdout
sha256 (Python 3.12.3) for its pre-probe run of the byte-identical
verifier. That record is non-public and earns nothing here.

## Gate

Two-architecture computation gate: NOT YET PASSED. The formal local leg
and the GitHub check are both x86_64, which is a reproduction, not a
two-architecture gate; under POLICY.md a computation-only result at one
architecture class stands at most at C. The aarch64 local leg on the
byte-identical pinned verifier is the single remaining step; a differing
byte fires the preregistered failure threshold. The identities appear to
admit short self-contained classical proofs; the owner may pursue an
independent theorem-grade write-up, which could establish T with this
verifier as its audit. Both routes are owner decisions.

## Fold

Any registry row (METAL-TRACE-CASCADE), Canon section 4 text, or
reproduce/ bundle is a separate sealed fold under POLICY.md and is NOT
part of this probe pull request. The candidate fold proposal is staged
outside this probe directory (notes lane). The public lock is issue 70.
