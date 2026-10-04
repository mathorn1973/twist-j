# Disposition of the first public decoder pin

Status: ABANDONED

Pin `561679f65aa4b0a534cd94129fe243ac8fc9936b` was publicly pushed before
execution. An administrative Git-blob readback then found that repository
text normalization converted REVIEW-FREEZE.json from 1581 CRLF bytes to
1546 LF bytes. INPUTS.sha256 retained the original byte hash:

- original: `c662fad63b3073095e2bd757b27a3a156b4b2cbfcfe70d3cc9447d7acc9fb9e6`
- committed: `5ba9763ff7ac5f402e194c8ae14974f71f9c39a2ceedebefe97cb794fd01da98`

The public bundle therefore failed byte custody. No scientific verifier was
started, and no scientific conclusion, EXPECTED.txt or RUN.md exists for this
pin. This is a coordinator packaging error, not a decoder counterexample.
The original preregistration, accepted programs and manifest remain unchanged.

The identifier is consumed and must not be reused.

Successor `P-J-LAMBDA6-DECODER-INTERFACE-2` will preserve the reviewed source
and mathematical scope, disclose this predecessor before its own pin, and
bind explicit Git attributes for the original freeze-record bytes. Its
manifest will be compared against staged Git blobs before publication and
against committed blobs before execution. The original ramified-depth archive
publication in the preceding commit is unaffected.
