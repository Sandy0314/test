#!/usr/bin/env python
# coding: utf-8

# In[2]:


import mysql.connector
import requests
from bs4 import BeautifulSoup
import random

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="password",
    database = 'sql_crawing'
)
cursor = connection.cursor() #連線
cursor.execute('SET SQL_SAFE_UPDATES=0;')
for num in range(1,20):
    content=str()
    temp = random.randint(1608393,1923844)
    url='https://news.ltn.com.tw/news/politics/breakingnews/'+str(temp)
    web = requests.get(url)                        # 取得網頁內容
    soup = BeautifulSoup(web.text, "html.parser")  # 轉換成標籤樹
    title = soup.title.string                      # 取得 title
    p = soup.find_all("p")
    for i in p:
        content+=i.getText()
    sql="INSERT INTO `news` VALUES(%d,'%s','%s')"%(num,title,content)
    cursor.execute(sql)
    """cursor.execute('SELECT * FROM `news`;')
    records = cursor.fetchall()
    for r in records:
        print(r)"""
cursor.close()
connection.commit()
connection.close()


# In[ ]:





# In[ ]:




