# Two-architecture verification receipt

The required computation gate passed on result head
`d9bca109be0a8becc3513c742bc4ad564b0df236` in
[workflow run 37162017185](https://github.com/mathorn1973/twist-j/actions/runs/37162017185).

- [aarch64 job 111317237487](https://github.com/mathorn1973/twist-j/actions/runs/37162017185/job/111317237487): success.
- [x86_64 job 111317237605](https://github.com/mathorn1973/twist-j/actions/runs/37162017185/job/111317237605): success.
- [aggregate check 111317331406](https://github.com/mathorn1973/twist-j/actions/runs/37162017185/job/111317331406): success.

The actual job logs report their respective native architectures and the same
VERIFY PASS pair:

```text
verifier SHA-256 58a9ce2a846572842927f2fb18307a30bd7fe216b16233af3c35f53e319191c4
stdout SHA-256   613ac47b49187ee1e7b89f7587ca393d8b82c71815d7d55a20605fbf7756925e
```

The checker enforces exit zero, empty stderr and exact EXPECTED.txt byte
identity. Both frozen programs run inside that wrapper on each architecture.
The architecture jobs also passed policy, tool tests, Canon, ledger,
gate-contract and changed-reproduction checks. Publication is deliberately
skipped on PR events; no release or Canon promotion is implied.

This receipt is appended after the result run. It changes no frozen program,
contract, manifest, expected stdout or scientific evidence. The PR's newest
workflow remains the authority for any subsequent documentation-only head.
