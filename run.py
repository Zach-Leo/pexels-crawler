#!/usr/bin/python
# _*_ coding:utf _*_

import os
import sys
import time
import os.path
import random
import requests
from lxml import etree
from imp import reload




def set_header(url, user_agent):

    headers = {"User-Agent": user_agent}
    try:
        req = requests.get(url, headers=headers)
        if req.status_code == 200:
            return req.text.encode('utf8')
        else:
            return ''
    except Exception as e:
        print
        e


def get_picture(url, download_dir, user_agent):

    if not os.path.exists(download_dir):
        os.mkdir(download_dir)
    html = set_header(url,user_agent)
    selector = etree.HTML(html)

    for url in selector.xpath('//img[@class="photo-item__img"]/@src'):
        url = "https://static." + url.split("images.")[1].split("?")[0]
        picture_name = url.split("?")[0].split("/")[-1].replace('-', '_')
        print(picture_name)
        print("downloading picutre %s" % (picture_name))
        with open(download_dir + picture_name, 'wb') as f:
            f.write(requests.get(url).content)
            f.close()
        with open(download_dir + "list.txt", 'ab') as f:
            url = url+'\n'
            f.write(url.encode(encoding='utf-8'))
            f.close()
        #time.sleep(random.randint(1, 3))

def run(user_agent,download_dir,element,search_range):
    search_element = 'https://www.pexels.com/search/' + element + '/?page={}'
    url_lists = [search_element.format(i) for i in range(1, search_range)]
    for url in url_lists:
        get_picture(url, download_dir, user_agent)


if __name__ == "__main__":

    user_agent = 'Mozilla/5.0 AppleWebKit/537.36 Chrome/65.0.3325.181 Safari/537.36'
    download_dir = '/users/haohao/Desktop/pexels/'
    element = 'cat'
    search_range = 20
    search_element = 'https://www.pexels.com/search/'+element+'/?page={}'
    url_lists = [search_element.format(i) for i in range(1, search_range)]
    for url in url_lists:
        get_picture(url, download_dir, user_agent)
