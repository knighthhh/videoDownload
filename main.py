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

def main():
    print('程序开始运行...')
    reader = read.ReadTxt()
    mul = multithreading.Multithreading()
    toutiao_uid_list = reader.read_toutiao_uid()
    print(toutiao_uid_list)
    mul.start(toutiao_uid_list,'toutiao')


if __name__ == '__main__':
    main()