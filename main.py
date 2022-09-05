import random

# This is a comment
# print("Hello, Bro!")
print("Hello, World!")

if 5 > 2:
    print("Five is greater than two!")  # This is a comment

x = 5
y = "Hello, World!"

print(x)
print(y)

x = str(3)
y = int(3)
z = float(3)

print(x)
print(y)
print(z)

y = "John"
print(type(x))
print(type(y))

x = "John"
print(x)
# double quotes are the same as single quotes:
x = 'John'
print(x)

a = 4
A = "Sally"

print(a)
print(A)
# convert from int to float:
x = float(1)

# convert from float to int:
y = int(2.8)

# convert from int to complex:
z = complex(1)

print(x)
print(y)
print(z)

print(type(x))
print(type(y))
print(type(z))

print(random.randrange(1, 10))

a = "Hello, World!"
print(a[1])

for x in "banana":
    print(x)

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")
print(10 > 9)
print(10 == 9)
print(10 < 9)
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
print(bool("Hello"))
print(bool(15))
x = "Hello"
y = 15

print(bool(x))
print(bool(y))
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class MyClass:
    def __len__(self):
        return 0


myObj = MyClass()
print(bool(myObj))


def myfunction():
    return True


print(myfunction())

if myfunction():
    print("YES!")
else:
    print("NO!")
x = 200
print(isinstance(x, int))

print(10 + 5)

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)

thisTuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thisTuple)

thisSet = {"apple", "banana", "cherry", "apple"}

print(thisSet)

thisDict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print(thisDict)

i = 1
while i < 6:
    print(i)
    i += 1

x = lambda a, b: a * b
print(x(5, 6))

try:
    print(demoException)
except:
    print("An exception occurred")

username = input("Enter username:")
print("Username is: " + username)

price = 49
txt = "The price is {} dollars"
print(txt.format(price))
