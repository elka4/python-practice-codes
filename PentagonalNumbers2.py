n = 0


def getPentagonalNumber(n):
    for n in range(0, 101):
        print(n * (3 * n - 1) / 2)
        n += 1


def main():
    print(getPentagonalNumber(n))


main()

