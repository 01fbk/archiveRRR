import urllib.request
import urllib.parse
import os
import datetime
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="python"
)

url = 'https://google.com/'
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
dir_name = 'g'

req = urllib.request.Request(url, headers=hdr)
response = urllib.request.urlopen(req)
savePage = response.read()

director = dir_name + "-" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")
directory = os.path.join('C:/PyCharm/archive/sites/', director)

page = "index.html"

os.mkdir(directory)
with open(directory + '/' + page, 'wb') as fp:
    fp.write(savePage)

mycursor = mydb.cursor()

sql = "INSERT INTO python (url, directory, date_added) VALUES (%s, %s, %s)"
val = (url, directory, datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"))
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")
