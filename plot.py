from matplotlib import pyplot as plt
from matplotlib import style
style.use('ggplot')

x=["O","E","A","B","C","D","F"]
y=[0,0,0,0,0,0,0]

x1=["O","E","A","B","C","D","F"]
y1=[0,0,0,0,0,0,0]

x2=["O","E","A","B","C","D","F"]
y2=[0,0,0,0,0,0,0]

f1=open("2013_res.txt",'r')
s1=f1.readline().strip(",")
s1=s1.split(",")

while True:
    line=f1.readline()
    if not line:
        break
    line=line.strip(",")
    line=line.split(",")
    if line[1][0]=="O":
        y[0]=y[0]+1
    elif line[1][0]=="E":
        y[1]=y[1]+1
    elif line[1][0]=="A":
        y[2]=y[2]+1
    elif line[1][0]=="B":
        y[3]=y[3]+1
    elif line[1][0]=="C":
        y[4]=y[4]+1
    elif line[1][0]=="D":
        y[5]=y[5]+1
    elif line[1][0]=="F":
        y[6]=y[6]+1


plt.plot(x,y,'g',label='2013_BATCH',linewidth=5)

f2=open("2014_res.txt",'r')
s1=f2.readline().strip(",")
s1=s1.split(",")

while True:
    line=f2.readline()
    if not line:
        break
    line=line.strip(",")
    line=line.split(",")
    if line[1][0]=="O":
        y1[0]=y1[0]+1
    elif line[1][0]=="E":
        y1[1]=y1[1]+1
    elif line[1][0]=="A":
        y1[2]=y1[2]+1
    elif line[1][0]=="B":
        y1[3]=y1[3]+1
    elif line[1][0]=="C":
        y1[4]=y1[4]+1
    elif line[1][0]=="D":
        y1[5]=y1[5]+1
    elif line[1][0]=="F":
        y1[6]=y1[6]+1

plt.plot(x1,y1,'c',label='2014_BATCH',linewidth=5)

f3=open("2015_res.txt",'r')
s1=f3.readline().strip(",")
s1=s1.split(",")

while True:
    line=f3.readline()
    if not line:
        break
    line=line.strip(",")
    line=line.split(",")
    if line[1][0]=="O":
        y2[0]=y2[0]+1
    elif line[1][0]=="E":
        y2[1]=y2[1]+1
    elif line[1][0]=="A":
        y2[2]=y2[2]+1
    elif line[1][0]=="B":
        y2[3]=y2[3]+1
    elif line[1][0]=="C":
        y2[4]=y2[4]+1
    elif line[1][0]=="D":
        y2[5]=y2[5]+1
    elif line[1][0]=="F":
        y2[6]=y2[6]+1

plt.plot(x2,y2,'r',label='2015_BATCH',linewidth=5)
f1.close()
f2.close()
f2.close()
plt.title("Results of MCS(401)")
plt.ylabel('NO. OF STUDENTS')
plt.xlabel('GRADES')
plt.legend()
plt.grid(True,color='k')
plt.show()
