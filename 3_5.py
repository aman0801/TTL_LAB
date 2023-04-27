# WAP in Python to swap the values of two variables by using a suitable user defined function (saySWAP) for it

def swap(a,b):
    return b,a

a = int(input("Enter "))
b = int(input("Enter "))
print("Before ", a, b)
a,b = swap(a,b)
print("After ", a, b)
