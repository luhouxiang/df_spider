# -*- coding: utf-8 -*-
"""
@funcs: 全局环境变量，所有配置及全局变量最终集成到这里
"""
import json
import os
import platform
from kds_util.user_logbook import user_log as logger
from kds_util.mysql_database import PyMySql


class Envs:
    version: str = ""  # 新版本
    mysql_config = ""
    mysql = None


class JsonConf:
    def __init__(self, file_name):
        self.file_name = file_name
        self._data = self.load_file(file_name)

    def get(self, arge):
        return self._data[arge]

    def load_file(self, file_name):
        if not os.path.exists(file_name):
            return {}
        with open(file_name, encoding="utf-8") as json_file:
            try:
                data = json.load(json_file)
            except Exception as e:
                print(e)
                data = {}
        return data


def init_envs():
    if platform.system().lower() == 'windows':
        config_path = "../etc"
    else:
        config_path = "/opt/kds/work/etc"
    f = JsonConf(f"{config_path}/df_config.json")
    Envs.mysql_config = f.get("mysql_config")
    Envs.mysql = PyMySql(f"pymysql://root:Zhao123@Lu123@120.79.221.160:3306/dfdb?charset=utf8")
    return


init_envs()
