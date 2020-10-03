def digitalRoot(num):
    if num == "0":
        return 0
    elif int(num) > 25:
        ans = int(num) % 25
        if ans == 0:
            return 25
        else:
            return ans


base26 = {
    "a": "0",
    "b": "1",
    "c": "2",
    "d": "3",
    "e": "4",
    "f": "5",
    "g": "6",
    "h": "7",
    "i": "8",
    "j": "9",
    "k": "10",
    "l": "11",
    "m": "12",
    "n": "13",
    "o": "14",
    "p": "15",
    "q": "16",
    "r": "17",
    "s": "18",
    "t": "19",
    "u": "20",
    "v": "21",
    "w": "22",
    "x": "23",
    "y": "24",
    "z": "25"
}
queries = int(input())
for i in range(queries):
    sumOfStr = 0
    size = int(input())
    string = input()
    for i in string:
       sumOfStr += int(base26[i])
    base26Char = digitalRoot(str(sumOfStr))
    for k, v in base26.items():
        if v == str(base26Char):
            print(k)
            break
