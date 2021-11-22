import re
import requests,json
from bs4 import BeautifulSoup
import os,time
w=0
with open("file.txt","r") as f:
    res = f.read()
soup = BeautifulSoup(res,'html.parser')
title_sum = soup.find_all("div",class_="type02_s004 clearfix")
for i in title_sum:
    main = i.div.h4.text
    main  = main.replace("/","_")
    main2_list = i.find_all("tr")
    for x  in main2_list:
        main2 = x.th.h5.text
        main2= main2.replace("/","_")
        if(w<232):
            w=w+1
            continue
        else:
            os.system("mkdir ./data/"+str(main)+"_"+str(main2))
            main3 = x.find_all("li")
            for j in main3:
                href = j.text
                if(href==""):
                    continue
                else:
                    href=j.a["href"]
                    text =j.a.text
                    text = text.replace("/","_")
                    # print(href)
                    print(main2+">"+text)
                    url = requests.get(href)
                    time.sleep(3)
                    soup = BeautifulSoup(url.text,'html.parser')
                    msg =soup.find_all("div",class_="msg")
                    newlist = [a.h4.text for a in msg]
                    os.chdir("data/"+str(main)+"_"+str(main2))

                    a =str(text)+".txt"
                    with open(a,"w+") as f:
                        f.write(str(newlist))
                    os.chdir("../../")
        # print(str(main2)+">"+str(main3))
    # main1 =  i.tr.th.h5.text
        # print(main+">"+main2)
        # main3 = i.tr.td.ul
        # main3 =main3.find_all("li") 

        # for j in main3:
        #     href = j.text
        #     if(href==""):
        #         continue
        #     else:
        #         href=j.a["href"]
        #         text = j.text
        #         print(href)
        #         print(text)
                # url = requests.get(href)
                # time.sleep(3)
                # soup = BeautifulSoup(url.text,'html.parser')
                # msg =soup.find_all("div",class_="msg")
                # newlist = [a.h4.text for a in msg]
                # os.chdir("data/"+str(main)+"_"+str(x.text))

                # a =str(text)+".txt"
                # with open(a,"w+") as f:
                #     f.write(str(newlist))
                # os.chdir("../../")
