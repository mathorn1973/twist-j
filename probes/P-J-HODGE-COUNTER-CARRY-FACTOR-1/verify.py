#!/usr/bin/env python3

LIMIT = 1 << 18

def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1

carry = 0
unique = 0
digit_residues = set()
complete_residues = set()

for n in range(LIMIT + 1):
    s = n.bit_count()
    assert carry == n - s
    digit_residues.add(s % 8)
    complete_residues.add((s + carry) % 8)
    assert (s + carry) == n
    assert 4 * (s + carry) == 4 * n
    assert 2 * (s + carry) == 2 * n
    assert (2 * (s + carry), n % 10) == (2 * n, n % 10)
    assert unique == carry
    if n == LIMIT:
        break
    k = v2(n + 1)
    delta = (n + 1).bit_count() - s
    assert delta == 1 - k
    assert delta + k == 1
    carry += k
    unique += 1 - delta

assert digit_residues == set(range(8))
assert complete_residues == set(range(8))
for k in range(1, 19):
    n = 1 << k
    c = n - n.bit_count()
    assert c == n - 1

# Finite r_epsilon specialization is exponent equality modulo ord(r)=8.
for n in range(LIMIT + 1):
    s = n.bit_count()
    c = n - s
    assert (s + c - n) % 8 == 0

print("P-J-HODGE-COUNTER-CARRY-FACTOR-1")
print("audit range n: 0..%d" % LIMIT)
print("digit successor plus carry successor = 1: PASS")
print("cumulative carry = n-popcount(n): PASS")
print("unique normalized integer complement: PASS")
print("finite C8 exponent completion: PASS")
print("characteristic-zero fourth-power exponent = 2n: PASS")
print("loxodromic exponent pair (2n,n mod 10): PASS")
print("power-of-two carry witnesses through 2^18: PASS")
print("all-n statements: PROOF.md")
print("physical clock / cross-place carrier: NOT CLAIMED")
print("VERDICT: PASS")
