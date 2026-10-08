# C-FIELD-STATIC-TRANSPOSITION-COMPLETION-N: preregistration

Status: **NON-CANONICAL, conditional candidate-T proofs, candidate-C finite
audits, L1.** This is a new local research note, not a formal public probe,
public preregistration, Canon amendment, or physical derivation.

## Authority, provenance, and disclosure

The checked public authority is `mathorn1973/twist-j`, `main`
`7d7f588c42422c2cf37b04d76ebc13ca55eb96dc`, ACTIVE Public Canon v100,
content commit `a4cc9666662967527abe711441833ff600c00337`, tag `canon-v100`.
The Canon has 980212 bytes and SHA-256
`5e4de2da8d57ff2f7e4b873e6236b0695677e20d173d894ee70562c1389648c4`.
The declared content and tag target are ancestors of main. The five normative
hashes and the required public checks were verified. POLICY.md, AGENTS.md,
CORE.md, FRONTIER.md and the relevant registry/evidence/gates were consulted.
An explicit scan of 222 remote heads and searches of public code, issues and
registry found no collision for this candidate identifier. No public issue or
branch is claimed, and nothing is being committed or published by this note.

Comparison sources are PR #1424, head
`c404723bbda3a65dd39c86ae4fc1152b587977c3`, and the user-supplied
`C-FIELD-STATIC-CONTACT-SYMMETRY-N.zip`. All eleven files in that bundle's
SHA256SUMS were verified. That bundle is non-canonical evidence, not authority.
Its fired S3 factorization and S4b global uniqueness claims remain fired.
Its uploaded scientific programs have not been read or executed for this work.

The new completion and the witnesses below were derived by hand before this
local freeze and discussed with two separate assistant agents. Consequently
the witnesses are discovery inputs, not blind predictions. The second program
will be independently implemented from this specification without reading or
importing the primary program. This is implementation independence, not a
claim of an independent external scientific review or blind discovery.

This specification is frozen first. Both program sources and this file will
then receive SHA-256 pins in FREEZE.md before either program is first run.
Compilation and source inspection are allowed before that joint freeze;
scientific evaluation, trial imports and dry scientific runs are not. Exact
first stdout, stderr, exit status and environment will be retained. A failed
claim or program is not silently edited and rerun under the same pin.

## 1. Equation and complete carrier

The carrier is all cells `s=(m,b,E,M,r)`, where m and b are triples of vectors
in Z^4, E is in Z^4, M is in Z^2 and r is a nonnegative integer. No Gauss,
integral-split, accepted-reaction, or charge-neutral restriction is implicit.
All m registers reside at vertex 0; b_i resides at vertex i. Write
`chi(v)=sum(v)`, `Q(v)=v^t K v` and

```text
C = ((1,-1),(-1,0),(0,1),(0,1))
D = ((1,1,1,0),(-1,-1,0,-1),(0,0,-1,1))
K = ((6,2,-1,2),(2,6,2,-1),(-1,2,6,2),(2,-1,2,6))
L = ((1,-3,-1,-2),(-3,4,-2,1),(0,5,1,2),(5,-5,2,-1))
Vinv = ((1,2,1,2),(2,-1,2,-1),(0,-5,1,-3),(-5,5,-3,4))
Af = ((1,0,1,0),(0,1,0,1),(-2,1,-1,1),(1,-3,1,-2))
Bf = ((4,-2,2,-1),(-2,6,-1,3),(2,-1,2,0),(-1,3,0,2))
R = ((1,-2,1,0),(0,0,0,0),(0,0,0,0))
AM = ((1,0,0,0),(0,-1,0,0),(0,-1,1,0))
```

Define `Hraw=E.E+M.M+E.(C M)`,
`H1=sum Q(m_i)+sum Q(b_i)+Hraw+r`,
`rho=(chi(b0)+sum chi(m_i),chi(b1),chi(b2))`, and `defect=D E-rho`.
The comparison family is `Hc=H1+(c-1)(r mod 2)`, with a fixed real parameter
domain C containing 1. For a chain, the parity term is the sum over stocks;
other stocks are fixed when applying a cell contact.

For y=(a,b,c,d) and sigma=(u,w), use

```text
P y = (a-b,-a,b,b,c,d)
S sigma = (u,u,w,u-w,0,0)
a = (2 E0-3 E1+E2+E3)/5
b = (-E0-E1+2 E2+2 E3)/5
c = M0; d = M1
u = (2 E0+2 E1+E2+E3)/5
w = (E0+E1+3 E2-2 E3)/5
H(y) = 2 a*a-2 a*b+3 b*b+c*c+d*d+2 a*c-a*d-b*c+3 b*d
Hstatic(u,w) = 3 u*u-2 u*w+2 w*w
EC(q) = (q0*q0+q1*q1+2 q2*q2)/5, for sum(q)=0.
```

This gives the unique rational split `(E,M)=P y+S sigma`, with
`Hraw=H(y)+Hstatic(sigma)=H(y)+EC(D E)`. An integral split has all six split
coordinates integral. For integral y, `y in L Z^4` iff `Vinv y` is divisible
by 5 in every coordinate (equivalently a+2b and c+2d vanish modulo 5).

The inherited complete reaction G is identity off the following funded
branches. It fixes b and sigma.

* R branch: require integral split and `y=L x`, x integral. If
  `r+4 H(x)-2>=0`, replace R by AM, y by x, and r by `r+4 H(x)-2`.
* AM branch: require integral split. If `r+2-4 H(y)>=0`, replace AM by R,
  y by L y, and r by `r+2-4 H(y)`.

Every rejection fixes the entire cell. Set `aG(s)=1` iff G changes m, and
`e(s)=1` iff it performs the R-to-AM branch. The recorder is
`Ghat(s,p)=(G(s),p+e(s) mod 5)` on all p in Z/5.
The inherited field step is `F(E,M)=(E+C M, M-C^t(E+C M))`; it fixes all other
registers. The proof may use, and the audit rechecks, `F G=G F`,
`F P=P Af`, `F S=S`, `Af L=L Af`, and the energy identities.

### Frozen new proposal and completion

For ij in {01,02,12}, swap the entire registers b_i,b_j, leave m and M fixed,
and put `E'=E+(t/5) k_ij`, with

| ij | t | k_ij |
|---|---|---|
| 01 | chi(b0)-chi(b1) | (-2,-2,-1,-1) |
| 02 | chi(b2)-chi(b0) | (1,1,3,-2) |
| 12 | chi(b2)-chi(b1) | (-1,-1,2,-3) |

The raw funded proposal P_ij exists exactly when `5 divides t` and
`r-kappa>=0`, where

```text
kappa = Hraw(E',M)-Hraw(E,M)
      = (t/5)^2 |k_ij|^2 + 2(t/5) E.k_ij.
P_ij also sets r'=r-kappa.
S_ij(s) = P_ij(s) if that proposal exists and aG(P_ij(s))=aG(s);
          s otherwise (identity on every register).
```

The symbol S_ij denotes a contact; S without a subscript remains the static
embedding above. No other contact proposal or energy family is admitted by
the new maximality claim.

### Claims frozen before evaluation

T1. These shifts are the unique rational shifts with `C^t(E'-E)=0` and the
specified Gauss-defect-preserving register transposition. They are integral
exactly when 5 divides t. The price formula holds on every raw state with an
integral proposal and equals `EC(D E')-EC(D E)` there.

T2. Each S_ij is an involution of the complete carrier. It preserves H1,
the full Gauss defect, m, M and the rational active coordinate y. It commutes
with complete G and F, preserves e, and, with p fixed, commutes with Ghat.

T3. On every accepted reaction state, set `deltaG=r(Gs)-r(s)`. The completion
acts by its proposal precisely when 5 divides t and
`kappa<=min(r,r+deltaG)` (a fixed proposal may equal identity). Rejected
reaction states may only be sent to rejected states. The acceptance rule
is symmetric between the proposal endpoints.

T4. Within the fixed class of complete maps choosing only identity or the
same legal P_ij at each state and commuting with G, S_ij is the unique map
with greatest nonidentity support by set inclusion. This is class-relative
maximality, not a source selection principle or uniqueness of all contacts.

T5. Every committed S01 event has even kappa and preserves all Hc. For S02
and S12, kappa is odd exactly when t/5 is odd. Each of these complete laws
therefore preserves exactly c=1 in the specified family C. Witnesses below
prove the necessity; preservation of H1 proves sufficiency on the infinite
carrier. There is no independent derivation of H1 from conservation here.

T6. The naive rule accepting whenever its own stock is nonnegative fails
G-commutation on the frozen r=5 and r=6 witnesses below. The new S02/S12
are the identity at these states and their G partners. Commutation with F
does not require zero field price in the full static-transposition class.
Commutation with occupied-stock swaps A/B or the whole old chain step is not
claimed and has a frozen counterexample below.

## 2. Code and execution protocol

`verify.py` will use exact rational splitting (fractions.Fraction) and a
general quadratic-form calculation. `break_check.py`, written by a separate
assistant agent, will use raw integer fields, residue tests and integer
division for G. It must not import or read verify.py or any uploaded program.
Both use only the Python standard library, no random sampling and no floats
in scientific comparisons. All three contacts and all rejected branches are
tested. Runtime budget is 300 seconds per program. An execution timeout is
an incomplete audit, not a pass. Run from this directory as:

```text
LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 -I verify.py
LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 python3 -I break_check.py
```

The programs print deterministic exact counts, branch coverage and the
specific witness outcomes, and return nonzero on any discrepancy. Environmental
metadata and times are recorded separately. The first outputs are evidence;
they may be copied to EXPECTED files only after a successful completed run.

## 3. Data and finite audit domains

No external measured data. Matrices, definitions and discovery witnesses are
the complete inputs. Each program freezes its final loops and ordering in its
source before the joint pin. The mandatory domains are:

* Primary raw domain: E in {-1,0,1}^4; M in {(0,0),(1,0),(0,1)}; m in
  {R,AM,zero triple,R with (1,0,0,0) added to its first vector}; r in {0,2,7}.
  Cycle deterministically through eight b fixtures with charge triples
  (0,0,0), (5,-5,0), (5,0,-5), (0,5,-5), (1,0,-1), (2,-1,-1),
  (10,-5,-5), (-5,5,0). Embed q as q*(1,0,0,0); add the neutral vector
  (1,-1,0,0) to b0 on odd raw-field indices. All defects, including nonzero
  defects and non-neutral m, remain admitted.
* Primary integral domain: x in {-1,0,1}^4; sigma in
  {(-1,0),(0,0),(1,0),(2,1),(1,3)}. Test both R with y=Lx and AM with y=x.
  Choose Gauss b charges from DE (both endpoint totals are zero); add the
  same neutral b0 vector on odd x indices. For algebraic reaction cost
  deltaG, set h=max(0,-deltaG) and test the unique stocks in
  {0,1,h,h+1,h+5,h+7}. Add all fixture stocks 0 through 12.
* Independent breaker domain: raw E in {-1,0,1}^4 and M in {-1,0,1}^2 with
  a deterministic rotation through the above m, b and stock fixtures; and
  x in {-1,0,1}^4, sigma in {-2,-1,0,1,2}^2, both R/AM branches, stocks
  {0,1,2,5,6,7,20}. Include structurally rejected R image cosets, nonintegral
  splits, both directions of admission-mismatch rejection, and all frozen
  witnesses. Additional boundary stocks calculated mechanically from deltaG
  and kappa are allowed only if specified in its source before the joint pin.

Both check full-state involution, H1, defect, G/F/Ghat commutation, active
coordinate preservation, raw proposal reversal and the parity formula. They
recheck the inherited field/reaction identities separately. Coverage counts
distinguish integral rejections, stock rejections, admission-mismatch
rejections, committed accepted/accepted and committed rejected/rejected
events, and actual nonidentity events. Finite counts do not establish T1-T5
on the unbounded domain; the separate written proof must do so.

### Fixed witnesses

Let v=(1,0,0,0). At m=R, b=(5v,-5v,0), E=(2,2,1,1), M=0 and r=7,
the active coordinate is zero. Both reactions and both proposals 02 and 12
are admitted. Their prices are +5 and output stocks are 2:

```text
02: E'=(1,1,-2,3), b'=(0,-5v,5v)
12: E'=(1,1,3,-2), b'=(5v,0,-5v)
G before contact has stock 5; G after contact has stock 0.
H1=335 throughout each complete square; parity changes from 1 to 0.
```

At the same input with r=5 or6, the raw proposal is funded but changes G
admission. The new contacts reject the whole proposal. The reverse raw
proposal outputs with stocks 0 and1 respectively test rejected-to-accepted
admission mismatch. With m=AM, y=(0,0,1,0), the same static sigma=(2,1),
M=(1,0) and r=7, F acts nontrivially and both +5 contacts remain accepted.

At the common PR contact input m=R, b=(5v,0,-5v), E=(2,2,1,-4), M=0,
r=81, the static proposal prices are (0,0,-5). S12 is committed and has
E'=(3,3,-1,-1), r'=86. H1=424. The old direct and alternative contacts
at this input instead cost 5 and80. The comparison makes no new assertion
about those old programs or their runs.

For the chain limitation, extend the r=7, price +5 witness by a nonnegative
external stock eta=0. Let B exchange eta and the cell stock. Then B after
S gives changed field, cell stock0, eta2; S after B rejects and gives the
original field, cell stock0, eta7. Thus the complete maps do not commute.

## 4. Systematics and limits

The family is chosen before the test and the price compensation already uses
H1. Agreement cannot derive that choice independently. Both audits run on
one local architecture; same-architecture agreement is not the public
two-architecture gate. An assistant proof review is separate from the author
but is not external peer review. Public CI for PR #1424 does not validate
these new files. No source-U occurrence rule, preparation of a contact label,
operational readout, physical calibration, metric, Hilbert coherence, or
photon phase is added. Old fired statements remain recorded in their source;
the old phrase 'zero price and nonzero moved charge exactly on Zdom' must
restrict to Zdom intersect {nu != 0} when nonzero charge movement is required.

## 5. Failure threshold

One exact counterexample to T1-T6 fires the corresponding claim. No tolerance,
post-run threshold changes, hidden failures, or finite-to-infinite inference.
The deliberate naive-rule and stock-swap counterexamples must be found with
the specified outputs; their failure would also fail the audit. If a program
fault prevents evaluation, retain its first outputs and disposition before
any successor version. There is no formal gate or promotion in this local pin.

## 6. Action layer

L1 only. All mathematical assertions are conditional on the restated carrier
and laws. The deliverable is a self-contained proof, frozen exact audit
sources and run records, a separate assistant review, and a short promotion
proposal retaining the physical source-selection obligation.
