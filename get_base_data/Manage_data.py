# -*- coding = utf-8 -*-
# @Time : 2021/1/23 18:45
# @Author : xxx
# @File : Manage_data.py
# @Software : PyCharm

import json


def get_values_from_total_json_to_single_json(key, Name, othername, path):  # key要找的关键字 , fp json文件
    w_flieName = "\\" + Name + "_" + othername + "_values.json"
    flieName = "\\" + Name + ".json"
    read_fp = open(path + flieName, 'rb')
    write_fp = open(path + w_flieName, 'w', encoding='utf-8')

    fileJson = json.load(read_fp)
    # print(type(fileJson))

    AddList = []
    for i in range(1, len(fileJson)):
        for trait in fileJson[i]:
            AddList.append(trait[key])

    json.dump(AddList, fp=write_fp, ensure_ascii=False)
    write_fp.close()
    read_fp.close()
    #print(Name + "_" + othername + "导入json成功")


# 计算出日增长率写入json文件
def get_values_to_json_for__daily_growth_rate(Name, path):
    othername0 = "累计净值"
    othername1 = "单位净值"
    othername2 = "日增长率"
    flieName0 = "\\" + Name + "_" + othername0 + "_values.json"
    flieName1 = "\\" + Name + "_" + othername1 + "_values.json"
    read_fp0 = open(path + flieName0, 'rb')
    read_fp1 = open(path + flieName1, 'rb')
    fileJson0 = json.load(read_fp0)
    fileJson1 = json.load(read_fp1)

    w_flieName = "\\" + Name + "_" + othername2 + "_values.json"
    write_fp = open(path + w_flieName, 'w', encoding='utf-8')

    AddList = []
    for i in range(0, len(fileJson0) - 1):
        if (len(fileJson0[i])==0):    #防止其中某个字符串为空
            a=0
        else:
            a = float(fileJson0[i])

        if (len(fileJson0[i + 1])==0):
            aa==0
        else:
            aa = float(fileJson0[i + 1])

        b = float(fileJson1[i])
        sum = round(((a - aa) / b) * 100, 3)
        AddList.append(str(sum))

    json.dump(AddList, fp=write_fp, ensure_ascii=False)
    write_fp.close()
    read_fp0.close()
    read_fp1.close()
    #print(Name + "_" + othername2 + "导入json成功")
