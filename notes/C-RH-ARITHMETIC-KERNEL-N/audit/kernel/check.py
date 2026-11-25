"""Exact candidate-C checks for complete kernels and a finite support-mask witness."""
from fractions import Fraction
from itertools import product
from math import gcd, isqrt, lcm, prod

H = (0, 1, 0, -1, 0)
CHI = (0, 1, -1, -1, 1)


def K(n, d):
    return H[(n // d) % 5]


def period_pair(d, e):
    period = 5 * lcm(d, e)
    return Fraction(sum(K(n, d)*K(n, e) for n in range(period)), period)


def predicted_pair(d, e):
    g = gcd(d, e)
    return Fraction(2 * CHI[(d//g) % 5] * CHI[(e//g) % 5] * g*g, 5*d*e)


def s5(d):
    value = 1
    p = 2
    while p * p <= d:
        if d % p == 0:
            if CHI[p % 5] != 1 or (d // p) % p == 0:
                return 0
            d //= p
            value *= -2
        p += 1
    if d > 1:
        return value * (-2) if CHI[d % 5] == 1 else 0
    return value


def floor_two_thirds(n):
    lo, hi = 0, n + 1
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**3 <= n*n:
            lo = mid
        else:
            hi = mid
    return lo


basis = [x for x in range(1, 37) if x % 5]
for a in basis:
    counts = [sum(K(i, a) for i in range(j, 5*a, 5)) for j in range(5)]
    assert counts == [CHI[a % 5]*h for h in H]
for d, e in product(basis, repeat=2):
    assert period_pair(d, e) == predicted_pair(d, e)
print('Exact CRT residue identities:', len(basis), 'scales;', len(basis)**2, 'complete pair correlations.')

primes = (11, 19)
support = [1, *primes, prod(primes)]
period = 5 * prod(primes)
energy = Fraction(sum(sum(s5(d)*K(n, d) for d in support)**2 for n in range(period)), period)
gram = sum(s5(d)*s5(e)*predicted_pair(d,e) for d,e in product(support, repeat=2))
cube = Fraction(2,5)*prod(5-Fraction(4,p) for p in primes)
assert energy == gram == cube
print('Full divisor cube for primes 11,19: exact mean square', energy)

def is_prime(n):
    return n > 1 and all(n%p for p in range(2, isqrt(n)+1))

X, D = 10000, 300
split_primes = [p for p in range(D,2*D+1) if CHI[p % 5] == 1 and is_prime(p)]
def selected(start):
    return [p for p in split_primes if 3*p <= start % (5*p) < 3*p+p//2]
start = max(range(X, 3*X//2+1), key=lambda n: len(selected(n)))
mask = selected(start)
height = 2*len(mask)
assert mask and all(sum(s5(p)*K(n,p) for p in mask) == height for n in range(start, start + D//2+1))
print('Positive prime mask:', len(mask), 'of', len(split_primes), 'primes; start', start, 'height', height, 'for', D//2+1, 'successive integers.')

weights = [0] + [s5(d) for d in range(1,513)]
prefix = [sum(weights[:d+1]) for d in range(513)]
for n in range(1,513):
    k = floor_two_thirds(n)
    small = sum(weights[d]*K(n,d) for d in range(1, k+1))
    large = sum(weights[d]*K(n,d) for d in range(k+1,n+1))
    quotient_sum = sum(H[j%5]*(prefix[n//j]-prefix[max(k,n//(j+1))])
                       for j in range(1,n//(k+1)+1))
    assert large == quotient_sum
    assert small + large == sum(weights[d]*K(n,d) for d in range(1,n+1))
print('Moving integer cutoff and exact complementary quotient formula:', 512, 'integers.')
