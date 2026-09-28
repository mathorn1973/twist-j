#!/usr/bin/env python3
"""Exact append-only selected geometry. Generation ticks are not event time.

No file writes and no external dependencies. Requires a public twist-j tree.
The archive is mathematical decoder output, not native physical memory.
"""
from __future__ import annotations
from collections.abc import Callable, Iterator
from dataclasses import dataclass
from fractions import Fraction
from itertools import product
from pathlib import Path
from typing import Any
import contextlib
import hashlib
import importlib.util
import io
import runpy

ROOT=Path(__file__).resolve().parents[2]
NATIVE='probes/P-U-COUNTER-AMPLITUDE-CLASS-1/verify.py'
NATIVE_HASH='d811afdd74cc11891282d93bf4575e7fc087a2ee209d74729e4ba1e3feb0e703'
EVENT='notes/C-HODGE-EVENT-CAUCHY-N/model.py'
EVENT_HASH='adc99adac6ff1e3d9e76d4952b97af16fcdbe919021c5947bdb6c0feb7b3a772'
Site=tuple[int,int,int]
Address=tuple[int,Site]
Pair=tuple[Fraction,Fraction]


def _checked(path:str,digest:str)->Path:
    p=ROOT/path
    if hashlib.sha256(p.read_bytes()).hexdigest()!=digest:
        raise RuntimeError('STOP: inherited source hash mismatch: '+path)
    return p


def dependencies():
    with contextlib.redirect_stdout(io.StringIO()):
        native=runpy.run_path(str(_checked(NATIVE,NATIVE_HASH)))
    p=_checked(EVENT,EVENT_HASH)
    spec=importlib.util.spec_from_file_location('selected_event_model',p)
    if spec is None or spec.loader is None:raise RuntimeError('Cannot load event model')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return native,module.Model()


def phi(r:int,x:int,y:int)->Site:
    if r<0 or max(abs(x),abs(y),abs(x-y))>r:
        raise ValueError('Outside the tagged hexagonal ball')
    c=r-max(0,x,y)
    return x+c,y+c,c


def phi_inverse(z:Site)->tuple[int,int,int]:
    if min(z)<0:raise ValueError('Positive cube coordinates required')
    a,b,c=z
    return max(z),a-c,b-c


def shell(r:int,reverse:bool=False)->list[Site]:
    """Signed hex/cube shell with canonical + sign at zero, no duplicates."""
    if r<0:raise ValueError('Nonnegative radius required')
    groups=[[],[],[],[]]
    for x in range(-r,r+1):
        for y in range(max(-r,x-r),min(r,x+r)+1):
            a=phi(r,x,y)
            for signs in product(*[((1,) if v==0 else (-1,1)) for v in a]):
                z=tuple(v*s for v,s in zip(a,signs))
                boundary=sum(abs(v)==r for v in z)
                groups[boundary].append(z)
    return [z for g in groups for z in sorted(g,reverse=reverse)]


def spatial_size(r:int)->int:
    return (2*r+1)**3 if r>=0 else 0


def spacetime_size(r:int)->int:
    return (r+1)**2*(2*(r+1)**2-1) if r>=0 else 0


def adjacent(z:Site)->Iterator[Site]:
    for i in range(3):
        for s in (-1,1):
            v=list(z);v[i]+=s;yield tuple(v)


def predecessors(m:int,z:Site)->tuple[Address,...]:
    if m<2:return ()
    return ((m-1,z),)+tuple((m-1,v) for v in adjacent(z))+((m-2,z),)


def squared_spatial_distance(model:Any,x:tuple,y:tuple):
    """Positive spatial-projection metric, NOT the Lorentz interval."""
    d=[a-b for a,b in zip(x,y)]
    tau=model.time(d)
    return model.inner(d,d)+model.ct*tau*tau


def pack(x:Any)->Pair:return x.a,x.b


@dataclass(frozen=True)
class Record:
    ordinal:int
    address:Address
    coordinates:tuple[Pair,...]
    value:Pair|None
    prior_links:tuple[Address,...]
    shell_radius:int
    shell_bit:int


class Generator:
    """One immutable vertex/event record per checked native transition.

    mode='space': e_h(0,z), spatial neighbors linked at later endpoint.
    mode='field': e_h(m,z), exact inherited scalar values and predecessor links.
    Initial data and source are selected inputs, not inferred from the native head.
    """
    def __init__(self,head:tuple[int,...],h:int=3,mode:str='space',
                 initial:Callable[[int,Site],Any]|None=None,
                 source:Callable[[int,Site],Any]|None=None,
                 loaded:tuple|None=None):
        if len(head)!=6 or any(type(x) is not int or not 0<=x<5 for x in head):
            raise ValueError('A native head is six residues 0,...,4')
        if type(h) is not int or h<3 or mode not in ('space','field'):
            raise ValueError('h>=3 and mode space/field required')
        self.native,self.model=loaded or dependencies()
        self.head=head;self.current=head;self.h=h;self.mode=mode;self.tick=0
        self.initial=initial or (lambda m,z:int(m==1 and z==(0,0,0)))
        self.source=source or (lambda m,z:0)
        self.records:list[Record]=[]
        self.values:dict[Address,Any]={}
        self.positions:dict[Address,tuple]={}
        self._pending:list[Address]=[];self._index=0;self._radius=-1;self._bit=0

    def _coerce(self,x):return x if isinstance(x,self.model.Q) else self.model.Q(x)

    def next_checkpoint(self)->tuple[int,...]:
        return self.native['edge'](self.native['theta'](self.tick),self.current)

    def _open_shell(self):
        self._radius+=1
        selected=(sum(self.current)+2*self.native['theta'](self.tick))%5
        self._bit=selected%2
        if self.mode=='space':
            self._pending=[(0,z) for z in shell(self._radius,bool(self._bit))]
        else:
            self._pending=[(m,z) for m in range(self._radius+1)
                           for z in shell(self._radius-m,bool(self._bit))]
        self._index=0

    def advance(self,next_checkpoint:tuple[int,...]|None=None)->Record:
        expected=self.next_checkpoint()
        if next_checkpoint is not None and tuple(next_checkpoint)!=expected:
            raise ValueError('Illegal native prefix extension')
        if self._index==len(self._pending):self._open_shell()
        m,z=self._pending[self._index];address=(m,z)
        if address in self.positions:raise RuntimeError('Duplicate event')
        M=self.model
        position=tuple(M.event(self.h,m,z))
        value=None
        if self.mode=='space':
            links=tuple((0,v) for v in adjacent(z) if (0,v) in self.positions)
        else:
            links=predecessors(m,z)
            if any(a not in self.values for a in links):
                raise RuntimeError('Missing dependency; no boundary value may be substituted')
            if m<2:value=self._coerce(self.initial(m,z))
            else:
                value=(2-2*M.total)*self.values[(m-1,z)]-self.values[(m-2,z)]
                for i,a in enumerate(M.alpha):
                    for d in (-1,1):
                        v=list(z);v[i]+=d
                        value+=a*self.values[(m-1,tuple(v))]
                value+=self._coerce(self.source(m-1,z))/self.h**2
        record=Record(self.tick,address,tuple(pack(v) for v in position),
                      None if value is None else pack(value),links,self._radius,self._bit)
        self.positions[address]=position
        if value is not None:self.values[address]=value
        self.records.append(record);self._index+=1;self.tick+=1;self.current=expected
        return record

    def run_to(self,count:int)->tuple[Record,...]:
        if type(count) is not int or count<self.tick:
            raise ValueError('Count cannot precede the existing archive')
        while self.tick<count:self.advance()
        return tuple(self.records)


def decode_prefix(history:list[tuple[int,...]],**kwargs)->tuple[Record,...]:
    if not history:raise ValueError('Prefix must include an initial head')
    writer=Generator(tuple(history[0]),**kwargs)
    for state in history[1:]:writer.advance(tuple(state))
    return tuple(writer.records)
