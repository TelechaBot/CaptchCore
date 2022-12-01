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
import CaptchaCore

start = time.time()
res = CaptchaCore.gravity_work(time.time()).create()
print(res)
res = CaptchaCore.biological_DNA(time.time()).create()
print(res)
res = CaptchaCore.binary_first_equation(time.time()).create()
print(res)
res = CaptchaCore.Combustion_Calculations(time.time()).create()
print(res)
res = CaptchaCore.cosmic_speed(time.time()).create()
print(res)
end = time.time()
print(end - start)


def MD5(strs: str):
    import hashlib
    hl = hashlib.md5()
    hl.update(strs.encode(encoding='utf-8'))
    return hl.hexdigest()
