# -*- coding: utf-8 -*-
"""
@author: luhx
@file: e3.py
@time: 2023/4/5 17:04
@desc: 测试xpath
"""
from lxml import etree
text = '''
<div>
    <ul>
         <li class="item-0"><a href="https://ask.hellobi.com/link1.html">first item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link2.html">second item</a></li>
         <li class="item-inactive"><a href="https://ask.hellobi.com/link3.html">third item</a></li>
         <li class="item-1"><a href="https://ask.hellobi.com/link4.html">fourth item</a></li>
         <li class="item-0"><a href="https://ask.hellobi.com/link5.html">fifth item</a>
     </ul>
 </div>
'''
html = etree.HTML(text)
result = etree.tostring(html)
print(result.decode('utf-8'))

html = etree.parse('./test.html', etree.HTMLParser())
result = etree.tostring(html)
print(result.decode('utf-8'))


result = html.xpath('//*')
[print(r) for r in result]

print("*" * 80)
result = html.xpath('//li')
print(result)
[print(r) for r in result]

print("*" * 80)
result = html.xpath('//li/a')
[print(r) for r in result]

print("*" * 80)
result = html.xpath('//li//a')
[print(r) for r in result]

print("*" * 80)
result = html.xpath('//a[@href="https://ask.hellobi.com/link4.html"]/../@class')
print(result)

print("*" * 80)
result = html.xpath('//li[@class="item-0"]')
print(result)

print("*" * 80)
result = html.xpath('//ul')
html = result[0]
result = html.xpath('//li')
print(result)
