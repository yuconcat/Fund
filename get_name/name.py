# -*- coding = utf-8 -*-
# @Time : 2021/6/27 16:48
# @Author : xxx
# @File : name.py
# @Software : PyCharm
import requests
import time
import pandas as pd
from get_base_data import fund_name_excle_to_mysql
def get_jijin_name():
    num = []
    name = []
    today_price = []
    yesterday_price = []
    day_value = []
    day_value_rate = []
    subscription_status = []
    service_charge = []

    q = 0
    i = 0
    for j in range(1, 2):   #总共49页
        url = f'http://fund.eastmoney.com/Data/Fund_JJJZ_Data.aspx?t=1&lx=1&letter=&gsid=&text=&sort=zdf,desc&page={j},200&dt=1597126258333&atfc=&onlySale=0'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER'
        }
        resp = requests.get(url, headers=headers).text
        str_ = resp[102:]
        list1 = eval(str_.split(",count")[0])

        i = i + q
        for i in range(len(list1)):
            # 1、基金代码号
            num.append(list1[i][0])
            # 2、股票名称
            name.append(list1[i][1])
            # 3、今日基金净额
            number = float(list1[i][3])
            today_price.append(number)
            # 4、昨日基金净额
            number = float(list1[i][5])#5
            yesterday_price.append(number)
            # 5、日增长值
            number = float(list1[i][3])-float(list1[i][5])
            day_value.append(number)
            # 6、日增长率
            number = float(list1[i][8])#8
            day_value_rate.append(number)
            # 7、申购状态
            subscription_status.append(list1[i][10])#9
            # 9、手续费
            service_charge.append(list1[i][17])
            q = i

    df = pd.DataFrame()
    df['基金代码'] = num
    df['基金名称'] = name
    df['今日单位净值'] = today_price
    df['昨日单位净值'] = yesterday_price
    df['日增长值'] = day_value
    df['日增长率\n%'] = day_value_rate
    df['申购状态'] = subscription_status
    df['手续费'] = service_charge


    try:
        df.to_excel(f'D:\\基金\\全部基金.xlsx', sheet_name="Sheet", index=None, encoding='utf-8')


    except Exception as e:
        print(e)

    print("爬好了")
if __name__ == '__main__':
    get_jijin_name()
    dbname = "jijin"
    Name = "全部基金"
    fundcode = "000000"
    tablename = "fundname"
    exclepath = "D:\\基金\\" + Name + ".xlsx"
    fund_name_excle_to_mysql.connect_db(dbname,tablename,exclepath,fundcode)




