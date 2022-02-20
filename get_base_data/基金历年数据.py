# -*- coding = utf-8 -*-
# @Time : 2021/1/22 18:01
# @Author : xxx
# @File : 基金历年数据.py
# @Software : PyCharm

import requests
import json
import re
import math
from get_base_data import leadin_in_excle, Manage_data, to_directory, use_agent_pool
from Donchian_channel import channel_line
from Bollinger_Bands import boll
from Donchian_channel import Excle_r_w
from get_base_data import detail_data_excle_to_mysql


# 获取单页的数据
def get_one_page_data(pageIndex, fundcode):
    url = 'http://api.fund.eastmoney.com/f10/lsjz'
    param = {
        'callback': 'jQuery18303949389716617069_1611321798841',
        'fundCode': fundcode,
        'pageIndex': pageIndex,
        'pageSize': '20'
    }
    headers = {
        'User-Agent': use_agent_pool.random_headers_key(),
        # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Host': 'api.fund.eastmoney.com',
        'Referer': 'http://fundf10.eastmoney.com/jjjz_%s.html' % fundcode,
    }
    response = requests.get(url=url, params=param, headers=headers, timeout=(3,7))
    # response.text

    text = re.findall('\((.*?)\)', response.text)[0]  # 提取response里面的字典--><class 'str'>
    LSJZList = json.loads(text)['Data']['LSJZList']  # 获取LSJZList里的每个字典数据--><class 'list'>

    # print('text',type(text))
    # print('LSJZList',type(LSJZList))
    # print('TotalCount',type(TotalCount))
    return LSJZList


# 获取数据的条数-->用来算页数
def get_page(fundcode):
    url = 'http://api.fund.eastmoney.com/f10/lsjz'
    param = {
        'callback': 'jQuery18303949389716617069_1611321798841',
        'fundCode': fundcode,
        'pageIndex': 1,
        'pageSize': '20'
    }
    headers = {
        'User-Agent': use_agent_pool.random_headers_key(),
        # 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
        'Host': 'api.fund.eastmoney.com',
        'Referer': 'http://fundf10.eastmoney.com/jjjz_%s.html' % fundcode,
    }
    response = requests.get(url=url, params=param, headers=headers)
    # response.text
    text = re.findall('\((.*?)\)', response.text)[0]  # 提取dict
    TotalCount = json.loads(text)['TotalCount']  # 转化为dict
    return TotalCount


def get_all_values(name, fundcode):
    page = math.ceil(get_page(fundcode) / 20)  # 向上取整
    aa = [[]] * page  # 创建2维数组，相当于创建[ []*20 ]
    flieName = "\\" + name + '.json'  #
    fp = open(path + flieName, 'w', encoding='utf-8')

    for i in range(1, page):  # 从一开始的循环
        aa[i] = get_one_page_data(i, fundcode)

    json.dump(aa, fp=fp, ensure_ascii=False)
    fp.close()
    print(name + "爬取成功")


def main():
    get_all_values(name=Name, fundcode=fundcode)
    # 获得相应的json文件
    Manage_data.get_values_from_total_json_to_single_json("FSRQ", Name, "净值日期", path)
    Manage_data.get_values_from_total_json_to_single_json("DWJZ", Name, "单位净值", path)
    Manage_data.get_values_from_total_json_to_single_json("LJJZ", Name, "累计净值", path)
    Manage_data.get_values_to_json_for__daily_growth_rate(Name, path)  # 获得日增长率数据
    leadin_in_excle.to_excle2(Name, column_name, path)



if __name__ == '__main__':
    #excle_path = "D:\\基金\\" + "全部基金" + ".xlsx"

    name_list =["招商中证白酒指数(LOF)","国泰国证有色金属行业指数(LOF)","农银汇理新能源主题","交银施罗德医药","招商医药","东方阿尔法"]#Excle_r_w.get_column_values(excle_path,2)[1:]
    #["招商中证白酒指数(LOF)","国泰国证有色金属行业指数(LOF)","农银汇理新能源主题","交银施罗德医药","招商医药","东方阿尔法"]
    fundcode_list =["161725","160221","002190","004075","000960","009644"]#Excle_r_w.get_column_values(excle_path,1)[1:]   #里面的数据不满足6位会爬不出数据
    #["161725","160221","002190","004075","000960","009644"]

    for i in range(len(name_list)):
        for j in range(len(fundcode_list)):
            if i==j:
                Name = name_list[i]
                fundcode = fundcode_list[j] #str(fundcode_list[j]).zfill(6)   #zfill方法用来给字符串前面补0,补足6位

                othername0 = "净值日期"
                othername1 = "单位净值"
                othername2 = "累计净值"
                othername3 = "日增长率"
                column_name = [othername0, othername1, othername2, othername3]

                path = "D:\\" + "基金\\" + Name + fundcode  # 创建文件夹
                to_directory.make_directory(path)

                path_excle = "D:\\" + "基金\\" + Name + fundcode + "\\" + Name + ".xlsx"

                main()
                detail_data_excle_to_mysql.connect_db("jijin", "fund", path_excle, fundcode)  # 导入sql

                #channel_line.main(path_excle)
                #boll.main(path_excle)
            else:
                continue



