#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""Frozen exact co-located paid readout and during-path recorder audit."""
import itertools
import json

ZERO = (0, 0, 0, 0)
ONE = (1, 0, 0, 0)
JROOT = (0, 1, 0, 0)
RHO = (0, 0, 1, 0)
JINV = (0, -1, -1, 0)
checks = 0


def ck(test, label):
    global checks
    checks += 1
    if not test:
        raise AssertionError(label)


def add(a, b):
    return tuple(x+y for x, y in zip(a, b))


def neg(a):
    return tuple(-x for x in a)


def sub(a, b):
    return add(a, neg(b))


def scale(n, a):
    return tuple(n*x for x in a)


def mul(a, b):
    c = [0]*7
    for k in range(4):
        for l in range(4):
            c[k+l] += a[k]*b[l]
    for k in range(6, 3, -1):
        for l in range(1, 5):
            c[k-l] -= c[k]
    return tuple(c[:4])


def power(a, n):
    out = ONE
    for _ in range(n):
        out = mul(out, a)
    return out


ROOTS = tuple(power(JROOT, k) for k in range(5))


def total(items):
    out = ZERO
    for a in items:
        out = add(out, a)
    return out


def conj(a):
    return total(scale(v, ROOTS[-k % 5]) for k, v in enumerate(a))


def h(a):
    return mul(a, conj(a))


def q(a):
    value = 5*sum(x*x for x in a)-sum(a)**2
    ck(value % 2 == 0, 'integral Q')
    return value//2


def real(a, b):
    return (a, 0, -b, -b)


def ordinary(a, b):
    delta = sub(a, b)
    if any(v % 2 for v in delta):
        return a, b, False, ZERO
    t = tuple(v//2 for v in delta)
    c = tuple(v//2 for v in add(a, b))
    r = mul(RHO, t)
    return add(c, r), sub(c, r), True, h(t)


def loaded(x, v, field):
    numerator = add(sub(scale(2, v), x), field)
    if any(a % 4 for a in numerator):
        return x, v, field, False
    d = tuple(a//4 for a in numerator)
    current = mul(sub(RHO, ONE), d)
    return sub(x, current), add(v, current), add(field, current), True


def account(slots, field, norm):
    values = [norm(slots[0]), norm(field)]
    for v in slots[1:]:
        values.extend((norm(v), norm(ZERO), norm(sub(v, ZERO))))
    return sum(values) if norm is q else total(values)


def stats():
    return dict(attempts=0, admitted=0, changed=0, diagonal=0, field_changes=0)


class Device:
    def __init__(self, slots, label):
        self.slots = tuple(slots)
        self.field = neg(slots[0])
        self.label = label
        self.initial = (self.slots, self.field)
        self.energy = account(self.slots, self.field, q)
        self.hermitian = account(self.slots, self.field, h)
        self.residues = tuple(sum(v) % 5 for v in self.slots)
        self.field_residue = sum(self.field) % 5
        self.counts = stats()
        self.area = ZERO
        self.sections = {}
        ck(total(slots) == ZERO, label+' initial neutrality')

    def step(self, edge, section):
        a, b = edge
        old, old_f = self.slots, self.field
        shadow = list(old)
        shadow[a], shadow[b], shadow_yes, increment = ordinary(old[a], old[b])
        shadow_f = add(old_f, sub(old[0], shadow[0]))
        actual = list(old)
        if 0 in edge:
            v = b if a == 0 else a
            actual[0], actual[v], self.field, yes = loaded(old[0], old[v], old_f)
        else:
            actual[a], actual[b], yes, _ = ordinary(old[a], old[b])
        self.slots = tuple(actual)
        cut = self.counts['attempts']+1
        tag = f'{self.label} cut{cut} {section} {edge}'
        ck((self.slots, self.field, yes) == (tuple(shadow), shadow_f, shadow_yes),
           tag+' shadow')
        ck(neg(self.field) == self.slots[0] and self.field == total(self.slots[1:]), tag+' Gauss')
        ck(total(self.slots) == ZERO, tag+' charge')
        ck(account(self.slots, self.field, q) == self.energy, tag+' complete E')
        ck(account(self.slots, self.field, h) == self.hermitian, tag+' complete H_account')
        ck(tuple(sum(v) % 5 for v in self.slots) == self.residues, tag+' residues')
        ck(sum(self.field) % 5 == self.field_residue, tag+' field residue')
        sec = self.sections.setdefault(section, {'area': ZERO, 'counts': stats()})
        for counts in (self.counts, sec['counts']):
            counts['attempts'] += 1
            counts['admitted'] += yes
            counts['changed'] += old != self.slots
            counts['diagonal'] += yes and old == self.slots
            counts['field_changes'] += old_f != self.field
        self.area = add(self.area, increment)
        sec['area'] = add(sec['area'], increment)

    def apply(self, word, section):
        for edge in word:
            self.step(edge, section)


def inverse(word):
    return [edge for edge in reversed(word) for _ in range(4)]


def pword(i, j):
    a = (2*i, 2*i+1)
    k = [(2*i, 2*j+1), (2*i+1, 2*j)]
    out = []
    for n in range(1, 5):
        out.append(a)
        out.extend(k*n)
    return out+[a]


def pair_state(phases):
    return tuple(v for p in phases for v in (ROOTS[p % 5], neg(ROOTS[p % 5])))


def paid_audit():
    rstock = (3, 4, 2, 0)
    word = pword(0, 1)*2+pword(0, 2)*2+pword(1, 2)*2
    reader = [(2, 6), (2, 3)]*5
    stock_states = [(3,4,2,0),(2,3,3,1),(1,1,1,1),(1,0,-1,-1),(3,2,0,-1)]
    stock_q = [32,17,2,7,27]
    memory_q = [4,19,34,29,9]
    rows = []
    for r, s, t in itertools.product(range(5), repeat=3):
        start = pair_state((r,s,t))+(rstock,neg(rstock))
        dev = Device(start, f'paid {(r,s,t)}')
        ck(dev.energy == 152 and dev.hermitian == real(48,56), 'paid account fixture')
        dev.apply(word, 'writer')
        phase = ((r+3*s+2*t)%5, (r+4*s+t)%5, (2*s+4*t)%5)
        ck(dev.slots[:6] == pair_state(phase), 'actual writer phase matrix')
        ck(dev.slots[6:] == start[6:], 'stocks untouched during writer')
        before = (dev.slots, dev.field)
        if t == s:
            ck(phase == (r,r,s), 'writer family copy')
            ck(dev.slots[:2] == start[:2] and dev.slots[4:6] == start[4:6]
               and dev.field == dev.initial[1], 'writer family returns')
        for edge in reader:
            dev.step(edge, 'reader')
            ck(dev.slots[:2] == before[0][:2] and dev.slots[4:6] == before[0][4:6]
               and dev.field == before[1], 'source reference field fixed through read')
            ck(total(dev.slots[k] for k in (2,3,6,7)) == ZERO, 'complete read archive neutral')
        b = phase[1]
        ck(dev.slots[6] == stock_states[b], 'stock coordinate response')
        sq = q(dev.slots[6]); mq = q(dev.slots[2])+q(dev.slots[3])
        ck(sq == stock_q[b] and mq == memory_q[b], 'paid response accounts')
        rc = dev.sections['reader']['counts']
        ck(rc['admitted'] == (6 if b == 0 else 5) and rc['diagonal'] == 0
           and rc['field_changes'] == 0, 'reader branches')
        final_field = dev.field
        rows.append({'input':[r,s,t], 'writer_phase':list(phase), 'stock':list(dev.slots[6]),
                     'stock_q':sq, 'memory_q':mq, 'account':dev.energy,
                     'field_returned':final_field == dev.initial[1],
                     'counts':dict(dev.counts), 'reader_counts':dict(rc),
                     'area':list(dev.area)})
        dev.apply(inverse(reader), 'read_inverse')
        ck((dev.slots, dev.field) == before, 'receiver inverse boundary')
        dev.apply(inverse(word), 'writer_inverse')
        ck((dev.slots, dev.field) == dev.initial, 'paid full inverse')
        ck(dev.counts['attempts'] == 800, 'paid roundtrip count')
    return {'rows':rows, 'inputs':125, 'writer_inputs':25, 'account':152,
            'forward_attempts':160, 'inverse_attempts':640}


def source_words():
    raw = '12 12 12 12 35 36 16 16 16 16 46 46 46 46 24 36 36 36 36 16 12 12 46 45 45 45 45'
    p27 = [(int(v[0])-1, int(v[1])-1) for v in raw.split()]+[(0,2)]*8
    p35 = [(0,1)]*5+([(2,4)]+[(2,5)]*5+[(2,4)]*4)*3
    ck(len(p27) == len(p35) == 35, 'source word lengths')
    return [('P27',p27),('P35',p35)]


def path_audit():
    B = sub(ONE,RHO); u = sub(ONE,JROOT); X = (1,1,0,-2)
    source = (B,neg(B),u,u,X,scale(2,ONE))
    companion = neg(total(source))
    a = [B,mul(B,power(RHO,4))]
    c = [mul(v,JINV) for v in a]
    helpers = [add(v,scale(2,cc)) for v,cc in zip(a,c)]
    delta = [mul(sub(ONE,RHO),v) for v in c]
    archive = tuple(v for helper in helpers for v in (helper,ZERO,neg(helper)))
    start = source+(companion,)+archive
    port = [(0,7),(0,8),(0,10),(0,11)]
    ck(c[0] == (-1,-2,-2,0) and helpers[0] == (-1,-4,-5,0), 'selector coefficients')
    ck(h(c[0]) == real(3,4) and h(helpers[0]) == real(18,19)
       and h(delta[0]) == real(10,15), 'selector norm fixtures')
    rows = []
    for name, sourceword in source_words():
        baseline = [source]
        shadow = list(source)
        for i,j in sourceword:
            shadow[i],shadow[j],_,_ = ordinary(shadow[i],shadow[j])
            baseline.append(tuple(shadow))
        ck(baseline[-1] == source, name+' source closure')
        ck(baseline[5][0] == a[1 if name == 'P27' else 0], name+' source cut5')
        for timing in ('cut5','omitted','delayed'):
            dev = Device(start, name+' '+timing)
            ck(dev.energy == 672, 'path initial full E')
            word = []
            retained = None
            insert_after = 5 if timing == 'cut5' else (35 if timing == 'delayed' else None)
            for count, edge in enumerate(sourceword,1):
                dev.step(edge,'source'); word.append(edge)
                ck(dev.slots[:6] == baseline[count], 'uninstrumented source boundary')
                if retained is not None:
                    ck(dev.slots[7:] == retained, 'retained archive during source tail')
                if count == insert_after:
                    before = (dev.slots[:7],dev.field)
                    dev.apply(port,'port'); word.extend(port)
                    ck((dev.slots[:7],dev.field) == before, 'port restores complete source and field')
                    ck(dev.slots[:6] == baseline[count], 'post-port source boundary')
                    retained = dev.slots[7:]
            target = list(start)
            selected = None if timing == 'omitted' else (1 if timing == 'cut5' and name == 'P27' else 0)
            if selected is not None:
                target[7+3*selected] = scale(2,a[selected])
                target[8+3*selected] = delta[selected]
            ck(dev.slots == tuple(target) and dev.field == dev.initial[1], 'exact path endpoint')
            response = [q(dev.slots[8]),q(dev.slots[11])]
            expected_response = [0,0] if selected is None else ([35,0] if selected == 0 else [0,35])
            ck(response == expected_response, 'current record response')
            ck(dev.sections['source']['area'] == real(55,20), 'source area')
            expected_area = real(55,20) if selected is None else real(61,28)
            ck(dev.area == expected_area, 'complete area including recorder')
            if selected is not None:
                ck(dev.sections['port']['area'] == real(6,8), 'port area')
                ck(dev.sections['port']['counts']['admitted'] == 2, 'port admissions')
            admissions = (27 if name == 'P27' else 35)+(0 if selected is None else 2)
            ck(dev.counts['admitted'] == admissions and dev.counts['diagonal'] == 0,
               'whole word branch count')
            det = power(RHO,admissions)
            rows.append({'path':name, 'timing':timing, 'response':response,
                         'slots':[list(v) for v in dev.slots], 'field':list(dev.field),
                         'account':dev.energy, 'hermitian_account':list(dev.hermitian),
                         'area':list(dev.area), 'source_area':list(dev.sections['source']['area']),
                         'port_area':list(dev.sections.get('port',{'area':ZERO})['area']),
                         'determinant':list(det), 'counts':dict(dev.counts)})
            dev.apply(inverse(word),'inverse')
            ck((dev.slots,dev.field) == dev.initial, 'path full inverse')
            ck(dev.counts['attempts'] == 5*len(word), 'path roundtrip length')
    return {'rows':rows, 'inputs':6, 'account':672}


def main():
    a = paid_audit()
    b = path_audit()
    print(json.dumps({'status':'PASS','paid_readout':a,'path_record':b,'checks':checks},
                     sort_keys=True,separators=(',',':')))


if __name__ == '__main__':
    main()
