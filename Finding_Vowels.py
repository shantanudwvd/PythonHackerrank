from collections import defaultdict


def smallest(s1, s2):
    assert s2 != ''
    d = defaultdict(int)
    nneg = [0]

    def incr(c):
        d[c] += 1
        if d[c] == 0:
            nneg[0] -= 1

    def decr(c):
        if d[c] == 0:
            nneg[0] += 1
        d[c] -= 1

    for c in s2:
        decr(c)
    min_len = len(s1) + 1
    j = 0
    for i in range(len(s1)):
        while nneg[0] > 0:
            if j >= len(s1):
                return min_len
            incr(s1[j])
            j += 1
        min_len = min(min_len, j - i)
        decr(s1[i])
    return min_len


size = int(input())
s1 = input()
s2 = "aeiou"
ans = smallest(s1, s2)
if ans == size + 1:
    print(-1)
else:
    print(ans)
