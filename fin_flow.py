# -*- coding: utf-8 -*-
"""
@author: luhx
@file: fin_flow.py
@time: 2023/4/10 20:35
@desc: 资金流
"""
from selenium import webdriver
import time
from lxml import etree  # 数据的解析
from kds_util.user_logbook import user_log as logger


class FinFlow:
    """
    资金流
    """

    def __init__(self):
        option = webdriver.ChromeOptions()  # 网址获取
        option.add_argument('headless')  # 无界面启动,即设置浏览器静默
        self.driver = webdriver.Chrome(options=option)  # 等价于 options.headless=True
        self.mytree = None

        # self.from_http()
        self.from_file()

    def save_html(self):
        f = open("./data/bk_zj01.html", "wb")
        f.write(self.driver.page_source.encode())
        f.close()

    def from_file(self):
        self.mytree = etree.parse('./data/bk_zj01.html', etree.HTMLParser())

    def from_http(self):
        self.driver.get('https://data.eastmoney.com/bkzj/hy.html')
        time.sleep(2)
        self.mytree = etree.HTML(self.driver.page_source)
        self.save_html()

    def parse_table(self):
        table = self.mytree.xpath('//div[@id="dataview" and @class="dataview"]')[0]  # 定位表格
        # print(etree.tostring(table, encoding="utf-8", pretty_print=True, method="html").decode("utf-8"))
        table1 = table.xpath('./descendant::div[@class="dataview-body"]/table/tbody')[0]
        # print(etree.tostring(table1, encoding="utf-8", pretty_print=True, method="html").decode("utf-8"))
        tr_arr = table1.xpath('./descendant::tr[@data-index]')
        for index, tr in enumerate(tr_arr):
            print("[{}]{}".format(index, etree.tostring(tr, encoding="utf-8", pretty_print=True, method="html").decode("utf-8")))


if __name__ == '__main__':
    fina = FinFlow()
    fina.parse_table()
    logger.info("work end.")
