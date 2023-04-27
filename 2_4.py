# WAP to calculate the factorial of a given number
num = int(input("Give no"))
ans = 1
for x in range(1, num+1):
    ans = ans*x
    # x = x+1
print("ans is", (ans))