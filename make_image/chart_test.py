# -*- coding = utf-8 -*-
# @Time : 2021/3/24 14:08
# @Author : xxx
# @File : chart_test.py
# @Software : PyCharm

import numpy as np
from matplotlib import pyplot as plt


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1 = []
# 定义x轴的数据
x = list  # np.linspace(0,100,10)
# 定义y轴的数据
for i in range(len(list)):
    a = list[i] * i
    list1.append(a)
y = list1
# 制作单独的图像
plt.figure(figsize=(10, 20))  # 创建画布figure,添加参数figsize=()：设置画布的大小
plt.title("Title1")
plt.xlabel("x coordinate")  # 给x轴加描述
plt.ylabel("y coordinate")  # 给y轴加描述
# 设置坐标轴范围
plt.xlim((0, 10))
plt.ylim((0, 100))
# 设置坐标轴刻度
my_x_ticks = np.arange(0, 10, 1)
my_y_ticks = np.arange(0, 100, 1)  # 0,100的范围  10的间隔
plt.xticks(my_x_ticks)
plt.yticks(my_y_ticks)
plt.plot(x, y, color="g", linewidth=1, linestyle="-")
plt.show()  # 显示图像


# 定义x轴的数据
x = np.linspace(-1, 1, 100)  # x范围-1到1，间隔100个点
# 定义y轴的数据
y2 = x ** 3 + 100
# 制作单独的图像
plt.figure()  # 创建画布figure,添加参数figsize()：设置画布的大小
plt.title("Title2")
plt.xlabel("x coordinate")  # 给x轴加描述
plt.ylabel("y coordinate")  # 给y轴加描述
#plt.xlim((-1, 1))  # 限制x轴的显示范围
#plt.ylim((95, 100))  # 限制y轴的显示范围
# color:表示设置线的颜色
# linewidth:表示设置线的宽度
# linestyle:表示设置线的风格
plt.plot(x, y2, color="g", linewidth=2, linestyle="--")
# 替换纵坐标的标签，用level0代替之前的-1   同理替换横坐标的标签xticks
plt.yticks([95, 96, 97, 98, 99, 100], ["level0", "level1", "level2", "level3", "level4", "level5"])
plt.show()  # 显示图像


# 制作一个图像多个函数
x = np.linspace(-1, 1, 100)
# 定义y轴的数据
y1 = x * 2 + 100
y2 = x ** 3 + 100
plt.figure()
plt.title("Title3")
plt.xlabel("x coordinate")  # 给x轴加描述
plt.ylabel("y coordinate")  # 给y轴加描述
# 为两条线分别取名，这里的逗号必须要有
l1, = plt.plot(x, y1, color="r", linewidth=1, linestyle="-")
l2, = plt.plot(x, y2, color="g", linewidth=2, linestyle="--")
# handles控制图例中要说明的线
# labels为两条线分别取一个label
# loc控制图例的显示位置，一般用best，由代码为我们选择最优的位置即可
plt.legend(handles=[l1, l2], labels=["test1", "test2"], loc='best')
# 显示图像
plt.show()


# 绘制散点图
x = np.random.normal(1, 10, 500)
y = np.random.normal(1, 10, 500)
# s设置点的大小
# c是颜色
# alpha是透明度
plt.title("Title4")
plt.scatter(x, y, s=50, c='b', alpha=0.5)
plt.show()


