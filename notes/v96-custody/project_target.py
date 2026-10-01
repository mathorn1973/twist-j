"""Explicit allowlist projection; conversion and raw evidence remain in custody."""

import argparse
import copy
import json
from schema import VERSION, ROLES, canonical, digest, load, packet, packet_flags, require


def project(reduction, opaque_id):
    """Reduce only a typed, hash-bound reduction from independent acquisition.

    This function does not authenticate the acquisition provider. The complete
    auditor separately verifies the immutable raw bytes and provider receipt.
    No MEASURED receipt can be manufactured by this software package.
    """
    require(reduction.get("kind") == "CALIBRATED_OBSERVATIONS", "model trace is not raw acquisition")
    require(reduction.get("origin") in ("MEASURED", "SYNTHETIC"), "observation origin")
    for name in ("raw_sha256", "calibration_sha256", "reducer_sha256", "settings_sha256"):
        digest(reduction[name])
    target = reduction["target"]
    frames = []
    for frame in target["frames"]:
        readings = []
        for observed in frame["readings"]:
            item = {name: copy.deepcopy(observed[name]) for name in (
                "t_s", "coordinates", "p", "optical", "angle_deg", "temperature_C", "flags")}
            item["banks"] = {role: {name: observed["banks"][role][name]
                                   for name in ("energy_J", "U_J", "voltage_V")} for role in ROLES}
            readings.append(item)
        frames.append({"step": frame["step"], "layer": frame["layer"], "readings": readings})
    result = {
        "schema": VERSION, "id": opaque_id, "frames": frames,
        "ports": {role: [{name: copy.deepcopy(sample[name]) for name in ("t0_s", "t1_s", "V", "I", "flags")}
                         for sample in target["ports"][role]] for role in ROLES},
        "uncertainty": {name: copy.deepcopy(target["uncertainty"][name]) for name in (
            "time_s", "first_work_J", "whole_abs_J", "slot_abs_J")},
        "flags": copy.deepcopy(target["flags"]),
    }
    if reduction["origin"] == "SYNTHETIC" or "SYNTHETIC" in packet_flags(result):
        result["flags"] = sorted(set(result["flags"]) | {"SYNTHETIC"})
    return packet(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("reduction")
    parser.add_argument("opaque_id")
    args = parser.parse_args()
    print(canonical(project(load(args.reduction), args.opaque_id)).decode("ascii"))


if __name__ == "__main__":
    main()
