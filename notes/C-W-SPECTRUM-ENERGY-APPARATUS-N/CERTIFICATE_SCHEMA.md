# Canonical exact certificate

Each verifier accepts one positional output pathname, writes UTF-8 JSON
using json.dumps(data,sort_keys=True,separators=(',',':'))+'\n', and prints
a short success summary. Every rational uses the reduced Fraction string
format (integers have no /1). No implementation-specific check counts,
timestamps, hashes, or platform data belong in this common certificate.

The exact top-level object has these keys:

```
schema: "w-spectrum-exact-v1"
coin_unitary: true
coin_determinant: "1"
free_symbol_unitary: true
compact_rest_eigenvector: true
s_coin_expectation: "-3/5"
characteristic: array of [lambda_exponent,z_exponent,w_exponent,real,imag]
gap:
  cos_b: "3/5"
  sin_b: "4/5"
  cos_delta: "7/25"
  sqrt5_threshold: "53/25"
  squared_margin: "316/625"
  strictly_positive: true
beta_lower:
  rational_part: "3/80"
  sqrt5_part: "3/80"
```

The characteristic list contains ONLY nonzero coefficients of the
ACTUALLY COMPUTED characteristic polynomial and is sorted lexicographically
by the three integer exponents, in ascending order. `real` and `imag`
are rational strings. Lists keep this order. Boolean fields can be true
only after the corresponding complete exact identity was checked.
