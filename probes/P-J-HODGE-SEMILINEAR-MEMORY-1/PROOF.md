# Semilinear Hodge reading and one-scalar predictive memory

**L1 proof submission. No Canon promotion or physical interpretation.**

All notation is frozen by PREREG.md.

## 1. Why Hodge twists only the primary plane

On the rational primary plane im(T), the J-Hodge step has characteristic
polynomial
```text
X^2-3X+1,
```
while the Hodge involution exchanges its two reciprocal eigendirections.
Hence conjugation by Hodge inverts the primary step:
```text
K L K^-1 T = L^-1 T.
```
On the periodic mixed-plane sector im(R), the two plane stretch factors cancel
and Hodge commutes with L:
```text
(KL-LK)R=0.
```
The verifier checks both rational matrix identities directly.

## 2. The present Hodge triple is semilinear

Choose the deterministic column basis B_+ of P_+ used by the verifier and its
entrywise Galois conjugate B_-=sigma(B_+). Since sigma(P_+)=P_-, these are
bases of W_+ and W_-.

For any rational w, if
```text
P_+ w=B_+ x,
```
then rationality of w gives
```text
P_- w=sigma(P_+w)=B_- sigma(x).
```
Since P_++P_-=I,
```text
w=B_+x+B_-sigma(x).
```
The verifier checks that this map F^3 -> W_Q is a Q-linear bijection by the
six Q-basis vectors e_i and sqrt(5)e_i.

Projecting one J-step back to W_+ gives
```text
P_+Lw=P_+LB_+x+P_+LB_-sigma(x).
```
Writing the two terms in B_+ coordinates defines exact F-linear matrices A,B:
```text
x'=Ax+B sigma(x).
```
The one-step Hodge cross rank is one, hence rank(B)=1.

Because B is nonzero and sigma(sqrt(5))=-sqrt(5), choose x with
B sigma(x)!=0. Then
```text
S(sqrt(5)x)-sqrt(5)S(x)=-2 sqrt(5) B sigma(x) != 0.
```
So S is not F-linear. It is Q-linear, with the nonlinearity over F exactly one
rank-one conjugate channel.

## 3. One additional scalar linearizes the future

Let t span im(P_- L P_+), and take the basis
```text
E=(B_+ columns, t)
```
of E_J. The accepted cross-rank theorem gives dim_F E_J=4. In this basis,
the present output is simply
```text
O=(I_3  0).
```
The verifier constructs the exact 4x4 restriction C_E of L and checks
```text
rank [ O ; O C_E ] = 4.
```
Thus this four-state realization is observable from its fixed output and
attains the accepted future rank. Any F-linear exact realization producing
the same full family of future outputs has dimension at least that observable
rank, namely four. This is the stated linear minimality and no stronger
set-theoretic claim.

## 4. The extra scalar may be one past value of the primary axis

T commutes with the Hodge split. Restricted to W_+, its matrix T_+ is a
rank-one projector. Any nonzero row in its row space defines the frozen axial
output y; its kernel is exactly the two-dimensional periodic part of the
present Hodge triple.

The primary factor X^2-3X+1 implies, on every trajectory,
```text
y_(n+2)=3y_(n+1)-y_n.
```
The verifier checks the stronger matrix identity
```text
y (C_E^2-3C_E+I)=0.
```

At time n, the previous axial value is the row
```text
y C_E^-1
```
applied to the current four-state vector. The verifier checks
```text
rank [ O ; y C_E^-1 ] = 4.
```
Therefore the present three-coordinate Hodge output plus one scalar from the
previous step determines the entire fixed-J predictive state uniquely and
linearly.

## 5. Lucas/Fibonacci coefficients

Choose a nonzero rational vector v in im(T), and split it by Hodge:
```text
h_+=P_+v,  h_-=P_-v=sigma(h_+).
```
They form a conjugate basis of the primary plane. The primary step has
determinant one, trace three and Hodge conjugation sends it to its inverse.
Therefore its diagonal entries in this conjugate Hodge basis are both 3/2.
The off-diagonal product is 5/4, and Galois conjugacy makes each
off-diagonal coefficient a marked sign times sqrt(5)/2. Thus
```text
self coefficient       = 3/2 = L_2/2,
conjugate coupling     = +/- sqrt(5)/2 = +/- sqrt(5) F_2/2.
```
The marked rational vector fixes the signs before execution.

## 6. Boundary

For a single fixed J, the rank-one conjugate channel explains exactly the
jump from present dimension three to F-linear predictive dimension four.
Under arbitrary interleaved A5/J future words the accepted minimum is six,
so the four-state closure depends on the fixed-axis choice.

Nothing here intertwines native U with L. The counter/carry factorization may
supply a missing unbounded exponent resource, but that is a separate theorem.
Calling the negative chart direction physical time remains a reading.
