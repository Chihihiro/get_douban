# -*- coding: utf-8 -*-
import sys
from engine import *
import scrapy, re
import hashlib
from bs4 import BeautifulSoup
import json
import random
import pandas as pd
import datetime as dt

#
# class CarSpider(scrapy.Spider):
#     name = "car"
#     # allowed_domains = ["http://gs.amac.org.cn/"]
#     # custom_settings = {
#     #     'DOWNLOAD_DELAY': 1.2,
#     #     'CONCURRENT_REQUESTS_PER_IP': 16,
#     # }
#
#     headers = {
#         'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#         'Accept-Encoding': 'gzip, deflate, sdch',
#         'Accept-Language': 'zh-CN,zh;q=0.8',
#         'Cache-Control': 'max-age=0',
#         'Connection': 'keep-alive',
#         'Cookie': 'look=first',
#         'Host': 'gs.amac.org.cn',
#         'If-Modified-Since': 'Sun, 02 Jul 2017 21:29:20 GMT',
#         'If-None-Match': '',
#         'Upgrade-Insecure-Requests': '1',
#         'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
#     }
#     start_url = 'https://car.autohome.com.cn/'
#
#
#
#
#
#
# # -----------------------------------------------------------
from bs4 import BeautifulSoup
import pymysql
import requests
import re
import os

#
#     url = "http://gs.amac.org.cn/amac-infodisc/api/fund/account?rand=0.472343895178601&page=0&size=100"
#
#
#     s = json.dumps({'rand': '0.472343895178601', 'page': 0, 'size': 100})
#     headers = {'Content-Type': 'application/json'}
#
#
#     r = requests.post(url, headers=headers, data=s).text
#     soup = BeautifulSoup(response.body, "lxml")

# url = 'http://www.go-goal.com/data/Info/Handler/NewHandler.ashx'
#
# data = {'action': 'getproductinfo',
#         'fund_id': '107778',
#         'cache_name': {"action": "getproductinfo", "fund_id": "107778"}}
#
# headers = {'Accept': 'application/json, text/javascript, */*; q=0.01',
#            'Accept-Encoding': 'gzip, deflate',
#            'Accept-Language': 'zh-CN,zh;q=0.9',
#            'Connection': 'keep-alive',
#            'Content-Length': '120',
#            'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
#            'Origin': 'http://www.go-goal.com',
#            'Cookie':'ASP.NET_SessionId=imrb3zliwkc5nk3h3wn2kyvw; go-goal=login_name=F00025515&user_id=395370&user_name=%e5%88%98%e5%9d%a4&group=2&role=173,172,168&popedom=2003&validdate=2050/1/1 0:00:0&status=1&login_id=338506&org_id=0&integral=0&isResearch=1&token={}&Encrypttoken=85A4905BC5307BC048425BB4B15196193053A8DF315A5D869D1223BA902DB34871F6ADBDA7DD5112; Hm_lvt_27d1fcb4ad73a9f7b75d1c39e3f8fae2=1527666007; Hm_lpvt_27d1fcb4ad73a9f7b75d1c39e3f8fae2=1527730116'.format(a),
#            'Referer': 'http://www.go-goal.com/data/Fund/107778',
#            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
#            'X-Requested-With': 'XMLHttpRequest'}


headers = {'Referer': 'http://www.go-goal.com/data/Fund/107778',
          'cookie':'pgv_pvi=5095307264, pgv_si=s1169753088',
           'Referer': 'http://www.go-goal.com/data/Fund/107778',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
           'X-Requested-With': 'XMLHttpRequest'}
r = requests.get(url, headers=headers, data=data)
html = str(r).decode("utf-8")

headers = {'Accept': 'text/html,application/xhtml+xm…plication/xml;q=0.9,*/*;q=0.8',
           'Accept-Encoding': 'gzip, deflate, br',
           'Host': 'hr.tencent.com',
           'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
           'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; …) Gecko/20100101 Firefox/60.0'}

cookies = {'pgv_pvi': '242413568',
           'pgv_si': 's4366639104',
           'PHPSESSID': 'ph6safag0h2hqns92bgpgiu1v3'}


#
#
#     name = r.xpath('//table//td[@class="l square"]//a//text()').extract()
#     id = r.xpath('//tr/td/a//text()').extract()
#
#     url2 = 'http://gs.amac.org.cn/amac-infodisc/res/fund/account/1805241745100779.html'
#     r =requests.get(url2, headers=headers).content
#     html1 = r.decode("utf8")
#
#     url = 'https://car.autohome.com.cn/'
#     r = requests.get(url, headers=headers).content
#     r1 = r.decode("gbk", "Unicode")
#
#
#     def parse(self, response):
#         # print json.loads(response.body)
#         page = json.loads(response.body)['totalPages']
#         for i in range(page, -1, -1):
#             url = 'http://gs.amac.org.cn/amac-infodisc/api/fund/account?rand={}&page={}&size=100'.format(
#                 random.random(), i)
#             yield scrapy.Request(url, method='POST', body='{}', headers={'Content-Type': 'application/json'},
#                                  callback=self.parse_id, dont_filter=True)
#
#     def parse_id(self, response):
#         infos = json.loads(response.body)['content']
#         'http://ba.amac.org.cn/pages/amacWeb/user!search.action'
#         for info in infos[0:]:
#             url = 'http://gs.amac.org.cn/amac-infodisc/res/fund/account/{}.html'.format(info['id'])
#             fund_id = info['id']
#             yield scrapy.Request(url, callback=self.parse_account, meta={'fund_id': fund_id})
#
#     def parse_account(self, response):
#         self.log(response.url)
#         soup = BeautifulSoup(response.body, "lxml")
#         infos = soup.find("table", {"class": "table table-center table-info"})
#         item = xFundAccountItem()
#         item['fund_id'] = response.meta['fund_id']
#         item['reg_code_amac'] = infos.find('td', text=u"备案编码").find_next_sibling('td').text
#         item['fund_name_amac'] = infos.find('td', text=u"专户名称").find_next_sibling('td').text
#         item['fund_issue_org_amac'] = infos.find('td', text=u"管理人名称").find_next_sibling('td').text
#         item['fund_custodian_amac'] = infos.find('td', text=u"托管人名称").find_next_sibling('td').text
#         item['reg_time_amac'] = infos.find('td', text=u"备案日期").find_next_sibling('td').text
#         item['fund_time_limit_amac'] = infos.find('td', text=u"合同期限").find_next_sibling('td').text
#         item['issuing_scale_amac'] = infos.find('td', text=u"设立时募集资金总额（万元）").find_next_sibling('td').text.strip()
#         # item['fund_type_target_amac'] = infos.find('td', text=u"非专项资产管理计划产品类型").find_next_sibling('td').text
#         item['fund_type_allocation_amac'] = infos.find('td', text=u"是否分级").find_next_sibling('td').text
#         item['number_clients_amac'] = infos.find('td', text=u"成立时投资者数量").find_next_sibling('td').text
#         orientation_amac = re.search('"td-title">投资范围及比例</td>.+?"td-content" colspan="2">(.+?)</td>', response.body,
#                                      re.DOTALL)
#         item['orientation_amac'] = orientation_amac.group(1) if orientation_amac else None
#         for i in item:
#             if i != "fund_name_amac":
#                 item[i] = clean_str_strong(item[i])
#             elif item[i]:
#                 item[i] = clean_str_strong(item[i], 'edge')
#         item['reg_time_amac'] = regularize_time(item['reg_time_amac'])
#         print item
#         item['version'] = self.version
#         yield item
