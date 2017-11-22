

isLeap = int(input("Please input year"))

if (isLeap % 4 == 0 and isLeap % 100 != 0) or isLeap % 400 == 0:
    print(isLeap, "is a leap year")
else:
    print(isLeap, "is not a leap year")

