#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
-------------------------------------------------
   File Name：     multithreading
   Description :
   Author :        hayden_huang
   Date：          2018/12/4 19:22
-------------------------------------------------
"""

import multiprocessing
import json
import download
import config
import random
import base64
import re
import execjs

class Multithreading():
    def __init__(self):
        self.down = download.Download()

    def get_toutiao(self,item_list):
        print(11)
        for uid in item_list:
            start_url = 'https://www.365yg.com/c/user/article/?user_id={uid}&max_behot_time={pageToken}&max_repin_time=0&count=20&page_type=0'.format(uid=uid,pageToken='0')
            print(start_url)
            response = self.down.get_html(start_url)
            if response:
                json_obj = json.loads(response.text)
                for data in json_obj['data']:

                    #判断有没有爬取过

                    videoid = data['item_id']
                    r = str(random.random())[3:]
                    # origin_url = base64.b64decode(videoid).decode()
                    # vid = re.findall('https?://toutiao.com/group/(\d+)/', origin_url)
                    detail_url = 'http://www.365yg.com/a{videoid}/'.format(videoid=videoid)
                    detail_response = self.down.get_html(detail_url)
                    find_videoId_res = re.findall(r"videoId: '(.*)'", detail_response.text)
                    if find_videoId_res:
                        p = '/video/urls/v/1/toutiao/mp4/{}?r={}'.format(find_videoId_res[0], r)
                        s = execjs(config.js_str, 'getParam', p)
                        down_video_url = 'http://ib.365yg.com/video/urls/v/1/toutiao/mp4/{}?r={}&s={}'.format(data[0], r, s)
                        down_video_response = self.down.get_html(down_video_url)
                        video_url = json.loads(down_video_response.text)['data']['video_list']['video_1']['main_url']
                        video_url = base64.b64decode(video_url).decode()
                        print(video_url)
                    else:
                        print('没有找到 加密的videoId')

            else:
                print('获取页面数据失败')

    def get_yidian(self,item_list):
        pass

    def start(self,item_list,appCode):
        a = int(len(item_list) / 4)
        b = a * 2
        c = a * 3
        args = (
            (item_list[:a]),
            (item_list[a:b]),
            (item_list[b:c]),
            (item_list[c:])
        )
        p = multiprocessing.Pool(4)
        print(len(args))
        print(args)
        if appCode == 'toutiao':
            for arg in args:

                p.apply_async(self.get_toutiao, args=arg)
        elif appCode == 'yidianzixun':
            for arg in args:
                p.apply_async(self.get_yidian, args=arg)
        p.close()
        p.join()