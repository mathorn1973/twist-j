# Supplied integral relative contact

Author: A. M. Thorn <thorn@twistj.com>.
SPDX-License-Identifier: Apache-2.0.

This directory preserves the exact finite audit accompanying the analytical
contact proof now stated in the Canon as RELATIVE-CONTACT-INTEGRAL-LAW.
The theorem rests on that written proof and its independent acceptance.
This audit is supplementary; finite coverage does not establish its universal
scope. It is not a new formal public probe or a retrospective preregistration.

## Source custody

The verifier and expected stdout are byte-identical copies of
`notes/C-J-INTEGRAL-RELATIVE-CONTACT-N/verify.py` and `EXPECTED.txt` at
source head `d9d93f68c5cd15b7ab9cea4ba1ef3996352613d0` (PR #1833).
The prospective scientific input pin was
`898160aab70bc8908174df56ddca7afec39fa42f`.

| File | Bytes | SHA-256 |
| --- | ---: | --- |
| verify.py | 8702 | `0089529bd6f4a9488cbc74197a55912453fc48a1967859bce87c3986cea4951e` |
| EXPECTED.txt | 776 | `89e49565965d9d417cebefd6eb7b36bea864788e8356bbad8901043f1ad66890` |

The [original proof](https://github.com/mathorn1973/twist-j/blob/d9d93f68c5cd15b7ab9cea4ba1ef3996352613d0/notes/C-J-INTEGRAL-RELATIVE-CONTACT-N/PROOF.md)
is the PROOF.md mentioned in the unchanged verifier's docstring.
The [current Canon](../../canon/CANON.md) supplies the retained public statement;
[STATUS.md](../../STATUS.md) determines its authority.
The verifier's historical final output remains unchanged, including its
statement that an audit alone does not establish independent or canonical
acceptance. That wording is preserved evidence, not the current status ledger.

## Reproduction

From the repository root, after the complete release candidate is publicly
pinned and read back:

```text
python3 reproduce/relative-contact/verify.py
```

Run without `-O`. Require exit code zero, empty stderr and stdout
byte-identical to `EXPECTED.txt`. The verifier uses only exact integers and
Python's standard library. It imports no repository module, reads no file,
writes no file, makes no network request and has no working-directory
dependency. This directory is selected by the ordinary reproduction checks;
architecture execution results are established by the actual candidate jobs.

The frozen audit has nine groups: trace and minimum-shell regression;
the declared monomial family; exact parity admission and composition;
complete two-slot coefficient-box checks; recurring fixed-source response;
the specified finite-modulus witnesses; two-edge composition and order;
occupied continuations; and retained negative controls. Its broader inherited
regressions do not promote additional source claims into this release.

The accepted contact statement concerns a supplied Cartesian carrier,
relative phase, identity refusal rule and arithmetic trace account. It is
not a derivation of native U, a physical energy identification, an unknown-input
apparatus, a permanent record or a clean resource-renewal mechanism.
