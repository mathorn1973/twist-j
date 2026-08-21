# AUDIT of the [PUBLIC] synthesis "most stoji, ale ne cely", 2026-08-21

```text
STATUS      INTERNAL, NON-CANONICAL audit record. No authority, no repo edit,
            no registry motion. Independent second pass on the delivered
            synthesis of the QDD pure-record bridge.
SUBJECT     the posted synthesis claiming: B_W = R_cyc o iota_B0 |_W exists
            and is projectively faithful [candidate-T]; the current finite
            D_matter leg cannot carry the rational L4 source [candidate-T];
            Gate A (algebraic map) ready for a fold; Gate B (D_matter
            ownership) [O] pending an internal eta_post; no public
            GATE-L4-L1-QDD-PURE-RECORD exists.
BASIS       Public Canon v59 ACTIVE, gate run this session from a fresh clone:
            HEAD 47fa9ddd8db5e9fdbbd4440f29107ca298898350, STATE ACTIVE,
            AUTHORITY mathorn1973/twist-j main, TAG canon-v59 and
            CONTENT_COMMIT 5da6b883 ancestors of main, canon/SHA256SUMS
            5 of 5 OK, CANON_SHA256 7fdea700..87641, 314310 bytes.
METHOD      fresh code path (own Fraction kernel, own cyclotomic Q(zeta_5)
            arithmetic, nothing imported from any probe directory), 17 exact
            gates, plus replay of both sealed public verifiers from repo root.
VERDICT     AUDIT-PASS 17 of 17, zero findings in the mathematics. One
            currency finding in the prose: the synthesis is written against
            probe #498 only and does not register the already merged probe
            #504, which reframes and partially answers its closing question.
```

## 1. Independent verification, 17 of 17 PASS

audit_pure_record_synthesis.py, sha256
234a98572b158b8dbc6decf05bb1df7abb57cd11265f3b9f44c4e4bbf2e46ced,
stdout sha256 b53a1112dafe2e22615699667b745beffc9282b92221889bef7efc998d9140a0
(976 bytes, exit 0, empty stderr), Linux x86_64 CPython 3.11.15,
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC.

```text
A01  G, G^-1 = I + 11^T, E_low, E_high projector algebra          PASS
A02  W-basis b_i = e_i - e_3 has Gram H = [[2,1,1],[1,2,1],[1,1,2]] PASS
A03  O_* is an H-orthogonal involution                            PASS
A04  A = E_high D_J E_high preserves W, Tr(A) = -3/4              PASS
A05  x_L = O_*Av = (1,1,1,-3)/4, x_R = AO_*v = (1,1,-3,1)/4,
     v = (0,0,1,-1), reconstructed from scratch                   PASS
A06  m(x_L) = m(x_R) = 3/4                                        PASS
A07  branch weights (0, 3/4), normalized (0, 1), via lambda_B     PASS
A08  rho_L, rho_R equal the stated matrices and differ            PASS
A09  x_L, x_R outside V_eff (quarters), so no K_QDD preimage      PASS
A10  rho^2 = rho, rho^sharp = rho, rank 1, Tr rho = 1,
     vv^T = m rho G^-1, on a 1295-vector sweep incl. halves       PASS
A11  record fibres are exactly sign pairs on that sweep           PASS
A12  G positive definite on the sweep lattice                     PASS
A13  O_* commutes with S = A^sharp A, so scalar blindness is
     general, not a coincidence of the witness                    PASS
A14  m(O_*Aw) = m(AO_*w) on a 125-point coordinate sweep          PASS
A15  [O_*, A] nonzero with rank exactly 2                         PASS
A16  R_cyc leg from fresh cyclotomic arithmetic:
     <w,w>_tr = m(v) and MATRIX_B0(T_w) = vv^T G on the full
     624-vector balanced sweep                                    PASS
A17  witnesses: R_cyc totals 3/4 and densities equal rho_L, rho_R PASS
```

The typový lamač is therefore CONFIRMED by an independent construction: the
same reflection, reconstructed only from the H-Gram and the public
definitions, produces the same ordered outputs, equal scalar records, and
distinct densities, and both outputs fall outside V_eff, so the current
finite decoder leg is not typed on them.

## 2. Public-line claims of the synthesis, checked at head

```text
"sonda #498"                    CORRECT. P-QDD-AFFINE-PURE-RECORD-BRIDGE-1,
                                merge 1b288cb. RESULT status: PROVED AND
                                AUDITED IN THE FROZEN CLASS / PUBLIC REPLAY
                                PENDING / CANON UNCHANGED. Candidate rows
                                only, no registry motion. The synthesis
                                label [candidate-T] does not inflate this.
gate table                      CORRECT. canon/GATES.tsv has 11 gates; none
                                is GATE-L4-L1-* and none owns a QDD
                                pure-record bridge.
DEF-QDD dependencies            ALL PRESENT in CANON.md: AMPLITUDE-B0,
                                TRACE-PAIRING, MATTER-RECORD, DIRECT-WRITE,
                                GRAM (G = I - (1/5)11^T, G^-1 = I + 11^T).
QDD-U-INDUCED-CHANNEL           PRESENT as [T]; the 900-pair null is
                                QDD-U-INDUCED-FINITE-NONSELECTION [C].
                                Both quoted at their labels, no inflation.
"repo nezmenen timto krokem"    CONSISTENT with head.
```

Verifier replay, this session, from repository root under the frozen
environment, Linux x86_64 CPython 3.11.15:

```text
P-QDD-AFFINE-PURE-RECORD-BRIDGE-1/verify.py   exit 0, empty stderr,
    stdout BYTE-IDENTICAL to EXPECTED.txt
P-QDD-PURE-RECORD-TYPED-BRIDGE-1/verify.py    exit 0, empty stderr,
    stdout BYTE-IDENTICAL to EXPECTED.txt
```

Both RUN.md legs are x86_64, and this replay leg is also x86_64, so this
adds reproduction evidence only; it does not discharge the two-architecture
requirement.

## 3. The one finding: the closing question is already moved by #504

The synthesis ends with

```text
existuje cilove nezavisla interni mapa
eta_post : Dom_post subset K -> W(Q) ?
```

as the next decisive attack, and cites only probe #498. But
P-QDD-PURE-RECORD-TYPED-BRIDGE-1 (PR #504, merge 47fa9dd, the current head)
is already sealed and proves, inside its frozen classes:

```text
1  Static encodings of the full sign-class source into K exist (two
   disjoint injective conventions) and decode back to b_alg, but no public
   equivalence identifies them: the decoder type does not select a static
   typed bridge. [nonselection]
2  The faithful motor-congruent bridge class into the pointed U-orbit tail
   is EMPTY: eta(D_J[v]) = sigma^r eta([v]) with nonnegative lags forces
   all lags zero and a projective fixed vector of D_J, which does not
   exist. [no-go]
3  What remains constructible without new mathematics is a direct
   read-only L4 source port through the public global helper; adopting it
   is an architecture and gate decision, not a missing calculation.
```

Direction matters and the synthesis is not contradicted: #504's no-go
concerns embeddings source -> K, while eta_post is a read-out K -> W(Q).
The question stands. But the attack surface has changed shape: #504 already
formalizes the Gate B checklist as the public boundary (its section 6 names
the same missing objects, including the absent GATE-L4-L1-QDD-PURE-RECORD
by name), kills the congruent-embedding route, and names the read-only
source port as the surviving constructive option. Any next move on eta_post
should be preregistered against #504's boundary, not against #498 alone.

## 4. Status after this audit

```text
QDD-L4-PURE-RECORD-MAP            [candidate-T] CONFIRMED, independent pass
QDD-CURRENT-DMATTER-NONFACTOR     [candidate-T] CONFIRMED, independent pass
GATE-L4-L1-QDD-PURE-RECORD-MAP    proposal consistent with head; ABSENT
                                  from GATES.tsv as claimed
GATE-...-DMATTER-OWNERSHIP        [O] as claimed; sharpened by #504:
                                  congruent-embedding route closed,
                                  read-only source port open, adoption is
                                  an architecture decision
O1, O2                            open, untouched
SAMPLING                          NOT PROVIDED
```

Files: audit_pure_record_synthesis.py and .stdout.txt beside this record.
Repo unchanged by this audit.
