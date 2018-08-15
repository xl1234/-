# -*- coding:utf-8 -*-
f =open(r"C:\Users\Administrator\Desktop\report.txt","r")
f_copy = open(r"C:\Users\Administrator\Desktop\report-copy.txt","w")
f_copy.write("名字" + f.readline()[:-1] + " 总分"+" 平均分\n")
f_copy.close()
score = []
avg = []
for line in f.readlines():
    line = line.strip("\n")
    line = line.split(" ")
    total = sum([int(i) for i in line[1:]])
    total_avg = sum([int(i) for i in line[1:]])/len([int(i) for i in line[1:]])
    line.append(str(total))
    line.append(str(total_avg))
    score.append(line)
score.sort(key = lambda x:x[10],reverse = True)
for i in range(1,12):
    sum = 0
    for j in range(len(score)):
        sum = sum + int(score[j][i])
    avg.append(str(sum/len(score)))
avg.insert(0,"0")
avg.insert(1,"平均")
for i in range(0,len(score)):
    for j in range(1,len(score[0])):
        if int(score[i][j]) < 60 :
            score[i][score[i].index(score[i][j])] = "不及格"
f_copy = open(r"C:\Users\Administrator\Desktop\report-copy.txt","a")
for i in avg:
    f_copy.write(i+"\000") #直接将avg列表写入文件中，"平均"会成为assicc，请问是什么原因
f_copy.write("\n")
count = 1
for i in score:
    i.insert(0,str(count))
    for j in range(len(i)):
        f_copy.write(i[j]+'\000')
    f_copy.write("\n")
    count +=1
f_copy.close()
f.close()
