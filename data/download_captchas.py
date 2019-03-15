# -*- coding: utf8 -*-

import requests
import random

url = 'http://hyfw.95306.cn/gateway/DzswNewD2D/Dzsw/security/jcaptcha.jpg?update=%s'
print(random.random())


def download(batch, start, end):
    i = start
    while i < end:
        resp = requests.get(url % random.random(), timeout=10)
        with open("imgs/%d_%d.jpg" % (batch, i), 'wb') as f:
            f.write(resp.content)
        i += 1


if __name__ == '__main__':
    download(2, 0, 100)
