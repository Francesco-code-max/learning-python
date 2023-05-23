#A program to check if a number is divisible by 7 and a mulitple of 5 from the range of 1500 to 2700
def divisible_and_multiple(number):
    if  number % 7 == 0 and number % 5 == 0:
        return True
    else:
        return False
        
for number in range(1500, 2700):
    if divisible_and_multiple(number):
        print("Here are the numbers: ", number)