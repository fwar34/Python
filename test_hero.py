#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: test_hero.py
# Author: Feng
# Created Time: Sun 03 Jun 2018 06:22:20 AM PDT
# Content: 

from urllib.request import urlretrieve
import requests

# 下载王者荣耀英雄图片
def hero_images_download(url, header):
    req = requests.get(url = url, headers = header)
    print(req)


# 程序入口
if __name__ == '__main__':
    headers = {
            'Accept' : 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
            'Accept-Encoding' : 'gzip, deflate',
            'Accept-Language' : 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Cache-Control' : 'max-age=0',
            'Connection' : 'keep-alive',
            'Host' : 'gamehelper.gm825.com',
            'Upgrade-Insecure-Requests' : '1',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0'
            }

    # 英雄列表
    heros_url = "http://gamehelper.gm825.com/wzry/equip/list?channel="
    hero_images_download(heros_url, headers)

