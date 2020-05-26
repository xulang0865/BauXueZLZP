import urllib3
from time import sleep
import requests
import json

import csv

def readCsv(path):
    infoList = []
    with open(path,"r",encoding="gbk") as f:
        #使用csv.reader读取csv文件
        allFileInfo = csv.reader(f)
        #这里读出来的是一个对象
        print(allFileInfo)
        for row in allFileInfo:  #使用for一行一行拿数据，这里拿出来的是一个个列表
            #这里可以不用一行行在函数内打印，直接把所有列表传给info
            infoList.append(row)
            #返回infoList后传回的是包含列表的列表，在外面进行for循环
        return infoList
path = r"test.csv"
info = readCsv(path)
#打印出来是【【】，【】，【】。。】包含列表的列表
for rows in info:
    headLoginStep1 = {'User-Agent':'qianxian/1.1.0 (iPhone; iOS 13.3.1; Scale/3.00)','Accept-Language':'zh-Hans-CN;q=1','Accept-Encoding':'gzip, deflate','Connection':'keep-alive'}
    postText = {'id':1175 ,'wechatId': 0 }
    url = 'https://zhixianghezi-api.zhaopin.com/youzhiqi-api/api/article/articleDetail'
    session = requests.session()
    jsondata = json.dumps(postText)
    print(jsondata)
    data1 = 'id=1175&wechatId=0'
    postText1 = {'articleId' : 1175 , 'currentPage':1 , 'pageSize' : 10000}
    url1 = 'https://zhixianghezi-api.zhaopin.com/youzhiqi-api/api/wechat/commentList'
    postText13 = {"courseId":"1175",
                  "wechatId":0,
                  "courseName":"湖北地区—《战“疫”重生：重构人力资源职业生涯》",
                  "courseCreateTime":1586263477000,
                  "accountCreateTime":1581596218935,
                  "phone":rows[1],
                  "email":"",
                  "company":rows[0],
                  "title":"","adress":"",
                  "companyAccount":""}
    url3 = 'https://zhixianghezi-api.zhaopin.com/youzhiqi-api/api/add-course-visit-record'
    for n in range(2):
        r = session.post(url=url,headers = headLoginStep1,data = postText)
        r1 = session.post(url=url1,headers = headLoginStep1,data = postText1)
        r2 = session.post(url=url3, headers=headLoginStep1, json =postText13)
        print(r.text)
        print(r1.text)
        print(r2.text)
        sleep(0.5)
    sleep(1)

