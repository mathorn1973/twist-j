**Public extract.** Everything below the rule is the recon text frozen before the first
execution, byte for byte, except that four passages are replaced by the bracketed markers
O1 to O4. Complete frozen text: 8965 bytes, SHA-256
`e557dab31e8a801b53f57af74d431c64697cfdc71b8b1199f856a6b8b1dfa0a6`.
Custody and the hashes of the omitted passages are in [PROVENANCE.md](PROVENANCE.md).

---

# RECON-PATH-PHASE-ONE-CARRIER (review recon, frozen before first execution)

NON-CANONICAL. Project TWIST J incubation lane, 2026-11-06. Review session of
the owner's status note on the hbar/alpha branch. Target line on any later
promotion: public (mathorn1973/twist-j). No authority, no status movement.
Basis: Public Canon v109, main 650029c20408f1dd665983d72225d0d195fd030e,
canon/SHA256SUMS 5 of 5 OK. Inputs read before this freeze: STATUS.md, the
registry alpha rows, the text files and verifier sources of PR #1908, #1912,
#1915, #1917, and the counts table in RESULT.md of #1908. The per-step branch
traces in EXPECTED.txt of #1908 were replayed for byte identity but not read.
No computation of the quantities below was made before this freeze; every
expectation below is an analytical derivation written first.

## 1. Equations and targets

### Part U. Native U at a common counter

Native law (CANON.md, native conventions): x=(x0,x1,x2,x3,q,r) in F5^6,
z=sum, theta_n=s2(n) mod 2, F_t(x)=g_(z+2t mod 5)(x), counter from zero,

    a=(x1,x0,x3,x2,q,r)          b=(-x2,-x3,-x0,-x1,-q,-r)
    c=(2-x2,1-x3+r,2-x0,1-x1-r,1-q,-r)
    d=(2-x0,1-x1,3-x2,4-x3,1-q,1-r)   e=(2-x0,1-x1,3-x2,4-x3,2-q,1-r)

Integer lift of the fibre: rt_0=r_0 in {0..4}, rt_(n+1)=eps*rt_n+kappa with
(eps,kappa)=(+1,0) for a, (-1,0) for b and c, (-1,1) for d and e.

U1. For all 15625 states and both bits the selected letter, the new trace
    and (eps,kappa) depend on (z,t) only.
U2. Image sizes after ticks 1,2,3 are 6250, 6250, 3125. For 3<=n<=64 the
    reachable set E_n is the full sheet z_n=4+2 theta_(n-1) mod 5, and the
    tick is a bijection E_n -> E_(n+1).
U3. For 3<=n<64 the tick on E_n is one affine map x -> M_n x + t_n with
    M_n in {-P, -I}, P the swap (x0,x1,x2,x3)->(x2,x3,x0,x1); in particular
    (eps,kappa) is single valued on E_n. Hence for every window n0<n1,
    n0>=3, the lifted shift rt_n1 - (-1)^(n1-n0) rt_n0 is the same integer
    on all 15625 origin-zero trajectories, and the difference of any two
    trajectories only changes sign.
U4. For n>=3 the four pistons at n+1 are a function of the four pistons at n
    alone, and that function is a bijection of F5^4.
U5. Every y in E_3 has exactly five origin preimages, one on each trace
    sheet, with r_3 = r_0+1 (z_0=0), 1-r_0 (z_0 in {1,2}), 2-r_0 (z_0 in {3,4}).
U6. Closed form. With A(M)=sum_(i>=0) (floor(M/4^i)-floor(M/(2*4^i))), for
    even length 2m the common lifted shift from n0 is
    +(A(k0+m-1)-A(k0-1)) for odd n0=2k0-1 and -(A(k0+m-1)-A(k0-1)) for even
    n0=2k0. Range: n0>=3 on all states, n0>=1 on X1 union X4. In particular
    1->11, 11->21, 21->31 give +4, +2, +4 (PR #1915).
U7. Census, no threshold: distribution of the ten-tick shift over odd n0<4096
    carrying the same finite marks (n0 mod 5, theta_(n0-1), theta_n0)=(1,0,1).

Reading to be tested: at a common counter the native fibre phase carries no
information about the course of a trajectory; the two PR #1915 windows are
two times, not two paths.

### Part K. Contact carrier (PR #1908 law and word)

O=Z[j], power basis, u=1-j, rho=j^2. Total relative contact on a pair
(x,y): refused unless x-y in 2O; else d=(x-y)/2, x'=s+rho d, y'=s-rho d.
For v in O: residue c(v)=coefficient sum mod 5; v vbar = A(v)+B(v) phi with
A=sum a_i^2-(a0a1+a1a2+a2a3), B=(a0a1+a1a2+a2a3)-(a0a2+a1a3+a0a3);
Q(v)=2A+B. First digit: v1(v)=c((v-ct)/u), ct in {0..4} the integer lift of
c(v). Potential psi(state)=2*sum_i c(x_i)*v1(x_i) mod 5.

K1. Independent replay of WORD.txt (sha256 6fed5cf0...b65a7) and its slot
    1/2 image sigma on I_t, t=-2..2: complete targets G_t; counts
    (admitted, refused, changed, diagonal) for w are (137,185,135,2),
    (177,145,170,7), (112,210,100,12), (177,145,170,7), (123,199,123,0),
    and sigma at t equals w at -t.
K2. Account exactness. For every admitted contact, Q(d) = psi(after) -
    psi(before) mod 5. Derivation: (rho-1)=-u(1+j), 1+j=2 mod u, so the first
    digits move by -(c_x-c_y) and +(c_x-c_y); Q(d)=2c(d)^2=3(c_x-c_y)^2 mod 5.
    Audits: the ten forward runs; all admitted pairs with both entries in the
    box [-2,2]^4 (390625 ordered pairs); 200000 seeded random six-slot
    contacts with coefficients in [-9,9] (random.Random(20261106)).
K3. Blind consequence on the public word (residues are (0,0,0,0,0,2) and
    slot 6 returns): in each of the ten runs the number N6 of admitted
    contacts on pairs containing slot 6 is 0 mod 5, S=sum of Q(d) over
    admitted contacts is 0 mod 5, and every admitted contact inside slots
    1..5 has Q(d)=0 mod 5.
K4. Count phase at a common counter. At t=-2 the runs of w and sigma share
    start, complete end and 322 attempted contacts, with 135 and 123
    state-changing contacts: difference 12 = 2 mod 5. Mirror at t=+2; equal
    counts at t=-1,0,1. (Known from the public table; replay only.)
K5. Open test, both outcomes recorded. Edge weight W=(N,A,B) mod 5 with N=1
    for a state-changing contact and (A,B)=(A(d),B(d)) for an admitted one.
    Holonomy space H = span of spanning-tree defects of W on a contact orbit
    graph (all pairs of the bank as generators). K2 predicts H inside
    V={2a+b=0}. Hypothesis H_AREA: on closed loops the count phase is a
    mod-5 linear function of the area vector, N = kappa*a with one kappa.
    Carriers, frozen: (i) the single loop w * sigma^-1 at I_-2 (difference of
    the two run totals); (ii) the complete six-slot orbit of I_0; (iii) the
    six-slot orbits of I_1 and I_-2, breadth first, capped at 200000 states;
    (iv) the three-slot orbits of all 343 triples from
    {0,1,2,u,-u,B0,-B0}, B0=1-j^2, capped at 200000 states each.
    Secondary, reported only: the same with N counting every admitted contact.

### Part D

[O1 omitted from this public extract: Part D, a third part on the D3 lattice
carrier. It lies outside reservation #1922. See PROVENANCE.md.]

## 2. Code

recon_native_u_2026-11-06.py, recon_contact_phase_2026-11-06.py,
recon_d3_loops_2026-11-06.py: Python standard library only, exact integers
and Fractions, no float in any assertion, own code paths (no import from the
repository). Environment LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1
PYTHONHASHSEED=0 TZ=UTC, python3 -I -B.

## 3. Carrier and data

Native U: all 15625 origin-zero states, counters 0..64, formulas to 4096.
Contact: the public WORD.txt of PR #1908, read as input only; the orbits in
K5. [O2 omitted: the Part D carrier.] No external data, no fitting, no alpha target.

## 4. Systematics

One architecture (x86_64), one session, so every computed statement is at
most candidate-C; written proofs are candidate-T pending independent review.
K4 is a replay of a published table, not a prediction. The orbit caps in K5
make (iii) and capped cases of (iv) lower bounds on dim H only. The weight N
(state-changing count) is the declared primary; no other weight is tried.
[O3 omitted: one sentence on Part D.]

## 5. Failure thresholds

F-U: a state, tick or window violating any of U1..U6 fires that clause; in
particular two origin-zero trajectories with different lifted shifts over a
common window n0>=3 fire U3 and refute the reading.
F-K1: any endpoint or count mismatch. F-K2: one admitted contact with
Q(d) != psi' - psi mod 5. F-K3: one run with N6 or S nonzero mod 5.
F-K5 (falsifier of H_AREA): a closed loop with (a,b)=(0,0) and N != 0 mod 5,
equivalently dim H = 2 on one connected orbit, or two loops with different
kappa. If no orbit shows count holonomy at all, the count phase is exact
there and H_AREA is void on that orbit; that outcome is recorded as such.
[O4 omitted: the two Part D thresholds.]
Thresholds are not moved after the run; a fired falsifier is kept.

## 6. Layer

L1 only (state arithmetic on declared carriers). No physical calibration,
no Planck action, no electromagnetic phase and no alpha value is asserted.
