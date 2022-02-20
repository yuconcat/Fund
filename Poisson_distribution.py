# -*- coding = utf-8 -*-
# @Time : 2021/1/28 18:41
# @Author : xxx
# @File : Poisson_distribution.py
# @Software : PyCharm

import math

a = [1,2,3,4,5,6,7,8,9]
b = [9,8]
for i in range(len(a)):
    for j in range(len(b)):
        if (i+1)%3!=0:
            print(a[i],b[j])
        else:
            continue