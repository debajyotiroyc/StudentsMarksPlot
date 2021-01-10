f=open("2013_res.txt",'r')
s=f.readline()
s=s.strip(",")
l=s.split(",")
d=dict.fromkeys(l[1:11],0)
d1=dict.fromkeys(l[1:11],0)
d2=dict.fromkeys(l[1:11],0)
while True:
    line=f.readline()
    if not line:
        break
    line=line.strip(",")
    line=line.split(",")
    line=line[1:11]
    k=1
    for i in line:
        if i[0]=="O":
            d[l[k]]=d[l[k]]+1
            d1[l[k]] = d1[l[k]] + 1
        elif i[0]=="F":
            d2[l[k]] = d2[l[k]] + 1
        k=k+1
max=0
n=""
for x,y in d.items():
    if y>max:
        max=y
        n=x
print(" FOR YEAR 2013 BATCH:")
print("THE SUBJECT WITH MOST 'O' IS: ",n)
print("NO. OF STUDENTS WHO RECEIVED 'O' ARE :",max)


f1=open("2014_res.txt",'r')
s=f1.readline()
s=s.strip(",")
l=s.split(",")
d=dict.fromkeys(l[1:11],0)
while True:
    line=f1.readline()
    if not line:
        break
    line=line.strip(",")
    line=line.split(",")
    line=line[1:11]
    k=1
    for i in line:
        if i[0] == "O":
            d[l[k]] = d[l[k]] + 1
            d1[l[k]] = d1[l[k]] + 1
        elif i[0] == "F":
            d2[l[k]] = d2[l[k]] + 1

        k=k+1
max=0
n=""
for x,y in d.items():
    if y>max:
        max=y
        n=x
print(" FOR YEAR 2014 BATCH:")
print("THE SUBJECT WITH MOST 'O' IS: ",n)
print("NO. OF STUDENTS WHO RECEIVED 'O' ARE :",max)

f2=open("2015_res.txt",'r')
s=f2.readline()
s=s.strip(",")
l=s.split(",")
d=dict.fromkeys(l[1:11],0)
while True:
    line=f2.readline()
    if not line:
        break
    line=line.strip(",")
    line=line.split(",")
    line=line[1:11]
    k=1
    for i in line:
        if i[0] == "O":
            d[l[k]] = d[l[k]] + 1
            d1[l[k]] = d1[l[k]] + 1
        elif i[0] == "F":
            d2[l[k]] = d2[l[k]] + 1

        k=k+1
max=0
n=""
for x,y in d.items():
    if y>max:
        max=y
        n=x
print(" FOR YEAR 2015 BATCH:")
print("THE SUBJECT WITH MOST 'O' IS: ",n)
print("NO. OF STUDENTS WHO RECEIVED 'O' ARE :",max)

max=0
n=""
for x,y in d1.items():
    if y>max:
        max=y
        n=x
print(" FOR ALL THE 3 YEARS :")
print("THE SUBJECT WITH MOST 'O' IS: ",n)
print("NO. OF STUDENTS WHO RECEIVED 'O' ARE :",max)

min=500
n=""
for x,y in d1.items():
    if y<min:
        min=y
        n=x
print(" FOR ALL THE 3 YEARS :")
print("THE SUBJECT WITH LEAST 'F' IS: ",n)
print("NO. OF STUDENTS WHO RECEIVED 'F' ARE :",min)


f2.close()
f1.close()
f.close()

