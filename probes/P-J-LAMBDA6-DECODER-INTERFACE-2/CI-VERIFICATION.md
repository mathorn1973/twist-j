# Two-architecture verification receipt

The required computation gate passed on result head
`5002f58a6ffe9b373a6545d638cd7d41e950aded` in
[workflow run 37162114372](https://github.com/mathorn1973/twist-j/actions/runs/37162114372).

- [aarch64 job 111317521531](https://github.com/mathorn1973/twist-j/actions/runs/37162114372/job/111317521531): success.
- [x86_64 job 111317521420](https://github.com/mathorn1973/twist-j/actions/runs/37162114372/job/111317521420): success.
- [aggregate check 111317700261](https://github.com/mathorn1973/twist-j/actions/runs/37162114372/job/111317700261): success.

Actual logs identify the respective native architectures and the same
VERIFY PASS pair:

```text
verifier SHA-256 9e3b4af0fcfb680500fc04f7343ffe8f7f82bb24e893258523d2b2d6bd5f7625
stdout SHA-256   1104009a53640c1fc226418db83d1c4c254ee7e12d69e649599e04ae06f273df
```

The checker requires exit zero, empty stderr and exact EXPECTED.txt byte
identity. The wrapper runs both the primary and pre-exposure independently
frozen verifier on each architecture. Policy, tool tests, Canon, ledger,
gate-contract and changed-reproduction checks also passed. Publication is
skipped on PR events; no release or Canon promotion is implied.

This later receipt changes no frozen program, contract, manifest or expected
stdout. The PR's newest workflow controls any subsequent documentation-only
head. The original lower-depth census is not part of this new execution gate
and retains its own original provenance.
