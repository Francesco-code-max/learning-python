#PYTHON SETS 
# fruits = {"apple", "cherry", "Berry"}
# print(fruits)

#DUPLICATING SETS 
# fruits = {"apple", "cherry", "Berry", "apple"}
# print(fruits)
#IT WILL BE READ AS A DUPLICATE

#GETTING THE LENGTH OF A SET 
# fruits = {"apple", "cherry", "Berry"}
# print(len(fruits))

# #GETTING TYPE OF SET
# fruits = {"apple", "cherry", "Berry"}
# print(type(fruits))

# USING THE SET CONSTRUCTOR
# fruits = set(("apple", "cherry", "berry"))
# print(fruits)

#ACCESSING SET
# fruits = {"apple", "cherry", "Berry"}
# for x in fruits:
#     print(x)

# fruits = {"apple", "cherry", "Berry"}

# print("apple" in fruits)

# fruits = {"apple", "cherry", "Berry"}

# print("banana" in fruits)

#ADDING A NEW ITEM TO A SET
# fruits = {"apple", "cherry", "Berry"}
# fruits.add("orange")
# print(fruits) 

#UPDATING A SET USING UPDATE()
# fruits = {"apple", "cherry", "Berry"}
# tropical = {"banana", "mango", "grapes"}
# fruits.update(tropical)
# print(fruits)

#REMOVING AN ITEM IN A SET
# fruits = {"apple", "cherry", "Berry"}
# fruits.remove("apple")
# print(fruits)

# fruits = {"apple", "cherry", "Berry"}
# fruits.discard("apple")
# print(fruits)

#REMOVING A RANDOM ITEM ON A SET
# fruits = {"apple", "cherry", "Berry"}
# x = fruits.pop()

# print(x)

# print(fruits)

# # CLEARING ITEMS
# fruits = {"apple", "cherry", "Berry"}
# fruits.clear()
# print(fruits)

# DELETING THE SET COMPLETELY
# fruits = {"apple", "cherry", "Berry"}
# del fruits
# print(fruits)

# JOINING SETS 
#USING UNION
# fruits = {"apple", "cherry", "Berry"}
# tropical = {"banana", "mango", "grapes"}
# set3 = fruits.union(tropical)

# print(set3)

# USING UPDATE
# fruits = {"apple", "cherry", "Berry"}
# tropical = {"banana", "mango", "grapes"}
# fruits.update(tropical)

# print(fruits)

#KEEPING ONLY THE DUPLICATES
# fruits = {"apple", "cherry", "Berry"}
# tropical = {"banana", "mango", "grapes","apple"}
# fruits.intersection_update(tropical)

# print(fruits)
# x = {"apple", "cherry", "Berry"}
# y = {"banana", "mango", "grapes","apple"}

# z = x.intersection(y)

# print(z)

# KEEPING ALL BUT THE DUPLICATES
x = {"apple", "cherry", "Berry"}
y = {"banana", "mango", "grapes","apple"}

x.symmetric_difference_update(y)
 
print(x)

