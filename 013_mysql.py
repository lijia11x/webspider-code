# -*- coding:utf-8 -*-
import pymysql

db = pymysql.connect(host='localhost', user='root', password='1234', port=3306, db='spiders')
cursor = db.cursor()
# cursor.execute('SELECT VERSION()')
# data = cursor.fetchone()
# print('DataBase Version: %s' % data)
# cursor.execute('CREATE DATABASE spiders DEFAULT CHARACTER SET utf8mb4')
# db.close()
sql = 'CREATE TABLE IF NOT EXISTS student (id VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,' \
      'age INT NOT NULL,PRIMARY KEY(id))'
cursor.execute(sql)
id = '123445'
name='NiClaus'
age = 20
insert_sql = 'INSERT INTO student(id,name,age) values(%s,%s,%s);'
try:
    cursor.execute(insert_sql, (id, name, age))
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
db.close()
