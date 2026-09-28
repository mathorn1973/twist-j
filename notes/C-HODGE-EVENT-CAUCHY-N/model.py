#!/usr/bin/env python3
"""Exact scalar evolution on a selected subset of windowed Hodge events.

Field values are pairs of rational coefficients in Q(sqrt(5)). No floats.
This is a selected mathematical construction, not the native Omega,U map.
"""
from __future__ import annotations
from fractions import Fraction
from pathlib import Path
import contextlib
import hashlib
import io
import runpy
from typing import Any

ROOT=Path(__file__).resolve().parents[2]
ANCHOR='probes/P-J-HODGE-HERM2-LOXODROME-1/verify.py'
DIGEST='02f33f1de4174ee4d4aeb45202d838897e68c3bd205df23f9b208cc669f489d9'
Site=tuple[int,int,int]
Field=dict[Site,Any]

class Model:
    def __init__(self):
        p=ROOT/ANCHOR
        if hashlib.sha256(p.read_bytes()).hexdigest()!=DIGEST:
            raise RuntimeError('STOP: inherited exact anchor hash mismatch')
        with contextlib.redirect_stdout(io.StringIO()):
            a=runpy.run_path(str(p))
        self.anchor=a; self.Q=a['Q5']; Q=self.Q
        self.zero,self.one=Q(0),Q(1)
        self.mm,self.mv,self.tr=(a[k] for k in ('mm','mv','tr'))
        self.E,self.g,self.beta=(a[k] for k in ('E','B','WQ'))
        eye=a['eye'](4,Q)
        invg=self.tr([a['solve'](self.g,v) for v in self.tr(eye)])
        self.Pi=self.mm(self.mm(self.mm(self.E,invg),self.tr(self.E)),self.beta)
        self.N=a['sub'](a['eye'](6,Q),self.Pi)
        self.frame=[self.mv(self.E,list(map(Q,v))) for v in
                    ((0,0,0,1),(1,-1,0,0),(1,1,-2,0),(1,1,1,0))]
        self.ct=(Q(2)+a['S'])/8
        self.alpha=tuple((Q(5)+2*a['S'])/d for d in (16,48,60))
        self.total=sum(self.alpha,Q(0))
        self.c0=(Q(4)+2*a['S'])/5
        self.R=Q(10)-Q(Fraction(9,5))*a['S']

    def sign(self,x):
        x=self.Q(x) if not isinstance(x,self.Q) else x
        a,b=x.a,x.b
        if not b:return (a>0)-(a<0)
        if not a:return (b>0)-(b<0)
        if a*b>0:return (a>0)-(a<0)
        d=a*a-5*b*b
        if not d:raise ArithmeticError('unexpected nonzero irrational equality')
        y=a if d>0 else b
        return (y>0)-(y<0)

    def floor(self,x):
        a,b=x.a,x.b
        base=a.numerator//a.denominator
        bceil=(abs(b.numerator)+b.denominator-1)//b.denominator
        lo,hi=base-3*bceil-2,base+3*bceil+2
        while hi-lo>1:
            mid=(lo+hi)//2
            if self.sign(x-self.Q(mid))>=0:lo=mid
            else:hi=mid
        return lo

    def inner(self,x,y):
        return sum((a*b for a,b in zip(x,self.mv(self.beta,y))),self.zero)

    def event_label(self,n:int,m:int,z:Site)->tuple[int,...]:
        if n<3 or len(z)!=3:raise ValueError('n>=3 and a three-integer site are required')
        coeff=(m,)+tuple(z)
        target=[sum((c*v[j] for c,v in zip(coeff,self.frame)),self.zero)*n**3 for j in range(6)]
        return tuple(self.floor(x+self.Q(Fraction(1,2))) for x in target)

    def event(self,n:int,m:int,z:Site):
        w=self.event_label(n,m,z)
        return [x/n**4 for x in self.mv(self.Pi,list(map(self.Q,w)))]

    def admitted(self,label:tuple[int,...])->bool:
        v=self.mv(self.N,list(map(self.Q,label)))
        return self.sign(-self.inner(v,v)-self.c0)<=0

    def time(self,x):
        return -self.inner(self.frame[0],x)/self.ct

    @staticmethod
    def shifted(z:Site,i:int,d:int)->Site:
        v=list(z);v[i]+=d;return tuple(v)

    def combine(self,*terms:tuple[Any,Field])->Field:
        out={}
        for coefficient,f in terms:
            for z,a in f.items():out[z]=out.get(z,self.zero)+coefficient*a
        return {z:a for z,a in out.items() if a}

    def K(self,f:Field)->Field:
        out={}
        for z,a in f.items():
            out[z]=out.get(z,self.zero)+2*self.total*a
            for i,c in enumerate(self.alpha):
                for d in (-1,1):
                    q=self.shifted(z,i,d)
                    out[q]=out.get(q,self.zero)-c*a
        return {z:a for z,a in out.items() if a}

    def step(self,previous:Field,current:Field,drive:Field|None=None)->Field:
        """drive is the already scaled delta^2 j_m, not an unscaled source."""
        return self.combine((2,current),(-1,previous),(-1,self.K(current)),(1,drive or {}))

    def dot(self,a:Field,b:Field):
        return sum((v*b.get(z,self.zero) for z,v in a.items()),self.zero)

    def energy(self,previous:Field,current:Field):
        v=self.combine((1,current),(-1,previous))
        return (self.dot(v,v)+self.dot(current,self.K(previous)))/2

    def convolution(self,a:Field,b:Field)->Field:
        out={}
        for x,v in a.items():
            for y,w in b.items():
                z=tuple(x[i]+y[i] for i in range(3))
                out[z]=out.get(z,self.zero)+v*w
        return {z:v for z,v in out.items() if v}
