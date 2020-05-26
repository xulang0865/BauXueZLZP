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
print(len(info))



