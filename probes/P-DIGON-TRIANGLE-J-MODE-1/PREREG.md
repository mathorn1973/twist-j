# P-DIGON-TRIANGLE-J-MODE-1 preregistration

Status: PREREGISTERED CANDIDATE; FIRST FORMAL RUN PENDING REMOTE PIN READBACK

This document freezes one proof-first public probe. It contains no formal
gate output and earns no scientific status. Formal execution is forbidden
until this exact revision and `verify.py` are committed, pushed, and read
back as one immutable preregistration pin.

## Public identity and action layer

```text
program:          FIELD
probe:            P-DIGON-TRIANGLE-J-MODE-1
public lock:      issue 1732
owner:            A. M. Thorn
branch:           probe/P-DIGON-TRIANGLE-J-MODE-1
path:             probes/P-DIGON-TRIANGLE-J-MODE-1/
action layer:     L1 (exact algebra of one displayed integer cell); no lift
scientific state: candidate-T by the one-line proof below; the verifier
                  audits the exact identities; no physical selection claimed
```

Authority base is Public Canon v104, tag `canon-v104`, content commit
`4a50e527d20018839f006ed312454b710e6486b4`, Canon SHA-256
`c8d0cfadb44cf882af9f8ac303ba558b232663451d634d99467ce6d2c4a6814d`,
Canon byte count 1262204, main `e6240e26`, `canon/SHA256SUMS` 5 of 5 OK,
verified by fetch-and-hash this session. The probe earns at most public
status `T` by the proof frozen below; `verify.py` is an exact audit of the
finite identities, not the source of the theorem. The two-architecture
gate is the required GitHub x86_64 and aarch64 checks plus the local
record; no prior run is carried in as the public pin.

## Frozen preregistration body

```text
CANDIDATE:  P-DIGON-TRIANGLE-J-MODE-1 (incubation id C-DIGON-TRIANGLE-J-MODE-1)
SESSION:    digon-triangle-j-mode-2026-10-23; this document claims it; no
            other session owns the mode reading of this cell
DIRECTIVE:  owner, 2026-10-23: "push do repo jako PR pred slozenim do canonu"
TARGET:     public line. This probe carries no authority until public validation.
LAYER:      L1.
STATUS:     candidate-T. Expected honest outcome, stated up front: every
            identity T1 to T7 holds exactly; the verifier confirms. If any
            fails, that is the report and the probe is archived as F.
```

## 0. Currency and collisions

Registered rows touched by content, none a dependency of the proof:

```text
FIELD-FIVE-CELL-SHEAR-COMPARISON [T]  the five unweighted cells with Grams
    (2), (3), [[2,1],[1,2]], [[2,1],[1,3]], [[3,1],[1,3]] have active orders
    4, 3, 6, 5, infinite; orientation reversals give integral conjugacies;
    the row supplies no unique order-five selection. This probe inherits
    those orders and adds nothing to them. It adds the mode identity below,
    the hypotenuse-2 identity, the reason the form is 1 + mu^2, and the
    cells with a one-edge face, and it claims no selection either.
FIELD-SHEAR-ENERGY-BOUNDARY [T]       the electric-first shear, its
    conserved form, and the two-triangle Jordan block (the wall).
J-MODULUS-CHORD [T], J-TORAL-ENTROPY [T]   |J|^2 = 2 - phi and the two
    place-moduli phi, 1/phi; here they appear as amplitude ratios.
PHOTON-TEMPORAL-CHARACTERISTIC [T]    the dispersion form 4 sin^2(omega/2);
    the same form appears as lambda = |1 - mu|^2 here; no identification of
    this cell with the D3 carrier is claimed.
KAHLER-CAPACITY [T], GRAVITY-BRIDGE-LAW [D]   phi^2 and sqrt(3 - phi) appear
    there and here; this probe derives neither (4 pi)^3 nor 2^5 and leaves
    both rows unchanged.
```

Work in flight, credited, not a dependency: the unmerged notes
`C-FIELD-CYCLOTOMIC-WINDOW-N` and `C-FIELD-CYCLOTOMIC-WINDOW-AUDIT-N`
(issue 1301, pull request 1304) prove the universal window theorem and
identify the active lattice of this cell integrally with Z[zeta_5], with
I + A^2 identified with 1 + zeta_5^2. The present probe does not use the
window theorem; its census (T6) uses only the explicit eigenvalue condition
on the Gram matrix. Its mode identity is the per-mode form of that
identification together with the Gram eigenvector ratio, which is what
turns I + A^2 into a polar form. The collision scan (open issues, remote
heads, `probes/`, registry) found no other owner of this statement.

## 1. Object

```text
edges     e1, e2, e3, e4
faces     f1 = digon    = +e1 +e2
          f2 = triangle = -e2 +e3 +e4          (e2 is the shared edge)
C         4 x 2 incidence, columns f1, f2:  [[1,0],[1,-1],[0,1],[0,1]]
G         C^T C = [[2,-1],[-1,3]]            charpoly x^2 - 5x + 5
step      (E, M) in Z^4 x Z^2:  E' = E + C M,  M' = M - C^T E'
          as a 6 x 6 integer matrix T = [[I, C],[-C^T, I - G]]
```

Notation: zeta = zeta_5, J = 1 + zeta^2, sigma_k(J) = 1 + zeta^(2k) for
k = 1, 2, 3, 4, phi = -zeta^2 - zeta^3, 1/phi = phi - 1, s^2 = 3 - phi =
|1 - zeta|^2. All equalities are in Q(zeta_5) = Q[x]/(x^4+x^3+x^2+x+1).
This is the cell of FIELD-FIVE-CELL-SHEAR-COMPARISON with Gram
[[2,1],[1,3]] after the face reversal that row records as integrally
conjugate; T7 below covers both signs.

## 2. Claim under test

```text
T1  charpoly(T) = (x - 1)^2 Phi_5(x);  T^5 = I;  T != I.

T2  for each k in {1,2,3,4}, mu = zeta^k, lambda_k = 2 - mu - mu^-1 = |1-mu|^2:
    G (1, r_k)^T = lambda_k (1, r_k)^T with r_k = 2 - lambda_k = mu + mu^-1,
    and v = (C M / (mu - 1), M) with M = (1, r_k) satisfies T v = mu v.
    M = (digon amplitude, triangle amplitude); r_k = triangle / digon.

T3  r_k mu = 1 + mu^2 = sigma_k(J).
    k = 1:  r = 1/phi = |J|,  mu = zeta,     r mu = J
    k = 2:  r = -phi,         mu = zeta^2,   r mu = sigma_2(J)
    k = 3:  r = -phi,         mu = zeta^3,   r mu = sigma_3(J)
    k = 4:  r = 1/phi,        mu = zeta^4,   r mu = sigma_4(J) = Jbar
    Read: the polar form of J is the cell. Modulus = amplitude ratio
    triangle/digon, argument = mode frequency.

T4  lambda_k + 1 / r_k^2 = 4 for every k.
    k = 1:  (3 - phi) + phi^2 = 4      legs s and phi, hypotenuse 2 (36/54/90)
    k = 2:  (2 + phi) + phi^-2 = 4     legs sqrt(2+phi) and 1/phi   (18/72/90)
    The leg 1/r_k is the ratio digon/triangle; the leg sqrt(lambda_k) is
    |1 - mu|, the dispersion 4 sin^2(omega/2) at omega = 2 pi k/5.

T5  the digon is the reason for the form 1 + mu^2. For a two-face cell with
    Gram [[k1,-1],[-1,k2]] and reference face f1 of k1 edges,
    r = k1 - lambda, hence r mu = (k1 - 2) mu + 1 + mu^2. The form 1 + mu^2
    holds for every mode iff k1 = 2. With a triangle as reference face the
    form is 1 + mu + mu^2.

T6  census of two-face single-shared-edge Gram cells (k1, k2 >= 1,
    off-diagonal -1) inside the window "all eigenvalues of G in [0, 4)":
    lambda_max >= max(k1, k2) (Rayleigh quotient on a face vector) forces
    k1, k2 <= 4, and exhaustively
      (1,1) degenerate (lambda = 0)       (1,2) modes of order 10
      (1,3) modes of order 8              (2,2) modes of order 3 and 6
      (2,3) modes of order 5              (3,3) lambda = 4: the wall, outside
      every other pair: outside.
    Within this finite family (2,3) is the only cell with modes of order 5.
    This is a census fact about Gram matrices and asserts no physical or
    native selection, in agreement with FIELD-FIVE-CELL-SHEAR-COMPARISON.
    (1,2), with the digon as reference face, has charpoly Phi_10 (4 x 4, no
    static mode) and reads as the conjugates of J with mu a primitive tenth
    root of unity (angles 36 and 108 degrees and their negatives).

T7  orientation: with the shared edge taken with the same sign in both faces
    (off-diagonal +1) every r_k changes sign and r_k mu = -sigma_k(J).
    The Galois orbit of J is reached up to the common sign of the shared
    edge.
```

## 3. Proof (frozen; the verifier audits it)

T2, T3. For an eigenvalue mu of T with |mu| = 1, E' = mu E gives
C M = (mu - 1) E and M' = mu M gives C^T E' = (1 - mu) M, hence
G M = (mu - 1)(1 - mu)/mu M = (2 - mu - mu^-1) M = |1 - mu|^2 M. So M is a
G-eigenvector with eigenvalue lambda = |1 - mu|^2, and E = C M/(mu - 1).
The first row of G gives (2 - lambda) M_1 - M_2 = 0, so r = M_2/M_1 =
2 - lambda = mu + mu^-1, and r mu = mu^2 + 1 = sigma_k(J) for mu = zeta^k.
T1 follows: the four roots mu of Phi_5 give lambda in {3 - phi, 2 + phi},
the two eigenvalues of G, and the static part ker C^T has dimension 2 with
eigenvalue 1. T4: lambda + r^-2 = 4 is the cubic r^3 + 2 r^2 - 1 = 0 in
r = 2 - lambda, i.e. (r + 1)(r^2 + r - 1) = 0, satisfied by r = 1/phi and
r = -phi. T5: with k1 edges in the reference face the first row gives
r = k1 - lambda. T6: the Rayleigh bound and the finite list. T7: changing
the sign of the shared edge changes the sign of the off-diagonal entry and
of r.

## 4. The six fields

```text
equation     T1 to T7 above.
code         verify.py in this directory: standard library, Fractions in
             Q(zeta_5), Faddeev-LeVerrier characteristic polynomial, exact
             inverse by the norm, no float, no subprocess, no file access,
             deterministic, under 2 seconds.
carrier      no external data; the cell is displayed in section 1.
systematics  (a) disclosure: the statement was derived and checked in the
             author's incubation lane before this pin, with a verifier of
             SHA-256 ebfa53264d519d673ba11829a9151efb38b7fbe6d0ae5f4b4c08f53f58431518
             and an independent F_p breaker of SHA-256
             9be2a01438938671d734f10f5a92ee635a740587651c63011eb2b99fbae90847,
             both PASS there; this public pin is therefore confirmation-grade
             for the computation and proof-first for the status.
             (b) orientation convention as in section 1; T7 covers the other
             sign; reversing a whole face conjugates its modes.
             (c) the identity r mu = 1 + mu^2 is forced by the digon row; the
             claim is the exact identification and the census, not a
             coincidence.
             (d) L1 only; the words "observable" and "unobserved" do not
             occur in the claim.
threshold    any assertion in T1 to T7 failing in verify.py: the probe is F,
             archived, no threshold moved. A reproduction that is not
             byte-identical across the required architectures: the
             computation gate fails and the status stays at most C.
layer        L1. No lift.
```

## 5. What is not claimed

No selection of this cell by the native dynamics or by J; no physical
reading of the digon or the triangle; no derivation of 2^5 in
GRAVITY-BRIDGE-LAW or (4 pi)^3 in KAHLER-CAPACITY; no identification with
the D3 photon carrier; no change to any normative file. Registration, if
any, is a separate sealed fold.
