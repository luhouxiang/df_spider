# -*- coding: utf-8 -*-
"""
@author: luhx
@file: main.py
@time: 2023/4/15 16:11
@desc:
"""
from kds_util.user_logbook import user_log as logger, init_logger
from fin_flow import FinFlow


if __name__ == '__main__':
    init_logger("../log", "df_spider")
    fina = FinFlow()
    fina.parse_table()
    logger.info("work end.")
