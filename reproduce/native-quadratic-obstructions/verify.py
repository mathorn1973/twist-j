"""Supplementary exact audit of inline native-contact obstruction proofs."""
from collections import Counter
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import runpy
import sys
sys.stdout.reconfigure(newline="\n")

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "reproduce/kernel-connectivity/verify.py"
EXPECTED_SOURCE = "87ba627e27bebf5f9101da7691a5bd44f7f058ba007a1a28bb99d19720a93a63"
assert sha256(SOURCE.read_bytes()).hexdigest() == EXPECTED_SOURCE
env = runpy.run_path(str(SOURCE))
gens = [g for _, g in env["GENS"]]
states = list(product(range(5), repeat=6))
checks = []

def check(name, ok):
    assert ok, name
    checks.append(name)

def mm(a, b):
    return [[sum(x*y for x, y in zip(row, col)) % 5 for col in zip(*b)] for row in a]

def matvec(a, v):
    return tuple(sum(x*y for x,y in zip(row,v)) % 5 for row in a)

def rank(a):
    a = [list(row) for row in a]
    rr = 0
    for c in range(len(a[0])):
        p = next((i for i in range(rr,len(a)) if a[i][c] % 5), None)
        if p is None:
            continue
        a[p],a[rr] = a[rr],a[p]
        inv = pow(a[rr][c] % 5,-1,5)
        a[rr] = [v*inv % 5 for v in a[rr]]
        for i in range(len(a)):
            if i != rr:
                k = a[i][c]
                a[i] = [(u-k*v)%5 for u,v in zip(a[i],a[rr])]
        rr += 1
    return rr

B = [[1,4,2],[4,0,1],[3,4,4]]
L = [[3,3,2],[3,4,2],[3,2,0]]
M = [[0,3,0],[4,4,4],[0,3,3]]
check("marked Gram transport LB=BM", rank(B)==3 and mm(L,B)==mm(B,M))
lam = [[1,2,1]]
check("scalar coefficient transport", mm(lam,M)==[[3,4,1]])
C5 = [[-1,-1,-1,-1],[1,0,0,0],[0,1,0,0],[0,0,1,0]]
C52 = mm(C5,C5)
A4 = [[(C52[i][j]+int(i==j))%5 for j in range(4)] for i in range(4)]
qmap = [[1,0,0,4],[0,1,0,4],[0,0,1,4]]
Aq = [[1,4,0],[4,4,4],[1,4,1]]
S = [[2,1,1],[3,3,2],[4,4,4]]
Aw = [[1,1,3],[0,3,2],[1,3,2]]
g5 = [[2,4,0],[4,2,4],[0,4,2]]
g5inv = [[2,3,4],[3,1,3],[4,3,2]]
check("marked exterior target quotient qA=Aq q",mm(qmap,A4)==mm(Aq,qmap) and matvec(A4,(1,1,1,1))==(2,2,2,2))
check("marked quotient transport SAq=AwS",rank(S)==3 and mm(S,Aq)==mm(Aw,S))
check("residual metric inverse",mm(g5,g5inv)==[[1,0,0],[0,1,0],[0,0,1]])
def cross(u,v):
    return ((u[1]*v[2]-u[2]*v[1])%5,(u[2]*v[0]-u[0]*v[2])%5,(u[0]*v[1]-u[1]*v[0])%5)
def beta(u,v): return matvec(g5inv,cross(u,v))
basis3 = [(1,0,0),(0,1,0),(0,0,1)]
check("exact bracket-transported exterior target L5",all(beta(matvec(Aw,u),matvec(Aw,v))==matvec(L,beta(u,v)) for u in basis3 for v in basis3))
Q1 = [[1,1],[1,1]]
Q2 = [[3,2],[2,1]]
check("small quadratic ranks", rank(Q1)==1 and rank(Q2)==2)
for r in range(1,7):
    for delta in (1,2):
        diag = [1]*(r-1)+[delta]+[0]*(6-r)
        c = [[diag[i] if i==j else 0 for j in range(6)] for i in range(6)]
        k1 = [[Q1[i//6][j//6]*c[i%6][j%6] % 5 for j in range(12)] for i in range(12)]
        k2 = [[Q2[i//6][j//6]*c[i%6][j%6] % 5 for j in range(12)] for i in range(12)]
        check(f"quadratic ranks r={r} delta={delta}", rank(k1)==r and rank(k2)==2*r)

affine = {}
for name,g in env["GENS"]:
    v = g((0,)*6)
    cols = [tuple((g(tuple(int(k==j) for k in range(6)))[i]-v[i]) % 5 for i in range(6)) for j in range(6)]
    a = [list(row) for row in zip(*cols)]
    check(f"full native generator affine {name}", rank(a)==6 and all(g(x)==tuple((u+w)%5 for u,w in zip(matvec(a,x),v)) for x in states))
    affine[name] = {"linear":a,"translation":v}

tables = []
for bit in (0,1):
    fun = lambda x: gens[(sum(x)+2*bit)%5](x)
    image = Counter(fun(x) for x in states)
    phase = []
    for z in range(5):
        values = {sum(fun(x))%5 for x in states if sum(x)%5==z}
        check(f"selector phase bit={bit} z={z}",len(values)==1)
        phase.append(values.pop())
    expected = [0,4,0,4,4] if bit==0 else [2,1,1,3,1]
    check(f"selector phase table bit={bit}",phase==expected)
    histogram=Counter(image.values())
    check(f"selector maximum fiber three bit={bit}",max(image.values())==3)
    check(f"selector full image histogram bit={bit}",histogram==({2:3125,3:3125} if bit==0 else {1:6250,3:3125}))
    y=(4,0,0,0,0,0) if bit==0 else (1,0,0,0,0,0)
    inputs=[g(y) for g in gens if fun(g(y))==y]
    inputs=sorted(set(inputs))
    check(f"explicit triple collision bit={bit}",len(inputs)==3)
    tables.append({"bit":bit,"phase":phase,"image_size":len(image),"fiber_histogram":dict(sorted(histogram.items())),"collision_output":y,"collision_inputs":inputs})

# Conditional common-LINEAR-frame reader, never selected as physical C.
C4 = [[1,0,1,0,0,0],[0,1,0,1,0,0],[1,0,1,0,0,0],[0,1,0,1,0,0],[0,0,0,0,1,0],[0,0,0,0,0,1]]
check("conditional linear-frame example rank four",rank(C4)==4)
for name, data in affine.items():
    a=data["linear"]
    check(f"conditional linear-frame invariance {name}",mm(mm([list(row) for row in zip(*a)],C4),a)==C4)
check("example is not full affine invariant", any(matvec(C4,data["translation"])!=(0,)*6 for data in affine.values()))

print(json.dumps({"status":"Supplementary exact proof audit; native implementation remains open", "source":SOURCE.relative_to(ROOT).as_posix(),"source_sha256":EXPECTED_SOURCE,"checks_passed":len(checks),"checks":checks,"selector_tables":tables,"conditional_rank_four_example":C4},indent=2))
