# -*- coding:utf-8 -*-
import json
import csv
import datetime

def dt1():
    start='2016-06-01'  
    end='2016-07-01'  
       
    datestart=datetime.datetime.strptime(start,'%Y-%m-%d')  
    dateend=datetime.datetime.strptime(end,'%Y-%m-%d')  
       
    while datestart<dateend:  
        datestart+=datetime.timedelta(days=1)  
        print datestart.strftime('%Y-%m-%d')  

   
def dt():  
    begin = datetime.date(2014,6,1)  
    end = datetime.date(2014,7,7)  
    for i in range((end - begin).days+1):  
        day = begin + datetime.timedelta(days=i)  
        print str(day)  
