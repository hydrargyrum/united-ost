#!/usr/bin/env python3

import logging
import sys

import UnityPy
import UnityPy.Logger


logging.basicConfig()
#logging.root.handlers[0].setFormatter(UnityPy.Logger.ColoredFormatter())
#logging.root.addHandler(UnityPy.Logger.ListHandler())


am = UnityPy.AssetsManager()
am.load_file(sys.argv[1])

sf, = am.assets.values()
# msk = [v for v in sf.objects.values() if isinstance(v.read(), UnityPy.classes.AudioClip)]
msk = [v for v in sf.objects.values() if v.type == 'AudioClip']
for m in msk:
    obj = m.read()
    # with open(f'{mm.name}.dat', 'wb') as fp:
    #     fp.write(mm.m_AudioData)
    import code; code.interact(local=locals())
    # print(obj.m_AudioData)
    for filename, mem in obj.samples.items():
        try:
            with open(filename, 'xb') as fp:
                fp.write(mem)
        except FileExistsError:
            print(f"Will not overwrite exisisting file {filename}")
        else:
            print(f"Wrote {filename}")
