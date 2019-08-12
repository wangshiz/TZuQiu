# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy import logformatter


class TzuqiuPipeline(object):

    def __init__(self):
        print("正在连接数据库..")
        self.db = pymysql.connect(
            host="localhost",
            port=3306,
            user="root",
            db="test",
            charset="utf8",
            password="123456"
        )
        print("连接上了")
        self.course = self.db.cursor()

    def process_item(self, item, spider):

        try:
            for i in range(0, len(item["data"])):
                sql = """insert into player_price (player_name, age, player_main_position, league_name, current_club_name, mins, rate, current_market_value, last_market_value) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
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
            print("一组提交成功")
        except Exception as err:
            print(err)
        return item

    def close_spider(self, spider):
        self.db.close()
