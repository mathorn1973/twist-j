"""Frozen pilot-sentinel gate for the local ordered Z5 protocol.

Supply the inherited module from analyze_ordered.load_diagnostics.
Chains have the fixed order cold 1, cold 2, hot 1, hot 2 and contain
decoded SAMPLE lines with canonical consecutive indices. In thermal
mode, all supplied records are checked and only the last 512 are used.
The driver owns the allowed thermal endpoints and which endpoint passes
first. Measurement mode uses all 4096 records. Schedule, sampler
counter and saved-state custody checks remain the driver's responsibility.
"""

import math
import statistics


def _ims_pairs(length, correlation):
    """Evaluate only the pairs used by the frozen initial monotone sum."""
    pairs = []
    for lag in range(0, length - 1, 2):
        pair = correlation(lag) + correlation(lag + 1)
        if pair <= 0.0:
            break
        if pairs and pair > pairs[-1]:
            pair = pairs[-1]
        pairs.append(pair)
    return math.fsum(pairs)


def _series_stats(data, diagnostics):
    centre = diagnostics.arithmetic_mean(data)
    variance = statistics.variance(data)
    zero_lag = diagnostics.autocovariance(data, 0, centre)
    if zero_lag <= 0.0:
        tau = 0.5
    else:
        def correlation(lag):
            if lag == 0:
                return 1.0
            return diagnostics.autocovariance(data, lag, centre) / zero_lag

        tau = max(0.5, -0.5 + _ims_pairs(len(data), correlation))
    ess = min(float(len(data)), len(data) / (2.0 * tau))
    mcse = math.sqrt(max(0.0, variance) * 2.0 * tau / len(data))
    return diagnostics.SeriesStats(centre, mcse, tau, ess, variance)


def _half_drift_z(data, diagnostics):
    midpoint = len(data) // 2
    left = _series_stats(data[:midpoint], diagnostics)
    right = _series_stats(data[midpoint:], diagnostics)
    return diagnostics.z_difference(left.mean, left.mcse, right.mean, right.mcse)


def _multi_chain_ess(chains, diagnostics):
    length = len(chains[0])
    means = [diagnostics.arithmetic_mean(chain) for chain in chains]
    within = diagnostics.arithmetic_mean(statistics.variance(chain) for chain in chains)
    between = length * statistics.variance(means)
    var_plus = ((length - 1.0) / length) * within + between / length
    total = len(chains) * length
    if var_plus <= 0.0:
        return float(total) if between == 0.0 else 0.0

    def correlation(lag):
        if lag == 0:
            return 1.0
        mean_gamma = diagnostics.arithmetic_mean(
            diagnostics.autocovariance(chain, lag, centre)
            for chain, centre in zip(chains, means)
        )
        return min(1.0, 1.0 - (within - mean_gamma) / var_plus)

    tau = max(1.0, -1.0 + 2.0 * _ims_pairs(length, correlation))
    return min(float(total), total / tau)


def _bulk_tail_ess(chains, diagnostics):
    split = diagnostics.split_chains(chains)
    bulk = _multi_chain_ess(diagnostics.rank_normalize(split), diagnostics)
    flat = [value for chain in split for value in chain]
    low = diagnostics.empirical_quantile(flat, 0.05)
    high = diagnostics.empirical_quantile(flat, 0.95)
    low_indicator = [[1.0 if value <= low else 0.0 for value in chain] for chain in split]
    high_indicator = [[1.0 if value >= high else 0.0 for value in chain] for chain in split]
    tail = min(_multi_chain_ess(low_indicator, diagnostics),
               _multi_chain_ess(high_indicator, diagnostics))
    return bulk, tail


def _read_rows(chains, diagnostics, count, measurement):
    if len(chains) != 4:
        raise ValueError("expected four chains in cold/cold/hot/hot order")
    supplied = len(chains[0])
    if any(len(chain) != supplied for chain in chains):
        raise ValueError("chain SAMPLE counts disagree")
    if supplied < count or (measurement and supplied != count):
        raise ValueError(f"expected {'exactly' if measurement else 'at least'} {count} rows per chain")

    side = None
    first_index = None
    selected = []
    for chain_index, lines in enumerate(chains, start=1):
        tail = []
        for offset, line in enumerate(lines):
            if not isinstance(line, str):
                raise ValueError("SAMPLE rows must be decoded strings")
            if line.endswith("\n"):
                line = line[:-1]
            if not line.startswith("SAMPLE ") or any(not 32 <= ord(c) <= 126 for c in line):
                raise ValueError(f"malformed SAMPLE row in chain {chain_index}")
            fields = diagnostics.parse_fields(line)
            if set(fields) != diagnostics.SAMPLE_FIELDS:
                raise ValueError(f"SAMPLE field inventory in chain {chain_index}")
            index = diagnostics.parse_canonical_uint(fields["index"], "index")
            if first_index is None:
                first_index = index
            if index != first_index + offset:
                raise ValueError(f"nonconsecutive or mismatched SAMPLE index in chain {chain_index}")
            for name in ("state_hash", "cache_hash"):
                if not diagnostics.is_lower_hex(fields[name], 16):
                    raise ValueError(f"invalid {name} in chain {chain_index}")
            values = {
                metric: diagnostics.parse_finite(fields[metric], metric)
                for metric in diagnostics.MIXING_METRICS
            }
            flux_counts = [diagnostics.parse_canonical_uint(fields[name], name)
                           for name in diagnostics.FLUX_COUNT_FIELDS]
            total = sum(flux_counts)
            if side is None:
                side = math.isqrt(math.isqrt(total // 6))
            if side < 2 or side % 2 or total != 6 * side**4:
                raise ValueError(f"inconsistent even-volume flux counts in chain {chain_index}")
            tolerance = diagnostics.FRACTION_COUNT_TOLERANCE
            fractions = [values[f"flux_fraction_{j}"] for j in range(5)]
            if (any(abs(fraction - entries / total) > tolerance
                    for fraction, entries in zip(fractions, flux_counts))
                    or abs(math.fsum(fractions) - 1.0) > 5.0 * tolerance):
                raise ValueError(f"flux fractions disagree with counts in chain {chain_index}")
            if offset >= supplied - count:
                tail.append((fields["state_hash"], values))
        selected.append(tail)
    return side, first_index + supplied - count, selected


def _json_number(value):
    return value if math.isfinite(value) else None


def assess(chains, diagnostics, *, measurement=False):
    """Apply all inherited mixing thresholds and return a JSON-safe record."""
    count = 4096 if measurement else 512
    ess_min, rhat_max, bulk_min, tail_min, z_max = (
        (128, 1.03, 800, 400, 3) if measurement else (64, 1.05, 400, 200, 4)
    )
    try:
        side, first_index, rows = _read_rows(chains, diagnostics, count, measurement)
        failures = []
        unique_fractions = []
        for chain_index, chain in enumerate(rows, start=1):
            unique = len({hash_value for hash_value, _ in chain})
            unique_fractions.append(unique / count)
            if 100 * unique < 99 * count:
                failures.append(f"low_unique_state_c{chain_index}")

        metrics = {}
        for metric in diagnostics.MIXING_METRICS:
            series = [[values[metric] for _, values in chain] for chain in rows]
            stats = [_series_stats(data, diagnostics) for data in series]
            drifts = [_half_drift_z(data, diagnostics) for data in series]
            rank, folded = diagnostics.rank_folded_rhat(series)
            bulk, tail = _bulk_tail_ess(series, diagnostics)
            cold_mean, cold_se = diagnostics.conservative_group_mean_se(stats[:2])
            hot_mean, hot_se = diagnostics.conservative_group_mean_se(stats[2:])
            difference = diagnostics.z_difference(cold_mean, cold_se, hot_mean, hot_se)
            per_chain = []
            for chain_index, (summary, drift) in enumerate(zip(stats, drifts), start=1):
                if not math.isfinite(summary.variance) or summary.variance <= 0.0:
                    failures.append(f"nonpositive_or_nonfinite_variance_c{chain_index}_{metric}")
                if not math.isfinite(summary.ess) or summary.ess < ess_min:
                    failures.append(f"low_ess_c{chain_index}_{metric}")
                if not math.isfinite(drift) or drift > z_max:
                    failures.append(f"half_drift_c{chain_index}_{metric}")
                per_chain.append({
                    "mean": _json_number(summary.mean), "variance": _json_number(summary.variance),
                    "mcse": _json_number(summary.mcse), "tau_int": _json_number(summary.tau_int),
                    "ess": _json_number(summary.ess), "half_drift_z": _json_number(drift),
                })
            pooled = (
                ("rank_rhat", rank, rank <= rhat_max),
                ("folded_rhat", folded, folded <= rhat_max),
                ("low_bulk_ess", bulk, bulk >= bulk_min),
                ("low_tail_ess", tail, tail >= tail_min),
                ("hot_cold", difference, difference <= z_max),
            )
            for label, value, passes in pooled:
                if not math.isfinite(value) or not passes:
                    failures.append(f"{label}_{metric}")
            metrics[metric] = {
                "chains": per_chain, "rank_rhat": _json_number(rank),
                "folded_rhat": _json_number(folded), "bulk_ess": _json_number(bulk),
                "tail_ess": _json_number(tail), "cold_mean": _json_number(cold_mean),
                "hot_mean": _json_number(hot_mean), "hot_cold_z": _json_number(difference),
            }
    except (diagnostics.IntegrityError, ArithmeticError) as error:
        raise ValueError(f"sentinel integrity: {error}") from error

    return {
        "status": "STOP_MIXING" if failures else "PASS",
        "failures": failures,
        "L": side,
        "measurement": measurement,
        "window": {"first_index": first_index, "count": count},
        "unique_state_fractions": unique_fractions,
        "metrics": metrics,
    }
