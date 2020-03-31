def isPrime(name):
    if name <= 1:
        return False
    if name <= 3:
        return True

    if name % 2 == 0 or name % 3 == 0:
        return False

    i = 5
    while i * i <= name:
        if name % i == 0 or name % (i + 2) == 0:
            return False
        i = i + 6

    return True


def printPrime(name):
    count = 0
    for i in range(2, name + 1):
        if isPrime(i):
            count += 1
    print(count)


n = int(input())
printPrime(n)
