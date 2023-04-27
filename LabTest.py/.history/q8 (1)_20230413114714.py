# Write a python function passwordGen(), that will validate the string with following
# property
# a. The string should contain at least one Capital letter
# b. The string should contain at least one small letter
# c. The string should contain at least one special symbol
# d. The string should contain at least one digit
# e. The string should contain the user name as substring
# Input : username and password
# Output : Valid or invalid password

def passwordGen():
    username = input("Enter the username: ")
    password = input("Enter the password: ")
    count = 0
    for i in password:
        if i.isupper():
            count += 1
            break
        if(i<='z' and i>='a'):
            count += 1
            break
        if(i<='9' and i>='0'):
            count += 1
            break
        if(i<='@' and i>='!'):
            count += 1
            break
        if username in password:
            count += 1
            break
        if count == 5:
           print("Valid password")
        else:
           print("Invalid password")

def main():
    passwordGen()

if __name__ == "__main__":
    main()