# Write a recursive python program to calculate and display the factorial of a
# number.

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
def main():
    num = int(input("Ente "))
    print("factorial is: ", factorial(num))
main()
