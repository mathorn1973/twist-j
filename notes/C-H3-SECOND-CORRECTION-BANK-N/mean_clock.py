"""NON-CANONICAL #2133 E: exact mean-clock compatibility across arbitrary height."""
from pathlib import Path
import runpy
from itertools import product
from fractions import Fraction as Q
V=runpy.run_path(str(Path(__file__).resolve().parent/'prior.py'))
H=V['H'];Z,O,R,J,JI,P=map(V.get,('Z','O','R','J','JI','P'))
add,sub,mul,sc,neg=map(V.get,('add','sub','mul','sc','neg'))
L=V['L'];alpha=sc(Q(1,2),J);beta=sc(Q(1,2),L)
assert add(alpha,beta)==O
r,c=V['r'],V['c'];delta,delta5=V['delta'],V['delta5']
def need(w,d,tag):
    f=mul(d,H.inverse(sub(O,JI if tag==1 else J)))
    return mul(L,add(w,sc(2,f)))
g1=tuple(need(r,delta,tag) for tag in (1,2))
g2=tuple(need(c,delta5,tag) for tag in (1,2))
D=mul(L,delta)
print('E READY1',g1,'READY2',g2,'DELTA',D)
def pair(a,b):
    return add(mul(alpha,a),mul(beta,b)),add(mul(beta,a),mul(alpha,b))
def mean(a,b,c):
    E=add(g1[0],sc(a,sub(g1[1],g1[0])))
    G=add(g2[0],sc(b,sub(g2[1],g2[0])))
    Odd=mul(H.inverse(beta),sub(G,mul(alpha,sub(E,D))))
    v,w=E,Odd
    for _ in range(4):v,w=pair(v,w)
    target=add(g1[0],sc(c,sub(g1[1],g1[0])))
    return sub(v,target),v,Odd
zero=mean(0,0,0)[0]
columns=[sub(mean(*z)[0],zero) for z in ((1,0,0),(0,1,0),(0,0,1))]
print('E CONSTANT',zero,'COLUMNS',columns)
for a,b,c0 in product(range(2),repeat=3):
    res,val,odd=mean(a,b,c0)
    print('E CORNER',a,b,c0,'SECOND_CLK',val,'ODD',odd,'RESIDUAL',res)
# Augment by rhs and by the row-operation matrix to give checkable certificates.
M=[[Q(v[i]) for v in columns]+[-Q(zero[i])]+[Q(int(i==j)) for j in range(4)] for i in range(4)]
piv=[];row=0
for k in range(3):
    at=next((i for i in range(row,4) if M[i][k]),None)
    if at is None:continue
    M[row],M[at]=M[at],M[row]
    p=M[row][k];M[row]=[x/p for x in M[row]]
    for i in range(4):
        if i!=row:
            p=M[i][k];M[i]=[x-p*y for x,y in zip(M[i],M[row])]
    piv.append(k);row+=1
inconsistent=next((v for v in M if not any(v[:3]) and v[3]),None)
print('E RANK',row,'AUG_RANK',row+bool(inconsistent),'RREF',tuple(tuple(v[:4]) for v in M))
if inconsistent:
    witness=tuple(inconsistent[4:]);lhs=tuple(sum(witness[i]*v[i] for i in range(4)) for v in columns);rhs=-sum(witness[i]*zero[i] for i in range(4))
    assert lhs==(0,0,0) and rhs!=0
    print('E INCONSISTENT_CERTIFICATE',witness,'LHS',lhs,'RHS',rhs)
elif row==3:
    solution=tuple(M[i][3] for i in range(3));assert mean(*solution)[0]==Z
    print('E UNIQUE',solution,'CUBE',all(0<=v<=1 for v in solution))
else:
    free=tuple(k for k in range(3) if k not in piv)
    particular=[Q(0)]*3
    for i,k in enumerate(piv):particular[k]=M[i][3]
    basis=[]
    for j in free:
        v=[Q(0)]*3;v[j]=Q(1)
        for i,k in enumerate(piv):v[k]=-M[i][j]
        basis.append(tuple(v))
    print('E AFFINE',tuple(particular),tuple(basis))
    # For rank deficiency, enumerate vertices of the bounded cube slice
    # (including fixed coordinates). Solve using combinations of 3 independent
    # equations from the original constraints and six boundary equations.
    from itertools import combinations
    equations=[([Q(v[i]) for v in columns],-Q(zero[i])) for i in range(4)]
    for i in range(3):
        for v in (0,1):equations.append(([Q(int(i==j)) for j in range(3)],Q(v)))
    verts=set()
    for rows in combinations(equations,3):
        a=[list(co)+[rhs] for co,rhs in rows]
        for j in range(3):
            p=next((i for i in range(j,3) if a[i][j]),None)
            if p is None:break
            a[j],a[p]=a[p],a[j];v=a[j][j];a[j]=[x/v for x in a[j]]
            for i in range(3):
                if i!=j:
                    v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[j])]
        else:
            v=tuple(a[i][3] for i in range(3))
            if all(0<=x<=1 for x in v) and mean(*v)[0]==Z:verts.add(v)
    print('E CUBE_VERTICES',sorted(verts))
# Nonuniform but admitted integral pairs on both alternating orientations.
def avg(v,y):
    return sc(Q(2,len(v)),H.ring_sum(v[i] for i in range(y,len(v),2)))
for n in (2,4,6,8,10,12):
    values=tuple(add(sc(2*(y*y+3*y),P[(y+1)%5]),J) for y in range(n))
    for bit in (0,1):
        vv=V['vert'](values,bit)
        assert all(H.even(sub(values[i],values[(i+1)%n])) for i in range(bit,n,2))
        assert (avg(vv,0),avg(vv,1))==pair(avg(values,0),avg(values,1))
print('E MEAN_LAW_SAMPLE',12,'PASS')
print('DONE exact arbitrary-height conditional averaged-clock compatibility')
