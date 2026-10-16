# Serialized input and closed-campaign association

**NON-CANONICAL / read-only custody result; not a numerical restoration.**

Campaign source pin: `bca348445715c03f4cdc3af6079207024dd40332`.
First outcome: `6f378a1ba9b39fa1c29188b61a2e6507a92eb9d5`.
Audit source pin: `9a5c07e140d5781934e026414aa7f7b306b15952`.

The preserved closed offline campaign was read through its existing
connector. Original files remained unchanged. All five endpoint payloads,
the artifact inventory, final-custody receipt, serialized input and summary
were rehashed. Their hashes agree with the old inventory and audit receipts.
The actual `final-custody.json` records precisely the serialized input and
all 16 original source/binary pins declared in
[INPUT_BINDING.json](../../probes/P-DP5-ENDPOINT-RESTORATION-1/INPUT_BINDING.json).

`exact_input.txt` has 3918 bytes, SHA-256
`720f167680bbb51549165a10ba04ce9688de43cc67bb4087cd4ce5be20ebb471`.
Four earlier local comparison-campaign copies have exactly the same bytes.
An independently written decimal-token serializer applied to the immutable
campaign `input.json` reconstructed precisely these bytes. Its old module
was neither imported nor executed.

The source JSON SHA-256 is
`ca6b286c9e6d45795677b05e09fbe1b38043c8ff8369b57b652c83195a156d53`;
the pinned source-manifest SHA-256 is
`fa029eef8f387251a1a935f36605fdc84b24f311b3c32396881306b3a63015b1`.
The actual final-custody receipt has 1575 bytes, SHA-256
`ae81c8e940ae2beead4eca379c78b8d07380a573c4a04350e0316f366eed56a6`.
The inventory and summary hashes are frozen in the new preregistration.

This closes the formerly missing content/receipt association for the same
closed 500-microsecond campaign. It is custody evidence, not proof of the
original interval preparation or an attestation beyond the preserved
receipts. The separately accepted production validator rechecks these
bindings and all payload hashes before and after endpoint evaluation.
