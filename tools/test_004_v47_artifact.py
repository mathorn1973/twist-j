#!/usr/bin/env python3
"""Temporary prep-only byte transport for the reviewed v47 content tree.

Uses the GitHub Actions Results artifact runtime, not repository write
permission. It uploads one ZIP containing exactly the 17 intended content
paths after the v47 builder has materialized and checked them in the runner.
Removed before any release branch is formed.
"""

from __future__ import annotations

import base64
import hashlib
import io
import json
import os
from pathlib import Path
import urllib.parse
import urllib.request
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "canon/CANON.md",
    "canon/CHANGELOG.md",
    "canon/CORE.md",
    "canon/DEPENDENCIES.tsv",
    "canon/EVIDENCE.tsv",
    "canon/FRONTIER.md",
    "canon/FRONTIER_PROGRAMS.tsv",
    "canon/GATES.tsv",
    "canon/HISTORY.tsv",
    "canon/NORMATIVE.tsv",
    "canon/REGISTRY.tsv",
    "canon/SHA256SUMS",
    "canon/STATUS_COUNTS.tsv",
    "reproduce/status-separation/EXPECTED.txt",
    "reproduce/status-separation/README.md",
    "reproduce/status-separation/verify.py",
    "tools/test_architecture_map_report.py",
)

EXPECTED_GENERATED = {
    "canon/CANON.md": (225589, "5e4c454e53381e13df2bc2e894bd6e7328af9329c4b13df03106c902c7caf400"),
    "canon/CHANGELOG.md": (80806, "d06388a54bb69838357d0389f67edbc75cbfe051c810a7e29aea40368b0a8926"),
    "canon/CORE.md": (11304, "4092f370640f5f86b3f579b5cb3853e2b13cdfc5efa0eb074206d4b5b46883ae"),
    "canon/EVIDENCE.tsv": (45261, "2c75ef8dbbe374ebf4de9db01e3dd8007390d0f6d5d9e98636e9d26193778113"),
    "canon/FRONTIER.md": (16717, "c4dced43e3d96e070d7ca3ca84849a61655bad343ede069bbabcb68ca4baaa68"),
    "canon/HISTORY.tsv": (305737, "4c7803e0b3d245ff90defd3b548f83cbda5182c94b83738e7f35c5acc741218a"),
    "canon/SHA256SUMS": (415, "251a9285212b495e99e4a8d698fefc51c9c0a847096b3d3b31d4d2ff0f27064c"),
    "canon/STATUS_COUNTS.tsv": (243, "996e13cf0eb1df3570d1298e11fc2311ceed21de24c72d63f34299789740496a"),
    "reproduce/status-separation/EXPECTED.txt": (3126, "239ed874992be685910a13de2fd0906a303cdfec67ed0d994306c3c10b3ed5f3"),
    "reproduce/status-separation/README.md": (6277, "c215e5ac06a49547e3e78b936556392a47ecf5cd6a37d9bf33bb9b0de4e65fdd"),
    "reproduce/status-separation/verify.py": (102594, "8c25008a1e5405d987242fd28dc913beeae38fdb600e5d701ae1b17dc19a4454"),
}


def _backend_ids(token: str) -> tuple[str, str]:
    parts = token.split(".")
    if len(parts) < 2:
        raise AssertionError("invalid Actions runtime JWT")
    payload = parts[1] + "=" * (-len(parts[1]) % 4)
    decoded = json.loads(base64.urlsafe_b64decode(payload.encode("ascii")))
    for scope in decoded.get("scp", "").split():
        fields = scope.split(":")
        if len(fields) == 3 and fields[0] == "Actions.Results":
            return fields[1], fields[2]
    raise AssertionError("Actions.Results scope absent")


def _json_post(url: str, token: str, body: dict) -> dict:
    data = json.dumps(body, separators=(",", ":")).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "twist-j-v47-prep-artifact",
        },
    )
    with urllib.request.urlopen(request, timeout=60) as response:
        return json.loads(response.read().decode("utf-8"))


def _put_blob(url: str, data: bytes) -> None:
    request = urllib.request.Request(
        url,
        data=data,
        method="PUT",
        headers={
            "Content-Type": "application/zip",
            "x-ms-blob-type": "BlockBlob",
        },
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        if response.status not in {200, 201, 202}:
            raise AssertionError(f"blob upload status {response.status}")


def _zip_bytes() -> bytes:
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for relative in FILES:
            archive.write(ROOT / relative, arcname=relative)
    return out.getvalue()


class V47ArtifactTransport(unittest.TestCase):
    def test_upload_exact_content_artifact(self) -> None:
        token = os.environ.get("ACTIONS_RUNTIME_TOKEN")
        results_url = os.environ.get("ACTIONS_RESULTS_URL")
        if not token or not results_url:
            self.skipTest("not running inside GitHub Actions artifact runtime")

        for relative, (size, digest) in EXPECTED_GENERATED.items():
            data = (ROOT / relative).read_bytes()
            self.assertEqual(len(data), size, relative)
            self.assertEqual(hashlib.sha256(data).hexdigest(), digest, relative)

        run_backend_id, job_backend_id = _backend_ids(token)
        origin = f"{urllib.parse.urlsplit(results_url).scheme}://{urllib.parse.urlsplit(results_url).netloc}"
        service = f"{origin}/twirp/github.actions.results.api.v1.ArtifactService"
        arch = os.environ.get("RUNNER_ARCH", "UNKNOWN").lower()
        name = f"v47-reviewed-content-{arch}"

        create = _json_post(
            f"{service}/CreateArtifact",
            token,
            {
                "workflow_run_backend_id": run_backend_id,
                "workflow_job_run_backend_id": job_backend_id,
                "name": name,
                "mime_type": {"value": "application/zip"},
                "version": 7,
            },
        )
        self.assertTrue(create.get("ok"), create)
        signed_url = create.get("signed_upload_url") or create.get("signedUploadUrl")
        self.assertTrue(signed_url)

        payload = _zip_bytes()
        digest = hashlib.sha256(payload).hexdigest()
        _put_blob(signed_url, payload)

        finalize = _json_post(
            f"{service}/FinalizeArtifact",
            token,
            {
                "workflow_run_backend_id": run_backend_id,
                "workflow_job_run_backend_id": job_backend_id,
                "name": name,
                "size": str(len(payload)),
                "hash": {"value": f"sha256:{digest}"},
            },
        )
        self.assertTrue(finalize.get("ok"), finalize)
        artifact_id = finalize.get("artifact_id") or finalize.get("artifactId")
        self.assertTrue(artifact_id)
        print(f"V47_ARTIFACT_OK name={name} id={artifact_id} bytes={len(payload)} sha256={digest}")


if __name__ == "__main__":
    unittest.main()
