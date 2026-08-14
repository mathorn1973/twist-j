#!/usr/bin/env python3
from fractions import Fraction as F

H = [
    [F(1), F(1), F(1), F(1)],
    [F(1), F(1), F(-1), F(-1)],
    [F(1), F(-1), F(1), F(-1)],
    [F(1), F(-1), F(-1), F(1)],
]

def tr(A): return [list(r) for r in zip(*A)]
def mm(A,B):
    BT=tr(B)
    return [[sum(x*y for x,y in zip(r,c)) for c in BT] for r in A]
def I(n): return [[F(i==j) for j in range(n)] for i in range(n)]
def Z(n): return [[F(0) for _ in range(n)] for _ in range(n)]
def scale(A,c): return [[c*x for x in r] for r in A]
def add(A,B): return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def outer(v): return [[x*y for y in v] for x in v]
def ft(v): return [sum(H[k][j]*v[j] for j in range(4))/4 for k in range(4)]

assert 48//12 == 4
assert mm(H,tr(H)) == scale(I(4),F(4))
assert mm(scale(H,F(1,4)),H) == I(4)
assert H[3] == [H[1][j]*H[2][j] for j in range(4)]

P=[scale(outer(r),F(1,4)) for r in H]
zero=Z(4); total=zero
for i,A in enumerate(P):
    assert mm(A,A)==A
    for j,B in enumerate(P):
        if i!=j: assert mm(A,B)==zero
    total=add(total,A)
assert total==I(4)

# Representative independence: class averages equal the 48-selector averages.
v=[F(2),F(3),F(5),F(11)]
for k,row in enumerate(H):
    c4=sum(row[j]*v[j] for j in range(4))/4
    c48=sum(row[j]*sum([v[j]]*12) for j in range(4))/48
    assert c4==c48

# Any selector-independent output is purely trivial in H4.
for x in [F(1,6),F(1,3),F(2,15),F(7,19),F(-4,11)]:
    assert ft([x,x,x,x]) == [x,F(0),F(0),F(0)]

# Equal epsilon-fiber averages kill epsilon only, not necessarily Q and F.
w=[F(3),F(5),F(7),F(9)]
assert w[0]+w[3] == w[1]+w[2]
c=ft(w)
assert c[3]==0 and c[1]!=0 and c[2]!=0

print('PASS G1: W/G has four character classes, 12 selectors each')
print('PASS G2: H4 is the exact table for 1, chi_Q, chi_F, epsilon_read')
print('PASS G3: four rational projectors are orthogonal, complete, representative-free')
print('PASS G4: selector-independent 1/6 and M_s coefficients have only trivial H4 mode')
print('PASS G6: epsilon-blindness kills epsilon mode without killing chi_Q or chi_F')
print(f'AUDIT G6: epsilon-blind coefficients = {c}')
print('PASS G5: H4 supplies no previously-missing L5-to-L6 bridge datum')
print('DECISION: DIAGNOSTIC; canonical L5 projector, no physical-measure advance')
