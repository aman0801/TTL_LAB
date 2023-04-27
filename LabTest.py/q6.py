# Two files are given, one containing Roll No and Score (“RollNo_Score.txt”) and another
# containing Roll No and Name (RollNo_Name.txt). Write a python program to obtain a
# student list with corresponding Score. The format should be Roll No, Name and Score.
# The new list of students should follow the same order of name as in RollNo_Name.txt
# file.

def readRollandName():
    file = open("lab_exam/RollNo_Name.txt", "r")
    dic={}
    for line in file.readlines()[1:]:
        line=line.strip('\t')
        line=line.split()
        dic[line[0]]=line[1]
    file.close()
    return dic
def readScore():
    file = open("lab_exam/RollNo_Score.txt", "r")
    dic={}
    for line in file.readlines()[1:]:
        line=line.strip('\t')
        line=line.split()
        dic[line[0]]=line[1]
    file.close()
    return dic
def main():
    rollname=readRollandName()
    score=readScore()
    lis=[]
    for roll in rollname.keys():
        if roll in score.keys():
            lis.append([roll,rollname[roll],score[roll]])
    
    def main():
        rollname=readRollandName()
        score=readScore()
        lis=[]
        for roll in rollname.keys():
            if roll in score.keys():
                lis.append([roll,rollname[roll],score[roll]])
        for i in lis:
            print(i)

if __name__ == "__main__":
    main()