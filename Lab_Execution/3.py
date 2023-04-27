#  Write a menu driven Python program to accept a number from the user and
# check whether it is a Palindrome or a Perfect number.
# (a) Palindrome number: (A number is a Palindrome which when read in reverse
# order is same as in the right order)
# Example: 11, 101, 151 etc.
# (b) Perfect number: (A number is called Perfect if it is equal to the sum of its
# factors other than the number itself.)
# Example: 6 = 1 + 2 + 3

def reverse(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev
def isPalindrome(num):
    if num == reverse(num):
        return True
    else:
        return False
def isPerfect(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False
def main():
    num = int(input("Enter "))
    print("1 for palindrome ")
    print("2 for perfect ")
    ch = int(input())
    if(ch == 1):
        if isPalindrome(num):
            print("Palindrome")
        else:
            print("Not Palindrome")
    elif(ch == 2):
        if isPerfect(num):
            print("Perfect")
        else:
            print("Not Perfect")
    else:
        print("Invalid choice")
main()
