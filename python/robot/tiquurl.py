#!/usr/bin/env python
<<<<<<< HEAD
#coding: utf-8 
#Author: Wattshen
#Email:34665115@qq.com
#Date:2015年5月16日
#Filename:tiquurl.py
#Content:提取远程HTML页面包含的链出URL

#导入urllib2模块,并以之打开URL资源,再以read读取,并将之存到文件

import urllib2
import re

page_url = 'http://www.qq.com'

#获取页面内容
=======
#coding:utf-8
#filename:鎻愬彇杩滅▼HTML椤甸潰鍖呭惈鐨勯摼鍑篣RL
#date:2015骞�5鏈�16鏃�

#瀵煎叆urllib2妯″潡,骞朵互涔嬫墦寮�URL璧勬簮,鍐嶄互read璇诲彇,骞跺皢涔嬪瓨鍒版枃浠�
import urllib2
import re

page_url = 'http://www.sina.com.cn'

#鑾峰彇椤甸潰鍐呭
>>>>>>> master
def getHtml(url):
	page = urllib2.urlopen(url)
	html = page.read()
	return html

<<<<<<< HEAD
#提取页面a标签内的链接地址
=======

#鎻愬彇椤甸潰a鏍囩鍐呯殑閾炬帴鍦板潃
>>>>>>> master
def getLink(html):
	link = []
	#pat = '<a.*?href="([^"]*)".*?>([\S\s]*?)</a>'
	pat = 'href\s*=\s*\"((https?://)?.+?)\"'
<<<<<<< HEAD
	#pat = 'href=\"(.+?)\"'#https?一段加与不加意义不大
	link = re.findall(pat, html)
	return link

#函数调用
htmls = getHtml(page_url)
links = getLink(htmls)
#print htmls
#print links

#将结果存储到文件，并按元素换行
f1 = open(r'file1.txt','w')
f1.write(htmls)
f1.close()

f2 = open(r'file2.txt','w')
for element in links:
	f2.write(str(element)+'\n')#存储为一行一个
#f2.write(str(links))#不换行存储
f2.close()
=======
	#pat = 'href=\"(.+?)\"'#https?涓�娈靛姞涓庝笉鍔犳剰涔変笉澶�
	link = re.findall(pat, html)
	return link

#鎻愬彇椤甸潰鎵�鏈塼itle鐨勫唴瀹�
def getTitle(html):
	title = []
	pat = "<title>(.+?)</title>"
	title = re.findall(pat, html)
	return title



#鍑芥暟璋冪敤
htmls = getHtml(page_url)
links = getLink(htmls)
title = getTitle(htmls)
#print htmls
#print links
for x in title:
	print x


#灏嗙粨鏋滃瓨鍌ㄥ埌鏂囦欢锛屽苟鎸夊厓绱犳崲琛�
f1 = open(r'G:\watt\python\robot\file1.txt','w')
f1.write(htmls)
f1.close()

f2 = open(r'G:\watt\python\robot\file2.txt','w')
for element in links:
	f2.write(str(element)+'\n')
#f2.write(str(links))
f2.close()
>>>>>>> master
