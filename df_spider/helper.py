# -*- coding: utf-8 -*-
"""
@author: luhx
@file: helper.py
@time: 2023/4/15 9:53
@desc:
"""


def parse_value(txt):
    """
    分析数值
    :param txt:
    :return:
    """
    if txt[0] == "-" or txt[0].isdigit():
        if txt.find("%") != -1:
            return float(txt.replace("%", ""))
        elif txt.find("亿") != -1:
            return float(txt.replace("亿", "")) * 100000000
        elif txt.find("万") != -1:
            return float(txt.replace("万", "")) * 10000
        else:
            return float(txt)
    else:
        return txt


if __name__ == '__main__':
    print(parse_value("-2.79亿"))