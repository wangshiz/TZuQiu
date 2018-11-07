# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class TzuqiuPipeline(object):
    def __init__(self):
        self.db = pymysql.connect(
            "",
            "",
            ""
        )
        self.course = self.db.cursor()

    def process_item(self, item, spider):

        for i in range(0, len(item["data"])):
            sql = "insert into player_price values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            lst = [
                item["data"][i].get("playerName"),
                item["data"][i].get("age"),
                item["data"][i].get("playerMainPosition"),
                item["data"][i].get("leagueName"),
                item["data"][i].get("currentClubName"),
                item["data"][i].get("mins"),
                item["data"][i].get("rate"),
                item["data"][i].get("currentMarketValue"),
                item["data"][i].get("lastMarketValue")
            ]
            self.course.execute(sql, lst)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.db.close()
