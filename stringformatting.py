def print_formatted(number):
    i = j = 1
    while i <= number:
        octal = oct(j)
        hexadecimal = hex(j)
        binary = bin(j)
        print(f"{j} {octal[2::]} {hexadecimal[2::]} {binary[2::]}")
        i += 1
        j += 1


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
