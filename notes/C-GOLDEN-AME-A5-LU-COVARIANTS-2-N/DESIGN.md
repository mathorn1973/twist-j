# Pre-pin design audit

Status: **NON-CANONICAL, tensor-independent**

No golden tensor, its support, or any target covariant was loaded or computed
while designing this continuation.  The preregistration package contains
only:

- exhaustive colored-graph enumeration and exact double-edge rewrites;
- a generic-array contraction engine with no source parser;
- subset dynamic programming for the frozen contraction path; and
- generic random-array orientation, sparse-direct, and star-involution tests.

The graph classifier enumerates all `24^3=13,824` normalized triples and all
2,345 residual `S3` orbits.  Exactly four orbit representatives are
double-edge-free.  Their list SHA-256 is
`df5a7d9f6d3454119cc7eaf066a42e1382232c442f3ab69e6906319bde0f6134`.
All four are fixed by the graph-star involution up to the permitted dummy-copy
relabeling.

Run the design-only package with:

```bash
python3 classify_n4_graphs.py --output GRAPH_CLASSIFICATION.json \
  > CLASSIFY.txt
cmp EXPECTED_CLASSIFY.txt CLASSIFY.txt
gzip -n -9 -c GRAPH_CLASSIFICATION.json > GRAPH_CLASSIFICATION.replay.json.gz
cmp GRAPH_CLASSIFICATION.json.gz GRAPH_CLASSIFICATION.replay.json.gz
python3 optimize_paths.py GRAPH_CLASSIFICATION.json > PATHS.txt
cmp EXPECTED_PATHS.txt PATHS.txt
python3 test_n4_locator_engine.py > ENGINE_TEST.txt
cmp EXPECTED_ENGINE_TEST.txt ENGINE_TEST.txt
```

The compressed classification decompresses to SHA-256
`b26689374364d36211c04bc63718c4ef84b98de1c708f6ca22bdd2fa01896a7c`.
Formal computation on the pinned golden tensor is authorized only by the
public preregistration commit recorded after this file.

