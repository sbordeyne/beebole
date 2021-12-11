import argparse
import toml
import re
import sys
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('version')
    args = parser.parse_args()
    version = args.version

    if not re.search(r'\d+\.\d+\.\d+', version):
        print('Invalid version, use semver versionning.')
        sys.exit(1)

    root = Path(__file__).parent.parent

    with open(root / 'pyproject.toml', 'r+') as tomlfile:
        pyproject = toml.load(tomlfile)
        pyproject['tool']['poetry']['version'] = version
        tomlfile.seek(0)
        toml.dump(pyproject, tomlfile)

    with open(root / 'beebole/__init__.py', 'r+') as pyfile:
        data = pyfile.read()
        data = re.sub(
            r'__version__ = .+', f"__version__ = '{version}'",
            data, re.MULTILINE
        )
        pyfile.seek(0)
        pyfile.write(data)
