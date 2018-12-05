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
import time
import multiprocessing

def main():
    try:
        reader = read.ReadTxt()
        config.ALL_ID = reader.read_all_video_id()
        mul = multithreading.Multithreading()

        print('开始扫描今日头条。。')
        toutiao_uid_list = reader.read_toutiao_uid()
        mul.start(toutiao_uid_list,'toutiao')

        print('开始扫描一点资讯。。')
        yidianzixun_uid_list = reader.read_yidianzixun_uid()
        mul.start(yidianzixun_uid_list,'yidianzixun')
    except:
        print('未知错误')


if __name__ == '__main__':
    while True:
        print('程序开始运行...')
        print('当前时间：'+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
        multiprocessing.freeze_support()
        main()
        print('本次已跑完！！')
        print('10分钟后重新跑。。。')
        time.sleep(60*10)