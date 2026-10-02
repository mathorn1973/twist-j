# PREREG: C-NATIVE-FIBRE-PENTIT-WIGNER-N

**NON-CANONICAL. Candidate with no authority. Incubation lane.**
Frozen 2026-10-02, before the first execution of the verifier named in section 4.
Target line on promotion: public, `mathorn1973/twist-j`, as a note under
`notes/C-NATIVE-FIBRE-PENTIT-WIGNER-N/`. Action layer: L1 only.

Scope fixed by the owner on 2026-10-02: this candidate is an **exact
representation and a bounded prohibition of counting**. It is **not** a passage
through Gate 0 of `C-OCCURRENCE-CYCLE-COUNT-N`. Whatever Parts A and B return,
the disposition `STOP_APPLICABILITY / H_NOT_TESTED` of that note stands unless
Part C exhibits every input its contract requires.

## 0. Authority and currency

```text
Public Canon      v97, STATE ACTIVE, AUTHORITY mathorn1973/twist-j main
TAG               canon-v97 (annotated), peeled 738e0421bd15aaea5bb6ef2a56f1cab752d44de5
main              738e0421bd15aaea5bb6ef2a56f1cab752d44de5
CONTENT_COMMIT    82ecf0aac0ee79c947000968e71573d4c65d386d
CANON_SHA256      257f83a386aad7d309f7017bd719b6212e3cffea60e4986caa5169d6543f108d
CANON_BYTES       897762
canon/SHA256SUMS  5 of 5 OK
generator source  reproduce/census/verify.py
                  sha256 1df13ba2218acaa9cf48dab2480e6472b107691aac868618dc7f91d511718a5c
generator text    canon/CANON.md lines 580 to 584; selector line 448
compared note     notes/C-OCCURRENCE-CYCLE-COUNT-N/PREREG.md
                  sha256 524fca08604268cbada9210c0ae8e399532db8a9d48d1aa443f4b24cb548c15b
```

Only the public line was read. Collision check at freeze: no note, probe or
branch named after PENTIT, WIGNER or NATIVE-FIBRE exists on the public remote.

Registered rows used as inputs, at their registered status and scope:
`QDD-U-INDUCED-CHANNEL [T]`, `KERNEL-Z6-SYNCHRONIZATION [T]`,
`U-NATIVE-COMMON-READY-SOURCE-RETENTION [T]`, `U-NATIVE-READER-STREAM-SPECTRA [T]`.

## 1. Carrier, conventions, reading premise

Carrier. `X = F_5^6` with `x = (p1,p4,p1p,p4p,q,r)`, generators `a,b,c,d,e`
exactly as in the Canon text and the pinned source file. `kappa = p1+p4+p1p+p4p`,
fibre `f(x) = (q,r)`, `z = kappa+q+r`. Origin-zero clock `theta_n = s_2(n) mod 2`.
Selected step `U(n,x) = (n+1, g_sigma(x))`, `sigma = z(x) + 2 theta_n mod 5`,
index 0 to 4 for `a` to `e`.

Pentit. `zeta = zeta_5`. On `C^5` with basis `|j>`, `j in F_5`:

$$
A_{q,r}\,|j\rangle = \zeta^{\,2r(q-j)}\,|2q-j\rangle ,\qquad
D_{q,r}\,|k\rangle = \tau^{\,qr}\,\zeta^{\,rk}\,|k+q\rangle ,\quad \tau=\zeta^{3}.
$$

Wigner function of a density operator and negativity:

$$
W_\rho(u)=\tfrac15\operatorname{Tr}(\rho A_u),\qquad
\mathcal N(\rho)=\sum_{W_\rho(u)<0}|W_\rho(u)| .
$$

Lines. The 30 affine lines of `F_5^2` in 6 parallel classes, directions `(0,1)`
and `(1,m)`, `m in F_5`. Line operator:

$$
\Pi_L=\tfrac15\sum_{u\in L}A_u .
$$

Reading premise, declared and not a Canon row. The QDD real four-vector
`v=(v1,v2,v3,v4)`, `v_i = ell(p_i)`, `ell=(0,1,2,-2,-1)`, is read in the real
sum-zero sector of the pentit, coordinate 0 carrying no source:

$$
\tilde v=(0,v_1,v_2,v_3,v_4)-\tfrac{s}{5}(1,1,1,1,1),\qquad
s=\sum_i v_i,\quad Q=\sum_i v_i^2 .
$$

The LOW direction is `l = (4,-1,-1,-1,-1)/sqrt(20)`. The 624 preparations are
the nonzero `p in F_5^4`. Census statements over the whole set do not depend on
where the empty coordinate sits or on the order of the four sources, because
the set is invariant under permutations of the sources and a cyclic relabeling
is a Weyl translation. A statement about one named preparation does depend on
this convention.

`sqrt5` denotes the positive root. Signs in `Q(sqrt5)` are decided exactly.

## 2. Target exposure, complete

Blindness is **not** claimed for the items below. They were seen before this
freeze. The run is a confirmation and audit of exposed targets; independence
comes from the second implementation in section 6, not from blindness.

1. Recon of this session, run before any freeze:
   script sha256 `55648d730c13eaaed832215dd70af4be1049584c874842e5608899d900a320aa`,
   stdout sha256 `3694834d1d7d4312f9b0e17c9c5d4f970c33975143e3093790ceb4f9345bdcaf`,
   12 of 12 checks. Exposed: the four centres; solution dimensions 3,3,1,1 for
   sign multipliers; maximal rank 2; three-dimensional common radical;
   involution, conjugation and sum identities of `A_u`; the line `q=0` for `|0>`;
   the five LOW Wigner values; LOW negativity `sqrt5/5`; negativity positive for
   all 624; minimum `(1+sqrt5)/10`; the overlap identity for all 624.
2. Earlier exploration of this session: image sizes 6250 and 9375 of the
   selected one-step map; reachable sizes 15625, 6250, 6250, 3125 on ticks
   0 to 3; exactly five preimages per synchronized state; bijectivity on the
   3125-state set for ticks 3 to 3999.
3. Owner review of 2026-10-02: the collision pair `000000`, `212110`; the order
   50 of the fibre group; the line intersection formula; the inversion formula;
   the general negativity statement through two lemmas of Gross (2007); the
   closed form of the LOW weight; the analytic LOW negativity with
   multiplicities 4 and 8; the candidate minimizer `v=(1,-1,0,0)`.
4. Hand derivations of this author before the freeze: the self-contained
   row-zero proof and the bound `sqrt5/20` (B3); the multiplier lemma (A4); the
   common-generator rule on synchronized ticks (A5.4).

Not exposed before the freeze, recorded as found with no target: the solution
dimensions for multipliers 2 and 3 as a computed fact; the Weyl eigenprojector
audit B1.3; the number of minimizers, the maximum, the number of distinct
values and the SHA-256 of the full negativity table.

## 3. Equations and claims

Each claim carries its own falsifier. A fired falsifier is archived with the
run. No threshold moves after the freeze.

### Part A. Geometry and representation

**A1.** Each generator is affine on `X`. The fibre image depends on the fibre
only. `a` is the identity on the fibre; `b,c,d,e` act as point reflections
`u -> 2 s_g - u` with centres `s_b=(0,0)`, `s_c=(3,0)`, `s_d=(3,3)`, `s_e=(1,3)`.
These are the four exceptional readies of `U-NATIVE-COMMON-READY-SOURCE-RETENTION`.
Falsifier: any state or any fibre point where the stated form fails.

**A2.** The four reflections generate exactly the 50 maps `u -> +-u + t`: all 25
translations and all 25 point reflections, no other linear part. Consequence
stated as scope: each of the six parallel classes is mapped to itself, so the
generated group changes no direction, and the full stabilizer class is not
thereby a class of natively available preparations or instruments.
Falsifier: generated order different from 50, or a linear part outside `+-1`.

**A3.** Over `Z[zeta_5]`, for all points `u,v,s`:

$$
A_u^2=I,\quad A_u^\ast=A_u,\quad \operatorname{Tr}A_u=1,\quad
\operatorname{Tr}(A_uA_v)=5\,\delta_{u,v},\quad
A_sA_uA_s=A_{2s-u},\quad \sum_uA_u=5I ,
$$

and `A_u = D_u Par D_u^{-1}`, `D_v A_u D_v^{-1} = A_{u+v}`. Hence conjugation by
`A_{s_g}` sends `A_u` to `A_{g(u)}` for `g in {b,c,d,e}`: conjugation realizes
the fibre reflection on phase-point indices. Falsifier: any failing identity.

**A4.** Let `L_g` be the linear part of `g`. An alternating form `omega` on
`F_5^6` with `L_g^T omega L_g = m_g omega` for `g in {a,b,c}` and `m_g in F_5^*`
(`d,e` have linear part `-I` and impose nothing) is nonzero only for
`(m_a,m_b,m_c) in {(1,1,1),(4,1,1),(1,4,4),(4,4,4)}`. The strictly invariant
forms are exactly

$$
\operatorname{span}\{\,d\kappa\wedge dq,\ d\kappa\wedge dr,\ dq\wedge dr\,\}.
$$

Every nonzero solution for every multiplier triple has rank 2, hence a
four-dimensional radical. The common radical of the strictly invariant family is

$$
\bigcap_\omega \operatorname{rad}\omega=\ker d\kappa\cap\ker dq\cap\ker dr ,
$$

of dimension 3. Consequently no nondegenerate alternating form on `F_5^6` is
preserved, even up to a multiplier, by these linear parts. Scope: this excludes
a symplectic three-pentit reading **of this invariant linear and affine
realization in these coordinates** and nothing wider.
Falsifier: a nonzero solution for any other triple, or any solution of rank 4 or 6.

**A5.** Boundary between generators, the selected step and an autonomous factor.
(i) `U(0,x0) = U(0,x1) = (1,x0)` for `x0=000000`, `x1=212110`: the two states
select `a` and `c`. (ii) For either driver bit the selected one-step map on `X`
is not injective; image sizes 6250 and 9375. (iii) After ticks 0,1,2 the 15625
starts occupy 3125 states, five preimages each. (iv) On every tick `n >= 3` all
origin-zero states select one common generator, determined by the clock alone:
`b` if `theta_(n-1) != theta_n`, `d` if both are 1, `e` if both are 0. (v) On
those ticks the selected step is a bijection of the current 3125-state set.
Stated limits: (iv) and (v) are clock-driven statements about the synchronized
regime. They are not a finite autonomous factor, not a permutation of `X`, and
not an event contract. "The generators are bijections" must not be read as
"the selected U is a bijection of points".
Falsifier: failure of the collision, of either image size, or one tick in the
audited range with two selectors, a selector off the rule, or a merge.

### Part B. Counting and its bounded prohibition

**B1.** Each `Pi_L` is a Hermitian idempotent of trace 1, an eigenprojector of
the Weyl operator of its own direction, and for all lines `L,M`

$$
\operatorname{Tr}(\Pi_L\Pi_M)=\frac{|L\cap M|}{5}\in\{0,\tfrac15,1\}.
$$

This is a spatial count: common points over points of the preparation. It is
**not** a statement about frequencies of completed trials along a trajectory.
Control stated in advance: under the identity dynamics the spatial count on a
line is `1/5` while every single trajectory stays at one point.
Falsifier: a line whose operator is not such a projector, or a pair with a
different trace.

**B2.** Uniqueness of point counting with line reading. If `mu` is a real
function on the 25 points with total 1 and `p(L) = sum_(u in L) mu(u)`, then

$$
\mu(u)=\frac15\Big(\sum_{L\ni u}p(L)-1\Big).
$$

For `p(L)=Tr(rho Pi_L)` this `mu` equals `W_rho`. Therefore a nonnegative
distribution on these 25 points that returns all 30 line probabilities by
plain membership exists if and only if `W_rho >= 0`.
Exact scope of the prohibition: these 25 points, this membership reading, all
30 lines. It does not exclude a larger carrier, another reading, a contextual
apparatus, or a model that reproduces only the LOW and HIGH tests.
Falsifier: a state in the audited set whose inversion differs from `W`.

**B3.** General negativity in the real sum-zero sector. For every nonzero real
`psi` with `sum_j psi_j = 0`, in any odd dimension `d`:

$$
\sum_{q}W_\psi(q,0)=0,\qquad W_\psi(\cdot,0)\not\equiv0,\qquad
\mathcal N(\psi)\ \ge\ \frac{1}{2\sqrt{d(d-1)}} ,
$$

so `W_psi` has a strictly negative entry in the row `r=0`. At `d=5` the bound is
`sqrt5/20`. With B2: no state of the declared reading admits nonnegative point
counting with line reading. Reality of the amplitudes is essential: the complex
sum-zero vector `(1,zeta,zeta^2,zeta^3,zeta^4)/sqrt5` is a line state.
Falsifier: a nonzero real sum-zero vector with `W >= 0`; in the audit, one of
the 624 preparations with a nonnegative row zero or negativity below `sqrt5/20`.

**B4.** The LOW direction has Wigner values `1/5` once, `3/20` four times,
`-1/20` four times, `(1+sqrt5)/40` eight times, `(1-sqrt5)/40` eight times, and
negativity exactly `sqrt5/5`. Falsifier: any other multiset or value.

**B5.** For every real `v != 0`:

$$
\frac{|\langle \ell,\tilde v\rangle|^2}{\|\tilde v\|^2}=\frac{s^2}{4(5Q-s^2)}
=5\sum_uW_{\tilde v}(u)\,W_\ell(u).
$$

This certifies consistency of the embedding with the registered incidence ratio
of `U-NATIVE-READER-STREAM-SPECTRA`. It is not a new proof of any occurrence law.
Falsifier: one preparation where either equality fails.

**B6.** Finite census over the 624 preparations: every negativity is strictly
positive; the minimum is `(1+sqrt5)/10` and source `1400`, `v=(1,-1,0,0)`,
attains it. Recorded as found: number of minimizers, maximum, number of distinct
values, SHA-256 of the full table. No claim is made about the infimum over all
real sum-zero vectors beyond the bound of B3.
Falsifier: a preparation with negativity below `(1+sqrt5)/10`, or `1400` not attaining it.

### Part C. Physical applicability, no computation

The contract of `C-OCCURRENCE-CYCLE-COUNT-N` section 2 requires the inputs in
the left column. The right column is what this candidate supplies.

| Required input | Supplied here |
| --- | --- |
| finite actual carrier with literal equality | a 25-point index set of a representation; not shown to be an actual native carrier |
| total autonomous permutation of that carrier | no: A5 (i),(ii); the fibre step depends on `kappa` and the clock |
| or a proved finite autonomous factor preserving preparations and event history | no: A5 (iv),(v) are clock-driven, not autonomous |
| preparation domains fixed independently of the target | lines are target-independent, but A2 gives no native map between directions, and by B3 no QDD preparation is a line state |
| total event transducer for completed two-round trials | no |
| every admitted cycle contains completed trials | no cycles are defined |
| renewal inside the supplied resource account | no |

**C1, declared before the run.** Disposition of Part C is
`STOP_APPLICABILITY / H_NOT_TESTED`, unchanged, unless every row is exhibited.
This candidate exhibits none of the missing rows. What it does supply is an
exact finite contract of **spatial** counting for line states and line
readings (B1) and the exact reason the declared QDD reading lies outside it
(B2, B3). Realization as a native contract of actual repeated events remains a
separate target under a new identifier.

Further stated limits. Negativity neither explains the number 31 of the
channels of the registered incidence construction nor proves their minimality.
The owner of the 1/16 versus 1/96 boundary remains the registered information
boundary: the native apparatus history sees only the piston sum modulo five.
A classification of states is not a classification of instruments,
preparations, contexts and renewal; `QDD-INSTRUMENT-CLASS-COMPLETENESS` gains a
classification tool, not a complete apparatus class. The parity split of the
pentit into dimensions 3 and 2 (`Tr A_u = 1`, `A_u^2 = I`) characterizes `p=5`
among odd primes through `(p+1)/2, (p-1)/2`; it selects no physical dimension.

## 4. Code

`claude_verify_c_native_fibre_pentit_wigner_n_2026-10-02.py`. Python standard
library only. Exact arithmetic: integers modulo 5, integer cyclotomic
coefficient vectors, `Fraction`, exact `Q(sqrt5)` pairs. No float. Run from the
repository root with
`LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC`.
Static compilation was done before the pin. No execution preceded the pin.
The hashes of this file and of the verifier are recorded in
`claude_PIN-C-NATIVE-FIBRE-PENTIT-WIGNER-N.sha256` before the first run.

## 5. Systematics

1. Conventions of section 1 are part of the claim: the phase convention of
   `A_u` and `D_u`, the coordinate order of `X`, the lift `ell`, the embedding,
   the sign of `sqrt5`, the negativity convention.
2. The reading premise of section 1 is a premise. If the Canon's QDD carrier is
   not this sector, B3 to B6 say nothing about QDD and remain statements about
   the pentit.
3. Proof-grade claims rest on the inline proofs of section 7; the audits are
   exhaustive over the stated finite sets and are not extrapolated.
4. A5.4 and A5.5 are audited on ticks 3 to 1026; the all-tick statement rests on
   the proof in section 7 and on `KERNEL-Z6-SYNCHRONIZATION [T]`.
5. Target exposure is complete as listed in section 2.
6. One architecture is available to this session (platform Ubuntu 24.04,
   architecture x86_64). The second architecture leg belongs to public
   validation and is pending.
7. No external theorem is used in any proof. Sources are cited for
   terminology and for one boundary remark only (section 8).

## 6. Failure threshold, labels, breaking

Any `FAIL` falsifies the corresponding claim at its stated scope; the run is
archived as is. Exit status is nonzero on any `FAIL`.

Labels on a clean run. Claims with a complete inline proof: `candidate-T`
(A1, A3, A5 (i) and (iv), the trace formula of B1, B2, B3, B5). Finite
exhaustive computations: `candidate-C` in this lane (A2, A4, A5 (ii),(iii),(v)
on the audited range, the projector audit of B1, B4, B6), eligible for
computation-grade T only after byte-identical stdout on two architectures.
Part C carries no label: it is a disposition.

Breaking, after the run and before any packaging: an independent
implementation by a different code path. Generators retyped from the Canon
text, not imported. Wigner function from Weyl expectation values, not from the
parity formula. Cyclotomic arithmetic in the basis `1,zeta,zeta^2,zeta^3` with
reduction by the fifth cyclotomic polynomial. Invariant forms by a different
elimination. Counterexample searches: a real sum-zero integer vector outside
the 624 with nonnegative Wigner function or negativity below `sqrt5/20`; a
second collision; a tick with two selectors.

## 7. Proofs

**A3.** With `u=(q,r)`: `A_u A_u|j> = zeta^(2r(q-j)) zeta^(2r(j-q))|j> = |j>`.
`<k|A_u|j>` is `zeta^(2r(q-j))` at `k=2q-j`, and the conjugate of `<j|A_u|k>` at
`k=2q-j` is `zeta^(-2r(q-k)) = zeta^(2r(q-j))`: Hermitian. Only `j=q` is fixed,
with phase 1: trace 1. For `v=(q',r')`, `A_uA_v|j>` lands on `|2q-2q'+j>`, so the
trace vanishes unless `q=q'`, and then equals `sum_j zeta^(2(r-r')(j-q)) = 5 delta`.
For `s=(a,b)`: `A_sA_uA_s|j>` lands on `|4a-2q-j>` with exponent
`2b(4a-2q-2j)+2r(q-2a+j) = 2(2b-r)(2a-q-j)`, which is `A_(2s-u)|j>`. The entry
`<k|sum_u A_u|j>` forces `q=(k+j)/2` and sums `zeta^(2r(q-j))` over `r`, giving
`5 delta_(k,j)`. All steps use only that 2 is invertible.

**A4, multiplier lemma.** `L_a, L_b, L_c` are involutions (for `c`: the piston
shear along `u_c` is fixed by the piston part of `b`). If
`L^T omega L = m omega` with `L^2 = I`, then `omega = m^2 omega`, so a nonzero
solution has `m = +-1`. The remaining statements of A4 are exact finite linear
algebra over `F_5`.

**A5 (iv).** By `KERNEL-Z6-SYNCHRONIZATION [T]`, `z_n = 4 + 2 theta_(n-1)` for
every origin-zero state and `n >= 3`. Then
`sigma_n = 4 + 2 theta_(n-1) + 2 theta_n`, which is 4 (`e`) for bits 00, 8 = 3
(`d`) for bits 11, and 6 = 1 (`b`) for unequal bits.

**B1, trace formula.** `Tr(Pi_L Pi_M) = (1/25) sum_(u in L, v in M) 5 delta_(u,v)`.

**B2.** Six lines pass through `u`, one per direction, and every `v != u` lies
on exactly one of them. So `sum_(L through u) p(L) = 6 mu(u) + (1 - mu(u))`.
For `p(L) = Tr(rho Pi_L)`: `W_rho` has total `Tr(rho) = 1` by `sum_u A_u = 5I`
and line sums `Tr(rho Pi_L)` by definition of `Pi_L`, so it is the unique `mu`.

**B3.** For real `psi`, `W(q,0) = c(2q) / (d |psi|^2)` with the cyclic
convolution `c(m) = sum_k psi_k psi_(m-k)`. Summing over `q`:
`(sum psi)^2 / (d |psi|^2) = 0`. With `hat psi(k) = sum_j psi_j zeta^(-jk)`:
`hat c = (hat psi)^2`, `hat psi(0) = 0`, `sum_k |hat psi(k)|^2 = d |psi|^2`.
Since `psi != 0`, some `hat psi(k) != 0`, so `c` is not identically zero: the
row has a nonzero entry and sum zero, hence a strictly negative entry. By
Parseval and Cauchy-Schwarz over the `d-1` nonzero frequencies,
`sum_m c(m)^2 = (1/d) sum_k |hat psi(k)|^4 >= d |psi|^4 / (d-1)`, so
`sum_q W(q,0)^2 >= 1/(d(d-1))`. A zero-sum real row has negative mass
`(1/2) sum_q |W(q,0)| >= (1/2) (sum_q W(q,0)^2)^(1/2)`.

**B5.** `<l, v~> = -s / sqrt(20)` and `|v~|^2 = Q - s^2/5`. The second equality
is `Tr(rho sigma) = 5 sum_u W_rho(u) W_sigma(u)`, from `Tr(A_uA_v) = 5 delta`.

## 8. Sources

Cited for terminology and for one boundary remark. No proof above depends on them.

1. D. Gross, Hudson's theorem for finite-dimensional quantum systems,
   J. Math. Phys. 47, 122107 (2006), arXiv:quant-ph/0602001. Phase-point
   operators and Wigner functions of line states.
2. M. Howard, J. Wallman, V. Veitch, J. Emerson, Contextuality supplies the
   magic for quantum computation, arXiv:1401.4174. Read in this session: the
   text states that every single-qudit stabilizer projector belongs to exactly
   one context and that its construction therefore introduces two-qudit
   projectors. For this reason no contextuality theorem is imported into the
   one-pentit fibre; B2 is used instead.
3. D. Gross, Non-negative Wigner functions in prime dimensions,
   arXiv:quant-ph/0702004. Named by the owner as a route to B3. Not read in
   this session and not used; B3 has its own proof above.

## 9. Action layer

L1 only. No lift to L2 through L6 is claimed or implied. No row of the registry,
frontier or Canon is changed by this candidate.
