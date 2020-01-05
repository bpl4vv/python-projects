# Take a list, say for example this one:
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# and write a program that prints out all the elements of the list that are less than 5.

# Extras:
# 1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it
# and print out this new list.
# 2. Write this in one line of Python. UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUH HOW TO DO
# 3. Ask the user for a number and return a list that contains only elements from the original list a
# that are smaller than that number given by the user.

def printLess(list):
    for element in list:
        if element < 5:
            print(element)

def extra1printLess(list1):
    result = []
    for element in list1:
        if element < 5:
            result.append(element)
    print(result)

def extra3printLess(list3):
    result = []
    print("Number to print elements less than?")
    cap = int(input())
    for element in list3:
        if element < cap:
            result.append(element)
    print(result)

print("Give me a number.")
num = int(input())
print("Give me", num, "elements.")
List = []
for i in range(num):
    List.append(int(input()))

printLess(List)
extra1printLess(List)
extra3printLess(List)