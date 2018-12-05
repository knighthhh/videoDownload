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
import os
import execjs
import urllib.request

class Multithreading():
    def __init__(self):
        self.down = download.Download()

    def get_toutiao(self, item_list):
        for uid in item_list:
            start_url = 'https://www.365yg.com/c/user/article/?user_id={uid}&max_behot_time={pageToken}&max_repin_time=0&count=20&page_type=0'.format(uid=uid,pageToken='0')
            response = self.down.get_html(start_url)
            if response:
                json_obj = json.loads(response.text)
                for data in json_obj['data']:

                    #判断有没有爬取过
                    try:
                        videoid = data['item_id']
                        if videoid in config.ALL_ID:
                            print(data['title']+'  已下载')
                            continue
                        image_url = data['image_url']
                        title = data['title']
                        username = data['source']
                        write_path = self.make_dir('今日头条',username)

                        r = str(random.random())[3:]
                        detail_url = 'http://www.365yg.com/a{videoid}/'.format(videoid=videoid)
                        detail_response = self.down.get_html(detail_url)
                        find_videoId_res = re.findall(r"videoId: '(.*)'", detail_response.text)
                        if find_videoId_res:
                            p = '/video/urls/v/1/toutiao/mp4/{}?r={}'.format(find_videoId_res[0], r)
                            jscontext = execjs.compile(config.js_str)
                            s = jscontext.call('getParam', p)
                            down_video_url = 'http://ib.365yg.com/video/urls/v/1/toutiao/mp4/{}?r={}&s={}'.format(find_videoId_res[0], r, s)
                            down_video_response = self.down.get_html(down_video_url)
                            video_url = json.loads(down_video_response.text)['data']['video_list']['video_1']['main_url']
                            video_url = base64.b64decode(video_url).decode()
                            print('正在下载：'+title)
                            urllib.request.urlretrieve(image_url, "%s.png" % os.path.join(write_path, title))
                            urllib.request.urlretrieve(video_url, "%s.mp4" % os.path.join(write_path, title))
                            with open('all_video_id.txt','a') as f:
                                f.write(videoid+'\n')
                        else:
                            print('没有找到 加密的videoId')
                    except:
                        print('未知错误')
            else:
                print('获取页面数据失败')

    def get_yidian(self,item_list):
        pass

    def make_dir(self,typename,username):
        toutiao_path = os.path.join(os.getcwd(), typename)

        dir_name_list = []
        for root, dirs, files in os.walk(toutiao_path, topdown=False):
            for name in dirs:
                dir_name_list.append(name)
        if username not in dir_name_list:
            mkdir_path = os.path.join(toutiao_path, username)
            print('新建了文件夹：'+username)
            os.mkdir(mkdir_path)
        return os.path.join(toutiao_path, username)


    def start(self,item_list,appCode):
        a = int(len(item_list) / 4)
        b = a * 2
        c = a * 3
        args = (
            (item_list[:a],),
            (item_list[a:b],),
            (item_list[b:c],),
            (item_list[c:],)
        )
        p = multiprocessing.Pool(4)
        if appCode == 'toutiao':
            for arg in args:
                p.apply_async(self.get_toutiao, args=arg)
        elif appCode == 'yidianzixun':
            for arg in args:
                p.apply_async(self.get_yidian, args=arg)
        p.close()
        p.join()