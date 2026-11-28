# Exact run and custody record

NON-CANONICAL / NO AUTHORITY. L1. Claim #2139. These are candidate results
and informal exact reproductions, not a formal public-probe promotion.

## Authority and frozen basis

Public main:6f2e112aafc4f3aca4222bb4bf3dced1d79fe2ed.
Public Canon:v117. Content:d65e32c4b8e9a14496d3b7aba46fc384f51f81dc.
Annotated tag object:63ff3d2f7edc0c921a6c8ddd033badb59b632436,
targeting that main commit. The declared ancestry, five normative hashes,
Canon byte count and required checks were verified before new work.
The preceding candidate is #2138 at
524dd4622cf23d04ef78ecc2564f649ab2a832e2. Its unchanged full121 endpoint
is checked before every new verifier proceeds.

PREREG.md was committed, pushed and publicly read back at
0fabe9ffdb8b387614344aa484589e3898bdb784 before any new trajectory.
It has14967 bytes and SHA256
dafa06568fe1a38f21c806ebeea694e5e635b151667045c5e6761498c7879981.
The checker requested exact reference-cut conventions before execution.
CLARIFICATION.md at24d4fb366850b38e0cd09d69ece0a38f366d4c89 has SHA256
6193dfed88dc00ebb381c981228ffa5c541cf3c1bd62946405d53619f44a2064;
CLARIFICATION-2.md atf4e398b7e41700ae2b205c8a873b2222a8930d88 has SHA256
b04236f7070d0cb6df6566b9e2f45dc4b825542e757a4155305c7394e3a872f9.
Both were public and read back before execution. The original preregistration
bytes were preserved. No scientific output existed when either clarification
was chosen. The primary A source already implemented the second convention.

## Source freezes

All scientific sources were published together and read back before the
first execution at this immutable common source commit:

    5dc831942deba5a9e5f333632ddc7a13234286c1

| Source | First local source commit | Public integration commit |
|---|---|---|
|model.py|24d4fb366850b38e0cd09d69ece0a38f366d4c89|same|
|reader.py|f27365179796c7f12599158b7f29ce4270cd5cd4|same|
|continuation.py|a82d8dbd8a4f6910769544d4ee48d00353debe41|57b7bc261f341f88fffe5ace21abb506d5a7bf83|
|break.py|c54ae0bb8b46376697a298a96300a2447199fe3b|5dc831942deba5a9e5f333632ddc7a13234286c1|

Local helper commits and their public cherry-picked integration objects are
distinct where shown; only identical source bytes are asserted. No original
helper object is falsely described as the public source pin. Later commits
add outputs and reports; these source bytes remain unchanged.

| Source | Bytes | SHA256 |
|---|---:|---|
|model.py|9158|7b2f12553efe075e97a3814e68b6402690d1f66c389e1a6c45694aeccd91365d|
|continuation.py|14479|9720af2f1bad512cf91976d39cc740c485bb43102a8cc7a08a86acafe482b03e|
|reader.py|12550|8562af3e9ae4c48164add52389a9a19c22a5fa28929cda3e267ff18a673a8f34|
|break.py|29660|4fe75646960f64bc4c47a1964341bd03e6e9ecfa2a02cc9c4daf013ae4e1c457|

The canonical law read by model.py is
reproduce/h3-referenced-record/verify.py, SHA256
4553945d3bf32574ffd55de917859497e9644394f506aaf01ff9492adb8eeedd.
The alternate has its own cyclic-five ring arithmetic, transport, B update,
inverse, initial constructor and account checks. It does not import any
new primary source. Its author read the frozen preregistration, clarifications
and earlier sources, but no new primary code or output before completing
the alternate run. This is blind authorship within the same session, not
independent external review.

## Commands

From a clean checkout containing the pinned source, run each command with
PYTHONDONTWRITEBYTECODE=1 and PYTHONHASHSEED=0. Capture stdout and stderr
separately outside the checkout. The run used no third-party Python package.

```sh
python3 -B -u notes/C-H3-MATERIAL-READ-CONTROL-N/continuation.py
python3 -B -u notes/C-H3-MATERIAL-READ-CONTROL-N/reader.py
python3 -B -u notes/C-H3-MATERIAL-READ-CONTROL-N/break.py
```

Compare each stdout byte-for-byte with its corresponding committed file.
The alternate and primary formats differ; they are not expected to be
byte-identical to each other.

| Command | Committed stdout | Bytes | SHA256 |
|---|---|---:|---|
|continuation.py|CONTINUATION.txt|7112|c8181e084ca3102e8feb403ab57c2f35148b5d92ce77f2b61b626cb442ba476e|
|reader.py|EXPECTED.txt|12166|2e0ad994444c2c526429b2080ff9600daffef26b46e5ba635dc0e6a68ec941e2|
|break.py|BREAK.txt|21491|8426a5773a8afe9c6a1129eab2697a11e78a1b70478e159f7af0c3378cd34a92|

## Completed architecture results

| Platform | Architecture | Python | continuation.py | reader.py | break.py |
|---|---|---|---|---|---|
|Linux|x86_64|3.12.14|exit0,stderr0,exact bytes|exit0,stderr0,exact bytes|exit0,stderr0,exact bytes|
|Linux|aarch64|3.12.3|exit0,stderr0,exact bytes|exit0,stderr0,exact bytes|exit0,stderr0,exact bytes|

The aarch64 checkout was clean and detached at the exact common source pin.
All four source hashes were verified before execution; the checkout was
still clean afterward. The local helper runs used their unchanged frozen
source commits, byte-identical to that public pin. No runtime or fixture
failure occurred in any of these six scientific runs.

The primary A program checks1780 predecessor native steps,9030 A1 steps
and18060 A2 steps. The primary B program checks1780 predecessor steps and
2475 loaded/successor steps on all25 actual and50 control arms, total4255.
The alternate checks29860 steps using proved equal-field representatives
while retaining every compound reserve state. Every native step checks
accounts at both cuts and its exact inverse. Diagnostic boundaries retain
all displaced stocks and have their swap inverses checked. Fixed isolated
reserve accounts extend each native field account to its compound account.

Primary and alternate A1/A2 full evolving-field endpoint digests agree
exactly. The B primary prints aggregate digests over all25/50 cases, while
the alternate prints its10/20 distinct evolving fields, so those differently
ordered/domain digests are not equality tests. Their selected label, probe,
complete accounts, first-read classes, side contacts, failure times and
split/collision witnesses agree. Each program's full stdout independently
matches its own second-architecture run byte-for-byte.

Repository policy checks are separate from these scientific runs. This
notes package is not registered as a public probe or reproduction, so a
green repository workflow is not claimed to have rerun these three notes
verifiers. All source/output custody and candidate status remain explicit.
