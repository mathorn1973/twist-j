"""Slab slice-optimum scan: does the exact min-cost flow optimum track
F_slice = 5n^2 + 8n, i.e. c2(n) = (F_slice - n^2)/2 = 2n^2 + 4n?

Threshold comparison per slice: ratio (5n^2+8n)/(2n^2) = 5/2 + 4/n
against log2(7) = 2.8073549...; exact integer form: the slice
increment (dL, dF) = (2n^2, 5n^2+8n) is on the falsifier side iff
2^dF < 7^dL.
"""
from checker_witness import build_current  # noqa: F401  (import path)
from build_witness import flow2d

print("n    c2(flow)  c2(formula)  F_slice  dL    2^dF<7^dL")
for n in (8, 10, 12, 14, 16):
    u, w, cost = flow2d(n, pad=4)
    formula = 2 * n * n + 4 * n
    fs = n * n + 2 * cost
    dl = 2 * n * n
    under = 2 ** fs < 7 ** dl
    print("%-4d %-9d %-12d %-8d %-5d %s"
          % (n, cost, formula, fs, dl, under))
