"""Independent acquisition and immutable evidence interfaces, no fake driver."""

from dataclasses import dataclass
from hashlib import sha256
from typing import Protocol
from schema import digest, require


@dataclass(frozen=True)
class Capture:
    origin: str
    raw_bytes: bytes
    acquisition_receipt: bytes


class InstrumentAdapter(Protocol):
    """Runs separately from controller; never receives an expected state trace.

    The future NI/Keysight implementation must capture simultaneous raw signed
    ADC, external time, specimen identity/temperature, probe on-time, gaps,
    saturation and physical pointer/cut/dock feedback. No real adapter is
    available here; this interface cannot qualify or energize equipment.
    """
    def capture(self, frozen_settings: bytes) -> Capture: ...


class ImmutableEvidenceStore(Protocol):
    """Approved, versioned, licensed external corpus; retains failed attempts.

    put_once must enforce immutability independently of the caller and return
    a provider-authenticated receipt. No large ADC payload enters Canon.
    """
    def put_once(self, content_sha256: str, data: bytes) -> bytes: ...
    def get(self, content_sha256: str) -> bytes: ...
    def verify_receipt(self, receipt: bytes, content_sha256: str) -> None: ...


def retain(capture, store, source, version, license_id):
    require(isinstance(capture, Capture) and capture.origin in ("MEASURED", "SYNTHETIC"), "typed capture")
    require(type(capture.raw_bytes) is bytes and capture.raw_bytes, "raw bytes required")
    require(bool(source) and bool(version) and bool(license_id), "external corpus metadata")
    require(store is not None, "approved immutable evidence store unavailable")
    content_hash = sha256(capture.raw_bytes).hexdigest()
    receipt = store.put_once(content_hash, capture.raw_bytes)
    store.verify_receipt(receipt, content_hash)
    require(sha256(store.get(content_hash)).hexdigest() == content_hash, "immutable store readback mismatch")
    return {"origin": capture.origin, "sha256": content_hash, "bytes": len(capture.raw_bytes),
            "source": source, "version": version, "license": license_id}


def confirm_acquisition(capture, verifier):
    """Origin cannot be promoted by renaming a file or setting origin=MEASURED."""
    require(capture.origin == "MEASURED", "synthetic capture cannot confirm")
    require(verifier is not None, "independent acquisition attestation unavailable")
    verifier.verify(capture.raw_bytes, capture.acquisition_receipt)


class SyntheticAdapter:
    def __init__(self, data):
        self.data = bytes(data)

    def capture(self, frozen_settings):
        require(type(frozen_settings) is bytes, "settings bytes")
        return Capture("SYNTHETIC", self.data, b"SYNTHETIC-NOT-AN-INSTRUMENT-RECEIPT")
