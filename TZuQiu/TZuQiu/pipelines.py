# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TzuqiuPipeline(object):

    def process_item(self, item, spider):
        print(spider.name)
        print(item["data"][0].get("playerName"))
        for i in range(0, len(item["data"])):
            pass
            # print(item["data"][i])
            # print(item["data"][i].get("playerMainPosition"))
            # print(item["data"][i].get("leagueName"))
            # print(item["data"][i].get("playerName"))
            # print(item["data"][i].get("currentMarketValue"))
            # print(item["data"][i].get("currentClubName"))
            # print(item["data"][i].get("mins"))
            # print(item["data"][i].get("age"))
            # print(item["data"][i].get("rate"))
            # print(item["data"][i].get("lastMarketValue"))
        return item
