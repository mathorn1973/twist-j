# P-ENTROPY-BRIDGE-1 preregistration

Status: PRE-PIN DRAFT

This document freezes the complete decision surface for the first probe of
the ENTROPY-BRIDGE program: the frozen joint Cesaro law of the public kernel
under the Thue-Morse drive, the formalization of one fired lift falsifier,
and the finite necessary conditions on the finite-cylindrical cut. It
contains no gate output and earns no scientific status. Formal execution is
forbidden until this document and the accepted verifier are committed and
pushed as one immutable preregistration pin and that remote pin is read back.

## Public identity and action layer

```text
program:          ENTROPY-BRIDGE
probe:            P-ENTROPY-BRIDGE-1
public lock:      issue 25
owner:            entropy-bridge session
branch:           probe/P-ENTROPY-BRIDGE-1
path:             probes/P-ENTROPY-BRIDGE-1/
initial base:     57de0af8a50e14e52f0fa81e0158f6a370cab5a5
action layer:     L5 stream; L6 statements scoped to the frozen finite
                  window; no L2 lift is claimed by this probe
scientific state: O (ENTROPY-LAYER-BRIDGE), plus one F formalized
```

This probe is based on Public Canon 2, tag `canon-v2`, activation commit
`5abb22319007fd3172f7123f4b3a71b547fb94af`, content commit
`7cfe2a62a456d0f84b1f60b4945dcdfe896e99db`, and Canon SHA-256
`abd0e026ccc2be00cdb0d9d13d634e0a71602b1565e6d53ac23a99b506281021`.

## Pinned owner ruling (R4, 2026-07-14), the definitional source

The owner ruling fixing this program, quoted in its operative parts:

1. The literal 5-adic lift of the generator presentation fails the relation
   `(bc)^5 = 1`: over the integers, with `bc = c o b` in the public order,
   `(bc)^5` is the affine map `x + (10, 5 - 5r, 10, 5 + 5r, 5, 0)`. Modulo 5
   it is the identity; over `Z_5` it is not. The five-element relation is a
   property of the shadow, not of the literal lift. The lifted-generator
   source (named Y5-i in session records) is FIRED as the bridge source; it
   may remain a zero-entropy control model only.
2. Frozen finite-place carrier (Y5-ii): `K = Q(zeta_5)`, `lambda = 1 -
   zeta_5`, `Y_5 = O_{K,lambda}` (the completion at the unique place above
   5, `5 = u lambda^4`, `O/5O = F_5[lambda]/(lambda^4)`). The finite-place
   verb is pure multiplication `V_5(y) = J y`: invertible, Haar-preserving,
   zero entropy (J is a lambda-adic unit; V_5 an isometry). The coordinates
   `(q, r)` are not adjoined as free `Z_5` factors; they must arise from
   higher lambda-adic digits and the carry structure of the cut. That
   construction is sought, not assumed.
3. Frozen clock: `K_TM` is the two-sided Thue-Morse subshift with shift
   `S_K`, unique substitution measure `m_TM`, and reading `theta(kappa) =
   kappa_0`. The public one-sided word is its distinguished forward orbit.
   No digit-sum parity on all of `Z_2` is introduced.
4. Frozen source and cut: `X = K_TM x O_{K,lambda} x T^4` with
   `S(kappa, y, x) = (S_K kappa, J y, T_J x)`. By the Pinsker structure the
   finite cut must satisfy `P(kappa, y, x) = P_5(kappa, y)` almost
   everywhere: the archimedean point never enters the finite cut. The sought
   equation is `P_5(S_K kappa, J y) = F_{theta(kappa)}(P_5(kappa, y))` with
   `F_eps(psi) = g_{z(psi) + 2 eps mod 5}(psi)`. The target is the full
   public carrier `F_5^6`; the image of the invariant source law lies on the
   recurrent core; surjectivity onto all 15625 states is not required;
   transient states enter through basin weights only.
5. Frozen joint law: `U_hat(kappa, psi) = (S_K kappa,
   F_{theta(kappa)}(psi))`, `nu_N = (1/N) sum_{j<N} (U_hat^j)_* (m_TM x
   u_6)` with `u_6` uniform on `F_5^6`; the weak limit `nu_* = lim nu_N` is
   a gate, not an assumed result. Required closed form, also a gate: the 312
   size-20 components carry weight `50/15625 = 2/625` each, the singlet
   `25/15625 = 1/625`; the conditional law on each attractor is uniform; the
   psi-marginal is `1/6250` on every recurrent state. Neither branch `F_0`
   nor `F_1` alone preserves the uniform law on the recurrent core (each has
   indegree 2 on half the support and 0 on the other half); their fair
   average preserves it; therefore the gates must verify actual correlations
   with Thue-Morse time, not the frequency 1/2 alone.

Primary falsifiers fixed by the ruling: failure of equivariance (this
probe's definitional slice), non-existence of the limit (failure of the
frozen exact window equalities), wrong pushforward, wrong gyron or generator
statistics.

## Frozen carrier and operators

Work over the public kernel exactly as pinned by the Canon reproduction:

```text
X6 = F_5^6, x = (p1, p4, p1p, p4p, q, r), arithmetic mod 5.

a(p1,p4,p1p,p4p,q,r) = (p4,p1,p4p,p1p,q,r)
b(p1,p4,p1p,p4p,q,r) = (-p1p,-p4p,-p1,-p4,-q,-r)
c: piston -> b4(piston) + (2,1,2,1) + r (0,1,0,-1); q -> 1-q; r -> -r
d(x) = (2,1,3,4,1,1) - x
e(x) = (2,1,3,4,2,1) - x

(g o h)(x) = g(h(x));  bc = c o b.
z(x) = sum of the six coordinates mod 5.
drive theta_n = popcount(n) mod 2; selector i_n = (z + 2 theta_n) mod 5;
(g_0,...,g_4) = (a, b, c, d, e); branch maps F_eps(x) = g_{(z(x)+2 eps) mod
5}(x) for eps in {0, 1}.
Integer lift: the same five formulas read over Z (hence over Z_5), no
reduction.
Multiplication-by-J matrix M_J on Z^4 in basis (1, zeta, zeta^2, zeta^3):
rows (1,0,-1,1),(0,1,-1,0),(1,0,0,0),(0,1,-1,1).
```

Census protocol (as in the public reproduction): full enumeration of all
15625 seeds, warmup 400 ticks, collection window 300 ticks, attractor
signature = the window visit set; closure of every signature under both
branch maps is a gate.

Cesaro protocol, frozen: integer occupation transport. `w_0` = one unit of
mass per state (15625 units). One tick: push every unit through
`F_{theta_n}`. Frozen window `W = [512, 2048)` (1536 ticks); frozen ladder
point `N = 1024` for the mid-window witness gate. All statistics below are
exact integers or exact rationals derived from them.

## The six frozen fields

```text
equation:     the R4 ruling above, operative clauses 1 to 5, with the gate
              targets G01 to G16 below as exact equalities; in particular
              the closed form of nu_* on the frozen window: occupation
              exactly 3840 = 1536 x 15625 / 6250 units per recurrent state
              and 0 per transient state; component masses exactly the basin
              sizes from n = 512 on; letter masses exactly
              (b, d, e) = (16000000, 4000000, 4000000) on W; TM pair (0,0)
              count exactly 256 on W.
code:         verify.py in this directory, Python 3 standard library only,
              exact integer and Fraction arithmetic, no float in any
              assertion, single process, no filesystem writes, runtime
              under 120 seconds.
carrier:      the public F_5^6 kernel with the constants above; the
              Thue-Morse drive by popcount; the integer affine lifts; the
              matrix M_J. No external data.
systematics:  one distinguished forward driver word (theta_n)_{n>=0}; the
              frozen dyadic window; recon-lane exploration disclosed below;
              interpreter version immaterial (integer operations only);
              the census reproduction re-derives, not imports, the public
              313 = 312 x 20 + 1 x 10.
failure
threshold:    any gate FAIL. Every gate is an exact equality or exact
              integer inequality. There are no tolerances and no
              thresholds that could move.
action layer: L5; the L6 measure content is scoped to the frozen finite
              window equalities; the L2 (toral, archimedean) side enters
              this probe only through its cited theorems and is not
              computed here; no L2 -> L5 lift is claimed closed.
```

## Gates (all exact; the frozen decision surface)

```text
G01 RELATIONS      a^2 = b^2 = c^2 = d^2 = e^2 = id and (bc)^5 = id on F_5^6.
G02 LIFT-DEFECT    over Z, (bc)^5(x) = x + (10, 5-5r, 10, 5+5r, 5, 0)
                   exactly (matrix defect -5, +5 in the r column at rows
                   p4, p4p; translation (10,5,10,5,5,0)); nonzero over Z;
                   zero mod 5. This formalizes the fired lift falsifier.
G03 UNIT           det(M_J) = 1 (exact integer determinant), hence
                   multiplication by J is bijective on (Z/5^m)^4 for every
                   m >= 1; witness J = 1 + zeta^2 == 2 (a unit) at the
                   ramified place (zeta == 1 mod lambda).
G04 COUNT-313      the census yields exactly 313 attractors.
G05 SIZES          312 of size 20, 1 of size 10; support 6250, disjoint.
G06 BASINS         312 basins of 50, 1 basin of 25; coverage 15625.
G07 SHEET          every recurrent state has z in {1, 4}; the selector
                   fires only b, d, e on the sheet.
G08 CLOSED-BOTH    every signature is closed under both branch maps.
G09 ANCHOR-312     (5^4 - 1)/2 = 312 and 312 x (2/625) + 1/625 = 1: the
                   component-weight vector normalizes and its multiplicity
                   pattern matches the antipodal census of F_5^4 (312 pairs
                   and one fixed point). Recorded as arithmetic; the
                   correspondence itself carries no claim here.
G10 INDEGREE       on the recurrent support, each branch F_0 and F_1 has
                   indegree histogram exactly {0: 3125, 2: 3125}, and the
                   total indegree F_0 + F_1 is exactly 2 at every recurrent
                   state (the fair average preserves the uniform law;
                   neither branch alone does).
G11 COMPONENT-MASS at n = 512 the mass per component equals its basin size
                   exactly: histogram {50: 312, 25: 1}.
G12 OCCUPATION     the integer occupation over W = [512, 2048) equals
                   exactly 3840 units at every recurrent state and 0 at
                   every transient state (the psi-marginal of the frozen
                   window is exactly uniform 1/6250 on the recurrent core).
G13 LADDER-1024    the maximal within-component L1 distance of the
                   normalized occupation to uniform at N = 1024 is exactly
                   1/256, and at N = 2048 it is exactly 0: the convergence
                   is real, the exactness at the full window is not
                   tautological.
G14 LETTERS        letter mass counts on W are exactly b = 16000000,
                   d = 4000000, e = 4000000, and no other generator fires;
                   the ratios are exactly (2/3, 1/6, 1/6).
G15 PAIR00         the count of n in W with theta_n = theta_{n+1} = 0 is
                   exactly 256 = 1536/6 (the gyron pair density on the
                   frozen window is exactly 1/6).
G16 DEPTH          subword counts of the driver: p_TM(3) = 6 and
                   p_TM(4) = 10; since a finite-cylindrical cut at
                   lambda-depth 4 (piston shadow only) has at most
                   p_TM(K) x 625 values and the recurrent core has 6250
                   states, TM-depth K >= 4 is necessary at lambda-depth 4.
                   The feasibility question itself is out of scope here.
```

Falsifier map, per the ruling: equivariance slice = G01, G02, G03 (the
definitional surface this probe touches); limit existence = G11, G12, G13;
pushforward = G11, G12 (component weights 2/625 and 1/625, uniform
conditional law, uniform psi-marginal); gyron and generator statistics =
G14, G15. A fired gate is a first-class outcome and is merged, not hidden.

## Environment and execution

```text
cd <repo root>
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 probes/P-ENTROPY-BRIDGE-1/verify.py
```

Exit 0 and the exact stdout captured as EXPECTED.txt on the first formal
run (aarch64); RUN.md records platform, architecture, Python version,
hashes, byte counts, commit pins, neutral descriptors only. The pull
request check reruns on GitHub x86_64; byte identity of stdout across the
two architectures is required for the computation gate.

## Disclosure

Recon-lane exploration (incubation lane, session records of 2026-07-14,
project docs C-ENTROPY-RESIDUE-1 and O-ENTROPY-LAYER-BRIDGE_RECON) computed
the values frozen above before this pin, on x86_64, outside this
repository, with an unpinned recon script. That exploration carries no
public status; it is disclosed here in full per policy. The formal status
of every gate derives only from the post-pin two-architecture runs of the
pinned verifier.

## Out of scope, explicitly

The construction or feasibility of the cut P_5 beyond the necessary
condition G16 (successor probe, to be preregistered separately); any toral
or archimedean computation; the L2 -> L5 entropy transport statement; any
physical or proper-time reading; any claim that the public architecture is
derived from J or M_J. Nothing in this probe modifies canon/, the registry,
or the frontier; folding any outcome is a separate sealed step.
