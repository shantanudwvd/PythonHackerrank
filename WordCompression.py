from itertools import groupby
word = input()
word_list = list(word)
prev_list = list(word)
k = int(input())
while True:
    groups = groupby(word)
    result = [(label, sum(1 for _ in group)) for label, group in groups]
    ct = 0
    for i in result:
        if i[1] == k:
            for j in range(0, k):
                word_list.remove(i[0])
                ct = 1
        elif ct == 1:
            break
    if word_list == prev_list:
        break
    else:
        prev_list = word_list
        word = ''.join(word_list)
print(''.join(word_list))
