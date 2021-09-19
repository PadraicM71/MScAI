# Solutions Week 1

# Quiz

######## Remember store a phone number as a string - due to integer removing 0 at start of some numbers! This got yopu in the quiz.

print("Hello World")

name = "Padraic"
print("Hello", name)

# age = input("Enter your age: ")
# print(age)

fullname = "Joe Bloggs"
firstname, lastname = fullname.split()
print(lastname)
print(firstname + lastname)

message = "Hello World"
print(message[6])

######## Remember the string methods return another string based on the origional string!
######## These methods do not change the origional string. You got caught with this in a quiz question!
username = "JoeB"
print(username.lower())
print(username)

firstname = "Colin"
print(firstname[:3])

fullname = "ObiWan KenObi"
print(fullname.title())

# age = float(input("Enter your age: "))
# print(age)

# age = int(input("Enter your age: "))
# print(age)

# hogsheads = float(input('Enter number of hogsheads '))
# print(hogsheads)

# barrels = hogsheads * 2
# print(barrels)

litres = 654.63696
print(f"Equivalent metric volume is {litres:.2f} litres")

from math import pi, sqrt

length=23
gravity=9.8
T = 2*pi*sqrt(length/gravity)
print(T)

time = 23.123456
print(f"The time is {time:.3f} seconds")
print(f"The time is {time:.6} seconds") # me experimenting!


