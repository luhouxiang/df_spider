# -*- coding: utf-8 -*-
"""
@author: luhx
@file: obj.py
@time: 2023/4/14 23:51
@desc:
"""


class FinFlowItem:
    def __init__(self):
        self.serial_no: int = 0  # 序号
        self.bk_name: str = ""  # 板块名称
        self.today_zdf: float = 0.0  # 今日涨跌幅
        self.today_main_net: float = 0.0  # 今日主力净流入净额
        self.today_main_rate: float = 0.0  # 今日主力净流入净占比
        self.today_large_net: float = 0.0  # 今日超大单净流入净额
        self.today_large_rate: float = 0.0  # 今日超大单净流入净占比
        self.today_big_net: float = 0.0  # 今日大单净流入净额
        self.today_big_rate: float = 0.0  # 今日大单净流入净占比
        self.today_middle_net: float = 0.0  # 今日中单净流入净额
        self.today_middle_rate: float = 0.0  # 今日中单净流入净占比
        self.today_small_net: float = 0.0  # 今日小单净流入净额
        self.today_small_rate: float = 0.0  # 今日小单净流入净占比
        self.delegate_name: str = ""  # 今日主力净流入最大股

    def __str__(self):
        return f"serial:{self.serial_no},bk:{self.bk_name}:zdf:{self.today_zdf}," \
               f"m_net:{self.today_main_net},m_rate:{self.today_main_rate}" \
               f"l_net:{self.today_large_net},l_rate:{self.today_large_rate}" \
               f"b_net:{self.today_big_net},b_rate:{self.today_big_rate}" \
               f"m_net:{self.today_middle_net},m_rate:{self.today_middle_rate}" \
               f"s_net:{self.today_small_net},s_rate:{self.today_small_rate}" \
               f"delegate:{self.delegate_name}"

    def __repr__(self):
        return self.__str__()
