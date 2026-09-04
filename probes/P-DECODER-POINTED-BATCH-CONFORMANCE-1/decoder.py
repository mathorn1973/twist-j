"""Executable chosen decoder on every pointed Canon trajectory.

Mathematical candidate only. Run this program after its public preregistration
pin. All exact ratios are serialized as numerator/denominator objects. There
is no physical occurrence sampler, SI calibration or write into autonomous U.
"""

from dataclasses import dataclass, fields, is_dataclass
from fractions import Fraction

import apparatus
import geometry
import kernel


CANDIDATE_ID = "DECODER-POINTED-BATCH-1"


@dataclass(frozen=True, slots=True)
class MatterRecord:
    anchored_piston: tuple[int, int, int, int]
    qdd: kernel.QDDRecord
    linear_tr4: int
    binary_theta: int


@dataclass(frozen=True, slots=True)
class GeometryFrame:
    seed: geometry.GeometryRecord
    wave: geometry.WaveState


@dataclass(frozen=True, slots=True)
class ClockRecord:
    source_header: kernel.Checkpoint
    checkpoint: kernel.Checkpoint
    elapsed_cut: int
    absolute_counter: int
    tick_cycles: Fraction
    batch: apparatus.BatchRecord
    terminal_batch: bool


@dataclass(frozen=True, slots=True)
class Frame:
    matter: MatterRecord
    geometry: GeometryFrame
    clock: ClockRecord


@dataclass(frozen=True, slots=True)
class History:
    candidate_id: str
    source_header: kernel.Checkpoint
    frames: tuple[Frame, ...]


@dataclass(frozen=True, slots=True)
class Decoder:
    source: kernel.Checkpoint

    def __post_init__(self) -> None:
        kernel.validate_head(self.source)

    def stream(self):
        """The unique infinite stream, interpreted through finite prefixes.

        Matter is evaluated first, then geometry, then the clock/batch write.
        Per-cut linear and binary observations read the actual checkpoint.
        Only the five QDD fields, source injections and A seed are head anchored.
        """
        v = kernel.balanced_head(self.source)
        qdd = kernel.direct_qdd(self.source)
        seed = geometry.geometry_seed(v)
        wave_previous, wave_next = geometry.wave_initial(v)
        wave = wave_previous
        support, controller = apparatus.prepare(self.source, v)
        while True:
            checkpoint = support.checkpoint
            matter = MatterRecord(v, qdd, kernel.linear_tr4(checkpoint),
                                  kernel.theta(checkpoint[0]))
            spatial = GeometryFrame(seed, wave)
            successor = kernel.u_step(checkpoint)
            next_support, next_controller, batch = apparatus.step(
                support, controller, successor)
            clock = ClockRecord(self.source, checkpoint, support.relative_cut,
                                checkpoint[0], Fraction(checkpoint[0], 5),
                                batch, apparatus.terminal(batch))
            yield Frame(matter, spatial, clock)
            if support.relative_cut == 0:
                wave = wave_next
            else:
                wave_previous, wave_next = wave_next, geometry.wave_step(
                    wave_previous, wave_next)
                wave = wave_next
            support, controller = next_support, next_controller

    def prefix(self, cuts: int) -> History:
        if type(cuts) is not int or cuts < 0:
            raise ValueError("cuts must be an exact nonnegative integer")
        stream = self.stream()
        return History(CANDIDATE_ID, self.source, tuple(next(stream) for _ in range(cuts)))


def exact_json(value):
    """Lossless JSON presentation of this candidate's typed finite records."""
    if isinstance(value, Fraction):
        return {"numerator": value.numerator, "denominator": value.denominator}
    if is_dataclass(value) and not isinstance(value, type):
        return {"type": type(value).__name__,
                **{field.name: exact_json(getattr(value, field.name))
                   for field in fields(value)}}
    if isinstance(value, tuple):
        return [exact_json(item) for item in value]
    if value is None or type(value) in (str, int, bool):
        return value
    raise TypeError("unsupported exact record value")


def main() -> None:
    import argparse
    import json

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--head", nargs=7, type=int, required=True,
                        metavar=("N", "P1", "P4", "P1P", "P4P", "Q", "R"))
    parser.add_argument("--cuts", type=int, default=3)
    args = parser.parse_args()
    source = args.head[0], tuple(args.head[1:])
    print(json.dumps(exact_json(Decoder(source).prefix(args.cuts)),
                     sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
