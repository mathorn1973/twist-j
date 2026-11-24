# A complete bounded stock audit and an exact account-22 separator

**NON-CANONICAL / L1. Conditional analytical candidate-T.**

This additive note keeps the receiver word and reading fixed:

    W=[C_(p,R), C_(p,q)]^5,
    (p,q)=(j^b,-j^b), b=0,...,4,
    output=Q(R_out).

A stock R in O=Z[j] succeeds exactly when the five outputs are pairwise
distinct. There is one common stock for all five inputs, no conditional
choice of the contact word, and no substitution of a phase label for the
actual final stock account. This is a restricted optimization over this
word, preparation family and quadratic output, not global receiver or
apparatus optimality. Earlier receiver-source bytes and outcomes stay fixed.

## 1. The finite coefficient bound is complete

For the four power-basis coefficients c of a stock,

    Q(c)=(5 sum_i c_i^2-(sum_i c_i)^2)/2=c^T G c,
    G=(5I_4-11^T)/2,
    G^-1=(2/5)(I_4+11^T).

In particular (G^-1)_ii=4/5. Cauchy-Schwarz in this positive definite
metric gives

    c_i^2 <= (e_i^T G^-1 e_i)(c^T G c)=(4/5)Q(c),
    Q(c) >= 5 c_i^2/4.                                  (B1)

Thus Q(c)<=32 implies c_i^2<=128/5<36. Every integral coefficient lies
in [-5,5]. Enumerating that entire four-dimensional box and filtering by
Q<=32 is therefore a complete finite decision over every stock of those
accounts, not a heuristic search radius. Equality in the real-coordinate
bound occurs when the other three coordinates are c_i/2; for example
(5,2,2,2) has Q=32, so a smaller coordinate cutoff would be unsafe.

A prospective exact census using this bound can establish that no stock
of account below22 succeeds. Together with the hand witness below this
would establish the exact restricted minimum22. That census conclusion
must be tied to its actual frozen run; it is not borrowed from an informal
review or asserted here as an already executed computation. A separate
analytical-minimum draft, if accepted, has its own proof review status.

## 2. A separator constructed by hand before enumeration

Take the fixed stock

    T=1+2j-2j^3=1+2a,       a=j-j^3.

Its four coefficients are (1,2,0,-2), so Q(T)=(5*9-1)/2=22. Also
Q(a)=5 and Q(1+a)=7. Since T modulo2 is1, the first accepted stock
contact for input j^b occurs at block k=2b modulo5. Before that hit the
balanced source pair rotates by rho=j^2. At the hit p=1,q=-1; subsequently

    R_n=1+a+rho^n a,       p_n=1+a-rho^n a.

Both a and 1+a are nonzero modulo2. Thus, for n=1,...,4, the intervening
balanced contact refuses, since (1-rho^n)a is nonzero in O/2O=F16.
The final stock has n=5-k. At n=5 the following balanced contact can
admit again but does not change the already returned stock.

The exact cyclic five-coefficient product is

    (1+a) abar=2-j^2-j^3+j^4-j^2
              =2-2j^2-j^3+j^4,
    coefficients (2,0,-2,-1,1), sum0.

For any cyclic coefficient vector w, Tr(w rho^-n)=5w_(2n mod5)-sum w.
Therefore

    (Q(R_1),...,Q(R_5))=(2,17,12,7,22),
    (output_b)_(b=0,...,4)=(22,12,2,7,17).               (B2)

All five outputs are distinct. The stock transfers respectively
0,10,20,15,5 units of the conserved Q account to the source pair. The
actual contact backreaction is retained. Reversing the ten contacts with
C^4 restores the complete pointer and stock and erases the new output.

A second useful representative is S=2-2j+j^2, also of account22.
Multiplication by j^3 gives 1+2j^3-2j^4, whose response is
(22,2,17,12,7). Undoing that common frame rotation gives the response

    S: (12,7,22,2,17).                                  (B3)

These are exposed hand derivations, not outputs from an unrecorded search.

## 3. Complete accounts and relative-frame covariance

For the known-port native clock experiment of RECEIVER-DYNAMICS.md, the
clock account4 plus stock22 gives account26. Adding a completely retained
neutralizing spectator -T or -S adds22, giving48. For the original two-pair
25-state pointer, the corresponding accounts are8+22=30 and52 with the
neutralizing spectator. No earlier account32-stock result is overwritten.
These prices concern the specified finite apparatus, not its physical
realization, clock duration, global minimum or endlessly reusable storage.

For every unit u=+j^s or -j^s, the complete ordinary contact obeys

    C(up,uq)=u C(p,q).

Admission and refusal are preserved because u is an integral unit and
p-q lies in2O exactly when u(p-q) does. The admitted linear formula then
commutes with u, and the refused identity does too. The same covariance
holds for the literal whole word and its complete inverse. Q(ua)=Q(a).
Simultaneously rotating all input, stock and retained reference slots by u
therefore leaves every quadratic output and complete account unchanged.

For a stock-only rotation R_s=j^s R while the input frame j^b is kept fixed,
the precise response rule is

    output_(R_s)(b)=output_R(b-s mod5).                  (B4)

Do not infer the analogous fixed-positive-input rule for a stock-only
minus sign from simultaneous covariance; that is a different comparison.

Any successful R is nonzero. Its five stocks j^s R are distinct, have the
same Q, and all succeed, with permuted response tables. If two were equal,
(j^(s-t)-1)R=0 in the field would force s=t modulo5. Because the response
is injective, these permutations change the fixed-frame readings.
Consequently minimizing stock Q alone cannot select one of these five
relative phase frames. This is a restricted no-selection statement for
the fixed word, readout and Q-only objective, not a no-go for physical
receivers or for another independently supplied coupling rule.

The operational next step remains a law for the complete relative
source/receiver preparation and coupling, or a proof that all complete
predictions are gauge invariant. A cheaper stock does not supply that law.
