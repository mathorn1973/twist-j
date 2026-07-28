# PREREG C-EM-UNIT-CARRIER-1

NON-CANONICAL. Frozen before any verifier code is written or run.

```text
candidate_id    C-EM-UNIT-CARRIER-1
target line     mathorn1973/twist-j (public)
basis           Public Canon v25, tag canon-v25, content commit b914755b,
                canon/CANON.md sha256
                53fa5acc9f2d910b26293d5152d93deac6596abd012997c7ff195397d9e476bb,
                canon/SHA256SUMS verified 5 of 5 OK at freeze time
status ceiling  C
```

## 1. Equation

Frozen definitions, exact, symbolic:

```text
alpha := e^2 / (4 pi eps_0 hbar c),   mu_0 eps_0 c^2 = 1,   hbar := h / (2 pi)
R_K   := h / e^2
Z_0   := sqrt(mu_0 / eps_0) = mu_0 c
G_0   := 2 e^2 / h
Phi_0 := h / (2 e)
K_J   := 2 e / h
```

Frozen assertions:

```text
E1  Z_0 = 4 pi alpha (hbar / e^2) identically
E2  Z_0 / R_K = 2 alpha identically
E3  each of R_K, G_0, Phi_0, K_J is a monomial in h and e with rational
    coefficient and integer exponents, and contains no alpha
E4  empirical input count over the audited set is 0, 0, 0, 0 for
    R_K, G_0, Phi_0, K_J and 1 (alpha) for Z_0
E5  in the dimension lattice spanned by the SI exponents of h and e alone,
    the mass direction is not reachable: no rational exponent pair (a, b)
    gives dim(h^a e^b) = mass
E6  the electromagnetic rows of canon/REGISTRY.tsv cite no calibration input
    other than m_e
```

E1 to E5 are symbolic and exhaustive. E6 is a finite register audit at the
frozen basis, hence the ceiling C.

## 2. Code

```text
verifier      notes/C-EM-UNIT-CARRIER-1/C-EM-UNIT-CARRIER-1_verifier.py
language      Python standard library only
arithmetic    fractions.Fraction over an explicit dimension vector space and an
              explicit symbolic monomial type; no float in any assertion; no
              third party CAS
runtime       under 120 seconds
environment   LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC
              run from repository root
output        deterministic stdout, one line per frozen assertion, final line
              PASS or FAIL with the fired identifier
```

Compilation and static checks are permitted before the pin. No formal gate is
run before the pin.

## 3. Carrier or data

```text
carrier   the SI dimension lattice over the base exponents
          (mass, length, time, current), with h, e, c, eps_0, mu_0 entered by
          their exact SI dimension vectors and by the frozen definitions above
data      canon/REGISTRY.tsv and canon/CANON.md at the frozen basis commit,
          read only, hashes checked against canon/SHA256SUMS before the audit
external  none. No CODATA value, no measured number, no fitted quantity is
          read at any point. The 2019 SI exactness of h and e is a definition,
          entered as such.
```

## 4. Systematics

```text
S1  post-2019 SI only. Any pre-2019 reading, in which mu_0 was exact and h was
    measured, inverts the empirical bookkeeping and is out of scope. The
    verifier states the SI epoch as a frozen constant.
S2  the audit of E6 is only as complete as the register at the frozen basis.
    A later public fold can add a row that changes it; the result is scoped to
    the frozen commit and says so.
S3  "empirical input count" is defined before the run as the number of
    independent measured dimensionless quantities appearing in the exact
    expression of the constant, with h and e counted as zero because they are
    definitions. This definition is frozen here and is not adjusted afterwards.
S4  identification of Z_0 and R_K with laboratory quantities is a reading, not
    an assertion of the verifier. The verifier operates on the frozen
    definitions only.
S5  alpha enters as a symbol. Whether the register derives it is out of scope.
```

## 5. Failure threshold

```text
the candidate fires on any one of:
F1  a member of the audited set requiring an empirical input beyond alpha
F2  a rational exponent pair (a, b) with dim(h^a e^b) = mass
F3  symbolic failure of E1 or E2
F4  an electromagnetic register row citing a calibration input that is neither
    m_e nor derived
F5  any float in an assertion
threshold   exact. No tolerance, no window, no approximate equality anywhere.
            There is no numerical comparison to loosen.
on firing   the run record and the witness are committed; the candidate is
            relabelled F; the threshold is not moved and the file is not
            deleted.
```

## 6. Action layer

```text
L6 (measure).
```

The claim concerns the unit and measurement map only. It asserts nothing at
L1 state, L2 manifold, L3 boundary, L4 support or L5 stream. Any lift to
another layer requires its own named gate and is not authorized here.

## 7. Break plan, declared before the run

```text
B1  independent path: rebuild the dimension check from the SI base unit
    definitions of the 2019 revision rather than from the frozen definition
    list, and require the same verdict on E5
B2  adversarial search: enumerate rational exponent pairs over a declared range
    seeking a mass direction from h and e alone, and report the nearest miss
B3  register adversary: grep the full register, not only the rows judged
    electromagnetic, for any calibration or anchor token, and hand-classify
    every hit
B4  epoch adversary: run the same bookkeeping in the pre-2019 SI and confirm
    the verdict inverts as S1 predicts. If it does not invert, the bookkeeping
    definition in S3 is wrong and the candidate is suspect even if it passes.
```

Freeze ends here. Nothing below this line existed at pin time.
