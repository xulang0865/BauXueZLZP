import urllib3
from time import sleep
import requests
import json
headLoginStep1 = {'User-Agent':'qianxian/1.1.0 (iPhone; iOS 13.3.1; Scale/3.00)','Accept-Language':'zh-Hans-CN;q=1','Accept-Encoding':'gzip, deflate','Connection':'keep-alive'}
postText = {'id':1175 ,'wechatId': 0 }
url = 'https://zhixianghezi-api.zhaopin.com/youzhiqi-api/api/article/articleDetail'
session = requests.session()
jsondata = json.dumps(postText)
print(jsondata)
data1 = 'id=1175&wechatId=0'
postText1 = {'articleId' : 1175 , 'currentPage':1 , 'pageSize' : 10000}
url1 = 'https://zhixianghezi-api.zhaopin.com/youzhiqi-api/api/wechat/commentList'
postText13 = {"courseId":"1175","wechatId":0,"courseName":"湖北地区—《战“疫”重生：重构人力资源职业生涯》","courseCreateTime":1586263477000,"accountCreateTime":1581596218935,"phone":"18871878794","email":"","company":"湖北邮政集团","title":"","adress":"","companyAccount":""}
url3 = 'https://zhixianghezi-api.zhaopin.com/youzhiqi-api/api/add-course-visit-record'
for n in range(1000):
    r = session.post(url=url,headers = headLoginStep1,data = postText)
    r1 = session.post(url=url1,headers = headLoginStep1,data = postText1)
    r2 = session.post(url=url3, headers=headLoginStep1, json =postText13)
    print(r.text)
    print(r1.text)
    print(r2.text)
    sleep(0.5)

