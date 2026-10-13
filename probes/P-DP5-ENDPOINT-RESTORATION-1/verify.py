#!/usr/bin/env python3
"""Exact post-pin controls for independent endpoint restoration; Apache-2.0."""
import importlib.util
import json
from pathlib import Path
import sys


def main():
    sys.dont_write_bytecode = True
    path = Path(__file__).resolve().with_name('restore.py')
    spec = importlib.util.spec_from_file_location('independent_endpoint_restoration', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    receipts = module.source_receipts()
    module.source_binding()
    result = module.controls()
    print(json.dumps({'status': 'PASS', 'scope': 'EXACT_MATHEMATICAL_CONTROLS_ONLY',
                      'action_layer': 'L1', 'controls': result,
                      'precision_bits': module.P, 'scalar_degree': module.N,
                      'production_restoration_executed': False,
                      'propagation_executed': False,
                      'restore_sha256': receipts['restore.py']['sha256'],
                      'binding_sha256': module.BINDING_SHA256}, sort_keys=True))


if __name__ == '__main__':
    main()
