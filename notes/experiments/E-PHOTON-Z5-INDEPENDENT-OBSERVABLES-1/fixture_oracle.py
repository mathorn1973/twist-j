#!/usr/bin/env python3
"""Independent standard-library oracle for frozen Z5 link-state fixtures.

This module deliberately reconstructs every observable from the serialized
link residues.  It imports and shares no C++ reader source.
"""

from __future__ import annotations

from dataclasses import dataclass
import argparse
import hashlib
import itertools
import json
from pathlib import Path
import re
import sys
from typing import Iterable, Sequence


DIM = 4
MODULUS = 5
PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
PAIR_TO_INDEX = {pair: index for index, pair in enumerate(PAIRS)}
TRIPLES = tuple(itertools.combinations(range(DIM), 3))
STATE_SCHEMA = "TWISTJ_Z5_LINK_STATE_V1"
OBSERVABLE_SCHEMA = "TWISTJ_Z5_INDEPENDENT_OBSERVABLES_V1"
CHAIN_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,63}")
DECIMAL_RE = re.compile(r"0|[1-9][0-9]*")
SHA256_RE = re.compile(r"[0-9a-f]{64}")
MASK64 = (1 << 64) - 1
UINT64_MAX = (1 << 64) - 1


class IntegrityError(ValueError):
    """A strict state or exact observable invariant failed."""


@dataclass(frozen=True)
class LinkState:
    raw: bytes
    sha256: str
    L: int
    chain: str
    sample: int
    macrocycle: int
    links: tuple[int, ...]


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n"


def _canonical_decimal(text: str, field: str) -> int:
    if DECIMAL_RE.fullmatch(text) is None:
        raise IntegrityError(f"noncanonical {field}")
    value = int(text)
    if value > UINT64_MAX:
        raise IntegrityError(f"{field} decimal overflow")
    return value


def parse_state_bytes(data: bytes, expected_sha256: str) -> LinkState:
    if SHA256_RE.fullmatch(expected_sha256) is None:
        raise IntegrityError("invalid expected sha256")
    actual = hashlib.sha256(data).hexdigest()
    if actual != expected_sha256:
        raise IntegrityError("state sha256 mismatch")
    try:
        text = data.decode("ascii")
    except UnicodeDecodeError as exc:
        raise IntegrityError("state is not ASCII") from exc
    if not text.endswith("\n") or "\r" in text or "\x00" in text:
        raise IntegrityError("state must be LF-only ASCII with final LF")
    pieces = text.split("\n")
    if len(pieces) != 8 or pieces[-1] != "":
        raise IntegrityError("state must have exactly seven lines")
    lines = pieces[:-1]
    if lines[0] != STATE_SCHEMA or lines[6] != "END":
        raise IntegrityError("state framing mismatch")
    prefixes = ("L=", "CHAIN=", "SAMPLE=", "MACROCYCLE=", "LINKS=")
    for line, prefix in zip(lines[1:6], prefixes):
        if not line.startswith(prefix):
            raise IntegrityError(f"missing {prefix[:-1]}")
    linear_size = _canonical_decimal(lines[1][2:], "L")
    if not 2 <= linear_size <= 32:
        raise IntegrityError("L must be in the frozen range 2..32")
    chain = lines[2][6:]
    if CHAIN_RE.fullmatch(chain) is None:
        raise IntegrityError("invalid CHAIN")
    sample = _canonical_decimal(lines[3][7:], "SAMPLE")
    macrocycle = _canonical_decimal(lines[4][11:], "MACROCYCLE")
    payload = lines[5][6:]
    expected_links = DIM * linear_size**DIM
    if len(payload) != expected_links or any(char not in "01234" for char in payload):
        raise IntegrityError("invalid LINKS payload")
    links = tuple(ord(char) - ord("0") for char in payload)
    if data != encode_state_bytes(linear_size, chain, sample, macrocycle, links):
        raise IntegrityError("state is not in exact canonical serialization")
    return LinkState(
        raw=data,
        sha256=actual,
        L=linear_size,
        chain=chain,
        sample=sample,
        macrocycle=macrocycle,
        links=links,
    )


def read_state(path: Path | str, expected_sha256: str) -> LinkState:
    return parse_state_bytes(Path(path).read_bytes(), expected_sha256)


def encode_state_bytes(
    L: int,
    chain: str,
    sample: int,
    macrocycle: int,
    links: Sequence[int],
) -> bytes:
    if (
        not 2 <= L <= 32
        or CHAIN_RE.fullmatch(chain) is None
        or not 0 <= sample <= UINT64_MAX
        or not 0 <= macrocycle <= UINT64_MAX
    ):
        raise IntegrityError("invalid generated state metadata")
    if len(links) != DIM * L**DIM or any(value not in range(MODULUS) for value in links):
        raise IntegrityError("invalid generated link field")
    payload = "".join(str(value) for value in links)
    return (
        f"{STATE_SCHEMA}\nL={L}\nCHAIN={chain}\nSAMPLE={sample}\n"
        f"MACROCYCLE={macrocycle}\nLINKS={payload}\nEND\n"
    ).encode("ascii")


class Geometry:
    def __init__(self, L: int) -> None:
        self.L = L
        self.volume = L**DIM
        self.coords = tuple(self._decode(site) for site in range(self.volume))
        plus: list[tuple[int, int, int, int]] = []
        minus: list[tuple[int, int, int, int]] = []
        for coordinate in self.coords:
            forward: list[int] = []
            backward: list[int] = []
            for mu in range(DIM):
                xp = list(coordinate)
                xm = list(coordinate)
                xp[mu] = (xp[mu] + 1) % L
                xm[mu] = (xm[mu] - 1) % L
                forward.append(self._encode(xp))
                backward.append(self._encode(xm))
            plus.append(tuple(forward))
            minus.append(tuple(backward))
        self.plus = tuple(plus)
        self.minus = tuple(minus)

    def _decode(self, site: int) -> tuple[int, int, int, int]:
        coordinate = [0] * DIM
        for mu in range(DIM - 1, -1, -1):
            coordinate[mu] = site % self.L
            site //= self.L
        return tuple(coordinate)  # type: ignore[return-value]

    def _encode(self, coordinate: Sequence[int]) -> int:
        site = 0
        for value in coordinate:
            site = site * self.L + (value % self.L)
        return site

    def shifted(self, site: int, mu: int, steps: int) -> int:
        result = site
        table = self.plus if steps >= 0 else self.minus
        for _ in range(abs(steps)):
            result = table[result][mu]
        return result


def _principal(residue: int) -> int:
    residue %= MODULUS
    return residue if residue <= 2 else residue - MODULUS


def _fnvlike(values: Iterable[int]) -> str:
    fingerprint = 1469598103934665603
    for value in values:
        fingerprint ^= value
        fingerprint = (fingerprint * 1099511628211) & MASK64
    return f"{fingerprint:016x}"


def _plaquette_flux(geometry: Geometry, links: Sequence[int]) -> tuple[int, ...]:
    flux = [0] * (geometry.volume * len(PAIRS))
    for site in range(geometry.volume):
        for pair_index, (a, b) in enumerate(PAIRS):
            flux[site * len(PAIRS) + pair_index] = (
                links[site * DIM + a]
                + links[geometry.plus[site][a] * DIM + b]
                - links[geometry.plus[site][b] * DIM + a]
                - links[site * DIM + b]
            ) % MODULUS
    return tuple(flux)


class DisjointSets:
    def __init__(self, items: Iterable[int]) -> None:
        self.parent = {item: item for item in items}

    def find(self, item: int) -> int:
        parent = self.parent[item]
        if parent != item:
            self.parent[item] = self.find(parent)
        return self.parent[item]

    def join(self, left: int, right: int) -> None:
        a = self.find(left)
        b = self.find(right)
        if a != b:
            if a > b:
                a, b = b, a
            self.parent[b] = a

    def groups(self) -> list[list[int]]:
        result: dict[int, list[int]] = {}
        for item in self.parent:
            result.setdefault(self.find(item), []).append(item)
        return [sorted(group) for group in result.values()]


def _cube_faces(geometry: Geometry, site: int, triple: tuple[int, int, int]) -> list[tuple[int, int]]:
    result: list[tuple[int, int]] = []
    for position, axis in enumerate(triple):
        face = tuple(value for value in triple if value != axis)
        pair_index = PAIR_TO_INDEX[face]
        sign = 1 if position % 2 == 0 else -1
        result.append((geometry.plus[site][axis] * len(PAIRS) + pair_index, sign))
        result.append((site * len(PAIRS) + pair_index, -sign))
    return result


HODGE = (
    ((0, 1), (2, 3), +1),
    ((0, 2), (1, 3), -1),
    ((0, 3), (1, 2), +1),
    ((1, 2), (0, 3), +1),
    ((1, 3), (0, 2), -1),
    ((2, 3), (0, 1), +1),
)


def _vortex_homology(
    geometry: Geometry,
    flux: Sequence[int],
    allowed_faces: set[int] | None,
) -> list[int]:
    periods: list[int] = []
    for homology_pair, primal_pair, sign in HODGE:
        pair_index = PAIR_TO_INDEX[primal_pair]
        total = 0
        for site, coordinate in enumerate(geometry.coords):
            if any(coordinate[axis] != 0 for axis in homology_pair):
                continue
            face = site * len(PAIRS) + pair_index
            if allowed_faces is None or face in allowed_faces:
                total += sign * flux[face]
        periods.append(total % MODULUS)
    return periods


def _vortex_observables(geometry: Geometry, flux: Sequence[int]) -> dict[str, object]:
    occupied = [face for face, value in enumerate(flux) if value]
    sets = DisjointSets(occupied)
    closure_ok = True
    for site in range(geometry.volume):
        for triple in TRIPLES:
            boundary = _cube_faces(geometry, site, triple)
            if sum(sign * flux[face] for face, sign in boundary) % MODULUS:
                closure_ok = False
            active = sorted({face for face, _ in boundary if flux[face]})
            for face in active[1:]:
                sets.join(active[0], face)
    if not closure_ok:
        raise IntegrityError("vortex mod-five closure failed")
    components: list[dict[str, object]] = []
    for group in sorted(sets.groups(), key=lambda faces: faces[0]):
        face_set = set(group)
        homology = _vortex_homology(geometry, flux, face_set)
        components.append(
            {
                "anchor_face": group[0],
                "support_faces": len(group),
                "charged_area": sum(abs(_principal(flux[face])) for face in group),
                "charged_homology_f5": homology,
                "wraps": any(homology),
            }
        )
    global_homology = _vortex_homology(geometry, flux, None)
    if any(global_homology):
        raise IntegrityError("exact link state has nonzero global vortex homology")
    return {
        "charged_area": sum(
            int(component["charged_area"]) for component in components
        ),
        "homology_order": [f"{a}{b}" for a, b in PAIRS],
        "occupied_faces": len(occupied),
        "wraps": any(bool(component["wraps"]) for component in components),
        "closure": "PASS",
        "global_charged_homology_f5": global_homology,
        "components": components,
        "support_size_tail_desc": sorted(
            (int(component["support_faces"]) for component in components), reverse=True
        ),
    }


def _monopole_current(geometry: Geometry, flux: Sequence[int]) -> tuple[int, ...]:
    current = [0] * (geometry.volume * DIM)
    for missing in range(DIM):
        axes = [axis for axis in range(DIM) if axis != missing]
        a, b, c = axes
        pbc = PAIR_TO_INDEX[(b, c)]
        pac = PAIR_TO_INDEX[(a, c)]
        pab = PAIR_TO_INDEX[(a, b)]
        epsilon = 1 if missing % 2 == 0 else -1
        for site in range(geometry.volume):
            df = (
                _principal(flux[geometry.plus[site][a] * len(PAIRS) + pbc])
                - _principal(flux[site * len(PAIRS) + pbc])
                - _principal(flux[geometry.plus[site][b] * len(PAIRS) + pac])
                + _principal(flux[site * len(PAIRS) + pac])
                + _principal(flux[geometry.plus[site][c] * len(PAIRS) + pab])
                - _principal(flux[site * len(PAIRS) + pab])
            )
            if df % MODULUS:
                raise IntegrityError("monopole current is not integral")
            value = epsilon * (df // MODULUS)
            if value < -2 or value > 2:
                raise IntegrityError("monopole current outside frozen range")
            dual_base = geometry.minus[site][missing]
            current[dual_base * DIM + missing] = value
    for site in range(geometry.volume):
        divergence = sum(
            current[site * DIM + mu] - current[geometry.minus[site][mu] * DIM + mu]
            for mu in range(DIM)
        )
        if divergence:
            raise IntegrityError("monopole current closure failed")
    return tuple(current)


def _component_windings(
    geometry: Geometry,
    current: Sequence[int],
    links: Sequence[int] | None,
) -> list[int]:
    result = []
    allowed = None if links is None else set(links)
    for mu in range(DIM):
        total = 0
        for link in range(geometry.volume * DIM):
            if link % DIM != mu or (allowed is not None and link not in allowed):
                continue
            site = link // DIM
            if geometry.coords[site][mu] == geometry.L - 1:
                total += current[link]
        result.append(total)
    return result


def _monopole_observables(geometry: Geometry, current: Sequence[int]) -> dict[str, object]:
    occupied = [link for link, value in enumerate(current) if value]
    sets = DisjointSets(occupied)
    at_vertex: list[list[int]] = [[] for _ in range(geometry.volume)]
    for link in occupied:
        site, mu = divmod(link, DIM)
        at_vertex[site].append(link)
        at_vertex[geometry.plus[site][mu]].append(link)
    for incident in at_vertex:
        active = sorted(set(incident))
        for link in active[1:]:
            sets.join(active[0], link)
    components: list[dict[str, object]] = []
    for group in sorted(sets.groups(), key=lambda links: links[0]):
        windings = _component_windings(geometry, current, group)
        components.append(
            {
                "anchor_link": group[0],
                "support_links": len(group),
                "charged_length": sum(abs(current[link]) for link in group),
                "windings_z": windings,
                "wraps": any(windings),
            }
        )
    counts = [sum(1 for value in current if value == charge) for charge in range(-2, 3)]
    support_tail = sorted((int(item["support_links"]) for item in components), reverse=True)
    charged_tail = sorted((int(item["charged_length"]) for item in components), reverse=True)
    global_windings = _component_windings(geometry, current, None)
    if any(global_windings):
        raise IntegrityError("exact link state has nonzero global monopole winding")
    return {
        "current_count_order": [-2, -1, 0, 1, 2],
        "current_counts": counts,
        "occupied_links": len(occupied),
        "charged_length": sum(abs(value) for value in current),
        "wraps": any(bool(component["wraps"]) for component in components),
        "closure": "PASS",
        "global_windings_z": global_windings,
        "largest_support_over_volume": [max(support_tail, default=0), geometry.volume],
        "components": components,
        "support_size_tail_desc": support_tail,
        "charged_length_tail_desc": charged_tail,
    }


def _polyakov_observables(
    geometry: Geometry,
    links: Sequence[int],
) -> dict[str, object]:
    directions: list[dict[str, object]] = []
    for mu in range(DIM):
        counts = [0] * MODULUS
        for site, coordinate in enumerate(geometry.coords):
            if coordinate[mu] != 0:
                continue
            phase = 0
            cursor = site
            for _ in range(geometry.L):
                phase = (phase + links[cursor * DIM + mu]) % MODULUS
                cursor = geometry.plus[cursor][mu]
            counts[phase] += 1
        directions.append({"mu": mu, "phase_counts": counts})
    return {"directions": directions, "line_count": geometry.L**3}


def _correlator_observables(geometry: Geometry, flux: Sequence[int]) -> dict[str, object]:
    plus_terms = [
        (rho, pair_index)
        for rho in range(DIM)
        for pair_index, pair in enumerate(PAIRS)
        if rho in pair
    ]
    minus_terms = [
        (rho, pair_index)
        for rho in range(DIM)
        for pair_index, pair in enumerate(PAIRS)
        if rho not in pair
    ]
    if len(plus_terms) != 12 or len(minus_terms) != 12:
        raise IntegrityError("correlator orientation census failed")
    terms: list[dict[str, object]] = []
    for kind, inventory in (("plus", plus_terms), ("minus", minus_terms)):
        for rho, pair_index in inventory:
            separations: list[dict[str, object]] = []
            for separation in range(1, geometry.L // 2 + 1):
                product_counts = [0] * MODULUS
                left_counts = [0] * MODULUS
                right_counts = [0] * MODULUS
                for site in range(geometry.volume):
                    other = geometry.shifted(site, rho, separation)
                    left_flux = flux[site * len(PAIRS) + pair_index]
                    right_flux = flux[other * len(PAIRS) + pair_index]
                    left_phase = left_flux if kind == "plus" else (-left_flux) % MODULUS
                    product_counts[(left_phase + right_flux) % MODULUS] += 1
                    left_counts[left_phase] += 1
                    right_counts[right_flux] += 1
                separations.append(
                    {
                        "n": separation,
                        "count": geometry.volume,
                        "product_counts": product_counts,
                        "left_counts": left_counts,
                        "right_counts": right_counts,
                    }
                )
            terms.append(
                {
                    "kind": kind,
                    "rho": rho,
                    "pair": list(PAIRS[pair_index]),
                    "separations": separations,
                }
            )
    return {"n_max": geometry.L // 2, "terms": terms}


def observe(state: LinkState) -> dict[str, object]:
    geometry = Geometry(state.L)
    flux = _plaquette_flux(geometry, state.links)
    current = _monopole_current(geometry, flux)
    flux_counts = [sum(1 for value in flux if value == residue) for residue in range(MODULUS)]
    link_bytes = bytes(state.links)
    return {
        "schema": OBSERVABLE_SCHEMA,
        "state": {
            "schema": STATE_SCHEMA,
            "sha256": state.sha256,
            "bytes": len(state.raw),
            "L": state.L,
            "chain": state.chain,
            "sample": state.sample,
            "macrocycle": state.macrocycle,
            "links_sha256": hashlib.sha256(link_bytes).hexdigest(),
            "state_fingerprint": _fnvlike(itertools.chain(state.links, flux)),
            "cache_fingerprint": _fnvlike(flux),
        },
        "flux": {"counts": flux_counts},
        "polyakov": _polyakov_observables(geometry, state.links),
        "vortex": _vortex_observables(geometry, flux),
        "monopole": _monopole_observables(geometry, current),
        "correlator": _correlator_observables(geometry, flux),
    }


def _main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--state", required=True, type=Path)
    parser.add_argument("--expected-sha256", required=True)
    options = parser.parse_args()
    state = read_state(options.state, options.expected_sha256)
    sys.stdout.buffer.write(canonical_json(observe(state)).encode("ascii"))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
