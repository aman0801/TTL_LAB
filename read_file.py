def readlide_returnList(filename):
	name_list=[]
	file=open(filename,'r')
	for i in file.readlines():
		name_list.append(i.rstrip("\n"))
	return(name_list)

filename1='D:\TTL\student1.csv'
filename2='D:\TTL\student2.csv'

studentlist1=readlide_returnList(filename1)
studentlist2=readlide_returnList(filename2)


# print(studentlist1)
# print(studentlist2)
# Q-1

def printli(list):
	for i in list:
		print(i)
# printli(studentlist1)
# Q-2

studentlist1.sort()
studentlist2.sort()
# printli(studentlist1)
# printli(studentlist2)
# Q-3

# print(studentlist1.count("HIMANSHU"))
# print(studentlist1.count("PRIYANSHU"))
# Q-4

studentlist1.extend(studentlist2)
# printli(studentlist1)
# Q-5

for i in studentlist1:
	if studentlist1.count(i)>1:
		studentlist1.remove(i)
# printli(studentlist1)
d = {}
for i in studentlist1:
    if i[0] in d:
        d[i[0]]+=1
    else:
        d[i[0]]=1
# print(d)
a={}
for i in studentlist2:
    if i in a:
        a[i]+=1
    else:
        a[i]=1

d.update(a)
print(d)
