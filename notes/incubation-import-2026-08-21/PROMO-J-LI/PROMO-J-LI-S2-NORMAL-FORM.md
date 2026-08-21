# PROMO-J-LI-S2-NORMAL-FORM. Fold hand-off (Lane B1)

```
CANDIDATE:     notes/C-LI-S2-RELATIVE-DETERMINANT-1 (parent) plus the finalized
               skeleton verifier below
TARGET:        public mathorn1973/twist-j, sealed fold v6 -> v7
PROPOSED ROWS: J-LI-S2-NORMAL-FORM [T as equivalence]
               J-LI-S2-SPECTRAL-RIGIDITY [T]
SCOPE:         operator-theoretic reformulation of Li's criterion; imports labeled.
AUTHORITY:     none (incubation). Public two-architecture validation required.
RH:            O.
```

## 1. Claim (exact, equivalence)

```
RH  iff  there is a separable real Hilbert space and an orthogonal O with
         I - O Hilbert-Schmidt and lambda_n = (1/2) || I - O^n ||_S2^2 for all n >= 1.
```

Under RH, O_xi = direct_sum_{gamma>0} R(theta_gamma)^{m_gamma}, with
e^{i theta_gamma} = (gamma + i/2)/(gamma - i/2) the Cayley image of the zero
ordinate. One block gives || I - R(theta_gamma) ||_S2^2 = 2/(gamma^2 + 1/4).

Spectral rigidity (J-LI-S2-SPECTRAL-RIGIDITY): every exact S2 witness has the
SAME non-identity eigenangles and multiplicities as O_xi; the only free datum is
dim ker(I - O). The second differences of the ladder reproduce the symmetrized
atomic measure sigma_xi exactly (t_n = integral z^n d sigma_xi), with total mass
t_0 = 2 lambda_1. Consequence: constructing the realization is constructing the
zeros; there is no parameter fitting.

## 2. Falsifier

An exact S2 witness whose non-identity spectrum differs from the Cayley image of
the zeros, or a ladder second-difference that misses the sigma_xi moment. For the
finite skeleton: any pinned gate below failing on re-run.

## 3. Verifier and pins (non-formal incubation run, single architecture)

```
file            verify_s2_normal_form.py  (project: claude/verify_s2_normal_form.py)
file sha256     ea2fd130ef0d54d341457438852fae705d684a85fd36801f2b373388517520fb  (6496 bytes)
stdout sha256   2b67278ac86604bdbca0af30941742cdd7d107827badd51057683755c9fe5fda  (930 bytes, 11 lines)
environment     LC_ALL=C LANG=C ... TZ=UTC; Linux x86_64, Python 3.11.15; 7/7 PASS
gates           S1 one-block defect 2/(gamma^2+1/4)
                S2 block Li formula lambda_n = (1/2)||I-O^n||_S2^2
                S3 second differences = symmetrized moments integral z^n d sigma_xi
                S3b total mass sigma(T) = t_0 = 2 lambda_1
                S4a rigidity: identity blocks invisible (only ker(I-O) free)
                S4b rigidity: distinct nonidentity atoms give a distinct ladder
                S4c rigidity: nonidentity atom cosines forced by the moments (Prony)
```

Imports (frozen in the public PREREG): Li's criterion; the spectral theorem for
normal compact perturbations of the identity; Fourier uniqueness for finite
measures on the circle.

## 4. Scope caution (honest, guards G6)

These are equivalences, that is reformulations of Li's criterion in operator
language with imports labeled. They are genuine T rows and useful public
scaffold, but they are NOT an advance on RH and must be registered as reductions,
not progress. The novelty they legitimately carry is the J-native realization
TARGET (rigidity pinning it to the zeros), not a new proof of Li. Guard against
the F pattern RENAMED-STANDARD-AS-NEW-PROOF: the summary label is never stronger
than "equivalence, imports labeled".

## 5. Dependency edges

```
parents   C-LI-COCYCLE-1 (cocycle normal form, the T_1/T_2 gates); C-LI-TORAL-
          HAAR-1 (forced symmetrized measure sigma_xi); the carrier no-go.
siblings  the complex positive-Fredholm form and the G0-G8 wall live in the same
          parent candidate and are NOT part of this fold (they stay [O]).
```

## 6. Exact fold edits

REGISTRY.tsv, add (tab-separated):

```
J-LI-S2-NORMAL-FORM   T   RH iff there is an orthogonal O with I-O Hilbert-Schmidt and lambda_n = (1/2)||I-O^n||_S2^2 for all n; imports Li's criterion and the spectral theorem   <RH/Li lane>   probes/P-J-LI-S2-NORMAL-FORM-1
J-LI-S2-SPECTRAL-RIGIDITY   T   every exact S2 witness shares the nonidentity eigenangles and multiplicities of the Cayley-transformed zeta zeros; only dim ker(I-O) is free; the realization target is a J-native construction of the zeros   <RH/Li lane>   probes/P-J-LI-S2-NORMAL-FORM-1
```

CANON.md: add both under the RH/Li lane heading, with the "equivalence, imports
labeled" scope note. CHANGELOG.md, HISTORY.tsv: one sealed entry.
STATUS_COUNTS.tsv: T +2. SHA256SUMS: recomputed.

## 7. Non-claims

Equivalences only. RH [O]. The realization
(J-LI-S2-RELATIVE-DETERMINANT-REALIZATION) [O]. Every finite gate is a
necessary-condition calibration with zero evidence for RH by itself.
