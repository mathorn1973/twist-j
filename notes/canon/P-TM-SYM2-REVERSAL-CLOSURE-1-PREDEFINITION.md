# P-TM-SYM2-REVERSAL-CLOSURE-1 predefinition

```text
DEFINITION NOTE / NON-CANONICAL / NO EVALUATION OUTPUT / NO PROBE RUN
```

Status: theorem-grade predefinition of the reversal-closure probe on the
`TM-SYM2-MEASURE` lane. This note freezes the object, the action, the
transport question, and the route grammar. It evaluates nothing: no route
value, no translation value, no transport verdict, and no orbit count is
stated here. It changes no canon table and adopts no gauge. Target for
publication: `notes/canon/`, alongside the definition notes of the
semilinear antecedent, under a public definition issue and PR before the
formal lock.

## 1. Authority and antecedents

```text
Public Canon:  v16 ACTIVE (STATUS.md on public main is authority; re-read
               at pin time)
frozen basis:  the v16 S_TM definition surface
               (notes/canon/P-TM-SYM2-MEASURE-1-OWNER-DEFINITION.md and
               its two merged inputs)
antecedent 1:  P-TM-SYM2-MEASURE-1, NEGATIVE/N2: the complete selector
               class has 48 members; the frozen projective-linear gauge
               has order 12 and acts freely with four orbits of 12
               (complete partition published in EXPECTED.txt)
antecedent 2:  P-TM-SYM2-SEMILINEAR-GAUGE-1, PASS/SEMILINEAR-DOUBLE:
               the projective-semilinear realization image Gamma_sl has
               order 24, coset character (1,1), two selector orbits of
               24, residual invariant chi_Q chi_F
```

Both antecedents are consumed only through their pinned public
transcripts, as byte-identical snapshots inside the probe pin. Neither
old verifier is imported, invoked, or replayed.

## 2. The object: drive-word reversal

The frozen carrier is the six-word window language

```text
W3 = {001, 010, 011, 100, 101, 110},   N(w) = bitwise complement.
```

DEFINITION (reversal). `R(abc) = cba` on three-bit words.

The following facts are definitional lemmas, provable by finite
inspection and by the registered doubling
`theta_(2m) = theta_m, theta_(2m+1) = 1 - theta_m`; the probe verifier
re-proves each as a structural certificate:

```text
L1  R maps W3 bijectively to W3 and is an involution.
L2  R commutes with N (complement of reversal = reversal of complement).
L3  The child maps E_even(a,b,c) = (1-a, b, 1-b) and
    E_odd(a,b,c) = (b, 1-b, c) satisfy, for every counter m >= 1,
    q(2m) = E_even(q(m)) and q(2m+1) = E_odd(q(m)) on centered windows
    q(n) = (theta_(n-1), theta_n, theta_(n+1)); they generate the frozen
    public transfer of the measure PREREG (001 -> 101 + 011 and the five
    siblings).
L4  R o E_even = N o E_odd o R exactly on W3: reversal intertwines the
    doubling children up to negation. Reversal is drive structure, not a
    relabeling.
```

Registered anchor (interpretation only, no proof weight): the public row
`TWO-PLACE-PHYSICS [D]` reads T from the Thue-Morse reversal. The window
at counter n is (theta_(n-1), theta_n, theta_(n+1)); reversal swaps the
past and future neighbor of the tick.

## 3. The action and the uniformity lemma

The frozen class (antecedent 1, unchanged) is

```text
Sel_class = {s : W3 -> Lines, N-to-sigma_line equivariant bijections},
|Sel_class| = 48,
```

with the six registered lines, `sigma_line = (v1 v2)(v3 v4)(v5 v6)`, the
oriented pairs `D0 = (001,110) -> E0 = (v1,v2)`,
`D1 = (010,101) -> E1 = (v3,v4)`, `D2 = (011,100) -> E2 = (v5,v6)`, and
the two frozen characters of the semilinear antecedent on the
centralizer `W = Cent(sigma_line) = C2 wr S3` (order 48):
`chi_Q = sgn` of the induced pair permutation, `chi_F` = flip parity.
Selector fibers `(Q, F)` are assigned through the free torsor structure;
the four fibers are exactly the four published orbit blocks.

DEFINITION (candidate equivalence enlargement). For a window-side
bijection `b` of W3 commuting with N, precomposition `s -> s o b` maps
`Sel_class` to itself (equivariance is preserved because b commutes with
N). The three structural involutions of the lane are `N`, `R`, and
`N o R`.

LEMMA (well-definedness and uniformity; proved in the pin's structural
certificates, values not evaluated here). Precomposition by a fixed `b`
translates the selector fiber `(Q, F)` by a constant element of
`F_2 x F_2` independent of the selector, namely the character pair of
the window-side wreath element `b` (sign of its induced pair
permutation, parity of its flips). Consequently the fiber translations
of `N`, `R`, and `N o R` are three well-defined constants `t_N`, `t_R`,
`t_NR` with `t_NR = t_N + t_R`. One identity is structural and exact:
`s o N = sigma_line o s` for every class member, so `t_N` is the
translation realized by `sigma_line` postcomposition. No value of `t_N`,
`t_R`, or `t_NR` is stated in this note.

DEFINITION (transport). For a class member `s` and window symmetry `b`,
the transport is the line permutation `s o b o s^(-1)`. It lies in `W`
(it commutes with `sigma_line` by L2 and equivariance). Its realizability
by a projective-linear (`e = 0`) or projective-semilinear (`e = 1`)
transformation over `Q(sqrt5)` is decided by the same incidence problem
the semilinear antecedent scanned exhaustively; the probe re-decides all
96 cases by two independent internal methods (projective four-line frame
construction, and full RREF nullspace with a determinant-polynomial grid
witness) with mandatory per-case agreement.

## 4. The question and the two routes

The open edge after antecedent 2 is the residual twofold selector
ambiguity, invariant `chi_Q chi_F`. The probe decides exactly one
question:

```text
Does precomposition by the drive reversal R toggle the residual
invariant chi_Q chi_F, or preserve it?
```

equivalently, whether the equivalence generated by `Gamma_sl`
postcomposition together with `R` precomposition has one orbit (48) or
two orbits (24, 24) on the class. The route is derived, not selected, by
the frozen table on the computed translation `t_R`:

```text
t_R in {(1,0), (0,1)}  ->  ROUTE: REVERSAL-TOGGLE
                           (consistency: one extended orbit of 48)
t_R in {(0,0), (1,1)}  ->  ROUTE: REVERSAL-SILENT
                           (consistency: two extended orbits of 24)
```

Both routes are first-class scientific results with exit zero. A
consistency mismatch between the translation and the orbit count is
STOP, not science. The transcript additionally carries, as computed
fields, the translations and transport verdicts of all three structural
involutions; no expected value of any field is embedded in the pin.

## 5. Scope firewall

```text
No outcome adopts R, N, or N o R as gauge, edits any canon table,
changes the published N2 or SEMILINEAR-DOUBLE records, selects a
selector, claims microscopic canonicality, derives physical probability
or a Born halving, or supplies an L5-to-L6 bridge. Whether a positive
toggle is quotiented (reading-orientation identification) or carried as
a physical datum is an owner decision on a later, separately reviewed
fold; this probe supplies the exact material to both options and
prejudges neither. Field enlargement beyond Q(sqrt5) (in particular
Q(zeta_5) semilinearity) is out of scope. The window-side negation is
drive structure per the frozen S_TM; nothing here turns it into gauge.
```

## 6. Provenance disclosure

Two incubation-lane candidates on this edge exist in the project space
and are disclosed as provenance only, not evidence: 
`C-TM-SYM2-REVERSAL-CLOSURE-1` (this question; freeze, verifier,
independent breaker, run record, 2026-07-23) and
`C-TM-SYM2-TWOFOLD-NOGO-1` (independent parallel session, same day: the
geometric irreducibility of the residual twofold including a
field-enlargement robustness check, and the selector-invariance of the
physical measure). The route of this probe is derivable by hand from
public data and was derived in the incubation lane; this pin therefore
claims validation, not blind discovery, and deliberately embeds no
route value. An incubation twin of the verifier bytes was executed in
the incubation lane as an engineering integrity check; the formal run
under this probe id remains the single authorized execution.
