#!/usr/bin/env python3
from collections import Counter, defaultdict, deque
from itertools import product

P=5
N=P**6

def modt(xs):
    return tuple(x%P for x in xs)

def a(x):
    p1,p4,p1p,p4p,q,r=x
    return (p4,p1,p4p,p1p,q,r)

def b(x):
    p1,p4,p1p,p4p,q,r=x
    return modt((-p1p,-p4p,-p1,-p4,-q,-r))

def c(x):
    p1,p4,p1p,p4p,q,r=x
    return modt((-p1p+2,-p4p+1+r,-p1+2,-p4+1-r,1-q,-r))

def d(x):
    p1,p4,p1p,p4p,q,r=x
    return modt((2-p1,1-p4,3-p1p,4-p4p,1-q,1-r))

def e(x):
    p1,p4,p1p,p4p,q,r=x
    return modt((2-p1,1-p4,3-p1p,4-p4p,2-q,1-r))

GS=(a,b,c,d,e)

def enc(x):
    n=0
    for v in x:
        n=n*P+v
    return n

def dec(n):
    x=[0]*6
    for i in range(5,-1,-1):
        x[i]=n%P; n//=P
    return tuple(x)

parent=list(range(N))
size=[1]*N

def find(x):
    while parent[x]!=x:
        parent[x]=parent[parent[x]]
        x=parent[x]
    return x

forest_edges=0
def union(x,y):
    global forest_edges
    x=find(x); y=find(y)
    if x==y: return
    if size[x]<size[y]: x,y=y,x
    parent[y]=x; size[x]+=size[y]
    forest_edges+=1

adj=[[] for _ in range(N)]
edge_count=0

for idx in range(N):
    x=dec(idx)
    assert enc(x)==idx
    for g in GS:
        assert g(g(x))==x
    z=sum(x)%P
    for j in (z,(z+2)%P):
        y=enc(GS[j](x))
        union(idx,y)
        adj[idx].append(y)
        adj[y].append(idx)
        edge_count+=1

roots=[find(i) for i in range(N)]
comp=defaultdict(list)
for i,r in enumerate(roots):
    comp[r].append(i)

component_count=len(comp)
sizes=Counter(len(v) for v in comp.values())

# Independent graph-search reconstruction.
seen=set()
bfs_sizes=[]
for start in range(N):
    if start in seen: continue
    q=deque([start]); seen.add(start); count=0
    while q:
        u=q.popleft(); count+=1
        for v in adj[u]:
            if v not in seen:
                seen.add(v); q.append(v)
    bfs_sizes.append(count)

assert len(seen)==N
assert Counter(bfs_sizes)==sizes
assert len(bfs_sizes)==component_count
assert forest_edges==N-component_count

# Every frozen equality edge lies inside one final component.
for u in range(N):
    ru=find(u)
    for v in adj[u]:
        assert find(v)==ru

trace_hist=Counter()
trace_sets=[]
for verts in comp.values():
    zs={sum(dec(i))%P for i in verts}
    trace_sets.append(tuple(sorted(zs)))
    trace_hist[len(zs)]+=1

print("P-U-J-HODGE-SEPARABLE-COUNTER-READ-1")
print("checkpoint vertices / directed frozen edges: %d %d" % (N,edge_count))
print("equivalence components: %d" % component_count)
print("component size histogram: "+" ".join("%d:%d"%item for item in sorted(sizes.items())))
print("trace-set-size histogram: "+" ".join("%d:%d"%item for item in sorted(trace_hist.items())))
print("spanning-forest rank / free quotient dimension: %d %d" % (forest_edges,component_count))
print("independent BFS partition match: PASS")
print("set-valued and free-linear classifications: PROOF.md")
print("verdict: "+("CHECKPOINT-ERASED" if component_count==1 else "CHECKPOINT-QUOTIENT %d"%component_count))
print("restricted preparations / physical sufficiency: NOT CLAIMED")
print("VERDICT: COMPLETE")
