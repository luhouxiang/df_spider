from selenium import webdriver  # 导入模块，selenium导入浏览器驱动，用get方法打开浏览器
import time
import re
import csv  # 存储数据
from lxml import etree  # 数据的解析
# 东方财富网 > 数据中心 > 公告大全 > 沪深京A股公告 > 风险提示 > 公告类型 > 申请撤销风险警示及特别处理
# 东方财富网 > 数据中心 > 公告大全 > ST瀚叶 > ST瀚叶-公告正文

option = webdriver.ChromeOptions()   # 网址获取
option.add_argument('headless')  # 无界面启动,即设置浏览器静默
# 等价于 options.headless=True
driver = webdriver.Chrome(options=option)  
# 等价于 driver = webdriver.Chrome(desired_capabilities=options.to_capablities())
driver.get('https://data.eastmoney.com/zjlx/000040.html')  # 打开浏览器
time.sleep(2) #推迟调用线程的运行，可表示进程挂起的时间，这里让他推迟执行2秒

source = driver.page_source #获取页面源码
print(source)
mytree = etree.HTML(source) #解析网页内容
tables = mytree.xpath('//div[@class="dataview"]/table') #定位表格
for i in range(len(tables)): #循环表格
    onetable = []
    trs = tables[i].xpath('.//tr') #取出所有tr标签
    for tr in trs:
        ui = []
        for td in tr:
            texts = td.xpath(".//text()") #取出所有td标签下的文本
            mm = []
            for text in texts:
                mm.append(text.strip("")) #去掉所有空格、换行符
            ui.append(','.join(mm))
        onetable.append(ui) #整张表格

with open('data.csv', 'a', newline='') as file: #将数据写入文件
    csv_file = csv.writer(file)
    for i in onetable:
        csv_file.writerow(i) #按行写入

time.sleep(2)
driver.close() #关闭当前窗口