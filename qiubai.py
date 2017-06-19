#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import re
import sys
# from bs4 import BeautifulSoup

# url = 'https://www.qiushibaike.com/8hr/page/2/?s=4992659'

baseUrl = 'https://www.qiushibaike.com/8hr/page/'
page = 1
s = 4992659

def getUrlString(url,page,s=s):
	urlString = url + str(page) +'/?s=' + str(s)
	return urlString

def getContentList(page):

	html = requests.get(getUrlString(baseUrl,page,s))
	p = r'<div class="content">\s*?<span>(.*?)</span>' # 正则
	pattern = re.compile(p)
	con_list = re.findall(pattern, html.text)

	return con_list

def showInfo(conlist,seq):
	i = seq
	for item in conlist:
		i+=1
		print '%d: %s' %(i,item.replace('<br/>','\n'))
		string = str(raw_input('press n to break:'))
		string.replace(' ','')
		if string=='n':
			return 0
		else:
			continue
	return 1;


def main():
	page = 1
	seq = 0
	con_list = getContentList(page)
	showInfo(con_list, seq)
	seq += len(con_list)
	while True:
		ret = showInfo(getContentList(page), seq)
		if ret==0:
			return
		page +=1
		seq +=20


if __name__ == '__main__':
	main()
	sys.exit(0)



