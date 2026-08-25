# C-J-SINGER-MAHLER-LIFT-1-N

Noncanonical exact incubation bundle for the preregistered Singer/Mahler lift
attack at public pin `49ce4081e021171bc4c8c79a3fc7ffe4a496ea1a`.

Start with:

1. `RESULT.md` for the decision and interpretation;
2. `THEOREM.md` for the global proof;
3. `FINITE_CERTIFICATE.md` and `verify.py` for the frozen-window certificate;
4. `BREAKER_AUDIT.md` and `breaker.py` for the blind independent check;
5. `PROMO-C-J-SINGER-MAHLER-LIFT-1-N.md` for the unexecuted promotion plan.

Exact quick checks:

```text
python3 verify.py
python3 crosscheck_schur.py
```

The blind breaker is also exact but deliberately verbose:

```text
python3 breaker.py
```

All decision paths use integer or rational arithmetic.  Any NumPy output in
the breaker is explicitly `RECON_ONLY` and follows, rather than supports, an
exact negative certificate.

This directory has no authority and changes no Canon, registry, evidence,
dependency, frontier, or status row.
