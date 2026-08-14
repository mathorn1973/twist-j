# Pre-lock construction record

Status: **NON-CANONICAL structural preregistration record**
Public lock: [issue #369](https://github.com/mathorn1973/twist-j/issues/369)

No target ideal operation was run in this record.  It contains only the
permitted source, construction, serialization, and artificial-method checks.

## Authority

```text
Public Canon v46 activation  6545c1d0de61ff4696eb3de1a258139e8891f436
Canon SHA-256                6c57e714c441bd679b9f6c673352cfae44ac993433d7c4624cd9c3c93df291ff
AME46_ORIGINAL.m SHA-256     55fbc0ba2747b4e5adc5a5abd15ac7241a461ff8182268ebdae464d8a29cc9ae
block944.m SHA-256           af0aac863f54beb2c8396368fd87102e75192a38ec77efee0605210123540649
```

The upstream files were recovered from commit
`1fa4a4d4d2b9a3c6d3b6c8d802116415fb679fe8` and were not vendored.

## Commands

```sh
PYTHONDONTWRITEBYTECODE=1 python3 prelock_audit.py \
  /path/to/AME46_ORIGINAL.m --block944 /path/to/block944.m

PYTHONDONTWRITEBYTECODE=1 python3 cas_selftest.py

PYTHONDONTWRITEBYTECODE=1 python3 verify_prereg.py \
  --original /path/to/AME46_ORIGINAL.m \
  --block944 /path/to/block944.m
```

Each command was run twice.  Both pairs were byte-identical to their single
committed expected transcript.

## Environment

```text
OS            Ubuntu 24.04.3 LTS
architecture  x86_64
Python        CPython 3.12.13
```

## Frozen outputs

```text
PRELOCK_EXPECTED.txt       db6b65ae3243096f663778ced57ee9f5682fffc01b27ff74d7d150d197eb9c79
CAS_SELFTEST_EXPECTED.txt  500ccdbdd9a64ef8a3fc62c280f621ef519960f7c491e9bf454c8cfb44b7aa48
PREREG_VERIFY_EXPECTED.txt f1b67c2fddb704d2ddf6ca0b2c38adf3526f6719f278416dc99fc2af359f1376
verify_prereg.py           31623cce049004c83a83eb92d82051f4512fd1be408b779fee1726830be3a4a5
raw equation serialization 09aac23466680ba762e363ad75845aa1535f4e8e32cee75ad41119f43cb16762
```

The construction transcript explicitly records:

```text
GROEBNER=NOT_RUN
RADICAL=NOT_RUN
ELIMINATION=NOT_RUN
SATURATION=NOT_RUN
TARGET_RELATION_TESTS=NOT_RUN
```

The artificial CAS self-test uses no golden tensor equation or source value.
It checks only generic algebraic identities needed by the post-lock method.
