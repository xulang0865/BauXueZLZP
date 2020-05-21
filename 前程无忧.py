import requests
import csv
requests.packages.urllib3.disable_warnings()
str1 = ""
import datetime
#无忧爬虫
def writerCsv(path, data):  # 目标path文件，写入data数据，data为包含列表的列表，以追加的方式
    with open(path, "a", newline="") as f:
        writer = csv.writer(f)
        for rowData in data:
            print("rowData = ", rowData)
            writer.writerow(rowData)

def list_get(L,i,v=None):
    try:
        num = L[i]
        return num
    except:
        return "None"
for n in range(1,30):
    r = requests.get('https://search.51job.com/list/180200,000000,0000,00,9,99,%25E9%2594%2580%25E5%2594%25AE,2,'+ str(n)+'1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=',verify = False)
    r.encoding = 'gbk'
    str1 = str1 + r.text
print(str1)
import re
comment = re.compile(r'<div class="el">(.*?)</div>', re.DOTALL)
list1 = comment.findall(str1)
print(list1)
f = open('out.csv','a')
writeTmp = []
for n in list1:
    tmplist = []
    comName = list_get(re.findall('<span class="t2"><a target="_blank" title="(.*?)"',n),0)
    comZw = list_get(re.findall('<a target="_blank" title="(.*?)"',n),0)
    comCity = list_get(re.findall('<span class="t3">(.*?)</span>',n),0)
    comMon = list_get(re.findall('<span class="t4">(.*?)</span>',n),0)
    comDate = list_get(re.findall('<span class="t5">(.*?)</span>',n),0)
    tmplist = [comCity,comName,comZw,comMon,comDate]
    writeTmp.append(tmplist)
print(writeTmp)
time_stamp = datetime.datetime.now()
date1 = time_stamp.strftime('%H%M%S')
writerCsv('%s.csv'%date1,writeTmp)
