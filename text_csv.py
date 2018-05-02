# -*- coding:utf-8 -*-
import json
import csv
with open("d:\\22.json", 'r') as f:
    gj_json = json.loads(f.read())
#print(temp)
#print(temp['beans']['carNum'])
i = 0
ii = 0
a=open(r'd:\\qqq.txt','w')
csvFile3 = open('d:\\csvFile3.csv','w', newline='') 
writer2 = csv.writer(csvFile3)

for each in gj_json['beans']:
    try:
        i = i + 1
        if each['terminalCode']:
            a.write(each['carNum']+"  "+each['terminalCode']+'\n')
            writer2.writerow([each['carNum'],each['terminalCode']])
        else:
            ii = ii + 1
            a.write(each['carNum']+'\n')
            writer2.writerow([each['carNum']])
    except Exception as err:  
        pass
a.close()
print(i)
print(ii)
