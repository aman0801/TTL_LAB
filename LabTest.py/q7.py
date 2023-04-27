# Create a programme that counts the number of times each character appears in a string.
# Input : kndhffihfuifuichfhfehuchurhucghtuhieheichnnhhgjpmofojcewhgghjnnfjpqjrgndjhg

def main():
    string = input("Enter a string: ")
    count = {}
    for i in string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    print(count)

if __name__ == "__main__":
    main()