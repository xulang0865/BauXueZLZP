import urllib3
from time import sleep
import requests
import json
headLoginStep1 = {'User-Agent':'qianxian/1.1.0 (iPhone; iOS 13.3.1; Scale/3.00)','Accept-Language':'zh-Hans-CN;q=1','Accept-Encoding':'gzip, deflate','Connection':'keep-alive'}
postText = {"courseId":"1175","wechatId":0,"courseName":"湖北地区—《战“疫”重生：重构人力资源职业生涯》","courseCreateTime":1586263477000,"accountCreateTime":1581596218935,"phone":"18871878794","email":"","company":"湖北邮政集团","title":"","adress":"","companyAccount":""}
#postText1 =
url = 'https://zhixianghezi-api.zhaopin.com/youzhiqi-api/api/add-course-visit-record'
session = requests.session()
jsondata = json.dumps(postText)
print(jsondata)
for n in range(20):
    r = session.post(url=url,headers = headLoginStep1,json = postText)
    print(r.text)
    sleep(1)

