# Compact six-coordinate forward-membership certificate

Variables are `a,b,c,y,x`; put `z=xy`, `q=z-1` and
`S_n=1+z+...+z^(n-1)`.  Sources, in frozen raw order, are

```text
R0=01:00:00, R1=01:02:02, R2=02:08:05,
R3=02:12:13, R4=02:13:22, Rq=unit_phase=q.
```

The dependency-free checker expands every line below, tracks its full
six-entry coefficient vector, reconstructs the claimed polynomial from the
raw sources, and finally verifies the five resulting vectors against the
reduced complex Gröbner basis.

First remove only powers of `xy`:

```text
A = R0 = 2c^2-1
B = R1-q(2b^2 S3+2a^2 S18) = 2a^2+2b^2-1
C = x^3 R3-q ab(S4+x^10 S3) = ab(1+x^10)
D = x R2-q ab(S3+x^2 S18) = b T
E = x^6 R4-q(bc x^11 S14+b^2 S10+a^2 x^4 S5)
  = bc x^11+b^2+a^2 x^4
T = c x^11+a(1+x^2).
```

The following small residuals certify the units needed for legal
cancellation inside the *raw* ideal:

```text
Hb = -2 y^4[c x^11+b(1-x^4)]
Ub = b Hb-1 = x^4 y^4 B-2y^4 E+S4 q
T  = Hb D-T Ub

Ha = -2c y^11(1+x^2)
Ua = a Ha-1 = -2c y^11 T+z^11 A+S11 q

Hr = -2ac y^11,  r=1+x^2
Ur = r Hr-1 = Ua.
```

Now `s=1+x^10`, `phi=x^8-x^6+x^4-x^2+1` are obtained without
saturation:

```text
as  = Hb C-(as)Ub
s   = Ha(as)-s Ua
phi = Hr s-phi Ur                    [s=(1+x^2)phi]
```

For `P=x^7-2x^5+3x^3-4x` and `g0=a+cP/5`,

```text
q0   = T-cxs = a(1+x^2)-cx
r g0 = q0+(cx/5)phi
g0   = Hr(r g0)-g0 Ur.
```

For `Q=3x^7-x^5-x^3-2x`, `g1=b+cQ/5`, set

```text
F  = E-bT
L0 = B/2-F-A/2
H  = x^10-6x^8+6x^6-6x^4+x^2+25
W  = -5ax^2+5a+cx^9-6cx^7+6cx^5-6cx^3+6cx
Z  = -(1+x^2)W g0/5 + phi H A/50 + H phi/50
   = a(1+x^2)g1-L0
a g1 = Hr(L0+Z)-(a g1)Ur
g1   = Ha(a g1)-g1 Ua.
```

The remaining basis elements are direct:

```text
g2 = A/2 = c^2-1/2
g3 = (y-g3)q+y phi = y+x^7-x^5+x^3-x
g4 = phi.
```

The expanded representation vector is deliberately not tracked as a file.
It is 233819 canonical JSON bytes with 9899 nonzero terms and SHA-256
`541295971b4ebf3f221fd65e4435a9801b8c9e760c43191340ca17d6c281034b`;
the checker regenerates and verifies it in memory from this compact DAG.
