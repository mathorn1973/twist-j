from __future__ import annotations

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW = ROOT / ".github" / "workflows" / "policy.yml"


class WorkflowArchitectureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.text = WORKFLOW.read_text(encoding="utf-8")

    def test_exact_architecture_runners(self) -> None:
        self.assertEqual(self.text.count("architecture: x86_64"), 1)
        self.assertEqual(self.text.count("runner: ubuntu-latest"), 1)
        self.assertEqual(self.text.count("architecture: aarch64"), 1)
        self.assertEqual(self.text.count("runner: ubuntu-24.04-arm"), 1)
        self.assertIn("runs-on: ${{ matrix.runner }}", self.text)

    def test_timeouts_match_policy(self) -> None:
        architecture_at = self.text.index("\n  architecture:")
        check_at = self.text.index("\n  check:")
        publication_at = self.text.index("\n  publication:")
        architecture_block = self.text[architecture_at:check_at]
        check_block = self.text[check_at:publication_at]
        publication_block = self.text[publication_at:]
        self.assertIn("timeout-minutes: 60", architecture_block)
        self.assertIn("timeout-minutes: 5", check_block)
        self.assertIn("timeout-minutes: 60", publication_block)
        self.assertEqual(self.text.count("timeout-minutes: 60"), 2)
        self.assertEqual(self.text.count("timeout-minutes: 5"), 1)

    def test_aggregate_check_depends_on_architecture(self) -> None:
        block = (
            "  check:\n"
            "    if: always() && github.ref_type != 'tag' "
            "&& github.event_name != 'release' && github.event_name != 'workflow_dispatch'\n"
            "    needs: architecture\n"
            "    runs-on: ubuntu-latest"
        )
        self.assertIn(block, self.text)
        self.assertIn('echo "TWO-ARCHITECTURE CHECK PASS"', self.text)

    def test_aggregate_fails_rather_than_skips_on_architecture_failure(self) -> None:
        """A skipped required check can count as passing. The aggregate
        therefore runs always() and asserts the matrix result itself, so a
        failed architecture job fails the required context instead of
        vanishing from it."""
        self.assertIn("if: always() &&", self.text)
        self.assertIn("if: needs.architecture.result != 'success'", self.text)

    def test_publication_is_single_runner(self) -> None:
        block = (
            "  publication:\n"
            "    if: github.ref_type == 'tag' || github.event_name == 'release' || github.event_name == 'workflow_dispatch'\n"
            "    runs-on: ubuntu-latest"
        )
        self.assertIn(block, self.text)
        publication_at = self.text.index("\n  publication:")
        upload_token = "actions/upload-artifact@043fb46d1a93c77aae656e7c1c64a875d1fc6a0a"
        self.assertEqual(self.text.count(upload_token), 1)
        self.assertGreater(self.text.index(upload_token), publication_at)

    def test_both_architectures_run_reproduction_checks(self) -> None:
        architecture_at = self.text.index("\n  architecture:")
        aggregate_at = self.text.index("\n  check:")
        architecture_block = self.text[architecture_at:aggregate_at]
        self.assertIn('python tools/check_verifier.py --base "$BASE_SHA"', architecture_block)
        self.assertIn('python tools/check_reproduce.py --base "$BASE_SHA"', architecture_block)

    def test_publication_does_not_run_changed_path_checks(self) -> None:
        publication_at = self.text.index("\n  publication:")
        publication_block = self.text[publication_at:]
        self.assertNotIn("--base", publication_block)
        self.assertIn("python -u tools/check_verifier.py", publication_block)
        self.assertIn("python -u tools/check_reproduce.py", publication_block)
        self.assertIn("check_activation.py --full --post-activation", publication_block)

    def test_forbidden_trigger_absent(self) -> None:
        self.assertNotIn("pull_request_target:", self.text)


class V107RecoveryTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import textwrap
        text = WORKFLOW.read_text(encoding='utf-8')
        begin = text.index('          # BEGIN PINNED V107 RECOVERY RECEIPT\n')
        end_marker = '          # END PINNED V107 RECOVERY RECEIPT\n'
        end = text.index(end_marker, begin) + len(end_marker)
        cls.source = textwrap.dedent(text[begin:end])
        cls.namespace = {'__name__': 'receipt_unit_test'}
        exec(compile(cls.source, str(WORKFLOW), 'exec'), cls.namespace)
        cls.text = text

    def environment(self):
        return {'GITHUB_REPOSITORY': 'mathorn1973/twist-j',
                'GITHUB_EVENT_NAME': 'workflow_dispatch',
                'GITHUB_SHA': 'a' * 40, 'GITHUB_WORKFLOW_SHA': 'a' * 40,
                'GITHUB_WORKFLOW_REF': 'mathorn1973/twist-j/.github/workflows/policy.yml@refs/heads/reviewed-controller',
                'GITHUB_REF': 'refs/heads/reviewed-controller',
                'GITHUB_RUN_ID': '123', 'GITHUB_RUN_ATTEMPT': '2'}

    def test_dispatch_has_no_inputs_and_immutable_science_pins(self):
        self.assertIn('  workflow_dispatch:\n\npermissions:', self.text)
        self.assertNotIn('  inputs:', self.text)
        self.assertIn('test "$(git cat-file -t refs/tags/canon-v107)" = "tag"', self.text)
        for pin in ('03f010760d85c62795b74b3fa8fde79c2c36be7f',
                    '81c57853b7b5126fa2d8ec465b8ad903e2402c04',
                    'f5615ed4dcdfc672dc2e468399284a1dc03ce805'):
            self.assertIn(pin, self.text)
        self.assertNotIn('continue-on-error:', self.text)
        self.assertNotIn('contents: write', self.text)
        self.assertNotIn('actions: write', self.text)
        self.assertIn('permissions:\n  contents: read\n  actions: read', self.text)

    def test_replay_and_validation_precede_artifact(self):
        start = self.text.index('\n  publication:')
        block = self.text[start:]
        ordered = ('Pin manual recovery to immutable v107',
                   'python -u tools/check_verifier.py',
                   'python -u tools/check_reproduce.py',
                   'python -u tools/check_activation.py',
                   'Validate v107 recovery assets and bind provenance',
                   'Preserve tag readback manifest', 'Complete pinned v107 recovery')
        positions = [block.index(marker) for marker in ordered]
        self.assertEqual(positions, sorted(positions))
        self.assertNotIn('--base', block)
        self.assertIn("if: github.event_name != 'workflow_dispatch'", block)

    def test_receipt_binds_actual_controller_attempt_and_hashes(self):
        import hashlib
        result = self.namespace['provenance'](self.environment(), b'manifest', b'checksums', 'absent', None)
        self.assertEqual(result['controller_commit'], 'a' * 40)
        self.assertEqual(result['workflow_commit'], 'a' * 40)
        self.assertEqual((result['run_id'], result['run_attempt']), (123, 2))
        self.assertEqual(result['files']['activation-manifest.json'],
                         {'bytes': 8, 'sha256': hashlib.sha256(b'manifest').hexdigest()})
        self.assertEqual(result['release_state_at_readback'], 'absent')

    def test_receipt_rejects_wrong_context_and_mixed_release_state(self):
        for field, bad in (('GITHUB_REPOSITORY', 'other/repo'),
                           ('GITHUB_EVENT_NAME', 'push'), ('GITHUB_SHA', 'short'),
                           ('GITHUB_WORKFLOW_SHA', 'b' * 40), ('GITHUB_RUN_ID', '0'),
                           ('GITHUB_RUN_ATTEMPT', '01'), ('GITHUB_WORKFLOW_REF', 'other')):
            with self.subTest(field=field):
                env = self.environment()
                env[field] = bad
                with self.assertRaises(ValueError):
                    self.namespace['provenance'](env, b'', b'', 'absent', None)
        with self.assertRaises(ValueError):
            self.namespace['provenance'](self.environment(), b'', b'', 'published', None)

    def test_tag_controller_ref_is_rejected(self):
        environment = self.environment()
        environment['GITHUB_REF'] = 'refs/tags/recovery-controller'
        environment['GITHUB_WORKFLOW_REF'] = 'mathorn1973/twist-j/.github/workflows/policy.yml@refs/tags/recovery-controller'
        with self.assertRaises(ValueError):
            self.namespace['provenance'](environment, b'manifest', b'checksums', 'absent', None)
        self.assertIn('case "$GITHUB_REF" in refs/heads/?*)', self.text)

    def test_release_classification_distinguishes_draft_from_published(self):
        classify = self.namespace['classify_release']
        self.assertEqual(classify({'tag_name': 'canon-v107', 'id': 7, 'draft': True}), ('draft', 7))
        self.assertEqual(classify({'tag_name': 'canon-v107', 'id': 7, 'draft': False,
                                   'published_at': '2026-11-01T00:00:00Z'}), ('published', 7))
        for bad in (None, {}, {'tag_name': 'canon-v106', 'id': 7, 'draft': True},
                    {'tag_name': 'canon-v107', 'id': True, 'draft': True},
                    {'tag_name': 'canon-v107', 'id': 7, 'draft': False}):
            with self.subTest(payload=bad), self.assertRaises(ValueError):
                classify(bad)

    def test_only_http_404_means_absent(self):
        from urllib.error import HTTPError
        from unittest.mock import patch
        def fail(code):
            def opener(request, timeout):
                raise HTTPError(request.full_url, code, 'failure', {}, None)
            return opener
        with patch.dict('os.environ', {'GH_TOKEN': 'test-only'}):
            self.assertEqual(self.namespace['read_release'](fail(404)), ('absent', None, False))
            for code in (401, 403, 429, 500, 503):
                with self.subTest(code=code), self.assertRaises(HTTPError):
                    self.namespace['read_release'](fail(code))

    def successful_run(self):
        return {'id': 123, 'run_attempt': 2, 'head_sha': 'a' * 40,
                'event': 'workflow_dispatch', 'status': 'completed', 'conclusion': 'success',
                'repository': {'full_name': 'mathorn1973/twist-j'},
                'path': '.github/workflows/policy.yml', 'head_branch': 'reviewed-controller'}

    def successful_jobs(self):
        return [{'name': 'publication', 'run_id': 123, 'status': 'completed', 'conclusion': 'success',
                 'steps': [{'name': name, 'status': 'completed', 'conclusion': 'success'}
                           for name in self.namespace['REQUIRED_RECOVERY_STEPS']]}]

    def test_archived_receipt_requires_matching_digests_and_successful_attempt(self):
        import copy
        receipt = self.namespace['provenance'](self.environment(), b'manifest', b'checksums', 'absent', None)
        run = self.successful_run()
        jobs = self.successful_jobs()
        validate = self.namespace['validate_published_provenance']
        run_reader = lambda rid, attempt: run
        jobs_reader = lambda rid, attempt: jobs
        validate(receipt, b'manifest', b'checksums', 'a' * 40, run_reader, jobs_reader)
        for changed_manifest, controller in ((b'changed', 'a' * 40), (b'manifest', 'b' * 40)):
            with self.assertRaises(ValueError):
                validate(receipt, changed_manifest, b'checksums', controller, run_reader, jobs_reader)
        for field, bad in (('run_attempt', 1), ('head_sha', 'b' * 40), ('event', 'push'),
                           ('conclusion', 'cancelled'), ('status', 'in_progress'),
                           ('path', '.github/workflows/other.yml'), ('head_branch', 'other')):
            wrong = copy.deepcopy(run)
            wrong[field] = bad
            with self.subTest(field=field), self.assertRaises(ValueError):
                validate(receipt, b'manifest', b'checksums', 'a' * 40,
                         lambda rid, attempt: wrong, jobs_reader)

    def test_published_release_cannot_omit_recovery_receipt(self):
        import io
        import json
        from unittest.mock import patch
        payload = {'tag_name': 'canon-v107', 'id': 7, 'draft': False,
                   'published_at': '2026-11-01T00:00:00Z',
                   'assets': [{'name': 'activation-manifest.json'}, {'name': 'SHA256SUMS'}]}
        def opener(request, timeout):
            return io.BytesIO(json.dumps(payload).encode())
        with patch.dict('os.environ', {'GH_TOKEN': 'test-only'}), self.assertRaises(ValueError):
            self.namespace['read_release'](opener)

    def test_three_asset_integration_fails_closed(self):
        import copy
        import json
        import tempfile
        receipt = self.namespace['provenance'](self.environment(), b'manifest', b'checksums', 'absent', None)
        files = {'activation-manifest.json': b'manifest', 'SHA256SUMS': b'checksums',
                 'recovery-provenance.json': (json.dumps(receipt) + '\n').encode()}
        for fault in (None, 'missing-receipt', 'substituted-manifest', 'substituted-receipt',
                      'cancelled-run', 'skipped-step', 'missing-artifact', 'expired-artifact',
                      'wrong-artifact-run', 'extra-artifact-file', 'missing-artifact-file',
                      'download-failure'):
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as temp:
                destination = Path(temp) / 'published'
                run = self.successful_run()
                jobs = self.successful_jobs()
                artifact = {'name': 'canon-v107-recovery-123-2', 'expired': False,
                            'workflow_run': {'id': 123, 'head_sha': 'a' * 40}}
                if fault == 'cancelled-run':
                    run['conclusion'] = 'cancelled'
                if fault == 'skipped-step':
                    jobs[0]['steps'][9]['conclusion'] = 'skipped'
                if fault == 'expired-artifact':
                    artifact['expired'] = True
                if fault == 'wrong-artifact-run':
                    artifact['workflow_run']['id'] = 999
                calls = []
                def runner(command, check):
                    import subprocess
                    self.assertTrue(check)
                    calls.append(command)
                    if fault == 'download-failure':
                        raise subprocess.CalledProcessError(1, command)
                    if command[0] != 'gh':
                        self.assertEqual(command[1], 'tools/check_release_manifest.py')
                        return
                    target = Path(command[command.index('--dir') + 1])
                    is_original = command[1] == 'run'
                    if is_original:
                        self.assertEqual(command[3], '123')
                        self.assertEqual(command[command.index('--name') + 1], 'canon-v107-recovery-123-2')
                    else:
                        self.assertIn('recovery-provenance.json', command)
                    for filename, data in files.items():
                        if (fault == 'missing-receipt' and not is_original and filename == 'recovery-provenance.json'):
                            continue
                        if (fault == 'missing-artifact-file' and is_original and filename == 'SHA256SUMS'):
                            continue
                        if is_original and ((fault == 'substituted-manifest' and filename == 'activation-manifest.json') or
                                            (fault == 'substituted-receipt' and filename == 'recovery-provenance.json')):
                            data += b' '
                        (target / filename).write_bytes(data)
                    if fault == 'extra-artifact-file' and is_original:
                        (target / 'extra.txt').write_text('extra')
                def exercise():
                    self.namespace['verify_published_assets'](
                        destination, b'checksums', runner, include_receipt=True,
                        run_reader=lambda rid, attempt: run,
                        jobs_reader=lambda rid, attempt: jobs,
                        artifact_reader=lambda rid: [] if fault == 'missing-artifact' else [artifact],
                        environment=self.environment())
                if fault is None:
                    exercise()
                    self.assertEqual(len(calls), 3)
                else:
                    with self.assertRaises((ValueError, __import__('subprocess').CalledProcessError)):
                        exercise()



if __name__ == "__main__":
    unittest.main()
