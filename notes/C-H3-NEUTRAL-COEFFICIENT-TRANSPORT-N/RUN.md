# Informal exact audit

NON-CANONICAL. Initial issue #2109 froze A-C before computation;
four subsequent issue comments froze D-G before their respective
comparisons. Later diagnostics were result-exposed as explicitly
recorded in PREREG.md. No earlier target or threshold was altered.

Public source commit 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed,
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
Source SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
The Apache-2.0 public source is imported unchanged and not copied
into this package. The alternate implementation uses its own
five-power cyclic arithmetic, fraction-free rank tests and native
local updates. Exact memoization in the height-8 primary tests
does not change pure local primitives.

First execution: Linux aarch64, Python 3.11.2. All scripts exited
zero, empty stderr. EXPECTED.txt combines the original A/B and C
outputs. The alternate A-C stdout matched it byte for byte.
CLOSED.txt is the complete eight-period replay on the literal
source. FOLLOW.txt combines D, E, F, G in that order. The alternate
follow_break.py (also reruns and verifies the alternate A-C)
matched FOLLOW.txt byte for byte. All executed sources archived
unchanged. This is result-exposed checking, not blind independent
review or the repository's formal two-architecture scientific gate.

Original component stdout SHA-256 values:
```text
5f06564c564a2c912f50f2d42248abcb551a10ccc5c237e17e5a3ba0268551aa  AB
2548ea45f1e46abd644bb336fc02d096a7151b5c82f08e07cb40eddbd70d7665  C
3915add4d08532556a2457dc3b28a27261f3c2a661ffdf2d972dc3289e1b6aa5  D
68d51a5ff44fb1acd8aaabfb1052b3afc2c0ab59d5f25c3122b47948e98b30ac  E
b28ddcd48e0c71cb8c1745a3a9f916ebd99d5c385d40b9a475280b59cb6582d4  F
13f353e4fe33fd08fdf229bc4e9b9261170561e2241bb31c7df417f033edfa9f  G
```

Executed source and retained transcript SHA-256 values:
```text
940e88da559a9d3ee7f50d5b27e7ddb669404e052a432b61b24067d4752e9424  verify.py
d4e942a19117241a8c795538d244f331e211a970e6c797d03215bf6da42889cd  search2d.py
2141203bf998d111d77d3de774cf0fb105f0d9ef4b7a86f1ec050360f3c57d44  break.py
26af8531010bd4575e17dd1e70060bd077baed761911190a48fe24363c91c786  closed_audit.py
138f55be5f09c1ca2406e4f465cde88a8a5887f6034a596e940c9237e1b5f48d  phase_diagnostic.py
5d24157d0877bb7193d8410db75e9d1d0d232327a805d1798c223b8faa30d92e  phase_record.py
cc7cbbe6cb6de7735b96cb4a299659d824604a2c15b6398794de15a8d6de5335  height8.py
5055ed929b3095c2ed8d30f09a4f7af741cb425b1c36c2c79b9a6180465fbf70  four_stroke.py
d6a1cab6bde5f30467d9fca268d19ee33acce321b5a741de6883f0769b899886  follow_break.py
582d3dbea2b85592f23af765869fca985806ff16a470b1a652571c7c115867e0  EXPECTED.txt
320f20fa60bc23bc3cc12d4c3dc08a54ab7e0bc27b37d899a413ec4cdf360dd7  CLOSED.txt
87f7994339bca2bfcfbc891c07952a36ea497ea81608b7b1a82aae4ca2a3a9d9  FOLLOW.txt
```

No scientific registry, Canon or formal gate change.

Second-architecture informal reproduction: Linux x86_64, Python 3.12.3.
Input commit d09a7961e2444216b8ad626fc8a9a169db8e2af5 and the immutable
public H3 source at the base were fetched as raw files. All thirteen
script, transcript and source SHA-256 values were checked before
execution. Primary A-C, literal closed-period replay, primary D-G,
and alternate A-C plus D-G all passed with empty stderr. The exact
output SHA-256 values are the same EXPECTED.txt, CLOSED.txt and
FOLLOW.txt values above. This is cross-architecture reproduction,
not blind independent review or the repository's formal public gate.
