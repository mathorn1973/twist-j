#!/usr/bin/env python3
"""Source-exposed finite correction audit, not a replay of either old audit.

P-U-NONLINEAR-AUDIT-ERRATA-1; A. M. Thorn; Apache-2.0.
Only this new program's first output is evidence of a new execution.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import product
import json
from pathlib import Path

NAME = "P-U-NONLINEAR-AUDIT-ERRATA-1"
F5 = range(5)
HERE = Path(__file__).resolve().parent


class ExactFailure(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ExactFailure(message)


def mod(values):
    return tuple(v % 5 for v in values)


def chart(x):
    a, b, c, d, q, r = x
    return mod((a+b+c+d+q+r, a+c, b+d, a-c-2, b-d-1, q))


def unchart(y):
    z, A, B, C, D, q = y
    return mod((3*(A+C+2), 3*(B+D+1), 3*(A-C-2),
                3*(B-D-1), q, z-A-B-q))


def g(j, x):
    a, b, c, d, q, r = x
    if j == 0:
        raw = (b,a,d,c,q,r)
    elif j == 1:
        raw = (-c,-d,-a,-b,-q,-r)
    elif j == 2:
        raw = (2-c,1-d+r,2-a,1-b-r,1-q,-r)
    elif j == 3:
        raw = (2-a,1-b,3-c,4-d,1-q,1-r)
    elif j == 4:
        raw = (2-a,1-b,3-c,4-d,2-q,1-r)
    else:
        raise ValueError("invalid generator")
    return mod(raw)


def g_chart(j, y):
    z,A,B,C,D,q = y
    r = (z-A-B-q) % 5
    rows = ((z,B,A,D-1,C+1,q),
            (-z,-A,-B,C,D,-q),
            (2-z,4-A,2-B,C,D+2*r,1-q),
            (2-z,-A,-B,-C,-D,1-q),
            (3-z,-A,-B,-C,-D,2-q))
    return mod(rows[j])


def step(t, x):
    return g((sum(x)+2*t) % 5, x)


def qstep(t, v):
    z,q,r = v
    j = (z+2*t) % 5
    rows = ((z,q,r),(-z,-q,-r),(2-z,1-q,-r),
            (2-z,1-q,1-r),(3-z,2-q,1-r))
    return mod(rows[j])


def quotient(x):
    return (sum(x) % 5, x[4], x[5])


def theta(n):
    return bin(n).count("1") % 2


def phi(x):
    z,A,B,C,D,q = chart(x)
    if z == 0:
        return (z,C,A,B,D,q)
    if z == 2:
        return (z,q,A,B,C,D)
    if z in (1,4):
        tau = (z*A**3+1-A**4) % 5
        return (z,tau*D % 5,A,B,C,q)
    return (z,D,A,B,C,q)


def phi_inverse(y):
    z,T,A,B,V,W = y
    if z == 0:
        C,D,q = T,V,W
    elif z == 2:
        C,D,q = V,W,T
    elif z in (1,4):
        C,D,q = V,((z*A+1-A**4)*T) % 5,W
    else:
        C,D,q = V,T,W
    return unchart((z,A,B,C,D,q))


def labels(x):
    z,A,B,C,D,q = chart(x)
    require(z in (1,4) and A != 0, "label domain")
    return (z*pow(A,3,5)*C % 5, z*pow(A,3,5)*D % 5)


def semantic(x):
    z,T = phi(x)[:2]
    return ("BLANK",) if z in (2,3) else ("PRESENT",T)


def prepare(lam, mu):
    return mod((3*(lam+3),3*(mu+1),3*(-lam-1),3*(-mu-1),0,1))


def tail(lam, mu):
    return {unchart((z,A,0,lam*A*z % 5,mu*A*z % 5,q))
            for z in (1,4) for A in (1,4) for q in F5}


# Canonical polynomial functions in six independent affine coordinates.
# x^5=x is applied to exponents; each coordinate degree is at most four.
ZERO = (0,0,0,0,0,0)


def constant(c):
    return {ZERO: c % 5} if c % 5 else {}


def variable(i):
    e = [0]*6
    e[i] = 1
    return {tuple(e): 1}


def p_add(*polys):
    out = {}
    for p in polys:
        for e,c in p.items():
            out[e] = (out.get(e,0)+c) % 5
    return {e:c for e,c in out.items() if c}


def p_scale(p, n):
    return {e:c*n % 5 for e,c in p.items() if c*n % 5}


def p_mul(a, b):
    out = {}
    for e,c in a.items():
        for f,d in b.items():
            r = tuple(0 if u+v == 0 else 1+(u+v-1) % 4
                      for u,v in zip(e,f))
            out[r] = (out.get(r,0)+c*d) % 5
    return {e:c for e,c in out.items() if c}


def p_pow(a, n):
    out = constant(1)
    for _ in range(n):
        out = p_mul(out,a)
    return out


def p_eval(p, y):
    powers = [[pow(v,n,5) for n in range(5)] for v in y]
    ans = 0
    for exponents,coeff in p.items():
        term = coeff
        for i,n in enumerate(exponents):
            term = term*powers[i][n] % 5
        ans = (ans+term) % 5
    return ans


def audit_local_inputs():
    expected = {"PREREG.md","PROOF.md","CUSTODY.md","README.md",
                "SOURCES.tsv","verify.py"}
    rows = (HERE/"INPUTS.sha256").read_text(encoding="utf-8").splitlines()
    seen = set()
    for row in rows:
        digest,name = row.split()
        require(name in expected and name not in seen, "local manifest name")
        seen.add(name)
        require(sha256((HERE/name).read_bytes()).hexdigest() == digest,
                "local input hash " + name)
    require(seen == expected, "local manifest incomplete")
    return {"local_files":len(seen), "external_source_check":"pre-pin_git_object_readback"}


def audit_native():
    counts = [Counter(),Counter()]
    frame_checks = 0
    quotient_checks = 0
    chart_checks = 0
    for x in product(F5,repeat=6):
        y = chart(x)
        require(unchart(y)==x and chart(unchart(x))==x, "affine chart inverse")
        require(phi_inverse(phi(x))==x and phi(phi_inverse(x))==x,
                "nonlinear chart inverse")
        chart_checks += 4
        for j in range(5):
            gx = g(j,x)
            require(g(j,gx)==x, "generator not involutive")
            require(chart(gx)==g_chart(j,y), "raw/frame generator mismatch")
            frame_checks += 1
        for t in (0,1):
            sx = step(t,x)
            counts[t][sx] += 1
            require(quotient(sx)==qstep(t,quotient(x)), "quotient mismatch")
            quotient_checks += 1
    require(len(counts[0])==6250, "T0 image")
    require(Counter(counts[0].values())=={2:3125,3:3125}, "T0 fibres")
    require(len(counts[1])==9375, "T1 image")
    require(Counter(counts[1].values())=={1:6250,3:3125}, "T1 fibres")
    return {"states":15625,"generator_frame_checks":frame_checks,
            "chart_inverse_checks":chart_checks,"quotient_edges":quotient_checks,
            "T0_image":len(counts[0]),"T0_fibres":{"2":3125,"3":3125},
            "T1_image":len(counts[1]),"T1_fibres":{"1":6250,"3":3125}}


def audit_tail_images():
    x = (4,3,2,2,0,0)
    y = (4,3,2,2,2,1)
    image = (3,3,1,2,0,0)
    require(x != y and x in tail(0,0) and y in tail(0,0), "collision inputs")
    require(step(0,x)==image==step(0,y), "collision missing")
    union = set()
    edge_count = 0
    inverse_count = 0
    restricted_bijections = 0
    for lam,mu in product(F5,repeat=2):
        family = tail(lam,mu)
        require(len(family)==20 and union.isdisjoint(family), "tail partition")
        union.update(family)
        for t in (0,1):
            target_z = (4+2*t) % 5
            target = {x for x in family if sum(x) % 5 == target_z}
            outputs = Counter(step(t,x) for x in family)
            require(set(outputs)==target and len(target)==10, "exact image sheet")
            require(set(outputs.values())=={2}, "tail must be two-to-one")
            edge_count += len(family)
            for source_z in (1,4):
                source = {x for x in family if sum(x) % 5 == source_z}
                j = (source_z+2*t) % 5
                require({step(t,x) for x in source}==target, "restricted image")
                require({g(j,y) for y in target}==source, "restricted inverse image")
                for a in source:
                    require(g(j,step(t,a))==a, "left inverse with known sheet")
                    inverse_count += 1
                for b in target:
                    require(step(t,g(j,b))==b, "right inverse with known sheet")
                    inverse_count += 1
                restricted_bijections += 1
    require(len(union)==500, "tail union")
    return {"pairs":25,"tail_states":500,"edges":edge_count,
            "fixed_bit_tail_image":10,"fixed_bit_multiplicity":2,
            "sheet_bijections":restricted_bijections,
            "inverse_compositions":inverse_count,"collision":list(image)}


def audit_retention():
    invariant_states = 0
    invariant_edges = 0
    for x in product(F5,repeat=6):
        z,A,B,C,D,q = chart(x)
        if z not in (1,4) or A == 0:
            continue
        invariant_states += 1
        lab = labels(x)
        require(semantic(x)==("PRESENT",lab[1]), "invariant readout")
        for t in (0,1):
            y = step(t,x)
            yz,yA,*_ = chart(y)
            require(yz in (1,4) and yA != 0, "invariant carrier closure")
            require(labels(y)==lab, "invariant changed")
            invariant_edges += 1
    require((invariant_states,invariant_edges)==(5000,10000), "invariant counts")
    prefix_states = {pair:prepare(*pair) for pair in product(F5,repeat=2)}
    original = dict(prefix_states)
    history_checks = 0
    # Only 0..32 is a regression. The all-time proof is the finite edge identity.
    for n in range(33):
        require(len(set(prefix_states.values()))==25, "prepared family merged")
        require(len({quotient(x) for x in prefix_states.values()})==1,
                "prepared quotient not common")
        require(len({x[:4] for x in prefix_states.values()})==25,
                "prepared piston blocks not distinct")
        selected = {(sum(x)+2*theta(n)) % 5 for x in prefix_states.values()}
        require(len(selected)==1, "prepared word not common")
        for (lam,mu),x in prefix_states.items():
            expected = ("BLANK",) if n in (0,2) else ("PRESENT",lam if n==1 else mu)
            require(semantic(x)==expected, "prepared semantic trace")
            if n == 2:
                require(x==original[(lam,mu)], "checkpoint restoration")
            if n >= 3:
                require(labels(x)==(lam,mu) and x in tail(lam,mu), "tail base/retention")
                require(chart(x)[0]==(4+2*theta(n-1)) % 5, "actual time phase")
                require(chart(x)[1]==pow(4,n,5), "actual time A sign")
            history_checks += 1
        if n < 3:
            require(next(iter(selected))==(2,2,4)[n], "prefix selector")
        if n < 32:
            prefix_states={pair:step(theta(n),x) for pair,x in prefix_states.items()}
    return {"invariant_states":invariant_states,"invariant_edges":invariant_edges,
            "prepared_pairs":25,"regression_checkpoints":history_checks,
            "regression_last_n":32,"all_time_basis":"invariant_induction"}


def audit_polynomial():
    one = constant(1)
    z,A,B,C,D,q = (variable(i) for i in range(6))
    e = [p_add(one,p_scale(p_pow(p_add(z,constant(-j)),4),-1)) for j in F5]
    tau = p_add(p_mul(z,p_pow(A,3)),one,p_scale(p_pow(A,4),-1))
    T = p_add(p_mul(e[0],C),p_mul(e[2],q),
              p_mul(p_mul(p_add(e[1],e[4]),tau),D),p_mul(e[3],D))
    require(p_add(e[1],e[4])==p_add(p_scale(p_pow(z,4),3),p_scale(p_pow(z,2),3)),
            "indicator sum")
    degree = max(map(sum,T))
    require(degree==9 and T.get((4,4,0,0,1,0))==2, "global degree witness")
    count = 0
    for y in product(F5,repeat=6):
        require(p_eval(T,y)==phi(unchart(y))[1], "polynomial/chart value mismatch")
        count += 1
    return {"variables":"z,A,B,C,D,q","reduced_degree":degree,
            "z4_A4_D_coefficient":2,"evaluation_points":count,
            "scope":"this_global_reader_not_minimum_over_readers"}


def audit_historical_fixture():
    fixture = {(z,q,(z-A-q) % 5) for z in (1,4) for A in (1,4) for q in F5}
    require(len(fixture)==20, "independent fixture cardinality")
    found = {(2,0,1)}
    pending = [(2,0,1)]
    while pending:
        x = pending.pop()
        for t in (0,1):
            y = qstep(t,x)
            if y not in found:
                found.add(y)
                pending.append(y)
    require(found==fixture|{(2,0,1),(0,1,4)}, "quotient closure set")
    return {"fixture_size":20,"closure_size":22,
            "old_fixture_target_10":False,"old_closure_target_12":False,
            "old_program_executed":False,"historical_capture":"NOT_RECOVERED"}


def main() -> int:
    stages = (("inputs",audit_local_inputs),("native",audit_native),
              ("tail_images",audit_tail_images),("retention",audit_retention),
              ("polynomial",audit_polynomial),("historical_fixture",audit_historical_fixture))
    for index,(name,fn) in enumerate(stages):
        try:
            result = fn()
        except ExactFailure as exc:
            print("FAIL "+name+" "+str(exc))
            print("NOT_RUN "+",".join(n for n,_ in stages[index+1:]))
            print(NAME+" SCIENTIFIC_FAIL")
            return 0
        print(name.upper()+" "+json.dumps(result,sort_keys=True,separators=(",",":")))
    print(NAME+" PASS scope=corrected_mathematics historical_custody=HOLD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
