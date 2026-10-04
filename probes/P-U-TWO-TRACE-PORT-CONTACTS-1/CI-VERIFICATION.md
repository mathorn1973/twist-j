# Clean public architecture reproduction

NON-CANONICAL evidence receipt. The required workflow
[37166124857](https://github.com/mathorn1973/twist-j/actions/runs/37166124857)
completed successfully at result head
`bf1fe0bda4b5496c92501527d94de4b815035ead` in PR #1355.

| Job | ID | Conclusion |
| --- | --- | --- |
| architecture-aarch64 | [111329255807](https://github.com/mathorn1973/twist-j/actions/runs/37166124857/job/111329255807) | SUCCESS |
| architecture-x86_64 | [111329255979](https://github.com/mathorn1973/twist-j/actions/runs/37166124857/job/111329255979) | SUCCESS |
| aggregate check | [111329315861](https://github.com/mathorn1973/twist-j/actions/runs/37166124857/job/111329315861) | SUCCESS |

Both architecture logs contain the exact successful verifier line with
verifier SHA-256
`5e57a4d9e9c1129fd68c453baf9679d25104b45664742608ccc8ba94b1c9d5fe`
and stdout SHA-256
`cc8109a7b389fc77db7f25366d143b198aaf7d3d1b1ff5c781713e3b57ad82fc`.
They match the same committed 2636-byte EXPECTED.txt and original local
execution. The aarch64 line is timestamped 2026-10-04T00:49:51.8276697Z;
the x86_64 line is timestamped 2026-10-04T00:49:53.9683577Z. Repository
checks additionally require zero exit and empty stderr. The public workflow
uses clean Ubuntu runners and Python 3.12; publication is intentionally
skipped for this PR event.

The original public scientific pin remains
`5d122f0cab1fb20b368302cee4b4989d13ff16d2`. This receipt adds no code,
input, proof, carrier, timing, target or threshold change. Local standard
repository verifier replay also passed at the result commit before push.
The exact first-run evidence and all frozen sources remain unchanged.

This establishes the declared two-architecture computation gate. Independent
implementation and symbolic proof review are separately recorded and are
not implied by architecture count. The result remains candidate-T outside
Canon, within its explicit two-use added-interaction scope. This receipt
does not merge the PR or perform a Canon fold. A later documentation-only
head receives the ordinary required checks again; the live final-head jobs
remain the authority for that head.
