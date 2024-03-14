#https://youtu.be/FiHcS5OYLRA?list=PLlvFEn0NKwXIImY5-7YYc6wYqmSBdXYLZ
import numpy as np 
import pandas as pd
students = ({'std_id':[1000,1001,1002,1003],
            'std_name':['michel', 'rita','josephine','georges'],
            'marks':[480,245,777,555],
            'average':[80,67,23,94]
             }) 
df = pd.DataFrame(students)
print(df)
std_name1 = ['michel','rita','josephine','georges' ]
average = [90,65,87,90,]
x = pd.Series(data = std_name1,index=average)
# print(x)
# print(x['rita'])#output average for rita
print(x[65])#output rita 
print(x[87])#search for has average of 87
#https://youtu.be/FiHcS5OYLRA?list=PLlvFEn0NKwXIImY5-7YYc6wYqmSBdXYLZ&t=234