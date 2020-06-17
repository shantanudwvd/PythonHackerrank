def solve(s):
    string = ""
    s = s + " "
    i = j = 0
    while i <= len(s) - 1:
        string = ""
        while s[j] != " ":
            if len(s) == j:
                break
            string = string + s[j]
            j += 1
        k = 0
        while k < len(string):
            if k == 0:
                string = string + string[0].upper()
            else:
                string = string + string[k]
            k += 1
        string = string + " "
        j += 1
        i = j
    return string


s = input()
result = solve(s)
print(result)
