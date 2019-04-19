import textwrap


def wrap(my_string, max_width):
    print(textwrap.fill(my_string,max_width))


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
