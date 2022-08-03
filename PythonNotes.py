# print("Pravith")
# 2*3
a = "harry"
b = 6
c = 9.7
d = False
e = None

# Printing the variables
print(a)
print(b)
print(c)
print(d)
print(e)

# Printing the type of variables
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

# Arithmetic Operators
print("The value of 3+4 is ", 3+4)
print("The value of 3-4 is ", 3-4)
print("The value of 3*4 is ", 3*4)
print("The value of 3/4 is ", 3/4)
print("The value of 3%4 is ", 3 % 4)

# Assignment Operators
a = 32
a += 2
a -= 2
a *= 2
a /= 2  # division always results in floating numbers
print(a)

# Comparison Operatos
b = (14 > 7)
print(b)

# Logical Operatorss
bool1 = True
bool2 = False
print("The value of bool1 and bool2 is ", (bool1 and bool2))
print("The value of bool1 or bool2 is ", (bool1 or bool2))
print("The value of not bool2 is ", (not bool2))

# Typecasting
a = "3435"
a = int(a)
print(type(a))

# Taking input (scanning)
print("Enter your name : ")
a = input()
print(a)
a = input("Enter your name: ")
print(a+" Chary")  # Concatenation of two strings

# ------------------------------------- STRINGS -----------------------------------------------

print(a[4])
print(a[0:3])  # Printing from i = 0 to i < 3 ------------ Called Slicing
# Accessing in opposite order is also easy in Python
print(a[-1])
print(a[-4])
print(a[0:])  # Starting from i = 0 to last
print(a[:4])  # Starting from beginning to i = 4
print(a[-4:-1])  # Starting from i = n-4 to i = n-1
a = "PravithIsGreatBoy"
print(a[1:11:3])  # Starting from i = 1; i <=11; i+=3
# a[0] = "b" # Changing the chars is not accepted

# -------------------------------------- STRINGS FUNCTIONS -------------------------------------
story = "Once upon a time there lived a crow"
print(len(story))  # Length of the string
print(story.endswith("ow"))  # The last characters
print(story.count("er"))  # Count the no.of times the substring is repeating
print(story.capitalize())  # Capitalise the first character of the string
print(story.find("time"))  # Finds the position of the substring

# Replace the left substr with the right substr
print(story.replace("lived", "bathinkindhi"))

# ------------------------------------- ESCAPE CHARACTERS ---------------------------------------
story = "Once upon a time\tthere jeevan bithathi ek \' crow.\nlekin mujhe \\ pataa nhi tha"

# ------------------------------------- LIST AND TUPLES -----------------------------------------
a = [1, 2, 3, 4, 5]  # List is almost like an array or a class
print(a)  # Prints the entire list
print(a[3])  # Prints the 4th element
b = [2, "MnC", 45.0]  # Can store any datatype
print(b)
b[1] = 3  # Can change the elements
print(b[0:3])  # Slicing can also be used

# --------------- list functions (methods) -------------- #
a = [1, 2, 67, 85, 3, 5.6]
print(a)
a.reverse()
print(a)
a.sort()
print(a)
a.append(8)
print(a)
a.insert(3, 99)  # adds the second one at the index of first int
print(a)
a.pop()  # normal pop
print(a)
a.pop(3)  # removes the element at the mentioned index
print(a)
a.remove(67)  # removes the element itself
print(a)


# ---------------- tuple --------------- #
t = (1, 6, 5, 7)
print(t)
print(t[2])
# t[0] = 4 # Can't be updated
a = ()  # Empty tuple
a = (4, )  # Needs a comma for singleton tuple
print(a)

# ----------------- tuple funcfunctions (methods)tions ------------ #
print(t.count(1))  # no.of occurences of 1
print(t.index(5))  # the first time 5 is appearing

# ----------------------------------------------- DICTIONARY AND SETS ----------------------------------
# ----------------
# somewhat like classes. It is collection of  key-value pairs
# it is unordered, mutable, indexed, can't contain duplicate keys
# ----------------
myDict = {
    'a': 5,
    'b': "Pravith",
    "c": [3, 2, 5, 1],
    'd': (1, 2, 3, 4),
    "anotherDict": {"e": 5.6}  # dictionary within a dictionary
}
print(myDict)
print(myDict['a'])
print(myDict["b"])
print(myDict['anotherDict'])
print(myDict["anotherDict"]['e'])  # contents of the inner dictionary

# --------------- dictionary functions (methods) -----------#
print(myDict.items())  # prints all the keys and values of the dictionary
print(type(myDict))  # dict is a data type
print(list(myDict.keys()))  # prints all the keys
print(myDict.keys())  # prints the data type and the keys as a list
print(type(myDict.keys()))  # dict_keys is a data type
print(list(myDict.values()))  # prints all the values
print(myDict.values())  # prints the data type and the values as a list
print(type(myDict.values()))  # dict_values is a data type

print(myDict)
newDict = {
    "Pravith": 'Friend',
    "Ranjith": 'Friend'
}

myDict.update(newDict)  # adds the one in the braces to the original dictionary
print(myDict)

myDict.update({'Anil': "Friend"})  # another way of updating the dictionary
print(myDict)

# same as myDict["Pravith"] but gives None if not present without any error as the last one
myDict.get("Pravith")

# --------------- sets -----------#
# --------------
# a collection of non repetitive elements
# unordered, unindexed, no way to change items in the set, no duplicate values
# --------------
mySet = {1, 3, 4, 5, 1}
print(mySet)  # we get {1,3,4,5} printed. Repeated elements are ignored
print(type(mySet))  # <class 'set'>
mySet = {}
print(type(mySet))  # empty set is a dictionary. so <class 'dict'> gets printed
mySet = set()
print(type(mySet))  # syntax to create an empty set

# --------------- sets functions(methods) --------------
mySet.add(6)  # addition of elements
mySet.add("Pravith")  # any data type is accepted
print(mySet)
mySet.add((1, 2, 3))  # tuple is accepted
# mySet.add([1, 2, 3])  # list is not accepted
# mySet.add({1: 2})  # dictionary is not accepted

print(len(mySet))  # prints the length of the set
mySet.remove(6)  # updates and removes 3

print(mySet)
print(mySet.pop())  # pops a random element

mySet.clear()  # clears the entire set (removes all the elements)
mySet.union({1, 2, 3})
mySet.intersection({2, 4, 5, 3})

# ----------------------------------------------- CONDITIONAL EXPRESSIONS ----------------------------------
a = 8
if a < 2:  # bracket is not mandatory
    print("a is less than 2")
elif(a > 10 or a < 20):
    print("a is greater than 10 or less than 20")
else:
    print("I am not responsible for the situation")

# ---------- is and in keyword ----------- #
a = None
print(a is None)  # it's a bool
a = [1, 2, 3]
print(2 in a)  # in is also used in for loop
print(13 in a)

# ----------------------------------------------- LOOPS IN PYTHON ----------------------------------
# ----------------- while loop
i = 9
while i < 10:
    print(i, " is printed")
    i = i+1

fruits = ["Banana", "Apple", "Mango"]
i = 0
while i < len(fruits):
    print(fruits[i])
    i = i + 1

# ----------------- for loop
# a for loop is used to iterate lists, tuples or strings(iterables)
l = [1, 7, 8]
for item in l:
    print(item)

# range function used in for loop
for i in range(1, 10, 2):  # (start, stop, step size) # if only one element is mentioned - it is stop, if only 2 - they are start and stop
    if i == 3:
        continue  # continue
    print(i)
    if i == 7:
        break  # break
else:
    print("Pravith")

# pass - it is a null statement in python. It instructs to do nothing
if 0 <= 5:
    pass


def function1(a, b):  # def is used to define a function
    pass

# ----------------------------------------------- FUNCTIONS AND DEFINITIONS ----------------------------------


def greet(name):
    a = "Hello " + name
    print(a)


greet("Pravith")


# function2
def factorial(a):
    if a == 0 or a == 1:
        return 1
    return a*factorial(a-1)


print(factorial(5))
