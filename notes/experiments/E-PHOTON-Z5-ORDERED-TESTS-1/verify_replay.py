"""Exercise receipt admission and rejection on a constructed two-state ledger."""
import hashlib
import io
import json
from unittest.mock import patch

import analyze_ordered as analysis
import replay_ordered_volume as replay

L, endpoint = 16, 1024
sampler = "a" * 64
records = []
for i in replay.CHAIN_IDS:
    name = replay.chain_settings(L, i)[0]
    for index in range(2):
        cycle = endpoint + index + 1
        records.append({
            "L": L, "chain": name, "sample": index, "macrocycle": cycle,
            "state_sha256": hashlib.sha256(name.encode() + bytes([index])).hexdigest(),
            "state_bytes": replay.state_size(L, name, index, cycle),
        })
raw = b"".join(json.dumps(row).encode() + b"\n" for row in records)
filehash = hashlib.sha256(raw).hexdigest()


class BytesInput:
    def __init__(self, data):
        self.data = data

    def open(self, mode):
        assert mode == "rb"
        return io.BytesIO(self.data)


class ReceiptInput:
    def __init__(self, digest):
        self.digest = digest

    def read_text(self, *, encoding):
        return json.dumps({
            "L": L, "endpoint": endpoint, "status": "PASS", "verified_states": 8,
            "measurement_sha256": self.digest, "sampler_sha256": sampler,
        })


with patch.object(replay, "SAMPLES", 2), patch.object(analysis, "SAMPLES", 2):
    digest, ledger = replay.read_ledger(BytesInput(raw), L, endpoint)
    assert digest == filehash and len(ledger) == 8
    flags = {str(L): {"endpoint": endpoint, "sampler_sha256": sampler}}
    analysis.verify_replay_receipts(flags, [BytesInput(raw)], [ReceiptInput(filehash)])
    assert flags[str(L)]["replay_pass"]
    try:
        analysis.verify_replay_receipts(flags, [BytesInput(raw)], [ReceiptInput("0"*64)])
    except ValueError:
        pass
    else:
        raise AssertionError("Divergent replay receipt accepted")
    corrupted = raw.replace(records[0]["state_sha256"].encode(), b"invalid", 1)
    try:
        replay.read_ledger(BytesInput(corrupted), L, endpoint)
    except ValueError:
        pass
    else:
        raise AssertionError("Invalid ledger hash was accepted")
print("REPLAY LEDGER AND ANALYSIS CUSTODY FIXTURES PASS")
