# -*- coding: utf-8 -*-
# @Author  : Stone
# @Time    : 2023-04

import io
import requests
import os
from bs4 import BeautifulSoup

# gceguide papers下载网页的网址
# 请直接修改这里
target_url = 'https://papers.gceguide.com/Cambridge%20IGCSE/Physics%20(0625)/'


def download_pdf(save_path, pdf_name, pdf_url):
    send_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
        "Connection": "keep-alive",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.8"}
    response = requests.get(pdf_url, headers=send_headers)
    bytes_io = io.BytesIO(response.content)
    with open(save_path + "%s" % pdf_name, mode='wb') as f:
        f.write(bytes_io.getvalue())
        print('%s.PDF,下载成功！' % (pdf_name))


def url_request():
    save_path = './'
    target = target_url
    req = requests.get(url=target)
    html = req.text
    div_bf = BeautifulSoup(html)
    div = div_bf.find_all('ul', class_='paperslist')
    # print(div[0])
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    for each in a:
        save_path1 = save_path + each.get('href') + '/'
        new_target = target + each.get('href') + '/'
        req2 = requests.get(url=new_target)
        html2 = req2.text
        div_bf2 = BeautifulSoup(html2)
        div2 = div_bf2.find_all('ul', class_='paperslist')
        print(div2[0])
        a_bf2 = BeautifulSoup(str(div2[0]))
        a2 = a_bf2.find_all('a')
        for each2 in a2:
            pdf_name = each2.get('href')
            pdf_url = new_target + each2.get('href')
            if not os.path.exists(save_path1):
                os.makedirs(save_path1)
            download_pdf(save_path + each.get('href') + '/', pdf_name, pdf_url)
            print(new_target + each2.get('href'))


if __name__ == '__main__':
    # save_path = './'
    # pdf_name = '2007年年度报告'
    # pdf_url = "https://papers.gceguide.com/Cambridge%20IGCSE/Physics%20(0625)/2003/0625_s03_ab_5.pdf"
    # download_pdf(save_path, pdf_name, pdf_url)
    url_request()
