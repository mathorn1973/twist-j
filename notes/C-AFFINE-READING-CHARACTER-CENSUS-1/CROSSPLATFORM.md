# C-AFFINE-READING-CHARACTER-CENSUS-1 second architecture leg

NON-CANONICAL. This record adds a second independent execution leg to the
candidate. It does **not** amend the frozen preregistration, the frozen
verifier, or `EXPECTED.txt`, all three of which are byte identical to the
values pinned before the first run.

## What is claimed here, and what is not

Claimed: the frozen verifier produces byte identical stdout on two
architectures, two operating systems and two Python minor versions, and the
independent break attempt does the same.

Not claimed: the POLICY section 4 public two architecture gate. That gate is
defined for a pinned public probe under `probes/`, with the GitHub x86_64 check
at pull request time and the aggregate `check` job. This candidate lives under
`notes/`, has no public issue claim and no probe pin, so it remains
**candidate-T at L1** and is not computation grade. The leg below strengthens
the candidate; it does not substitute for the gate.

## Legs

```text
leg A   platform      Ubuntu 24.04
        architecture  x86_64
        python        3.12.3
        elapsed       1473 ms, engineering readout

leg B   platform      Darwin 26.5.2
        architecture  arm64
        python        3.9.6
        elapsed       1 s, engineering readout
```

Both legs ran the identical command in the identical environment:

```text
LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
  python3 verify_C-AFFINE-READING-CHARACTER-CENSUS-1.py
```

## Transfer integrity, checked before execution

The verifier and the break script were transferred to the second platform and
their SHA-256 sums were verified **before** either was executed. No execution
was permitted on an unverified blob.

```text
verify_C-AFFINE-READING-CHARACTER-CENSUS-1.py
  829f91d1269f4802c2dfb0e0afba1b9bd78e0830bb665547719f5371bc2ff430   match
PREREG-C-AFFINE-READING-CHARACTER-CENSUS-1.md
  473f64da93c9b6c488ffe266bb33c1b9c54705c8debc85166757b80aa192ba40   match
BREAK-C-AFFINE-READING-CHARACTER-CENSUS-1.py
  066635b7a1463d333b66cc478f2b21e8c053cc5326dc05357cc6873715a335af   match
```

All nine files of the first commit were verified against `SHA256SUMS` on the
second platform, nine of nine OK, and the commit rebuilt there from those bytes
reproduced the identical git commit object
`82416b480f3355affde01a47704bceb636364752` with tree
`a2c03678fddeb5341565ae908e97854acda95d81`. Commit identity is therefore an
independent witness to the byte integrity of the whole directory.

## Results

```text
verifier      exit 0, stderr 0 bytes, stdout 1101 bytes
              stdout sha256 on both legs
              4a3813fa115f875d6f8da44c6d26c8a3c161cef9a273221b7f66539e6fab35f5
              decision line READING-CENSUS-CERTIFIED on both legs

break attempt exit 0, stderr 0 bytes
              stdout sha256 on both legs
              692847c9a2a4efa1ea7076abd7b7dc09ef34083d25b28488d0021d37e907efb1
```

Byte identity holds across the architecture change, the operating system change
and the Python minor version change. The Python 3.9 leg is the stricter of the
two: the verifier uses no syntax or standard library behaviour introduced after
3.9, so the exact result does not depend on interpreter version.

## Currency gate on the second platform

Performed independently against a fresh clone of public `main`, not against a
copy of the first platform's tree: `canon/SHA256SUMS` five of five OK, tag
`canon-v60` an ancestor of `main`, content commit
`18b21bdaf2c2236c9444b120900277ccfb63e050` an ancestor of `main`, and `main`
still at `f9b7438747e612eeebf63cb3ac95283fcb2a7085`, which is the basis this
candidate was frozen against. The basis had not moved, so no stop condition
fired.

## Effect on the recorded status

None. The decision, the gate outcomes and the recorded defect are unchanged.
The candidate remains candidate-T at L1 with the same fired self-check in
`RESULT-C-AFFINE-READING-CHARACTER-CENSUS-1.md`. What changes is only the
strength of the execution evidence behind it.
