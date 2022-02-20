# -*- coding = utf-8 -*-
# @Time : 2021/2/4 10:32
# @Author : xxx
# @File : quick_sort.py
# @Software : PyCharm

'''非递归版本 （区别仅为Qsort方法，使用栈来保存中间结果），python3 执行
'''
import copy

def swap(lst, left, right):
    lst[left], lst[right] = lst[right], lst[left]


def paritition(lst, left, right):
    key = lst[left]
    while left < right:
        if left < right and key <= lst[right]:
            right = right - 1
        swap(lst, left, right)

        if left < right and lst[left] <= key:
            left = left + 1
        swap(lst, left, right)

    return left


def Qsort(lst, left, right):
    piviots = [(left, right)]
    while len(piviots) > 0:
        piviot = piviots.pop(0)
        if piviot[0] < piviot[1]:
            piviot_num = paritition(lst, piviot[0], piviot[1])

            if piviot_num - 1 > piviot[0]:
                piviots.append((piviot[0], piviot_num-1))

            if piviot_num + 1 < piviot[1]:
                piviots.append((piviot_num+1, piviot[1]))

    return lst


def Quicksort_get_list(lst0):
    lst = copy.deepcopy(lst0)
    Qsort(lst, 0, len(lst) - 1)
    return lst


def Quicksort_get_min_max(lst0):
    lst = copy.deepcopy(lst0)
    a_list = Qsort(lst, 0, len(lst) - 1)
    return a_list[0],a_list[-1]


if __name__ == "__main__":
    ll = [1, 20, 3, 50, 40, 70, 23, 100, 23]
    Quicksort_get_list(ll)
    print(ll)