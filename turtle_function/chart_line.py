# -*- coding = utf-8 -*-
# @Time : 2021/2/14 10:47
# @Author : xxx
# @File : chart_line.py
# @Software : PyCharm

from Donchian_channel import Excle_r_w
import turtle
import math
from construction import quick_sort


class chart:
    dial = 10  # 单位刻度长度

    def __init__(self, x_list, y_list):
        self.x_list = x_list
        self.y_list = y_list
        self.width = len(x_list) * self.dial * 1.01
        self.height = 880
        # 设置原点在画布的位置
        self.x0 = -(self.width / 2) + self.dial * 2
        self.y0 = -(self.height / 3)
        # 确定值域的范围
        y_min, y_max = quick_sort.Quicksort_get_min_max(y_list)
        self.minus = math.ceil(y_max - y_min) + 1
        self.l = self.minus * self.dial * (16)  # 设置y轴长度

    # 画坐标轴
    def Cartesian_coordinates(self):

        turtle.screensize(self.width, self.height)  # 设置画布大小
        turtle.setup(width=1910, height=795, starty=0, startx=0)  # 设置窗体大小
        turtle.pensize(1)  # 设置画笔的宽度；
        turtle.pencolor("black")  # 没有参数传入，返回当前画笔颜色，传入参数设置画笔颜色，可以是字符串如"green", "red", 也可以是RGB 3 元组。
        turtle.speed(0)  # 设置画笔移动速度，画笔绘制的速度范围(0, 10]整数，数字越大越快 ,0最快
        turtle.delay(0)
        turtle.hideturtle()  # 隐藏方向
        # 画x轴
        turtle.penup()
        turtle.goto(self.x0, self.y0)  # 到原点
        turtle.pendown()
        turtle.forward(len(self.x_list) * self.dial)
        # 画y轴
        turtle.penup()
        turtle.goto(self.x0, self.y0)  # 到原点
        turtle.pendown()
        turtle.left(90)  # 向上
        turtle.forward(self.l)

        turtle.goto(self.x0, self.y0)  # 到原点
        # x轴刻度信息
        for i in range(len(self.x_list)):
            xi = self.x0 + self.dial * (i + 1)  # 在(1,0)开始画
            yi = self.y0

            turtle.penup()
            turtle.goto(xi, yi)
            turtle.pendown()
            turtle.forward(5)
            # 日期竖向展示
            j = 1
            for q in self.x_list[i][2:]:
                turtle.penup()
                turtle.goto(xi, yi - j * 10 - self.dial / 2)
                turtle.pendown()
                turtle.write(arg=q, align="center", move=False)
                j = j + 1

        turtle.penup()
        turtle.goto(self.x0, self.y0)  # 到原点
        turtle.pendown()
        turtle.right(90)  # 向右

        # y轴刻度信息
        for i in range(self.minus + 1):
            xi = self.x0
            yi = self.y0 + (self.l / self.minus) * i
            turtle.penup()
            turtle.goto(xi, yi)
            turtle.pendown()
            turtle.forward(5)

            turtle.penup()
            turtle.goto(xi - self.minus, yi - 5)
            turtle.pendown()
            turtle.write(arg=str(i), align="center", move=False)

    # 画折线图
    def contunious_line_chart(self, x_data_list, y_data_list):
        # 画折线
        turtle.penup()
        for i in range(len(x_data_list)):
            xi = self.x0 + self.dial * (i + 1)
            yi = self.y0 + (self.l / self.minus) * y_data_list[i]
            turtle.goto(xi, yi)
            turtle.pendown()
        # 把该点的信息打印
        # 把long_data点的信息打印
        turtle.penup()
        turtle.color("gray")
        for i in range(len(x_data_list)):
            xi = self.x0 + self.dial * (i + 1)
            yi = self.y0 + (self.l / self.minus) * y_data_list[i]
            # 时间竖向展示
            j = 1
            for q in reversed(str(x_data_list[i][-5:])):
                turtle.penup()
                turtle.goto(xi, yi + j * 10 + self.dial)
                turtle.pendown()
                turtle.write(arg=q, align="center", move=False)
                j = j + 1

            # 标记点位
            turtle.penup()
            turtle.color("green")
            turtle.goto(xi, yi - 9)
            turtle.pendown()
            turtle.write(arg="*", move=False, align="center")

            # 标记累计净值
            turtle.penup()
            turtle.color("gray")
            # 净值竖向展示
            j = 1
            for q in reversed(str(y_list[i])):
                turtle.penup()
                turtle.goto(xi, self.y0 + j * 10 + self.dial / 10)  # j*10-->数字间隔
                turtle.pendown()
                turtle.write(arg=q, align="center", move=False)
                j = j + 1
            turtle.penup()

    # 画通道线
    def contunious_line_with_child_chart(self, x_long_data_list, x_short_data_list, y_short_data_list, color):
        # 画折线-->short data
        turtle.penup()
        temp = 0
        turtle.color(color)
        for i in range(len(x_short_data_list)):
            for j in range(temp, len(x_long_data_list)):
                if x_long_data_list[j] == x_short_data_list[i]:
                    xi = self.x0 + self.dial * (temp + 1)
                    yi = self.y0 + (self.l / self.minus) * y_short_data_list[i]
                    turtle.goto(xi, yi)
                    turtle.pendown()
                    temp = temp + 1
                    break
                else:
                    temp = temp + 1

    def scatter(self, x_long_data_list, x_short_data_list, y_short_data_list, color):
        turtle.penup()
        temp = 0
        turtle.color(color)
        for i in range(len(x_short_data_list)):
            for j in range(temp, len(x_long_data_list)):
                if x_long_data_list[j] == x_short_data_list[i]:
                    xi = self.x0 + self.dial * (temp + 1)
                    yi = self.y0 + (self.l / self.minus) * y_short_data_list[i]
                    turtle.goto(xi, yi)
                    turtle.pendown()
                    turtle.write(arg="0", move=False, align="center")
                    temp = temp + 1
                    turtle.penup()
                    break
                else:
                    temp = temp + 1


if __name__ == '__main__':
    Name = "招商中证白酒指数(LOF)"
    fundcode = "161725"
    path = "D:\\" + "基金\\" + Name + fundcode + "\\" + Name + ".xlsx"
    x_list = Excle_r_w.get_column_values(path, 1)[1:]
    y_list = Excle_r_w.get_column_values(path, 3)[1:]
    image = chart(x_list=x_list, y_list=y_list)
    image.Cartesian_coordinates()
    image.contunious_line_chart(x_list, y_list)

    # x_short_list1 = Excle_r_w.get_column_values(path, 13)[1:]
    # y_short_list1 = Excle_r_w.get_column_values(path, 14)[1:]
    # togndao.contunious_line_with_child_chart(x_list, x_short_list1, y_short_list1,"red")
    # x_short_list2 = Excle_r_w.get_column_values(path, 15)[1:]
    # y_short_list2 = Excle_r_w.get_column_values(path, 16)[1:]
    # togndao.contunious_line_with_child_chart(x_list,x_short_list2,y_short_list2,"green")

    # rzzl_time_list = Excle_r_w.get_column_values(path, 17)[1:]
    # rzzl_list = Excle_r_w.get_column_values(path, 18)[1:]
    # image.scatter(x_list, rzzl_time_list, rzzl_list, "purple")

    rzzl_time_list = Excle_r_w.get_column_values(path, 20)[1:]
    rzzl_list = Excle_r_w.get_column_values(path, 21)[1:]
    image.scatter(x_list, rzzl_time_list, rzzl_list, "purple")

    turtle.mainloop()
