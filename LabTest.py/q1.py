# Write a python program to accept a number and check whether it is a “Spy Number”; or
# not.
# (Hint : A number is a spy if the sum of its digits equals the product of its digits.)
# Example:
# Sample Input : 1124
# Sum of the digits = 1 + 1 + 2 + 4 = 8
# Product of the digits = 1*1*2*4 = 8


def Spy_Number(num):
    sum=0
    product=1
    while num>0:
        rem=num%10
        sum=sum+rem
        product=product*rem
        num=num//10
    if sum==product:
        print("Spy Number")
    else:
        print("Not a Spy Number")

def main():
    num=int(input("Enter a number: "))
    Spy_Number(num)  

if __name__ == "__main__":
    main()
