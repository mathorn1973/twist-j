# Scalar semantics and scope of the witness

NON-CANONICAL / L1. This note explains the exact law audited by the frozen
verifier. It does not assume the claimed success of WORD.txt.

## Two integral coordinates

O=Z[j]=Z[T]/(1+T+T^2+T^3+T^4) has the basis 1,j,j^2,j^3.
Multiplication by j sends (a,b,c,d) to (-d,a-d,b-d,c-d).
Alternatively use Z^5 modulo the common all-ones vector. The unique gauge
with fifth coefficient zero maps (a0,...,a4) to
(a0-a4,a1-a4,a2-a4,a3-a4,0). Multiplication by j^2 is cyclic rotation
by two before gauge normalization. These descriptions are integrally
isomorphic, so membership in 2O is exactly coefficientwise evenness in
the power basis and its fifth-zero gauge. No rounding or tolerance is involved.

The verifier deliberately uses a different canonical gauge in its cyclic
route: subtract the minimum coefficient. In that gauge a class belongs to
2O precisely when all five coefficients share the same parity. For the
difference delta=x-y, admission therefore tests delta_i-delta_0 even.
The coefficient vector x+y has the same parities as delta. Rotation of a
common-parity delta preserves those parities, so both numerators
x+y+rotate_2(delta) and x+y-rotate_2(delta) are coefficientwise even.
Divide these numerators by two before minimum-zero normalization. This
implements the same integral contact without converting through the power
basis, even when delta itself has five odd coefficients.

For coefficients a0,...,a4 the half trace is

    Q(a) = Tr(a*conjugate(a))/2
         = (5*sum(a_i^2)-(sum(a_i))^2)/2
         = sum_{i<k}(a_i-a_k)^2/2.

The numerator is even. The form is unchanged by adding a common integer
to all five coefficients and is positive definite on the quotient.
Setting j=1 identifies O/(1-j) with Z/5, so the residue is sum(a_i) mod 5.

## Total contact and inverse

For an admitted pair write x=s+d, y=s-d with s,d in O. One contact fixes
s and sends d to p*d, p=j^2. The new difference is 2*p*d, so admission
persists. Five contacts return d because p^5=1; a refused pair is fixed
from the outset. Thus the total contact satisfies C^5=I on all O^2 and
C^(-1)=C^4. Reversing the word and replacing every label by four copies
is therefore its literal inverse, including refusal branches.

The pair sum is 2*s. Its full Hermitian account is
2*(s*conjugate(s)+d*conjugate(d)), invariant because p*conjugate(p)=1;
taking the half trace proves conservation of total Q. The first coordinate
changes by (p-1)*d, a multiple of u=1-j, and the second changes by its
negative. Thus each labelled residue modulo u is invariant. Refusal
preserves all these quantities too.

For u=1-j, B=1-j^2 and X=1+j-2*j^3, Q(u)=Q(B)=5, Q(X)=15 and Q(2)=8.
Both prescribed endpoints therefore have total Q=10*t^2+33 and the same
ring sum 2*u+X+2. These necessary accounts alone do not prove reachability;
the entire word must be replayed with exact six-slot endpoint equality.

## Exchange symmetry

Let sigma exchange slots 1 and 2. The contact law is symmetric in its two
arguments. Conjugating every labelled contact by sigma gives the contact
on the exchanged unordered pair. Consequently

    sigma(I_t)=I_(-t), sigma(G_t)=G_(-t),
    sigma(I_t.W)=I_(-t).sigma(W).

Any successful common W therefore gives a successful common sigma(W).
The verifier also checks the correspondence of chronological admission
traces and complete endpoints. Sorting an exchanged pair changes no
orientation convention because the same law acts on unordered addresses.

## Meaning of a successful replay

The fixed program sees only slot values through the fixed admission rule;
it does not inspect a separate t variable or choose a program by input.
Admission/refusal and the admitted arithmetic together realize the
conditional evolution. The external contact schedule is still supplied.
This does not construct an autonomous clock or an input-preparation
mechanism, and neither schedule length nor Q is identified with measured
physical action or time by this finite L1 witness.

A successful certificate bounds the shortest possible word above by 322.
It provides no lower bound or minimum. Search histories, macro minima and
large stabilizer orbits are not needed to establish this finite existence
claim and are deliberately outside the new computation.
