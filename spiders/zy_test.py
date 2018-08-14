# _*_ coding: utf-8 _*_
import scrapy
import urllib
import json
from urllib import request
from http import cookiejar
import http.cookiejar
import urllib.request, urllib.parse, urllib.error
import http.cookiejar
import hashlib
from iosjk import to_sql
from sqlalchemy import create_engine
from items import zhaoyangItem
from engine import *



class zySpider(scrapy.Spider):
    name = "zy_test"  # 这个name是你必须给它一个唯一的名字  后面我们执行文件时的名字

    def login(self):
        login_url = 'http://www.go-goal.com/'
        post_URL = 'http://www.go-goal.com/data/handler/LoginHandler.ashx'
        get_url = 'http://www.go-goal.com/data/Fund/53998'  # 利用cookie请求訪问还有一个网址

        # hash = hashlib.md5()
        # hash.update('68125542'.encode('utf-8'))
        # hs1 = hash.hexdigest()
        # hash = hashlib.sha1()
        # hash.update(hs1.encode('utf8'))
        # passw = hash.hexdigest()
        # print(passw)

        values = {'action': 'loginbyapi',
                  'login_name': '15026588463',
                  'password': '68125542'}

        postdata = urllib.parse.urlencode(values).encode()
        user_agent = r'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36'
        headers = {'User-Agent': user_agent}

        cookie_filename = 'cookie_jar.txt'
        cookie_jar = http.cookiejar.MozillaCookieJar(cookie_filename)
        handler = urllib.request.HTTPCookieProcessor(cookie_jar)
        opener = urllib.request.build_opener(handler)

        try:
            print('-------------')
            request = urllib.request.Request(post_URL, data=postdata, headers=headers, method='POST')
            response = opener.open(request)
            # print(response.read())
            r = response.read()
            ll = re.search('"token":"(.+?)"', str(r), re.DOTALL).group(1)
            print(ll)
        except urllib.error.URLError as e:
            print(e.reason)
        else:
            pass

        return ll

    def start_requests(self):
        import time
        token = self.login()
        time = '%.0f' % time.time()
        cookies = {
            "ASP.NET_SessionId": "imrb3zliwkc5nk3h3wn2kyvw",
            "go-goal": "login_name=F00025515&user_id=395370&user_name=%e5%88%98%e5%9d%a4&group=2&role=173,172,168&"
                       "popedom=2003&validdate=2050/1/1 0:00:0&status=1&login_id=338506&org_id=0&integral=0&isResearch=1"
                       "&token={}&Encrypttoken=B8150F8EF398C3628F7A59BF5C5F7001CF4CF2A86E8F985D35DEB07C4150F1B"
                       "13374B8D2C10409CC".format(token),
            "Hm_lvt_27d1fcb4ad73a9f7b75d1c39e3f8fae2": "{}".format(time),
            "Hm_lpvt_27d1fcb4ad73a9f7b75d1c39e3f8fae2": "{}".format(time),

        }
        Result = range(107778, 200000)
        for q in Result:
            url = 'http://www.go-goal.com/data/Info/Handler/NewHandler.ashx'
            data = {'action': 'getproductinfo',
                    'fund_id': '{}'.format(q),
                    'cache_name': {"action": "getproductinfo", "fund_id": "{}".format(q)}
            }
            yield scrapy.FormRequest(url, callback=self.parse, meta={'fund_id': q}, formdata=data, cookies=cookies)

    def parse(self, response):
        fund_id = response.meta['fund_id']
        a = response.text
        r = json.loads(a)
        item = zhaoyangItem()
        item["fund_full_name"] = r.get("fundfullname")
        item["fund_name"] = r.get("fundname")
        item["fund_manager"] = r.get("fundmanager")
        item["reg_code"] = r.get("regcode")
        item["fund_manager_nominal"] = r.get("fundissueorg")
        item["fund_member"] = r.get("fundmember")
        item["fund_status"] = r.get("fundstatus")
        item["type_name"] = r.get("defaulttypename")
        item["data_freq"] = r.get("data_freq")
        item["foundation_data"] = r.get("foundation")
        item["fund_type_structure"] = r.get("fundtypeallocation")
        item["data_source"] = '999999'
        item["data_source_name"] = '朝阳永续'
        item['fund_id'] = fund_id
        print(now2)
        return item
