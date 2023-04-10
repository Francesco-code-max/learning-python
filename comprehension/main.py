# fruits = ["Apple", "Mango", "Lemon", "Kiwi", "Pineapple"]
# newList =[]

# for x in fruits:
#     if "a" in x:
#         newList.append(x)

# print(newList)

#THIS IS A SHORTER WAY
# fruits = ["apple", "Mango", "Lemon", "Kiwi", "Pineapple"]
# newList = [ x for x in fruits if "a" in x]
# print(newList)

#TO CHECK IF AN ITEM IN A LIST IS NOT
# fruits = ["apple", "Mango", "Lemon", "Kiwi", "Pineapple"]
# newList = [x for x in fruits if x !="apple"]
# print(newList)

# # Range
# newList = [ x for x in range (10)]
# print(newList)

# Display numbers that are less than 5
newList = [x for x in range (10) if x < 5]
print(newList)


