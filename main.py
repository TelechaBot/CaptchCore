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

from CaptchaCore.CaptchaWorker import Tool_CaptchaCore

Tool_CaptchaCore.peiping("H2O+Fe", "FeO+H4")
