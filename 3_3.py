#  WAP in Python to find out the sum of digits of a number n by suing function.

def sum(n):
    if n==0:
        return 0
        return n%10 + sum(n//10)

n = int(input("Enter "))
print("Sum is: ", sum(n))