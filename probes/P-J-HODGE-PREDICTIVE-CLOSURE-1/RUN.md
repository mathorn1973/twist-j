# P-J-HODGE-PREDICTIVE-CLOSURE-1 run

Pin commit: `8766a31ccbcb59db8b5161fcd186852c1e773fd9`
Preregistration SHA-256: `b47430d93a809bd181fb75ecf3bdca569096ba45feef80d2569a4ddbfea5e009`
Verifier SHA-256: `3938e0d23cf5003fb022263dd5c360ddf3fed3ad41d974ba4c37936adb803cbc`

Command, from repository root:

```text
LC_ALL=C LANG=C TZ=UTC PYTHONHASHSEED=0 PYTHONDONTWRITEBYTECODE=1 \
python3 probes/P-J-HODGE-PREDICTIVE-CLOSURE-1/verify.py
```

Local formal run:

```text
platform: Debian GNU/Linux 13
architecture: x86_64
python: 3.13.5
exit code: 0
stderr bytes: 0
stdout bytes: 258
stdout SHA-256: 8b02840a92462b82e41ebc2526e069587f4435f73a6f221b928422209776c596
```

The two pinned source files were publicly read back from the reserved GitHub
branch before execution and matched the recorded byte counts and SHA-256
values exactly. Network checkout is unavailable in the execution container;
the formal local tree was reconstructed from those exact read-back bytes and
run from its repository root. No source byte was changed after the pin.

The local run is one x86_64 lane only. It is not the required public
two-architecture gate. The unchanged verifier must replay against the one
EXPECTED.txt on the required GitHub x86_64 and aarch64 jobs.
