#Science: calculate energy

amountofWater = input("Enter the amount of water in kilograms")
initialTemp = input("Enter the initial temperature")
finalTemp = input("Enter the final temperature")

energyInJoules= float(amountofWater) * ( float(finalTemp ) - float(initialTemp)) *4184

print ("The energy needed is ", energyInJoules)
