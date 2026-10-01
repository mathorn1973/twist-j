"""34465A external-trigger voltage capture through an injected SCPI transport.

No socket discovery, charging, relay drive or laboratory run occurs on import.
The transport carries persistent origin; a real driver/provider is required
for MEASURED data and independently authenticated capture receipts.
"""

from dataclasses import dataclass
from copy import deepcopy
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from hashlib import sha256
from typing import Protocol

from stage_a import Invalid, check, digest, keys, number


class SCPITransport(Protocol):
    origin: str
    def write(self, command: str) -> None: ...
    def query(self, command: str) -> str: ...


@dataclass(frozen=True)
class FrozenSettings:
    idn_sha256: str
    calibration_sha256: str
    sample_count: int
    range_V: str = "1"
    nplc: str = "1"


class Keysight34465A:
    def __init__(self, transport, settings):
        check(transport.origin in ("MEASURED", "SYNTHETIC"), "transport provenance required")
        check(isinstance(settings, FrozenSettings), "frozen settings")
        check(type(settings.sample_count) is int and settings.sample_count > 0, "sample count")
        # Ten PLC needs >=1/6 s on a 50/60 Hz supply and cannot fit the
        # frozen 100 ms read window. One PLC is the selected capture mode.
        check(settings.range_V in ("1", "10", "100") and settings.nplc == "1", "reviewed 100 ms DMM mode")
        for value in (settings.idn_sha256, settings.calibration_sha256):
            digest(value, "frozen identity/calibration")
        self.transport, self.settings = transport, settings
        self.origin = transport.origin
        self.armed = False

    def text_query(self, command):
        value = self.transport.query(command)
        check(type(value) is str, "SCPI text response required")
        return value.strip()

    def rational_query(self, command):
        value = self.text_query(command)
        try:
            return Fraction(value)
        except (ValueError, ZeroDivisionError) as exc:
            raise Invalid("invalid/nonfinite SCPI numeric readback") from exc

    def configure(self):
        was_armed, self.armed = self.armed, False
        check(not was_armed, "attempt already armed; duplicate configuration consumes eligibility")
        check(self.transport.origin == self.origin, "transport provenance changed")
        identity = self.text_query("*IDN?")
        fields = identity.split(",")
        check(len(fields) == 4 and fields[0].strip() in ("Keysight Technologies", "Agilent Technologies")
              and fields[1].strip() == "34465A", "wrong instrument model/vendor")
        check(sha256(identity.encode("ascii")).hexdigest() == self.settings.idn_sha256, "unfrozen serial/firmware identity")
        # No *RST: do not hide pre-existing status or silently change outputs.
        preexisting = self.text_query("SYST:ERR?")
        check(preexisting.split(",", 1)[0] in ("0", "+0"), "pre-existing instrument error")
        for command in ("ABOR", "CONF:VOLT:DC " + self.settings.range_V,
                        "VOLT:DC:NPLC " + self.settings.nplc,
                        "VOLT:DC:ZERO:AUTO OFF", "TRIG:SOUR EXT", "TRIG:SLOP POS",
                        "TRIG:DEL 0",
                        "SAMP:COUN 1", "TRIG:COUN " + str(self.settings.sample_count)):
            self.transport.write(command)
        # Every external trigger produces one reading, at the frozen cadence.
        check(self.text_query("TRIG:SOUR?") == "EXT", "trigger readback")
        check(self.text_query("TRIG:SLOP?") == "POS", "trigger polarity")
        for command, expected in (("VOLT:DC:RANG?", number(self.settings.range_V)),
                                  ("VOLT:DC:NPLC?", number(self.settings.nplc)),
                                  ("VOLT:DC:RANG:AUTO?", 0), ("VOLT:DC:ZERO:AUTO?", 0),
                                  ("SAMP:COUN?", 1), ("TRIG:COUN?", self.settings.sample_count),
                                  ("SAMP:COUN:PRET?", 0), ("TRIG:DEL?", 0), ("TRIG:DEL:AUTO?", 0)):
            check(self.rational_query(command) == expected, "frozen readback: " + command)
        check(self.text_query("SYST:ERR?").split(",", 1)[0] in ("0", "+0"), "SCPI configuration error")

    def arm(self):
        self.configure()
        self.transport.write("INIT")
        check(self.text_query("SYST:ERR?").split(",", 1)[0] in ("0", "+0"), "SCPI initiation error")
        self.armed = True

    def fetch(self, acquisition_metadata):
        check(self.armed, "capture not armed")
        self.armed = False  # Any failure consumes this initiated attempt.
        check(self.transport.origin == self.origin, "transport provenance changed")
        response = self.transport.query("FETC?")
        check(type(response) is str, "SCPI text response required")
        values = response.strip().split(",")
        check(len(values) == self.settings.sample_count, "missing/extra readings")
        converted = []
        for value in values:
            try:
                parsed = Decimal(value.strip())
            except InvalidOperation as exc:
                raise Invalid("invalid SCPI voltage") from exc
            check(parsed.is_finite() and abs(parsed) < Decimal("9e36"), "overload/nonfinite reading")
            check(abs(parsed) <= Decimal(self.settings.range_V) * Decimal("1.2"), "voltage over range")
            converted.append(str(Fraction(parsed)))
        check(self.text_query("SYST:ERR?").split(",", 1)[0] in ("0", "+0"), "acquisition instrument error")
        required = {"specimen", "dock", "temperature_C", "history", "protocol_sha256", "external_trigger_times_s",
                    "measurement_complete_times_s", "time_U_s", "probe_on_intervals_s",
                    "both_poles_open_between_windows", "acquisition_receipt_sha256"}
        keys(acquisition_metadata, required, "complete independently observed metadata")
        acquisition_metadata = deepcopy(acquisition_metadata)
        for key in ("specimen", "dock", "history"):
            check(type(acquisition_metadata[key]) is str and acquisition_metadata[key].strip(), "capture context identifier")
        number(acquisition_metadata["temperature_C"])
        check(type(acquisition_metadata["external_trigger_times_s"]) is list and type(acquisition_metadata["measurement_complete_times_s"]) is list,
              "independent trigger/completion timestamp lists")
        check(len(acquisition_metadata["external_trigger_times_s"]) == len(converted), "missing external trigger timestamps")
        check(len(acquisition_metadata["measurement_complete_times_s"]) == len(converted), "missing observed measurement-complete timestamps")
        times = [number(x) for x in acquisition_metadata["external_trigger_times_s"]]
        completes = [number(x) for x in acquisition_metadata["measurement_complete_times_s"]]
        check(times == sorted(set(times)), "nonmonotone trigger timestamps")
        time_u = number(acquisition_metadata["time_U_s"])
        check(0 <= time_u <= Fraction(1, 1000), "time uncertainty")
        check(type(acquisition_metadata["both_poles_open_between_windows"]) is bool and acquisition_metadata["both_poles_open_between_windows"],
              "both probe poles must be observed open between windows")
        intervals = acquisition_metadata["probe_on_intervals_s"]
        check(type(intervals) is list and intervals, "observed probe intervals required")
        parsed_intervals = []
        for interval in intervals:
            check(type(interval) is list and len(interval) == 2, "probe interval shape")
            start, end = map(number, interval)
            check(end - start == Fraction(1, 5), "frozen 100 ms settle plus 100 ms read interval")
            if parsed_intervals:
                check(start > parsed_intervals[-1][1], "overlapping/out-of-order probe intervals")
            parsed_intervals.append((start, end))
        used_intervals = set()
        for i, (trigger, complete) in enumerate(zip(times, completes)):
            check(complete - trigger > 2 * time_u, "invalid measurement-complete timestamp")
            if i:
                check(trigger - time_u >= completes[i - 1] + time_u, "next trigger overlaps prior capture")
            matching = [j for j, (start, end) in enumerate(parsed_intervals)
                        if trigger - time_u >= start + Fraction(1, 10) and complete + time_u <= end]
            check(len(matching) == 1, "capture outside the settled 100 ms read window")
            used_intervals.add(matching[0])
        check(len(used_intervals) == len(parsed_intervals), "probe interval missing captured samples")
        for key in ("protocol_sha256", "acquisition_receipt_sha256"):
            digest(acquisition_metadata[key], "metadata")
        return {"kind": "RAW_DMM_CAPTURE", "origin": self.origin,
                "idn_sha256": self.settings.idn_sha256, "calibration_sha256": self.settings.calibration_sha256,
                "scpi_response": response, "voltage_V": converted, "metadata": acquisition_metadata}
