# A special two-digit number is such that when the sum of its digits is added to the
# product of its digits, the result is equal to the original two-digit number.
# Example:
# Consider the number 59.
# Sum of digits = 5 + 9 = 14
# Product of digits = 5 * 9 = 45
# Sum of the sum of digits and product of digits = 14 + 45 = 59
# Write a python program to accept a two-digit number. Add the sum of its digits to the
# product of its digits. If the value is equal to the number input, then display the
# message “Special 2 - digit number”; otherwise, display the message “Not a special
# two-digit number”.

def special_two_digit_number(num):
    sum=0
    product=1
    temp = num
    while num>0:
        rem=num%10
        sum=sum+rem
        product=product*rem
        num=num//10
    if sum+product==temp:
     
       print(temp)
       print("Special two-digit number")
    else:
        print("Is not a special two-digit number")

def main():
    num=int(input("Enter a number: "))
    special_two_digit_number(num)

if __name__ == "__main__":
    main()