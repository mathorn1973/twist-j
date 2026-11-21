# Supplied source bundle manifest and custody

**NON-CANONICAL source archive, not public authority.** The author supplied `C-HODGE-UNIT-N_bundle.zip` as reference data. The ZIP itself is not checked into the public repository; the named text files and their submitted hashes are retained below for audit comparison. The bundled `PREREG.md` was authored after the result, and the `verify.py` is a result-exposed, previously modified one-architecture witness.

```
ZIP SHA256: ad0432218d1524a8f93ed32f75cf64c83c61f31ac33b6d0b46a1e7e5c7cd49a6
ZIP bytes: 8282
```

Seven contained text entries, no parent traversal or absolute paths:

```
1961  PREREG.md    5ed2696ad3608d17f71f185e0822f3003d31c9d258238dcb9ec23f6ee5c43949
6424  verify.py    28545c7e550d243468ab9d29668b5f17a18f3846632f984caec31828191da3d7
 705  EXPECTED.txt 1925cfa4ffa3eec2cc02aa2cdf7a593cd5836b5ba38faa919b8395ec90324291
2389  RESULT.md    c2ce85c64161b617d103bbff0e6b6f87438ad469914fc0d5962a04cb99d8435f
1842  PROMO.md     994e72cebf92e301618740acc19ef69feff85040b633e1f04d546c26871d256c
 642  RUN.md       0617e26922696425629457bed46a60ac111a67c5dae47daaba471cd9c330f6d0
 455  SHA256SUMS   f3d502abbaa93466398d02d14c9192c321f0f819b35c4e553a25f0ccb118d0d7
```

Six of the seven source files are covered by the original `SHA256SUMS`; all six digests matched the actual ZIP entry bytes. This note also pins the source `SHA256SUMS` digest separately to avoid a self-reference. No software was executed from inside the archive. The reviewer-reported additional nine-check `claude/` files were not available for byte verification or copying; their claims are therefore treated as source commentary only.

Public source authority at review time:

```
Public Canon: v104 ACTIVE, tag canon-v104
CONTENT_COMMIT: 4a50e527d20018839f006ed312454b710e6486b4
CANON_SHA256: c8d0cfadb44cf882af9f8ac303ba558b232663451d634d99467ce6d2c4a6814d
CANON_BYTES: 1262204
STATUS.md blob: 75227ff5535f7c7ae33c5fd265f1a79641e6015d
canon/REGISTRY.tsv blob: d30c4ea89899585e0b7f4755ff55bf2ab5119d68
canon/FRONTIER.md blob: acc208da19cf123cd50f538ee1f967530daadbc4
```

The active `canon-v104` annotated tag resolves to commit `e6240e2689bb22aab5f02bad90b75d3692bb96d9`; its release exists and both required architecture jobs and the aggregate check succeeded. This is the public authority context for the note, not a certification of the new unregistered mathematical candidate.
