# -*- coding = utf-8 -*-
# @Time : 2021/3/24 14:14
# @Author : xxx
# @File : test_1.py
# @Software : PyCharm

from pylab import mpl
from matplotlib import pyplot as plt

x =[15,20,25,30,35,40,45]
y =[330,345,365,405,445,450,455]
# 拟合曲线参数计算
def liner_fitting(data_x,data_y):
  size = len(data_x)
  i = 0
  sum_xy =0
  sum_y =0
  sum_x =0
  sum_sqare_x = 0
  while i<size:
    sum_xy+=data_x[i]*data_y[i]
    sum_y+=data_y[i]
    sum_x+=data_x[i]
    sum_sqare_x+=data_x[i]*data_x[i]
    i=i+1
  average_x=sum_x/size
  average_y=sum_y/size
  return_k=(size * sum_xy-sum_x*sum_y)/(size*sum_sqare_x-sum_x*sum_x)
  return_b=average_y-average_x * return_k
  return [return_k,return_b]

#曲线上相应的函数值的计算
def calculate(data_x,k,b):
  datay = []
  for x in data_x:
      datay.append(k*x +b)
  return datay
#绘制函数
def draw(data_x,data_y_new,data_y_old):
  plt.plot(data_x,data_y_new,label="拟合曲线",color="black")
  plt.scatter(data_x,data_y_old,label="离散数据")
  mpl.rcParams['font.sans-serif']= ['SimHei']
  mpl.rcParams['axes.unicode_minus'] = False
  plt.title("一元线性拟合")
  plt.legend(loc ="upper left")
  plt.show()
parameter = liner_fitting(x,y)
draw_data = calculate(x,parameter[0],parameter[1])
draw(x,draw_data,y)
