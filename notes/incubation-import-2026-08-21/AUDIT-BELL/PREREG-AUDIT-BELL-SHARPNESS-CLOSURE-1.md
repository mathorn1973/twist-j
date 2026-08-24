# PREREG: AUDIT-BELL-SHARPNESS-CLOSURE-1

```text
ID:          AUDIT-BELL-SHARPNESS-CLOSURE-1
STATUS:      INTERNAL, NON-CANONICAL. Candidate-lane audit. No authority.
TARGET:      the PASS-BRIDGE + STOP-SOURCE verdict on the prime-2 Clifford
             read, sections 1 to 7, as supplied to this session.
BASIS:       Public Canon v58. Gate run this session against
             mathorn1973/twist-j main:
             STATE ACTIVE, AUTHORITY mathorn1973/twist-j main,
             TAG canon-v58, CONTENT_COMMIT 05a0749e,
             CANON_SHA256 647822f5...6acc1, CANON_BYTES 304010,
             canon/SHA256SUMS 5 of 5 OK, tag and content commit both
             ancestors of main (HEAD 317d731).
DISCLOSURE:  RESULT-EXPOSED / IMPLEMENTATION-INDEPENDENT / NOT BLIND.
             Written after reading the verdict text and after reading
             claude/AUDIT-C-BELL-BETA-4_2026-08-21.md. Independent code,
             no import of probe or prior-audit code.
LAYER:       L1 state (algebra of the piston factor). No L2-L6 lift is
             claimed, attempted, or available here.
```

## The six fields

**1. Equation.** Over Q(i) implemented as ordered pairs of Fractions, with
no built-in complex type and no float anywhere, decide the following, each
as an exact statement:

```text
A1  invariance under the single quarter-turn (X,K,Z) -> (Z,K,-X):
    the symmetric invariants are exactly diag(a,b,a).
A2  hermiticity of eta_c(xX + yK + zZ) = xX + y c K + zZ holds iff
    c + conj(c) = 0, giving G_r = diag(1, r^2, 1) and beta(r) = 4 r^4.
A3  sharpness (cK)^2 = I over Q(i) holds iff c^2 = -1 iff c = +-i,
    and E_+- = (I +- r Gamma_2)/2 satisfies E^2 - E = ((r^2-1)/4) I.
A4  for c = +-i and Gamma = (X, cK, Z): Gamma_j^dagger = Gamma_j,
    Gamma_j^2 = I, anticommutation, (1/2)Tr(Gamma_j Gamma_k) = delta_jk;
    C_y and C_z generate a group of order exactly 24, and the space of
    symmetric M with C^T M C = M for both generators has dimension 1.
A5  eta(A) is hermitian, eta(A^T) = conj(eta(A)),
    (1/2)Tr(eta(A) eta(B)) = xx' + yy' + zz', -det eta(A) = x^2+y^2+z^2.
A6  for real 2x2 M, T_ij = Tr(M^T S_i M S_j^T) with S = (X,K,Z) and
    C_ij = Tr(M^T Gamma_i M Gamma_j^T) with Gamma = (X,-iK,Z) satisfy
    C_ij = T_ij for all (i,j) except C_22 = -T_22, and C^T C = T^T T,
    with Spec(C^T C) = {Q^2, R^2, R^2}.
A7  CLOSURE TEST. For 2x2 traceless hermitian H:
    H^2 = -det(H) I and Tr(H^2) = -2 det(H). Hence
    H^2 = I  <=>  ||H||_F^2 = 2.
    A7 decides whether the verdict's sharpness condition is a NEW
    condition or is the SAME equation the 2026-08-21 audit already named
    as the open obligation.
A8  BREAK ATTEMPT on A6: search for a real M with a nonzero entry in the
    four off-block positions (1,2),(2,1),(2,3),(3,2) of T. If one exists,
    C_ij = T_ij fails there and the verdict's section 6 is wrong as
    written.
```

**2. Code.** `audit_bell_sharpness_closure_1.py`, Python standard library
only, exact arithmetic (Fraction, hand-rolled Q(i) and Q[a,b,c,d]), no
float in any assertion, no built-in complex, run from this directory with
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.

**3. Carrier.** A1-A5, A7: symbolic over Q(i) and over Z[a,b,c,d]. A6, A8:
symbolic over Z[a,b,c,d] first, then an exhaustive integer sweep
a,b,c,d in [-4,4], 6561 matrices, as an independent witness.

**4. Systematics.** Single platform this session (Linux x86_64,
CPython 3.11.15). One leg, therefore computation-grade rows stay at most
candidate-C; symbolic results carry candidate-T on the proof, not on the
sweep. Two byte-identical runs required; empty stderr required.

**5. Failure threshold.** The audit FIRES against the verdict if any of
A1-A6 is false as stated, or if A8 produces a counterexample. The audit
fires against the verdict's CLAIM OF PROGRESS, separately, if A7 shows
`H^2 = I` and `||H||_F^2 = 2` are the same equation on the class in which
the verdict works, since in that case the verdict renames the open
obligation rather than discharging it.

**6. Action layer.** L1. No promotion. The output is a verdict document in
the incubation lane and, if A7 fires, a correction to the labelling of
the verdict's section 3, not to its arithmetic.

## Explicit falsifier

```text
The audit's own headline "PASS ON ARITHMETIC / RENAMED, NOT CLOSED" is
falsified by exhibiting a 2x2 traceless hermitian H over Q(i) with
H^2 = I and Tr(H^2) != 2, or with Tr(H^2) = 2 and H^2 != I.
Either exhibit converts the verdict's sharpness step into an independent
condition and the headline is wrong.
```

Frozen before first execution. No computation has been run on any of
A1-A8 at the time of this freeze.
