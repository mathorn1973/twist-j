# Origin-zero affine two-coordinate readout with a different preparation

Status: NON-CANONICAL / L1 / candidate-T.

This is a new preparation family. It does not modify the fixed family,
proofs or quadratic minimum of PR #1536, and it does not change the
native U or Canon v101. All arithmetic is in F5.

## 1. Exact native law

Use checkpoint coordinates x=(a,b,c,d,q,r), trace
z=a+b+c+d+q+r, and selector g_(z+2 theta_n), where
theta_n=popcount(n) modulo 2. The five unchanged generators are

    g0(x)=(b,a,d,c,q,r),
    g1(x)=(-c,-d,-a,-b,-q,-r),
    g2(x)=(2-c,1-d+r,2-a,1-b-r,1-q,-r),
    g3(x)=(2-a,1-b,3-c,4-d,1-q,1-r),
    g4(x)=(2-a,1-b,3-c,4-d,2-q,1-r).

Define affine quantities

    A=a+c, B=b+d, C=a-c-2, D=b-d-1.

## 2. Preparation, reader and total decoder

For independent lambda,mu in F5, prepare once at n=0:

    r0=3(1+mu-lambda),
    q0=2-mu-r0,
    E(lambda,mu)=(3mu,3,3mu,2,q0,r0).

Equivalently,

    E(lambda,mu)=(3mu,3,3mu,2,mu+3lambda+4,3mu+2lambda+3).

Both messages are present in this stipulated initial condition. This is
an affine injection: a=3mu recovers mu, and then r0 recovers lambda.
Its two parameter directions

    v_lambda=(0,0,0,0,3,2),
    v_mu=(3,0,3,0,1,3)

are linearly independent.

Use the fixed affine reader

    R(x)=(X,H),
    X=A+D,
    H=C+z.

In original coordinates,

    X=a+b+c-d-1,
    H=2a+b+d+q+r-2.

The linear part of R has rank two: the first row is nonzero and has
zero q coefficient, whereas the second has q coefficient one. Thus R
is an affine surjection F5^6 -> F5² and can be completed to an affine
coordinate chart.

The fixed total decoder is

    delta(X,H)=BLANK             if H=0,
                 PRESENT(H²X)   if H!=0.

BLANK is a sixth distinct meaning, not PRESENT(0). The decoder is not
required to be affine. In particular this is an affine observation with
an arbitrary fixed decoder, as in the question under consideration.

## 3. Actual origin-zero prefix

Initially,

    A=mu, B=0, C=3, D=0, z=2.

The actual selector bits are theta_0,theta_1,theta_2=(0,1,1).
At n=0 the selected generator is g2. It sends z=2 to z=0.
At n=1 the selected generator is again g2. Since g2 is an involution,
x2=x0 and z2=2. At n=2 the selected generator is g4. Therefore the
common actual prefix is g2,g2,g4, without dependence on the messages.

Initially and again at n=2,

    R(x0)=R(x2)=(mu,3+2)=(mu,0),

which decodes to BLANK.

The identities for g2 are

    A'=4-A, B'=2-B, C'=C, D'=D+2r, z'=2-z.

Consequently at n=1,

    X1=4-mu+2r0
      =4-mu+(1+mu-lambda)
      =-lambda,
    H1=3+0=3.

Since 3²=4=-1, the decoded first message is

    H1² X1=(-1)(-lambda)=lambda.

At n=3, g4 sends the initial quantities to

    A3=-mu, B3=0, C3=2, D3=0, z3=1.

In particular R(x3)=(-mu,3), whose decoded message is mu.

## 4. Exact all-time tail

On the trace set z in {1,4}, the selector under either possible control
bit chooses only g1,g3,g4. More explicitly, at z=1 it chooses g1 or
g3, and at z=4 it chooses g4 or g1. Their relevant actions are

    g1: (A,C,D,z) -> (-A, C, D,-z),
    g3 or g4 when selected: (A,C,D,z) -> (-A,-C,-D,z).

The trace set is closed under both choices. It follows inductively from
x3 that, for every n>=3,

    D=0, C in {2,3}, z in {1,4}.

Moreover 2ACz is invariant under either action: g1 negates A and z,
while g3/g4 negate A and C. At x3 its value is

    2A3 C3 z3=2(-mu)(2)(1)=-4mu=mu.

Hence 2ACz=mu throughout the tail. Because C²=4 and z²=1,

    H²=(C+z)²=4+2Cz+1=2Cz.

Both C and z are nonzero, so H²!=0 and H!=0. The reader has X=A
because D=0, and the decoded tail message is therefore

    H²X=2ACz=mu

at every n>=3. The argument uses no division by A and remains valid
when mu=0, including A=0 throughout that trajectory.

This proves, for every one of the 25 preparations, the exact history

    BLANK, PRESENT(lambda), BLANK, PRESENT(mu), PRESENT(mu), ... .

The proof is by closure under both selector choices and applies in
particular to the actual infinite Thue-Morse continuation. It does not
infer infinite retention from a finite sample.

## 5. Exact finite support

For each mu, independently choose C in {2,3}, z in {1,4}, r in F5.
Set A=2Cz*mu, b=3,d=2, a=3(A+C+2),c=3(A-C-2),q=z-A-r.
These are20 distinct states per mu and100 in total; B=D=0 and2ACz=mu.
The previous closure proof includes every actual tail point in this set.
Conversely, actual times3,4,7,8 have(C,z) respectively(2,1),(2,4),(3,4),
(3,1). Varying lambda at fixedmu supplies all5 initialr values, and every
subsequent common-time r map has slope+1 or-1. Thus those actual times
already cover the complete100-point tail union across preparations.
The25 blank and25 first points have traces2 and0, so are disjoint from
each other and this tail. The exact required set contains150 checkpoints.

## 6. Exact scope and the former obstruction

The raw blank value is (mu,0). It varies with the second message across
the preparation family. The reader state returns exactly within each
individual trajectory, R(x2)=R(x0), and indeed x2=x0, but there is no
single raw ready value shared by all preparations. All blank values have
the same decoded meaning.

Thus this construction does not satisfy, and cannot contradict, the
previous common-raw-reset no-go: that theorem assumes one common R(x2)
for all message pairs. Nor does it contradict the affine impossibility
in PR #1536, which concerns a different fixed preparation family.

The distinction is substantive. Here the second message is already
present as the first raw reader coordinate at n=0, while the decoder
calls that state BLANK. No later insertion or new information is
claimed. The initial q,r values jointly encode the first message and
the second message is also carried in A. The construction only changes
the preparation, not the native dynamics or the reader over time.

The reader uses all six native coordinates across its two components,
although H alone omits c after simplification. This is a global affine
observation, not a prescribed separated receiver block or a physical
detector design. It proves no physical locality, funded contact, energy
law, transfer between disjoint sectors, source depletion or instrument
realization.

For the class that allows changing the preparation and permits only a
common decoded blank, an affine two-coordinate reader exists. A constant
reader cannot produce six meanings, so the least polynomial degree in
this class is exactly one. A single F5 coordinate has only five values,
so no one-coordinate reader, even nonlinear and followed by an arbitrary
decoder, can produce all six meanings; two coordinates are necessary
and sufficient in this class.

This proof was obtained analytically. No scientific code or old audit
was executed to obtain it.
