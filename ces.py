# -*- coding:utf-8 -*-
f =open(r"C:\Users\99406\Desktop\report.txt","r")
f_copy = open(r"C:\Users\99406\Desktop\report-copy.txt","w")
f_copy.write("名字" + f.readline()[:-1] + " 总分"+" 平均分\n")
f_copy.close()
score = []
avg = []
for line in f.readlines():
    line = line.strip("\n")
    total = sum([int(i) for i in line.split(" ")[1:]])
    total_avg = sum([int(i) for i in line.split(" ")[1:]])/len([int(i) for i in line.split(" ")[1:]])
    line = line+" "+ str(total)+" "+ str(total_avg)
    score.append(line.decode('utf-8'))
score.sort(key = lambda x:x.split(" ")[10],reverse = True)
for i in range(1,12):
    sum = 0
    for j in range(len(score)):
        sum = sum + int(score[j].split(" ")[i])
    avg.append(str(sum/len(score)))
avg.insert(0,"0")
avg.insert(1,"平均")
f_copy = open(r"C:\Users\99406\Desktop\report-copy.txt","a")
for i in avg:
    f_copy.write(i+"\000") #直接将avg列表写入文件中，"平均"会成为assicc，请问是什么原因
f_copy.write("\n")
count = 1
for i in score:
    f_copy.write(str(count) + "\000" + i.encode("utf-8")+"\n")
    count +=1
f_copy.close()
f.close()
