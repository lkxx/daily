# -*- coding:utf-8 -*-
import json
import csv
import datetime  
start='2016-06-01'  
end='2017-01-01'  
   
datestart=datetime.datetime.strptime(start,'%Y-%m-%d')  
dateend=datetime.datetime.strptime(end,'%Y-%m-%d')  
   
while datestart<dateend:  
    datestart+=datetime.timedelta(days=1)  
    print datestart.strftime('%Y-%m-%d')  
