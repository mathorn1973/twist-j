# Informal exact audit

NON-CANONICAL. Issue #2135 froze A/B; comments 7239307527,
7239316925, 7239333177, 7239345628 separately froze D,F,G,H
before their respective computations. No earlier failed threshold
altered. Public v117 base 6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.
Native H3 reproduce/h3-referenced-record/verify.py, Git blob
fd215e24fefbbebf83cf3985d8ebcedd590aa709, SHA-256
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
Apache-2.0 public source imported unchanged and not copied.

Initial execution: Linux aarch64, Python3.11.2. All six
scripts exited zero with empty stderr. Alternate separately
recomputes principal A/B/D/F/G/H results including all
enumerations and selected native trajectories, using a distinct
five-cycle multiplication and explicit equality sets for H.
It has compact stdout; F phase/counterfactual and some mask
diagnostic prints are not independently duplicated. Result-exposed,
not blind independent review. No formal public runner invoked.

Exact archived bytes:
```text
08852c48a2c0ed434a689b6f278b29320d9a57e47009c11d88d1da7d5ce4a324  verify.py
faa1c602db6a8b92b09b6bcc9f3b551c7ddbf10c4dab0d378d89b70506c375cf  gate.py
bb30ae1cc2c6aacfe8959dec39e6b16b282faa3598828e3e051c94f2e923b4fd  reference_gate.py
2c2d16ec93148be20001de3a46439877f0fd63c2b1cac06b51bd0bed670e0fb4  target_gate.py
488b84ba5725cc1a598ea832a03a92df97a3dd5e26a323ad2399a1490e0f0969  coupled_gate.py
046efe34baaeaaffa53ce05b661540aedcb56b68596290724ad3e7bb93552f5e  break.py
25e6a72fe49309659dbd2407dea19e7991cb48df8ce5d200049881bbc2a9ffb5  EXPECTED.txt
3dfb4fbf4bd13e547822657cdfb58cc65f315d17af409933198f7bf5b7a180b1  D.txt
4f3cf3c7f4e6c95e2028c7fa72c9403e49604dc99b2b6af301501f3ed3e92b82  F.txt
68a126178904fbc8a84409b92fa2593dd316501397e53f118f600e2bb543fd73  G.txt
23977eb4d9c5d41fbeee944bc8dd1a8435890de144ba6e7af50bf54e85328fa8  H.txt
09458af97d01078b72d6778004948740471fdfc2dff020b414ddf514d5e8b4fd  BREAK.txt
```

No registry/Canon change; no authority or formal gate claimed.

Second-architecture informal reproduction: Linux x86_64, Python 3.12.3.
Input commit 06f86cf4db3b5e657629f76677cc3e6e41d5ca0e and immutable
public H3 source at the base were fetched as raw files. All thirteen
source and transcript SHA-256 values were checked before execution.
All five primary scripts and the alternate exited zero with empty
stderr. Each of the six complete stdout transcripts agrees byte
for byte with its own archived transcript across the two architectures.
Result-exposed reproduction, not blind independent review or the
formal public scientific gate. Trailing whitespace only was normalized
in the copied issue preregistrations; no scientific criterion changed.
