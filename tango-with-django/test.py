# -*- coding: utf-8 -*-
# 文件路径问题

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print __file__ # 文件名
print "os.path.abspath(__file__) results is %s" % os.path.abspath(__file__) # 文件路径包括文件名
print "os.path.dirname(os.path.abspath(__file__)) results is %s" \
    % os.path.dirname(os.path.abspath(__file__)) # test.py 的目录名称


"""
输出是这样的
test.py
os.path.abspath(__file__) results is C:\Users\we\test.py
os.path.dirname(os.path.abspath(__file__)) results is C:\Users\we
"""