# C-H3-NATIVE-COINCIDENCE-N

NON-CANONICAL / NO AUTHORITY. L1 mathematical and finite H3 results.
Reservation #2113, result-exposed successor D declared separately in
comment 7220227085 before its calculation. The original targets are
retained. Public Canon v117 base 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.
Predecessor draft #2112 at 85c17c40506645f18a7ee699cbdc78bb4e2efc0e.
No formal public probe or cross-layer claim.

## 1. Target and scope

The previous paired address carrier implements the cyclic action
on the dual integral bases X_r=K^r(j^2), Y_u=W^u(-j^2) by a fixed
mathematical code, with ell(X_r Y_u)=delta_(r,u). Its unmodified
radiation is blind to the independent address choices. Here the
target is an actual native value written by the H3 law, not another
external coefficient extraction.

Use O=Z[j], Phi5(j)=0, rho=j^2, J=1+rho, h(z)=z conjugate(z),
T=h(J), and m=8. Set transport coefficients A=J/2 and B=(1-rho)/2.
The letters A and B in this formula are coefficients, not new
contact operators or branch names.

The carrier is the 8 by 8 torus, matching bit zero, faster b=1
background of #2112, with marker columns 0 and 7 (neighbors
across the periodic boundary). The unshifted material values are
d=(-1)^y except j,j^2 at y=-2r,4-2r on column 0 and j^3,j^4 at
y=-2u,4-2u on column 7. Both phases r,u range independently
over 0..3. Opposite material rails are retained. The prior
background is CLK=0 and CORR=2J(-1)^(x+y).

For reader A use exactly the common offsets and stocks in
PREREG.md and verify.py. In particular the even-row material
differences in the two marked columns are m+p-j, m+q-j^3
where p and q are the unshifted raw material values. Their
odd-row material differences are 1. All changes to the complete
initial field relative to the previous carrier are independent
of r,u. This is a fixed, affine, common-stock measurement
preparation of those raw inputs, NOT a native coupling procedure
applied to the unmodified running motor. No future target value
or equality-dependent stock is provided. Evolution from the
initial state is exactly the original H3 update throughout.

## 2. A: native two-tick coincidence mark

At an even row let p in {1,j,j^2}, q in {1,j^3,j^4}, and let
a=[p=j], b=[q=j^3]. These symbols describe the initial data;
they are not an externally supplied control to H3.

The even-row cells on columns 0 and 7 have respective radiation
centers n_A=-Jm, n_B=(4-J)m and common initial half-difference
Jm. Here a cell (d,-d,g,c) has radiation center (g+c)/2 and
half-difference (g-c)/2. The odd rows have d=1, CLK=1, CORR=0.

For both columns the even-row material residues modulo 2
are 0 or the difference of two of the indicated roots;
none equals 1. After an active first B1 the selected
matter value is Jm, still even. Thus the relevant vertical
material C contacts refuse. CLK is even on the even rows
and odd on the neighboring odd rows, so its vertical C also
refuses. The horizontal first matching has equal CORR at
(0,1) and (6,7) in column coordinates, and consequently
does not change the supplied even-row CORR values of
columns 0,7. The odd-row B contacts refuse.

At the first B the exact norm tests select only p=j or
q=j^3 respectively. This follows by reducing the three
norms in each column in O, or by the complete finite norm
table in the verifier. B2 cannot qualify. B1 leaves each
radiation center unchanged and sends Jm to m. Hence the
post-first-B half-differences are exactly

    f_A=m(1+(1-a)rho), f_B=m(1+(1-b)rho).

The second horizontal C pairs columns 7 and 0, and the
difference of their two CORR values is even for every
case. The new CORR at column 0 is A*c_A+B*c_B. Its CLK
is retained. Substituting c_i=n_i-f_i and g_i=n_i+f_i,
using A+B=1 and n_A-n_B=-4m, gives the pre-second-B
half-difference at column 0:

    F=m*rho*(1+(1-a)(1+A)/2+(1-b)B/2).

The material difference is Jm if a=1, otherwise m+p-j.
For a=b=1 this is the exact reciprocal B2 balance:
h(Jm)=T*h(m*rho). The nine possible (p,q) cases have
no B1 balance at this cut, and B2 balance only for
(p,q)=(j,j^3). Both exact algorithms verify the full
nine-case norm table. B2 changes CLK by rho*F. Thus
the actual full tick-two CLK at column 0 is

    R=m(rho^2-rho)   if a=b=1,
    S=-m*rho         if a=1,b=0,
    0                if a=0.

R,S,0 are distinct. All four even rows are tested
simultaneously. Each phase has exactly one first tag,
so there is exactly one R on the fixed four-address strip
if r=u, and none otherwise. This is an actual native
distributed coincidence mark; the code does not perform
an external multiplication of input flags and write
the result. Recognizing the mark R and its presence
on the strip is still a mathematical observation.
There is not yet a native OR or a single fixed-register
output.

## 3. B and C: limits of reader A

The complete quadratic account H in the power basis
(1,j,j^2,j^3) is (13880,0,132,132), giving Q=27628,
common across all sixteen inputs. Both complete linear
sums and H are checked at every post-C and full cut
through tick 160, and every tick is inverted exactly.
This is conservative evolution, not restoration of the
original motor or physical energy metrology.

At none of 40,80,120,160 does even one of the sixteen
modified preparations equal its required translated
complete reader preparation. At 42,82,122 the expected
rotated R mask holds for twelve of sixteen each time,
not all sixteen. No recurrent comparator is claimed.

The entire fixed single-CLK binary record scan for all
sites at full cuts 2..160 finds zero candidates: no
one such register has one identical value on all four
positive inputs and a distinct identical value on all
twelve negative inputs. This is the exact finite scan,
not a general impossibility result. The equal-tag
controls (1,1,3,4) and (1,2,3,3) each yield a false
validity appearance of one R in eight of sixteen
tested preparations; the other declared controls and
the no-marker case give no R. Thus the observed mark
does not certify valid preparation outside the input
contract.

## 4. D: native third-tick cancellation and binary strip

D is a separately frozen successor, not a repair of the
failed recurrence target. Keep the two input columns and
their common offsets, but use zero material half-difference
at columns 1,2,3 and replace the stated CORR stock there.
Let

    Hstar = m*(-4-2rho-rho B).

Its exact power-basis coordinates are (-36,-4,-24,-4).
At every even row initialize the CORR pair on columns
0,1 by the inverse of the native C contact on (-2Jm,Hstar).
This gives, in power-basis coordinates,

    ((-24,-2,-22,6),(-28,-2,-18,-10)).

The difference is even and the first C maps it exactly
to the declared target. Set even-row CORR at columns 2,3
to Hstar and odd-row CORR at columns 0..3 to zero.
The rest is the frozen A preparation. B is necessarily
idle wherever the matter difference is zero, because
both reciprocal branches require nonzero differences
with equal positive Hermitian accounts after the indicated
factor. First C at (2,3) and second C at (1,2) see equal
values. Consequently the second full-cut CORR at column 1
is Hstar, independently of both inputs. The first two
ticks at columns 0,7 are literally unchanged from A;
the audit checks both local post-C and full states.

At a first-only row the second full-cut local values at
column 0 satisfy g=S=-m*rho and f=m*rho*(1+B/2). Hence

    c=g-2f=-m*rho*(3+B).

At the third C the incoming common CORR partner is Hstar.
The native horizontal C is admitted, and the new local
half-difference is (g-A*c-B*Hstar)/2. Substitution with
A=1-B and rho=1-2B gives exactly m. The existing
material difference is Jm, so the third B must be B2.
It adds rho*m to CLK and cancels S exactly.

In all other local input cases the third B is idle.
This is an exact finite verification, with all nine
local pre/post words recorded in D.txt and independently
replayed. In particular the coincident mark R is retained.
Vertical C of the data and CLK at these sites refuses,
and the third horizontal C is genuinely changing in all
nine cases. Thus the actual output at full tick 3 is

    CLK(0,y)=R*[p(y)=j and q(y)=j^3], y=0,2,4,6.

For every unequal pair all four output registers are
literally zero; for each equal pair there is exactly
one nonzero register, with the same value R. No S remains
on the strip. This is a binary-valued native local record
in four positions, not a native scalar reduction of them.

The full common quadratic account is (30472,0,7300,7300),
Q=53644. This accounts for the complete modified 256-slot
field and is not a minimal resource requirement. The
original motor's Q=1024 is not maintained by the changed
initial preparation; the new Q and H are conserved during
each evolution. Every tick through 160 is audited,
including exact inverse.

All sixteen binary strips remain exactly unchanged at
every post-C/full cut from full tick 3 through full tick
11, and also at post-C tick 12. At full tick 12 only the
four coincident cases retain their exact strip. The
certified common hold is therefore finite. No single
fixed-register binary read occurs on the scanned full
cuts 3..160. All complete translated-state return tests
at 40,80,120,160 again have zero matches. The controls
again have the same aliases as A; their strips are
binary-valued, but that is not a valid-preparation test.

## 5. Relation to the dual pairing and scientific boundary

For the sixteen declared valid inputs, presence of the
native R on the fixed strip is equivalent to ell(X_r Y_u)=1;
absence is equivalent to ell(X_r Y_u)=0 at the declared
cut. The previous address-code pairing has therefore been
connected to a native write on a *modified, supplied*
initial field with common stocks. The local AND is selected
by a real reciprocal balance using actual incoming
radiation and material differences. The auxiliary cancellation
is itself a native reciprocal contact.

The position of R when present still carries address
information; the remaining material and radiation slots
can also retain input information. This is not a
demonstration of a measurement that distinguishes *only*
the pairing in the complete world, nor a proof of
quantum coherence or a physical occurrence rule.
A zero strip has meaning only with the frozen input
contract and time context. No native completion marker,
one-port reducer, independent common-stock coupling to
a running motor, stable archival storage, nondestructive
measurement, regeneration, fresh-input renewal, or
physical energy identification is supplied.

The exact finite native witnesses and finite exclusions
are candidate-C at L1. The symbolic contact implications
are conditional elementary algebra on the specified H3
law; no adopted higher-layer statement follows.
A and D use distinct fixed common preparations. A's
three-valued output and failed recurrence remain recorded.
Both algorithms are result-exposed, not blind independent
reviewers. Architecture reproduction is informal and
does not meet the formal public scientific gate.

The next sharply delimited issue is an actual native
reduction/transfer of the distributed binary record into
one common register and its coupling to an unmodified
periodic source with a separately counted reader stock.
No RH estimate, curvature selection, native-U equivalence
or unnamed L1-to-other-layer lift is claimed.
