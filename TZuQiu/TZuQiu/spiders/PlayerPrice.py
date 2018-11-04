# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from TZuQiu.items import TzuqiuItem
import json


class PlayerpriceSpider(scrapy.Spider):
    name = 'PlayerPrice'
    allowed_domains = ['tzuqiu.cc/marketValues.do']
    # start_urls = ['http://tzuqiu.cc/marketValues.do/']
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/53.0.2785.89 Safari/537.36"

    }
    part1 = "http://www.tzuqiu.cc/players/querysPlayerWithCurSeasonStat.json?draw=1&columns%5B0%5D%5Bdata%5D=playerId&columns%5B0%5D%5Bname%5D=&columns%5B0%5D%5Bsearchable%5D=true&columns%5B0%5D%5Borderable%5D=false&columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B1%5D%5Bdata%5D=playerFormat&columns%5B1%5D%5Bname%5D=&columns%5B1%5D%5Bsearchable%5D=true&columns%5B1%5D%5Borderable%5D=false&columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B2%5D%5Bdata%5D=leagueFormat&columns%5B2%5D%5Bname%5D=&columns%5B2%5D%5Bsearchable%5D=true&columns%5B2%5D%5Borderable%5D=false&columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B3%5D%5Bdata%5D=appsFormat&columns%5B3%5D%5Bname%5D=ps.apps&columns%5B3%5D%5Bsearchable%5D=true&columns%5B3%5D%5Borderable%5D=true&columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B4%5D%5Bdata%5D=minsFormat&columns%5B4%5D%5Bname%5D=ps.mins&columns%5B4%5D%5Bsearchable%5D=true&columns%5B4%5D%5Borderable%5D=true&columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B5%5D%5Bdata%5D=rateFormat&columns%5B5%5D%5Bname%5D=ps.rate&columns%5B5%5D%5Bsearchable%5D=true&columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=marketValueFormat&columns%5B6%5D%5Bname%5D=p.currentMarketValue&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&start="
    part2 = "&length=10&search%5Bvalue%5D=&search%5Bregex%5D=false&extra_param%5BorderCdnLgZero%5D=true&_=1"

    def start_requests(self):
        url = self.part1+str(0)+self.part2
        yield Request(url, callback=self.parse, headers=self.header)

    def parse(self, response):
        it = TzuqiuItem()
        # 调用body_as_unicode()是为了能处理unicode编码的数据
        datas = json.loads(response.body_as_unicode())
        lst = datas["data"]
        it["data"] = lst
        return it
        # for j in range(1, 11):    # 3687
        #     url = self.part1 + str(j * 10) + self.part2
        #     yield Request(url, callback=self.parse, headers=self.header)






