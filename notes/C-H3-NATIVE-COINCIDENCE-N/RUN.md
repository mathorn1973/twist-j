# Informal exact audit

NON-CANONICAL. Issue #2113 froze A-C before computation;
comment 7220227085 froze D before its new calculation.
No earlier failed target or scientific threshold changed.

Public H3 source at 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed:
reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709.
Source SHA-256:
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
The public Apache-2.0 source is imported unchanged and not copied
into this package. The alternate implementation uses its own
five-power cyclic arithmetic and independent local updates.
Exact memoization of pure native primitives does not change them.

Initial execution: Linux aarch64, Python 3.11.2. Primary A-C,
primary D (also rechecks the primary A-C transcript) and both
alternate stages exited zero with empty stderr. The exact
full A-C and D transcripts matched their respective alternate
outputs byte for byte. All executed sources archived unchanged.
The second algorithm was written after the primary results
and is result-exposed, not blind independent review.

Exact executed source and retained transcript SHA-256 values:

```text
307fc5dfca088e1ba21c86440a64528be3438cefc5c71ced3b258bfeb90b404c  verify.py
1a037f0289fd764102a3bdf214731917e450867ccf97d6b9f9574b4867717dce  binary_strip.py
6b54feb59a7427f2b8ec03b19c0a8fba8f4b18208d0a6007df10103f7ff9c347  break.py
c39f5be3bedf05891240d6608fc23176d6b335618a543e78207a8c5e45bbf6c2  EXPECTED.txt
a61ddff6991732077c5caa8a59491e07026158016d3ac15ff816f5dec6c6ce64  D.txt
```

The negative recurrence tests, fixed single-port scans,
control aliases and finite hold boundary are preserved.
No formal scientific gate, public registry or Canon change.
