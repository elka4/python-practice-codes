number1= int(input("Enter number1"))
number2= int(input("Enter number2"))

gcd= 1
k = 2

while k <= number1 and k <= number2:
    number1 % k == 0 and number2 % k == 0
    gcd = k

    k += 1

print("Greatest Common Divisor is: ", gcd)



