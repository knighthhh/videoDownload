#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :        hayden_huang
   Date：          2018/12/4 18:39
-------------------------------------------------
"""

import multithreading
import read
import config

def main():
    print('程序开始运行...')
    reader = read.ReadTxt()
    config.ALL_ID = reader.read_all_video_id()
    mul = multithreading.Multithreading()
    toutiao_uid_list = reader.read_toutiao_uid()
    mul.start(toutiao_uid_list,'toutiao')


if __name__ == '__main__':
    main()