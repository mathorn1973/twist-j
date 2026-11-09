# Exact conjugation, guards and stepwise account

NON-CANONICAL / L1. This analytical addendum expands the existing proof;
it changes no law, carrier, preparation, reader, threshold or theorem scope.
The [frozen PROOF.md](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/PROOF.md)
and all frozen scientific sources remain unchanged. No scientific execution
or symbolic-computation run was used to write this expansion. Independent
acceptance of the all-parameter argument is a separate review decision.

## 1. Coefficients determine conjugation and every account exactly

Work in O=Z[j], Phi5(j)=1+j+j^2+j^3+j^4=0, with basis 1,j,j^2,j^3.
Conjugation sends j to j^4, j^2 to j^3 and j^3 to j^2. Substituting
j^4=-1-j-j^2-j^3 gives, for z=c0+c1*j+c2*j^2+c3*j^3,

    conjugate(z)=(c0-c1)-c1*j+(c3-c1)*j^2+(c2-c1)*j^3.

This is the coefficient map in the
[frozen verifier at line 74](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/verify.py#L74).
Here is also a complete multiplication rule. Set a4=b4=0 and
p_k=sum_(0<=i,l<=3, i+l=k mod5) a_i*b_l for k=0,...,4. Then the product's
four coefficients are (p0-p4,p1-p4,p2-p4,p3-p4): first use j^5=1, then
eliminate j^4. Equivalently, the
[degree-reduction implementation at line 61](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/verify.py#L61)
forms the degree-six convolution and, for degrees 6,5,4 in that order,
subtracts the current degree-d coefficient from degrees d-4,...,d-1.

Put phi=-j^2-j^3, so phi^2=phi+1 and j+j^4=phi-1. Define

    s0=c0^2+c1^2+c2^2+c3^2,
    s1=c0*c1+c1*c2+c2*c3,
    s2=c0*c2+c0*c3+c1*c3.

Expanding z*conjugate(z) groups the six off-diagonal products into
s1*(j+j^4)+s2*(j^2+j^3). Therefore

    h(z)=z*conjugate(z)=(s0-s1)+(s1-s2)*phi.

In particular h(z)=A+B*phi has canonical four coefficients (A,0,-B,-B).
For any real w=A+B*phi define ell(w)=Tr_(Q(j)/Q)(w)/2=2A+B. The cell account is

    q(z)=ell(h(z))=2s0-s1-s2
        =[5*sum c_i^2-(sum c_i)^2]/2.

It is integral and q(z)>=sum c_i^2/2 by Cauchy-Schwarz, with q(z)=0 iff z=0.
Conjugation, h, ell and equality thus require only integer operations.
Equivalently ell is the degree-two real-field trace; do not halve that trace
again. A low cell 1 has q=2, not 1.

## 2. Parity and balance guards without an implicit norm test

For J=1+j^2, Jinv=-j-j^2, rho=j^2 and W=J*rho, direct reduction gives

    J*Jinv=-(j+j^2+j^3+j^4)=1,
    g=h(J)=2+j^2+j^3=2-phi,
    g^(-1)=1+phi,  (2-phi)*(1+phi)=1,
    W=-1-j-j^3.

Both real embeddings of g are positive; g!=1 and g^2!=1. If h(u)=A+B*phi,

    g*h(u)=(2A-B)+(B-A)*phi,
    g^(-1)*h(u)=(A+B)+(A+2B)*phi.

Thus balance is equality of two explicit integer coefficient pairs. Since
1,j,j^2,j^3 is an integral basis of O, x-y belongs to 2O exactly when all
four coefficients of x-y are even; the same applies to p-r. Only then set
c=(x+y)/2, d=(p+r)/2, u=(x-y)/2, v=(p-r)/2, all in O.

The [frozen total gate at line 109](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/verify.py#L109)
uses precisely: forward if u!=0 and h(v)=g*h(u); reverse if v!=0 and
h(u)=g*h(v); identity otherwise, including parity rejection. The nonzero
branches cannot overlap: overlap gives (g^2-1)h(u)=0, hence u=0. Each
accepted branch enters the opposite branch. The new differences remain
2Ju,2Jinv*v, or their reverse, so parity admission is preserved.
No approximate modulus, sign choice, square root or fitted tolerance enters.

## 3. Every individual cell and every marked pair

For a fixed center c define the real cross term

    K_c(w)=c*conjugate(w)+conjugate(c)*w.

If the relative value changes u -> lambda*u, where lambda is J or Jinv,
write a_lambda=h(lambda)-1 and w_lambda=(lambda-1)*u. Expansion gives

    Delta h(c+u)=a_lambda*h(u)+K_c(w_lambda),
    Delta h(c-u)=a_lambda*h(u)-K_c(w_lambda).

Their exact Delta q values are ell of the respective right-hand sides.
For h(u)=A+B*phi, the common per-cell term has ell=A-2B for lambda=J,
and ell=A+3B for lambda=Jinv; the cross contributions are respectively
+ell(K_c(w_lambda)) and -ell(K_c(w_lambda)). Apply the identical formulas
to d,v and the other multiplier. These include occupied, nonzero centers;
no interference term is dropped or assigned to an uncounted reservoir.

Let U=h(u), V=h(v). The complete local balance table is:

| Branch | Multipliers on (u,v) | Delta H of (x,y) | Delta H of (p,r) | Guard |
|---|---|---|---|---|
| Forward | (J,Jinv) | 2(g-1)U | 2(g^(-1)-1)V = -2(g-1)U | V=gU |
| Reverse | (Jinv,J) | 2(g^(-1)-1)U | 2(g-1)V = -2(g^(-1)-1)U | U=gV |
| Any refusal | (1,1) | 0 | 0 | Identity |

If U=A+B*phi, the first marked pair's Delta H/Delta E are explicitly

    forward: 2[(A-B)-A*phi],       2A-4B;
    reverse: 2[B+(A+B)*phi],      2A+6B.

The second pair has their negatives by the guard. Cross terms cancel
WITHIN each pair, so the full four-cell Delta H and Delta E are zero.
Every refusal has zero change in each individual cell. Each pair sum 2c
or 2d is fixed; hence the additive source sum S is also conserved.

## 4. Explicit source cells and local transfers in the encoder

For a=+/-1 use the frozen states

    A_a=(2a,0,W,-W), C_a=(a(1+J),a(1-J),rho,-rho),
    B_+=(2,-W,W,0), Z_a=(a(1+J),a(1-J),W,-W),
    D_a=(2a,0,rho,-rho).

In particular 1-J=-rho and h(1+J)=h(2+rho)=1+2g=5-2phi. The per-cell
accounts in source-cell order are therefore:

| Source state | Four h values | Four q values | Source H | Source E |
|---|---|---|---|---:|
| A_a | (4,0,g,g) | (8,0,3,3) | 8-2phi | 14 |
| B_+ | (4,g,g,0) | (8,3,3,0) | 8-2phi | 14 |
| C_a | (1+2g,1,1,1) | (8,2,2,2) | 8-2phi | 14 |
| Z_a | (1+2g,1,g,g) | (8,2,3,3) | 10-4phi | 16 |
| D_a | (4,0,1,1) | (8,0,2,2) | 6 | 12 |

The elementary source transitions have these exact per-cell changes.
B0/B1 rows use fixed source order (0,1,2,3), including the cyclic B1 gate:

| Transition, in the four affected cells | Delta h vector | Delta q vector |
|---|---|---|
| B0: A_a -> C_a | (2g-3,1,1-g,1-g) | (0,2,-1,-1) |
| B1: C_+ -> B_+ | (3-2g,g-1,g-1,-1) | (0,1,1,-2) |
| I: payer low, launch high -> payer high, launch low | (g-1,g-1,1-g,1-g) | (1,1,-1,-1) |

Reverse transitions negate the relevant row; refusals give four zeros.
For I the cell order is (x2,x3,p0+,p0-). The third row funds C_- -> Z_-
at tick 1; its inverse funds Z_- -> C_- at tick 2 and A_a -> D_a at tick 3.
A conveyor low/high swap has the SAME third row in its own four-cell order.
Its reverse has the negative row. This applies to data AND clock contacts.

## 5. All first-three-tick layer boundaries, with both rails counted

Let d,h>=1, L=2d+h+3, m=2L and P=2L+4. Then L>=6, so none of the
displayed rail indices wraps. Here h is the integer hold parameter;
h(z) above remains the Hermitian account function. A rail low pair costs
(H,E)=(2,4), a high pair (2g,6). HIGH/LOW name the trace costs, not
an ordering of h at one real embedding. The complete data subtotals are

| Number k of high data sites | H_data | E_data |
|---:|---|---:|
| 0 | 4L | 8L |
| 1 | 4L+2-2phi | 8L+2 |
| 2 | 4L+4-4phi | 8L+4 |

At EVERY layer the clock contains one high and 2P-1 lows, giving
H_clock=4P+2-2phi and E_clock=8P+2. Its occupied background is never removed.
The following table gives every prefix; listed sets are high DATA SITE
indices, so they determine k and the preceding exact subtotals. The final
column is the high CLOCK SITE index. Source accounts are the explicit table
in section 4. No B0, B1, interface or conveyor boundary is omitted.

| Prefix | Source + | Data highs + | Source - | Data highs - | Clock high |
|---|---|---|---|---|---:|
| Initial | A_+ | {0} | A_- | {0} | 0 |
| Tick 1, B0 | C_+ | {0} | C_- | {0} | 0 |
| Tick 1, B1 | B_+ | {0} | C_- | {0} | 0 |
| Tick 1, I | B_+ | {0} | Z_- | {} | 0 |
| Tick 1, K0 | B_+ | {1} | Z_- | {} | 1 |
| Tick 1, K1 | B_+ | {2} | Z_- | {} | 2 |
| Tick 2, B0 | B_+ | {2} | Z_- | {} | 2 |
| Tick 2, B1 | C_+ | {2} | Z_- | {} | 2 |
| Tick 2, I | C_+ | {2} | C_- | {0} | 2 |
| Tick 2, K0 | C_+ | {3} | C_- | {1} | 3 |
| Tick 2, K1 | C_+ | {4} | C_- | {2} | 4 |
| Tick 3, B0 | A_+ | {4} | A_- | {2} | 4 |
| Tick 3, B1 | A_+ | {4} | A_- | {2} | 4 |
| Tick 3, I | D_+ | {0,4} | D_- | {0,2} | 4 |
| Tick 3, K0 | D_+ | {1,5} | D_- | {1,3} | 5 |
| Tick 3, K1 | D_+ | {2,6} | D_- | {2,4} | 6 |

For clarity, the full-tick subtotals, before adding the SAME clock subtotal,
are explicitly (H_source,H_data; E_source,E_data):

    Initial, both: (8-2phi, 4L+2-2phi; 14, 8L+2).
    Tick 1, +:    (8-2phi, 4L+2-2phi; 14, 8L+2).
    Tick 1, -:    (10-4phi,4L;        16, 8L).
    Tick 2, both: (8-2phi, 4L+2-2phi; 14, 8L+2).
    Tick 3, both: (6,      4L+4-4phi; 12, 8L+4).

Every prefix in the table has total H=12L+28-6phi, E=24L+50 and S=2a.
The tick-1 negative interface borrows two E units from the launch pair;
tick 2 returns them. At tick 3 both sources pay two units to the data rail.
Every movement of either rail's high site is itself a balanced local swap.

## 6. Universal continuation, not endpoint inference

For any raw integer state let z^(r) denote its state after layer r of
F=K1_joint K0_joint I B1 B0. Section 3 gives Delta H=Delta E=Delta S=0
for EACH B, including every occupied-state or rejected branch. Unchanged
cells contribute zero; disjoint blocks add to zero inside each K layer.
Consequently sum_(r=1..5)[H(z^(r))-H(z^(r-1))]=0, with every summand zero;
the same holds for E and S. The clock's B blocks participate in these sums.
Induction applies to every subsequent tick, including returning signals,
source reactivation and complete recurrence. It does not depend on the
initial code, the first three ticks, finite test counts or endpoint matching.

The [frozen layer implementation at line 279](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/verify.py#L279)
and [boundary audit at line 402](https://github.com/mathorn1973/twist-j/blob/015c6b6f68cb8e005f0833f8a1f6f71b051215a1/probes/P-J-SIGN-REMOTE-HOLD-1/verify.py#L402)
check that already defined law; the algebra above supplies the universal
conservation proof. It does not identify these accounts with measured
physical energy, derive native-U dynamics, or turn regional delay memory
into a stationary latch. The supplied geometry, stock, clock and reader
remain premises. This exposition changes none of the frozen outputs.
