# -*- coding: utf-8 -*-
"""
@author: luhx
@file: fin_trading_day.py
@time: 2023/4/11 21:59
@desc: 获取东方财富的当前交易日，为板块资金流写入表奠定交易日的逻辑
"""
import random
import traceback

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime
from lxml import etree  # 数据的解析
from kds_util.user_logbook import user_log as logger
from envs import Envs


class FinTradingDay:
    """
    东方财富网站交易日
    """
    def __init__(self):
        self.driver = None
        self.mytree = None
        self.kline_time: str = ""   # K线数据时间
        self.server_time: str = ""
        self.trading_day: str = ""
        self.init_trading_day()

    def save_html(self):
        f = open("./data/zs000001.html", "wb")
        f.write(self.driver.page_source.encode())
        f.close()

    def from_file(self):
        self.mytree = etree.parse('./data/zs000001.html', etree.HTMLParser())

    def from_http(self):
        url = "http://quote.eastmoney.com/zs000001.html"
        logger.info("will get url: {}".format(url))
        self.driver.get(url)
        # self.save_html()

    def init_trading_day(self):
        base_second = 2
        while True:
            if self.parse_table():
                break
            seconds = random.randint(base_second, base_second * 5)
            base_second += 1
            logger.info("will wait {} seconds for get trading day again.".format(seconds))
            time.sleep(seconds)
        self.trading_day = self.kline_time[:10].replace("-", "")
        self.server_time = str(datetime.now())
        sql = "replace into tbl_trading_day(TradingDay,KlineTime,ServerTime) values('{}','{}','{}')".\
            format(self.trading_day, self.kline_time, self.server_time)
        Envs.mysql.exec(sql)

    def parse_table(self):
        # chrome_options = Options()
        # chrome_options.add_argument('--disable-browser-side-navigation')
        # # chrome_options.add_argument('--headless')
        # self.driver = webdriver.Chrome(options=chrome_options)  # 等价于 options.headless=True
        try:
            options = webdriver.ChromeOptions()
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option("useAutomationExtension", False)
            options.add_argument('--disable-browser-side-navigation')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-setuid-sandbox')
            options.add_argument('--no-sandbox')    # 在root权限下跑
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            self.driver = webdriver.Chrome(options=options)  # 等价于 options.headless=True

            self.from_http()
            # self.from_file()
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
                print(f"当前上证指数K线时间：{text[1:11]} {text[-9:-1]}")
                self.kline_time = f"{text[1:11]} {text[-9:-1]}"
                # self.save_html()
                break
        except:
            logger.error("error: {}".format(traceback.format_exc()))
        finally:
            time.sleep(1)
            # self.driver.quit()
        return len(self.kline_time) >= 19


if __name__ == '__main__':
    fin = FinTradingDay()


    logger.info("work end.")
