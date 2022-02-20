# -*- coding = utf-8 -*-
# @Time : 2021/1/28 18:42
# @Author : xxx
# @File : test.py
# @Software : PyCharm
from typing import List, Any


from Donchian_channel import Excle_r_w

# class huice:
#
#     time_buy_list = []  # 记录买入时间
#     time_sell_list = []  # 记录卖出时间
#     proportion_list = []  # 记录份额
#
#     def __init__(self, list_tow, capital, price_basic, month_complement, start_time, change):
#         self.capital = capital  # 本金
#         self.price_basic = price_basic  # 一次买入的金额基数
#         self.one_buy_price = 0  # 单次买入金额
#         self.proportion = 0  # 初始份额为0
#         self.month_complement = month_complement  # 每个月可以存入的金额
#         self.jijin = 0  # 基金里的金额
#         self.start_time = start_time  # 多少天前
#         self.change = change  # 在跌多少点时买入
#         self.list_tow = list_tow
#         self.much = 0  # 记录买入次数
#         self.total_captial = 0  # 总金额
#         self.tr_total_captial = 0  # 投入总金额
#         self.syl = 0 #收益率
#         self.jjsyl = 0 #基金收益率
#         self.sell_price = 0 #卖出金额
#
#     # 跌就买不卖
#     def first(self):
#         self.total_captital = 1000  # 记录投入总金额
#         # ['净值日期', '单位净值', '累计净值', '日增长率', '唐通道上界', '唐通道中线', '唐通道下界', 'Bool_Up', 'MA', 'Bool_Down']
#         # [    0         1           2        3          4           5           6          7        8         9     ]
#         for i in range(self.start_time, 0, -1):  # list[i][3]最后一个是none-->columns-2,第一行不要-->到0
#             if i % 21 == 0:
#                 self.capital = self.capital + self.month_complement
#                 self.total_captital = self.total_captital + self.month_complement
#                 # print("金额增加了", self.month_complement)
#
#             if (self.list_tow[i][3] < self.change):
#                 # 计算当前的金额是否足够购买
#                 self.one_buy_price = -(self.list_tow[i][3]) * self.price_basic
#                 self.capital = self.capital - self.one_buy_price
#                 # 打印可以购买的时间
#                 # print(self.list_tow[i][0], "此时间可以购买")
#                 # 判断当前的金额是否足够购买
#                 if self.capital >= 0:
#                     self.proportion = self.proportion + float(
#                         format((self.one_buy_price / self.list_tow[i][2]), ".14f"))
#                     self.proportion_list.append(self.proportion)
#                     self.time_buy_list.append(self.list_tow[i][0])
#                     self.jijin = self.proportion * self.list_tow[i][2]
#                     # print("总金额  ", self.total_captital)
#                     # print("买前本金 ", self.capital + self.one_buy_price)
#                     # print("买入时间 ", self.list_tow[i][0])
#                     # print("日增长率 ", self.list_tow[i][3])
#                     # print("买入金额基数", self.price_basic)
#                     # print("买入金额 ", self.one_buy_price)
#                     # print("买后本金 ", self.capital)
#                     # print("当前份额 ", self.proportion)
#                     # print("基金金额 ", self.jijin)
#                     # print("\n")
#                 else:
#                     self.capital = self.capital + self.one_buy_price
#         #             print("本金不够 ")
#         #             print("\n")
#         #     else:
#         #         print("未买入")
#         #         print("\n")
#         #
#         # print("投入总金额", self.total_captital)
#         # print("基金金额 ", self.jijin)
#         # print("当前份额 ", self.proportion)
#         # print("净收益  ", self.capital + self.jijin - self.total_captital)  # 基金的加上未买入的减去总金额
#
#     # 跌的天数越多，买的越多
#     def second(self):
#         count = 0  # 连跌标记
#         self.total_captital = 1000  # 记录投入总金额
#         # ['净值日期', '单位净值', '累计净值', '日增长率', '唐通道上界', '唐通道中线', '唐通道下界', 'Bool_Up', 'MA', 'Bool_Down']
#         # [    0         1           2        3          4           5           6          7        8         9     ]
#         for i in range(self.start_time, 0, -1):  # list[i][3]最后一个是none-->columns-2,第一行不要-->到0
#             if i % 21 == 0:  # 每个月存一部分钱在手上
#                 self.capital = self.capital + self.month_complement
#                 self.total_captital = self.total_captital + self.month_complement
#                 # print("金额增加了", self.month_complement)
#             if self.list_tow[i][3] < 0:
#                 count = count + 1
#                 if (self.list_tow[i][3] < self.change):
#                     # 计算当前的金额是否足够购买
#                     self.one_buy_price = self.price_basic * count * 5  # -(self.list_tow[i][3])
#                     self.capital = self.capital - self.one_buy_price
#                     # 打印可以购买的时间
#                     # print(self.list_tow[i][0], "此时间可以购买")
#                     # 判断当前的金额是否足够购买
#                     if self.capital >= 0:
#                         if count >= 1:
#                             self.proportion = self.proportion + float(
#                                 format((self.one_buy_price / self.list_tow[i][2]), ".14f"))
#                             self.proportion_list.append(self.proportion)
#                             self.time_buy_list.append(self.list_tow[i][0])
#                             self.jijin = self.proportion * self.list_tow[i][2]
#                             # print("总金额  ", self.total_captital)
#                             # print("买前本金 ", self.capital + self.one_buy_price)
#                             # print("买入时间 ", self.list_tow[i][0])
#                             # print("日增长率 ", self.list_tow[i][3])
#                             # print("count=  ", count)
#                             # print("买入金额基数", self.price_basic)
#                             # print("买入金额 ", self.one_buy_price)
#                             # print("买后本金 ", self.capital)
#                             # print("当前份额 ", self.proportion)
#                             # print("基金金额 ", self.jijin)
#                             # print("\n")
#                         else:
#                             self.capital = self.capital + self.one_buy_price
#                     else:
#                         self.capital = self.capital + self.one_buy_price
#                         # print("本金不够 ")
#                         # print("\n")
#             else:
#                 count = 0  # 标记清零
#         #         print("日增长率为正，未买入",count)
#         #         print("\n")
#         #
#         # print("投入总金额", self.total_captital)
#         # print("基金金额 ", self.jijin)
#         # print("当前份额 ", self.proportion)
#         # print("净收益  ", self.capital + self.jijin - self.total_captital)  # 基金的加上未买入的减去总金额
#
#     def third(self):
#         count = 0  # 连跌标记
#         self.total_captital = 1000  # 记录投入总金额
#         # ['净值日期', '单位净值', '累计净值', '日增长率', '唐通道上界', '唐通道中线', '唐通道下界', 'Bool_Up', 'MA', 'Bool_Down']
#         # [    0         1           2        3          4           5           6          7        8         9     ]
#         for i in range(self.start_time, 0, -1):  # list[i][3]最后一个是none-->columns-2,第一行不要-->到0
#             if i % 21 == 0:  # 每个月存一部分钱在手上
#                 self.capital = self.capital + self.month_complement
#                 self.total_captital = self.total_captital + self.month_complement
#
#             if self.list_tow[i][3] < 0:
#                 count = count + 1
#                 if (self.list_tow[i][3] < self.change):
#                     # 计算当前的金额是否足够购买
#                     self.one_buy_price = self.price_basic * count * 5
#                     self.capital = self.capital - self.one_buy_price
#                     # 打印可以购买的时间
#
#                     # 判断当前的金额是否足够购买
#                     if self.capital >= 0:
#                         if count >= 1:
#                             self.proportion = self.proportion + float(
#                                 format((self.one_buy_price / self.list_tow[i][2]), ".14f"))
#                             self.proportion_list.append(self.proportion)
#                             self.time_buy_list.append(self.list_tow[i][0])
#                             self.jijin = self.proportion * self.list_tow[i][2]
#
#                             self.tr_total_captial = self.tr_total_captial + self.one_buy_price
#                             self.jjsyl = ((self.jijin - self.tr_total_captial)/self.tr_total_captial)* 100
#                             self.syl = ((self.capital + self.jijin - self.total_captital) / self.total_captital) * 100
#
#                             print("---------------------------------------------------")
#                             print("总金额  ", self.total_captital)
#                             print("买前本金 ", self.capital + self.one_buy_price)
#                             print("买入时间 ", self.list_tow[i][0])
#                             print("日增长率 ", self.list_tow[i][3])
#                             print("count=  ", count)
#                             print("买入金额基数", self.price_basic)
#                             print("买入金额 ", self.one_buy_price)
#                             print("买后本金 ", self.capital)
#                             print("当前份额 ", self.proportion)
#                             print("投入总金额 ", self.tr_total_captial)
#                             print("基金金额 ", self.jijin)
#                             print("基金收益率  ", self.jjsyl)
#                             print("总收益率   ", self.syl)
#                             print("---------------------------------------------------")
#                             print("\n")
#                         else:
#                             self.capital = self.capital + self.one_buy_price
#                     else:
#                         self.capital = self.capital + self.one_buy_price
#                         print("此时间可以购买", self.list_tow[i][0])
#                         print("日增长率 ", self.list_tow[i][3])
#                         print("本金不够 ")
#                         print("\n")
#             else :
#                 count = 0  # 标记清零
#                 print("当前时间 ", self.list_tow[i][0])
#                 print("日增长率为正，未买入",self.list_tow[i][3])
#                 self.jijin = self.proportion * self.list_tow[i][2]
#                 self.jjsyl = ((self.jijin - self.tr_total_captial) / self.tr_total_captial ) * 100
#                 self.syl = ((self.capital + self.jijin - self.total_captital) / self.total_captital) * 100
#                 print("当前份额 ", self.proportion)
#                 print("投入总金额 ", self.tr_total_captial)
#                 print("基金金额 ", self.jijin)
#                 print("基金收益率  ", self.jjsyl)
#                 print("总收益率   ", self.syl)
#                 print("\n")
#
#                 if self.jjsyl >= 15:
#                     print("$$$$$$$$$$$$$")
#                     print("$$$$","卖出60%","$$$$")
#                     print("$$$$$$$$$$$$$")
#                     temp_proportion = self.proportion * 0.6
#                     self.sell_price = temp_proportion * self.list_tow[i][2]
#                     self.proportion = self.proportion - temp_proportion
#                     self.capital = self.capital + self.sell_price
#
#
#         print("投入总金额", self.total_captital)
#         print("基金金额 ", self.jijin)
#         print("当前份额 ", self.proportion)
#         print("净收益  ", self.capital + self.jijin - self.total_captital)  # 基金的加上未买入的减去总金额
#         print("收益率   ", self.syl)
#
#     # 计算每个count的概率
#     def compute_counts_probility(self):
#         count_list = []
#         count = 0
#         # ['净值日期', '单位净值', '累计净值', '日增长率', '唐通道上界', '唐通道中线', '唐通道下界', 'Bool_Up', 'MA', 'Bool_Down']
#         # [    0         1           2        3          4           5           6          7        8         9     ]
#         for i in range(self.start_time, 0, -1):
#             if self.list_tow[i][3] < 0:
#                 count = count + 1
#             else:
#                 count_list.append(count)
#                 count = 0
#
#         for j in range(1,7):
#             locals()['count_' + str(j)] = 0
#             for i in range(0,len(count_list)):
#                 if count_list[i] == j:
#                     locals()['count_' + str(j)] = locals()['count_' + str(j)] + 1
#
#             print("count_" + str(j) + ":",locals()['count_' + str(j)],"//",(locals()['count_' + str(j)]/len(count_list))*100 ,"%")

def onr():
    excle_path =  "D:\\基金\\全部基金.xlsx"
    name_list = Excle_r_w.get_column_values(excle_path, 2)[1:]
    fundcode_list =Excle_r_w.get_column_values(excle_path, 1)[1:]

    print(name_list[0])
    print(fundcode_list[1])
    print(str(fundcode_list[1]))






def time_change(list_tow, start_time, min_change, max_change):
    # 寻找对收益影响最大的一次买入价格与入手时间
    # locals()函数可以将字符串转换为变量名
    change = 0
    max_jijin = 0
    max_1 = 0
    total_captital = 0
    capital = 0

    for i in range(50, 600):  # 一次买入价格影响
        for j in range((min_change * 10), (max_change * 10), -1):  # 买入时机影响
            j = j / 10
            locals()['demo_' + str(i)] = huice(list_tow=list_tow, capital=1000, price_basic=i, month_complement=1000,
                                               start_time=start_time, change=j)
            locals()['demo_' + str(i)].second()
            price = locals()['demo_' + str(i)].jijin
            if max_jijin <= price:
                max_jijin = price
                max_1 = i
                total_captital = locals()['demo_' + str(i)].total_captital
                capital = locals()['demo_' + str(i)].capital
                change = j

    print("投入总金额  ", total_captital)
    print("最大基金金额", max_jijin)
    print("净收益     ", capital + max_jijin - total_captital)
    print("一次买入   ", max_1)
    print("最低入手时机", change)
    print("收益率     ", ((capital + max_jijin - total_captital) / total_captital) * 100)


if __name__ == '__main__':
    onr()
    # Name = "招商中证白酒指数(LOF)"
    # fundcode = "161725"
    # path = "D:\\" + "基金\\" + Name + fundcode + "\\" + Name + ".xlsx"
    # list_tow = Excle_r_w.get_all_data(path)  # 获得全部数据
    #
    # # # 计算每个count的概率
    # # a = huice(list_tow=list_tow, capital=1000, price_basic=187, month_complement=1000, start_time=270,
    # #           change=-1)
    # # a.compute_counts_probility()
    #
    # list_price = []
    #
    # #time_change(list_tow=list_tow, start_time=271, min_change=0, max_change=-5)
    #
    # # # 寻找一次买入价格对收益的影响
    # # for i in range(50, 500):
    # #     locals()['demo_' + str(i)] = huice(list_tow=list_tow, capital=1000, price_basic=i, month_complement=1000,
    # #                                        start_time=280, change=-2)
    # #     locals()['demo_' + str(i)].second()
    # #     price = locals()['demo_' + str(i)].jijin
    # #     list_price.append([price, i])
    # # print(list_price)
    #
    # a = huice(list_tow=list_tow, capital=1000, price_basic=187, month_complement=1000, start_time=270,change=-1)
    # a.third()


