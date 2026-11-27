"""NON-CANONICAL #2121 B: separated archive capture and worker reset."""
from pathlib import Path
import runpy
from itertools import product
from collections import Counter
V=runpy.run_path(str(Path(__file__).resolve().parent/'verify.py'))
H=V['H'];Z,O,R,J,JI,P=V['Z'],V['O'],V['R'],V['J'],V['JI'],V['P']
add,sub,mul,sc,h,neg=V['add'],V['sub'],V['mul'],V['sc'],V['h'],V['neg']
seed,cols,hist,step,account,ix=V['seed'],V['cols'],V['hist'],V['step'],V['account'],V['ix']
src,worker,store,archive,reader=V['sourcepart'],V['worker'],V['store'],V['archive'],V['reader']
N=(0,2,3,4)
def prepare(F,x,f,G):
    G0=list(F);d=mul(JI,f);assert not H.even(d)
    for y in range(2):
        G0[ix(x,y,0):ix(x,y,0)+3]=(d if y==0 else Z,neg(d) if y==0 else Z,G)
    return tuple(G0)
def pretest(old,x,t,f,G):
    d=mul(JI,f)
    for u,k,y in product(range(1,t+1),range(5),range(2)):
        c=old[k][1][u][ix(x,y,3)]
        actual=H.collision(cols(d if y==0 else Z,G,c))[1]
        if actual!=int(u==t and k==1 and y==0):
            return False
    return True
def trial(old,x,t,f,G,M,ks,collect=False):
    initial={k:prepare(old[k][0][0],x,f,G) for k in ks}
    F=initial.copy();acs={k:account(ff) for k,ff in initial.items()}
    assert len(set(acs.values()))==1
    assert len({reader(ff) for ff in initial.values()})==1
    active=True;ne=True;po=False;loss=None;weak=[];full=[];heads=[]
    port,ref=ix(x,0,2),ix(x,1,2)
    for u in range(1,257):
        mids={};nxt={};tags={}
        for k,ff in F.items():
            G1,N1,E=step(ff,(u-1)%2,acs[k])
            mids[k]=G1;nxt[k]=N1;tags[k]=E
            if u<t:
                if src(N1)!=src(old[k][0][u]) or worker(N1)!=worker(old[k][0][u]) or any(N1[i]!=old[k][0][u][i] for i in range(3,len(N1),4)) or any(E[2*x:2*x+2]):
                    return 'EARLY_CONTINUATION',[],[],None
            elif u==t:
                if E[2*x:2*x+2]!=(int(k==1),0) or G1[ix(x,0,3)]!=old[k][1][u][ix(x,0,3)] or N1[port]!=(M if k==1 else G) or N1[ref]!=G:
                    return 'CAPTURE',[],[],None
        for stage,states in ((1,mids),(0,nxt)):
            ne &= len({reader(v) for k,v in states.items() if k!=1})==1
            po |= reader(states[1])!=reader(states[0])
            if u>t and active and any(v[port]!=(M if k==1 else G) or v[ref]!=G for k,v in states.items()):
                active=False;loss=(u,stage)
        F=nxt
        if collect:heads.append((u,mids,nxt,tags,ne,po,active))
        if u>=t and u%2==0 and active and ne and po and all(src(F[k])==src(initial[k]) for k in ks):
            W=all(store(F[k])==store(initial[k]) for k in ks)
            U=all(worker(F[k])==worker(initial[k]) for k in ks)
            A=len({archive(v) for k,v in F.items() if k!=1})==1 and archive(F[1])!=archive(F[0])
            if W and A:weak.append(u)
            if U and A:full.append(u)
        if not collect and (not active or not ne):break
    return ('FULL' if full else 'WEAK' if weak else 'NO_HELD_RESET'),weak,full,(initial,acs,heads,loss)
def report(label,variant,x,t,f,G,M,result,old):
    status,weak,full,info=result;ini,acs,heads,loss=info
    T=(full or weak)[0]
    print('B SELECT',label,variant,x,t,'F',f,'G',G,'MARK',M,'WEAK',weak,'FULL',full,'LOSS',loss,'Q',H.scalar_account(acs[0][2]),'H',acs[0][2])
    hh=[hist(ini[k],256,True) for k in range(5)]
    for k,w in enumerate(hh):
        F=w[0][T]
        assert src(F)==src(ini[k])
        assert store(F)==store(ini[k])
        if status=='FULL':assert worker(F)==worker(ini[k])
        assert F[ix(x,0,2)]==(M if k==1 else G) and F[ix(x,1,2)]==G
        print('B WITNESS',label,k,'SOURCE',src(F),'WORKER',worker(F),'ARCHIVE_CELL',F[ix(x,0,0):ix(x,0,0)+8])
        print('B SECTORS',label,k,'SOURCE_DELTA',tuple(sub(a,b) for a,b in zip(account(src(F)),account(src(ini[k])))),
             'WORKER_DELTA',tuple(sub(a,b) for a,b in zip(account(worker(F)),account(worker(ini[k])))),
             'ARCH_DELTA',tuple(sub(a,b) for a,b in zip(account(archive(F)),account(archive(ini[k])))))
    for u,mid,cut,ts,ne,po,active in heads:
        if u in {t-1,t,t+1,T-1,T,T+1,256}:
            print('B CUT',label,u,'ARCH_TAGS',tuple(ts[k][2*x:2*x+2] for k in range(5)),'PORTS',tuple(cut[k][ix(x,0,2)] for k in range(5)),
                  'SOURCE_MATCH',sum(src(cut[k])==src(ini[k]) for k in range(5)),'WORKER_MATCH',sum(worker(cut[k])==worker(ini[k]) for k in range(5)),
                  'NEG_EQUAL',int(ne),'POS_SEEN',int(po),'HOLD',int(active))
def main():
    stats=Counter();firstweak=None
    vecs=tuple(v for v in product(range(2),repeat=4) if any(v))
    for variant in V['VARIANTS']:
        old=[hist(seed(k,variant),24) for k in range(5)]
        for x,t in product((5,7,4,3,2,1),range(7,25)):
            Rp=old[1][1][t][ix(x,0,3)];nv={old[k][1][t][ix(x,0,3)] for k in N}
            if len(nv)!=1 or Rp in nv:
                stats['cut_reject']+=1
                continue
            local=Counter()
            for v,n in product(vecs,(1,3,5)):
                f=sc(n,v);G=add(Rp,sc(2,f));M=add(G,mul(sub(JI,O),f))
                assert M!=G
                stats['tried']+=1;local['tried']+=1
                if not pretest(old,x,t,f,G):
                    stats['guard_reject']+=1;local['guard_reject']+=1;continue
                stats['pretest_pass']+=1;local['pretest_pass']+=1
                a=trial(old,x,t,f,G,M,(0,1))
                if not a[1] and not a[2]:
                    stats['screen_'+a[0]]+=1;local['screen_'+a[0]]+=1;continue
                full=trial(old,x,t,f,G,M,tuple(range(5)),True)
                stats['five_'+full[0]]+=1;local['five_'+full[0]]+=1
                if full[2]:
                    print('B SEARCH_CUT',variant,x,t,sorted(local.items()))
                    print('B COUNTS',sorted(stats.items()))
                    report('FULL',variant,x,t,f,G,M,full,old)
                    print('B PASS complete source and worker restored, separate native archive')
                    return
                if full[1] and firstweak is None:
                    firstweak=(variant,x,t,f,G,M,full,old)
            print('B SEARCH_CUT',variant,x,t,sorted(local.items()),flush=True)
    print('B COUNTS',sorted(stats.items()))
    if firstweak:report('WEAK',*firstweak)
    print('B NO FULL RESET WITH ARCHIVE')
if __name__=='__main__':main()
