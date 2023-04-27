#  Write a program in Python to calculate the factorial of n 
# numbers using recursion
def fact(n):
    if n==0:
        return 1
    x=n*fact(n-1)
    return x

n = int(input("Enter a number: "))
print("sum is: ", fact(n))