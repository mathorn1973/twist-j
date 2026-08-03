"""Standalone exact verification of a kappa falsifier witness JSON.

Checks, all in exact integer arithmetic:
  1. j is ternary, closed, nonzero, with connected support;
     an explicit Eulerian traversal certifies one closed edge-simple
     worldline through every support edge;
  2. n is ternary;
  3. partial n = 5 j coefficientwise on every edge of Z^4;
  4. L = |supp j|, F = |supp n|, and 2^F <= 7^L as exact integers.

A passing witness refutes every universal coefficient kappa with
F_occ >= kappa L and 2^(4 kappa) > 2401 on the predefinition's
candidate surface (owner disposition R0A-R5B).
"""
import sys
import json
from kappa_lib import (chain_d, edge_d, is_ternary,
                       check_connected_edge_simple)


def main(path):
    with open(path) as fh:
        data = json.load(fh)
    j = {(tuple(v), d): c for v, d, c in data["j"]}
    n = {(tuple(v), a, b): c for v, a, b, c in data["n"]}
    assert j, "empty current"
    assert is_ternary(j), "j not ternary"
    assert edge_d(j) == {}, "j not closed"
    L, walk = check_connected_edge_simple(j)
    assert is_ternary(n), "n not ternary"
    dn = chain_d(n)
    assert dn == {e: 5 * c for e, c in j.items()}, "dn != 5j"
    F = len(n)
    lhs, rhs = 2 ** F, 7 ** L
    assert lhs <= rhs, "2^F > 7^L"
    print("KAPPA-WITNESS PASS")
    print("L = %d   F = %d   F/L = %.6f < log2(7) = 2.807355" %
          (L, F, F / L))
    print("2^F <= 7^L verified as exact integers "
          "(%d-digit vs %d-digit)" % (len(str(lhs)), len(str(rhs))))
    print("closed edge-simple worldline: Eulerian walk of %d steps "
          "over connected support" % len(walk))
    print("candidate consequence (NON-CANONICAL, no probe run): this "
          "pair is a candidate refutation of every universal kappa "
          "with 2^(4 kappa) > 2401 on the R0A-R5B candidate surface; "
          "the registered outcome vocabulary (CANDIDATE-REFUTED) is "
          "reachable only through the formal probe protocol")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
