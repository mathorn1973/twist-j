"""SOFTWARE regression; reference is a separate pinned implementation."""
import hashlib
import importlib.util
import random
import unittest
from pathlib import Path
from dataclasses import replace
import runtime as impl


def reference():
    path = Path(__file__).resolve().parents[1] / 'C-FIELD-WORK-RECORD-UNIT-N/challenger.py'
    source = path.read_bytes()
    expected = '5067aa1f50b433d6c1ddd50c00f40151164982226b665e51728a211e184c072c'
    if hashlib.sha256(source).hexdigest() != expected:
        raise RuntimeError('reference pin changed')
    spec = importlib.util.spec_from_file_location('independent_v96_reference', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def cases():
    ref = reference()
    # Shared LOGICAL cases, not analog confirmation or the reserved holdout.
    for off in (False, True):
        for cut in (None, 0, 1):
            state = ref.initial(3, (0, 0, 1, 0), offimage=off)
            for _ in range(10):
                for _, state in ref.layers(state, 3, cut=cut):
                    yield state
    from itertools import product
    hs = {}
    for v in product(range(-2, 3), repeat=4):
        h = impl.quadratic(impl.H, v)//2
        if 0 <= h <= 4:
            hs.setdefault(h, v)
    for h, v in hs.items():
        for matter, field, resource in ((impl.R, impl.mv(impl.L,v), max(0,2-4*h)),
                                        (impl.AM, v, max(0,4*h-2))):
            cell = matter + (0,)*12 + impl.mv(impl.P,field)+(resource,)
            state = [0]*62 + list(cell) + [0,0]
            state[93] = 41-sum(impl.bank_counts(tuple(state)))
            if state[93] >= 0:
                for p in range(5):
                    yield tuple(state)+(p,)
    rng = random.Random(9603)
    # Literal ordering, funding rejections, nonsplit and offimage fields.
    for matter,raw,r in ((impl.AM,impl.mv(impl.P,hs[h]),0) for h in range(1,5)):
        state=[0]*62+list(matter+(0,)*12+raw+(r,))+[0,0]
        state[93]=41-sum(impl.bank_counts(tuple(state)))
        if state[93]>=0: yield tuple(state)+(0,)
    for matter in (impl.R[4:8]+impl.R[:4]+impl.R[8:],impl.AM[4:8]+impl.AM[:4]+impl.AM[8:]):
        state=[0]*62+list(matter+(0,)*18+(0,))+[0,0]
        state[93]=41-sum(impl.bank_counts(tuple(state)))
        yield tuple(state)+(0,)
    for _ in range(160):
        state = [0]*95
        cell = rng.randrange(3)*31
        state[cell:cell+12] = rng.choice((impl.R, impl.AM, (0,)*12))
        state[cell+12+4*rng.randrange(3)+rng.randrange(4)] = rng.choice((-1,0,1))
        state[cell+24:cell+30] = [rng.randrange(-1,2) for _ in range(6)]
        remaining = 41-sum(impl.bank_counts(tuple(state)))
        if remaining < 0:
            continue
        for index in (30,61,92,93):
            take = rng.randrange(remaining+1)
            state[index] = take
            remaining -= take
        state[94] = remaining
        yield tuple(state)+(rng.randrange(5),)


class RuntimeTests(unittest.TestCase):
    def test_layer_reference_and_inverse(self):
        ref = reference()
        for state in cases():
            for inverse in (False, True):
                for cut in (None,0,1):
                    current = state
                    for kind, expected in ref.layers(state,3,cut=cut,inverse=inverse):
                        out,p = impl.layer(current[:-1],current[-1],kind[0],inverse=inverse,
                                           cuts=0 if cut is None else 1<<cut)
                        self.assertEqual(out+(p,),expected)
                        restored,rp = impl.layer(out,p,kind[0],inverse=not inverse,
                                                cuts=0 if cut is None else 1<<cut)
                        self.assertEqual(restored+(rp,),current)
                        current = expected

    def test_parameterized(self):
        ref = reference()
        for n in (2,4,8,16):
            state = ref.initial(n,(0,0,1,0))
            current = state
            for kind, expected in ref.layers(state,n):
                out,p = impl.layer(current[:-1],current[-1],kind,n=n)
                self.assertEqual(out+(p,),expected)
                current=expected

    def test_invalid_inputs(self):
        state=next(cases())
        for p in (-1,5,True):
            with self.assertRaises(ValueError): impl.validate(state[:-1],p)
        for index,value in ((0,32767),(0,10**100),(30,-1),(94,42)):
            bad=list(state[:-1]);bad[index]=value
            with self.assertRaises(ValueError): impl.layer(bad,0,'G')
        with self.assertRaises(ValueError): impl.validate([0]*95,0)

    def test_faults_are_absorbing(self):
        state=next(cases())
        healthy=impl.Confirmation(True,True,True,True,True,True,True,0,0,0,True,0,voltage_ok=True)
        for field in ('measured','adc_ok','samples_complete','dock_identity_ok',
                      'reserve_ok','energy_bounds_ok','p_valid','disconnected','voltage_ok'):
            controller=impl.Controller(state[:-1],state[-1])
            controller.plan(state[-1])
            with self.assertRaises(RuntimeError): controller.confirm(replace(healthy,**{field:False}))
            self.assertEqual(controller.phase,'ERROR')
            with self.assertRaises(RuntimeError): controller.plan(0)
        for change in ({'cut_a':1},{'cut_b':1},{'elapsed_us':1700001},{'elapsed_us':-1}):
            controller=impl.Controller(state[:-1],state[-1]);controller.plan(state[-1])
            with self.assertRaises(RuntimeError): controller.confirm(replace(healthy,**change))

    def test_commit_needs_physical_pointer(self):
        ref=reference()
        state=ref.initial(3,(0,0,1,0))
        for _ in range(2): state=ref.step(state,3)
        controller=impl.Controller(state[:-1],state[-1])
        _,(candidate,p)=controller.plan(state[-1])
        self.assertEqual(p,1)
        healthy=impl.Confirmation(True,True,True,True,True,True,True,0,0,0,True,0,voltage_ok=True)
        self.assertFalse(controller.confirm(healthy))
        self.assertEqual(controller.registers,state[:-1])
        self.assertFalse(controller.confirm(replace(healthy,operation_done=True,elapsed_us=1000)))
        with self.assertRaises(RuntimeError): controller.confirm(replace(healthy,elapsed_us=2000000))
        self.assertEqual(controller.phase,'ERROR')
        self.assertEqual(controller.registers,state[:-1]) # stale, invalid physical state

    def test_interface_types_windows_and_success(self):
        state=reference().initial(3,(0,0,1,0))
        healthy=impl.Confirmation(True,True,True,True,True,True,True,0,0,0,True,0,voltage_ok=True)
        for changes in ({'pointer':False},{'pointer':0.0},{'cut_a':False},{'cut_b':0.0}):
            controller=impl.Controller(state[:-1],0);controller.plan(0)
            with self.assertRaises(RuntimeError): controller.confirm(replace(healthy,**changes))
        controller=impl.Controller(state[:-1],0)
        with self.assertRaises(RuntimeError): controller.plan(5)
        self.assertEqual(controller.phase,'ERROR')
        controller=impl.Controller(state[:-1],0);_,(candidate,p)=controller.plan(0)
        controller.confirm(healthy)
        controller.confirm(replace(healthy,operation_done=True,elapsed_us=1000))
        self.assertTrue(controller.confirm(replace(healthy,pointer=p,elapsed_us=2000000)))
        self.assertEqual(controller.registers,candidate)


if __name__ == '__main__': unittest.main()
