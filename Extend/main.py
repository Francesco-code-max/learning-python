numbers = [2, 3, 5, 7, 9]
print("list 1", numbers)

even_numbers = [4, 6, 8, 10]
print("list 2", even_numbers)

numbers.extend(even_numbers)
print("Here is the final output", numbers)