# Semilinear Hodge reading and normalized one-scalar memory

This is the successor of the abandoned P-J-HODGE-SEMILINEAR-MEMORY-1. The
predecessor failed only because an arbitrary conjugate primary basis was
incorrectly required to already be Hodge-normalized. The normalization used
here is part of the preregistration.

For rational w, sigma(P_+)=P_- and sigma(w)=w. If P_+w=B_+x in the frozen
plus basis and B_-=sigma(B_+), then
    w=B_+x+B_-sigma(x).
Projection after one J-step therefore gives
    x'=A x+B sigma(x),
with A,B F-linear and rank(B)=1. Since sigma(sqrt5)=-sqrt5 and B is nonzero,
this update cannot be F-linear.

The rank-one cross image im(P_-LP_+) adds exactly one scalar to the present
Hodge triple. In the basis E=(B_+ columns,t) of E_J the present output is
O=(I_3 0). The exact restriction C_E of L satisfies
    rank [O ; O C_E]=4,
giving an attained four-state F-linear realization and the standard
observability lower bound four for this frozen output.

The rational projector T preserves the Hodge split and has rank one on W_+.
A nonzero row y of that rank-one projector kills the periodic two-plane.
Because the primary factor is X^2-3X+1,
    y(C_E^2-3C_E+I)=0,
hence y_(n+2)=3y_(n+1)-y_n. Also
    rank [O ; y C_E^-1]=4.
Thus the whole predictive state is determined by the present triple plus one
previous axial scalar.

On im(T), Hodge conjugation inverts L, while on im(R) Hodge commutes with L:
    K L K^-1 T=L^-1 T,
    (KL-LK)R=0.
This is the algebraic source of the rank-one conjugate channel.

For the deterministic conjugate primary basis (h_+,h_-), rationality gives a
boost matrix [[3/2,b],[c,3/2]] with bc=5/4. This product is basis-invariant,
but b and c individually depend on the conjugate scale. The preregistered
rescaling h_-'=r h_- with
    r=(-sqrt5/2)/b
gives, by direct change of basis,
    [[3/2,-sqrt5/2],[-sqrt5/2,3/2]].
Therefore the self coefficient is 3/2=L_2/2 and the normalized conjugate
coupling is -sqrt5/2=-sqrt5 F_2/2.

The accepted full A5/J future-word result still needs six coordinates. This
four-state closure is for one fixed marked J axis only. Nothing here
intertwines native U with L or identifies the negative coordinate with
physical time.
