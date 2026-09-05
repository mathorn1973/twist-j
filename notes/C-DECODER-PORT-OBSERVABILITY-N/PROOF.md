# Source observability of the chosen reservoir readout

**Status: candidate-T / NON-CANONICAL / L1 ONLY.**
Author: A. M. Thorn. Session PUBLIC-BRIDGE-REVIEW-20260905.
No public probe, physical certificate, status promotion, or priority claim.
The local preregistration and its hash were recorded before execution. This
Git handoff is packaged after execution and is not an immutable public pre-run pin.

## 1. Inputs and output equality

Use the exact public D3 scalar transport, its complete shells and its chosen
five-site source, at public main 8ea01cd36ade943af10718593b0e1348d6837a3b.
Write H=2I-L and

    y0=(0,0,0), y1=(1,1,0), y2=(1,0,1), y3=(0,1,1), y4=(2,0,0),
    s=z0+z1+z2+z3,
    S(z)=sum_(i=0)^3 (zi-s/5) delta_yi - (s/5) delta_y4,
    G=I-11^T/5,  P0=(0,S(z)),  E(P0)=z^T G z/2.

The source domain for the linear claims is Q^4. It contains the public
balanced subset {-2,-1,0,1,2}^4 but is not a newly admitted physical source class.
For cold input the next wave and signed outgoing value at a port x are

    w_x=[(Hv)_x-(1-g_x/2)u_x]/(1+g_x/2),
    b_x=-(w_x-u_x)/2.

The observation is the ordered signed outgoing port sequence. Its equality
is entrywise equality. It excludes the source header, the complete residual
wave, and inaccessible apparatus-state snapshots. Equal port observations
therefore do not mean equality of complete model states or archived provenance.

## 2. One origin port: exact two-dimensional invisible source space

Assume R={0} and g>0. Then the all-time signed observation map has kernel

    W={z in Q^4: z0=0 and z1+z2+z3=0}.

**Inclusion W in the kernel.** The full shell operator commutes with every
signed coordinate permutation. A sole origin port and observation there have
the same symmetry. By linearity, the response to delta_y1, delta_y2 and
delta_y3 is identical at every cut: the three sites are in one coordinate
permutation orbit. The coefficients of delta_y0 and delta_y4 depend only on
z0 and t=z1+z2+z3. Thus the entire signed observation depends on only z0,t.
On W, both coefficients vanish and the remaining three coefficients sum to
zero. Every outgoing value is zero. This argument is an induction for the
actual damped evolution, not merely a symmetry of the free operator.

**No larger kernel.** Put

    a(z)=(H S(z))_0,
    c(z)=((H^2-2I)S(z))_0.

Exact shell sums give the row vectors

    a=(1421,-349,-349,-349)/1620,
    c=(-53999/87480,4757/29160,4757/29160,4757/29160).

The first two outputs are

    b0=-a(z)/(2+g),
    b1=-[c(z)-g*(10/9)*a(z)/(2+g)]/(2+g).

Their row span is the span of a,c for every g>0. On the two variables z0,t,

    det[[a0,a1],[c0,c1]]=8959/885735 != 0.

So b0=b1=0 implies z0=t=0, proving the exact kernel statement for every
positive rational g. The same algebra and symmetry argument also hold for
positive real g on the corresponding real finite-support extension; no
physical real-parameter identification is inferred.

**Nonzero balanced control.** Take z=(0,1,-1,0). Its source is

    S(z)=delta_(1,1,0)-delta_(1,0,1),
    z^T G z=2, E(P0)=1.

All signed origin outputs, deposited heat and threshold counts are zero for
all cuts and every positive threshold. The whole residual wave energy remains
one by the public energy identity. Thus this observation cannot distinguish
this nonzero balanced source from zero. Changing only the threshold or
waiting longer cannot restore the missing distinction. This says nothing
about observation of the complete wave or another port arrangement.

## 3. Four first-cut signed ports: exact source reconstruction

Choose R={y0,y1,y2,y3}, independently marked in that order, with arbitrary
positive rational conductances g0,g1,g2,g3. Define

    D=diag(2+g0,2+g1,2+g2,2+g3),
    v=(349,354,354,348)^T,
    M=(1770 I-v 1^T)/1620.

The first cold signed vector obeys b=-D^(-1)Mz. To compute M, restrict H S
to these four sites. H has diagonal 10/9 and shell entries w_n/324.
Subtracting one fifth of each five-site row sum gives

    1620 M = [[1421,-349,-349,-349],
              [-354,1416,-354,-354],
              [-354,-354,1416,-354],
              [-348,-348,-348,1422]].

Since 1^T v=1405, the determinant and inverse are

    det M=1770^3*365/1620^4=14992667/51018336 != 0,
    M^(-1)=(54/59)(I+v 1^T/365),
    z=-(54/59)(I+v 1^T/365)D b.

The first signed four-port record therefore reconstructs all four rational
source coefficients. In particular, it separates every balanced source.
No threshold or probability is needed. The calculation does not reconstruct
the full autonomous head (n0,x0), which contains additional data.

Four scalar coordinates are necessary for a linear injective single-cut
observation on Q^4. This is not a minimality theorem for the number of ports
when several cuts, another geometry, or nonlinear observations are allowed.
The value g_i=2 in the local tests is an illustrative mathematical context,
not a selected physical conductance or an extra fundamental constant.

## 4. Squaring is a different observation

With g_i=2, choose q=(1,1,0,0)^T, q'=(1,-1,0,0)^T, and
z=M^(-1)q, z'=M^(-1)q'. Their first signed vectors are -q/4 and -q'/4.
Their first deposited-energy vectors are identical, namely

    (1/8,1/8,0,0).

Yet the algebraic QDD LOW weights after normalization are respectively
313290/380329 and 0. These are rational-domain controls, not two asserted
balanced preparations. They have different total source energies, so adding
an independently observed total energy may distinguish this particular pair.
The claim is only that the four first-port deposits alone do not reconstruct
the signed source or its QDD weights. Later heats are not claimed identical.
Global sign loss alone would be weaker, because QDD also identifies z and -z.

## 5. Local checking and status

The exact script uses only integers and Fraction. One construction enumerates
all displacement triples by squared norm and forms matrix products. A second
uses signed permutations of shell representatives and independently written
sparse evolution. The first two origin transitions and first four-port
transition are checked on every source basis vector at g=1/2,2,5. Two dark
basis sources are additionally checked for three steps. Those finite checks
support the algebra; the all-time assertion rests on the symmetry proof.

This is one author on one local x86_64 lane, not blind two-agent confirmation
or the repository's two-architecture procedure. The complete local output is
RESULT.txt. A later public probe requires a new reservation, immutable
preregistration/readback, source exposure disclosure, and the public runners.
Do not treat this package or its SHA256SUMS as a public gate receipt.

## 6. Physical boundary

The selected source and stencil are existing dictionary inputs. This proof
makes no physical source identification, no statement that these ports exist
in the NIST apparatus, no photon or polarization claim, no outcome exclusivity,
no Born frequency theorem, no SI scale, and no full apparatus-class claim.
Signed source reconstruction is a diagnostic bridge inside a chosen model.
It does not defeat the separately registered nonnegative QDD-postprocessing
obstruction or modify the frozen A/U5 incidence route.
