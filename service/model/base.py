#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : base.py
# @Author: Cedar
# @Date  : 2019/12/21
# @Desc  :


import configparser
import os
import redis
import hashlib


# 用os模块来读取
cur_path = os.path.dirname(os.path.realpath(__file__))
cfg_path = os.path.join(cur_path, '..', "config.ini")  # 读取到本机的配置文件
# 调用读取配置模块中的类
conf = configparser.RawConfigParser()
conf.read(cfg_path, encoding="utf-8")

# redis配置
redis_connect_params = dict(
    host=conf.get("redis", "host"),
    port=int(conf.get("redis", "port")),
    db=conf.get("redis", "db"),
    password=conf.get("redis", "password"),
    decode_responses=True  # 返回解码结果
)
new_task_set_key_pattern = conf.get("redis", "new_task_set_key_pattern")
running_task_set_key_pattern = conf.get("redis", "running_task_set_key_pattern")
items_dict_key_pattern = conf.get("redis", "items_dict_key_pattern")
twitter_guest_token_sorted_set_pattern = conf.get("redis", "twitter_guest_token_sorted_set_pattern")
pool = redis.ConnectionPool(**redis_connect_params)
redis_help = redis.Redis(connection_pool=pool)


def get_token(md5str):
    # md5str = "abc"
    # 生成一个md5对象
    m1 = hashlib.md5()
    # 使用md5对象里的update方法md5转换
    m1.update(md5str.encode("utf-16LE"))
    token = m1.hexdigest()
    return token


class BaseExtractor:
    """
    基类，规定输入输出，对外接口
    调用get_page_content_by_request可根据page_type返回相应结果
    """

    def __init__(self, request_params=None):
        # config参数
        self.config = conf
        # 默认值
        self.agent_type = ''
        self.page_type = ''
        self.html_code = '0'
        # self.target_id = ''
        self.target_express = ''
        self.target_list = ''        # 逗号隔开
        self.page_count = 0
        self.page_url = ''
        # 传入request_params
        # 传入的参数必须是self.__dict__规定的keys
        if request_params:
            for param in request_params:
                if param in self.__dict__.keys():
                    self.__dict__[param] = request_params[param]


if __name__ == '__main__':
    aa = BaseExtractor()
    configs = aa.config.get("chromedriver", "user_data_dir")
    print(configs)
