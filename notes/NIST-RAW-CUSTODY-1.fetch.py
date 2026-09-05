"""NON-CANONICAL opaque custody only; never parse experimental data."""
from pathlib import Path
import hashlib
import json
import subprocess
import sys
import urllib.request


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise RuntimeError('Redirect refused')


def main():
    if len(sys.argv) != 3:
        raise SystemExit('Usage: python3 NIST-RAW-CUSTODY-1.fetch.py EXTERNAL_DIR PUBLIC_CUSTODY_COMMIT')
    destination = Path(sys.argv[1]).resolve()
    pin = sys.argv[2]
    if len(pin) != 40 or any(c not in '0123456789abcdef' for c in pin):
        raise RuntimeError('Full public custody commit required')
    note_dir = Path(__file__).resolve().parent
    checkout = note_dir.parent
    git = ['git', '-C', str(checkout)]
    if subprocess.check_output(git + ['rev-parse', 'HEAD']).decode().strip() != pin:
        raise RuntimeError('Checkout is not the declared custody commit')
    common_git = Path(subprocess.check_output(git + ['rev-parse', '--path-format=absolute', '--git-common-dir']).decode().strip()).resolve()
    if destination.is_relative_to(checkout) or checkout.is_relative_to(destination) or destination.is_relative_to(common_git):
        raise RuntimeError('Custody destination must be outside this checkout and Git metadata')
    for name in ['NIST-RAW-CUSTODY-1.md', 'NIST-RAW-CUSTODY-1.objects.json', 'NIST-RAW-CUSTODY-1.fetch.py']:
        committed = subprocess.check_output(git + ['show', pin + ':notes/' + name])
        if committed != (note_dir / name).read_bytes():
            raise RuntimeError('Local custody file differs from its pin: ' + name)
    raw_manifest = (note_dir / 'NIST-RAW-CUSTODY-1.objects.json').read_bytes()
    manifest = json.loads(raw_manifest)
    destination.mkdir(parents=True, exist_ok=False)
    notice = (note_dir / manifest['notice_file']).read_bytes()
    (destination / 'NIST-SOURCE-NOTICE.md').write_bytes(notice)
    opener = urllib.request.build_opener(NoRedirect)
    receipts = []
    for obj in manifest['objects']:
        request = urllib.request.Request(obj['url'], headers={
            'If-Match': obj['etag'], 'Accept-Encoding': 'identity',
            'User-Agent': 'TWIST-J-public-opaque-custody/1'})
        digest = hashlib.sha256()
        size = 0
        print('OPAQUE_FETCH_BEGIN ' + obj['id'], flush=True)
        with opener.open(request, timeout=manifest['socket_timeout_seconds']) as response:
            if response.status != 200 or response.geturl() != obj['url']:
                raise RuntimeError('Unexpected response identity')
            for header, expected in [('Content-Length', str(obj['archive_bytes'])),
                                     ('ETag', obj['etag']), ('Last-Modified', obj['last_modified'])]:
                if response.headers.get(header) != expected:
                    raise RuntimeError('Provider header changed: ' + header)
            if response.headers.get('Content-Encoding', 'identity') != 'identity':
                raise RuntimeError('Encoded response refused')
            with (destination / (obj['id'] + '.zip')).open('xb') as output:
                while True:
                    chunk = response.read(1024 * 1024)
                    if not chunk:
                        break
                    size += len(chunk)
                    if size > obj['archive_bytes']:
                        raise RuntimeError('Object exceeds pinned size')
                    digest.update(chunk)
                    output.write(chunk)
        if size != obj['archive_bytes']:
            raise RuntimeError('Truncated object')
        receipt = dict(obj, sha256=digest.hexdigest(), semantic_opening=False)
        receipts.append(receipt)
        print(json.dumps(receipt, sort_keys=True), flush=True)
    result = {'schema': 'nist-opaque-custody-receipt/1', 'public_custody_commit': pin,
              'manifest_sha256': hashlib.sha256(raw_manifest).hexdigest(),
              'notice_sha256': hashlib.sha256(notice).hexdigest(),
              'fetcher_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
              'semantic_opening': False, 'objects': receipts}
    (destination / 'custody-receipt.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('OPAQUE_CUSTODY_COMPLETE_NO_SEMANTIC_OPENING', flush=True)


if __name__ == '__main__':
    main()
