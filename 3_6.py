# calculate GCD

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("GCD is: ", gcd(a, b))