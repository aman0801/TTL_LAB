# Write a program in Python to calculate the sum of first n 
# numbers using recursion.

def sum(n):
    if n==0:
        return 0
    x=n+sum(n-1)
    return x

n = int(input("Enter a number: "))
print("sum is: ", sum(n))