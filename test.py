#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     test
   Description :
   Author :        hayden_huang
   Date：          2018/12/4 21:32
-------------------------------------------------
"""
import os
for root, dirs, files in os.walk("/Users/hayden/Documents/hhh/project/videoDownload/今日头条", topdown=False):

    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
    print(dirs)
    print(1)