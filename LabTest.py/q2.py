# Write a python program to input a number. Check and display whether it is a Niven
# number or not.
# (Hint : A number is said to be Niven which is divisible by the sum of its digits).
# Example:
# Sample Input : 126
# Sum of its digits = 1 + 2 + 6 = 9 and 126 is divisible by 9.

def Niven_Number(num):
    sum=0
    temp = num
    while num>0:
        rem=num%10
        sum=sum+rem
        num=num//10
       
    if temp%sum==0:
        print("Niven Number")
    else:
        print("Not a Niven Number")

def main():
    num=int(input("Enter a number: "))
    Niven_Number(num)

if __name__ == "__main__":
    main()