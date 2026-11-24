"""Exercise receipt admission and rejection on a constructed two-state ledger."""
import hashlib
import io
import json
from pathlib import Path
from threading import Barrier
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

    observed = []
    parallel_barrier = Barrier(len(replay.CHAIN_IDS), timeout=5)

    def fake_chain(sampler_path, directory, deadline, side, i, thermal, samples,
                   previous_prefix, accepted_state, *, cohort):
        name = replay.chain_settings(side, i)[0]
        assert side == L and thermal == endpoint and samples == 2
        assert directory.name == f"replay-c{i}"
        assert previous_prefix == [f"prefix-c{i}"]
        if mode == 4:
            assert cohort is not None
            parallel_barrier.wait()
        for sample in range(samples):
            data = name.encode() + bytes([sample])
            accepted_state(data, side, name, sample, thermal + sample + 1)
        observed.append(i)

    def fake_prefix(original_log, thermal):
        assert thermal == endpoint
        return ["prefix-" + original_log.parent.name.removeprefix("measurement-")]

    expected = [{"chain": replay.chain_settings(L, i)[0], "verified_states": 2}
                for i in replay.CHAIN_IDS]
    with patch.object(replay, "run_chain", fake_chain), patch.object(
        replay, "verified_prefix", fake_prefix
    ):
        for mode in (1, 4):
            observed.clear()
            result = replay.replay_chains(Path("original"), L, Path("sampler"),
                                          Path("output"), 0, endpoint, ledger, mode)
            assert result == expected
            assert sorted(observed) == list(replay.CHAIN_IDS)
            assert len(ledger) == len(replay.CHAIN_IDS) * 2

    def misrouted_chain(sampler_path, directory, deadline, side, i, thermal, samples,
                        previous_prefix, accepted_state, *, cohort):
        wrong_name = replay.chain_settings(side, 2)[0]
        accepted_state(wrong_name.encode() + b"\0", side, wrong_name, 0, thermal + 1)

    with patch.object(replay, "run_chain", misrouted_chain), patch.object(
        replay, "verified_prefix", fake_prefix
    ):
        try:
            replay.replay_chains(Path("original"), L, Path("sampler"),
                                 Path("output"), 0, endpoint, ledger, 1)
        except ValueError as error:
            assert "Unexpected replay state identity" in str(error)
        else:
            raise AssertionError("Cross-chain replay data accepted")
print("REPLAY LEDGER, CONCURRENT CHAINS AND ANALYSIS CUSTODY FIXTURES PASS")
