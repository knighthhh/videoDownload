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
"""
for (var o = "sptoken", a = "", c = 1; c < arguments.length; c++)
                o += arguments[c];
            for (var c = 0; c < o.length; c++) {
                var r = 10 ^ o.charCodeAt(c);
                a += String.fromCharCode(r)
            }
"""
from urllib.parse import quote
o = 'sptokenm631766010'
a = ''
for i in range(len(o)):
    r = 10^ord(o[i])
    a +=chr(r%256)

print(a)
print(quote(a))

import time

date_timestamp = int(time.mktime(time.strptime('2018-12-05 11:40:32','%Y-%m-%d %H:%M:%S')))

print(date_timestamp)
