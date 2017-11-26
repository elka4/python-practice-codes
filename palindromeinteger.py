def reverse(number):
    return (str(number)[::-1])


def isPalindrome(number):
    return str(number) == reverse(number)


def main():
    number = str(input("Please enter a number"))
    if isPalindrome(number) == True:
        print("Number is palindrome")
    else:
        if isPalindrome(number) == False:
            print("Number is not a palindrome")


main()





