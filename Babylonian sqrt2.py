MAXEXECUTIONCOUNT = 2
accuracy = 0.001

def sqrt(n):
    lastGuess = n/2.0


    _executionsLeft = MAXEXECUTIONCOUNT
    while True:

        nextGuess = (lastGuess + (n / float(lastGuess))) / 2.0
        if abs(nextGuess - lastGuess) < accuracy:
            break



        lastGuess = nextGuess

        if _executionsLeft < 1:
            print("The computations exceed the max amount of " + str(MAXEXECUTIONCOUNT) + " operations")
            break
        else:
            _executionsLeft -= 1


    return nextGuess


def main():
    n = int(input("Please enter number: "))
    print(round(sqrt(n),4))

main()