#!/usr/bin/env python3
#-*- coding: utf-8 -*-
 
# File Name: get_net.py
# Author: Feng
# Created Time: Sat Aug  4 21:29:08 2018
# Content: 
import requests
import time
from math import fabs
from base64 import b64encode

class RaspberryMonitorNetSpeed:
    url = "http://192.168.123.1/update.cgi?output=netdev"
    headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            # 'Connection':'keep-alive',
            'Connection': 'close',
            'Cookie': 'n56u_cookie_bw_rt_tab=WAN',
            'Host': '192.168.123.1',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            }

    #最近一次请求 
    last_time = 0
    #最近一次请求的下行数据总量
    last_rbytes = 0
    #最近一次请求的上行数据总量
    last_tbytes = 0

    def __init__(self, username, passwd):
        self.headers['Authorization'] = 'Basic ' + b64encode((username + ':' + passwd).encode()).decode()
        data = self.__get_wan_rx_and_tx()
        if data:
            self.last_rbytes = data[0]
            self.last_tbytes = data[1]
            self.last_time = data[2]
        print("data = ", data)

    def __get_wan_rx_and_tx(self):
        text = requests.get(self.url, headers = self.headers).text
        print(text)
        try:
            rx = int(text.split(',')[25].lstrip('rx:').strip(), 16)
            tx = int(text.split(',')[26].lstrip('tx:').rstrip('}\n').strip(), 16)
            new_time = time()
        except (IndexError, ValueError, TypeError):
            return False
        return [rx, tx, new_time]

if __name__ == '__main__':
    RaspberryMonitorNetSpeed('admin', '413162555')

