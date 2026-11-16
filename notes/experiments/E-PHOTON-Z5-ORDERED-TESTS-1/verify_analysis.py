from decimal import Decimal
import io
import json

import analyze_ordered as suite

assert suite.PRIMARY_COUNT == 90
assert suite.VOLUMES == [16, 24, 32, 36, 40, 48, 64]
observables = {
    k: ["0", "0.0000000001"]
    for k, volumes in suite.ROW_VOLUMES.items()
    if 16 in volumes
}


class InputFixture:
    def __init__(self, entry):
        self.entry = entry

    def open(self, *, encoding):
        assert encoding == "utf-8"
        return io.StringIO(json.dumps(self.entry) + "\n")


entry = {
    "L": 16, "chain": "L16-c1", "sample": 0, "macrocycle": 1025,
    "observables": observables,
}
receipts = {"16": {"endpoint": 1024}}
cells = suite.get_chains([InputFixture(entry)], receipts)
assert cells[("A:E:4", 16)]["L16-c1"][0] == Decimal("0.00000000005")
rows = suite.volume_rows(cells, receipts, None)
assert rows["A:E:4"]["volumes"]["16"]["status"] == "incomplete"
assert suite.decisions(rows)["A"] == "unresolved"
entry["macrocycle"] = 1024
try:
    suite.get_chains([InputFixture(entry)], receipts)
except ValueError as error:
    assert "Wrong macrocycle" in str(error)
else:
    raise AssertionError("Wrong macrocycle was accepted")

fixture = {k: {"envelope": [0.02, 0.025], "tail_upper_display": 0.04}
           for k in suite.ROW_VOLUMES}
assert suite.decisions(fixture)["positive_channels"] == ["E", "M"]
assert suite.decisions(fixture)["B"] == "finite-grid-tail-small"
fixture["A:E:8"] = {"status": "volume-unresolved"}
assert suite.decisions(fixture)["positive_channels"] == ["M"]
fixture["D:8:pi/4:12:2"] = {"status": "volume-unresolved"}
assert suite.decisions(fixture)["B"] == "unresolved"
print("ORDERED ANALYSIS FIXTURES PASS")
