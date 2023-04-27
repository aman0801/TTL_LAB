# Write a python program to accept a number from the user and check whether it is a
# Prime number or an Automorphic number.
# Hint :
# (a) Prime number: (A number is said to be prime, if it is only divisible by 1 and
# itself)
# Example: 3,5,7,11
# (b) Automorphic number: (Automorphic number is the number which is contained

# in the last digit(s) of its square.)
# Example: 25 is an Automorphic number as its square is 625 and 25 is present as the
# last two digits.

def Automorphic_Number(num):
    square = num*num
    temp = num
    counter=0
    while num>0:
        rem=num%10
        if rem==square%10:
            
            pass
        else:
            counter=1
            break
        num=num//10
        square=square//10
    if counter==0:
        print("Automorphic Number")
    else:
        print("Not a Automorphic Number")

def prime_number(num):
    count=0
    for i in range(1,num+1):
        if num%i==0:
            count=count+1
    if count==2:
        print("Prime Number")
    else:
        print("Not a Prime Number")

def main():
    num=int(input("Enter a number: "))
    prime_number(num)
    Automorphic_Number(num)

if __name__ == "__main__":
    main()