# check whether an input integer is perfect number or not
num = int(input("Give No"))
rem = 0 
sum = 0
for x in range(1, num):
    rem = num%x
    if(rem == 0):
        sum = sum + x

if(sum == num):
    print("perfect")
else:
    print("Not")