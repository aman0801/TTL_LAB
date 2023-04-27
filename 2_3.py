# write a program to check wether a number is prime or not in given range
start = int(input("start "))
end = int(input("end "))
for num in range(start, end + 1):
    prime = True
    if num <= 1:
        prime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                prime = False
                break
    if prime:
        print(num, "is a prime number.")
      