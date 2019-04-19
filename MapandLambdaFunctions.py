cube = lambda x: x**3


def fibonacci(size):
    fib = []
    if size == 0:
        return fib
    elif size == 1:
        fib.append(0)
        return fib
    else:
        fib.append(0)
        fib.append(1)
        i = 2
        while i < size:
            fib.append(fib[i-1]+fib[i-2])
            i += 1
        return fib


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
