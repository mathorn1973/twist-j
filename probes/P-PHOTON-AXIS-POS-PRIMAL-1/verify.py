#!/usr/bin/env python3
"""Formal verifier of P-PHOTON-AXIS-POS-PRIMAL-1 (Python standard library only).

Run from the repository root:

    LC_ALL=C LANG=C PYTHONDONTWRITEBYTECODE=1 PYTHONHASHSEED=0 TZ=UTC \
        python3 probes/P-PHOTON-AXIS-POS-PRIMAL-1/verify.py

It checks, in order:

1. the pin manifest SHA256SUMS when present, and the immutable pilot-2
   dependency bytes;
2. the orientation, pair and score tables written into axis_engine.cpp;
3. the exact score identities in Z[phi];
4. the AXIS fixtures: slice sums recomputed here from the fixture link
   strings, and the exact identity between the direct centred Fourier power
   and the folded autocorrelation reduction, in Q(phi)[x]/Phi_2L(x);
5. the deterministic cosine table, the Student-t quantile and the a_L formula;
6. bit identity of the lazy statistics with the pilot-2 originals;
7. the twenty seeds and the terminal grammar;
8. when production records exist, a complete replay of the frozen analysis,
   which must equal ANALYSIS.txt byte for byte.

The last line is VERIFY PASS, or VERIFY FAIL with a reason and exit code 1.
"""

from __future__ import annotations

from fractions import Fraction
import hashlib
import math
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import axis_core as core  # noqa: E402

P = core.P

PINNED_FILES = (
    "PREREG.md", "AXIS_PIN.md", "README.md", "axis_engine.cpp", "axis_core.py",
    "axis_reader.py", "run_axis.py", "verify.py", "FIXTURE_EXPECTED.txt",
)
PILOT_DEPENDENCIES = (
    ("photon_z5.cpp", "68232b2f44bca6fd71514547e2f5aa0ad8aa85b9d298dde5d9a4109ac2151e14"),
    ("photon_z5_part1.inc", "263b631d6322526296cef5b32104f9bbc34184a8506f30fc15962687fcd6727a"),
    ("photon_z5_part2.inc", "7d1183e0f8368310be259fb88fac54aaba9e8661c64112e2577e9929e8ea379d"),
    ("photon_z5_part3.inc", "c6f5776e5c401618bd8478cf98bf99ad9020f50b0dc4495e53e2eea4a971686a"),
    ("photon_z5_part4.inc", "442f79534fc7849fa4801d46908c24abf2d22e0b31a5fdec2e4b068bfd66db4b"),
    ("analyze_pilot.py", "d3d2ffba5ade37863f8e34a9b6c8198cf3e222aa8f12a6ba78b621d5c5bef4ce"),
    ("SELFTEST_EXPECTED.txt", "621f95193d744e3b33d1c469e45d83d84d7b44f8cc571ca7695457f08e9a43da"),
    ("REFERENCE_EXPECTED.txt", "6c86ca3be9c94b0581fe9af2fde41352db0b7f20c48d6b7e066bcebe1476d7be"),
)
FIXTURE_SIZES = (3, 4, 6)
ENGINE_PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))
T995_TABLE = ((30, Fraction(2749996, 10**6)), (60, Fraction(2660283, 10**6)),
              (120, Fraction(2617421, 10**6)))


class VerifyError(Exception):
    pass


def require(ok: bool, message: str) -> None:
    if not ok:
        raise VerifyError(message)


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


# ---------------------------------------------------------------------------
# 1. Custody
# ---------------------------------------------------------------------------


def custody(out: list[str]) -> None:
    manifest = HERE / "SHA256SUMS"
    if manifest.exists():
        raw = manifest.read_bytes()
        require(raw.endswith(b"\n") and b"\r" not in raw, "SHA256SUMS format")
        names = []
        for line in raw.decode("ascii").splitlines():
            digest, sep, name = line.partition("  ")
            require(bool(sep) and len(digest) == 64, "SHA256SUMS malformed")
            require(sha256((HERE / name).read_bytes()) == digest, f"pinned hash mismatch {name}")
            names.append(name)
        require(tuple(names) == PINNED_FILES, "SHA256SUMS inventory or order")
        out.append(f"PIN_MANIFEST PASS entries={len(names)} sha256={sha256(raw)}")
    else:
        out.append("PIN_MANIFEST ABSENT mode=PRE_PIN")
    for name, digest in PILOT_DEPENDENCIES:
        require(sha256((core.PILOT_DIR / name).read_bytes()) == digest, f"pilot dependency {name}")
    out.append(f"PILOT_DEPENDENCIES PASS files={len(PILOT_DEPENDENCIES)}")


# ---------------------------------------------------------------------------
# 2. Engine tables
# ---------------------------------------------------------------------------


def engine_tables(out: list[str]) -> None:
    text = (HERE / "axis_engine.cpp").read_text(encoding="ascii")
    require('#define main pilot2_engine_main\n#include "../P-PHOTON-Z5-EXACT-HEATBATH-MIXING-PILOT-2/'
            'photon_z5.cpp"\n#undef main\n' in text, "engine does not include pilot-2 byte for byte")
    orient = re.findall(r'\{"(\d\d)", (\d), ([+-]1)\}', text)
    require(len(orient) == 6, "engine orientation table")
    for (name, pair, sign), expected in zip(orient, core.ORIENT):
        require(name == expected, "engine orientation order")
        a, b = int(name[0]), int(name[1])
        require(ENGINE_PAIRS[int(pair)] == (min(a, b), max(a, b)), f"engine pair index {name}")
        require(int(sign) == (1 if a < b else -1), f"engine orientation sign {name}")
    score = re.findall(r"\{\{(-?\d+), (-?\d+)\}\}", text.split("SCORE_UV", 1)[1].split(";", 1)[0])
    require(tuple((int(u), int(v)) for u, v in score) == core.SCORE_UV, "engine score table")
    for name in core.ORIENT:
        require(sum(core.CONTAINS[core.ORIENT.index(name)]) == 2, "orientation axis count")
    for r in range(4):
        require(sum(row[r] for row in core.CONTAINS) == 3, "three orientations contain each axis")
    out.append("ENGINE_TABLES PASS orientations=01,02,03,23,31,12 F31=-F13 score_basis=1,phi")


# ---------------------------------------------------------------------------
# 3. Score identities in Z[phi] (u + v phi, phi^2 = phi + 1, sqrt5 = 2 phi - 1)
# ---------------------------------------------------------------------------


def score_identities(out: list[str]) -> None:
    mul = core.zphi_mul
    G = core.SCORE_UV
    require(all(G[(5 - f) % 5] == (-G[f][0], -G[f][1]) for f in range(5)), "score is odd under f -> -f")
    kappa2 = (7, -4)  # 5 - 2 sqrt5
    require(mul(G[2], G[2]) == (5, 8), "(2 + sqrt5)^2 = 9 + 4 sqrt5")
    require(mul(kappa2, mul(G[1], G[1])) == (7, -4), "X^2 = 5 - 2 sqrt5 at flux 1")
    require(mul(kappa2, mul(G[2], G[2])) == (3, 4), "X^2 = 5 + 2 sqrt5 at flux 2")
    require(mul((7, -4), (3, 4)) == (5, 0), "tan^2(pi/5) tan^2(2pi/5) = 5")
    require(core.KAPPA2 == 5.0 - 2.0 * math.sqrt(5.0), "float kappa^2")
    out.append("SCORE_IDENTITIES PASS G=(0,1,2+sqrt5,-(2+sqrt5),-1) kappa^2=5-2sqrt5 "
               "X^2_1,4=5-2sqrt5 X^2_2,3=5+2sqrt5")


# ---------------------------------------------------------------------------
# 4. Fixtures and the exact Fourier reduction
# ---------------------------------------------------------------------------


def poly_divmod_int(num: list[int], den: list[int]) -> tuple[list[int], list[int]]:
    num = num[:]
    q = [0] * max(1, len(num) - len(den) + 1)
    while len(num) >= len(den) and any(num):
        shift = len(num) - len(den)
        coef = num[-1] // den[-1]
        require(coef * den[-1] == num[-1], "inexact cyclotomic division")
        q[shift] = coef
        for i, d in enumerate(den):
            num[shift + i] -= coef * d
        while num and num[-1] == 0:
            num.pop()
    return q, num


def cyclotomic(n: int) -> list[int]:
    poly = [-1] + [0] * (n - 1) + [1]
    for d in range(1, n):
        if n % d == 0:
            poly, rem = poly_divmod_int(poly, cyclotomic(d))
            require(not rem, "cyclotomic remainder")
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def reduce_mod(poly: dict[int, tuple[Fraction, Fraction]], phi_n: list[int]) -> list[tuple[Fraction, Fraction]]:
    deg = len(phi_n) - 1
    top = max(poly) if poly else 0
    coeffs = [[Fraction(0), Fraction(0)] for _ in range(max(top + 1, deg))]
    for e, (u, v) in poly.items():
        coeffs[e][0] += u
        coeffs[e][1] += v
    for e in range(len(coeffs) - 1, deg - 1, -1):
        cu, cv = coeffs[e]
        if cu == 0 and cv == 0:
            continue
        for i, d in enumerate(phi_n):
            coeffs[e - deg + i][0] -= cu * d
            coeffs[e - deg + i][1] -= cv * d
    return [(u, v) for u, v in coeffs[:deg]]


def fixture_blocks() -> dict[int, tuple[str, dict[tuple[str, int], list[tuple[int, int]]]]]:
    lines = core.text_lines((HERE / "FIXTURE_EXPECTED.txt").read_bytes(), "FIXTURE_EXPECTED.txt")
    blocks = {}
    cursor = 0
    for L in FIXTURE_SIZES:
        head = core.parse_fields(lines[cursor], "AXIS_FIXTURE")
        require(tuple(head) == ("L", "links") and head["L"] == str(L), "fixture header")
        cursor += 1
        S = {}
        for name in core.ORIENT:
            for r in range(4):
                fields = core.parse_fields(lines[cursor], "AXIS_FIXTURE_S")
                require((fields.get("index"), fields.get("I"), fields.get("r")) == ("0", name, str(r)),
                        "fixture order")
                S[(name, r)] = core.parse_pairs(fields["S"], L, "fixture")
                cursor += 1
        blocks[L] = (head["links"], S)
    require(cursor == len(lines), "fixture trailing lines")
    return blocks


def fixtures(out: list[str]) -> None:
    for L, (links, engine_S) in fixture_blocks().items():
        require(len(links) == 4 * L**4 and set(links) <= set("01234"), "fixture link string")
        expected_links = "".join(str((7 * site + 3 * mu + site // 3) % 5)
                                 for site in range(L**4) for mu in range(4))
        require(links == expected_links, "fixture link field differs from its definition")

        def coord(site: int) -> tuple[int, int, int, int]:
            x3 = site % L
            x2 = (site // L) % L
            x1 = (site // L**2) % L
            x0 = site // L**3
            return (x0, x1, x2, x3)

        def site_of(x) -> int:
            return ((x[0] * L + x[1]) * L + x[2]) * L + x[3]

        def link(x, mu: int) -> int:
            return int(links[4 * site_of(x) + mu])

        def step(x, mu: int):
            y = list(x)
            y[mu] = (y[mu] + 1) % L
            return tuple(y)

        phi_n = cyclotomic(2 * L)
        weights_exact = []
        for k in range(L // 2 + 1):
            mult = 1 if k == 0 or 2 * k == L else 2
            weights_exact.append((k, Fraction(mult, 2)))
        mine = {}
        R, _ = core.reduce_sample(engine_S, L)
        for i, name in enumerate(core.ORIENT):
            a, b = core.ORIENT_AXES[i]
            flux = {}
            for site in range(L**4):
                x = coord(site)
                flux[x] = (link(x, a) + link(step(x, a), b) - link(step(x, b), a) - link(x, b)) % 5
            for r in range(4):
                S = [[0, 0] for _ in range(L)]
                direct: dict[int, tuple[int, int]] = {}
                c = 1 if core.CONTAINS[i][r] else 0
                for x, f in flux.items():
                    g = core.SCORE_UV[f]
                    S[x[r]][0] += g[0]
                    S[x[r]][1] += g[1]
                    e = (-(2 * x[r] + c)) % (2 * L)
                    u, v = direct.get(e, (0, 0))
                    direct[e] = (u + g[0], v + g[1])
                mine[(name, r)] = [tuple(cell) for cell in S]
                # |F|^2 = F(x) F(1/x) modulo x^(2L) - 1, then modulo Phi_2L.
                power: dict[int, tuple[Fraction, Fraction]] = {}
                for e1, g1 in direct.items():
                    for e2, g2 in direct.items():
                        e = (e1 - e2) % (2 * L)
                        pu, pv = core.zphi_mul(g1, g2)
                        u, v = power.get(e, (Fraction(0), Fraction(0)))
                        power[e] = (u + pu, v + pv)
                lhs = reduce_mod(power, phi_n)
                rhs: dict[int, tuple[Fraction, Fraction]] = {}
                for k, half_mult in weights_exact:
                    ru, rv = R[(name, r)][k]
                    for e in ((2 * k) % (2 * L), (-2 * k) % (2 * L)):
                        u, v = rhs.get(e, (Fraction(0), Fraction(0)))
                        rhs[e] = (u + half_mult * ru, v + half_mult * rv)
                require(lhs == reduce_mod(rhs, phi_n), f"Fourier reduction L={L} I={name} r={r}")
        require(mine == engine_S, f"fixture slice sums differ from the engine at L={L}")
        _, Q = core.reduce_sample(engine_S, L)
        out.append(f"FIXTURE L={L} links_sha256={sha256(links.encode('ascii'))} slice_sums=EQUAL "
                   f"fourier_identity=EXACT Q_sha256={sha256(repr(Q).encode('ascii'))}")


# ---------------------------------------------------------------------------
# 5. Deterministic readout
# ---------------------------------------------------------------------------


def readout(out: list[str]) -> None:
    for L in core.FORMAL.sizes + FIXTURE_SIZES:
        for k in range(L // 2 + 1):
            value = core.cos_turn(Fraction(k, L))
            require(abs(value - math.cos(2.0 * math.pi * k / L)) <= 1.0e-15, f"cosine L={L} k={k}")
    out.append("COSINE_TABLE PASS sizes=" + ",".join(str(L) for L in core.FORMAL.sizes + FIXTURE_SIZES)
               + " tolerance=1e-15 source=sqrt_closed_forms")
    previous = math.inf
    for nu in range(1, 4097):
        value = core.t995(nu)
        if nu >= 4:
            require(value < previous, "t quantile not decreasing")
        previous = value
    for nu, expected in T995_TABLE:
        require(abs(Fraction(core.t995(nu)) - expected) <= Fraction(1, 10**5), f"t quantile nu={nu}")
    out.append(f"T995 PASS t(63)={core.fmt(core.t995(63))} t(255)={core.fmt(core.t995(255))} "
               f"z={core.fmt(core.Z995)}")
    for counts in ((1, 2, 3, 4, 5), (7, 0, 0, 0, 9), (0, 5, 6, 0, 0)):
        L = 2
        scale = Fraction(1, 6 * L**4)
        n14, n23 = counts[1] + counts[4], counts[2] + counts[3]
        # exact (1 + mean X^2)/2 with X^2 = 5 -+ 2 sqrt5, kept as p + q sqrt5
        p = (1 + scale * 5 * (n14 + n23)) / 2
        q = scale * 2 * (n23 - n14) / 2
        exact = float(p) + float(q) * math.sqrt(5.0)
        total = sum(counts)
        padded = [counts[0] + 6 * L**4 - total] + list(counts[1:])
        require(abs(core.a_value(padded, L) - exact) <= 1.0e-15, "a_L readout")
    out.append("A_READOUT PASS a=(1+E X^2)/2 X^2=kappa^2 G^2")


# ---------------------------------------------------------------------------
# 6. Lazy statistics are the pilot-2 statistics
# ---------------------------------------------------------------------------


def lcg_series(seed: int, length: int, rho: float, quantum: float = 0.0) -> list[float]:
    state = seed
    y = 0.0
    out = []
    for _ in range(length):
        state = (6364136223846793005 * state + 1442695040888963407) % (1 << 64)
        u = (state >> 11) / float(1 << 53)
        y = rho * y + (u - 0.5)
        out.append(round(y / quantum) * quantum if quantum else y)
    return out


def statistics_identity(out: list[str]) -> None:
    singles = [lcg_series(11, 1024, 0.0), lcg_series(12, 1024, 0.9), lcg_series(13, 512, -0.3),
               lcg_series(14, 512, 0.6, 0.25), [0.5] * 64]
    for data in singles:
        require(core.geyer_tau_int(data) == P.geyer_tau_int(data), "lazy Geyer differs from pilot-2")
        require(core.series_stats(data) == P.series_stats(data), "lazy series_stats differs")
        require(core.half_drift_z(data) == P.half_drift_z(data), "lazy half drift differs")
    groups = [[lcg_series(20 + i, 256, 0.7) for i in range(4)],
              [lcg_series(30 + i, 256, 0.2, 0.5) for i in range(4)]]
    for group in groups:
        require(core.multi_chain_ess(group) == P.multi_chain_ess(group), "lazy pooled ESS differs")
        require(core.bulk_tail_ess(group) == P.bulk_tail_ess(group), "lazy bulk/tail ESS differs")
    out.append(f"STATISTICS_IDENTITY PASS series={len(singles)} groups={len(groups)} comparison=bitwise")


# ---------------------------------------------------------------------------
# 7. Seeds and grammar
# ---------------------------------------------------------------------------


def seeds_and_grammar(out: list[str]) -> None:
    cfg = core.FORMAL
    seen = set()
    for name, L, start, replica in cfg.chains():
        seed = cfg.seed(L, start, replica)
        require(seed not in seen and seed != 0, "seed collision")
        seen.add(seed)
        out.append(f"SEED chain={name} seed=0x{seed:016x} spacing={cfg.spacing_for(L)} "
                   f"preimage={cfg.seed_prefix}|L={L}|start={start}|replica={replica}")
    grammar = "\n".join(core.TERMINALS) + "\n"
    out.append(f"TERMINAL_GRAMMAR {','.join(core.TERMINALS)} sha256={sha256(grammar.encode('ascii'))}")
    out.append(f"SCHEDULE sizes={','.join(str(L) for L in cfg.sizes)} fit_sizes="
               f"{','.join(str(L) for L in cfg.fit_sizes)} endpoints={','.join(str(e) for e in cfg.endpoints)} "
               f"window={cfg.window} samples={cfg.samples} b_min={cfg.b_min} min_blocks={cfg.min_blocks}")


# ---------------------------------------------------------------------------
# 8. Replay
# ---------------------------------------------------------------------------


def replay(out: list[str]) -> None:
    if not (HERE / "CHAINS.tsv").exists():
        require(not (HERE / "records").exists(), "records without CHAINS.tsv")
        out.append("REPLAY ABSENT mode=PRE_EXECUTION")
        return
    lines, terminal = core.analyze(HERE, core.FORMAL)
    produced = ("\n".join(lines) + "\n").encode("ascii")
    require(produced == (HERE / "ANALYSIS.txt").read_bytes(), "ANALYSIS.txt differs from the replay")
    out.extend(lines)
    out.append(f"REPLAY PASS analysis_sha256={sha256(produced)} terminal={terminal}")


def main() -> int:
    out: list[str] = [f"VERIFY {core.PROBE_ID} V1"]
    try:
        custody(out)
        engine_tables(out)
        score_identities(out)
        fixtures(out)
        readout(out)
        statistics_identity(out)
        seeds_and_grammar(out)
        replay(out)
        out.append("VERIFY PASS")
        code = 0
    except (VerifyError, core.IntegrityError, OSError, ValueError, KeyError) as error:
        out.append(f"VERIFY FAIL {error}")
        code = 1
    sys.stdout.write("\n".join(out) + "\n")
    return code


if __name__ == "__main__":
    raise SystemExit(main())
