# Informal exact audit

NON-CANONICAL. Issue #2125 froze A-C before computation;
comment 7223209475 froze the result-exposed D/E diagnostics
before further computation. Original A/C failure retained.
No earlier failed threshold altered.

Public H3 source at 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed:
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
Apache-2.0 public source imported unchanged and not copied.

predecessor.py and alternate_predecessor.py are exact copies
of the files of the same names at
4608516e88d6ef73bc476c8068b57c94e50e7983,
notes/C-H3-COMMUNICATION-BALANCE-N/. Those files were pinned
in turn from the #2122 package at
289b63b47566cafb37ccb873a7076052f0c88454.
Apache-2.0 repository license applies. The two files are
reused engine inputs, not new independent evidence.
Both are checked by SHA-256 before import.

Initial execution: Linux aarch64, Python 3.11.2. Primary A/C,
primary D/E and alternate A and DE exited zero with empty
stderr. The two complete primary stdout transcripts match
the corresponding alternate outputs byte for byte.
The separately implemented alternate engine is reused with
a new result-exposed audit, not a blind reviewer. It checks
the actual ten-state continuation and multiplicities for all
25 loaded pairs at each of the three starts, all guards,
D's local read classifications and the entire E screen.
The E shortcut uses the proved C-only prehistory; no
continuation beyond the failed relative6 screen is claimed.
No formal repository scientific runner invoked.

Exact archived bytes:
```text
ad4920e5d0322e33013f77e3bedd290733df4a054e2284060b72a94164f12e95  predecessor.py
48262b6e7bb600c069952412015385721c894210eec50da11314df792c2ac27e  alternate_predecessor.py
51708ca0a41af7c4881cb240975e118d9e5586c2dc5d90b1cd509ed1b2a87eae  verify.py
9565718325dccb9771716368a2034e109d4d38f43869bffda824812aab2c4618  diagnostic.py
d347884271750a07be18c1b1d6b7aeb47f20153cf2bd9885f268b40925e24663  break.py
4ce671e546256f129105af721d6f0563dc8f53c1fcdffaf7ce6553d239bdd961  EXPECTED.txt
93fe17355fade6af24142de2cf233827d97682f8ef1aea45a3af81421501a76b  D_E.txt
```

No registry/Canon change. No formal scientific gate or authority claimed.
