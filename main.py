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

from CaptchaCore.CaptchaWorker import chemical_formula

start = time.time()
res = chemical_formula(time.time()).difficulty()
print(res)
end = time.time()

print(end - start)
