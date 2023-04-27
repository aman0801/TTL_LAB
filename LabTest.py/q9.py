# Write a python program that will remove all digits and special characters from a string
# except integers.

def isSpecialCharacter(char):
    if char in ['@', '#', '$', '%', '&', '*', '!', '?']:
        return False
    return True

def remove_digits_and_special_characters(string):
    new_string = ""
    for i in string:
        if i == " " or isSpecialCharacter(i):
            new_string += i
    return new_string

def main():
    string = input("Enter a string: ")
    print(remove_digits_and_special_characters(string))

if __name__ == "__main__":
    main()