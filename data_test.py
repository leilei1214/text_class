import re
import requests,json
from bs4 import BeautifulSoup
url = requests.get("https://www.books.com.tw/web/sys_bbotm/books/190103/?loc=P_0001_3_744")
soup = BeautifulSoup(url.text,'html.parser')
msg =soup.find_all("div",class_="msg")
newlist = [x.h4.text for x in msg]
print(newlist)
