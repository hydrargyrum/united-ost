#!/usr/bin/env python3

import logging
import os
from pathlib import Path
import sys

try:
    import UnityPy
except ImportError:
    raise ImportError('Please pip install UnityPy')


logging.basicConfig(level=logging.INFO)

orig_path = Path.cwd()


for asset_fn in sys.argv[1:]:
    os.chdir(orig_path)
    # UnityPy searches for .resource files relative to current directory
    # not relative to .assets dir...
    os.chdir(Path(asset_fn).parent)

    am = UnityPy.AssetsManager()
    am.load_file(asset_fn)

    sf, = am.assets.values()
    msk = [v for v in sf.objects.values() if v.type == 'AudioClip']
    for m in msk:
        obj = m.read()

        for filename, mem in obj.samples.items():
            target = orig_path / filename
            try:
                with open(target, 'xb') as fp:
                    fp.write(mem)
            except FileExistsError:
                print(f"Will not overwrite exisisting file {filename}")
            else:
                print(f"Wrote {filename}")
