# WINDOWED KREIN CHECK

```text
STATUS: NON-FORMAL exact audit notes
ISSUE:  #355
```

The all-variable proofs are in `WINDOWED-KREIN-GRAM.md`. The following algebraic identities were independently checked symbolically before this note was written:

```text
pole:
  cosh(a)+cosh(b)-cosh(a-b)-1
    = sinh(a)sinh(b) - (cosh(a)-1)(cosh(b)-1)

prime half angle:
  -cos(theta) = sin(theta/2)^2 - cos(theta/2)^2

gamma OU feature:
  eta_c(t)(r)=sqrt(2c) exp[-c(t-r)] 1_(r<=t)
  <eta_c(t),eta_c(u)> = exp[-c|t-u|]

Brownian feature:
  <beta_t,beta_u> = (|t|+|u|-|t-u|)/2
```

The prime sum must be windowed **before** splitting into positive and negative half-angle Hilbert sectors. No global infinity-minus-infinity direct sum is claimed.

The exact source-side factorization is theorem algebra; these notes are only an audit reminder and do not constitute public evidence.
