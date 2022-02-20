# -*- coding = utf-8 -*-
# @Time : 2021/1/28 12:51
# @Author : xxx
# @File : boll.py
# @Software : PyCharm

from Donchian_channel import Excle_r_w
import math

N_day = 20
k = 4


# 计算n日算数平均
def count_MA(path):
    MA_list = []
    list = Excle_r_w.get_column_values(path, 3)  # 读取累计净值

    for i in range(1, len(list)):
        sum = 0
        for data in list[i:i + N_day]:
            sum = data + sum
        sum = format(sum / N_day, '.4f')
        sum = float(sum)
        MA_list.append(sum)

    return MA_list


# 求方差
def count_SD(path):
    MA_list = count_MA(path)
    SD_list = []
    list = Excle_r_w.get_column_values(path, 3)

    for i in range(1, len(list)):
        sum = 0
        for data in list[i:i + N_day]:
            sum = math.pow((data - MA_list[i - 1]), 2)

        sum = sum / (N_day - 1)
        sum = math.sqrt(sum)
        sum = format(sum, '.4f')
        sum = float(sum)
        SD_list.append(sum)

    return SD_list


# bool上下线
def BU_BD(path):
    list_BU = []
    list_BD = []
    for MA, SD in zip(count_MA(path), count_SD(path)):
        list_BU.append(MA + k * SD)
        list_BD.append(MA - k * SD)
    return list_BU, list_BD


def main(path):
    Excle_r_w.write_column_to_excle(path, 8, BU_BD(path)[0], "Bool_Up")
    Excle_r_w.write_column_to_excle(path, 9, count_MA(path), "MA-20均")
    Excle_r_w.write_column_to_excle(path, 10, BU_BD(path)[1], "Bool_Down")


if __name__ == '__main__':
    Name = "招商中证白酒指数(LOF)"  # input("输入基金的名称:")
    fundcode = "161725"  # input("输入基金的代码:")
    path = "D:\\" + "基金\\" + Name + fundcode + "\\" + Name + ".xlsx"
    main()
