"""Causal, lossless source-order packets; no physical trial/window definition.

Every original indexed uint64 row has exactly one owner.  A closing sync row
is a nonowning lookahead reference in an emitted packet and is retained as the
first owned row of the next pending suffix.  snapshot() is observation only:
there is deliberately no EOF operation that invents a terminal interval.
"""

from dataclasses import dataclass
import json


UINT64_MAX = (1 << 64) - 1
PHYSICAL_CHANNELS = frozenset((0, 2, 4, 5, 6))
KNOWN_CHANNELS = PHYSICAL_CHANNELS | frozenset((64,))
PACKET_KINDS = frozenset(("PREFIX", "CLOSED_INTERVAL", "PENDING_SUFFIX", "UNANCHORED"))


@dataclass(frozen=True, slots=True)
class RawRow:
    index: int
    channel: int
    word2: int
    transfer: int

    def __post_init__(self):
        if type(self.index) is not int or self.index < 0:
            raise ValueError("ROW_INDEX_MUST_BE_NONNEGATIVE_INTEGER")
        if any(type(value) is not int or not 0 <= value <= UINT64_MAX
               for value in (self.channel, self.word2, self.transfer)):
            raise ValueError("RAW_WORDS_MUST_BE_UINT64")


@dataclass(frozen=True, slots=True)
class Packet:
    stream_id: str
    kind: str
    owned_rows: tuple[RawRow, ...]
    right_sync_reference: RawRow | None
    emitted_at: int | None

    def __post_init__(self):
        if not isinstance(self.stream_id, str) or not self.stream_id:
            raise ValueError("STREAM_ID_REQUIRED")
        if self.kind not in PACKET_KINDS or type(self.owned_rows) is not tuple:
            raise ValueError("INVALID_PACKET_CARRIER")
        if any(not isinstance(row, RawRow) for row in self.owned_rows):
            raise ValueError("INVALID_OWNED_ROW")
        if self.owned_rows:
            start = self.owned_rows[0].index
            if any(row.index != start + offset
                   for offset, row in enumerate(self.owned_rows)):
                raise ValueError("OWNED_ROWS_NOT_CONSECUTIVE")
        anchored = self.kind in ("CLOSED_INTERVAL", "PENDING_SUFFIX")
        if anchored:
            if not self.owned_rows or self.owned_rows[0].channel != 6:
                raise ValueError("ANCHORED_PACKET_REQUIRES_LEFT_SYNC")
            if any(row.channel == 6 for row in self.owned_rows[1:]):
                raise ValueError("INTERIOR_SYNC_NOT_ALLOWED")
        elif any(row.channel == 6 for row in self.owned_rows):
            raise ValueError("UNANCHORED_ROWS_CONTAIN_SYNC")
        if not anchored and self.owned_rows and self.owned_rows[0].index != 0:
            raise ValueError("PREFIX_MUST_START_AT_ZERO")
        emitted = self.kind in ("PREFIX", "CLOSED_INTERVAL")
        if emitted:
            right = self.right_sync_reference
            if not self.owned_rows or not isinstance(right, RawRow) or right.channel != 6:
                raise ValueError("EMITTED_PACKET_REQUIRES_RIGHT_SYNC")
            if right.index != self.owned_rows[-1].index + 1:
                raise ValueError("RIGHT_SYNC_NOT_ADJACENT_TO_OWNED_RANGE")
            if type(self.emitted_at) is not int or self.emitted_at != right.index:
                raise ValueError("EMISSION_NOT_AT_RIGHT_SYNC_ARRIVAL")
        elif self.right_sync_reference is not None or self.emitted_at is not None:
            raise ValueError("SNAPSHOT_IS_NOT_EMITTED")


class LocalObservedInterval:
    """feed accepts indices 0,1,...; emitted packets never change thereafter."""

    def __init__(self, stream_id: str):
        if not isinstance(stream_id, str) or not stream_id:
            raise ValueError("STREAM_ID_REQUIRED")
        self._stream_id = stream_id
        self._next_index = 0
        self._has_sync = False
        self._pending = []

    @property
    def next_index(self):
        return self._next_index

    def feed(self, row: RawRow) -> tuple[Packet, ...]:
        if not isinstance(row, RawRow) or row.index != self._next_index:
            raise ValueError("FEED_REQUIRES_NEXT_INDEXED_RAW_ROW")
        emitted = ()
        if row.channel == 6:
            if self._has_sync or self._pending:
                kind = "CLOSED_INTERVAL" if self._has_sync else "PREFIX"
                emitted = (Packet(self._stream_id, kind, tuple(self._pending), row, row.index),)
            self._pending = [row]
            self._has_sync = True
        else:
            self._pending.append(row)
        self._next_index += 1
        return emitted

    def feed_many(self, rows):
        """Yield in arrival order; chunk boundaries have no semantic role."""
        for row in rows:
            yield from self.feed(row)

    def snapshot(self) -> Packet:
        kind = "PENDING_SUFFIX" if self._has_sync else "UNANCHORED"
        return Packet(self._stream_id, kind, tuple(self._pending), None, None)


def row_object(row):
    return [row.index, row.channel, row.word2, row.transfer]


def packet_object(packet: Packet):
    """Explicit references derive from owned rows; all raw words remain present.

Setting/detector labels classify records only.  Deltas are signed integer ticks,
never fitted windows.  A setting-relative delta exists only for a unique
setting row.  Channel 64 and unknown channels never enter timed-row views.
"""
    rows = packet.owned_rows
    left = rows[0] if packet.kind in ("CLOSED_INTERVAL", "PENDING_SUFFIX") else None
    settings = tuple(row for row in rows if row.channel in (2, 4))
    n0 = sum(row.channel == 2 for row in settings)
    n1 = len(settings) - n0
    if n0 == 0 and n1 == 0:
        setting_tag = "MISSING"
    elif n0 == 1 and n1 == 0:
        setting_tag = "ONEHOT_0"
    elif n0 == 0 and n1 == 1:
        setting_tag = "ONEHOT_1"
    elif n0 > 0 and n1 > 0:
        setting_tag = "BOTH"
    elif n0 > 1:
        setting_tag = "REPEATED_0"
    else:
        setting_tag = "REPEATED_1"
    unique_setting = settings[0] if len(settings) == 1 else None
    detectors = tuple(row for row in rows if row.channel == 0)
    detector_tag = ("NO_RECORDED_DETECTOR_ROW" if not detectors
                    else "SINGLE_RECORDED_DETECTOR_ROW" if len(detectors) == 1
                    else "MULTIPLE_RECORDED_DETECTOR_ROWS")
    right = packet.right_sync_reference
    return {
        "stream_id": packet.stream_id,
        "kind": packet.kind,
        "emitted_at": packet.emitted_at,
        "owned_rows": [row_object(row) for row in rows],
        "left_sync_reference_index": left.index if left is not None else None,
        "right_sync_reference": row_object(right) if right is not None else None,
        "right_sync_reference_is_nonowning": True,
        "right_minus_left_sync_ticks": right.word2 - left.word2
            if right is not None and left is not None else None,
        "setting_tag": setting_tag,
        "setting_counts": [n0, n1],
        "settings": [{
            "row_index": row.index,
            "recorded_setting_code": 0 if row.channel == 2 else 1,
            "delta_from_left_sync_ticks": row.word2 - left.word2 if left is not None else None,
        } for row in settings],
        "unique_setting_reference_index": unique_setting.index if unique_setting is not None else None,
        "detector_tag": detector_tag,
        "detectors": [{
            "row_index": row.index,
            "delta_from_left_sync_ticks": row.word2 - left.word2 if left is not None else None,
            "delta_from_unique_setting_ticks": row.word2 - unique_setting.word2
                if unique_setting is not None else None,
        } for row in detectors],
        "calendar_metadata": [{"row_index": row.index, "calendar_word": row.word2}
                              for row in rows if row.channel == 64],
        "pps_row_indices": [row.index for row in rows if row.channel == 5],
        "physical_time_row_indices": [row.index for row in rows if row.channel in PHYSICAL_CHANNELS],
        "unknown_row_indices": [row.index for row in rows if row.channel not in KNOWN_CHANNELS],
        "physical_trial_or_calibrated_no_click_claim": False,
    }


def packet_bytes(packet: Packet) -> bytes:
    """Canonical compact ASCII JSON and one LF; no timestamp/path additions."""
    return (json.dumps(packet_object(packet), sort_keys=True, ensure_ascii=True,
                       separators=(",", ":"), allow_nan=False) + "\n").encode("ascii")
