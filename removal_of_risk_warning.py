# -*- coding: utf-8 -*-
"""
@author: luhx
@file: removal_of_risk_warning.py
@time: 2023/4/3 23:27
@desc: 从东方财富爬取公告类型为：申请撤销风险警示及特别处理 的记录
东方财富网 > 数据中心 > 公告大全 > 沪深京A股公告 > 风险提示
链接：https://data.eastmoney.com/notices/hsa/3.html
"""
from selenium import webdriver
import time
from lxml import etree  # 数据的解析


def get_removal_risk_stocks():
    print("work begin...")
    option = webdriver.ChromeOptions()  # 网址获取
    option.add_argument('headless')  # 无界面启动,即设置浏览器静默
    driver = webdriver.Chrome(options=option)
    driver.get('https://data.eastmoney.com/notices/hsa/3.html')  # 打开浏览器
    time.sleep(2)
    mytree = etree.HTML(driver.page_source)

    titles = mytree.xpath('//div[@title="申请撤销风险警示及特别处理"]')
    for title in titles:
        p = title.xpath('./ancestor::tr[@data-index]')[0]
        code = p.xpath('./descendant::a[@data-code]')[0].attrib['data-code']
        name = p.xpath('./descendant::a[@data-code]')[0].attrib['data-name']
        gg_dt = p.xpath('./child::td[last()]')[0].text
        msg = p.xpath('./child::td/div[@class="ellipsis" and @title]')[0].attrib['title']
        print(f"[{code}]{name}: date:{gg_dt}, title:{msg}")
        # print(etree.tostring(p, encoding="utf-8", pretty_print=True, method="html").decode("utf-8"))
    print("work end.")


if __name__ == '__main__':
    get_removal_risk_stocks()
