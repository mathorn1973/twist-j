"""NON-CANONICAL #2123. Exact worker restitution by a final local correction."""
import sys,runpy,hashlib
from pathlib import Path
from itertools import product
from fractions import Fraction as Q
from collections import Counter
root=Path(__file__).resolve().parent
assert hashlib.sha256((root/'predecessor.py').read_bytes()).hexdigest()=='ad4920e5d0322e33013f77e3bedd290733df4a054e2284060b72a94164f12e95'
V=runpy.run_path(str(root/'predecessor.py'))
H=V['H'];Z,O,R,J,JI,P=V['Z'],V['O'],V['R'],V['J'],V['JI'],V['P']
add,sub,mul,sc,h,neg=V['add'],V['sub'],V['mul'],V['sc'],V['h'],V['neg']
seed,cols,hist,step,account,ix=V['seed'],V['cols'],V['hist'],V['step'],V['account'],V['ix']
src,worker,store,archive,reader=V['sourcepart'],V['worker'],V['store'],V['archive'],V['reader']
N=(0,2,3,4); K=range(5)
L=sub(O,R); beta=sc(Q(1,2),L)
BI=H.inverse(beta)
assert mul(beta,BI)==O
def integral(a):
    return all(Q(x).denominator==1 for x in a)
def ints(a):
    assert integral(a)
    return tuple(map(int,a))
def cpart(F,x,y):
    i=ix(x,y,0);return F[i:i+4]
def delta_accounts(F,I):
    return tuple(tuple(sub(a,b) for a,b in zip(account(part(F)),account(part(I)))) for part in (src,worker,archive))
def equal(F,I,part):
    return all(part(F[k])==part(I[k]) for k in K)
def two(F,part):
    return len({part(F[k]) for k in N})==1 and part(F[1])!=part(F[0])
def neg_equal(F,part):
    return len({part(F[k]) for k in N})==1
def rot(pair,n,back=False):
    for _ in range(n%5):pair=H.transport_pair(*pair,back)
    return pair
def initial_add(F,d,g):
    out=list(F)
    for y in range(2):
        i=ix(5,y,0);out[i:i+3]=(d[y],neg(d[y]),g)
    return tuple(out)
def hypotheses(old,T):
    t=T-1
    I=[w[0][0] for w in old]
    x=old[1][0][t][ix(6,0,3)]; y=old[1][0][t][ix(5,0,3)]
    u=I[1][ix(6,0,3)]
    ystar=add(x,mul(BI,sub(u,x)))
    correction=sub(ystar,y)
    neg_ready=all(src(old[k][0][T])==src(I[k]) and worker(old[k][0][T])==worker(I[k]) for k in N)
    pos_ready=src(old[1][0][T])==src(I[1]) and store(old[1][1][T])==store(I[1]) and old[1][1][T][ix(6,1,3)]==I[1][ix(6,1,3)]
    integral_ok=integral(ystar); parity=integral_ok and H.even(sub(ints(ystar),x))
    yout=H.transport_pair(x,ints(ystar),False)[0] if parity else None
    local_ok=parity and yout==u and correction!=Z
    print('A TARGET',T,'X',x,'Y',y,'U',u,'YSTAR',tuple(map(str,ystar)),'DELTA',tuple(map(str,correction)),'INTEGRAL',int(integral_ok),'PARITY',int(parity),'CORRECT_C',int(local_ok),'NEG_READY',int(neg_ready),'POS_READY',int(pos_ready))
    print('A PREVIOUS',T,'POS_SRC',src(old[1][0][t]),'POS_WORKER',worker(old[1][0][t]),'POS_ARCHIVE5',old[1][0][t][40:48])
    print('A ORIGINAL_SECTORS',T,delta_accounts(old[1][0][T],I[1]))
    if local_ok:
        F=list(old[1][0][t]);F[ix(5,0,3)]=ints(ystar);F=tuple(F)
        G=H.transport(F,2,1);N0,ev=H.collide(G,2)
        print('A HYPOTHETICAL',T,'BEFORE_C',delta_accounts(F,I[1]),'AFTER_C',delta_accounts(G,I[1]),'AFTER_B',delta_accounts(N0,I[1]),'WORKER_RESTORED',int(worker(N0)==worker(I[1])),'SOURCE_RESTORED',int(src(N0)==src(I[1])),'TAGS',ev)
    return (ints(correction),ints(ystar)) if local_ok and neg_ready and pos_ready else None

def pretest(old,t,d,g,tag):
    cur=d
    for u in range(1,t+1):
        cur=rot(cur,1)
        for k,y in product(K,range(2)):
            z=old[k][1][u][ix(5,y,3)]
            if H.collision(cols(cur[y],g,z))[1]!=(tag if u==t and k==1 and y==0 else 0):
                return False
    return True
def trial(old,T,d,g,tag,corr,ystar):
    t=T-1
    hh=[hist(initial_add(w[0][0],d,g),T+32,True) for w in old]
    I=[w[0][0] for w in hh]
    assert len({w[3] for w in hh})==1
    assert len({reader(f) for f in I})==1
    for k,w in enumerate(hh):
        for u in range(1,t):
            F=w[0][u]
            if src(F)!=src(old[k][0][u]) or worker(F)!=worker(old[k][0][u]) or any(F[i]!=old[k][0][u][i] for i in range(3,len(F),4)) or any(w[2][u][10:12]):
                return 'EARLY',None
        if w[2][t][10:12]!=(tag if k==1 else 0,0):
            return 'TAG',None
        if w[0][t][ix(5,0,3)]!=(ystar if k==1 else old[k][0][t][ix(5,0,3)]) or w[0][t][ix(5,0,2)]!=(sub(g,corr) if k==1 else g):
            return 'CORRECTION',None
    F=[w[0][T] for w in hh]
    if not equal(F,I,src):return 'SOURCE',None
    if not equal(F,I,worker):return 'WORKER',None
    if not two(F,archive):return 'ARCHIVE',None
    negsame=True;po=False
    for u in range(T+1):
        for s in ((0,) if u==0 else (1,0)):
            G=[w[s][u] for w in hh]
            negsame &= neg_equal(G,reader);po |= reader(G[1])!=reader(G[0])
    if not (negsame and po):return 'HISTORY',None
    port=ix(5,0,2);ref=ix(5,1,2)
    if not all(F[k][port]==F[0][port] for k in N) or F[1][port]==F[0][port] or not all(f[ref]==g for f in F):
        return 'PORT',None
    return 'PASS',hh
def main():
    old=[hist(seed(k,'static'),790,True) for k in K]
    assert len({w[3] for w in old})==1
    assert H.scalar_account(old[0][3][2])==2630
    targets={T:hypotheses(old,T) for T in (114,384,758)}
    stats=Counter()
    for T,ans in targets.items():
        if ans is None:
            stats['prerequisite_reject']+=1;continue
        corr,ystar=ans;t=T-1;rp=old[1][1][t][ix(5,0,3)]
        assert rp==old[1][0][t][ix(5,0,3)]
        aliases=[(u,k) for u,k in product(range(1,t),K) if (t-u)%5==0 and old[k][1][u][ix(5,0,3)]==rp]
        for tag in (1,2):
            f=mul(corr,H.inverse(sub(O,JI if tag==1 else J)))
            print('B SYNTHESIS',T,tag,'F',tuple(map(str,f)),'RP',rp,'ALIAS',aliases[0] if aliases else None)
            if aliases:
                stats['clock_alias']+=1;continue
            if not integral(f):stats['nonintegral']+=1;continue
            f=ints(f);g=add(rp,sc(2,f))
            base=mul(JI if tag==1 else J,f)
            local=Counter()
            ws=(Z,)+tuple(sc(n*s,P[k]) for n,s,k in product((1,3,5),(1,-1),range(5)))
            for sign,k,w in product((1,-1),range(5),ws):
                d0=mul(base,sc(sign,P[k]));d=rot((d0,add(d0,sc(2,w))),t,True)
                stats['tried']+=1;local['tried']+=1
                if not pretest(old,t,d,g,tag):
                    stats['guard_reject']+=1;local['guard_reject']+=1;continue
                status,hh=trial(old,T,d,g,tag,corr,ystar)
                stats[status]+=1;local[status]+=1
                if status!='PASS':continue
                print('B LOCAL',T,tag,sorted(local.items()))
                print('B COUNTS',sorted(stats.items()))
                print('B SELECT',T,tag,'F',f,'D',d,'G',g,'SIGN',sign,'K',k,'W',w,'Q',H.scalar_account(hh[0][3][2]))
                F=[w0[0][T] for w0 in hh];port=ix(5,0,2);ref=ix(5,1,2)
                for k in (0,1):
                    print('B WITNESS',k,'SRC',src(F[k]),'WORKER',worker(F[k]),'ARCHIVE5',F[k][40:48],'SECTORS',delta_accounts(F[k],hh[k][0][0]))
                loss=next(((u,s) for u in range(T+1,T+33) for s in (1,0) if any(w0[s][u][port]!=F[k][port] or w0[s][u][ref]!=g for k,w0 in enumerate(hh))),None)
                print('B HOLD_FIRST_LOSS',loss)
                print('B PASS full source and worker restored, native compensated archive')
                break
            else:
                print('B LOCAL',T,tag,sorted(local.items()))
                continue
            break
        else:continue
        break
    else:
        print('B COUNTS',sorted(stats.items()))
        print('B NO FULL RESET')
    a,b=O,neg(O)
    c,d=H.transport_pair(a,b,False)
    assert (c,d)==(R,neg(R)) and (a,b)!=(c,d) and add(a,b)==add(c,d) and add(h(a),h(b))==add(h(c),h(d))
    print('C COMPENSATED_PAIR',(a,b),(c,d),'SUM',add(c,d),'H',add(h(c),h(d)))
    print('DONE exact communication restitution experiment')
if __name__=='__main__':main()
