#!/usr/bin/env python3
"""Exact audit for P-O5-EULER-INCIDENCE-TRIANGLE-NOGO-1."""
from __future__ import annotations
import ast
from pathlib import Path
F=(1,2,10,11,19,121,209,500)

def ck(a,b,d=''):
 if not b: raise AssertionError(a+' failed'+(f': {d}' if d!='' else ''))
def ps(n):
 if n<2:return []
 s=[1]*(n+1);s[0]=s[1]=0;p=2
 while p*p<=n:
  if s[p]:
   for m in range(p*p,n+1,p):s[m]=0
  p+=1
 return [k for k in range(2,n+1) if s[k]]
def c(n):
 r=n%5;return 0 if r==0 else (1 if r in(1,4) else -1)
def sp(n,i=False):return ([2] if i and n>=2 else [])+[p for p in ps(n) if c(p)==1]
def ky(f):return len(f),tuple(sorted(f))
def nm(f):
 x=1
 for p,_ in f:x*=p
 return x
def fs(n,o=2,pair=False,i=False):
 ck('orientations',o in(1,2));z={frozenset()}
 for p in sp(n,i):
  a=set()
  for f in sorted(z,key=ky):
   x=nm(f)
   for q in range(o):
    if x*p<=n:a.add(f|{(p,q)})
   if pair and o==2 and x*p*p<=n:a.add(f|{(p,0),(p,1)})
  z|=a
 return z
def sq(n):
 if n==1:return 1,0
 r=n;w=0
 for p in ps(n):
  if p*p>r:break
  if r%p:continue
  e=0
  while r%p==0:r//=p;e+=1
  if e!=1 or c(p)!=1:return 0,0
  w+=1
 if r>1:
  if c(r)!=1:return 0,0
  w+=1
 return 1,w
def s5(n):
 q,w=sq(n);return (-2)**w if q else 0
def ss(n):return sum(s5(k) for k in range(1,n+1))
def eu(z,e=True):return sum((-1)**len(f) for f in z if e or f)
def cnt(z):
 d={}
 for f in z:d[len(f)]=d.get(len(f),0)+1
 return d
def sc(n):
 d={}
 for k in range(1,n+1):
  q,w=sq(k)
  if q:d[w]=d.get(w,0)+2**w
 return d
def iso(z):
 v={next(iter(f)) for f in z if len(f)==1};u={x for f in z if len(f)==2 for x in f};return v-u
def ii(n):return {(p,o) for p in sp(n) if 11*p>n for o in(0,1)}
def ng(f,z,v):
 a={f-{x} for x in f if f-{x} in z};a|={f|{x} for x in v if x not in f and f|{x} in z};return sorted(a,key=ky)
def mm(z):
 v=sorted({x for f in z for x in f});l=sorted((f for f in z if len(f)%2==0),key=ky);r={f for f in z if len(f)%2};a={f:[g for g in ng(f,z,v) if g in r] for f in l};m={}
 def aug(f,seen):
  for g in a[f]:
   if g in seen:continue
   seen.add(g);old=m.get(g)
   if old is None or aug(old,seen):m[g]=f;return 1
  return 0
 return sum(aug(f,set()) for f in l)
def fm(limit,**kw):
 for n in range(1,limit+1):
  if eu(fs(n,**kw))!=ss(n):return n
 return None

def g1():ck('residues',[c(r) for r in range(5)]==[0,1,-1,-1,1]);ck('first split',sp(50)[:5]==[11,19,29,31,41])
def g2():
 for n in F:
  z=fs(n);ck('unique',len(z)==len(set(z)),n)
  for f in z:
   ck('norm',nm(f)<=n,(n,f))
   for x in tuple(f):ck('down',f-{x} in z,(n,f))
def g3():
 for n in F:ck('Euler',eu(fs(n))==ss(n),n)
def g4():
 for n in F:ck('counts',cnt(fs(n))==sc(n),n)
def g5():
 for n in F:ck('isolated',ii(n)<=iso(fs(n)),n)
 z=fs(209);ck('edge',frozenset({(11,0),(19,0)}) in z);ck('strict',(19,0) not in iso(z))
def g6():
 for n in F:
  z=fs(n);i=len(ii(n));u=len(z)-2*mm(z);ck('aug floor',u>=max(0,i-1),(n,u,i))
  q={f for f in z if f};u=len(q)-2*mm(q);ck('nonempty floor',u>=i,(n,u,i))
def g7():
 ck('B1',fm(200,o=1)==11);ck('B2',fm(200,pair=True)==121);ck('B3',fm(20,i=True)==2)
 z=fs(209);ck('B4a',11*19>=209);ck('B4b',(19,0) not in iso(z));ck('B5',next(n for n in range(1,11) if eu(fs(n),False)!=ss(n))==1)
def root(x):
 if isinstance(x,ast.Import):return x.names[0].name.split('.')[0]
 if isinstance(x,ast.ImportFrom):return (x.module or '').split('.')[0]
 return ''
def g8():
 p=Path(__file__);b=p.read_bytes();ck('LF',b.endswith(b'\n') and b'\r' not in b);t=b.decode();a=ast.parse(t,p.name)
 good={'__future__','ast','pathlib'};bad={'cmath','http','math','mpmath','numpy','random','requests','socket','subprocess','sympy','urllib'};calls={'compile','complex','eval','exec','float','input','open'};im=[];ca=[]
 for x in ast.walk(a):
  if isinstance(x,(ast.Import,ast.ImportFrom)):im.append(root(x))
  if isinstance(x,ast.Constant):ck('literal',not isinstance(x.value,(float,complex)))
  if isinstance(x,ast.Call):
   if isinstance(x.func,ast.Name):ca.append(x.func.id)
   elif isinstance(x.func,ast.Attribute):ca.append(x.func.attr)
 ck('imports',set(im)<=good and not(set(im)&bad),im);ck('calls',not(set(ca)&calls));ck('tokens',('ZERO'+'_TABLE') not in t and ('site'+'-'+'packages') not in t)
def main():
 for f,s in ((g1,'G01 PASS chi_5 split census and first split prime 11'),(g2,'G02 PASS finite oriented faces are duplicate-free and simplicial'),(g3,'G03 PASS squarefree split sum equals augmented face-parity sum'),(g4,'G04 PASS face dimensions equal 2^omega support multiplicities'),(g5,'G05 PASS strict isolated-vertex theorem and N=209 boundary'),(g6,'G06 PASS maximum incidence matchings obey isolated-cell floors'),(g7,'G07 PASS breakers FIRE B1=11 B2=121 B3=2 B4=(209,19) B5=1'),(g8,'G08 PASS exact-integer stdlib source firewall')):f();print(s)
 print('VERIFY RESULT 8/8 ALL PASS');return 0
if __name__=='__main__':raise SystemExit(main())
