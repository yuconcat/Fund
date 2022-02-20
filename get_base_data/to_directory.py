# -*- coding = utf-8 -*-
# @Time : 2021/1/25 20:18
# @Author : xxx
# @File : to_directory.py
# @Software : PyCharm

import os


def make_directory(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  文件夹创建成功  ---")
    else:
        print("---  文件夹已存在  ---")
