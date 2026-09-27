#!/usr/bin/env python3
"""Exact selected point bridge from reachable native U to Hodge event mesh."""
from pathlib import Path
import contextlib, hashlib, importlib.util, io, runpy

ROOT=Path(__file__).resolve().parents[2]
COUNTER=ROOT/'probes/P-U-COUNTER-AMPLITUDE-CLASS-1/verify.py'
COUNTER_SHA='d811afdd74cc11891282d93bf4575e7fc087a2ee209d74729e4ba1e3feb0e703'
EVENT=ROOT/'notes/C-HODGE-EVENT-CAUCHY-N/model.py'
EVENT_SHA='adc99adac6ff1e3d9e76d4952b97af16fcdbe919021c5947bdb6c0feb7b3a772'

def _checked_modules():
    if hashlib.sha256(COUNTER.read_bytes()).hexdigest()!=COUNTER_SHA:
        raise RuntimeError('STOP: counter source hash mismatch')
    if hashlib.sha256(EVENT.read_bytes()).hexdigest()!=EVENT_SHA:
        raise RuntimeError('STOP: event source hash mismatch')
    with contextlib.redirect_stdout(io.StringIO()):
        native=runpy.run_path(str(COUNTER))
    spec=importlib.util.spec_from_file_location('hodge_event_model',EVENT)
    event=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(event)
    return native,event.Model()

NATIVE,EVENT_MODEL=_checked_modules()

def site(label):
    """Fixed faithful integer lift F5^5 -> Z^3."""
    a,b,c,d,e=(int(x)%5 for x in label)
    return (a+5*b,c+5*d,e)

def bridge_site(n,checkpoint):
    return site(NATIVE['label_at'](n,checkpoint))

def bridge_event(scale,n,checkpoint):
    return EVENT_MODEL.event(scale,n,bridge_site(n,checkpoint))

def bridge_event_label(scale,n,checkpoint):
    return EVENT_MODEL.event_label(scale,n,bridge_site(n,checkpoint))

def step_checkpoint(n,checkpoint):
    return NATIVE['edge'](NATIVE['theta'](n),checkpoint)
