#!/usr/bin/env python3
"""Accepted verifier for C-RH-RAY-FINITE-WINDOW-CERTIFICATE-3-N.

The result is exposed. The exact matrix engine is carried byte-identically and
hash-pinned. This fresh wrapper fixes only the predecessor's import integrity
defect by registering the module in sys.modules before executing it. It imports
no breaker code, accepts no arguments, and proxies the engine's deterministic
exact stdout and exit code.
"""

from __future__ import annotations

import hashlib
import importlib.util
import sys
from pathlib import Path

assert len(sys.argv) == 1

ROOT = Path(__file__).resolve().parent
ENGINE = ROOT / "engine.py"
EXPECTED_ENGINE_SHA256 = (
    "e386abd2b362f3cfc0bc3181f3cc7fdcecfe64e21988c7520f29f540ea39d29e"
)

payload = ENGINE.read_bytes()
assert hashlib.sha256(payload).hexdigest() == EXPECTED_ENGINE_SHA256

spec = importlib.util.spec_from_file_location("ray_v57_clean_retry_engine", ENGINE)
assert spec is not None and spec.loader is not None
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)
raise SystemExit(module.main())
