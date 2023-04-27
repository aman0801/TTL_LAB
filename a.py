# import sys
# def factor(n):
#     if n==0:
#         return 1
#     x=n*factor(n-1)
#     return x


# def main():
#     n = int(input("Enter a number: "))
#     if(n<=0):
#         print("Invalid input")
#     else:
#         print("Factorial of {} is: ".format(n))
#         print(factor(n))

# if __name__ == "__main__":
#     main()

# a = [1, 2, 3, 4, 5]
# b = [4, 3, 8, 9, 10]
# for i in range(len(a)):
# print(a.count(4))
# a.insert(2, 10)
# print(a)
# a.pop(2)
# print(a)
# # remove specific element
# a.remove(4)
# print(a)
# b.sort()
# print(b)
# make a list

# make a dictoinary
a = {1: "one", 2: "two", 3: "three", 4: "four", 5: "five"}
arr = [1, 2, 3, 4, 5]
d={}
print(*[val for key,val in a.items()])

# for i in a.values():
#     print(i)

# find frequency of each element in a dictionary 
for i in arr:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
print(d)