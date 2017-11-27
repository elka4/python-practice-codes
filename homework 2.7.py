#Sum the digits in an integer

minutes = input("Enter the number of minutes: ")

year = int(minutes) / 525600
remianMinutes = int(minutes) % 525600
days = int(remianMinutes) / 1440 

print (minutes, "is approximately ", year, "and ", days, " days")
