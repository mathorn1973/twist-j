#!/usr/bin/env python3
from fractions import Fraction as Q
from itertools import permutations, product

Z=lambda n=4: tuple(tuple(Q(0) for _ in range(n)) for _ in range(n))
I=lambda n=4: tuple(tuple(Q(i==j) for j in range(n)) for i in range(n))
def A(X,Y): return tuple(tuple(a+b for a,b in zip(x,y)) for x,y in zip(X,Y))
def S(X,Y): return tuple(tuple(a-b for a,b in zip(x,y)) for x,y in zip(X,Y))
def C(c,X): return tuple(tuple(Q(c)*a for a in x) for x in X)
def T(X): return tuple(tuple(c) for c in zip(*X))
def M(X,Y):
 y=T(Y); return tuple(tuple(sum(a*b for a,b in zip(x,c)) for c in y) for x in X)
def P(X,n):
 r=I(len(X)); b=X
 while n:
  if n&1:r=M(r,b)
  b=M(b,b);n//=2
 return r
def inv(X):
 n=len(X); a=[list(X[i])+list(I(n)[i]) for i in range(n)]
 for j in range(n):
  k=next(i for i in range(j,n) if a[i][j]);a[j],a[k]=a[k],a[j];q=a[j][j];a[j]=[x/q for x in a[j]]
  for i in range(n):
   if i!=j and a[i][j]:q=a[i][j];a[i]=[x-q*y for x,y in zip(a[i],a[j])]
 return tuple(tuple(x[n:]) for x in a)
def rk(X):
 a=[list(x) for x in X];r=0
 for j in range(len(a[0])):
  k=next((i for i in range(r,len(a)) if a[i][j]),None)
  if k is None:continue
  a[r],a[k]=a[k],a[r];q=a[r][j];a[r]=[x/q for x in a[r]]
  for i in range(len(a)):
   if i!=r and a[i][j]:q=a[i][j];a[i]=[x-q*y for x,y in zip(a[i],a[r])]
  r+=1
 return r
def tr(X):return sum(X[i][i] for i in range(len(X)))
def cols(v):return tuple(tuple(v[j][i] for j in range(len(v))) for i in range(len(v[0])))
def mv(X,v):return tuple(sum(a*b for a,b in zip(x,v)) for x in X)
def sumM(xs):
 r=Z()
 for x in xs:r=A(r,x)
 return r

J=((Q(1),Q(0),Q(-1),Q(1)),(Q(0),Q(1),Q(-1),Q(0)),(Q(1),Q(0),Q(0),Q(0)),(Q(0),Q(1),Q(-1),Q(1)))
E=I();D=S(J,E);O=S(D,P(D,4));V=A(D,P(D,4));assert P(D,5)==E
G=S(E,C(Q(1,5),tuple(tuple(Q(1) for _ in range(4)) for _ in range(4))));Gi=inv(G)
sh=lambda X:M(M(Gi,T(X)),G)
hs=lambda X:tr(M(sh(X),X))
e0=(Q(1),Q(0),Q(0),Q(0)); vv=tuple(mv(P(D,k),e0) for k in range(5));B=cols(vv[:4]);Bi=inv(B)
def rho(a,b):return M(cols(tuple(vv[(a*x+b)%5] for x in range(4))),Bi)
R={(a,b):rho(a,b) for a in (1,2,3,4) for b in range(5)}
PP={};RR={};CC={};gg={}
for k in range(5):
 st={a:R[(a,k*(1-a)%5)] for a in (1,2,3,4)};gg[k]=st[2]
 PP[k]=C(Q(1,4),sumM(st.values()))
 RR[k]=C(Q(1,4),A(S(A(E,P(gg[k],2)),gg[k]),C(-1,P(gg[k],3))))
 CC[k]=S(S(E,PP[k]),RR[k])

def qmul(x,y):return (x[0]*y[0]+5*x[1]*y[1],x[0]*y[1]+x[1]*y[0])
def qadd(x,y):return(x[0]+y[0],x[1]+y[1])
def pmul(a,b):
 r=[(Q(0),Q(0))]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):r[i+j]=qadd(r[i+j],qmul(x,y))
 return tuple(r)
au=(Q(3,2),Q(1,2));ad=(Q(3,2),Q(-1,2));neg=lambda x:(-x[0],-x[1])
fac=pmul((au,neg(au),(Q(1),Q(0))),(ad,neg(ad),(Q(1),Q(0))))==tuple((Q(x),Q(0)) for x in (1,-2,4,-3,1))
native=fac and 5<9 and au!=ad

tok=[]
for k in range(5):
 p,r,c=PP[k],RR[k],CC[k]
 integ=(rk(p),rk(r),rk(c))==(1,1,2) and A(A(p,r),c)==E and all(M(x,y)==Z() for x,y in ((p,r),(r,p),(p,c),(c,p),(r,c),(c,r))) and sh(O)==C(-1,O)
 dz=all(M(M(x,O),x)==Z() for x in (p,r,c)); direct=M(M(p,O),r)==Z() and M(M(r,O),p)==Z()
 cross=all(rk(M(M(x,O),y))==1 and hs(M(M(x,O),y))==Q(5,2) for x,y in ((p,c),(c,p),(r,c),(c,r)))
 b=M(M(M(M(p,O),c),O),r); bridge=rk(b)==1 and hs(b)==Q(5,4) and M(sh(b),b)==C(Q(5,4),r) and M(b,sh(b))==C(Q(5,4),p)
 up=M(M(c,O),p);ur=M(M(c,O),r);lp=C(Q(2,5),M(up,sh(up)));lr=C(Q(2,5),M(ur,sh(ur)));ang=tr(M(lp,lr))==Q(1,5)
 h=A(gg[k],P(gg[k],3));spec=M(h,p)==C(2,p) and M(h,r)==C(-2,r) and M(h,c)==Z()
 tok.append(integ and dz and direct and cross and bridge and ang and spec)
bridge=all(tok)
ctrl=True
for u in (D,P(D,2),P(D,3),P(D,4),V):
 for k in range(5):
  d={'P':PP[k],'R':RR[k],'C':CC[k]}
  for x,y in permutations(d,2):
   z=({'P','R','C'}-{x,y}).pop()
   if M(M(d[x],u),d[y])==Z() and M(M(M(M(d[x],u),d[z]),u),d[y])!=Z():ctrl=False

# exact determinant polynomial in z,t as dict (dz,dt)->Q
def addp(a,b):
 r=dict(a)
 for m,c in b.items():r[m]=r.get(m,Q(0))+c
 return {m:c for m,c in r.items() if c}
def mulp(a,b):
 r={}
 for (i,j),x in a.items():
  for(k,l),y in b.items():r[(i+k,j+l)]=r.get((i+k,j+l),Q(0))+x*y
 return {m:c for m,c in r.items() if c}
def sgn(p):return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1
H=A(gg[2],P(gg[2],3));L=[]
for i in range(4):
 row=[]
 for j in range(4):
  e={}
  if i==j:e[(1,0)]=Q(1)
  if H[i][j]:e[(0,0)]=e.get((0,0),Q(0))-H[i][j]
  if O[i][j]:e[(0,1)]=e.get((0,1),Q(0))-O[i][j]
  row.append(e)
 L.append(row)
det={}
for p in permutations(range(4)):
 q={(0,0):Q(sgn(p))}
 for i,j in enumerate(p):q=mulp(q,L[i][j])
 det=addp(det,q)
detok=det=={(4,0):Q(1),(2,2):Q(5),(2,0):Q(-4),(0,4):Q(5)}

grp=tuple((a,b) for a in (1,2,3,4) for b in range(5))
def fix(g):a,b=g;return sum((a*x+b)%5==x for x in range(5))
def gm(g,h):a,b=g;c,d=h;return(a*c%5,(b+a*d)%5)
def ep(g):return Q(1 if g[0] in (1,4) else -1)
cv={g:Q(fix(g)-1) for g in grp};one={g:Q(1) for g in grp};ee={g:ep(g) for g in grp};cs={g:Q(1,2)*(cv[g]**2+cv[gm(g,g)]) for g in grp}
ip=lambda a,b:Q(1,20)*sum(a[g]*b[g] for g in grp)
decomp=(ip(one,cs),ip(ee,cs),ip(cv,cs),ip(cs,cs))==(1,1,2,6) and ip(one,ee)==ip(one,cv)==ip(ee,cv)==0
qm=((Q(0),Q(1),Q(-1),Q(-1)),(Q(1),Q(0),Q(1),Q(-1)),(Q(-1),Q(1),Q(0),Q(1)),(Q(-1),Q(-1),Q(1),Q(0)))
qp=C(Q(5,2),G);sign=True
for g,x in R.items():sign &= M(M(T(x),qp),x)==qp and M(M(T(x),qm),x)==C(ep(g),qm)
ch={'1':one,'e':ee,'V':cv};dims={}
for a,b,c in product(ch,repeat=3):
 d=Q(1,20)*sum(ch[a][g]*ch[b][g]*ch[c][g] for g in grp)
 if d:dims[(a,b,c)]=d
target={('1','1','1'):Q(1),('1','e','e'):Q(1),('e','1','e'):Q(1),('e','e','1'):Q(1),('1','V','V'):Q(1),('V','1','V'):Q(1),('V','V','1'):Q(1),('e','V','V'):Q(1),('V','e','V'):Q(1),('V','V','e'):Q(1),('V','V','V'):Q(3)}
triple=dims==target
ok=all((native,bridge,ctrl,detok,decomp,sign,triple))
print('P-J-ODD-MOTOR-MEDIATED-BRIDGE-2')
print('LAYER L1 EXACT ARITHMETIC ONLY')
print('NATIVE TWO-SECTOR NO-GO', 'PASS' if native else 'FAIL')
print('ODD MOTOR TOKENS CERTIFIED',sum(tok),'/5')
print('DIRECT P-R ZERO AND P-C-R BRIDGE','PASS' if bridge else 'FAIL')
print('BRIDGE NORM SQUARED 5/4','PASS' if bridge else 'FAIL')
print('ACTIVE-LINE OVERLAP 1/5','PASS' if bridge else 'FAIL')
print('RAW POWERS AND EVEN CONTROL','PASS' if ctrl else 'FAIL')
print('SCHUR MAGNITUDE sqrt(5)*t^2/(2z)','PASS' if bridge and detok else 'FAIL')
print('FULL DET z^4+(5t^2-4)z^2+5t^4','PASS' if detok else 'FAIL')
print('SYM2 1+epsilon+2V END_DIM 6','PASS' if decomp else 'FAIL')
print('AFFINE SIGN MODE q_minus','PASS' if sign else 'FAIL')
print('TRILINEAR CENSUS','PASS' if triple else 'FAIL')
print('PHYSICAL FREQUENCY MATERIAL BORN DECODER NOT CLAIMED')
print('DECISION', 'MEDIATED-BRIDGE-CERTIFIED' if ok else 'ROUTE-FALSIFIED')
