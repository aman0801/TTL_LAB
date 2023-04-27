# Write a program in Python to print first 50 natural 
# numbers using recursion

def nat(n):
    if n>0:
        nat(n-1)
        print(n)

n = int(input("Enter a number: "))
nat(n)
