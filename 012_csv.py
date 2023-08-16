# -*- coding:utf-8 -*-
import csv

# with open('data.csv', 'w+', encoding='utf-8') as f:
#     filewriter = csv.writer(f, delimiter=' ')
#     filewriter.writerows([['id', 'name', 'age'], [10001, 'Bob', 18], [10002, 'Lily', 15], [10003, 'Eric', 30]])

import pandas as pd

# with open('data.csv', 'w+', encoding='utf-8') as f:
#     fieldsname = ['id', 'name', 'age']
#     filewriter = csv.DictWriter(f, fieldnames=fieldsname)
#     filewriter.writeheader()
#     filewriter.writerows([{'id': "10001", 'name': "Bob", 'age': "18"}, {'id': "10002", 'name': "Lily", 'age': "15"},
#                           {'id': "10003", 'name': "Eric", 'age': "30"}])
#

data = [{'id': "10001", 'name': "Bob", 'age': "18"}, {'id': "10002", 'name': "Lily", 'age': "15"},
                          {'id': "10003", 'name': "Eric", 'age': "30"}]

df = pd.DataFrame(data)
df.to_csv('data.csv', index=False)