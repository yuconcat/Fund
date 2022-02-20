# -*- coding = utf-8 -*-
# @Time : 2021/1/27 15:12
# @Author : xxx
# @File : channel_line.py
# @Software : PyCharm

from Donchian_channel import Excle_r_w

N_day = 20

#计算唐安奇通道数据
def count_channel_line(path):
    up_channel = []
    down_channel = []
    centre_line = []
    list = Excle_r_w.get_column_values(path, 3)

    for i in range(1, len(list)):
        max = list[i]
        for data in list[i:i + N_day]:
            if (data >= max):
                max = data
        up_channel.append(max)

    for i in range(1, len(list)):
        min = list[i]
        for data in list[i:i + N_day]:
            if (data <= min):
                min = data
        down_channel.append(min)

    for up, down in zip(up_channel, down_channel):  #
        centre = format((up + down) / 2, '.4f')
        centre = float(centre)
        centre_line.append(centre)

    return up_channel, centre_line, down_channel

#计算最高点时间 最高点价格数据-->趋势线
def up_channel_line(path):
    n_day = 13
    up_line_time = []
    list1 = []
    list2 = []
    # ['净值日期', '单位净值', '累计净值', '日增长率', '唐通道上界', '唐通道中线', '唐通道下界', 'Bool_Up', 'MA', 'Bool_Down']
    # [    0         1           2        3          4           5           6          7        8         9     ]
    list = Excle_r_w.get_all_data(path)
    columns = len(list)

    for i in range(1, columns, n_day):
        max = list[i][2]
        for j in range(i, i + n_day):
            if j < columns:
                if (list[j][2] >= max):
                    max = list[j][2]
                    q = j
        list1.append(list[q][0])
        list2.append(max)
        up_line_time.append([list[q][0], max])

    return up_line_time, list1, list2

#计算最低点时间 最低点价格数据-->趋势线
def down_channel_line(path):
    n_day = 13
    down_line_time = []
    list1 = []
    list2 = []
    # ['净值日期', '单位净值', '累计净值', '日增长率', '唐通道上界', '唐通道中线', '唐通道下界', 'Bool_Up', 'MA', 'Bool_Down']
    # [    0         1           2        3          4           5           6          7        8         9     ]
    list = Excle_r_w.get_all_data(path)
    columns = len(list)

    for i in range(1, columns, n_day):
        min = list[i][2]
        for j in range(i, i + n_day):
            if j < columns:
                if (list[j][2] <= min):
                    min = list[j][2]
                    q = j
        list1.append(list[q][0])
        list2.append(min)
        down_line_time.append([list[q][0], min])

    return down_line_time, list1, list2

def minus_rzzl(path,num):  # 负增长率小于num
    list1 = []
    list2 = []
    list3 = []
    # ['净值日期', '单位净值', '累计净值', '日增长率', '唐通道上界', '唐通道中线', '唐通道下界', 'Bool_Up', 'MA', 'Bool_Down']
    # [    0         1           2        3          4           5           6          7        8         9     ]
    list = Excle_r_w.get_all_data(path)
    columns = len(list)
    for i in range(1, columns-1):
        if list[i][3] <= num :
            list1.append(list[i][0])
            list2.append(list[i][2])
            list3.append(list[i][3])
    return list1,list2,list3


def main(path):
    Excle_r_w.write_column_to_excle(path, 5, count_channel_line(path)[0], "唐通道上界")
    Excle_r_w.write_column_to_excle(path, 6, count_channel_line(path)[1], "唐通道中线")
    Excle_r_w.write_column_to_excle(path, 7, count_channel_line(path)[2], "唐通道下界")

    Excle_r_w.write_column_to_excle(path, 13, up_channel_line(path)[1], "最高点时间")
    Excle_r_w.write_column_to_excle(path, 14, up_channel_line(path)[2], "最高点价格")
    Excle_r_w.w_col_to_ex_by_time(path, 11, up_channel_line(path)[0], "上线")

    Excle_r_w.write_column_to_excle(path, 15, down_channel_line(path)[1], "最低点时间")
    Excle_r_w.write_column_to_excle(path, 16, down_channel_line(path)[2], "最低点价格")
    Excle_r_w.w_col_to_ex_by_time(path, 12, down_channel_line(path)[0], "下线")

    Excle_r_w.write_column_to_excle(path, 17, minus_rzzl(path,0)[0], "负增长率时间")
    Excle_r_w.write_column_to_excle(path, 18, minus_rzzl(path,0)[1], "负增长率累计净值")
    Excle_r_w.write_column_to_excle(path, 19, minus_rzzl(path,0)[2], "负增长率")

    Excle_r_w.write_column_to_excle(path, 20, minus_rzzl(path, -1)[0], "负增长率时间-1")
    Excle_r_w.write_column_to_excle(path, 21, minus_rzzl(path, -1)[1], "负增长率累计净值-1")
    Excle_r_w.write_column_to_excle(path, 22, minus_rzzl(path, -1)[2], "负增长率-1")


if __name__ == '__main__':
    Name = "招商中证白酒指数(LOF)"  # input("输入基金的名称:")
    fundcode = "161725"  # input("输入基金的代码:")
    path = "D:\\" + "基金\\" + Name + fundcode + "\\" + Name + ".xlsx"
    main(path)