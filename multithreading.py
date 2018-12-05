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
import time
import urllib.request
import socket
socket.setdefaulttimeout(30)

class Multithreading():
    def __init__(self):
        self.down = download.Download()

    # 今日头条
    def get_toutiao(self, item_list):
        now_timestamp = int(time.time())
        for uid in item_list:
            flag = False  # 翻页标志
            pageToken = '0'
            for i in  range(0,20):
                start_url = 'https://www.365yg.com/c/user/article/?user_id={uid}&max_behot_time={pageToken}&max_repin_time=0&count=20&page_type=0'.format(uid=uid,pageToken=pageToken)
                response = self.down.get_html(start_url)
                if response:
                    json_obj = json.loads(response.text)
                    for data in json_obj['data']:
                        try:
                            # 判断有没有爬取过
                            videoid = data['item_id']
                            if videoid in config.ALL_ID:
                                print(data['title']+'  已下载')
                                continue
                            image_url = data['image_url']
                            title = data['title']
                            username = data['source']
                            date_timestamp = data['behot_time']

                            # 超过一周，不继续翻页
                            if now_timestamp - date_timestamp > 60 * 60 * 24 * 7:
                                flag = True
                                break

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
                    pageToken = str(json_obj['next']['max_behot_time'])

                else:
                    print('获取页面数据失败')

            if flag:
                break

    #一点资讯
    def get_yidian(self,item_list):
        headers = {
            'Accept': "*/*",
            'Accept-Encoding': "gzip, deflate",
            'Accept-Language': "zh-CN,zh;q=0.9",
            'Cache-Control': "no-cache",
            'Connection': "keep-alive",
            'Host': "www.yidianzixun.com",
            'Pragma': "no-cache",
            'Referer': "http://www.yidianzixun.com/channel/",
            'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            'X-Requested-With': "XMLHttpRequest",
            'cache-control': "no-cache",
        }
        now_timestamp = int(time.time())
        for uid in item_list:
            flag = False  # 翻页标志
            for i in range(0,20):
                cstart = str(i*10)
                cend = str(int(cstart)+10)
                pageToken = self.get_yidian_pageToken(uid, cstart, cend)
                start_url = 'http://www.yidianzixun.com/home/q/news_list_for_channel?channel_id={uid}&cstart={cstart}&cend={cend}&infinite=true&refresh=1&__from__=pc&multi=5&_spt={pageToken}&appid=web_yidian'.format(uid=uid,cstart=cstart,cend=cend,pageToken=pageToken)
                response = self.down.get_html(start_url,headers=headers)
                if response:
                    json_obj = json.loads(response.text)
                    for data in json_obj['result']:
                        try:
                            if data['ctype'] == 'video_live':
                                videoid = data['itemid']
                                if videoid in config.ALL_ID:
                                    print(data['title'] + '  已下载')
                                    continue
                                image_url = 'http://i1.go2yd.com/image.php?url='+data['image']
                                video_url = data['video_url']
                                date = data['date']
                                date_timestamp = int(time.mktime(time.strptime(date, '%Y-%m-%d %H:%M:%S')))
                                title = data['title']
                                username = data['source']

                                #超过一周，不继续翻页
                                if now_timestamp - date_timestamp > 60*60*24*7:
                                    flag = True
                                    break

                                write_path = self.make_dir('一点资讯', username)
                                print('正在下载：' + title)
                                urllib.request.urlretrieve(image_url, "%s.png" % os.path.join(write_path, title))
                                urllib.request.urlretrieve(video_url, "%s.mp4" % os.path.join(write_path, title))
                                with open('all_video_id.txt', 'a') as f:
                                    f.write(videoid + '\n')
                        except:
                            print('未知错误')
                else:
                    print('获取页面数据失败')

            if flag:
                break

    def get_yidian_pageToken(self,uid, cstart, cend):
        o = 'sptoken'+uid+cstart+cend
        a = ''
        for i in range(len(o)):
            r = 10 ^ ord(o[i])
            a += chr(r % 256)
        return a

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