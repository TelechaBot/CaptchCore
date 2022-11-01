# import time
# from CaptchaCore import CaptchaWorker
#
# some = CaptchaWorker.Importer(s=time.time())
# e1 = time.time()
# paper = some.pull(difficulty_min=2, difficulty_limit=9, model_name="生物题库")
# print(paper)
# e2 = time.time()
#
# print(e2 - e1)
# -*- coding: utf-8 -*-
import time

from CaptchaCore.CaptchaWorker import TTS_verification

start = time.time()
res = TTS_verification(time.time()).create()
print(res)
end = time.time()

print(end - start)


def MD5(strs: str):
    import hashlib
    hl = hashlib.md5()
    hl.update(strs.encode(encoding='utf-8'))
    return hl.hexdigest()
