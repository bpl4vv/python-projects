# Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
# Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

def ListComprehensionsEven(list):
    return [e for e in list if e % 2 == 0]

print("Give me 5 numbers.")
list1 = []
for i in range(5):
    list1.append(int(input()))

print(ListComprehensionsEven(list1))