# -*- coding: gbk -*-
import requests
import re
import time
import threading
import os
if not os.path.exists("D:\DingDing\sdsss"):
    os.makedirs("D:\DingDing\sdsss")
def html(url):
    htmlcode = requests.get(url)
    rex = r'img src="(//.*jpe?g)" alt'
    img = re.findall(rex,htmlcode.text)
    x = 0
    for i in img:
        img_url = "http:%s"%i
        img_text = requests.get(img_url)
        img_name = url.split("/")[-2]+"-"+str(x)+ "."+i.split(".")[-1]
        #print url.split("/")[-2]
        with open("D:\DingDing\sdsss\\" +img_name,"ab") as f:
            f.write(img_text.content)
        print  img_name.encode('gbk') + "���سɹ�\n"
        x = x+ 1
time_start = time.time()
s = raw_input("��������ʼҳ��")
e = raw_input("���������ҳ��")
for j in range(int(s),int(e)):
    t = threading.Thread(target = html,args=("https://www.qiushibaike.com/imgrank/page/%s/"%j,))
    t.start()
    time.sleep(1)
t.join()
print time.time()-time_start
