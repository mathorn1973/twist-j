import importlib.util, sys
from itertools import product
spec = importlib.util.spec_from_file_location("c", sys.argv[1]); 
# reuse ring/receiver definitions without rerunning the asserts: exec only the defs we need
src = open(sys.argv[1]).read().split("BOX1 = ")[0]
g = {}; exec(src, g)
Q, contact, jp, neg = g["Q"], g["contact"], g["jp"], g["neg"]
def receiver(p,q,r):
    for _ in range(5):
        p,r = contact(p,r); p,q = contact(p,q)
    return p,q,r
# Q(a) >= sum a_k^2 / 2, so Q<=32 needs sum a_k^2 <= 64, |a_k|<=8
res = {}
for r in product(range(-8,9), repeat=4):
    if sum(x*x for x in r) > 64: continue
    qr = Q(r)
    if qr > 32: continue
    outs = [Q(receiver(jp(b), neg(jp(b)), r)[2]) for b in range(5)]
    if len(set(outs)) == 5:
        res.setdefault(qr, []).append((r, outs))
for qv in sorted(res):
    print(qv, len(res[qv]), res[qv][:2])
