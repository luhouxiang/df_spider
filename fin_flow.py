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

from envs import Envs
from obj import FinFlowItem
import re
import helper
from fin_trading_day import FinTradingDay


class FinFlow:
    """
    资金流
    """

    def __init__(self):
        option = webdriver.ChromeOptions()  # 网址获取
        option.add_argument('headless')  # 无界面启动,即设置浏览器静默
        self.fin_day_info: FinTradingDay = FinTradingDay()
        self.driver = webdriver.Chrome(options=option)  # 等价于 options.headless=True
        self.mytree = None

        self.from_http()
        # self.from_file()

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
        table1 = table.xpath('./descendant::div[@class="dataview-body"]/table/tbody')[0]
        tr_arr = table1.xpath('./descendant::tr[@data-index]')
        for tr in tr_arr:
            # print("{}".format(etree.tostring(tr, encoding="utf-8", pretty_print=True, method="html").decode("utf-8")))
            td_arr = tr.xpath('./td')
            f = self.parse_td(td_arr)
            print(f)
            self.save_to_mysql(f)

    @staticmethod
    def parse_td(td_arr) -> FinFlowItem:
        f = FinFlowItem()
        for index, td in enumerate(td_arr):
            txt = ("{}".format(etree.tostring(td, encoding="utf-8", pretty_print=True, method="html").
                               decode("utf-8")))

            # print(f"[{index}]:{txt}")
            if index == 0:
                res_value = r'<td style.*?>(.*?)</td>'
                v = re.findall(res_value, txt, re.S | re.M)
                f.serial_no = int(v[0])
                logger.info(f"serial_no: {v[0]}")
            elif index == 1:
                res_value = r'<td style.*?>\s*<a .*?>(.*?)</a>\s*</td>'
                v = re.findall(res_value, txt, re.S | re.M)
                f.bk_name = str(v[0])
                logger.info(f"bk_name: {v[0]}")
            elif index == 2:
                res_value = r'<td style.*?>\s*<a .*?>(.*?)</a>.*</a>\s*</td>'
                v = re.findall(res_value, txt, re.S | re.M)
            else:
                res_value = r'<td .*?>\s*<span .*?>(.*?)</span>\s*(</a>)*</td>'
                v = re.findall(res_value, txt, re.S | re.M)[0]
                # print(v)
                if index == 3:
                    f.today_zdf = helper.parse_value(v[0])
                    logger.info(f"today_zdf: {v[0]}")
                elif index == 4:
                    f.today_main_net = helper.parse_value(v[0])
                    logger.info(f"today_main_net: {v[0]}")
                elif index == 5:
                    f.today_main_rate = helper.parse_value(v[0])
                    logger.info(f"today_main_rate: {v[0]}")
                elif index == 6:
                    f.today_large_net = helper.parse_value(v[0])
                    logger.info(f"today_large_net: {v[0]}")
                elif index == 7:
                    f.today_large_rate = helper.parse_value(v[0])
                    logger.info(f"today_large_rate: {v[0]}")
                elif index == 8:
                    f.today_big_net = helper.parse_value(v[0])
                    logger.info(f"today_big_net: {v[0]}")
                elif index == 9:
                    f.today_big_rate = helper.parse_value(v[0])
                    logger.info(f"today_big_rate: {v[0]}")
                elif index == 10:
                    f.today_middle_net = helper.parse_value(v[0])
                    logger.info(f"today_middle_net: {v[0]}")
                elif index == 11:
                    f.today_middle_rate = helper.parse_value(v[0])
                    logger.info(f"today_middle_rate: {v[0]}")
                elif index == 12:
                    f.today_small_net = helper.parse_value(v[0])
                    logger.info(f"today_small_net: {v[0]}")
                elif index == 13:
                    f.today_small_rate = helper.parse_value(v[0])
                    logger.info(f"today_small_rate: {v[0]}")
                elif index == 14:
                    f.delegate_name = helper.parse_value(v[0])
                    logger.info(f"delegate_name: {v[0]}")
        return f

    def save_to_mysql(self, f):
        info = self.fin_day_info
        sql = "replace into tbl_bk_fin_flow(TradingDay,BkName,SerialNo,TodayZdf,TodayMainNet,TodayMainRate," \
              "TodayLargeNet,TodayLargeRate,TodayBigNet,TodayBigRate,TodayMiddleNet,TodayMiddleRate," \
              "TodaySmallNet,TodaySmallRate,DelegateName,KlineTime)values({},'{}',{},{},{},{}," \
              "{},{},{},{},{},{}," \
              "{},{},'{}','{}')". \
            format(info.trading_day, f.bk_name, f.serial_no, f.today_zdf, f.today_main_rate, f.today_main_rate,
                   f.today_large_net, f.today_large_rate, f.today_big_net, f.today_big_rate,
                   f.today_middle_net, f.today_middle_rate,
                   f.today_small_net, f.today_small_rate, f.delegate_name, info.kline_time)
        rel = Envs.mysql.exec(sql)
        logger.info(f"rel={rel},{sql}")


if __name__ == '__main__':
    fina = FinFlow()
    fina.parse_table()
    logger.info("work end.")
