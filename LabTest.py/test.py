'''
Problem Statement : I have to conduct several classroom activities and tests of the students as
a teacher. I tabulated the scores in different ways. For instance, the marks are tabulated against
the Roll Number in certain cases (File Names: RollNo_Score_Quiz_1.txt and
RollNo_Score_Quiz_2.txt) or against the Name in other cases (File Name: Name_Viva.txt).
Fortunately, I have a single score sheet (File Name: RollNo_Name_Assignment.txt) that has
the Names, Roll Numbers, and corresponding scores of one Assignment. Making the final score
sheet by hand is now exceedingly challenging. I therefore wish to automate the procedure. I
want to keep the file the same and append the other scores to it simply because it already
contains the roll number and name associated with it in the file RollNo_Name_Assignment.txt.
Write a Python programme to read the other files and tabulate the results in accordance with the
RollNo_Name_Assignment.txt file. Add columns for Grades and Email addresses as well. Below
is a list of the grading rules. Add the gmail.com domain to the relevant roll number as your email
ID. The information about the grading scheme and Full Marks of each activity are given below.
'''
def newread():
    lis=[]
    with open('LabTest.py\RollNo_Name_Assignment.txt', 'r') as f:
        data = f.readlines()
        for lin in data[1:]:
            mini=[]
            line = lin.strip().split('\t')

            for i in line:
                mini.append(i)
            lis.append(mini)
    return lis
    
def readfiles(filename):
    dic = {}
    with open(filename, 'r') as f:
        data = f.readlines()
        for lin in data[1:]:
            line = lin.strip().split('\t')
            dic[line[0]]=[]
            for i in line[1:]:
                dic[line[0]].append(i)
            
    return dic

def writefiles(filename, data):
    with open(filename, 'w') as f:
        f.write('RollNo\tName\tEmail\tTotal\tGrade')
        for i in data:
            f.write('\n')
            f.write('\t'.join(data[i]))

        

def main():
    Name_Viva= readfiles('LabTest.py\RollNo_Score_Quiz_1.txt')
    RollNo_Score_Quiz_1 = readfiles('LabTest.py\RollNo_Score_Quiz_1.txt')
    RollNo_Score_Quiz_2 = readfiles('LabTest.py\RollNo_Score_Quiz_2.txt')
    RollNo_Name_Assignment = newread()
    l=50
    total_dic = {}
    for i in RollNo_Name_Assignment:
        mini=[i[0]]
        mini.append(i[1])
        mini.append(i[0]+"@gmail.com")
        total=0
        total+=int(i[2])
        if i[0] in RollNo_Score_Quiz_1.keys():
            total+=int(RollNo_Score_Quiz_1[i[0]][0])
        if i[0] in RollNo_Score_Quiz_2.keys():
            total+=int(RollNo_Score_Quiz_2[i[0]][0])
        if i[1] in Name_Viva.keys():
            total+=int(Name_Viva[i[1]][0])
        mini.append(str(total))
        if(total/l>=0.9):
            mini.append('O')
        elif(total/l>=0.8):
            mini.append('E')
        elif(total/l>=0.7):
            mini.append('A')
        elif(total/l>=0.6):
            mini.append('B')
        elif(total/l>=0.5):
            mini.append('C')
        elif(total/l>=0.4):
            mini.append('D')
        else:
            mini.append('F')
        total_dic[i[0]]=mini
    writefiles('ans.txt',total_dic)
main()
        
        

