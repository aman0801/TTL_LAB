# Write a program in Python to calculate the power of any 
# number using recursion

def power(n, p):
    if(p!=0):
        return n*power(n, p-1)
    else:
        return 1
    
n = int(input("Enter a number: "))
p = int(input("Enter a number: "))
print("power is: ", power(n, p))