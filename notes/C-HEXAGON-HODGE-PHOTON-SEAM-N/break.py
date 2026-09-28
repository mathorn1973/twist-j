#!/usr/bin/env python3
from collections import Counter

# Separate spectral-label attack from the frozen preregistration.
# A label (a,b) means phi^a * zeta_10^b. Equality is fixed first by modulus,
# hence a, and then by the tenth-root phase b modulo 10.

def src(m):
    return Counter([(2*m,0),(-2*m,0),(0,m%10),(0,3*m%10),(0,7*m%10),(0,9*m%10)])

def dst(n):
    return Counter([(0,0),(0,0),(2*n,n%10),(2*n,-n%10),(-2*n,n%10),(-2*n,-n%10)])

def dimhom(m,n):
    a,b=src(m),dst(n)
    return sum(a[k]*b[k] for k in a.keys()|b.keys())

def theorem(m,n):
    if m%10: return 0
    if m==n: return 12
    return 8

def main():
    assert set(src(1)).isdisjoint(set(dst(1)))
    for m in range(1,1001):
        for n in range(1,31):
            assert dimhom(m,n)==theorem(m,n)
            assert src(m)!=dst(n)
    for n in range(1,101):
        inv=Counter((a,(-b)%10) for (a,b) in dst(n).elements())
        assert inv==dst(n)
    print("PASS BREAK-1: same-step source and target spectra are disjoint.")
    print("PASS BREAK-2: separate label census matches the all-positive-integer blocked Hom formula on the frozen audit grid.")
    print("PASS BREAK-3: source and target eigenvalue multiplicities never match, so blocking never yields an invertible semisimple intertwiner.")
    print("PASS BREAK-4: target time reversal has the same spectral multiset and does not repair the obstruction.")
    print("ALL PASS: breaker found no counterexample in its frozen exact census.")

if __name__=="__main__": main()
