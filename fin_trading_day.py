# -*- coding: utf-8 -*-
"""
@author: luhx
@file: fin_trading_day.py
@time: 2023/4/11 21:59
@desc: 获取东方财富的当前交易日，为板块资金流写入表奠定交易日的逻辑
"""
from selenium import webdriver
import time
from lxml import etree  # 数据的解析
from kds_util.user_logbook import user_log as logger


class FinTradingDay:
    """
    东方财富网站交易日
    """
    def __init__(self):
        option = webdriver.ChromeOptions()  # 网址获取
        # option.add_argument('headless')  # 无界面启动,即设置浏览器静默
        self.driver = webdriver.Chrome(options=option)  # 等价于 options.headless=True
        self.mytree = None

        self.from_http()
        # self.from_file()

    def save_html(self):
        f = open("./data/zs000001.html", "wb")
        f.write(self.driver.page_source.encode())
        f.close()

    def from_file(self):
        self.mytree = etree.parse('./data/zs000001.html', etree.HTMLParser())

    def from_http(self):
        logger.info("will get url...")
        self.driver.get('http://quote.eastmoney.com/zs000001.html')
        # self.save_html()

    def parse_table(self):
        logger.info("wait_time begin...")
        # self.driver.implicitly_wait(10)
        # logger.info("wait_time begin...")
        # time.sleep(10)
        # logger.info("wait_time end.")
        #

        while True:
            time.sleep(1)
            self.mytree = etree.HTML(self.driver.page_source)
            table = self.mytree.xpath('//span[@class="quote_title_tradestate"]')  # 定位表格
            if not table:
                continue
            print(etree.tostring(table[0], encoding="utf-8", pretty_print=True, method="html").decode("utf-8"))
            table1 = table[0].xpath('./parent::*')
            if not table1:
                continue
            print(etree.tostring(table1[0], encoding="utf-8", pretty_print=True, method="html").decode("utf-8"))
            table2 = table1[0].xpath('./child::span[@class="quote_title_time"]')
            if not table2:
                continue
            print(etree.tostring(table2[0], encoding="utf-8", pretty_print=True, method="html").decode("utf-8"))
            text = table2[0].xpath('./text()')[0]
            print(f"当前交易日：{text[1:11].replace('-', '')}")
            break


if __name__ == '__main__':
    fin = FinTradingDay()
    fin.parse_table()
    fin.driver.quit()
    logger.info("work end.")