import requests
import re
import time
import threading
import os
if not os.path.exists("D:\DingDing\sdsss"):
    os.makedirs("D:\DingDing\sdsss")
def html(url):
    htmlcode = requests.get(url)
    rex = r'img src="(//.*jpe?g)" alt'# r'src="(.+?\.jpe?g)" alt='
    img = re.findall(rex,htmlcode.text)
    x = 0
    for i in img:
        img_url = "http:%s"%i
        img_text = requests.get(img_url)
        #print url.split("/")[-2]
        with open("D:\DingDing\sdsss\\" +url.split("/")[-2]+"-"+str(x)+ "."+i.split(".")[-1],"ab") as f:
            f.write(img_text.content)
        x = x+ 1
time_start = time.time()
for j in range(1,11):
    t = threading.Thread(target = html,args=("https://www.qiushibaike.com/imgrank/page/%s/"%j,))
    t.start()
    time.sleep(1)
    #t.join()
print time.time()-time_start
