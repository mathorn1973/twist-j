#!/usr/bin/env python3
"""Independent logic breaker for field-subset minimality."""
# Exhaust the Boolean condition itself: 5 fields, R mandatory, M or B mandatory.
fields=("S","M","B","R","N")
allowed=[]
for mask in range(32):
    s={fields[i] for i in range(5) if mask>>i&1}
    if "R" in s and ({"M","B"}&s): allowed.append(s)
assert len(allowed)==12
mins=[s for s in allowed if not any(t<s for t in allowed)]
assert {frozenset(s) for s in mins}=={frozenset(("M","R")),frozenset(("B","R"))}
print("BOOLEAN_CLASS_COUNT 12 PASS")
print("MINIMAL_SETS {M,R} {B,R} PASS")
print("BREAKER requires exact arithmetic witnesses from verify.py; no logical alternative survives")
