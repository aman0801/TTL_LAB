# Write a menu driven python program to input a number and display the new
# number after reversing the digits of the original number. The program also
# displays the absolute difference between the original number and the reversed
# number

def reverse(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev
def main():
    num = int(input("Enter "))
    print("press 1 for reverse ")
    ch = int(input())
    if(ch == 1):
        print("reverse number is: ", reverse(num))
        print("The absolute difference is: ", abs(num - reverse(num)))
main()
