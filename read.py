#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     read_txt
   Description :
   Author :        hayden_huang
   Date：          2018/12/4 18:50
-------------------------------------------------
"""

class ReadTxt():
    def __init__(self):
        pass

    def read_success_toutiao(self):
        pass

    def read_success_yidianzixun(self):
        pass

    def read_all_video_id(self):
        item_list = []
        try:
            with open('all_video_id.txt') as f:
                results = f.readlines()
                for res in results:
                    item_list.append(res.strip())
            return item_list
        except:
            return item_list

    def read_toutiao_uid(self):
        item_list = []
        try:
            with open('toutiao_uid.txt') as f:
                results = f.readlines()
                for res in results:
                    item_list.append(res.strip())
            return item_list
        except:
            return item_list

    def read_yidianzixun_uid(self):
        item_list = []
        try:
            with open('yidianzixun_uid.txt') as f:
                results = f.readlines()
                for res in results:
                    item_list.append(res.strip())
            return item_list
        except:
            return item_list

