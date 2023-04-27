#  WAP in Python to find the factorial of a number n by using a suitable user defined function (say fact) for it.

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)

n = int(input("Enter "))
print("Factorial is: ", fact(n))