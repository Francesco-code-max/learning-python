#GETTING THE LENGTH OF THE TUPLE
# fruits = ("apple", "berry", "cherry")
# print(len(fruits))

#GETTING THE TYPE OF THE TUPLE
# fruits = ("apple", "berry", "cherry")
# print(type(fruits))

#THE TUPLE CONSTRACTOR
# fruits = tuple(("apple", "berry", "cherry"))
# print(fruits)

#ACCESSING TUPLES
# fruits = ("apple", "berry", "cherry")
# print(fruits[1])

#NEGATIVE INDEXING
# fruits = ("apple", "berry", "cherry")
# print(fruits[-1])

#RANGE OF INDEXES
# fruits =("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(fruits[2:4])

#RANGE OF NEGATIVE INDEXES
# fruits =("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(fruits[-4:-1])

#CHECK IF AN ITEM EXISTS 
# fruits =("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# if "apple" in fruits:
#     print("Apple is in the fruit lists")

#CHANGING AN ITEM IN A TUPLE LIST
# x = ("apple", "banana","cherry")
# y = list(x)

# y[1] = "kiwi"
# x = tuple(y)

# print(x)

#ADDING AN ITEM TO A TUPLE 
# x = ("apple", "banana","cherry")
# y = ("orange", )
# x += y

# print(x)

#REMOVING AN ITEM IN TUPLE
# x = ("apple", "banana", "cherry", "orange")
# y = list(x)
# y.remove("orange")

# x = tuple(y)
# print(y)

# #PACKING AND UNPACKING 
# x = ("apple", "banana","cherry")
# (Red, Yellow, Black) = x

# print(Red)
# print(Yellow)
# print(Black)

#USING ASTERIKS 
x = ("apple", "banana", "cherry", "strawberry", "raspberry")
(Red, Yellow, *Black) = x
print(Red)
print(Yellow)
print(Black)