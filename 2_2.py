# write a program to print sum of digits of a number
number = int(input("Enter "))
sum = 0
while number>0:
    sum = sum + number%10
    number = number//10
print(sum)
