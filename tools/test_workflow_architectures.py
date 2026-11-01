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


class V107PostpublicationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import textwrap
        text=WORKFLOW.read_text(encoding='utf-8')
        begin=text.index('          # BEGIN PINNED V107 POSTPUBLICATION READBACK\n')
        marker='          # END PINNED V107 POSTPUBLICATION READBACK\n'
        end=text.index(marker,begin)+len(marker)
        cls.namespace={'__name__':'postpublication_unit_test'}
        exec(compile(textwrap.dedent(text[begin:end]),str(WORKFLOW),'exec'),cls.namespace)
        cls.text=text

    def environment(self):
        return {'GITHUB_REPOSITORY':'mathorn1973/twist-j','GITHUB_EVENT_NAME':'workflow_dispatch',
                'GITHUB_REF':'refs/heads/reviewed-controller','GITHUB_SHA':'a'*40,
                'GITHUB_WORKFLOW_SHA':'a'*40,
                'GITHUB_WORKFLOW_REF':'mathorn1973/twist-j/.github/workflows/policy.yml@refs/heads/reviewed-controller',
                'GITHUB_RUN_ID':'999','GITHUB_RUN_ATTEMPT':'1'}

    def fixture(self):
        ns=self.namespace
        release={'id':430574383,'tag_name':'canon-v107','target_commitish':ns['ACTIVATION'],
                 'draft':False,'immutable':True,'prerelease':False,'published_at':'2026-11-01T12:38:30Z',
                 'assets':[{'name':'activation-manifest.json','id':698301343,'size':ns['MANIFEST_BYTES'],
                            'digest':'sha256:'+ns['MANIFEST_SHA256'],'state':'uploaded'},
                           {'name':'SHA256SUMS','id':698301342,'size':ns['CHECKSUM_BYTES'],
                            'digest':'sha256:'+ns['CHECKSUM_SHA256'],'state':'uploaded'}]}
        run={'id':41301206166,'run_attempt':2,'head_sha':ns['ACTIVATION'],'head_branch':'canon-v107',
             'event':'push','status':'completed','conclusion':'success','path':'.github/workflows/policy.yml',
             'repository':{'full_name':'mathorn1973/twist-j'}}
        job={'id':124841413548,'run_id':41301206166,'name':'publication','status':'completed','conclusion':'success',
             'steps':[{'name':name,'status':'completed','conclusion':'success'} for name in ns['REQUIRED_TAG_STEPS']]}
        artifact={'id':13084185131,'name':'canon-v107-activation-manifest','size_in_bytes':ns['ZIP_BYTES'],
                  'digest':'sha256:'+ns['ZIP_SHA256'],'expired':False,
                  'workflow_run':{'id':41301206166,'head_sha':ns['ACTIVATION'],'head_branch':'canon-v107'}}
        return release,run,job,artifact

    def test_fixed_historical_bindings(self):
        ns=self.namespace
        self.assertEqual(ns['TAG_RUN_ID'],41301206166)
        self.assertEqual(ns['TAG_RUN_ATTEMPT'],2)
        self.assertEqual(ns['TAG_JOB_ID'],124841413548)
        self.assertEqual(ns['ARTIFACT_ID'],13084185131)
        self.assertEqual(ns['ZIP_SHA256'],'9d1392f72ca4bab4edf014408e12b3b19f7da14e047cd46ed0e2de5482b46536')
        self.assertEqual(ns['MANIFEST_SHA256'],'9ab61f8638f87d0f5b3d7ca13ebca2e2584b7af33be4747205abe816eee4ef33')
        self.assertEqual(ns['CHECKSUM_SHA256'],'21e8c6fe8eac20e5645625c3531960ada37914b7f87674becabc4edb05cb240b')

    def test_manual_route_neither_creates_nor_uploads_manifest(self):
        self.assertIn('  workflow_dispatch:\n\npermissions:',self.text)
        self.assertIn('permissions:\n  contents: read\n  actions: read',self.text)
        self.assertNotIn('  inputs:',self.text)
        self.assertNotIn('continue-on-error:',self.text)
        self.assertEqual(self.text.count('--manifest-out'),1)
        self.assertIn("if: github.ref_type == 'tag' && github.event_name != 'workflow_dispatch'",self.text)
        self.assertIn("if: github.event_name != 'workflow_dispatch'",self.text)
        start=self.text.index('      - name: Validate static v107 activation after complete replay')
        end=self.text.index('      - name: Run activation readback on immutable publication events',start)
        self.assertNotIn('--manifest-out',self.text[start:end])
        self.assertNotIn('recovery-provenance.json',self.text)

    def test_controller_requires_exact_branch_context(self):
        identity=self.namespace['controller_identity']
        self.assertEqual(identity(self.environment()),('a'*40,'999','1'))
        for field,bad in (('GITHUB_REPOSITORY','other/repo'),('GITHUB_EVENT_NAME','push'),
                          ('GITHUB_SHA','short'),('GITHUB_WORKFLOW_SHA','b'*40),
                          ('GITHUB_RUN_ID','0'),('GITHUB_RUN_ATTEMPT','01')):
            env=self.environment();env[field]=bad
            with self.subTest(field=field),self.assertRaises(ValueError):identity(env)
        env=self.environment()
        env['GITHUB_REF']='refs/tags/controller'
        env['GITHUB_WORKFLOW_REF']='mathorn1973/twist-j/.github/workflows/policy.yml@refs/tags/controller'
        with self.assertRaises(ValueError):identity(env)

    def test_metadata_rejects_changed_identity_failure_and_extra_assets(self):
        import copy
        validator=self.namespace['validate_metadata']
        validator(*self.fixture())
        for index,field,bad in ((0,'id',1),(0,'draft',True),(0,'immutable',False),
                                (1,'run_attempt',1),(1,'conclusion','cancelled'),(1,'path','other'),
                                (2,'id',1),(2,'conclusion','cancelled'),(3,'id',1),(3,'expired',True)):
            items=list(copy.deepcopy(self.fixture()));items[index][field]=bad
            with self.subTest(index=index,field=field),self.assertRaises(ValueError):validator(*items)
        for fault in ('skipped-step','missing-step','extra-asset','wrong-digest'):
            items=list(copy.deepcopy(self.fixture()))
            if fault=='skipped-step':items[2]['steps'][8]['conclusion']='skipped'
            if fault=='missing-step':items[2]['steps'].pop()
            if fault=='extra-asset':items[0]['assets'].append({'name':'extra'})
            if fault=='wrong-digest':items[0]['assets'][0]['digest']='sha256:'+'0'*64
            with self.subTest(fault=fault),self.assertRaises(ValueError):validator(*items)

    def test_pinned_zip_requires_exact_hash_and_single_manifest(self):
        import hashlib,io,zipfile
        from unittest.mock import patch
        def zipped(extra=False):
            stream=io.BytesIO()
            with zipfile.ZipFile(stream,'w') as archive:
                archive.writestr('activation-manifest.json',b'manifest')
                if extra:archive.writestr('extra.txt',b'extra')
            return stream.getvalue()
        archive=zipped()
        constants={'ZIP_BYTES':len(archive),'ZIP_SHA256':hashlib.sha256(archive).hexdigest(),
                   'MANIFEST_BYTES':8,'MANIFEST_SHA256':hashlib.sha256(b'manifest').hexdigest()}
        with patch.dict(self.namespace,constants):
            self.assertEqual(self.namespace['original_manifest'](archive),b'manifest')
            with self.assertRaises(ValueError):self.namespace['original_manifest'](archive+b'x')
        extra=zipped(True)
        constants.update(ZIP_BYTES=len(extra),ZIP_SHA256=hashlib.sha256(extra).hexdigest())
        with patch.dict(self.namespace,constants),self.assertRaises(ValueError):self.namespace['original_manifest'](extra)

    def test_two_asset_readback_integration_and_failures(self):
        import hashlib,io,json,subprocess,tempfile,types,zipfile
        from unittest.mock import patch
        manifest=b'manifest';checksum=b'checksums'
        stream=io.BytesIO()
        with zipfile.ZipFile(stream,'w') as bundle:bundle.writestr('activation-manifest.json',manifest)
        archive=stream.getvalue()
        constants={'ZIP_BYTES':len(archive),'ZIP_SHA256':hashlib.sha256(archive).hexdigest(),
                   'MANIFEST_BYTES':len(manifest),'MANIFEST_SHA256':hashlib.sha256(manifest).hexdigest(),
                   'CHECKSUM_BYTES':len(checksum),'CHECKSUM_SHA256':hashlib.sha256(checksum).hexdigest()}
        for fault in (None,'api-failure','expired','wrong-zip','wrong-manifest','wrong-checksum',
                      'missing-asset','extra-asset','validator-failure'):
            with self.subTest(fault=fault),tempfile.TemporaryDirectory() as temp,patch.dict(self.namespace,constants):
                root=Path(temp)/'checkout';temporary=Path(temp)/'temporary'
                (root/'canon').mkdir(parents=True);temporary.mkdir()
                (root/'canon/SHA256SUMS').write_bytes(checksum)
                release,run,job,artifact=self.fixture()
                if fault=='expired':artifact['expired']=True
                api={
                    'releases/430574383':release,
                    'actions/runs/41301206166/attempts/2':run,
                    'actions/jobs/124841413548':job,
                    'actions/artifacts/13084185131':artifact,
                }
                calls=[]
                def runner(command,check,stdout=None):
                    self.assertTrue(check);calls.append(command)
                    if fault=='api-failure':raise subprocess.CalledProcessError(1,command)
                    if command[:2]==['gh','api']:
                        key=command[2].removeprefix('repos/mathorn1973/twist-j/')
                        data=(archive+b'x' if fault=='wrong-zip' else archive) if key.endswith('/zip') else json.dumps(api[key]).encode()
                        return types.SimpleNamespace(stdout=data)
                    if command[:3]==['gh','release','download']:
                        self.assertEqual(command[3],'canon-v107')
                        dest=Path(command[command.index('--dir')+1])
                        if fault!='missing-asset':(dest/'activation-manifest.json').write_bytes(manifest+b'x' if fault=='wrong-manifest' else manifest)
                        (dest/'SHA256SUMS').write_bytes(checksum+b'x' if fault=='wrong-checksum' else checksum)
                        if fault=='extra-asset':(dest/'extra').write_bytes(b'x')
                        return
                    self.assertEqual(command[2],'tools/check_release_manifest.py')
                    self.assertEqual(command[-2:],['--expected-tag','canon-v107'])
                    if fault=='validator-failure':raise subprocess.CalledProcessError(1,command)
                if fault is None:
                    self.namespace['audit_assets'](root,temporary,runner)
                    self.assertEqual(len(calls),7)
                else:
                    with self.assertRaises((ValueError,subprocess.CalledProcessError)):
                        self.namespace['audit_assets'](root,temporary,runner)


if __name__ == "__main__":
    unittest.main()
