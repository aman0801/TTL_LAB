# Write a menu driven program that will read a list and remove the element based on
# a. Element
# b. Element index
# It should prompt for both options. Based on selection the program should again prompt
# for either index or the element.

def removeElement():
    list1=[]
    n=int(input("Enter the number of elements:"))
    for i in range(n):
        list1.append(int(input("Enter the element:")))
    print(list1)
    print("Enter 1 to remove element based on index")
    print("Enter 2 to remove element based on element")
    choice=int(input("Enter your choice:"))
    if choice==1:
        index=int(input("Enter the index of the element to be removed:"))
        list1.pop(index)
    elif choice==2:
        element=int(input("Enter the element to be removed:"))
        list1.remove(element)
    else:
        print("Invalid choice")
    print(list1)

def main():
    removeElement()

if __name__ == "__main__":
    main()