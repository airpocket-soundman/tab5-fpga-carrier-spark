"""Verify the published files against their recorded SHA-256 hashes."""
from pathlib import Path
import hashlib,json
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'manifest.json').read_text(encoding='utf8'))
errors=[]
for name,expected in manifest.items():
 path=root/name
 if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=expected:errors.append(name)
print(f'Verified {len(manifest)-len(errors)}/{len(manifest)} files')
if errors:raise SystemExit('Mismatches: '+', '.join(errors))
