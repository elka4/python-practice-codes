#Check whether a number entered by user is divisible by 2 and 3, 2 or 3 and 2 or 3 but not both.


number = int(input("Enter a number to check divisibility"))

if (number % 2 == 0 and number % 3 == 0):
    print("The number is divisible by 2 and 3")

if (number % 2 == 0 or number % 3 == 0):
    print("The number is divisible by 2 or 3")

if (number % 2 == 0 or number % 3 == 0) and not (number % 2 == 0 and number % 3 == 0):
    print("The number is divisible by 2 or 3 but not both")