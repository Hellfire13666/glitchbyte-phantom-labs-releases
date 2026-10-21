import io
import json
import pathlib
import sys
import tempfile
import unittest
import zipfile
from unittest.mock import Mock

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from archive_public_installers import digest, validate, verify_data, run


def fixture():
    content = io.BytesIO()
    with zipfile.ZipFile(content, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr('tool-v1/README.md', 'verified sample')
    archive = content.getvalue()
    name = 'tool-v1.zip'
    line = f'{digest(archive)}  {name}\n'.encode()
    return {
        'slug': 'tool', 'version': 'v1', 'repo': 'Hellfire13666/tool-repo',
        'tag': 'v1', 'archive': name, 'checksum': 'tool-v1.sha256',
        'archive_sha256': digest(archive), 'checksum_sha256': digest(line)
    }, archive, line


class InstallerVaultTests(unittest.TestCase):
    def test_rejects_path_traversal(self):
        entry, _, _ = fixture()
        for key, value in [('archive', '../bad.zip'), ('version', '../bad'), ('repo', 'foreign/strange')]:
            case = {**entry, key: value}
            with self.assertRaises(ValueError): validate(case)

    def test_tampering_fails(self):
        entry, archive, checksum = fixture()
        verify_data(entry, archive, checksum)
        with self.assertRaises(ValueError): verify_data(entry, archive+b'bad', checksum)
        with self.assertRaises(ValueError): verify_data(entry, archive, checksum+b'bad')

    def test_mirror_preserves_existing_archive(self):
        entry, archive, checksum = fixture()
        with tempfile.TemporaryDirectory() as td:
            root = pathlib.Path(td)
            registry = root/'registry.json'
            vault = root/'vault'
            registry.write_text(json.dumps({'schema_version': 1, 'approved_public_releases': [entry]}))
            def downloader(url):
                return archive if url.endswith('.zip') else checksum
            results = run(registry, vault, downloader)
            self.assertEqual(results[0]['status'], 'ARCHIVED')
            again = run(registry, vault, Mock(side_effect=AssertionError('Should not download existing archived release')))
            self.assertEqual(again[0]['status'], 'PRESERVED')
            self.assertTrue((vault/'SHA256SUMS.txt').is_file())
            (vault/'tool/v1/tool-v1.zip').write_bytes(b'invalid')
            with self.assertRaises(ValueError): run(registry, vault, downloader)


if __name__ == '__main__':
    unittest.main()
