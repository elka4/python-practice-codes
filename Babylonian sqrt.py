accuracy = 0.001

def sqrt(n):
    lastGuess = n/2.0

    while True:
        nextGuess = (lastGuess + (n / float(lastGuess))) / 2.0
        if abs(nextGuess - lastGuess) < accuracy:
            break


        lastGuess = nextGuess

    return nextGuess


def main():
    n = int(input("Please enter number: "))
    print(round(sqrt(n),4))

main()