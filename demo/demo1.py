# -*- coding: utf-8 -*-
"""
@author: luhx
@file: demo1.py
@time: 2023/4/14 21:12
@desc:
"""
#
# pymysql_url = "mysql+pymysql://root:Zhao123@Lu123@192.168.1.100:3306/hqdb?charset=utf8"
# config = {}
# pos = pymysql_url.find("://")
# b = pymysql_url[pos+3:]
# pos2 = b.rfind("@")
# user_pass = b[:pos2]
# ip_all = b[pos2+1:]
# host_port = ip_all.split("/")[0]
# db_utf = ip_all.split("/")[1]
# config['db_host'] = host_port.split(":")[0]
# config['db_port'] = int(host_port.split(":")[1])
# config['db_user'] = user_pass.split(":")[0]
# config['db_pass'] = user_pass.split(":")[1]
# config['db_database'] = db_utf.split("?")[0]
# print(config)


import re
txt = """<td style="">1</td>"""
res_value = r'<td style.*?>(.*?)</td>'
m_value = re.findall(res_value, txt, re.S | re.M)  # <td><span class="nickname">(字) 翔宇</span></td>
print(m_value)


txt = """<td style=""><a href="//quote.eastmoney.com/unify/r/90.BK1036">半导体</a></td>"""
res_value = r'<td style.*?><a .*?>(.*?)</a></td>'
m_value = re.findall(res_value, txt, re.S | re.M)  # <td><span class="nickname">(字) 翔宇</span></td>
print(m_value)

txt = """<td style="">
<a class="red" href="/bkzj/BK1036.html">大单详情</a> 
                <a href="//guba.eastmoney.com/list,BK1036.html">股吧</a>
</td>"""
res_value = r'<td .*?>\s*<a .*?>(.*?)</a>'
m_value = re.findall(res_value, txt, re.S | re.M)  # <td><span class="nickname">(字) 翔宇</span></td>
print(m_value)