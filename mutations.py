def mutate_string(string, position, character):
    s=""
    for i in range(0,position):
        s=s+string[i]
    s=s+character
    for i in range(position+1,len(string)):
        s=s+string[i]
    return s
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)